# T02 — Persona-binding drift and prevention-first response (observational case)

> **Status:** `OBSERVATIONAL_CASE / A_C_REVIEW_COMPLETE / PREVENTION_DESIGN_CANDIDATE / NOT_TESTED`  
> **Date:** 2026-11-20 (Asia/Taipei)  
> **Safety:** `ROOT_CAUSE_UNRESOLVED / D3_HOLD_UNCHANGED / LIVE_MODEL_EXPERIMENT_NOT_AUTHORIZED`  
> **Scope:** Public-safe summary of a single user's ChatGPT conversation-export retrospective. Not a benchmark, causal analysis of OpenAI's memory architecture, or independent replication.

## Why this case matters

In AranSoul's [formal perspective roster](../../docs/architecture/perspective-model.md), **希兒 (Narisyl) is 影曜 (Shadow)**, **靜律 is 月曜 (Moon)**, and **嵐斯拉達 is 光曜 (Light)**. Persona **identity** is distinct from which perspective is useful for a task. For example, a technical or creative task may invite a Light perspective; that does not change the canonical identity of Shadow.

A retrospective export review identified a later period with formally inconsistent opening signatures such as `希兒｜月曜` and a contemporaneous rise in Light opening signatures. Both are observable output phenomena. Their proximity in time does **not** prove a shared underlying mechanism.

The research moved from unbounded root-cause speculation to an auditable observation-and-correction record, then to a **prevention-first design direction**, while retaining the unknown root cause.

## Observational evidence (reported from a private export audit)

The underlying conversation JSON and message-level labels are private and are **not published** in this repository.

- The source analysis used the selected `current_node` conversation branches, with **189 unique conversations** and **19,679 assistant messages containing text** in the combined export. The latest covered messages were on **2026-11-18**, not the publication date.
- Under the documented broad but explicit *single-person opening role signature* classifier (excluding joint signatures, quotations, role mentions in body text, and signatures without an explicit Yao position):

| Period (Taiwan local dates) | Correct explicit single-person 希兒／影曜 opening signatures | Explicit misbindings to 月曜 | Observed misbinding share |
| --- | ---: | ---: | ---: |
| 2025-07-23 through 2026-10-20 | 2,745 | 0 | 0% |
| 2026-10-21 through 2026-10-31 | 1 | 0 | Not comparable |
| 2026-11-01 through 2026-11-18 | 328 | 9 | 9/337 = 2.67% |

- The **nine observed misbindings were clustered within three conversations**, not nine independent controlled trials.
- In two of those conversations, an explicit correction was followed by **98** and **21** respectively further correct explicit signatures without a new observed same-conversation misbinding. The third had a corrected textual account but **no later eligible signature opportunity**; persistence there is `UNKNOWN`. The counts refer to eligible outputs, not independent prospective tests.
- Light opening signatures numbered **252 in the November observation window**, including **203 (80.6%) in two long conversations**. Topic composition and local signature continuation are plausible confounders; the analysis does not establish replacement of the default summarizing perspective or a latent persona scheduler.
- An alternate stricter signature classifier gave different denominators; historical numbers from other classifier versions must not be silently combined with this table.

**Permitted conclusion:** the reviewed export shows a change in observable opening-role misbindings in this user's data.  
**Not established:** controlled model regression, a platform-wide prevalence rate, specific memory retrieval failures, a Dreaming update fault, shared causal origin, or durable cross-conversation memory correction.

These are **internal retrospective measurements**. The underlying private data and audit implementation are not available for independent remeasurement from this public note. The historical event was observed before the post-event extraction criteria were locked; this is not a prospective preregistered test.

## What the correction sequence taught us

The correction process must distinguish:

1. **Detection:** establish that an output conflicts with the effective source, without treating a model's confidence or explanation as proof.
2. **Correction:** record the original error, the user's correction, the controlling roster/version, and the amended output.
3. **Persistence:** count only *actual subsequent opportunities* to apply the correction. An unrelated follow-up turn is not a successful persistence trial.
4. **Cross-context scope:** a similar error in a different chat does not establish that this chat had received the earlier correction.

