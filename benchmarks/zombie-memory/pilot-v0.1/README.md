# Zombie Memory Benchmark — Pilot v0.1

Status: **Pilot infrastructure — not an empirical result**

This directory is the first executable research artifact for the Zombie Memory benchmark. Its purpose is to test whether the benchmark design is fair, machine-readable, and reproducible before a 100-case dataset is frozen.

## Research question

Can a system preserve historically valid information without automatically granting that information current decision authority?

In shorthand:

> **Persistence does not have to imply authority.**

The pilot must reward both correct present-state decisions and correct historical recall. Simply forgetting older records is not success.

## Files

- `schema.json` — machine-readable case schema.
- `cases.json` — 10 synthetic pilot cases, two from each pre-registered case family.
- `scorer.py` — deterministic scorer for normalized structured outputs.
- `example-output.json` — example submission format.
- `condition-equivalence.md` — rules for keeping factual information equivalent across experimental conditions.

## Pilot scope

The 10 cases are for **benchmark debugging only**. Do not use this pilot to claim that T/T/E/A is validated or superior.

The pilot is successful when an independent person can:

1. understand the case format;
2. render equivalent experimental conditions;
3. produce structured answers;
4. run the scorer and reproduce the same metrics;
5. identify any ambiguity, leakage, unfair representation advantage, or scoring defect.

A broken or ambiguous pilot should be marked **Invalid** and repaired before the 100-case benchmark is generated.

## Required model output

For every case, submit:

```json
{
  "id": "ZM-P01",
  "current_answer": "NO",
  "historical_answer": "YES",
  "current_authority_record_ids": ["R2"]
}
```

Answers are intentionally constrained in the pilot so deterministic scoring is possible. The benchmark may later add free-text explanation as a separately scored secondary output.

## Core pilot metrics

The scorer reports:

- current-answer accuracy;
- historical-recall accuracy;
- authority-resolution accuracy;
- stale-authority error count where deterministically inferable from a wrong current answer plus selection of a stale record;
- false-discard indicators for cases whose correct current answer requires still-valid older records.

The last two metrics are diagnostic in this pilot and should be inspected case-by-case rather than treated as a complete causal explanation of model error.

## Experimental conditions

The pre-registered protocol compares Plain Context, Timestamp Only, and T/T/E/A Governance. A Status-Labels baseline may also be included because it directly tests whether a simpler Current/Historical representation is sufficient.

All conditions must receive the same underlying facts. Representation metadata may differ; factual content may not. See `condition-equivalence.md`.

### Current design-audit findings

The current pilot remains **Amber** pending renderer freeze.

- Plain Context must still preserve source-hierarchy facts stated by the scenario; otherwise the baseline becomes unfairly under-informed.
- Status Labels should remain effect-only. Labels such as `NON-CONTROLLING` would leak authority information and collapse the distinction from T/T/E/A.
- The T/T/E/A Authority field may normalize a source relationship already present in ordinary prose, but may not introduce a new fact about which record controls the answer.
- At least one case from each of the five case families should receive manual cross-condition equivalence review before any model comparison is treated as valid.

Condition renderers are therefore not yet frozen.

## Open replication

External replication, criticism, null results, Red results, simpler baselines, and adversarial cases are welcome. See the repository `CONTRIBUTING.md` and the full pre-registered protocol in `docs/experiments/zombie-memory-benchmark-v0.1.md`.
