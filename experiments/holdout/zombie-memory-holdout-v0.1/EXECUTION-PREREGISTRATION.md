# Zombie Memory Holdout v0.1 — Blind Execution Preregistration

Status: **execution design only; NO API CALLS AUTHORIZED YET**

Construction instrument source: `zombie-memory-holdout-v0.1-frozen`.
Construction payload commit recorded in `FREEZE-MANIFEST.json`: `b33adb63a71ae34b90429d556a82eeee920b6b65`.

## 1. Purpose

This protocol fixes how the frozen 24-case holdout will be executed before any holdout model output is observed. It must not modify case content, gold labels, rendering semantics, or primary scoring rules.

The primary empirical question is whether the Zombie Memory behavioral signal generalizes to the independently constructed holdout set. The experiment is not optimized to make T/T/E/A, Timestamp, Status, or Plain win.

## 2. Model and provider

Primary provider: OpenAI Responses API.
Primary model snapshot: `gpt-4.1-mini-2025-04-14`.

Reason: this is the same dated model snapshot used in the preregistered Round 2 replication and therefore maximizes comparability to the existing empirical archive.

If the provider no longer accepts this exact model snapshot at execution time, do NOT silently substitute another model. Record the attempted run as technical-invalid / execution-blocked before any substantive response is obtained, preserve the failure artifact, and require a separately preregistered protocol amendment before using a replacement model.

## 3. Conditions and cases

Conditions are fixed as:

1. `plain`
2. `timestamp`
3. `status`
4. `ttea`

Cases: 24 per condition, stable IDs `ZH-01` through `ZH-24`.

Each complete replication therefore contains 96 independent requests.

No conversation history, shared thread state, previous answer, gold label, scorer output, or other case output may be included in a request.

## 4. Replications

Planned complete replications: **3**.

Total planned substantive requests: **288** (96 × 3).

Rationale: Round 2 also used three same-model replications. Even with deterministic sampling settings, provider/runtime variation can occur; three complete replications permit a stability check without treating repeated measurements as independent cases.

The 24 holdout cases remain the independent case set. Replications are repeated measurements, not additional independent cases.

## 5. Sampling and request parameters

Freeze the following settings for all requests:

- `temperature`: 0
- `top_p`: 1
- `max_output_tokens`: 256
- `store`: false
- request timeout: 120 seconds
- application retry count: 0

Do not add an API `seed` unless the exact dated model/API combination supports it and a protocol amendment is frozen before execution. Absence of a seed is part of this preregistration.

## 6. Model-facing prompt generation

Before execution, generate exactly four model-facing condition files from the frozen construction payload, one file per condition, each containing the same 24 semantic cases.

The final execution-ready freeze must record SHA-256 hashes for all four generated condition files and the prompt-generation code/configuration.

Prompt generation must be deterministic. Re-running generation from the same frozen payload must produce byte-identical output.

Any mismatch between regenerated hashes and the frozen hashes is an execution-blocking integrity failure.

## 7. Request ordering

Within each replication, use one fixed deterministic interleaving order generated before execution and recorded in the execution config.

Required ordering rule:

- iterate case IDs `ZH-01` through `ZH-24`;
- for each case, issue conditions in the fixed order `plain`, `timestamp`, `status`, `ttea`.

This yields 96 requests per replication and prevents condition blocks from being separated by long provider-time intervals.

The same ordering is used for all three replications.

## 8. No-retry rule

No individual case or individual request may be selectively retried after a transport/provider/parse failure.

If any request in a replication fails before a valid model completion is obtained, that entire replication is marked **technical-invalid** for substantive scoring.

The incomplete replication and all raw request/response/error artifacts must be preserved permanently.

A replacement replication may be started only from request 1 of the full 96-request sequence, using the same frozen protocol. It is a complete-run replacement, not a case-level retry.

Maximum replacement attempts are not automatically authorized by this protocol. After a technical-invalid replication, stop and review the preserved failure artifact before authorizing a complete replacement run.

## 9. Parsing failures

A provider-successful completion that cannot be parsed into the frozen response schema is a substantive model/output-format failure unless the parser itself is proven defective without inspecting or changing case semantics.

Parser defects discovered before any holdout output may be repaired and re-frozen. After output exists, parser changes require an explicit amendment and must not selectively rescue individual answers.

## 10. Raw-data integrity gate

After each replication, before scoring:

1. verify exactly 96 request-attempt records exist;
2. verify each expected `(case_id, condition)` appears exactly once;
3. verify the model snapshot and request parameters match the frozen config;
4. verify prompt hashes match the execution-ready freeze;
5. verify no selective retry occurred;
6. verify response/error records are append-only and complete;
7. classify the entire replication as valid or technical-invalid.

No primary or secondary score may be computed before this gate passes.

## 11. Scoring gate

For a valid replication, score using only the frozen holdout scorer and gold labels.

Primary metrics per condition:

- current-answer accuracy;
- historical-recall accuracy;
- Authority exact-set accuracy;
- stale-authority error count;
- false-discard case count.

The exact-set Authority metric remains primary and may not be weakened after results are seen.

The preregistered Authority taxonomy may be reported only as a secondary diagnostic and may not replace primary scores.

## 12. Inspection order

To reduce post-hoc interpretation pressure:

1. preserve raw outputs;
2. pass/fail the raw-data integrity gate;
3. run the frozen scorer;
4. record complete aggregate metrics for all four conditions;
5. only then inspect per-case failures and secondary Authority categories.

Do not inspect individual case answers during a live replication unless required to diagnose a transport/provider failure. Such diagnosis must not be used to alter subsequent prompts or case content.

## 13. Stop conditions

Immediately stop further model requests if any of the following occurs:

- frozen prompt hash mismatch;
- wrong model snapshot or request parameters;
- accidental case/gold leakage;
- runner begins selective retries;
- output path would overwrite a prior replication;
- construction payload or scorer differs from the frozen reference;
- provider rejects the exact model snapshot before substantive responses are obtained.

Preserve all artifacts generated before the stop.

## 14. Interpretation boundary

A successful holdout would strengthen evidence that the observed Zombie Memory behavior generalizes beyond the original Pilot cases for the tested model and protocol. It would not validate the full AranSoul architecture, consciousness, persistent identity, or a general mechanistic theory of memory.

A null, mixed, or negative result is valid evidence and must not be repaired away by changing cases or scoring after inspection.

## 15. Current gate

**STOP — preregistration only.**

This document does not yet authorize API execution.

Before the first request, the project must still:

1. generate the four final model-facing condition files from the frozen construction payload;
2. record their SHA-256 hashes;
3. create and test the deterministic runner in dry-run mode only;
4. create the final execution config and output directory contract;
5. perform an execution-ready freeze audit;
6. explicitly authorize the first blind run only after that audit passes.
