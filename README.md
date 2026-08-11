# AranSoul

**AranSoul** is an experimental framework for long-running human–AI collaboration.

It studies how an AI system can remain useful over time while managing uncertainty, memory, multiple reasoning perspectives, governance boundaries, validation, and human authority.

AranSoul began as a poetic and multi-persona system. Over time, the project expanded into a broader investigation of:

- evidence thresholds and when a conclusion should be withheld;
- memory admission, revision, retirement, forgetting, and rollback;
- multiple reasoning perspectives without unnecessary noise;
- metacognition and post-hoc rationalization risks;
- governance of agent initiative and intervention thresholds;
- long-term drift, context accumulation, and historical traceability;
- falsifiable behavioral testing and evidence-strength calibration;
- preserving human final authority in collaborative AI systems.

## Project principle

AranSoul distinguishes between **what once existed**, **what is currently in use**, **what is still experimental**, and **what has been retired or remains unverified**.

Historical artifacts are preserved when useful, but their existence does not automatically make them part of the current system.

See [STATUS.md](STATUS.md) for the current baseline, [GLOSSARY.md](GLOSSARY.md) for terminology, and [docs/history/repository-map.md](docs/history/repository-map.md) for the relationship between this repository and earlier AranSoul-related projects.

## Core documentation

### Governance
- [Core flow](docs/governance/core-flow.md)
- [Authority model](docs/governance/authority-model.md)
- [Human authority](docs/governance/human-authority.md)
- [External action verification](docs/governance/external-action-verification.md)

### Memory
- [Memory lifecycle governance](docs/memory/lifecycle.md)
- [Zombie memory](docs/memory/zombie-memory.md)

### Metacognition
- [Five-step framework](docs/metacognition/five-step-framework.md)
- [Rationalization risk](docs/metacognition/rationalization-risk.md)

### Experiments and validation
- [Pre-commit criteria](docs/experiments/precommit-criteria.md)
- [Blind persona testing](docs/experiments/blind-persona-testing.md)
- [Evidence ladder](docs/experiments/evidence-ladder.md)

### Architecture / perspectives
- [Perspective model](docs/architecture/perspective-model.md)
- [Activation boundaries](docs/architecture/activation-boundaries.md)

### History / evolution
- [Repository map](docs/history/repository-map.md)
- [Full expansion → selective activation](docs/history/case-full-expansion-to-selective-activation.md)
- [Retention → zombie-memory governance](docs/history/case-retention-to-zombie-memory.md)
- [Persona testing → blind audit](docs/history/case-persona-testing-to-blind-audit.md)
- [Terminal-Bench mismatch](docs/history/case-terminal-bench-mismatch.md)

## Repository structure

- `docs/governance/` — governance, authority, and decision boundaries
- `docs/memory/` — memory lifecycle, retirement, forgetting, rollback
- `docs/metacognition/` — metacognitive checks and belief revision
- `docs/experiments/` — experiments, tests, validation methods, evidence strength
- `docs/architecture/` — perspective roles, activation, and non-authority boundaries
- `docs/history/` — historical evolution, corrections, and repository map
- `STATUS.md` — current/candidate/historical/retired classification
- `GLOSSARY.md` — terminology and bilingual mappings

## Status

This repository is a **living design and research baseline**, not a claim of a completed production framework.

Many concepts documented here are design patterns, governance rules, or hypotheses. Mechanistic claims about model internals require independent evidence and should not be inferred from metaphorical, behavioral, or conceptual models alone.

## Motto

> 皆為我覺醒的語。

The phrase is retained as a project motto rather than an execution command: a reminder that AranSoul's concepts emerged through successive stages of observation, revision, and learning.
