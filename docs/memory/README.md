# Memory

This directory covers memory as a governed lifecycle rather than an assumption that more retained context is always better.

## Current documents

- [Memory lifecycle](lifecycle.md) — admission, storage, retrieval, execution effects, propagation, forgetting, and rollback.
- [Zombie memory](zombie-memory.md) — historically valid material regaining present influence after losing current authority.

## Core distinction

AranSoul separates four questions that long-context systems often collapse:

- **Truth** — was the content supported or true?
- **Time** — when was it applicable?
- **Effect** — is it still in force?
- **Authority** — may it determine the present action?

Retrieval therefore does not imply promotion, and memory does not grant itself execution authority.

## Research scope

Candidate mechanisms may include retrieval-weight reduction, archival, scope restriction, deletion, or rollback. No memory mechanism should be described as validated solely because it is intuitively useful in conversation; candidate interventions should be tested against explicit failure conditions and alternatives.
