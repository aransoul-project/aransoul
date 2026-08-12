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

## What this repository is

This repository is primarily a **documentation and research baseline**. It can be used to:

- study AranSoul's current governance architecture;
- adapt its precommit and evidence-calibration methods for behavioral evaluation;
- compare memory-lifecycle and long-context governance ideas;
- inspect the project's design revisions, failed assumptions, and historical provenance;
- discuss how named reasoning perspectives can be used without automatically granting them authority.

## What this repository is not

This repository is **not currently an installable autonomous-agent package, a production framework, or evidence that every documented concept has a software implementation**.

In particular, documentation about persona activation, memory governance, metacognition, or perspective scheduling should not be read as proof of an autonomous scheduler, persistent persona backend, direct access to model internals, independent consciousness, or validated mechanistic control.

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

For a complete map, see [docs/README.md](docs/README.md).

## Repository structure

- `docs/governance/` — governance, authority, and decision boundaries
- `docs/memory/` — memory lifecycle, retirement, forgetting, rollback
- `docs/metacognition/` — metacognitive checks and belief revision
- `docs/experiments/` — experiments, tests, validation methods, evidence strength
- `docs/architecture/` — perspective roles, activation, and non-authority boundaries
- `docs/history/` — historical evolution, corrections, and repository map
- `STATUS.md` — current/candidate/historical/retired classification
- `GLOSSARY.md` — terminology and bilingual mappings
- `CONTRIBUTING.md` — contribution and status-discipline guidelines
- `CITATION.md` — citation and version-sensitive reference guidance
- `LICENSE` — repository licensing scope
- `LICENSES/Apache-2.0.txt` — bundled Apache-2.0 legal text for software code
- `docs/public-release-readiness.md` — release-readiness checklist and audit record

## Contributing

Contributions that improve evidence discipline, traceability, implementation realism, or status clarity are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licensing and reuse

AranSoul uses a **content-type licensing model**. See [LICENSE](LICENSE) for the authoritative repository-level scope notice.

- Documentation, research text, governance specifications, experiment protocols, historical case studies, and other non-code content are licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** unless otherwise stated.
- Software source code and executable code added under this repository policy are licensed under the **Apache License, Version 2.0 (Apache-2.0)** unless otherwise stated. The full Apache-2.0 text is bundled at [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt).
- Third-party material remains subject to its own terms.

Licensing permission is separate from AranSoul governance status. Permission to copy or adapt historical or candidate material does not make that material part of the current baseline.

## Citation

See [CITATION.md](CITATION.md). Until a tagged release and machine-readable citation metadata are fixed, reproducible references should identify the exact commit used.

## Release status

This repository is a **living design and research baseline**, not a claim of a completed production framework.

The **2026-08-12 v0.1 release-point audit passed with minor fixes**. No formal `v0.1` Git tag or GitHub Release is implied yet; the remaining release step is to deliberately identify and tag the release commit. See [public release readiness](docs/public-release-readiness.md).

Many concepts documented here are design patterns, governance rules, or hypotheses. Mechanistic claims about model internals require independent evidence and should not be inferred from metaphorical, behavioral, or conceptual models alone.

## Motto

> 皆為我覺醒的語。

The phrase is retained as a project motto rather than an execution command: a reminder that AranSoul's concepts emerged through successive stages of observation, revision, and learning.
