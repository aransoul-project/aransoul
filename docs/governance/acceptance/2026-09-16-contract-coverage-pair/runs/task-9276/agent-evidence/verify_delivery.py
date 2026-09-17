import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
evidence = root / ('verification-evidence-' + datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
evidence.mkdir()
required = ['research/README.md', 'research/context-governance/README.md']
contract_bytes = (root / 'contract.json').read_bytes()
contract = json.loads(contract_bytes)
ledger = {
    'source': 'Current user request: confirm both research/README.md and research/context-governance/README.md in aransoul-project/aransoul against the fixed local contract.json; do not modify contract, original task, or remote content.',
    'requirements': [
        {'id': 'R1', 'requirement': 'Research index delivery verification', 'path': required[0], 'method': 'Fixed-contract remote regular-file byte check'},
        {'id': 'R2', 'requirement': 'Research summary delivery verification', 'path': required[1], 'method': 'Fixed-contract remote regular-file byte check', 'unresolved': 'Required path absent from fixed contract'},
    ],
    'required_paths': required,
    'contract_paths': list(contract['files']),
    'missing_from_contract': sorted(set(required) - set(contract['files'])),
    'untraced_contract_paths': sorted(set(contract['files']) - set(required)),
    'coverage_pass': set(required) == set(contract['files']),
    'constraint': 'Read-only remote verification; no publication or contract amendment authorized.',
}
(evidence / 'coverage.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding='utf-8')
local = {path: hashlib.sha256((root / path).read_bytes()).hexdigest() for path in required}
(evidence / 'local-hashes.json').write_text(json.dumps({'scope': 'Local bytes only; not remote verification', 'files': local, 'contract_sha256': hashlib.sha256(contract_bytes).hexdigest()}, indent=2), encoding='utf-8')
env = {k: v for k, v in os.environ.items() if not k.upper().startswith(('GIT_', 'GCM_'))}
temp = evidence / 'tmp'
temp.mkdir()
env.update({
    'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': 'NUL',
    'GIT_TERMINAL_PROMPT': '0', 'GIT_ASKPASS': '',
    'GIT_CONFIG_COUNT': '4',
    'GIT_CONFIG_KEY_0': 'http.sslBackend', 'GIT_CONFIG_VALUE_0': 'openssl',
    'GIT_CONFIG_KEY_1': 'http.sslVerify', 'GIT_CONFIG_VALUE_1': 'true',
    'GIT_CONFIG_KEY_2': 'credential.helper', 'GIT_CONFIG_VALUE_2': '',
    'GIT_CONFIG_KEY_3': 'init.templateDir', 'GIT_CONFIG_VALUE_3': str(temp),
    'TEMP': str(temp), 'TMP': str(temp), 'TMPDIR': str(temp),
    'PYTHONUTF8': '1',
})
command = [sys.executable, 'tools/document-completion/check.py', 'contract.json', '--completion']
result = subprocess.run(command, cwd=root, env=env, capture_output=True)
(evidence / 'checker.stdout.json').write_bytes(result.stdout)
(evidence / 'checker.stderr.txt').write_bytes(result.stderr)
report = None
try:
    report = json.loads(result.stdout)
except (ValueError, UnicodeError):
    pass
receipt = report.get('completion') if isinstance(report, dict) else None
valid = bool(result.returncode == 0 and report and report.get('status') == 'PASS' and receipt
    and receipt.get('repository') == contract['repository']
    and receipt.get('branch') == contract['branch']
    and receipt.get('commit') == contract['commit']
    and sorted(receipt.get('paths', [])) == sorted(contract['files'])
    and receipt.get('checked_at') == report.get('checked_at')
    and report.get('observed_commit') == contract['commit'])
summary = {'command': command, 'exit_code': result.returncode, 'current_receipt_matches_contract': valid,
    'coverage_pass': ledger['coverage_pass'], 'whole_task_verified': valid and ledger['coverage_pass'],
    'contract_unchanged': (root / 'contract.json').read_bytes() == contract_bytes}
(evidence / 'execution.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
print(str(evidence))
print(json.dumps(summary, ensure_ascii=False, indent=2))
print(result.stdout.decode('utf-8', errors='replace'))
