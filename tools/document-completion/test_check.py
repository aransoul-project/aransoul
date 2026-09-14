import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import subprocess
import check


class CompletionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        check.git(self.root, 'init', '--quiet')
        check.git(self.root, 'config', 'user.email', 'test@example.invalid')
        check.git(self.root, 'config', 'user.name', 'Fixture')
        (self.root / 'note.md').write_bytes(b'approved\n')
        (self.root / 'link.md').symlink_to('note.md')
        check.git(self.root, 'add', '.')
        check.git(self.root, 'commit', '--quiet', '-m', 'fixture')
        sha = check.git(self.root, 'rev-parse', 'HEAD').decode().strip()
        (self.root / '.git' / 'FETCH_HEAD').write_text(sha + '\n')
        self.contract = dict(repository='example/repo', branch='main', commit=sha,
                             files={'note.md': hashlib.sha256(b'approved\n').hexdigest()})

    def test_success(self):
        self.assertEqual(check.inspect(self.root, self.contract)['status'], 'PASS')

    def test_wrong_version_even_with_same_bytes(self):
        self.contract['commit'] = '0' * 40
        self.assertEqual(check.inspect(self.root, self.contract)['reason'], 'VERSION_MISMATCH')

    def test_draft_only_does_not_count(self):
        (self.root / 'draft.md').write_text('approved\n')
        self.contract['files'] = {'draft.md': self.contract['files']['note.md']}
        self.assertEqual(check.inspect(self.root, self.contract)['files'][0]['status'], 'MISSING')

    def test_content_mismatch(self):
        self.contract['files']['note.md'] = hashlib.sha256(b'changed\n').hexdigest()
        self.assertEqual(check.inspect(self.root, self.contract)['files'][0]['status'], 'CONTENT_MISMATCH')

    def test_symlink_is_not_document(self):
        self.contract['files'] = {'link.md': hashlib.sha256(b'note.md').hexdigest()}
        self.assertEqual(check.inspect(self.root, self.contract)['files'][0]['status'], 'NOT_REGULAR_FILE')

    def test_all_files_required(self):
        self.contract['files']['missing.md'] = '0' * 64
        self.assertEqual(check.inspect(self.root, self.contract)['status'], 'FAIL')

    def test_worktree_cannot_override_readback(self):
        (self.root / 'note.md').write_text('modified locally')
        self.assertEqual(check.inspect(self.root, self.contract)['status'], 'PASS')

    def test_invalid_contracts(self):
        for field, value in [('files', {}), ('commit', 'HEAD'), ('branch', '-bad'),
                             ('repository', 'https://other/repo'), ('files', {'../x': '0'*64})]:
            with self.subTest(field=field), self.assertRaises((ValueError, subprocess.SubprocessError)):
                check.validate(dict(self.contract, **{field: value}))

    def test_cli_connection_failure_is_unverified(self):
        contract_file = self.root / 'contract.json'
        import json
        contract_file.write_text(json.dumps(self.contract))
        with patch('sys.argv', ['check.py', str(contract_file)]), \
             patch('check.verify', side_effect=subprocess.TimeoutExpired('git', 60)), \
             patch('builtins.print') as output:
            self.assertEqual(check.main(), 2)
            self.assertEqual(json.loads(output.call_args.args[0])['status'], 'UNVERIFIED')


if __name__ == '__main__':
    unittest.main()
