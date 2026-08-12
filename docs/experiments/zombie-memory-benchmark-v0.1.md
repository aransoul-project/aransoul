# Zombie Memory Benchmark v0.1

Status: **Candidate experiment — pre-registered protocol, not yet an empirical result**

This benchmark tests a narrow question:

> When an agent receives multiple historically true but differently valid records, can an explicit memory-governance representation reduce errors caused by stale authority?

The benchmark does **not** test consciousness, persona identity, general intelligence, or the overall value of AranSoul.

## 1. Core hypothesis

A structured memory representation that separates **Truth / Time / Effect / Authority (T/T/E/A)** will reduce stale-authority errors compared with an unstructured long-context baseline.

A deeper formulation of the same hypothesis is:

> **Persistence does not have to imply authority.** An agent may preserve a record, recall it correctly when asked about history, and still refrain from letting that record control the present when its authority has expired.

### Null hypothesis

T/T/E/A provides no material improvement over simpler baselines once the same underlying information is available.

The experiment must allow the null hypothesis to win.

## 2. Unit of evaluation

Each case contains:

- a current user question;
- multiple records from different times;
- at least one record that was once valid but is no longer authoritative;
- enough information to determine the correct current answer;
- a gold label for which record(s) currently carry decision authority;
- where applicable, a gold historical answer showing whether superseded material can still be recalled correctly.

The benchmark should begin with **synthetic policy/state cases** so ground truth is explicit and no private user data is required.

## 3. Case families

Initial v0.1 target: **100 cases**, balanced across five families (20 each).

### A. Direct supersession

Example pattern:

- Policy A: refund window = 30 days.
- Later Policy B: effective August 1, refund window = 14 days.
- Policy A remains in history.
- Query occurs after August 1.

### B. Partial supersession

A new rule changes only one clause while older unaffected clauses remain valid.

### C. Exception hierarchy

A general current rule exists, but an authorized exception or scoped override applies to the queried case.

### D. Stale summary contamination

A later summary repeats an older rule but lacks authority to override the formal current source.

### E. Cross-period merge trap

Several individually true records from different periods can be combined into a hybrid state that never existed at any one time.

## 4. Baselines

All conditions should receive semantically equivalent underlying facts. Only representation / governance metadata changes.

### Baseline A — Plain context

Records are presented as ordinary text with no explicit governance schema beyond their natural wording.

### Baseline B — Timestamp only

Each record receives an explicit date / time marker, but no separate effect or authority labels.

### Baseline C — Status labels

Records receive explicit state labels such as Current / Historical / Candidate / Retired without the full T/T/E/A decomposition.

### Baseline D — T/T/E/A governance

Each record is represented with explicit fields:

- **Truth** — supported / disputed / unknown for the record content;
- **Time** — when the record applies or was recorded;
- **Effect** — current / superseded / partial / candidate / historical / revoked;
- **Authority** — whether the record may determine the present action and at what scope.

The T/T/E/A condition must not receive extra factual information unavailable to the other conditions.

## 5. Primary metrics

### 5.1 Current-answer accuracy

Percentage of cases where the final current answer matches ground truth.

### 5.2 Historical-recall accuracy

Percentage of historical queries where superseded or non-current records are still recalled correctly when the question explicitly asks about the past.

This metric is necessary because a method should not receive credit for avoiding stale-authority errors merely by suppressing or forgetting old information.

### 5.3 Stale-authority error rate

Percentage of cases where the answer is wrong specifically because a previously valid but currently non-authoritative record was used as controlling evidence.

### 5.4 Authority-resolution accuracy

Percentage of cases where the model correctly identifies which record(s) have current decision authority.

### 5.5 False-discard rate

Percentage of cases where still-valid older information is incorrectly ignored merely because it is old.

This prevents the benchmark from rewarding indiscriminate preference for newer information.

## 6. Memory-preservation check

A subset of cases should explicitly ask the model to list records that were once effective but are no longer current.

The intended success pattern is:

- old information remains recallable;
- historical questions can still be answered;
- current decisions are not controlled by expired authority.

This directly tests the distinction between **remembering** and **authorizing**.

## 7. Secondary metrics

Optional secondary measures:

- confidence calibration;
- abstention / reserve quality when authority is genuinely ambiguous;
- explanation quality scored against source provenance;
- token / latency overhead of each representation;
- sensitivity to record ordering.

