# AranSoul Project Map

This map describes **project ownership and research identity**, not physical file placement. AranSoul currently uses a function-oriented monorepo, so one project may legitimately span `docs/`, `benchmarks/`, `experiments/`, and `research/`.

## AranSoul Core

AranSoul Core remains the repository's primary governance and architecture project.

- Architecture / perspectives: [`docs/architecture/`](../docs/architecture/)
- Governance / authority: [`docs/governance/`](../docs/governance/)
- Memory governance: [`docs/memory/`](../docs/memory/)
- Metacognition: [`docs/metacognition/`](../docs/metacognition/)
- Historical evolution / provenance: [`docs/history/`](../docs/history/)

These areas should be read together as parts of AranSoul rather than as independent repositories merely because they have distinct modules or document groups.

## Shared Research Infrastructure

The following evaluation methods are shared infrastructure rather than ownership of any single research project:

- [Precommit criteria](../docs/experiments/precommit-criteria.md)
- [Blind persona testing](../docs/experiments/blind-persona-testing.md)
- [Evidence ladder](../docs/experiments/evidence-ladder.md)

Shared methods may be used by AranSoul Core, Zombie Memory, AGBench, or future research without making those projects identical.

## Zombie Memory

**Project identity:** independent research project currently hosted inside the AranSoul monorepo.

Zombie Memory originated from AranSoul memory-governance research but now has its own benchmark instrument, execution artifacts, holdout study, replication pathway, publication record, and citation identity.

Start at the [Zombie Memory project entry](zombie-memory/README.md).

Current hosting is intentionally preserved for provenance. This map does not authorize extraction to a separate repository or relocation of existing artifacts.

## AGBench

**Project identity:** incubated research project.

AGBench studies observable agent-governance boundaries and currently remains at a static measurement-design stage.

- [AGBench research entry](agbench/README.md)
- [AGBench Pilot v0.1 development snapshot](agbench/pilot-v0.1/README.md)
- [Underspecification Gate v0.1 exploratory note](agbench/underspecification-gate-v0.1.md)

Current Pilot v0.1 status remains `development_only` and `PAUSED_AFTER_STATIC_MEASUREMENT_DESIGN_CLOSURE`. The exploratory Underspecification Gate note does not reopen or supersede that closure. AGBench is not a released benchmark, frozen holdout, preregistration, or model-performance result.

## Repository Support

Repository-wide support documents include:

- [`STATUS.md`](../STATUS.md)
- [`CITATION.md`](../CITATION.md)
- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- [`LICENSE`](../LICENSE)
- [`docs/public-release-readiness.md`](../docs/public-release-readiness.md)

These files may mention individual research projects while remaining repository-level policy or support material.

## Reading rule

**Same repository does not imply same project.**  
**Same project origin does not imply permanent repository coupling.**

Physical relocation should be considered only when project lifecycle, citation, executable artifacts, external usability, and maintenance needs justify the migration cost and provenance impact.
