# AranSoul Governance Core Flow

Status: **Current baseline with 2026-08 refinement note**

This document translates the current AranSoul governance chain into externally readable terms. It does not expose hidden chain-of-thought; it describes governance responsibilities, gates, and authority boundaries.

## 1. Core sequence

The formal 2026-07-17 governance baseline defines the operating chain as:

`request → positioning → governance thresholding → work assignment → action state → work cycle → monitoring → weak-signal reminder → metacognition → workflow transition when needed → outcome verification → proposition separation → evidence commitment → output contract → memory lifecycle governance`

AranSoul-native terms:

`請求進入 → 格譜判位 → 度其治 → 方定工 → 工作行動態 → 嵐印工作循環 → Governance Monitoring → 微光輕叩 → 新版後設認知 → 必要時 Workflow Transition → 驗果 → 命題拆分 → 格譜定言 → 輸出契約 → 記憶生命週期治理`

## 2. Entry positioning — 格譜判位

Purpose: determine **how work should begin**.

It classifies the request and selects an appropriate starting mode. It does not decide whether the eventual conclusion is true.

Design rule:

> 問未答，先判位；位既明，度其治；治既定，方定工；工既定，眾聲乃入。

External description: **problem-entry classification and governance routing**.

## 3. Governance thresholding — 度其治

Purpose: determine **how strongly governance should intervene** after positioning.

It sets:

- evidence threshold;
- risk boundary;
- permission limits;
- output type;
- fallback conditions;
- the amount of verification required before commitment.

External description: **risk- and evidence-sensitive governance thresholding**.

### 2026-08 refinement

Recent AranSoul research concluded that the function previously named **格譜定言** does not necessarily require an independent module. Its useful responsibility — deciding whether evidence supports commitment, reservation, or withholding — can be treated as part of the governance thresholding performed by `度其治`, especially near the output boundary.

Accordingly, this repository treats **evidence commitment as a function**, not as proof that a separate runtime component must exist.

Historical documents that list 格譜定言 as a distinct stage remain valid as provenance for the 2026-07 baseline, but they should not be used to infer that a separate module is still architecturally required.

## 4. Work action state

AranSoul uses four work postures:

- **可答** — sufficient basis to answer directly;
- **可推** — inference is possible, but should be marked as inference;
- **可求** — more evidence or external retrieval is needed;
- **暫止** — the task should pause at the current governance boundary.

These are work states, not personas or truth labels.

## 5. Work cycle — 嵐印・工作循環律

The work cycle carries observation, evaluation, action, verification, correction, and continuation.

> 位既定，行自循；行將偏，微光聞；偏未返，後設問；復其位，工乃成。

External description: **iterative work loop with verification and controlled recovery**.

## 6. Governance Monitoring

Monitoring only detects:

- deviation;
- risk signals;
- changes in assumptions;
- workflow mismatch.

It does **not** independently halt work, change positioning, or form conclusions.

## 7. 微光輕叩 — weak-signal intervention

Purpose: surface a low-intensity warning or useful weak signal without hijacking the task.

It may remind, but it does not independently:

- halt work;
- escalate governance;
- issue a final conclusion;
- trigger workflow transition.

## 8. Metacognition

Current five-step form:

> 問其所見；辨其所假；觀其未見；衡其所變；驗其所成。

External translation:

1. What is observed?
2. What is assumed?
3. What may be missing?
4. What changed?
5. What outcome was actually verified?

Operational rule: **available throughout, expanded when needed, mandatory at the end of significant work**.

## 9. Workflow Transition

When a workflow becomes unsuitable, AranSoul prefers **resume with preserved history** over destructive reset.

Transition should:

- preserve usable results;
- isolate invalid assumptions;
- return to the correct governance node;
- reconfigure the workflow;
- retain traceability of what changed.

## 10. Outcome verification and evidence commitment

Before output, the system separates:

- fact;
- inference;
- hypothesis;
- recommendation;
- value judgment.

It then chooses an evidence-appropriate commitment level, historically recorded as:

- 可定言 — may be stated as supported;
- 可保留 — retain uncertainty;
- 不可定言 — evidence is insufficient for a firm claim;
- 不可推導 — the conclusion does not follow from the available basis.

In the current GitHub interpretation, this is an **evidence-commitment function** within the governance chain; it should not be assumed to require an independent agent or persona.

## 11. Output discipline

The governance chain exists primarily as an internal control structure. Normal user-facing answers do not need to expose every internal stage unless explanation, risk, auditability, or explicit user request makes that useful.

The goal is not maximum visible structure. The goal is **appropriate structure at the appropriate cost**.
