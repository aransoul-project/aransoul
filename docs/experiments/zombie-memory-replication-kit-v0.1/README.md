# Zombie Memory Replication Kit v0.1

Status: **Candidate replication kit — design and handoff materials only; no new replication result is claimed by this kit.**

This kit is intended to let a researcher or engineer outside the original AranSoul execution lineage prepare a reproducible Zombie Memory replication without requiring private project context or informal instructions from the original team.

The kit does not guarantee that a run qualifies as independent external replication. The evidence label depends on who controls case construction, generation, evaluation, and reporting. Use the accompanying evidence-label checklist and the [Independent Replication Protocol v0.1](../zombie-memory-independent-replication-protocol-v0.1.md).

## What this kit contains

- [`PREREGISTRATION-TEMPLATE.md`](PREREGISTRATION-TEMPLATE.md) — fields to freeze before substantive target-model outputs are inspected.
- [`IMPLEMENTATION-GUIDE.md`](IMPLEMENTATION-GUIDE.md) — provider-neutral handoff including cross-platform hash verification and pre-score structural validation.
- [`verify_frozen_hashes.py`](verify_frozen_hashes.py) — verifies frozen prompt hashes from Git repository bytes.
- [`validate_provider_neutral_responses.py`](validate_provider_neutral_responses.py) — fail-closed 24×4 structural gate before the historical scorer is invoked.
- [`VALID-RESPONSE-EXAMPLE.jsonl`](VALID-RESPONSE-EXAMPLE.jsonl) — minimal provider-neutral response-row example.
- [`RUN-METADATA-SCHEMA.json`](RUN-METADATA-SCHEMA.json) — minimum machine-readable metadata for a replication run.
- [`RUN-METADATA-EXAMPLE.json`](RUN-METADATA-EXAMPLE.json) — non-empirical metadata example.
- [`RESULT-REPORT-TEMPLATE.md`](RESULT-REPORT-TEMPLATE.md) — reporting structure that preserves evidence boundaries.
- [`EVIDENCE-LABEL-CHECKLIST.md`](EVIDENCE-LABEL-CHECKLIST.md) — conservative replication-label rules.

## Source benchmark and provenance

The completed Holdout v0.1 archive is preserved at `experiments/holdout/zombie-memory-holdout-v0.1/`. Replicators should cite an exact repository commit SHA for any source artifact they use.

## Two valid replication paths

### Path 1 — Public-benchmark reproduction
Reuse the frozen public Holdout cases and scoring definitions. If the original project lineage still controls execution and evaluation, the result should normally be labeled **reproduction** or **cross-model reproduction**, not independent external replication.

### Path 2 — Independent unfamiliar-case replication
Construct or obtain a new case set testing remembered/relevant material versus currently controlling authority. Gold authority must be fixed before target-model outputs are inspected.

## Minimum workflow

1. Choose the narrowest intended evidence label.
2. Fix the benchmark/case source and exact commit or case-set hash.
3. Freeze `PREREGISTRATION-TEMPLATE.md` before substantive target-model output inspection.
4. Use `IMPLEMENTATION-GUIDE.md` for provider-neutral execution.
5. Verify frozen prompt hashes with `verify_frozen_hashes.py` from the exact Git source commit.
6. Record model/provider/version, parameters, retries, ordering/randomization, and evaluator design.
7. Preserve raw outputs and run metadata.
8. Run `validate_provider_neutral_responses.py` and require PASS before invoking the historical scorer.
9. Apply frozen confirmatory scoring first.
10. Treat post-output metric changes as amendments and keep non-preregistered qualitative/error analysis exploratory.
11. Publish the completed result report with recoverable provenance.

## Important implementation note

The original `runner.py` is a provenance artifact for the completed Holdout and is tied to its original execution environment. External replicators may replace provider-facing mechanics, but must not silently change the frozen research payload or scoring meaning.

## Required evidence boundaries

Keep preregistered confirmatory, post-freeze amendment, exploratory, and invalid/technical-invalid evidence visibly separate. A null or Red result is a valid contribution.

## Contact-free standard

The kit is usable only if a technically competent external reader can determine, from repository artifacts alone, what to freeze, how to verify inputs across platforms, how to create and validate a complete 24×4 response archive before scoring, how to classify the evidence level, and how to report null/negative/amended/invalid outcomes without asking the original project to reinterpret them.
