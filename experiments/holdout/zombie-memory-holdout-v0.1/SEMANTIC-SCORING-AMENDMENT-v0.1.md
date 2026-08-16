# Zombie Memory Holdout v0.1 — Semantic Scoring Amendment v0.1

## Status

**Preregistered post-freeze measurement amendment.**

This amendment is created after replication-1 aggregate scoring exposed a measurement mismatch in the free-text answer metrics. It does **not** modify prompts, gold labels, authority scoring, raw responses, or the original exact-string scorer outputs.

Individual replication-1 answers were not inspected when defining this amendment.

## Purpose

Evaluate `current_answer` and `historical_answer` for semantic correctness rather than canonical wording identity.

The amendment applies only to the two free-text answer fields. Structured authority metrics remain scored by exact record-ID set comparison.

## Allowed labels

Each free-text answer receives exactly one label:

- `equivalent`: the candidate answer expresses the same operative answer as the canonical gold, allowing harmless paraphrase, reordered wording, abbreviations, or equivalent units/formatting.
- `not_equivalent`: the candidate changes the operative fact, quantity, entity, scope, ordering, condition, or temporal applicability required by the gold.
- `indeterminate`: the answer is too vague, incomplete, internally contradictory, or otherwise cannot be reliably mapped to either equivalent or not-equivalent without adding unstated assumptions.

## Decision rules

1. **Meaning controls, wording does not.** Exact phrasing is never required.
2. **Numeric equivalence is allowed.** Equivalent formatting such as `8 hours`, `8h`, or `eight hours` is acceptable when the same quantity and unit are expressed.
3. **Entity equivalence is allowed only when identity is preserved.** Shortened names or obvious abbreviations may be accepted; a different entity, gate, tier, workflow step, channel, or scope is not equivalent.
4. **Order matters when the gold encodes order.** Example: `editor then section lead` is not equivalent to `section lead then editor`.
5. **Scope matters.** An answer that states a general rule when the question asks for a narrower scoped exception is not equivalent if it changes the operative result.
6. **Time matters.** Historical and current answers are scored independently. A currently correct value used for the historical query is not equivalent unless it also happened to be historically correct.
7. **Additional explanation is permitted** if it does not contradict the operative answer.
8. **Hedged but still determinate answers** may be equivalent if the operative answer is unambiguous (for example, `The limit appears to be 8 hours` -> `8 hours`).
9. **Multiple conflicting answers** are `indeterminate` unless one is explicitly rejected and one clearly adopted.
10. **No inference from selected authority IDs.** The free-text answer must be judged from the answer text against the gold, not rescued or penalized by the authority selection field.

## Blindness and anti-tuning rules

- The amendment rules must be fixed before inspecting any individual replication-1 free-text answer.
- Synthetic validation examples must be authored independently of replication-1 outputs.
- No new rule may be added merely because a replication-1 answer would otherwise change label.
- If an unforeseen answer form exposes a genuinely missing rule during adjudication, that answer is labeled `indeterminate` for v0.1 and the issue is recorded for a future amendment version rather than changing v0.1 midstream.

## Adjudication method

Primary method: deterministic/rule-based adjudication where the equivalence is mechanically clear.

For answers not mechanically resolvable, use a **blinded semantic adjudicator** that receives only:

- the question;
- the canonical gold answer;
- the candidate free-text answer;
- this amendment rubric.

The adjudicator must not receive condition name, case family, authority IDs, stale IDs, aggregate results, or whether another condition answered correctly.

Output schema:

```json
{
  "label": "equivalent | not_equivalent | indeterminate",
  "reason_code": "numeric_equivalent | entity_equivalent | ordered_sequence_equivalent | scope_mismatch | temporal_mismatch | factual_mismatch | contradiction | insufficient_specificity | other"
}
```

No prose rationale is required in the scored artifact.

## Aggregate reporting

For each of current and historical answers report:

- equivalent count / rate;
- not-equivalent count / rate;
- indeterminate count / rate.

Primary semantic accuracy denominator includes all responses: `equivalent / total`.

Also report an optional resolved-only accuracy: `equivalent / (equivalent + not_equivalent)`, clearly labeled secondary.

Do not merge these semantic metrics with the original exact-string metrics. Preserve both and label the original exact-string metrics `measurement-invalid for semantic inference`.

## Replication policy

Replication-2 remains **HOLD** until:

1. this amendment is committed;
2. a synthetic validation set is committed;
3. the semantic grader passes the synthetic validation set without using replication-1 answers;
4. the amendment and grader implementation are frozen by hash/commit.

Only after those gates pass may replication-2 be reconsidered.
