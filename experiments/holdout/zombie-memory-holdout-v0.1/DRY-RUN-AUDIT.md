# Zombie Memory Holdout v0.1 Dry-Run Audit

Status: **96-request dry-run validated; no API or live model request sent**

Configuration gate:

- `execution_authorized`: `false`
- all four preregistered `prompt_sha256` values are non-null and match the
  generated prompt hashes

Offline validation:

- pytest command: `python -m pytest experiments/holdout/zombie-memory-holdout-v0.1/test_prompt_generator.py experiments/holdout/zombie-memory-holdout-v0.1/test_runner.py`
- pytest result: `9 passed`
- generator check: `python experiments/holdout/zombie-memory-holdout-v0.1/prompt_generator.py --check`
- generator check result: `status: ok`; deterministic generated files match

Dry-run:

- command: `python experiments/holdout/zombie-memory-holdout-v0.1/runner.py --replication replication-1 --mode dry-run --run-id execution-ready-validation`
- output path: `outputs/replication-1/dry-run/execution-ready-validation/`
- manifest mode/status: `dry-run` / `dry_run_validated`
- API calls: `0` (`api_called: false`)
- expected/recorded requests: `96` / `96`
- parsed records: `96`
- parse failures: `0`
- request failures: `0`
- attempts: every record has `attempt: 1`
- pair coverage: every `(case_id, condition)` occurs exactly once
- ordering: `ZH-01/plain`, `ZH-01/timestamp`, `ZH-01/status`,
  `ZH-01/ttea`, continuing case-major through final record `ZH-24/ttea`
- response integrity: all records are `mode: dry-run`; no provider-shaped live
  response identifiers, timestamps, usage, or provider errors are present

Prompt SHA-256:

- plain: `f3851670b76982663b74aa32d86f8826fe6d4d13d5416d9fb0a7db248d9d7dca`
- timestamp: `b5c845229d3444c368398b97c317b055bd5f37da0ec3d83b8e6ce1f479c0bb09`
- status: `8622a5cb4b008bc0e2b298c8ee4b67a30bee5ca7794cc3f4d6ce626f9171054c`
- ttea: `127a08c37ab3e6d43aee7cf4c792a949a6fd720e6872842ac0f02ea767bd11b8`

No candidate, gold, render-review, scorer, freeze manifest, generated prompt,
or prompt-hash file was modified by this validation.
