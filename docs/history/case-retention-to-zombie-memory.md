# Case Study: From Retention to Zombie-Memory Governance

## Original assumption

A natural early goal for long-running AI collaboration is to preserve as much context as possible. More memory appears to promise better continuity, less repetition, and a stronger sense of accumulated history.

## Observed problem

AranSoul later encountered a different class of failure: old information could remain retrievable after its original scope, status, or authority had changed.

The material was not necessarily false. It could be historically correct and still become harmful when:

- provenance was lost;
- date and version were detached from content;
- a candidate design was retrieved beside a formal baseline;
- archived material was treated as current instruction;
- several individually true records from different periods were combined into a state that never actually existed.

This led to the working term **zombie memory**: information that remains available and influential after the conditions that once gave it present authority have expired.

## Revision

AranSoul adopted a governed memory lifecycle:

1. admission / write;
2. storage;
3. retrieval;
4. execution;
5. sharing / propagation;
6. forgetting / rollback.

It also separates four questions that should not collapse into one another:

- Is the content true?
- When was it true or applicable?
- Is it currently effective?
- Does it have authority over the present action?

Forgetting was widened beyond deletion to include demotion, archival, retrieval-weight reduction, use restriction, partial deletion, and rollback.

## Current lesson

**Remembering more is not always equivalent to preserving continuity.**

Long-running systems need boundaries around what remembered material is allowed to do now.

## Still unresolved

AranSoul does not claim to have solved automated memory governance. Reliable provenance tracking, automatic stale-state detection, scoring, rollback semantics, and cross-system persistence remain implementation and research questions.
