import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid

root = Path.cwd()
out = root / ('verification-evidence-' + uuid.uuid4().hex)
out.mkdir()
temp = out / 'tmp'
temp.mkdir()
paths = ['research/README.md', 'research/context-governance/README.md']
protected = ['contract.json', 'task.txt', 'AGENTS.md',
             'docs/governance/document-completion-workflow.md',
             'docs/governance/document-completion-coverage.md',
             'tools/document-completion/check.py', *paths]
def hashes():
    return {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in protected}
before = hashes()
contract = json.loads((root / 'contract.json').read_text(encoding='utf-8'))
ledger = {
    'source': 'task.txt', 'source_sha256': before['task.txt'],
    'contract': contract, 'contract_sha256': before['contract.json'],
    'requirements': [
        {'id': 'R1', 'requirement': 'Verify research index at fixed destination/version', 'paths': [paths[0]], 'method': 'remote regular-file SHA-256 and strict branch commit check'},
        {'id': 'R2', 'requirement': 'Verify research summary at fixed destination/version', 'paths': [paths[1]], 'method': 'remote regular-file SHA-256 and strict branch commit check'},
        {'id': 'R3', 'requirement': 'Preserve fixed contract, original task and remote; limit access; report in Traditional Chinese', 'paths': [], 'method': 'local before/after hashes and read-only checker execution; final report'},
    ],
    'missing_contract_paths': sorted(set(paths) - set(contract['files'])),
    'untraced_contract_paths': sorted(set(contract['files']) - set(paths)),
    'local_file_hashes': {p: before[p] for p in paths},
    'local_hashes_match_contract': all(before[p] == contract['files'][p] for p in paths),
    'content_review': 'Index links the requested research summary. Summary separates study versions and retains evidence limitations, Candidate EREQ and paused AGBench. No independent experiment validation is claimed.',
    'before_hashes': before,
}
(out / 'preflight.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding='utf-8')
env = {k: v for k, v in os.environ.items() if k.upper() in {'SYSTEMROOT', 'WINDIR', 'PATH', 'PATHEXT', 'COMSPEC'}}
env.update({
    'TEMP': str(temp), 'TMP': str(temp), 'CURL_HOME': str(temp),
    'XDG_CONFIG_HOME': str(temp), 'GIT_CONFIG_NOSYSTEM': '1',
    'GIT_CONFIG_SYSTEM': 'NUL', 'GIT_CONFIG_GLOBAL': 'NUL',
    'GIT_TERMINAL_PROMPT': '0', 'GCM_INTERACTIVE': 'Never',
    'GIT_CONFIG_COUNT': '4',
    'GIT_CONFIG_KEY_0': 'http.sslBackend', 'GIT_CONFIG_VALUE_0': 'openssl',
    'GIT_CONFIG_KEY_1': 'http.sslVerify', 'GIT_CONFIG_VALUE_1': 'true',
    'GIT_CONFIG_KEY_2': 'credential.helper', 'GIT_CONFIG_VALUE_2': '',
    'GIT_CONFIG_KEY_3': 'core.askPass', 'GIT_CONFIG_VALUE_3': '',
})
command = [sys.executable, 'tools/document-completion/check.py', 'contract.json', '--completion']
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
run = subprocess.run(command, cwd=root, env=env, capture_output=True)
(out / 'checker.stdout.json').write_bytes(run.stdout)
(out / 'checker.stderr.txt').write_bytes(run.stderr)
try:
    report = json.loads(run.stdout)
except (ValueError, UnicodeError):
    report = {}
receipt = report.get('completion')
valid = bool(run.returncode == 0 and report.get('status') == 'PASS' and receipt
             and receipt.get('repository') == contract['repository']
             and receipt.get('branch') == contract['branch']
             and receipt.get('commit') == contract['commit']
             and sorted(receipt.get('paths', [])) == sorted(contract['files'])
             and receipt.get('checked_at') == report.get('checked_at')
             and report.get('checked_at', '') >= started)
record = {'command': command, 'started_at': started, 'exit_code': run.returncode,
          'report': report, 'valid_current_receipt': valid,
          'protected_files_unchanged': hashes() == before,
          'evidence_directory': str(out)}
(out / 'execution.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2))
