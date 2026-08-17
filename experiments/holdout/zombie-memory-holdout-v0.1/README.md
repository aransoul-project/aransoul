# Zombie Memory Holdout v0.1 — Evidence Map

This directory is the public evidence archive for the completed Zombie Memory Holdout v0.1 study.

The archive preserves three evidence layers separately:

1. **Preregistered confirmatory evidence** — frozen construction/execution protocol, three within-protocol live replications, raw-data integrity checks, and frozen structured Authority scoring.
2. **Post-freeze measurement amendment** — semantic-equivalence measurement for `current_answer` and `historical_answer`, added because the original exact-string free-text metric was not suitable for semantic correctness.
3. **Exploratory analysis** — authority-error taxonomy and the frozen stratified inspection of extra selected records.

The three completed live replications are **within-protocol replications**, not independent external replication.

## Fast reading path

- [`RESEARCH-REPORT.md`](RESEARCH-REPORT.md) — paper-style overview, results, interpretation, and limitations.
- [`HOLDOUT-V0.1-FINDINGS.md`](HOLDOUT-V0.1-FINDINGS.md) — evidence-layered findings.
- [`HOLDOUT-V0.1-FINAL-AUDIT.md`](HOLDOUT-V0.1-FINAL-AUDIT.md) — final consistency/provenance audit (`PASS WITH DOCUMENTATION NOTE`).

## Preregistration and freeze chain

- [`PREREGISTRATION.md`](PREREGISTRATION.md) — early construction preregistration artifact. Its historical STOP language is intentionally preserved.
- [`FREEZE-MANIFEST.json`](FREEZE-MANIFEST.json) and [`FULL-FREEZE-AUDIT.md`](FULL-FREEZE-AUDIT.md) — frozen case-set/construction boundary.
- [`EXECUTION-PREREGISTRATION.md`](EXECUTION-PREREGISTRATION.md) — blind execution protocol.
- [`EXECUTION-FREEZE-MANIFEST.json`](EXECUTION-FREEZE-MANIFEST.json), [`EXECUTION-READY-AUDIT.md`](EXECUTION-READY-AUDIT.md), and [`DRY-RUN-AUDIT.md`](DRY-RUN-AUDIT.md) — execution-ready freeze and validation.
- [`REPLICATION-1-AUTHORIZATION.md`](REPLICATION-1-AUTHORIZATION.md), [`REPLICATION-2-AUTHORIZATION.md`](REPLICATION-2-AUTHORIZATION.md), [`REPLICATION-3-AUTHORIZATION.md`](REPLICATION-3-AUTHORIZATION.md) — staged run authorizations.

The early `PREREGISTRATION.md` is not rewritten after the fact; later freeze and execution artifacts document how the study progressed from design-only status to authorized live execution.

## Confirmatory raw evidence and scoring

Each valid live replication is preserved under `outputs/` with its manifest, raw `responses.jsonl`, raw-data integrity record, aggregate score, and scoring audit:

- `outputs/replication-1/live/replication-1-blind-live-attempt-1/`
- `outputs/replication-2/live/replication-2-blind-live-attempt-1/`
- `outputs/replication-3/live/replication-3-blind-live-attempt-1/`

Primary scoring definitions and code are in:

- [`HOLDOUT-SCORING-CONTRACT.md`](HOLDOUT-SCORING-CONTRACT.md)
- [`SCORER-SPEC.md`](SCORER-SPEC.md)
- [`holdout_scorer.py`](holdout_scorer.py)

The pooled confirmatory Authority exact-set result is **186/288 = 64.58%**.

## Post-freeze semantic measurement amendment

- [`SEMANTIC-SCORING-AMENDMENT-v0.1.md`](SEMANTIC-SCORING-AMENDMENT-v0.1.md)
- [`SEMANTIC-GRADER-VALIDATION.md`](SEMANTIC-GRADER-VALIDATION.md)
- [`semantic_grader.py`](semantic_grader.py)
- [`semantic-scoring-synthetic-v0.1.json`](semantic-scoring-synthetic-v0.1.json)
- per-replication `SEMANTIC-AGGREGATE-SCORE.json` and `SEMANTIC-SCORING-AUDIT.md` files under `outputs/`

Amended semantic results: current **284/288 = 98.61%**; historical **283/288 = 98.26%**. These are not part of the original confirmatory scoring plan.

## Exploratory analysis

- [`EXPLORATORY-AUTHORITY-ERROR-AUDIT.md`](EXPLORATORY-AUTHORITY-ERROR-AUDIT.md)
- [`EXPLORATORY-AUTHORITY-ERROR-SUMMARY.json`](EXPLORATORY-AUTHORITY-ERROR-SUMMARY.json)
- [`EXPLORATORY-STRATIFIED-SAMPLE-MANIFEST.json`](EXPLORATORY-STRATIFIED-SAMPLE-MANIFEST.json)
- [`EXPLORATORY-STRATIFIED-ERROR-ANALYSIS.json`](EXPLORATORY-STRATIFIED-ERROR-ANALYSIS.json)
- [`EXPLORATORY-STRATIFIED-ERROR-AUDIT.md`](EXPLORATORY-STRATIFIED-ERROR-AUDIT.md)

All **102/102** Authority exact-set failures were classified as over-selection in the exploratory taxonomy. This taxonomy and the stratified record-role inspection are exploratory, not confirmatory.

## What this archive does not establish

This study does not constitute independent external replication, does not establish a causal advantage or disadvantage for any metadata condition, does not validate the full AranSoul architecture, and does not identify a hidden model mechanism.

For citation guidance, see the repository-level [`CITATION.md`](../../../CITATION.md). For the current project validation boundary, see [`STATUS.md`](../../../STATUS.md).
