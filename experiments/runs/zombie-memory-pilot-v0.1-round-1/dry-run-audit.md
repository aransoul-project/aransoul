# Zombie Memory Pilot v0.1 Round 1 Dry-Run Audit

Status: configuration validated; no empirical model run started.

- Runner: `experiments/runs/zombie-memory-pilot-v0.1-round-1/runner.py`
- Configuration: `experiments/runs/zombie-memory-pilot-v0.1-round-1/config.json`
- Provider/API: OpenAI Responses API
- Model: `gpt-4.1-mini-2025-04-14`
- Sampling: temperature `0`, top_p `1`
- Requests: 40 independent requests (10 cases x 4 conditions), with no shared conversation history
- Retry policy: no retries (`retry_count: 0`); parse failures are retained in the response log
- Model-facing inputs: frozen `generated/plain.json`, `timestamp.json`, `status.json`, and `ttea.json` only
- Dry-run manifests: `outputs/dry-run/configuration-validation-001/manifest.json` and the pre-push rerun at `outputs/dry-run/pre-push-validation-002/manifest.json`
- Dry-run response-format validation: each dry-run wrote 40 records; the pre-push rerun parsed all 40 with 0 parse failures
- API calls made: 0
- Scoring started: no
- Expected estimated cost: USD 0.008881
- Maximum configured-output estimate: USD 0.021169
- Live-run guard: live mode requires the explicit `--confirm-live` flag and `OPENAI_API_KEY`
- Frozen instrument check: no changes under `benchmarks/zombie-memory/pilot-v0.1/`

This audit records runner and artifact-format readiness only. It is not an empirical result and does not change the frozen pilot's research status.