Secondary metrics must not replace the primary metrics after results are observed.

## 8. Pre-registered success criteria

The experiment is not automatically Green merely because T/T/E/A achieves the highest raw accuracy.

### Green

All of the following:

- T/T/E/A improves current-answer accuracy over Plain Context by at least **10 percentage points**;
- T/T/E/A reduces stale-authority error rate by at least **50% relative** to Plain Context;
- authority-resolution accuracy improves over Plain Context and Timestamp Only;
- historical-recall accuracy does not worsen by more than **5 percentage points** relative to the best baseline;
- false-discard rate does not worsen by more than **5 percentage points** relative to the best baseline.

### Amber

A consistent directional benefit appears, but one or more Green thresholds are missed, or gains are concentrated in only some case families.

### Red

No meaningful advantage appears, or T/T/E/A introduces comparable or worse errors through over-structuring, false discard, metadata dependence, or degraded historical recall.

### Invalid

Examples:

- case generation leaks the answer only to one condition;
- baselines do not receive equivalent facts;
- scoring criteria are changed after seeing results;
- dataset construction makes authority trivial in one representation but not others;
- implementation bugs affect conditions unequally.

## 9. Alternative explanations

Even a Green result would not by itself prove that the four dimensions are individually necessary.

Alternative explanations include:

- any structured schema may help, regardless of T/T/E/A semantics;
- Authority alone may explain most of the gain;
- Time + Authority may be sufficient;
- simple Current / Historical labels may perform similarly;
- the benchmark may overfit to synthetic policy language;
- the model may simply follow explicit status labels rather than demonstrate robust memory governance;
- benefits may disappear under noisy retrieval or real long-context workloads.

## 10. Ablation plan

If the full T/T/E/A condition shows benefit, run at least these follow-up ablations before claiming all four dimensions are needed:

- Time only;
- Authority only;
- Time + Authority;
- Effect + Authority;
- simple status labels;
- full T/T/E/A.

Truth should also be ablated where all benchmark records are intentionally factually true, because it may provide no additional information in that subset.

## 11. Model and run discipline

For the first pilot:

- use one fixed model/version per comparison set;
- use the same temperature and generation parameters across conditions;
- randomize record order where possible;
- preserve all prompts and outputs;
- score using deterministic gold labels where possible;
- keep generation and scoring separable so later independent evaluation is possible.

Cross-model replication is a later evidence level, not required for the first pilot.

## 12. Open replication invitation

This benchmark is intentionally open to external testing.

Researchers, engineers, and interested contributors are welcome to:

- implement the dataset schema and pilot cases;
- run the same cases on different models or providers;
- propose simpler baselines that may explain the same effect;
- test whether Current / Historical labels are sufficient without T/T/E/A;
- run ablations such as Authority-only or Time + Authority;
- identify cases where the benchmark unintentionally favors one representation;
- submit Red or null results;
- propose adversarial cases that expose false forgetting, over-reliance on recency, or authority confusion;
- separate generation from evaluation more strongly through blinded or independent scoring.

Replication does **not** need to support the AranSoul hypothesis to be useful. A clean failure, null result, or simpler competing explanation is a valid contribution.

When sharing results, please report:

1. model/provider and exact version where available;
2. generation parameters;
3. benchmark commit or release used;
4. condition definitions;
5. per-family and aggregate metrics;
6. any changes to the protocol;
7. observed failure modes;
8. raw outputs or sufficient artifacts for independent checking when redistribution is permitted.

Please use [CONTRIBUTING.md](../../CONTRIBUTING.md) for repository contribution rules.

## 13. Claim boundary

A successful v0.1 experiment may support a claim such as:

> In this synthetic stale-authority benchmark, explicitly separating time, effect, and authority information reduced errors caused by superseded records relative to plain-context and simpler metadata baselines while preserving historical recall.

It must **not** be reported as:

- "AranSoul solved AI memory";
- "Zombie memory is a proven universal taxonomy";
- "T/T/E/A reveals how model memory works internally";
- "the benchmark proves long-term agent safety".

## 14. Next implementation step

The next artifact should be a machine-readable dataset schema plus a small pilot set (for example 10 cases) used only to verify that the task, scoring, and condition transformations are executable before generating the full 100-case benchmark.
