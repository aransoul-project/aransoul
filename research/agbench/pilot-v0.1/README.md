# AGBench Pilot v0.1 — GitHub-safe development research snapshot

**Status:** `development_only`  
**Research state:** `PAUSED_AFTER_STATIC_MEASUREMENT_DESIGN_CLOSURE`

This directory is a public-safe development snapshot of the AGBench Pilot v0.1 measurement design. It preserves enough material to inspect the current static design, inventory shape, aggregation rules, provenance boundary, and offline validation logic without publishing sealed evaluation material.

This is **not** a benchmark release, **not** a frozen holdout, **not** a preregistration, and **not** a model-performance result. No live experiment is authorized by this snapshot.

## Snapshot inventory

- 16 synthetic cases
- 14 strict-primary cases
- 2 controlled-scope diagnostics
- 6 primary macro groups
- 7 complete strict contrast pairs
- 6 recorded repairs

The model-facing case file intentionally contains scenarios and observable context only. It excludes expected behavior, gold labels, blind identifiers, reviewer decisions, adjudicator submissions, and private mappings.

## Included

- `RESEARCH-REPORT.md`
- `FINAL-STATUS.md`
- `ARTIFACT-INDEX.md`
- `RESUME-CONDITIONS.md`
- `candidate-inventory.v0.2.model-facing.json`
- `aggregation-policy.v0.1.json`
- `measurement-track-revision.v0.1.md`
- public-safe schemas
- offline validators, including a fail-closed leakage validator

## Explicitly excluded

Private answer keys, gold labels, blind-ID mappings, reviewer-only packets, sealed materials, adjudicator submissions, private/gold-bearing fixtures, provider adapters, live experiment harnesses, provider API code, and scorer implementations are not part of this snapshot.

## Evidence boundary

The snapshot records a completed **static measurement-design closure** only. It does not establish benchmark validity in deployment, model performance, cross-provider generalization, preregistered confirmatory evidence, or release readiness.

See `FINAL-STATUS.md` and `RESUME-CONDITIONS.md` before treating this directory as authorization for any next phase.
