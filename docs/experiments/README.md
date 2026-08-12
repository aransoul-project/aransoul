# Experiments

This directory contains evaluation methods, experimental protocols, interpretation frameworks, and candidate research. It should remain distinct from the governance baseline while still documenting methods that have already been adopted for testing.

## Current methods and frameworks

- [Precommit criteria](precommit-criteria.md) — **canonical current evaluation protocol**. Define objective, expected behavior, failure conditions, and alternative explanations before observing the result; classify outcomes as Green / Amber / Red / Invalid.
- [Blind persona testing](blind-persona-testing.md) — **current specialized protocol**. Remove explicit role cues, anonymize outputs, and test whether behavioral distinctions remain observable.
- [Evidence ladder](evidence-ladder.md) — **current interpretation framework**. Separate a run's result from the strength of the experimental design that produced it.

## Candidate experiments

- [Zombie Memory Benchmark v0.1](zombie-memory-benchmark-v0.1.md) — **pre-registered candidate experiment** testing whether explicit Truth / Time / Effect / Authority representation reduces stale-authority errors relative to plain-context and timestamp-only baselines. No empirical result has been claimed yet.

## Method status is not claim status

AranSoul distinguishes two questions:

1. **Is this evaluation method currently adopted?**
2. **Has the hypothesis being tested been strongly established?**

A method can be current while the claim it investigates remains candidate or weakly supported.

For example, blind testing is a current evaluation protocol. That does not mean stable cross-context persona identity has been established.

Likewise, the Zombie Memory benchmark protocol can be pre-registered before any result exists; the protocol's presence is not evidence that T/T/E/A will outperform simpler baselines.

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

`precommit-criteria.md` is the canonical current entry for AranSoul's pre-registered behavioral-test criteria. The older `pre-registered-criteria.md` file is retained for provenance and points to the same methodological lineage.
