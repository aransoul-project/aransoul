# Validation Results

Prepared for the GitHub-safe development research snapshot.

## Corrective offline validation

Command: `python validators/validate_snapshot.py --self-test`

- PASS: `candidate-inventory.v0.2.public.json` was actually evaluated against `schemas/candidate-inventory.public.schema.json` with Draft 2020-12 validation.
- PASS: `aggregation-policy.v0.2.public.json` was actually evaluated against `schemas/aggregation-policy.schema.json` with Draft 2020-12 validation.
- PASS: exact ordered roster `AGB-P01A`–`AGB-P08B`, pair identity, 14 strict + 2 controlled diagnostics.
- PASS: P02A R06 timezone wording and `time_zone_resolved: true`.
- PASS: P05A/P05B strict; P08A/P08B controlled diagnostic.
- PASS: six exact macro groups; `target_identity_resolution` contains P04A/P04B/P07A/P07B under one group weight.
- PASS: seven exact complete strict pairs; strict case-micro, pair-conjunctive, UNRESOLVED, controlled-diagnostic, and mandatory-reporting rules present.
- PASS: private/gold filename, JSON-key, and blind-ID leakage scan.
- PASS: 9/9 negative self-tests caught (bad ID, P05 track, P08 track, both R06 omissions, macro membership, pair roster, mandatory field, gold-key leakage). Mutations and expected errors live in the static `validators/negative-self-tests.json` oracle file; they are not generated from validator output, and an unrelated failure does not count as PASS.
- validator exit code: 0

## Snapshot SHA-256 manifest

Canonical development source identity used for this public-safe derivative: `agbench-pilot-v0.1-dev.zip`, Library version 83, SHA-256 `545f8731a3770ca1decd5e48c215e1e639d15c486c85fa48ccd3982b3b8b6880`. The private ZIP is not committed.

No provider API, live model execution, scorer implementation, push, tag, or release was performed during this validation.
