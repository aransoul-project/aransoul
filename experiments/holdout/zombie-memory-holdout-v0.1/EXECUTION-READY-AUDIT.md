# Zombie Memory Holdout v0.1 — Execution-Ready Freeze Audit

Status: **PASS — execution payload frozen, live execution not yet authorized**

Audited execution payload commit: `878b21f62faa9d999793b731198caac88a97bf62`.
Construction payload commit: `b33adb63a71ae34b90429d556a82eeee920b6b65`.

## Frozen instrument checks

- 24 accepted holdout cases / 6 families.
- Four model-facing conditions: `plain`, `timestamp`, `status`, `ttea`.
- 24 prompts per condition; 96 unique `(case_id, condition)` pairs per replication.
- Accepted-version routing is fixed by `FREEZE-MANIFEST.json`.
- Candidate/gold/render/scorer construction payload was not modified during prompt generation or dry validation.

## Prompt integrity

SHA-256 values frozen in `execution-config.prereg.json`:

- plain: `f3851670b76982663b74aa32d86f8826fe6d4d13d5416d9fb0a7db248d9d7dca`
- timestamp: `b5c845229d3444c368398b97c317b055bd5f37da0ec3d83b8e6ce1f479c0bb09`
- status: `8622a5cb4b008bc0e2b298c8ee4b67a30bee5ca7794cc3f4d6ce626f9171054c`
- ttea: `127a08c37ab3e6d43aee7cf4c792a949a6fd720e6872842ac0f02ea767bd11b8`

Deterministic regeneration audit: PASS (`prompt_generator.py --check`).

## Runner / response contract

- model snapshot: `gpt-4.1-mini-2025-04-14`
- provider/API: OpenAI Responses API
- temperature: 0
- top_p: 1
- max_output_tokens: 256
- store: false
- timeout: 120 seconds
- application retry count: 0
- seed: none
- response schema does not use the previously rejected `uniqueItems` keyword; authority-ID uniqueness is validated in application code.
- request order is case-major, then fixed condition order `plain`, `timestamp`, `status`, `ttea`.

## Replication policy

- planned complete replications: 3
- requests per replication: 96
- planned substantive requests: 288
- individual/selective retry: prohibited
- any transport/provider request failure renders the complete replication technical-invalid and stops the run; replacement requires separate review before authorization.

## Dry-run evidence

`DRY-RUN-AUDIT.md` records:

- pytest: 9 passed
- deterministic generator check: PASS
- 96/96 dry-run request records
- 96 parsed responses
- 0 parse failures
- 0 request failures
- all attempts = 1
- unique complete case/condition coverage
- expected first/final ordering
- `api_called=false`
- scoring not started

Dry-run output: `outputs/replication-1/dry-run/execution-ready-validation/`.

## Inspection/scoring boundary

For a live replication, raw outputs must first pass the preregistered raw-data integrity gate. Only then may the frozen scorer be run. Aggregate primary metrics for all four conditions are recorded before individual failure inspection. Primary scoring rules, gold labels, prompts, and cases must not change after live output exists.

## Authorization boundary

This audit freezes the executable research instrument but **does not itself authorize a live API run**. The frozen config remains `execution_authorized=false` at audit time. A live run requires an explicit subsequent authorization step and must use the exact frozen execution payload without modifying prompts, hashes, cases, gold, scorer, model snapshot, sampling settings, request ordering, or retry policy.

No holdout target-model API request had been made when this audit was written.
