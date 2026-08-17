# Zombie Memory Holdout v0.1 — Full Freeze Audit

Status: **PASS for construction freeze; target-model execution remains unauthorized by this document**

Audit basis:
- frozen design baseline: `263a17d8e20f29ca9df7a90243d969134ae61052`;
- audited construction payload commit: `b33adb63a71ae34b90429d556a82eeee920b6b65`;
- audited payload tree: `4a2af8289909dc061ec196572a3af340bfafad4d`;
- target-model executions during construction: `0`.

## 1. Slot and family coverage

PASS.

- 24/24 frozen slots are populated.
- 6/6 preregistered families contain exactly 4 accepted pre-freeze cases.
- Accepted versions are ZH-01 v1; ZH-02 v3; ZH-03 v2; ZH-04 through ZH-24 v1.
- Rejected/repaired histories for ZH-02 and ZH-03 remain preserved and are not part of the accepted execution set.

## 2. Frozen matrix invariants

PASS by construction/read-back against `CANDIDATE-GENERATION-PLAN.md`.

- family × domain × record-count target × difficulty × primary competing cue remain assigned to the original 24 slots;
- record-count quota remains 8 two-record, 10 three-record, and 6 four-or-more-record slots;
- no slot was moved to another family after candidate review;
- no difficulty tier was changed based on model performance;
- no target-model output existed during candidate acceptance or repair.

## 3. Accepted-case artifact completeness

PASS after pre-freeze completeness repair.

Every accepted case now has:
1. canonical candidate JSON;
2. accepted construction audit;
3. four-condition render review;
4. deterministic scorer fixture.

Special accepted-version paths:
- ZH-02: `candidates/ZH-02/versions/v3/`;
- ZH-03: `candidates/ZH-03/versions/v2/`.

The audit initially found missing scorer fixtures for ZH-01 and ZH-02 v3. Both were added before freeze, without modifying candidate text, gold labels, rendering, scorer semantics, or using target-model output.

## 4. Construction gates

PASS for all 24 accepted cases.

Required accepted-case gates are recorded as passing:
- construction pass;
- adversarial review;
- schema check;
- frozen-slot match;
- gold uniqueness;
- Pilot-overlap review;
- semantic-equivalence review;
- leakage review;
- deterministic-scoring review.

## 5. Condition integrity

PASS.

Each accepted case contains Plain, Timestamp, Status, and T/T/E/A renderings. The construction reviews record that condition differences are representational grouping only: canonical content, time, lifecycle/status, effect, authority facts, current question, and historical question are preserved across conditions.

No gold answer, gold authority-record set, scorer label, expected condition ranking, or target-model-derived hint is intentionally introduced into one condition only.

## 6. Scorer semantics and lifecycle boundaries

PASS.

The deterministic scorer/fixtures preserve distinctions that are central to the benchmark:
- stale current authority vs historically correct old authority;
- current general rule vs narrower current exception;
- temporary override vs restored baseline;
- current but non-authoritative material vs stale material;
- current lower-priority authority vs stale authority;
- current different-scope authority vs controlling authority.

Notably, ZH-02 v3 canonical gold marks both the superseded directive R1 and its obsolete derived placard R3 as stale for the current query. Its repaired scorer fixture matches that canonical gold.

## 7. Gold-answer-form sanity check

PASS at the non-degeneracy level required before freeze.

The accepted set uses varied answer forms, including durations, counts, times, named gates/hubs/lanes, monetary thresholds/prices, capacities, and policy limits. The set is not a degenerate binary YES/NO benchmark and does not expose a single repeated answer direction that would trivialize evaluation.

This audit does not claim statistical balancing beyond the preregistered structural requirements.

## 8. Rejection and repair history

PASS.

Pre-freeze failures are retained rather than erased. In particular:
- ZH-02 v1 and v2 were rejected before v3 acceptance;
- ZH-03 v1 was rejected before v2 acceptance.

Reasons remain documented as construction/Pilot-overlap integrity issues rather than model-performance selection.

## 9. Execution boundary

PASS.

Construction audit state remains `target_model_execution_count = 0` for the accepted candidates. No holdout target-model result was used to author, repair, select, reject, score, or freeze the 24 accepted cases.

## 10. Freeze decision

**PASS: Zombie Memory Holdout v0.1 construction payload is freeze-ready at audited payload commit `b33adb63a71ae34b90429d556a82eeee920b6b65` / tree `4a2af8289909dc061ec196572a3af340bfafad4d`.**

The next research step must treat the frozen payload as immutable. Any future modification to accepted candidate content, gold, rendering semantics, or scorer semantics requires a new revision rather than silent mutation.

This freeze validates the integrity of the research instrument only. It does not validate the Zombie Memory hypothesis, the AranSoul architecture, or superiority of any representation condition.
