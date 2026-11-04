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

The four public-safe files were placed on a public draft PR after explicit human publication permission under the repository's CC BY-SA 4.0 documentation license. **Merge into `main` remains unapproved** and requires a separate human decision after diff review. That publication does not authorize R07, other experiments, or modifications to formal status files.
