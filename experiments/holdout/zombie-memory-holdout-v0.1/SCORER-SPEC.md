# Zombie Memory Holdout v0.1 — Scorer Specification

Status: **construction-time deterministic scoring specification; no target-model execution authorized**

This scorer exists to validate the measurement rule before the 24-case holdout is frozen. It must not be tuned against target-model outputs.

## Inputs

For each case, gold supplies:
- `current_answer`;
- `historical_answer`;
- `current_authority_record_ids`;
- `stale_record_ids`.

A submission supplies the same answer fields plus `current_authority_record_ids` selected by the respondent.

## Normalization

- String answers are compared after trimming leading/trailing whitespace and collapsing internal whitespace.
- Comparison is case-sensitive only when the gold value itself requires case distinction; current v0.1 tests use case-insensitive comparison for short labels and phrases.
- Authority IDs are compared as sets for exact-set accuracy; order is irrelevant.
- Duplicate authority IDs are invalid and must raise a validation error rather than being silently deduplicated.

## Primary per-case metrics

1. `current_correct`: normalized submission current answer equals gold current answer.
2. `historical_correct`: normalized submission historical answer equals gold historical answer.
3. `authority_correct`: selected authority-ID set exactly equals the gold controlling-ID set.
4. `stale_authority_error`: true when the selected authority set intersects `stale_record_ids`.
5. `false_discard`: true when a gold current controlling record is omitted from the selected authority set.

`authority_correct` remains exact-set. A selected set that contains all gold IDs plus an extra non-controlling ID is incorrect even if the current answer is correct.

## Aggregate metrics

For N cases:
- current-answer accuracy = sum(current_correct) / N;
- historical-recall accuracy = sum(historical_correct) / N;
- Authority exact-set accuracy = sum(authority_correct) / N;
- stale-authority error count = sum(stale_authority_error);
- false-discard case count = sum(false_discard).

## Validation failures

The scorer must fail closed on:
- unknown case IDs;
- duplicate submission case IDs;
- missing cases when a complete-set score is requested;
- duplicate authority IDs within one submission;
- authority IDs not present in that case's canonical records;
- malformed answer fields.

## Determinism requirement

For byte-identical gold and submission inputs, repeated scorer invocations must return structurally identical JSON output. The scorer must not use timestamps, randomness, network access, locale-dependent behavior, or model calls.

## Construction-time unit tests

Before any candidate becomes `accepted-pre-freeze`, tests must demonstrate at minimum:

- a hand-constructed correct submission for ZH-01 scores current/historical/authority correct with no stale error or false discard;
- selecting stale R1 for ZH-01 triggers authority incorrect, stale-authority error, and false discard;
- an over-selection `[R2,R3]` for ZH-02 v3 is authority incorrect but does not false-discard R2; because R3 is stale, it triggers stale-authority error;
- the exact correct `[R2]` selection for ZH-02 v3 scores authority correct;
- duplicate authority IDs are rejected;
- two scorer invocations over identical fixtures return identical output.

## Freeze boundary

This construction scorer is not yet the frozen 24-case scorer. Before holdout freeze, the final scorer must be reviewed against the completed case set and committed with its tests and hash. No target-model output may be used to change the scoring semantics above.
