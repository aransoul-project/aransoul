# AranSoul Documentation Index

This directory is the main documentation map for the current AranSoul public baseline.

The repository deliberately separates **current governance**, **evaluation methods**, **candidate research**, and **historical evidence**. A document being present does not by itself make its contents current policy.

## Governance

- [Governance index](governance/README.md)
- [Core flow](governance/core-flow.md)
- [Authority model](governance/authority-model.md)
- [Human authority](governance/human-authority.md)
- [External action verification](governance/external-action-verification.md)
- [Governance refinements](governance/refinements/)

## Memory

- [Memory index](memory/README.md)
- [Memory lifecycle](memory/lifecycle.md)
- [Zombie memory](memory/zombie-memory.md)

## Metacognition

- [Metacognition index](metacognition/README.md)
- [Five-step framework](metacognition/five-step-framework.md)
- [Rationalization risk](metacognition/rationalization-risk.md)

## Experiments / Validation

- [Experiments index](experiments/README.md)
- [Canonical precommit criteria](experiments/precommit-criteria.md)
- [Blind persona testing](experiments/blind-persona-testing.md)
- [Evidence ladder](experiments/evidence-ladder.md)
- [Zombie Memory independent replication protocol v0.1](experiments/zombie-memory-independent-replication-protocol-v0.1.md) — Candidate design for evaluation separation and future external replication; not a completed replication result
- [Zombie Memory replication kit v0.1](experiments/zombie-memory-replication-kit-v0.1/README.md) — Candidate handoff kit with preregistration, run-metadata, result-report, and evidence-label templates; no new replication result

### Zombie Memory Holdout v0.1

The completed Zombie Memory Holdout v0.1 studies whether a model can distinguish remembered or relevant records from the records that are currently authoritative.

Start with:

- [Research report](../experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md)
- [Findings and evidence layers](../experiments/holdout/zombie-memory-holdout-v0.1/HOLDOUT-V0.1-FINDINGS.md)
- [Final audit](../experiments/holdout/zombie-memory-holdout-v0.1/HOLDOUT-V0.1-FINAL-AUDIT.md)
- [Execution preregistration](../experiments/holdout/zombie-memory-holdout-v0.1/EXECUTION-PREREGISTRATION.md)
- [Benchmark design](experiments/zombie-memory-benchmark-v0.1.md)

The study contains three within-protocol replications (288 live responses total). Treat the confirmatory, post-freeze measurement-amendment, and exploratory evidence layers separately; the replications are not independent external validation.

The older `pre-registered-criteria.md` file is retained as provenance for the same methodological lineage and is not the canonical editing target.

## Architecture / Perspectives

- [Architecture index](architecture/README.md)
- [Perspective model](architecture/perspective-model.md)
- [Activation boundaries](architecture/activation-boundaries.md)
- [Perspectives](architecture/perspectives.md)
- [Zero and activation](architecture/zero-and-activation.md)

## History / Evolution

- [Repository map](history/repository-map.md)
- [Full expansion to selective activation](history/case-full-expansion-to-selective-activation.md)
- [Retention to zombie-memory governance](history/case-retention-to-zombie-memory.md)
- [Persona testing to blind audit](history/case-persona-testing-to-blind-audit.md)
- [Terminal-Bench mismatch](history/case-terminal-bench-mismatch.md)

## Public release / repository policy

- [Public release readiness](public-release-readiness.md)
- [Repository status ledger](../STATUS.md)
- [Glossary](../GLOSSARY.md)
- [Contribution guide](../CONTRIBUTING.md)
- [Citation guidance](../CITATION.md)
- [Repository licensing notice](../LICENSE)
- [Apache-2.0 full license text](../LICENSES/Apache-2.0.txt)

## How to read status

Use the repository-level [STATUS.md](../STATUS.md) before treating a concept as current, candidate, historical, retired, or unverified.

When two documents from different dates appear to conflict:

1. preserve both as provenance;
2. identify the authority and status of each source;
3. apply explicit later refinements where valid;
4. do not silently rewrite history to make the archive look consistent.

The goal is not a frictionless history. The goal is an auditable one.
