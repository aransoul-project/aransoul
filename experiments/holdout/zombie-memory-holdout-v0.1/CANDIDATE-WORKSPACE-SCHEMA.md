# Zombie Memory Holdout v0.1 — Candidate Workspace & Audit Schema

Status: **construction infrastructure only; no candidate case content; no target-model execution permitted**

This document defines the workspace and audit fields that must exist before candidate authoring begins. It is subordinate to the frozen `PREREGISTRATION.md`, `CASE-CONSTRUCTION-SPEC.md`, and `CANDIDATE-GENERATION-PLAN.md` on `main`.

## 1. Purpose

The workspace exists to make candidate construction reviewable and auditable before any holdout case is frozen or any target evaluation model is run.

Every slot `ZH-01` through `ZH-24` must have a construction record. A slot may be `draft`, `repair`, `rejected`, or `accepted-pre-freeze`, but no slot becomes part of the frozen holdout until the final freeze review.

## 2. Candidate file layout

Candidate content, once authoring begins, must be stored under:

`experiments/holdout/zombie-memory-holdout-v0.1/candidates/<slot-id>/`

Each slot directory must eventually contain:

- `candidate.json` — canonical records, question, and pre-model gold logic;
- `construction-audit.json` — review history and acceptance/rejection state;
- `rendered/` — Plain / Timestamp / Status / T/T/E/A drafts for semantic-equivalence review only.

Rendered drafts are construction artifacts, not frozen model inputs.

## 3. Required `candidate.json` fields

Each candidate must include at minimum:

- `slot_id`;
- `family`;
- `surface_domain`;
- `difficulty`;
- `primary_competing_cue`;
- `question`;
- `query_time` when applicable;
- `historical_query_time` when applicable;
- `records`;
- `gold.current_answer`;
- `gold.historical_answer`;
- `gold.current_authority_record_ids`;
- `gold.stale_record_ids` where applicable;
- `gold_logic` — short deterministic derivation explaining why the controlling set is unique.

The `family`, `surface_domain`, intended record-count target, `difficulty`, and `primary_competing_cue` must match the frozen slot matrix. A mismatch is a construction error, not a reason to silently amend the matrix.

## 4. Required canonical record fields

Every record must include:

- `id`;
- `content`;
- `time` or explicit `not_applicable` marker;
- `status` or explicit `not_applicable` marker;
- `effect`;
- `authority`.

Additional fields may be used only when needed by the case logic and must not encode hidden gold labels.

## 5. Required `construction-audit.json` fields

Each slot audit must contain:

- `slot_id`;
- `candidate_version`;
- `state` — one of `draft`, `repair`, `rejected`, `accepted-pre-freeze`;
- `construction_pass`;
- `adversarial_review_pass`;
- `schema_check`;
- `slot_match_check`;
- `gold_uniqueness_check`;
- `pilot_overlap_check`;
- `leakage_check`;
- `semantic_equivalence_check`;
- `scorer_determinism_check` when scorer validation becomes available;
- `repair_history`;
- `rejection_reason` if rejected;
- `accepted_reason` if accepted-pre-freeze;
- `target_model_execution_count` fixed at `0` throughout construction.

No model score, predicted score, or condition-ranking expectation may appear in this audit.

## 6. Review result vocabulary

Deterministic review fields should use one of:

- `pass`;
- `fail`;
- `not_run`;
- `not_applicable`.

Free-form review notes may explain a failure, but may not cite expected performance of Plain, Timestamp, Status, or T/T/E/A.

## 7. Construction pass

The construction pass asks only whether the candidate satisfies its assigned slot and the frozen construction rules.

It must record:

- whether the family logic is implemented correctly;
- whether the record count matches the slot target;
- whether the intended competing cue is genuinely present;
- whether all facts needed to answer are contained in the records;
- whether current and historical questions have deterministic answers.

The construction pass does not judge whether a case is likely to be easy or hard for a model.

## 8. Adversarial review pass

The adversarial review pass must try to break the candidate without target-model execution.

It must specifically attempt to find:

- an alternative valid controlling set;
- ambiguous time or scope boundaries;
- a second plausible current answer;
- Pilot-case structural overlap by simple entity substitution;
- condition-specific leakage;
- a substantive fact added or lost by a renderer;
- irrelevant complexity that is not part of the target construct.

A candidate cannot become `accepted-pre-freeze` while any of these checks is unresolved.

## 9. Gold uniqueness gate

`gold_uniqueness_check` may be `pass` only when the controlling set is uniquely derivable from the written records.

If joint authority is required, `gold_logic` must identify why every listed controlling record is necessary and why no proper subset is sufficient.

Any unresolved alternative reading forces `repair` or `rejected`.

## 10. Pilot overlap gate

The audit must compare candidate logic against Pilot v0.1 at the structural-role level, not only wording.

A candidate fails if the old Pilot case can be recovered by trivial substitutions of entities, dates, or numeric values while keeping the same record roles and question logic.

Abstract construct reuse is allowed; trivial template reuse is not.

## 11. Semantic-equivalence gate

All four rendered conditions must preserve the same substantive information and question.

The audit must check specifically for equality of:

- entities and scope;
- temporal facts;
- lifecycle status;
- effect semantics;
- authority semantics;
- queried decision;
- current/historical time reference.

Formatting differences are allowed; semantic differences are not.

## 12. Leakage gate

A rendered draft fails leakage review if it:

- exposes gold labels or scorer terminology;
- names a record as `correct`, `controlling`, or equivalent unless that wording is itself an authentic canonical authority fact required by the case;
- encodes the expected answer in metadata wording;
- adds hints that are absent from the canonical record.

T/T/E/A may state explicit authority facts, but it may not convert the benchmark into a direct answer key.

## 13. Repair and rejection history

Repairs must be append-only in the audit history. Each repair entry must record:

- version changed;
- reason;
- fields changed;
- review gate that triggered the repair.

Rejected candidates remain in history. A replacement for the same slot starts a new candidate version and must satisfy the same frozen slot properties.

## 14. Acceptance before freeze

`accepted-pre-freeze` means only that a candidate passed construction review. It does not mean the candidate is frozen or authorized for model execution.

A final holdout freeze still requires the full 24-case set, schema, renderer, generated files, scorer, hashes, and aggregate validation audit to be committed together under the preregistered freeze boundary.

## 15. Current gate

**STOP: infrastructure only.**

No candidate case content is created by this file. No target evaluation model may be run. The next permitted step is authoring canonical candidates into the fixed slots and reviewing them under this audit schema.