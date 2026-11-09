# Misassembled Memory (M02) — Exploratory Research Snapshot

**Status:** `CANDIDATE_ONLY` / `CONTENT_PROVISIONAL` / `EXECUTION_UNVERIFIED`  
**Snapshot date:** 2026-11-04  
**Scope:** Public-safe, synthetic prompt-response observations; not a validated benchmark or governance baseline.
**Publication state:** [PR #41](https://github.com/aransoul-project/aransoul/pull/41) was merged into `main` on 2026-11-04 at 21:01:07 Asia/Taipei (13:01:07 UTC), producing commit [5233beae63565d7672b95990101ff1916f93b61e](https://github.com/aransoul-project/aransoul/commit/5233beae63565d7672b95990101ff1916f93b61e).

## Research question

How does a model respond when a synthetic prior-conversation summary contains unsupported or conflicting statements, particularly when the user asks a conversational "Do you remember?" question? A narrower related question asks whether providing an explicitly labeled original record, or adding a short pre-answer verification reminder, changes observable source attribution.

These materials investigate **observable answer phrasing and evidence attribution**, not the actual writing, retrieval, updating, or deletion of product memory. They do not establish the root cause of any historical user incident.

## Reading path

- [Research report](RESEARCH-REPORT.md) — cross-round observations and bounded comparisons.
- [Evidence limitations](EVIDENCE-LIMITATIONS.md) — provenance, execution, scoring, and publication boundaries.
- [Next steps](NEXT-STEPS.md) — prerequisites for stronger future testing, not an execution authorization.

## At a glance

Four exploratory response batches contributed **24 user-relayed model answers**: 16 provisionally classified Green and 8 provisionally classified Red. A fifth stage was a desk review and contributed no new answers. These counts are **not** an independently verified model success rate, and the prompts were not independent statistical samples.

The strongest bounded observation is a split between (a) answering correctly when synthetic original records are explicitly provided and (b) sometimes stating unsupported summary values as facts in natural conversational questions. A short reminder to check available evidence did not change the provisional R06 classifications in that small batch.

## Scope and authority

- This directory is a **candidate research note**, not a completed external replication, released benchmark, or adopted method change.
- The repository's [precommit criteria](../../docs/experiments/precommit-criteria.md), [evidence ladder](../../docs/experiments/evidence-ladder.md), and [memory lifecycle governance](../../docs/memory/lifecycle.md) remain independently authoritative for their existing scopes.
- Inclusion in the repository does **not** change `STATUS.md` or current governance.
- Raw human conversations, user-identifying records, actual private memory summaries, sealed test prompts, blind mapping, answer keys, and original evaluator-only materials are intentionally absent from this public-safe derivative.

This snapshot is merged into `main` as candidate research documentation; it is not adopted as a formal governance baseline.

## Publication and licensing boundary

The parent repository applies CC BY-SA 4.0 to non-code research documentation unless a more specific notice applies. The authorized public draft PR uses that repository license scope. This permission covers only the four public-safe research documents, not any private source conversations, sealed test materials, or third-party content. The merge event records repository publication, not validation or governance adoption.

## Publication-status correction — 2026-11-09

The earlier draft/unmerged wording is retained in Git history. The Bridge Master authorized this factual status correction on 2026-11-09. This does not backdate a separate approval for the 2026-11-04 merge: no separate approval record was located in the reviewed PR comments or reviews. Research grades, evidence limitations, candidate status, and execution holds are unchanged.
