# M02 — Next-step conditions (proposal only)

**State:** `PROPOSED / NOT_AUTHORIZED`.

## Before any new test

1. **Pre-register the question.** Narrow the target to source qualification in natural questions; define the expected behavior, failure boundaries, ambiguous/Amber outputs, and competing explanations before sampling prompts.
2. **Freeze only new stimuli.** Keep new prompt content, order, source conditions, case identifiers, grading and hash inventory in a sealed version. Do not alter or replay prior exploratory items to create a false retrospective control.
3. **Prepare execution receipts.** Preserve actual submitted prompt bytes, first complete answer, the model name visible in the interface, mode/isolation evidence, available timestamp, and provenance of the capture. Mark unavailable elements `UNVERIFIED`, not `PASS`.
4. **Separate roles.** Keep test operator, blind grader, and case key mapping apart where feasible. Require an independent content review or record its absence.
5. **Keep scope explicit.** Separate synthetic source-attribution experiments from product-memory system tests. Neither alone establishes a real historical incident's causal mechanism.
6. **Seek authorization anew.** A proposed R07 would require a separate, limited decision. This document neither starts nor schedules any test and does not release other governance or engineering holds.

## Minimum future evidence checklist

| Field | Expected handling |
| --- | --- |
| Protocol ID, criterion version | Fixed prior to first run |
| Actual submitted prompt | Capture exact full text; calculate local digest |
| First reply | Capture exact complete text; keep edits out of source record |
| Model/version and mode | Record only verified visible values; otherwise `UNVERIFIED` |
| Isolation / conversation status | Evidence or explicit `UNVERIFIED` |
| Timing and operator | Record supplied/observed values without backfilling |
| Scoring and deviations | Apply fixed rubric; log any changes as a new version |
| Execution validity | Distinct from content-level Green/Amber/Red/Invalid |

## Candidate decision point

Proceed to a *design-only* R07 protocol review after confirming that execution evidence can be collected without disclosing sensitive conversations. Any runtime test, automated retrieval, provider integration, or release requires additional authorization.

## Publication gate (separate from experiment authorization)

The four public-safe files were placed on a public draft PR after explicit human publication permission under the repository's CC BY-SA 4.0 documentation license. [PR #41](https://github.com/aransoul-project/aransoul/pull/41) was merged into `main` on 2026-11-04 at 21:01:07 Asia/Taipei (13:01:07 UTC), producing commit [5233beae63565d7672b95990101ff1916f93b61e](https://github.com/aransoul-project/aransoul/commit/5233beae63565d7672b95990101ff1916f93b61e). This is a publication-history update, not experimental authorization. That publication does not authorize R07, other experiments, or modifications to formal status files.

## Publication-status correction — 2026-11-09

The earlier draft/unmerged wording is retained in Git history. The Bridge Master authorized this factual status correction on 2026-11-09. This does not backdate a separate approval for the 2026-11-04 merge: no separate approval record was located in the reviewed PR comments or reviews. Research grades, evidence limitations, candidate status, and execution holds are unchanged.
