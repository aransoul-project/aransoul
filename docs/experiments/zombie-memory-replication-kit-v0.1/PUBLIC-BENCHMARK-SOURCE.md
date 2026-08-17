# Zombie Memory Replication Kit v0.1 — Recommended Public Benchmark Source

Status: **replication handoff guidance; not a new research result.**

For a public-benchmark reproduction that reuses the original frozen generated prompts, use an exact Git source commit that contains both the four generated prompt arrays and `generated/prompt-hashes.json`.

## Recommended historical execution-ready source

The earliest convenient execution-ready source currently recommended for prompt-payload recovery and hash verification is:

`878b21f62faa9d999793b731198caac88a97bf62`

Commit message:

`experiment: validate Holdout execution dry run`

At that commit, the repository recorded a complete 96-request dry-run with zero live API calls and documented the four prompt SHA-256 values. The dry-run audit states that the generated prompt hashes matched and that the 96 `(case_id, condition)` pairs were complete.

A replicator may instead preregister a later immutable commit or publication tag, provided that the frozen prompt payload and hashes verify identically. Do not select an earlier construction-only commit that predates the generated prompt arrays or hash manifest and then interpret verifier failure as a benchmark change.

## Verification

After choosing and preregistering the exact source ref, run:

```text
python docs/experiments/zombie-memory-replication-kit-v0.1/verify_frozen_hashes.py --ref <exact-source-commit-or-tag>
```

For the historical execution-ready source above:

```text
python docs/experiments/zombie-memory-replication-kit-v0.1/verify_frozen_hashes.py --ref 878b21f62faa9d999793b731198caac88a97bf62
```

A PASS verifies the repository-byte SHA-256 values for the four generated prompt artifacts against `generated/prompt-hashes.json`.

## Scope of this recommendation

This source recommendation is specifically about recovering and verifying the original public benchmark prompt payload. It does not imply that every later research artifact already existed at this historical commit. In particular, the completed-study repository later added the fixture-derived executable Holdout scorer/scoring contract and publication-facing documentation. For scoring provenance, follow the precedence and chronology described in `IMPLEMENTATION-GUIDE.md` and the completed Holdout research archive.
