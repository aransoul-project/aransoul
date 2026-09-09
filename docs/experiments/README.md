# Experiments

This directory contains evaluation methods, experimental protocols, interpretation frameworks, and project-specific research support. It should remain distinct from the governance baseline while still documenting methods that have already been adopted for testing.

## Shared evaluation methods and frameworks

These documents are reusable research infrastructure and are not owned by a single research project.

- [Precommit criteria](precommit-criteria.md) — **canonical current evaluation protocol**. Define objective, expected behavior, failure conditions, and alternative explanations before observing the result; classify outcomes as Green / Amber / Red / Invalid.
- [Blind persona testing](blind-persona-testing.md) — **current specialized protocol**. Remove explicit role cues, anonymize outputs, and test whether behavioral distinctions remain observable.
- [Evidence ladder](evidence-ladder.md) — **current interpretation framework**. Separate a run's result from the strength of the experimental design that produced it.

## EREQ candidate research companion

- [External Review Evidence Qualification (EREQ)](ereq/README.md) — v0.1–v0.13 semantic scorer development notes and the D03 integrated development regression, whose full-match gate was not met; includes local reviewer agreement, gold-support concerns, errata, and explicit evidence limits. This is not a validated benchmark, a complete scorer, or evidence of real-repository review capability. Historical protocol and provenance limitations remain explicit.

## Zombie Memory project-specific materials

The following files support the Zombie Memory research project rather than defining shared AranSoul evaluation methods:

- [Zombie Memory Benchmark v0.1](zombie-memory-benchmark-v0.1.md) — protocol for the original benchmark line.
- [Independent replication protocol v0.1](zombie-memory-independent-replication-protocol-v0.1.md) — candidate protocol for stronger evaluator separation and external replication.
- [Replication kit v0.1](zombie-memory-replication-kit-v0.1/README.md) — handoff materials and integrity tooling for replication.
- [External replication handoff v0.1](zombie-memory-external-replication-handoff-v0.1.md) — researcher-facing handoff that explicitly permits null, negative, contradictory, or Invalid outcomes.
- [External replication outreach template](EXTERNAL-REPLICATION-OUTREACH-TEMPLATE.md) — communication template for prospective external replication.
- [Preprint readiness audit](ZOMBIE-MEMORY-PREPRINT-READINESS-AUDIT.md) — audit for the publication pathway; not a new empirical result.

For the cross-directory project map, use the [Zombie Memory project entry](../../research/zombie-memory/README.md).

## Method status is not claim status

AranSoul distinguishes two questions:

1. **Is this evaluation method currently adopted?**
2. **Has the hypothesis being tested been strongly established?**

A method can be current while the claim it investigates remains candidate or weakly supported.

For example, blind testing is a current evaluation protocol. That does not mean stable cross-context persona identity has been established.

Likewise, the presence of a Zombie Memory protocol, replication kit, or outreach package does not by itself establish the hypothesis, complete an independent replication, or strengthen an empirical result beyond the evidence actually recorded.

## Candidate research and stronger evidence goals

Examples include:

- context-reset / breathing mechanisms for long-run drift;
- memory retirement and rollback strategies;
- exchange stress tests across non-habitual domains;
- independent evaluation and stronger evaluator separation;
- cross-context, cross-model, or cross-environment replication;
- measurable cost/benefit criteria for multi-perspective activation.

## Interpretation rule

An experiment becoming interesting is not the same as an experiment becoming current policy.

Likewise, a Green result does not automatically establish a strong claim. Evidence strength depends on design level, alternative explanations, replication, and independence of evaluation.

Green / Amber / Red / Invalid and the Evidence Ladder answer different questions:

- result class = performance against predefined criteria;
- evidence level = strength of design and isolation from competing explanations.

## Naming note

`precommit-criteria.md` is the canonical current entry for AranSoul's pre-registered behavioral-test criteria. The older `pre-registered-criteria.md` file is retained for provenance and already carries an explicit status notice; future edits should target the canonical file unless historical comparison is the purpose.
