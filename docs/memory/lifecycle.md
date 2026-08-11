# Memory Lifecycle Governance

AranSoul treats memory as governed state, not as an automatically trusted instruction channel.

The central principle is simple: **a memory may be true and still be stale, non-binding, out of scope, or unauthorized for the current action.** Retrieval therefore does not imply execution.

## Six lifecycle stages

### 1. Admission / Write
Before long-term admission, check:

- whether the information has durable value;
- provenance and date;
- sensitivity and authorization;
- whether it is fact, inference, hypothesis, preference, decision, or historical record;
- intended scope and expected lifetime.

One-off context should normally remain contextual rather than becoming durable memory.

### 2. Storage
Store materially different states separately. At minimum distinguish:

- current / formally effective;
- candidate / validation;
- historical;
- retained but non-authoritative material.

A newer note does not automatically supersede an older formal decision, and an archived artifact does not regain authority merely because it remains retrievable.

### 3. Retrieval
Retrieval should be conditioned on:

- the user's actual question;
- temporal relevance;
- current validity;
- source authority;
- task risk and scope.

Retrieval is selection, not promotion. A retrieved historical statement remains historical unless a valid governance decision changed its status.

### 4. Execution
Retrieved memory must not directly become an action command.

Before acting, re-check:

- current task position;
- governance depth;
- freshness;
- authorization;
- tool and system boundaries.

This separates **memory influence** from **execution authority**.

### 5. Sharing / Propagation
Expose only what is necessary for the current task. Avoid propagating sensitive information, stale rules, or unvalidated candidates as if they were current facts.

Summarization and repetition do not raise authority. In AranSoul terms: a statement may travel while its authority must remain attached to its original provenance and status.

### 6. Forgetting / Rollback
Forgetting is not limited to deletion. Available interventions include:

- lowering retrieval priority;
- removing an item from the active baseline;
- historical archival;
- restricting permitted uses;
- partial deletion;
- complete deletion;
- version rollback.

When the problem is interference from old material, prefer demotion or archival before destructive deletion. Irreversible deletion of core identity or major governance history requires elevated review.

## Four dimensions of memory validity

A useful memory check separates four questions:

| Dimension | Question |
| --- | --- |
| Truth | Was this content supported or true? |
| Time | During what period was it true or applicable? |
| Effect | Is it currently in force? |
| Authority | May it determine the present action? |

These dimensions prevent a common long-context failure: several individually true records from different periods being combined into a current state that never actually existed.

## Update discipline

> 論可更新，必先問：我更新的是證據，還是信念？

Updating evidence does not mean the previous historical record never existed. Updating a belief or policy must not be rewritten as though the system had always held the new position.

## Operational rule

**Memory can inform reasoning; memory cannot grant itself authority.**

This rule applies especially to long-running agents, where accumulated context can otherwise convert old assumptions, experiments, or superseded rules into silent present-day instructions.

## Status

The six-stage lifecycle and the separation of current, candidate, historical, and retained material are part of the current AranSoul governance baseline. More elaborate provenance chains, immutable audit trails, or automatic memory scoring remain implementation questions rather than established capabilities.
