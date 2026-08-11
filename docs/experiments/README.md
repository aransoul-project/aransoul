# Experiments

This directory contains evaluation methods, experimental protocols, and candidate research. It should remain distinct from the current governance baseline while still documenting methods that have already been adopted for testing.

## Current evaluation methods

- [Precommit criteria](precommit-criteria.md) — define objective, expected behavior, failure conditions, and alternative explanations before observing the result; classify outcomes as Green / Amber / Red / Invalid.
- [Blind persona testing](blind-persona-testing.md) — remove explicit role cues, anonymize outputs, and test whether behavioral distinctions remain observable.
- [Evidence ladder](evidence-ladder.md) — separate a test result from the strength of the experimental design that produced it.

## Candidate research

Examples include:

- context-reset / breathing mechanisms for long-run drift;
- memory retirement and rollback strategies;
- exchange stress tests across non-habitual domains;
- independent evaluation and cross-model replication;
- measurable cost/benefit criteria for multi-perspective activation.

## Interpretation rule

An experiment becoming interesting is not the same as an experiment becoming current policy.

Likewise, a Green result does not automatically establish a strong claim. Evidence strength depends on the design level, alternative explanations, replication, and independence of evaluation.

## Naming note

`precommit-criteria.md` is the canonical current entry for AranSoul's pre-registered behavioral-test criteria. The older `pre-registered-criteria.md` file is retained for provenance and points to the same methodological lineage.
