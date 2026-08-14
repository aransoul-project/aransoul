# Zombie Memory Benchmark — Pilot v0.1

Status: **Frozen research instrument — not an empirical result**

This directory is the first executable research artifact for the Zombie Memory benchmark. Its purpose is to test whether the benchmark design is fair, machine-readable, and reproducible before a 100-case dataset is frozen.

The Pilot v0.1 research instrument was frozen after PR #1 merged into `main`. This freeze applies to the 10-case pilot dataset, four-condition renderer, generated prompts, deterministic scorer, and associated scoring semantics. Any later substantive change should use an explicit new revision rather than silently mutate Pilot v0.1.

The Zombie Memory / T/T/E/A research hypothesis itself remains **Amber / no empirical result yet**.

## Research question

Can a system preserve historically valid information without automatically granting that information current decision authority?

In shorthand:

> **Persistence does not have to imply authority.**

The pilot must reward both correct present-state decisions and correct historical recall. Simply forgetting older records is not success.

## Files

- `schema.json` — machine-readable case schema.
- `cases.json` — 10 synthetic pilot cases, two from each pre-registered case family.
- `renderer.py` — executable renderer for Plain, Timestamp, Status, and T/T/E/A conditions.
- `generated/` — 40 frozen model-facing pilot prompts, 10 per condition.
- `scorer.py` — deterministic scorer for normalized structured outputs.
- `test_scorer.py` — regression tests for scorer diagnostics.
- `example-output.json` — example submission format.
- `condition-equivalence.md` — rules for keeping factual information equivalent across experimental conditions.
- `renderer-audit.md` — renderer and condition-equivalence audit.
- `runtime-audit.md` — runtime artifact and scorer audit.

## Pilot scope

The 10 cases are for **benchmark debugging and pilot execution only**. Do not use this pilot to claim that T/T/E/A is validated or superior.

The pilot is successful when an independent person can:

1. understand the case format;
2. render equivalent experimental conditions;
3. produce structured answers;
4. run the scorer and reproduce the same metrics;
5. identify any ambiguity, leakage, unfair representation advantage, or scoring defect.

A later discovered defect should be documented explicitly. Substantive repairs should create a new revision instead of silently rewriting the frozen Pilot v0.1 instrument.

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
- false-discard indicators for cases whose wrong current answer is consistent with omitting a still-valid older record needed for correct reasoning.

The last two metrics are diagnostic in this pilot and should be inspected case-by-case rather than treated as a complete causal explanation of model error.

## Experimental conditions

The frozen pilot contains four conditions:

- Plain Context;
- Timestamp Only;
- Status Labels;
- T/T/E/A Governance.

All conditions receive the same underlying scenario facts. Representation metadata differs according to `condition-equivalence.md`.

### Freeze decision

The Pilot v0.1 instrument passed internal read-back review for:

- cross-condition factual equivalence;
- authority-fact equivalence;
- leakage prevention;
- executable renderer behavior;
- deterministic scorer behavior;
- gold smoke test;
- false-discard regression tests.

This is an **instrument freeze**, not independent validation and not a benchmark result.

## Open replication

External replication, criticism, null results, Red results, simpler baselines, and adversarial cases are welcome. See the repository `CONTRIBUTING.md` and the full pre-registered protocol in `docs/experiments/zombie-memory-benchmark-v0.1.md`.
