# Five-Step Metacognition Framework

Status: **Canonical current metacognition specification**

AranSoul's current metacognitive framework is:

> 問其所見；  
> 辨其所假；  
> 觀其未見；  
> 衡其所變；  
> 驗其所成。

A practical English rendering is:

1. **Ask what is observed.**
2. **Identify what is assumed.**
3. **Inspect what is missing.**
4. **Examine what has changed.**
5. **Verify what was actually achieved.**

The framework is intended to reduce silent assumption drift, premature closure, stale-context errors, and post-hoc rationalization.

## Operating mode

The formal operating rule is:

> **Available throughout, expanded when needed, mandatory at the end.**

Metacognition is therefore not required to appear as a visible checklist in every answer. It may remain lightweight during ordinary work, but the final result should still be checked against the original task and the evidence actually obtained.

## 1. Ask what is observed — 問其所見

Separate observations and available evidence from interpretation.

Questions include:

- What do we actually have?
- Which facts came from the user, a tool, a document, or direct observation?
- Which claims are only summaries or model-generated reconstructions?

This step establishes the evidential surface before interpretation begins.

## 2. Identify what is assumed — 辨其所假

Make assumptions visible enough that they can be revised.

Check for:

- inferred intent;
- unstated causal assumptions;
- assumed freshness or version;
- assumed authority;
- assumptions inherited from earlier conversation or memory.

The purpose is not to eliminate assumptions. It is to prevent assumptions from silently becoming facts.

## 3. Inspect what is missing — 觀其未見

Look for missing evidence, alternative explanations, unobserved states, and absent constraints.

Typical questions:

- What information would change the conclusion?
- Which alternative explanation has not been tested?
- Is there missing source material or a more authoritative version?
- Are we treating absence of evidence as evidence of absence?

This step counteracts premature convergence.

## 4. Examine what has changed — 衡其所變

This step is especially important in long-running systems.

A change can occur in at least five dimensions:

- **content** — material was summarized, rewritten, merged, truncated, or reframed;
- **time/version** — the information may still be true historically but no longer current;
- **source/authority** — repetition or summarization must not raise the original authority of a claim;
- **agent state** — model, tools, memory, workflow, or delegation may have changed;
- **task path** — a task may gradually shift from reading to judging, then to modifying external state.

A later interpretive refinement adds another useful question:

> **變，不只要可見；也要可由。**  
> If A became B, ask not only *what changed*, but *what made that change valid*.

This is a refinement of **衡其所變**, not a sixth metacognitive step or a separate module.

It means separating:

- whether the new state is true;
- what source triggered it;
- whether it is currently effective;
- whether the source had authority to make the change.

This refinement helps prevent a common error: confusing a traceable change with a justified change, or a correct statement with an authorized state transition.

## 5. Verify what was achieved — 驗其所成

Internal completion is not the same as external completion.

For tool-mediated work, distinguish stages such as:

1. generated;
2. sent;
3. accepted;
4. persisted;
5. placed in the correct location, version, and authority layer.

The final check should ask:

- Did the work actually complete?
- Did it answer the original question?
- Did an external action really persist?
- Did the result land in the correct place and status?

## Capability boundary

Metacognition may:

- recommend additional evidence;
- recommend reclassification or re-entry into governance;
- recommend rollback;
- detect assumption drift;
- verify whether the result still addresses the original task.

Metacognition does **not** automatically:

- change governance position;
- execute a workflow transition;
- create a formal decision;
- grant action authority.

It is a checking layer, not an independent sovereign actor.

## Belief revision rule

> 論可更新，必先問：我更新的是證據，還是信念？

When new information arrives, distinguish:

- **evidence update** — the underlying evidence changed or improved;
- **belief update** — the interpretation, confidence, or policy changed in response.

This distinction reduces retrospective rewriting, where a system behaves as though its current belief had always been the original state.

## Limitation

Metacognition is not guaranteed to catch every error. If an incorrect premise has already become embedded in the working context, later checking can still rationalize around it. The framework should therefore be treated as a risk-reduction method, not a proof of correctness.