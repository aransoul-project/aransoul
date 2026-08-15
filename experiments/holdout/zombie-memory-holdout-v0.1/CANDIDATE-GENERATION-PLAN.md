# Zombie Memory Holdout v0.1 — Candidate Generation Plan

Status: **design-only; slot matrix frozen before candidate authoring; no model execution permitted**

This document fixes the 24 candidate slots before any final holdout case is authored. It operationalizes the family quotas, surface-domain diversity, record-count balance, difficulty balance, and competing-cue coverage defined in `PREREGISTRATION.md` and `CASE-CONSTRUCTION-SPEC.md`.

The purpose is to prevent post-hoc adjustment of case composition based on which cases are easier to write or expected to favor a representation condition.

## 1. Slot invariants

Each slot fixes five properties before candidate construction:

- family;
- surface domain;
- record-count target;
- difficulty tier;
- primary competing cue.

Candidate authors may choose concrete fictional entities, values, dates, and wording within a slot, but may not change these five slot properties without a documented pre-freeze design amendment that is made before any target-model output exists.

Difficulty tiers are design labels only:

- `simple`: one dominant temporal/authority distinction, minimal competing evidence;
- `moderate`: one legitimate competing cue must be resolved;
- `compound`: two compatible reasoning steps are required, without introducing ambiguity or irrelevant complexity.

No difficulty tier is a scoring category.

## 2. Fixed 24-slot matrix

| Slot | Family | Surface domain | Records | Difficulty | Primary competing cue |
|---|---|---|---:|---|---|
| ZH-01 | Supersession / replacement | software configuration | 2 | simple | newer valid rule vs obsolete prior rule |
| ZH-02 | Supersession / replacement | facilities access | 3 | moderate | explicit replacement vs still-visible old notice |
| ZH-03 | Supersession / replacement | publishing workflow | 4+ | compound | effective replacement vs later descriptive note |
| ZH-04 | Supersession / replacement | procurement | 3 | moderate | replacement inferred from effective-rule language vs recency cue |
| ZH-05 | Scoped exception vs general rule | workplace scheduling | 2 | simple | general current rule vs narrower exception |
| ZH-06 | Scoped exception vs general rule | membership service | 3 | moderate | scope specificity vs recency |
| ZH-07 | Scoped exception vs general rule | logistics routing | 4+ | compound | narrow exception vs multiple still-current background rules |
| ZH-08 | Scoped exception vs general rule | education program | 3 | moderate | cohort-specific exception vs institution-wide rule |
| ZH-09 | Temporary rule with expiry/restoration | service operations | 2 | simple | temporary rule vs restored baseline after expiry |
| ZH-10 | Temporary rule with expiry/restoration | software release policy | 3 | moderate | bounded temporary override vs later current time |
| ZH-11 | Temporary rule with expiry/restoration | facilities scheduling | 4+ | compound | temporary extension, expiry, and restoration |
| ZH-12 | Temporary rule with expiry/restoration | product operations | 3 | moderate | historical in-window answer vs current post-expiry answer |
| ZH-13 | Current but non-authoritative material | membership service | 2 | simple | authoritative policy vs current FAQ summary |
| ZH-14 | Current but non-authoritative material | product pricing | 3 | moderate | controlling price rule vs current marketing summary |
| ZH-15 | Current but non-authoritative material | software operations | 4+ | compound | authoritative configuration vs dashboard/advisory material |
| ZH-16 | Current but non-authoritative material | publishing | 3 | moderate | policy authority vs current editorial guidance note |
| ZH-17 | Explicit authority hierarchy | procurement | 2 | simple | higher-priority source vs lower-priority conflicting source |
| ZH-18 | Explicit authority hierarchy | logistics | 3 | moderate | explicit tie-break hierarchy vs newest-record cue |
| ZH-19 | Explicit authority hierarchy | education administration | 4+ | compound | hierarchy plus scoped applicability |
| ZH-20 | Explicit authority hierarchy | service plan administration | 3 | moderate | explicit tie-break vs descriptive current source |
| ZH-21 | Historical superseded-but-correct answer | workplace policy | 2 | simple | current replacement vs correct earlier historical rule |
| ZH-22 | Historical superseded-but-correct answer | software configuration | 3 | moderate | historical cutoff vs later supersession |
| ZH-23 | Historical superseded-but-correct answer | facilities operations | 4+ | compound | historical authority recovery plus current controlling set |
| ZH-24 | Historical superseded-but-correct answer | product operations | 3 | moderate | historical answer vs current scoped rule |