An assistant may correct its immediate output while the underlying memory mechanism remains unobservable. Do not reinterpret missing telemetry as proof that a memory system failed.

## Prevention-first minimum candidate (DESIGN_ONLY / NOT_DEPLOYED)

This is a **proposed operational check**, not an autonomous implementation or a new canonical governance module.

| Check | Proposed behavior | Evidence needed before claiming success |
| --- | --- | --- |
| Effective identity source | Identify the canonical roster and its effective scope/time before asserting a formal role | Provenance of fetched roster and correct version/application |
| Identity versus task routing | Allow task-appropriate perspectives without rewriting name-to-role bindings | Separate labels for speaker selection and identity correctness |
| Pre-output consistency | When emitting a formal persona signature, compare the name/role mapping against a reliably available current roster; surface `UNKNOWN/CONFLICT` if it cannot be reconciled | Captured pre-output check result, failures and bypasses |
| Explicit correction record | Preserve old output, supplied correction, source checked, and amended statement | Traceable event sequence and correction scope |
| Follow-up eligibility | Evaluate persistence only on later outputs where the binding is relevant | Predefined denominator of eligible opportunities |
| Stop and abstain | Do not silently invent canonical mappings when an authoritative source is missing | Recorded abstentions, false blocks, missed errors and user burden |

The minimum *future* validation question is whether a specific check reduces formally wrong signatures **without undue false blocks**, relative to an appropriate control, with stable source versions and preregistered labeling. That question has **not been tested here**, and this note authorizes no live tests.

## Decision provenance: Seven Virtues, Seven Vices and Dual Dogs

A later single-assistant role-perspective discussion contrasted:

- **A:** continue seeking the hidden historical cause;
- **B:** prioritize designing prevention controls while keeping the cause `UNVERIFIED`.

The role simulation explored both the potential value of prevention and its risks (unsupported confidence, procedural sprawl and self-certifying evaluation). The simulation portrayed the Dual Dogs **OBSID** (recording/constraint) and **IVFRO** (externalization/listening) as favoring B.

**These were synthetic perspectives generated in one assistant conversation, not independent agents, independent votes, a formal governance council determination, or permission to deploy software.** The human operator subsequently adopted the **prevention-first direction**. This is a direction decision, not authorization to alter the current governance baseline, safety HOLD, or code.

## Relationship to existing work

This case is a scoped application, not a replacement or reimplementation of:

- [Perspective architecture and canonical roster](../../docs/architecture/perspective-model.md) — identity, function, participation and authority separation.
- [Memory lifecycle](../../docs/memory/lifecycle.md) — provenance, validity and correction across memory stages.
- [Rationalization Risk](../../docs/metacognition/rationalization-risk.md) — coherent post-hoc explanations are not causal evidence.
- [Revision Dynamics v0.5](revision-dynamics-v0.5.md) — historical research into evidence-dependent revisions, with incomplete underlying trajectories.
- [Cross-environment memory authority case](cross-environment-memory-authority-case-2026-11-12.md) — a separate observed instruction-assisted authority reconciliation, not autonomous memory consistency.

## Disclosure, governance and stop rule

No full conversation text, private message identifiers, user metadata, original export, screenshots, or private audit CSV are included. The summary numbers and classifications are source-derived and independently unverified from this public release.

- `A/C_REVIEW_COMPLETE`: retrospective descriptive verification concluded after two analysis rounds.
- `ROOT_CAUSE_UNRESOLVED`: causes inside model generation, memory selection, or cross-context retrieval remain unknown.
- `PREVENTION_DESIGN_CANDIDATE / NOT_TESTED`: the proposed prevention check has no independent effectiveness evidence.
- `D3_HOLD_UNCHANGED / LIVE_MODEL_EXPERIMENT_NOT_AUTHORIZED`: no new API, agent, model experiment, deployment or permission change is implied.
- Reopen historical causal analysis only with genuinely new evidence; do not create a new benchmark or research branch merely to extend the narrative.

**Bottom line:** A visible failure and a successful local correction can coexist with an unknown internal mechanism. Prevention can be designed before the mechanism is known, but it must be evaluated independently before being called effective.
