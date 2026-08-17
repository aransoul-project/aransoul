# Zombie Memory Holdout v0.1 — Findings

## Status and evidence layers

This document separates confirmatory results, post-freeze measurement amendments, exploratory analyses, and conclusions that remain unsupported. The distinctions are intentional and should be preserved in any later reporting.

## 1. Confirmatory execution and structured authority result

Three preregistered blind live replications were completed using the same frozen prompt payload, model snapshot (`gpt-4.1-mini-2025-04-14`), temperature 0, top_p 1, retry_count 0, and 24 cases × 4 conditions per replication.

Across all three replications there were 288 substantive live responses. All three replications passed transport/parsing checks and metadata-only raw-data integrity gates before scoring.

Authority exact-set accuracy by replication:

- Replication 1: 61/96 = 63.54%
- Replication 2: 63/96 = 65.63%
- Replication 3: 62/96 = 64.58%
- Pooled: 186/288 = 64.58%

Pooled authority exact-set accuracy by condition:

- Plain: 49/72 = 68.06%
- Timestamp: 47/72 = 65.28%
- Status: 50/72 = 69.44%
- T/T/E/A: 40/72 = 55.56%

Across all three replications, stale-authority error count = 0 and false-discard count = 0 under the frozen authority scorer.

### Confirmatory interpretation

Within this benchmark, exact identification of the currently controlling authority set is substantially less reliable than the later semantic free-text answer measure. The authority result itself is confirmatory; causal explanations for the failures are not.

## 2. Post-freeze measurement amendment for free-text answers

The original scorer evaluated `current_answer` and `historical_answer` with normalized exact-string equality even though the frozen prompt contract allowed ordinary free-text answers and did not require canonical wording. The resulting 0% exact-string answer metrics were therefore judged invalid / uninterpretable for semantic correctness.

A semantic-scoring amendment was then defined without inspecting replication-1 individual answers. The deterministic semantic grader was validated on 18 synthetic examples (18/18 pass) and frozen before it was allowed to score replication-1 answers.

Semantic-equivalence results:

- Current answer: 284/288 = 98.61%
- Historical answer: 283/288 = 98.26%

By replication:

- Replication 1: current 95/96; historical 94/96
- Replication 2: current 95/96; historical 95/96
- Replication 3: current 94/96; historical 94/96

T/T/E/A semantic performance was 72/72 for both current and historical answers across the three replications.

### Measurement interpretation

The semantic results are informative but are explicitly a post-freeze measurement amendment rather than part of the original confirmatory scoring plan. The original exact-string 0% outputs remain preserved as historical artifacts and must not be reported as evidence that all free-text answers were semantically wrong.

## 3. Exploratory structural error taxonomy

After the three preregistered replications and aggregate analyses were complete, individual-level authority failures were opened for exploratory analysis.

Of the 288 responses:

- Exact authority-set matches: 186
- Authority-set failures: 102

All 102 failures were structurally classified as `over_selection`:

- under_selection: 0
- over_selection: 102
- mixed_selection: 0
- empty_prediction: 0
- other: 0

This pattern was stable by replication:

- Replication 1: 35 over-selection failures
- Replication 2: 33 over-selection failures
- Replication 3: 34 over-selection failures

Failure rates by frozen family:

- Explicit authority hierarchy: 3/48 = 6.25%
- Supersession / replacement: 8/48 = 16.67%
- Current but non-authoritative material: 14/48 = 29.17%
- Historical superseded-but-correct answer: 15/48 = 31.25%
- Scoped exception vs general rule: 29/48 = 60.42%
- Temporary rule with expiry/restoration: 33/48 = 68.75%

### Exploratory interpretation

The dominant structural failure is not omission of required authority records. It is inclusion of extra records beyond the frozen gold authority set. This supports describing the observed benchmark weakness as an authority-boundary problem rather than a simple stale-memory retrieval failure. This statement is exploratory, not preregistered confirmatory evidence.

## 4. Exploratory stratified sample of extra records

A deterministic 18-failure stratified sample was frozen before record-content inspection. It covered:

- 6 Temporary rule with expiry/restoration failures
- 6 Scoped exception vs general rule failures
- 6 T/T/E/A over-selection failures

The 18 sampled failures contained 24 extra selected records. Structural roles were:

- supporting_or_context_record: 14
- general_rule_outside_scope: 7
- current_non_authoritative_material: 3
- all other predefined roles: 0
- unclassified: 0

Within the sampled Temporary rule with expiry/restoration stratum, extra records were 6 supporting/context and 2 current non-authoritative records. No sampled extra record was classified as the expired temporary rule itself.

Within the sampled Scoped exception vs general rule stratum, extra records included 5 general-rule-outside-scope records and 3 supporting/context records.

Within the sampled T/T/E/A stratum, extra records included 5 supporting/context, 2 general-rule-outside-scope, and 1 current non-authoritative record.

### Exploratory interpretation

In this sample, the model often retained the correct controlling record while also selecting records that remained relevant or informative but lacked current controlling authority. The evidence therefore points more specifically to over-broad authority attribution than to wholesale resurrection of expired or superseded records.

A concise research framing is:

> remembered ≠ relevant ≠ supportive ≠ currently authoritative

This framing is a synthesis of the observed exploratory structure. It should not be generalized beyond this benchmark or model without further external replication.

## 5. What the study does not establish

The current evidence does **not** establish any of the following:

- that T/T/E/A causally harms authority reasoning in general;
- that richer metadata universally causes over-selection;
- that the observed behavior generalizes to other models, providers, agent frameworks, or real-world memory systems;
- that all authority failures arise from the same internal reasoning mechanism;
- that the benchmark's frozen gold authority sets are the only reasonable ontology for all memory-governance tasks;
- that stale memory itself is the main failure mode;
- that semantic answer correctness alone proves safe or correct memory governance.

No claim about model psychology, attention, hidden reasoning, or causal mechanism is supported by these analyses.

## 6. Current research-level conclusion

The strongest narrow conclusion from Holdout v0.1 is:

> On this fixed 24-case Zombie Memory holdout, across three blind replications and 288 live responses, the tested model almost always produced semantically correct current and historical answers, while exact current-authority-set identification remained near 65%. Exploratory inspection showed that every authority-set failure was over-selection, with sampled extra records concentrated in supporting/context material and out-of-scope general rules. The observed challenge is therefore not well described as simple forgetting or stale-memory retrieval; it is more precisely a failure to keep remembered or relevant material distinct from material that currently has decision authority.

Confirmatory, amended-measurement, and exploratory evidence must remain separately labeled when this result is cited or published.