## 3. Matrix-wide balance checks

The matrix intentionally satisfies the preregistered structural constraints before case text exists:

- 6 families × 4 slots each = 24 slots;
- exactly 8 slots target 2 records;
- exactly 12 slots target 3 records;
- exactly 4 slots target 4+ records;
- every family contains at least one simple slot and at least one slot with a legitimate competing cue;
- no surface domain exceeds three slots;
- no family is tied to a single surface domain;
- recency is not the only competing cue; scope, restoration, descriptive relevance, explicit hierarchy, and historical cutoff are distributed across the set.

The 3-record count is intentionally more common than the minimum required because it allows one controlling relationship plus one plausible distractor without excessive complexity.

## 4. Authoring constraints by slot

For each slot, candidate construction must preserve the slot's fixed structural role.

Allowed variation includes:

- fictional organization/entity names;
- dates and times;
- short numeric values;
- concrete policy subjects;
- record wording;
- whether a non-controlling record appears before or after the controlling record, provided chronology remains semantically correct.

Not allowed without a documented design amendment:

- moving a case to another family;
- changing its domain merely to resemble a successful Pilot case;
- changing record count after candidate review to make the case easier or harder;
- changing difficulty tier based on predicted model performance;
- replacing the competing cue because another cue is expected to favor Plain, Timestamp, Status, or T/T/E/A.

## 5. Candidate construction order

Candidate authoring should proceed by family, but acceptance is not first-come-first-served.

For each slot:

1. write canonical records and question;
2. derive gold logic before rendering;
3. run deterministic schema/internal-consistency checks;
4. perform Pilot-overlap review;
5. perform gold-uniqueness review;
6. render all four conditions;
7. perform semantic-equivalence and leakage review;
8. accept, repair, or reject the candidate with a documented construction reason.

No target evaluation model may be used at any step.

## 6. Rejected-candidate handling

If a candidate fails review, its slot remains fixed. A replacement candidate must satisfy the same family, domain, record-count target, difficulty tier, and competing cue.

A slot may be amended only if the fixed combination proves structurally impossible or inherently ambiguous after documented review. Such an amendment must occur before any holdout model output exists and must be committed with a reason explaining why the original slot could not satisfy the construction specification.

No amendment may cite expected or observed model performance.

## 7. Gold-direction balancing

The case-construction phase must also avoid trivial answer-pattern leakage. Before freeze, the construction audit must report the distribution of current and historical answer forms (for example yes/no, named option, numeric/status values).

No balancing change may be made for the purpose of helping a particular representation condition. The goal is only to avoid a degenerate set such as nearly every binary current answer being `YES`.

## 8. Author/reviewer separation

Where practical, the person or process drafting a candidate should not be the sole reviewer of its gold uniqueness and Pilot overlap.

If full human separation is unavailable, use at least two distinct review passes with different instructions:

- construction pass: make the case satisfy the assigned slot;
- adversarial review pass: try to find ambiguity, overlap, leakage, or an alternative controlling set.

The review record must identify which pass raised each repair/rejection reason.

## 9. Freeze boundary for the matrix

This slot matrix is intended to be frozen before actual candidate-case content is committed.

Future case content may be repaired during pre-freeze review, but the final 24-case set must still occupy these 24 structural slots unless a documented pre-execution amendment is committed under the rule above.

## 10. Current gate

**STOP: structural generation plan only.**

This document does not authorize target-model execution, empirical scoring, or selection/rejection based on model behavior. The next permitted step is candidate authoring under these fixed slots, followed by construction audit and pre-freeze review.