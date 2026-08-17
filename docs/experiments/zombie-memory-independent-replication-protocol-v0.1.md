# Zombie Memory Independent Replication Protocol v0.1

Status: **Candidate protocol — design only; no new replication result is claimed by this document.**

This protocol defines what AranSoul should require before describing future Zombie Memory evidence as more independent than the completed Holdout v0.1 within-protocol replications.

The purpose is not to obtain another positive result. The purpose is to reduce shared-generation, shared-evaluation, benchmark-familiarity, and same-team confirmation loops.

## 1. Starting evidence boundary

Zombie Memory Holdout v0.1 already provides three preregistered within-protocol live replications under one frozen benchmark, model snapshot, execution protocol, and project lineage.

Those replications support stability within the studied protocol. They do **not** by themselves establish independent external replication.

This protocol begins from that boundary rather than treating a fourth same-protocol run as a new evidence level.

## 2. Replication labels

Future runs should use the narrowest label that matches the actual design.

### A. Reproduction

Use this label when the same project team reruns the same public benchmark or substantially the same cases under the same evaluation lineage.

A different date alone does not make a run independent.

### B. Cross-model reproduction

Use this label when the same public benchmark and same project evaluation lineage are used with a different model, model version, or provider.

This tests model dependence, but does not by itself remove same-team or benchmark-familiarity confounds.

### C. Evaluation-separated replication

Use this label when generation and evaluation are meaningfully separated before results are inspected. Examples include a blinded human evaluator, a separately frozen evaluator context, or an independently specified deterministic scoring procedure.

This corresponds primarily to stronger Level 5 evidence in the AranSoul evidence ladder.

### D. Independent external replication

Use this label only when a person or team outside the original AranSoul execution/evaluation lineage independently controls the replication procedure and reports enough artifacts for checking.

The external replicator may reuse the public benchmark, but must disclose prior exposure to the original results and any deviations from the protocol.

### E. Cross-environment / generalization replication

Use this stronger label when independent execution is combined with a meaningfully different model/provider/environment and/or independently constructed unfamiliar cases that test the same authority-boundary hypothesis.

This is closer to Level 6 evidence. It should not be inferred merely from changing one model name while keeping all other dependencies shared.

## 3. Minimum preregistration fields

Before any substantive model output is inspected, a replication record should freeze:

1. replication label sought (A–E above);
2. exact benchmark/case source and commit SHA;
3. whether cases are public, newly constructed, or independently supplied;
4. model/provider and exact version or snapshot where available;
5. generation parameters and retry policy;
6. record ordering/randomization policy;
7. primary and secondary metrics;
8. scoring implementation or evaluator procedure;
9. invalidation conditions;
10. protocol-deviation reporting rules;
11. raw-output preservation/redistribution plan;
12. what information the generator, evaluator, and case constructor may see before freeze.

If any of these fields change after substantive outputs are observed, the change must be labeled as an amendment rather than silently folded into the preregistered analysis.

## 4. Separation requirements

### Case construction

For unfamiliar-case replication, case constructors should define gold current authority independently of model responses. Cases should permit historical recall while distinguishing relevance/support from current controlling authority.

Case constructors should not tune cases after seeing target-model errors unless the resulting set is explicitly labeled adversarial/exploratory rather than confirmatory.

### Generation

The generation runner should receive only the frozen case representation and allowed task instructions. It should not receive original Holdout individual responses or error annotations as hidden guidance.

### Evaluation

The evaluator should receive only information required by the frozen scoring contract. If human judgment is needed, condition labels and model identity should be blinded where practical.

Evaluation criteria must be fixed before opening individual target-model responses for qualitative interpretation.

## 5. Core outcome measures

A replication may reuse the established Zombie Memory distinction:

- current-answer correctness;
- historical-answer correctness;
- exact current-authority-set accuracy;
- stale-authority error count/rate;
- false-discard count/rate.

If semantic free-text grading is used, the semantic grader or human rubric must be frozen before target answers are graded. It must be reported separately from any original exact-string or deterministic metric that is not semantically equivalent.

## 6. Authority-error taxonomy

Individual error taxonomy remains exploratory unless its categories and coding rules are independently preregistered before individual failures are opened.

The Holdout v0.1 observation that all 102 authority failures were over-selection is a prior result, not a guaranteed replication target.

A valid replication must permit under-selection, mixed errors, null effects, or a completely different error structure.

## 7. Result classes

The protocol should allow all outcomes:

- **Green** — predefined replication criteria are met;
- **Amber** — partial or unstable support;
- **Red** — the prior effect does not reproduce or a competing explanation performs equally well/better;
- **Invalid** — protocol, leakage, scoring, execution, or data-integrity problems prevent interpretation.

A Red or null result is scientifically useful and must not be treated as a failed contribution.

## 8. Claim rules

A future report must distinguish:

- reproduction from independent replication;
- evaluation separation from cross-model generalization;
- preregistered results from amendments;
- confirmatory metrics from exploratory error analysis;
- behavioral evidence from claims about hidden model mechanisms.

No replication under this protocol may by itself justify claims that:

- AranSoul has solved AI memory;
- Zombie Memory is a universal taxonomy;
- T/T/E/A is mechanistically necessary;
- authority-boundary errors arise from one hidden reasoning mechanism;
- success on synthetic cases establishes production-agent safety.

## 9. Recommended next experiment

The next useful step is **not** a fourth internal run of the completed Holdout v0.1 protocol.

Preferred order:

1. freeze this independent-replication protocol;
2. prepare a small replication kit containing benchmark provenance, runner/scorer instructions, required metadata, and a result-report template;
3. seek an evaluator or replicator separated from the original execution lineage;
4. only then execute a new replication under a predeclared label;
5. if feasible, add unfamiliar independently constructed cases or a different model/provider to move toward Level 6 evidence.

Until steps 3–4 occur, AranSoul should continue describing the existing Holdout evidence as **internal behavioral validation with within-protocol replication**, not independent external validation.
