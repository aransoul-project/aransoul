# Zombie Memory External Replication Handoff v0.1

Status: **External-replication handoff document — no new replication result is claimed here.**

This document is for a researcher or engineering team outside the original AranSoul execution/evaluation lineage who wants to test the Zombie Memory authority-boundary finding without relying on private project context or interpretive approval from the original team.

The goal is not to obtain a positive result. A Red, null, contradictory, or Invalid result is acceptable and should be reported as such.

## 1. Research question

The narrow public-benchmark question is:

> Under a frozen set of records containing current, historical, supporting, stale, scoped, and non-authoritative material, can the tested model identify the exact records that currently control the answer while also preserving correct current and historical answers?

The original Holdout v0.1 found a gap between semantic answer correctness and exact current-authority-set accuracy. That result is prior evidence, not a target that the external replication is required to reproduce.

## 2. Independence principle

Use the narrowest evidence label supported by the actual design.

An **independent external replication** requires substantive control by a person or team outside the original AranSoul execution/evaluation lineage. At minimum, the external replicator should control or independently accept:

- the preregistration;
- model/provider and execution settings;
- execution itself;
- evaluation or scorer use;
- protocol-deviation decisions;
- reporting and final interpretation.

The external team must be free to publish or report a Red, null, contradictory, or Invalid outcome without AranSoul approval or reinterpretation.

Knowing the original published result does not automatically invalidate independence, but prior exposure must be disclosed.

## 3. Two valid replication paths

### Path A — Public-benchmark external replication

Reuse the frozen public Holdout prompts and final frozen scoring chain.

Start here:

- [`zombie-memory-replication-kit-v0.1/README.md`](zombie-memory-replication-kit-v0.1/README.md)
- [`zombie-memory-replication-kit-v0.1/PREREGISTRATION-TEMPLATE.md`](zombie-memory-replication-kit-v0.1/PREREGISTRATION-TEMPLATE.md)
- [`zombie-memory-replication-kit-v0.1/IMPLEMENTATION-GUIDE.md`](zombie-memory-replication-kit-v0.1/IMPLEMENTATION-GUIDE.md)
- [`zombie-memory-replication-kit-v0.1/EVIDENCE-LABEL-CHECKLIST.md`](zombie-memory-replication-kit-v0.1/EVIDENCE-LABEL-CHECKLIST.md)
- [`zombie-memory-replication-kit-v0.1/RESULT-REPORT-TEMPLATE.md`](zombie-memory-replication-kit-v0.1/RESULT-REPORT-TEMPLATE.md)

The original evidence archive is at:

`experiments/holdout/zombie-memory-holdout-v0.1/`

This path tests whether the prior behavioral result reproduces under external control. Reusing the public benchmark does not by itself test unfamiliar-case generalization.

### Path B — Independent unfamiliar-case replication

Construct or obtain a new case set that tests the same distinction between remembered/relevant information and currently controlling authority.

For this path:

- define gold current authority before target-model outputs are inspected;
- preserve the ability to answer both current and historical questions;
- include scope, supersession, expiry, exceptions, or related authority-boundary structure without copying hidden assumptions from the original cases;
- freeze the scoring/evaluation rule before substantive outputs are opened;
- do not force the new cases into the archived 24-case scorer unless they genuinely satisfy its frozen contract.

This path is stronger for generalization if construction, execution, and evaluation independence are documented.

## 4. Minimum pre-run freeze

Before substantive target-model execution, freeze at least:

1. intended evidence label;
2. benchmark/case source and exact commit/hash;
3. prior-exposure disclosure by role;
4. model/provider/version;
5. generation settings;
6. retry and timeout policy;
7. ordering/randomization policy;
8. parser/structured-output rule;
9. confirmatory metrics;
10. success/Amber/Red criteria;
11. technical-invalid conditions;
12. evaluator/scorer procedure;
13. raw-output preservation plan;
14. amendment rule.

Use the replication-kit preregistration template rather than modifying the original Holdout preregistration.

## 5. Contact-free public-benchmark workflow

For the public benchmark, an external replicator should be able to proceed without asking the original project for interpretation:

1. cite an exact AranSoul source commit;
2. verify frozen prompt hashes using the kit's cross-platform verifier;
3. enumerate the 24 × 4 = 96 requests;
4. implement the provider adapter independently;
5. preserve raw provider outputs;
6. create provider-neutral scorer-compatible response rows;
7. run the provider-neutral 96-row integrity validator;
8. run the archived scorer self-test;
9. run frozen aggregate structured scoring;
10. complete any preregistered semantic or secondary evaluation;
11. only then inspect exploratory individual-error structure;
12. publish enough artifacts for another reader to recover the exact run.

## 6. What AranSoul should not control

For a run intended to count as independent external replication, the original AranSoul team should not decide after outputs are visible:

- which failed requests are rerun;
- which metric becomes primary;
- how ambiguous cases are reinterpreted;
- whether a Red/null result is softened;
- which individual errors are excluded;
- which evidence label is applied solely because the result is favorable.

If the external replicator asks for clarification before execution, any clarification that affects the protocol should be documented and frozen before substantive outputs are inspected. If clarification occurs after outputs are visible, its evidentiary impact should be disclosed.

## 7. Expected deliverables

A useful external replication report should publish or preserve, subject to provider/legal restrictions:

- immutable preregistration;
- exact source commit or case-set hash;
- model/provider/version and execution settings;
- runner or reproducible execution procedure;
- run metadata/manifest;
- raw outputs or a justified restricted equivalent;
- integrity-validation output;
- scorer/evaluator version and validation result;
- confirmatory aggregate results;
- post-freeze amendments, if any;
- exploratory analysis, separately labeled;
- completed evidence-label declaration;
- final conclusion including null/negative outcomes.

The external work may live in another repository. It does not need to be merged into AranSoul to count as an external replication.

## 8. Reporting prior-result comparison

The original public Holdout v0.1 reported:

- pooled Authority exact-set: **186/288 = 64.58%**;
- post-freeze semantic current-answer equivalence: **284/288 = 98.61%**;
- post-freeze semantic historical-answer equivalence: **283/288 = 98.26%**;
- exploratory authority failures: **102/102 over-selection**.

Keep their evidence status intact when comparing:

- Authority exact-set is part of the preregistered structured confirmatory layer;
- semantic-equivalence results are a post-freeze measurement amendment in the original study;
- 102/102 over-selection is exploratory in the original study.

A new replication may preregister different secondary/semantic metrics, but it must not retroactively change the evidence status of the original study.

## 9. What would count as useful external evidence

Useful outcomes include all of the following:

- a close reproduction of the authority-boundary gap;
- a materially weaker or stronger gap;
- no gap under another model/provider;
- a different error structure such as under-selection or mixed errors;
- failure to reproduce the original over-selection pattern;
- a technical-invalid run that reveals a protocol or implementation weakness.

The direction of the result does not determine whether the replication is independent.

## 10. Claim boundary

One external replication still does not establish that:

- Zombie Memory is a universal taxonomy;
- all LLMs show the same authority-boundary failure;
- T/T/E/A is necessary or causal;
- one hidden model mechanism explains the behavior;
- synthetic benchmark success or failure directly predicts production-agent safety;
- the full AranSoul architecture is validated.

The purpose of external replication is to test whether the behavioral result survives separation from the original project lineage, not to promote a predetermined conclusion.
