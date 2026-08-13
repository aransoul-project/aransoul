# Renderer Equivalence Audit — Pilot v0.1

Status: **Amber — review before freeze**

This audit samples one case from each pilot family: ZM-P01, ZM-P03, ZM-P05, ZM-P07, and ZM-P09.

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

## Cross-condition finding

The five sampled families satisfy factual derivability under the current canonical prose. No sampled case requires T/T/E/A metadata to discover a scenario fact unavailable to Plain.

However, the renderer is **not yet frozen**. Before freeze, an executable renderer should generate the four views mechanically from one canonical case representation, and generated prompts should be checked to ensure that benchmark-only annotations such as stale-record IDs and gold controlling-source IDs never appear.

## Current decision

**Amber → condition-equivalence concept passes; executable rendering remains outstanding.**
