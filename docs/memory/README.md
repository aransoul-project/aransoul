# Memory

This directory covers memory as a governed lifecycle rather than an assumption that more retained context is always better.

## Document authority

### Canonical governance specification

- [Memory lifecycle](lifecycle.md) — the current six-stage governance model for write, storage, retrieval, execution, sharing/propagation, and forgetting/rollback.

### Current risk concept / companion

- [Zombie memory](zombie-memory.md) — a current diagnostic concept for historically valid or once-authoritative material regaining present influence after its authority has expired.

`zombie-memory.md` explains a failure mode and mitigation logic. It does not by itself establish that AranSoul has an implemented autonomous memory-retirement engine.

## Core distinction

AranSoul separates four questions that long-context systems often collapse:

- **Truth** — was the content supported or true?
- **Time** — when was it applicable?
- **Effect** — is it still in force?
- **Authority** — may it determine the present action?

Retrieval therefore does not imply promotion, and memory does not grant itself execution authority.

## Governance policy vs implementation capability

The current governance baseline permits interventions such as:

- lowering retrieval priority;
- removing material from the active baseline;
- historical archival;
- restricting permitted use;
- partial or complete deletion;
- rollback.

These are **governance options**, not claims that every intervention is automatically implemented by a persistent memory backend.

Automated retrieval weighting, provenance scoring, archival pipelines, rollback engines, or autonomous lifecycle enforcement remain implementation candidates unless separately implemented and verified.

## Reading rule

When a memory document describes what the system *should do*, distinguish that governance rule from a claim about what the software *already does automatically*.
