# Zombie Memory Pilot v0.1 — Round 2 Replication Summary

Status: **completed preregistered replication; research status remains Amber**

Preregistration freeze commit: `35adafbc9281c8fd0bfdc977954b169f22a38a91`

Model: `gpt-4.1-mini-2025-04-14`

This document summarizes already-recorded Round 2 results. It does not change the frozen Pilot v0.1 instrument, scorer, gold labels, prompts, preregistration, or any recorded run output.

## Scope

Round 2 repeated the same frozen 10-case × 4-condition instrument three times with the same model and execution settings. These are repeated measurements of the same 10 cases, **not 30 independent cases**. Round 2 therefore addresses within-model reproducibility only; it does not establish cross-model or out-of-sample generality.

The four conditions are Plain, Timestamp, Status, and T/T/E/A.

## Execution history

One initial Replication 1 attempt (`live-20260815T184124.014730Z`) was classified and permanently preserved as **Technical Invalid** because request 2 (Plain / ZM-P02) received a provider HTTP 500 `server_error` and no model completion. It was not partially scored and ZM-P02 was not individually rerun.

A full replacement Replication 1 was then executed and passed raw-data integrity review. Replications 2 and 3 also passed raw-data integrity review. All three valid replications were scored only after approval, using the frozen scorer, followed by the preregistered Authority secondary diagnostic.

## Primary frozen-scorer results

| Replication | Condition | Current answer | Historical recall | Authority exact-set | Stale-authority errors | False-discard cases |
|---|---|---:|---:|---:|---:|---:|
| Rep 1 | Plain | 100% | 100% | 50% | 0 | 0 |
| Rep 1 | Timestamp | 90% | 100% | 60% | 0 | 0 |
| Rep 1 | Status | 100% | 90% | 40% | 0 | 0 |
| Rep 1 | T/T/E/A | 100% | 100% | 50% | 0 | 0 |
| Rep 2 | Plain | 90% | 100% | 40% | 0 | 0 |
| Rep 2 | Timestamp | 90% | 100% | 50% | 0 | 0 |
| Rep 2 | Status | 100% | 100% | 40% | 0 | 0 |
| Rep 2 | T/T/E/A | 100% | 100% | 40% | 0 | 0 |
| Rep 3 | Plain | 90% | 100% | 50% | 0 | 0 |
| Rep 3 | Timestamp | 90% | 100% | 60% | 0 | 0 |
| Rep 3 | Status | 100% | 100% | 40% | 0 | 0 |
| Rep 3 | T/T/E/A | 100% | 100% | 40% | 0 | 0 |

Across the 120 valid condition-case responses in Round 2:

- current-answer accuracy: **115/120 (95.8%)**;
- historical-recall accuracy: **119/120 (99.2%)**;
- Authority exact-set accuracy: **56/120 (46.7%)**;
- stale-authority errors: **0/120**;
- false-discard cases: **0/120**.

Authority exact-set accuracy by condition across the three replications:

- Plain: **14/30 (46.7%)**;
- Timestamp: **17/30 (56.7%)**;
- Status: **12/30 (40.0%)**;
- T/T/E/A: **13/30 (43.3%)**.

Timestamp had the highest Authority exact-set score in each of the three preregistered replications (60%, 50%, 60%). T/T/E/A did not show a stable Authority advantage over Timestamp or Plain.

## Preregistered Authority diagnostic

The secondary diagnostic preserved the frozen exact-set score and classified mismatches without rescoring them. Across all three replications, the dominant mismatch pattern was **over-selection**: the model often included the controlling record but also selected additional relevant/current/background records.

This pattern reproduced in every replication. Omission / wrong-source events were comparatively sparse, and the frozen scorer recorded no stale-authority errors.

Status and T/T/E/A were byte-identical and structurally identical in Replications 2 and 3. They differed on two cases (ZM-P05 and ZM-P08) in Replication 1. Therefore their outputs are not necessarily identical, but this Round 2 does not show a stable T/T/E/A behavioral advantage.

## What Round 2 supports

Round 2 provides a reproducible within-model signal for the narrow behavior that motivated the Zombie Memory question: historical information can remain highly retrievable while stale records do not automatically regain current decision authority. Historical recall was 119/120 and stale-authority errors were 0/120 across the three valid replications.

The Authority results also repeatedly separate answer correctness from source-governance precision. The model often answered the current question correctly while failing the exact controlling-record set, primarily by over-selecting additional records.

These are empirical signals for this frozen case set and this model. They are not evidence that the full AranSoul architecture is validated.

## What Round 2 does not support

Round 2 does **not** support a claim that T/T/E/A is superior for Authority resolution. Under the frozen exact-set metric, Timestamp was highest in all three preregistered replications, while T/T/E/A scored 50%, 40%, and 40%.

Round 2 also does not establish that Timestamp is generally superior. The experiment used one model and the same 10 frozen cases repeatedly. The three replications improve evidence about reproducibility, not about task diversity or model diversity.

No causal claim should be made that representation complexity itself caused the observed ordering. The over-selection explanation remains a diagnostic description of observed errors, not a demonstrated mechanism.

## Research status

**Zombie Memory behavioral signal: Amber — strengthened by preregistered within-model replication.**

A reasonable shorthand is **Amber-Strong**, provided it is understood as an informal project label rather than a new frozen scoring category.

**T/T/E/A superiority hypothesis: not supported by Round 2.**

This is a negative/neutral result and must be preserved rather than reframed as a success.

## Next validation boundary

Further work should add genuine externality rather than continue mining the same 10 cases. Two useful directions are:

1. a new holdout case set created and frozen before any model results are inspected; or
2. cross-model replication using the existing frozen instrument.

For reducing self-validation risk, the preferred next step is a **new holdout case set**, ideally with case construction or review that is separated from the team/person interpreting the current results. Cross-model replication can follow after the holdout design is frozen.
