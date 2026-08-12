# Zombie Memory

Status: **Current memory-governance risk concept / diagnostic companion**

**Zombie memory** is AranSoul's working term for information that remains available and influential after the conditions that once gave it authority have expired or changed.

It is not necessarily false memory.

A zombie memory may be historically accurate, emotionally meaningful, technically interesting, or once formally valid. The failure occurs when retrieval silently restores **present authority** that the item no longer has.

## Typical formation pattern

1. A rule, assumption, persona behavior, experiment, or design is recorded.
2. The system later changes, narrows, replaces, or retires it.
3. The old material remains searchable or is summarized into another context.
4. Provenance, date, status, or scope is lost.
5. The old item is retrieved alongside current material.
6. The model treats coexistence in context as evidence of equal validity.
7. A hybrid state is produced that may never have existed historically.

## Why this matters

Long-term memory systems often optimize for retention and retrieval. AranSoul treats **selective non-use** as equally important.

The danger is not only forgetting useful information. It is also remembering too much without preserving the boundaries that explain what each memory is allowed to mean now.

## Detection questions

When an old memory affects a current conclusion, ask:

- Is the content true?
- When was it true?
- Is it still effective?
- What superseded or limited it?
- Does its source have authority over this task?
- Was the item retrieved because it is relevant, or merely because it is semantically similar?
- Would combining it with other retrieved items create a state that never existed?

## Preferred governance response

Do not default to deletion.

Use the least destructive intervention that restores the boundary:

1. label status and provenance;
2. lower retrieval priority;
3. remove from the active baseline;
4. archive as history;
5. restrict allowed uses;
6. delete only when justified;
7. rollback when a later change itself was invalid.

These are governance responses. This document does **not** claim that AranSoul currently has an autonomous memory engine that can perform every response automatically.

## Relationship to history

AranSoul deliberately preserves historical artifacts. Historical preservation and current authority are separate concerns.

This repository therefore uses status distinctions such as `CURRENT`, `CANDIDATE`, `HISTORICAL`, and `RETIRED / UNVERIFIED`. The purpose is not to erase earlier AranSoul designs, but to prevent archive presence from becoming accidental governance.

## Generalizable hypothesis

For long-running AI systems, the difficult memory problem may shift from **"Can the system remember?"** toward **"Can the system preserve provenance, status, and useful forgetting well enough that remembering does not corrupt the present?"**

This is a design hypothesis, not a claim that AranSoul has solved machine memory or forgetting, and not a claim that the term `zombie memory` is an established external research taxonomy.
