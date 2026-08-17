# Zombie Memory Replication Kit v0.1

Status: **Candidate replication kit — design and handoff materials only; no new replication result is claimed by this kit.**

This kit is intended to let a researcher or engineer outside the original AranSoul execution lineage prepare a reproducible Zombie Memory replication without requiring private project context or informal instructions from the original team.

The kit does not guarantee that a run qualifies as independent external replication. The evidence label depends on who controls case construction, generation, evaluation, and reporting. Use the accompanying evidence-label checklist and the [Independent Replication Protocol v0.1](../zombie-memory-independent-replication-protocol-v0.1.md).

## What this kit contains

- [`PREREGISTRATION-TEMPLATE.md`](PREREGISTRATION-TEMPLATE.md) — fields to freeze before substantive target-model outputs are inspected.
- [`IMPLEMENTATION-GUIDE.md`](IMPLEMENTATION-GUIDE.md) — provider-neutral handoff from frozen prompts to request enumeration, response preservation, scorer-compatible rows, integrity checks, and reporting.
- [`RUN-METADATA-SCHEMA.json`](RUN-METADATA-SCHEMA.json) — minimum machine-readable metadata for a replication run.
- [`RESULT-REPORT-TEMPLATE.md`](RESULT-REPORT-TEMPLATE.md) — reporting structure that preserves confirmatory, amended, exploratory, and invalid evidence boundaries.
- [`EVIDENCE-LABEL-CHECKLIST.md`](EVIDENCE-LABEL-CHECKLIST.md) — conservative rules for calling a run reproduction, cross-model reproduction, evaluation-separated replication, independent external replication, or cross-environment/generalization replication.

## Source benchmark and provenance

The completed AranSoul Holdout v0.1 archive is preserved at:

`experiments/holdout/zombie-memory-holdout-v0.1/`

Useful source artifacts include:

- `README.md` — evidence map;
- `PREREGISTRATION.md` and `EXECUTION-PREREGISTRATION.md` — historical design/execution freezes;
- `FREEZE-MANIFEST.json` and `EXECUTION-FREEZE-MANIFEST.json` — frozen provenance;
- `runner.py` — guarded original OpenAI-specific runner used by the completed Holdout;
- `holdout_scorer.py` — deterministic structured scorer;
- `HOLDOUT-SCORING-CONTRACT.md` and `SCORER-SPEC.md` — scoring definitions;
- `SEMANTIC-SCORING-AMENDMENT-v0.1.md` — post-freeze semantic measurement amendment;
- `HOLDOUT-V0.1-FINDINGS.md` and `HOLDOUT-V0.1-FINAL-AUDIT.md` — completed-study findings and audit.

Replicators should cite an exact repository commit SHA for any source artifact they use.

## Two valid replication paths

### Path 1 — Public-benchmark reproduction

Reuse the frozen public Holdout cases and scoring definitions.

This is the fastest path for testing model/provider dependence. If the original project lineage still controls execution and evaluation, the result should normally be labeled **reproduction** or **cross-model reproduction**, not independent external replication.

### Path 2 — Independent unfamiliar-case replication

Construct or obtain a new case set that tests the same distinction between remembered/relevant material and currently controlling authority.

Gold authority must be defined before target-model outputs are inspected. New cases should permit historical recall while making scope, supersession, exceptions, and current authority independently decidable.

This path is more useful for testing generalization, but only if case construction, generation, and evaluation separation are documented clearly.

## Minimum workflow

1. Choose the narrowest intended evidence label.
2. Fix the benchmark/case source and exact commit or case-set hash.
3. Complete and freeze `PREREGISTRATION-TEMPLATE.md` before inspecting substantive target-model outputs.
4. Use `IMPLEMENTATION-GUIDE.md` to implement or adapt the provider-facing runner without silently changing the research payload.
5. Record model/provider/version, parameters, retries, ordering/randomization, and evaluator design.
6. Run transport/format validation before substantive scoring.
7. Preserve raw outputs and complete `RUN-METADATA-SCHEMA.json`-compatible metadata.
8. Apply only frozen confirmatory scoring first.
9. Treat any post-output metric change as an explicit amendment.
10. Keep qualitative/error-taxonomy analysis exploratory unless it was separately preregistered.
11. Publish the completed `RESULT-REPORT-TEMPLATE.md` with enough provenance for another reader to recover the artifacts.

## Important implementation note

The original `runner.py` is a provenance artifact for the completed Holdout and is intentionally strict: it is tied to the original 24 cases, four conditions, three planned replications, frozen hashes, and OpenAI Responses API execution. External replicators may adapt or replace the runner for another provider or environment, but any change must be documented. `IMPLEMENTATION-GUIDE.md` defines the minimum provider-neutral input/output and scorer-compatibility contract for that handoff.

Do not silently modify the original frozen Holdout files to make a new run fit. Put new replication artifacts in a separate directory or repository and cite the source commit used.

## Required evidence boundaries

A replication report must keep these distinctions visible:

- **Preregistered confirmatory:** metrics and decision rules fixed before substantive output inspection.
- **Post-freeze amendment:** a later measurement or procedure added after the original freeze; its rationale and timing must be explicit.
- **Exploratory:** error taxonomy, qualitative interpretation, subgroup inspection, or post-hoc hypotheses not preregistered as confirmatory.
- **Invalid / technical-invalid:** leakage, scoring defects, transport failures, missing provenance, or protocol violations that prevent the planned interpretation.

A null or Red result is a valid contribution.

## What successful replication would and would not mean

A successful external replication can strengthen the claim that authority-boundary errors recur beyond the original AranSoul execution lineage. A cross-model or unfamiliar-case replication can also test model and benchmark dependence.

It would still not establish that Zombie Memory is a universal taxonomy, that T/T/E/A is mechanistically necessary, that one hidden reasoning mechanism explains all failures, or that success on synthetic tasks guarantees production-agent safety.

## Contact-free standard

The kit should be considered usable only if a technically competent external reader can determine, from repository artifacts alone:

- what to freeze before running;
- how to turn the frozen public prompts into a provider-neutral execution and scorer-compatible response archive;
- what must be recorded;
- how to classify the evidence level;
- where the original benchmark/scoring provenance lives;
- how to report null, negative, amended, or invalid outcomes without asking the original project to reinterpret them.
