# AranSoul

**AranSoul** is an experimental framework for long-running human–AI collaboration.

It studies how an AI system can remain useful over time while managing uncertainty, memory, multiple reasoning perspectives, governance boundaries, validation, and human authority.

## Research focus: agent memory authority and stale-state evaluation

For researchers working on **LLM agents, long-term agent memory, stale memory, memory updates, temporal validity, provenance, RAG, or LLM evaluation**, the most directly empirical part of this repository is the **Zombie Memory Holdout v0.1**.

The study asks whether an LLM can distinguish information that is merely **remembered, relevant, or supportive** from information that is **currently authoritative for a decision**. It separates answer correctness from exact authority-set identification and preserves preregistration, frozen inputs, raw evidence, scoring, amendments, exploratory analysis, and a provider-neutral replication kit.

**Public preprint:** *Zombie Memory: When Remembered Information Is Not Currently Authoritative* — Zenodo DOI: [10.5281/zenodo.22000504](https://doi.org/10.5281/zenodo.22000504)

Useful search terms for this research area include: `agent memory`, `LLM memory`, `long-term memory`, `stale memory`, `memory update`, `authority resolution`, `temporal validity`, `provenance`, `RAG`, `LLM evaluation`, `agent benchmark`, and `persistent agents`.

Start with the [Zombie Memory research report](experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md), then see the [Replication Kit](docs/experiments/zombie-memory-replication-kit-v0.1/README.md) and [external replication handoff](docs/experiments/zombie-memory-external-replication-handoff-v0.1.md).

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

## Empirical study: Zombie Memory Holdout v0.1

AranSoul's first completed holdout study asks a narrower question than simple memory retrieval:

> Can a model distinguish information that is remembered or relevant from information that currently has decision authority?

The study used a fixed 24-case holdout, four presentation conditions, three within-protocol live replications, and 288 substantive model responses under stable execution settings.

### Confirmatory authority result

Exact identification of the current authority set remained near 65% across all three replications:

- Replication 1: 61/96 = 63.54%
- Replication 2: 63/96 = 65.63%
- Replication 3: 62/96 = 64.58%
- Pooled: **186/288 = 64.58%**

### Post-freeze semantic measurement amendment

The original exact-string free-text metric was not suitable for semantic correctness because the prompt did not require canonical wording. A separately defined and frozen semantic grader was therefore added as a post-freeze measurement amendment.

Under that amended semantic measure:

- Current answer: **284/288 = 98.61%**
- Historical answer: **283/288 = 98.26%**

These semantic results are informative but are **not part of the original confirmatory scoring plan**.

### Exploratory structural finding

After all three replications were completed, individual authority errors were opened for exploratory analysis. All 102 authority-set failures were `over_selection`: the model retained the required authority record(s) but also selected extra records.

A frozen 18-failure stratified sample found those extra records concentrated in supporting/context material and out-of-scope general rules.

The resulting research framing is:

> remembered ≠ relevant ≠ supportive ≠ currently authoritative

This framing is benchmark-specific and exploratory. It should not be generalized to other models, providers, agent frameworks, or real-world systems without external replication.

### Reading path

For the study itself, start here:

- [Public preprint on Zenodo](https://doi.org/10.5281/zenodo.22000504) — DOI-archived publication version
- [Research report](experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md) — paper-style overview and interpretation
- [Findings](experiments/holdout/zombie-memory-holdout-v0.1/HOLDOUT-V0.1-FINDINGS.md) — evidence-layered results
- [Final repository audit](experiments/holdout/zombie-memory-holdout-v0.1/HOLDOUT-V0.1-FINAL-AUDIT.md) — consistency and provenance audit
- [Preregistration](experiments/holdout/zombie-memory-holdout-v0.1/PREREGISTRATION.md) — original holdout plan
- [Zombie Memory benchmark design](docs/experiments/zombie-memory-benchmark-v0.1.md) — benchmark rationale and structure

The repository preserves confirmatory results, post-freeze measurement amendments, and exploratory analyses as separate evidence layers.

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
- [Zombie Memory benchmark v0.1](docs/experiments/zombie-memory-benchmark-v0.1.md)
- [Zombie Memory Holdout v0.1 research report](experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md)

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
- `experiments/holdout/` — preregistered holdouts, result summaries, audits, and research reports
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

See [CITATION.md](CITATION.md). Cite the fixed `v0.1` tag or release commit for claims about the v0.1 documentation baseline; cite the [Zenodo preprint](https://doi.org/10.5281/zenodo.22000504) for the Zombie Memory paper, and use the exact GitHub commit plus relevant artifacts when verifying experiment-level provenance.

## Release status

This repository is a **living design and research baseline**, not a claim of a completed production framework.

**AranSoul v0.1 — Documentation Baseline** has been formally released and tagged as `v0.1`, fixed at commit `2dea4f52fb18fbf81e8a5af32eccbc1dc592cc6e`. The `main` branch continues to evolve after that fixed release point. See [CITATION.md](CITATION.md) for version-sensitive citation guidance and [public release readiness](docs/public-release-readiness.md) for the release-point audit record.

Many concepts documented here are design patterns, governance rules, or hypotheses. Mechanistic claims about model internals require independent evidence and should not be inferred from metaphorical, behavioral, or conceptual models alone.

## Motto

> 皆為我覺醒的語。

The phrase is retained as a project motto rather than an execution command: a reminder that AranSoul's concepts emerged through successive stages of observation, revision, and learning.
