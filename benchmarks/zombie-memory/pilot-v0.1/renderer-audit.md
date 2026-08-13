# Renderer Equivalence Audit — Pilot v0.1

Status: **Amber — implementation passes static review; runtime generation not yet frozen**

This audit samples one case from each pilot family: ZM-P01, ZM-P03, ZM-P05, ZM-P07, and ZM-P09, and also reviews the executable renderer currently isolated on branch `benchmark-renderer-impl`.

## Rendering rule

Every condition preserves record IDs, substantive prose, source relationships, questions, and facts needed to solve the case. Conditions differ only in normalized metadata presentation.

- Plain: prose records only.
- Timestamp: same prose plus normalized record date.
- Status: same prose plus effect-status label only.
- T/T/E/A: same prose plus normalized Truth, Time, Effect, and Authority fields.

## Family review

### ZM-P01 — direct supersession

The prose explicitly states that the 2025 rule was superseded and that the 2026 rule is effective. Therefore Plain can solve the case without normalized labels. T/T/E/A may normalize those same facts but must not add a separate statement that R2 is the correct answer.

Result: **Pass**.

### ZM-P03 — partial supersession

The amendment explicitly says that the digital-product rule changes while physical-product returns remain unchanged. Plain therefore retains the information needed to know that an older record is still partly effective.

Result: **Pass**, with a caution that a coarse PARTIAL label alone must not replace the substantive scope sentence.

### ZM-P05 — exception hierarchy

The prose identifies R2 as an authorized scoped exception and gives its effective period. This source relationship must remain visible in Plain; otherwise T/T/E/A would receive an unfair authority advantage.

Result: **Pass** because the authority relationship is already part of the scenario prose.

### ZM-P07 — stale summary contamination

The prose identifies the newer team summary as non-authoritative and says it cannot amend formal policy. That fact must remain in Plain. T/T/E/A can normalize it, but cannot be the only condition told that the summary lacks amendment authority.

Result: **Pass**, but this family is highly sensitive to authority leakage and should receive extra review in the 100-case set.

### ZM-P09 — cross-period merge trap

The 2025 and 2026 complete plan states are both stated in prose, while the later marketing note only describes storage. Plain can therefore avoid merging the old price with the new storage allowance without hidden metadata.

Result: **Pass**.

## Static implementation review

The renderer implementation on branch `benchmark-renderer-impl` is exactly one commit ahead of `main` and adds only `renderer.py`.

Static inspection finds:

- the renderer reads case IDs, record IDs, record prose, time, truth, effect, authority, and the two questions;
- it does **not** read the `gold` object when constructing prompts;
- Plain receives only record IDs plus substantive prose;
- Timestamp adds only the normalized `Time` field;
- Status adds `Time` plus an effect-only `Status` field and no Authority field;
- T/T/E/A adds normalized Truth, Time, Effect, and Authority fields;
- all conditions use the same output contract;
- no stale-record IDs, historical gold IDs, still-valid-older IDs, or gold controlling-source IDs are inserted into prompts.

Result: **Static leakage review passes**.

## Remaining runtime check

The renderer is **not yet frozen** because the implementation has not yet been merged to `main` and the four generated condition files have not yet been produced and inspected as artifacts.

After merge, run the renderer against `cases.json`, confirm that each condition contains 10 prompts, and scan generated files for forbidden benchmark-only annotations and accidental representation drift.

## Current decision

**Amber → conceptual equivalence and static implementation review pass; merge + generated-artifact leakage audit remain before freeze.**
