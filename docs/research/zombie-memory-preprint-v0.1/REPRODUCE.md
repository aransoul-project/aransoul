# Zombie Memory Preprint v0.1 — Reproduction Entry Point

This file is the shortest publication-facing route for reconstructing the reported results from repository-local artifacts. It does not authorize any new live model execution.

## Scope

The completed Holdout evidence is archived under:

`experiments/holdout/zombie-memory-holdout-v0.1/`

The contact-free reproduction handoff is under:

`docs/experiments/zombie-memory-replication-kit-v0.1/`

For historical public-benchmark prompt/hash recovery, use the execution-ready source commit documented in:

`docs/experiments/zombie-memory-replication-kit-v0.1/PUBLIC-BENCHMARK-SOURCE.md`

Recommended historical source commit:

`878b21f62faa9d999793b731198caac88a97bf62`

## Offline verification order

1. Verify repository-byte hashes for the frozen generated prompts.
2. Run the Holdout scorer self-test.
3. Validate each archived 96-row response archive structurally.
4. Recompute aggregate structured authority scores for the three archived runs.
5. Recompute the post-freeze semantic-equivalence measurements.
6. Recompute the exploratory authority-error taxonomy and stratified analysis.
7. Compare reconstructed outputs against the archived findings and final audit.

Representative commands, run from repository root where paths apply:

```text
python docs/experiments/zombie-memory-replication-kit-v0.1/verify_frozen_hashes.py --ref 878b21f62faa9d999793b731198caac88a97bf62

python experiments/holdout/zombie-memory-holdout-v0.1/holdout_scorer.py --self-test

python docs/experiments/zombie-memory-replication-kit-v0.1/validate_provider_neutral_responses.py <responses.jsonl>

python experiments/holdout/zombie-memory-holdout-v0.1/holdout_scorer.py --responses <responses.jsonl> --output <aggregate-score.json>
```

The exact archived replication paths and derived artifacts are indexed in `PROVENANCE-INDEX.json`.

## Historical pre-score integrity gate vs current revalidation

`validate_raw_integrity.py` is a historical **pre-scoring state-machine gate** for the original live-run workflow. It intentionally expects pre-scoring manifest state, including `scoring_started=false`. A completed archived run may therefore be rejected by that historical gate because its manifest records the later post-scoring state.

This expected rejection does **not** imply evidence corruption.

For current post-hoc reconstruction of the completed archives, use:

- the preserved raw rows and run manifests;
- archived integrity-audit records;
- provider-neutral 96-row structural validation;
- deterministic scorer reconstruction;
- final findings and final audit.

Keep these two purposes separate:

- historical gate: prove the run met the pre-scoring workflow condition at the time;
- present reconstruction: verify the archived evidence and reported outputs after study completion.

## Evidence-status boundary

Do not collapse the manuscript's evidence layers during reproduction:

- exact current-authority-set result: preregistered structured confirmatory evidence;
- semantic current/historical equivalence: post-freeze measurement amendment;
- 102/102 over-selection taxonomy and stratified record-role analysis: exploratory;
- mechanism, cross-model generality, production safety impact, and independent external replication: not established by Holdout v0.1.

## Scorer chronology

The 24 record-level scorer fixtures and authority exact-set expectations were frozen before target-model execution. The final fixture-locked executable scorer and scoring contract were committed after live execution had begun. The manuscript treats this as a protocol implementation-timing deviation. Reproduction of the completed result should preserve that chronology rather than retrospectively describing the final executable package as having been committed pre-run.

## Publication snapshot

This document is still part of manuscript preparation. Before public preprint release, the author should replace mutable `main` references with an immutable publication commit/tag and verify every command/path against that snapshot.
