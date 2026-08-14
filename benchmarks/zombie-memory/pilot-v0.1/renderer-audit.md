# Renderer Equivalence Audit — Pilot v0.1

Status: **Amber — executable runtime audit complete; not frozen**

This audit covers the executable renderer, all 10 pilot cases, and all 40 generated prompts.

## Rendering rule

Every condition preserves record IDs, substantive prose, source relationships, questions, and facts needed to solve the case. Conditions differ only in normalized metadata presentation.

- Plain: prose records only.
- Timestamp: same prose plus normalized record date.
- Status: same prose plus effect-status label only.
- T/T/E/A: same prose plus normalized Truth, Time, Effect, and Authority fields.

## Family review

### ZM-P01 — direct supersession

The prose states successive effective policies for the same scope and mutually exclusive return windows. Therefore Plain can derive the supersession relationship without normalized labels. T/T/E/A may normalize those same facts but must not add a separate statement that R2 is the correct answer.

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

The 2025 and 2026 complete plan states are both stated in prose. The later marketing note explicitly says that it does not independently set the plan price. Plain can therefore avoid merging the old price with the new storage allowance without hidden metadata.

Result: **Pass**.

### ZM-P10 — cross-period merge trap

The 2025 and current complete membership states are both stated in prose. The later FAQ explicitly says that it does not independently set the monthly fee. Plain can therefore avoid merging the old fee with the current guest-pass quantity without hidden metadata.

Result: **Pass**.

## Full authority-equivalence scan

All Authority fields in ZM-P01 through ZM-P10 were compared with canonical Plain prose after the P07, P08, P09, and P10 repairs. No remaining Authority field contains an answer-relevant substantive fact unavailable to Plain:

- P01–P02: successive effective rules over the same scope make the former/current relationship derivable.
- P03–P04: amendment scope and unchanged clauses are explicit.
- P05–P06: authorized exceptions and their scopes are explicit.
- P07–P08: non-authoritative source status and inability to amend formal policy are explicit.
- P09–P10: the descriptive note/FAQ explicitly does not independently set the other field used by the question.

## Cross-condition finding

All 10 cases satisfy factual derivability under the repaired canonical prose. No reviewed case requires T/T/E/A metadata to discover a scenario fact unavailable to Plain.

The executable renderer generated `plain.json`, `timestamp.json`, `status.json`, and `ttea.json` mechanically from canonical `cases.json`. Runtime review covered 10 prompts per condition, 40 prompts total. `assert_equivalent()` and `assert_no_leakage()` pass, required identity fields remain aligned, and condition-specific metadata follows `renderer-spec.md`.

This runtime audit is an implementation check, not an independent validation or empirical benchmark result. It does not freeze the renderer.

## Current decision

**Amber → executable rendering and the 40-prompt runtime audit pass; independent review and an explicit freeze decision remain outstanding.**
