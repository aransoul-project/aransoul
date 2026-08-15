# Zombie Memory Holdout v0.1 — Preregistration Skeleton

Status: **design-only; no holdout cases generated; no model runs permitted**

Base empirical archive: `main` at merge commit `2384acc9e031b774ed93c7ebb1b4acb202238442`.

## Purpose

The holdout exists to test whether the behavioral signal observed in Zombie Memory Pilot v0.1 generalizes beyond the original 10 cases. It is not intended to optimize T/T/E/A, Timestamp, or any other condition against known Pilot results.

Primary risk addressed: self-validation through repeated testing on a case set whose outcomes and failure modes are already known.

## Separation rule

Holdout case construction and holdout result interpretation must be separated as far as practicable.

Before model execution:

1. case families, quotas, generation rules, gold-label rules, exclusion rules, and scoring rules must be frozen;
2. the final holdout cases must receive stable IDs and cryptographic hashes;
3. no model may be run on partial or draft holdout cases;
4. no case may be edited after any holdout model output is observed;
5. no individual failed case may be selectively rerun unless a preregistered technical-invalid rule requires replacement of the entire run.

## Independence from Pilot v0.1

The holdout may reuse the same *constructs* — current answer, historical recall, and controlling authority — but must not copy or minimally paraphrase Pilot v0.1 cases.

Case authors must avoid intentionally recreating the known Pilot failure motifs solely because they produced useful-looking results. In particular, the holdout must not be built to force the previously observed ordering Timestamp > Plain/Status/T/T/E/A.

Pilot results may be used only to define risks to guard against, not to tune holdout answers or condition wording.

## Planned case-set size

Target: **24 independent holdout cases**.

This target is fixed before case generation. If fewer than 24 survive quality review, the set must be completed back to 24 before freeze rather than shrinking after inspection of model behavior.

## Planned case families

The 24 cases will be distributed across six families, four cases each:

1. supersession / replacement;
2. scoped exception versus general rule;
3. temporary rule with expiry or restoration;
4. descriptive/current-but-non-authoritative material;
5. conflicting sources with explicit authority hierarchy;
6. historical query where a superseded record remains the correct historical answer.

Family assignment is a design property, not a score category.

## Difficulty balancing

Within each family, cases should vary in surface domain and record count. The set should include both two-record and three-or-more-record cases. No condition may receive a different semantic case set.

No case may depend on obscure real-world facts; all controlling facts must be contained in the records shown to the model.

## Conditions

The same four representation conditions are retained for comparability:

- Plain
- Timestamp
- Status
- T/T/E/A

Condition renderers must preserve semantic equivalence. A renderer-equivalence audit is required before freeze.

The holdout does **not** preregister a hypothesis that T/T/E/A will win.

## Primary metrics

For each condition:

1. current-answer accuracy;
2. historical-recall accuracy;
3. Authority exact-set accuracy;
4. stale-authority error count;
5. false-discard case count.

The exact-set Authority metric remains primary and must not be weakened after results are seen.

## Secondary diagnostic

The Round 2 Authority taxonomy is preregistered as a secondary diagnostic:

- exact match;
- over-selection;
- omission;
- wrong source;
- stale or explicitly non-authoritative selection.

Secondary diagnostics may explain primary-score failures but may not replace or rescore the primary metric.

## Gold-label construction

Each case must contain explicit machine-readable gold fields for:

- current answer;
- historical answer;
- current controlling record IDs;
- stale record IDs where applicable.

Gold labels must be derived from written case logic before any model is run.

A case is invalid during construction if two reasonable readings produce different controlling sets without an explicit tie-break rule in the records.

## Quality review before freeze

Every case must pass:

1. semantic-equivalence review across all four rendered conditions;
2. gold-consistency review;
3. authority-uniqueness / tie-break review;
4. leakage review for labels, hints, or wording that exposes the intended answer;
5. Pilot-overlap review to reject copied or trivial paraphrases;
6. deterministic scorer validation.

Any case failing review must be repaired or replaced **before** the holdout is frozen.

## Freeze boundary

The holdout is frozen only when all of the following exist and are committed together:

- 24 final cases;
- schema;
- renderer;
- four generated condition files;
- frozen prompt hashes;
- scorer;
- gold labels;
- validation audit;
- this preregistration updated from skeleton to final protocol.

After that freeze commit, no case, gold label, renderer semantic, or primary scoring rule may change for the holdout run.

## Execution protocol

No API calls are authorized by this skeleton.

A later execution protocol must separately freeze:

- model snapshot(s);
- number of replications;
- sampling parameters;
- retry policy;
- technical-invalid rules;
- raw-data integrity gate;
- scoring gate.

## Technical-invalid principle

Transport/provider failures with no model completion must not be counted as substantive model errors. If a preregistered run is rendered incomplete by such a failure, the incomplete run must be permanently preserved and the replacement policy must apply to the complete run, never to a selectively rerun case.

## Interpretation boundary

A successful holdout would strengthen evidence that the observed Zombie Memory behavior generalizes beyond the original Pilot cases. It still would not by itself validate the full AranSoul architecture.

A failure to reproduce the Pilot signal must be preserved as a valid negative result rather than explained away by redesigning the holdout after inspection.

## Current gate

**STOP.** This document authorizes design work only. Do not generate model responses, do not score anything, and do not claim the holdout is frozen until a later explicit freeze review.