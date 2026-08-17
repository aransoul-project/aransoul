# Zombie Memory Holdout v0.1 — Preprint Readiness Audit

Status: **Readiness audit only. This document does not submit or publish a preprint and does not change any research result.**

## Overall verdict

**AMBER — research core is mature; scholarly packaging is incomplete.**

The existing `RESEARCH-REPORT.md` already contains the essential research spine: a clear problem statement, benchmark design, execution settings, confirmatory result, post-freeze semantic amendment, exploratory error analysis, explicit unsupported claims, and reproducibility pointers. The main gap is not experimental evidence. It is positioning the work as a conventional scholarly artifact that a reader can discover, cite, compare against adjacent work, and attribute to named authors.

No additional live replication is required for preprint readiness. The present evidence boundary must remain unchanged.

## What is already preprint-ready

### Research question and abstract

The report already states a narrow, falsifiable question: whether a model can distinguish remembered/relevant/supportive information from records that currently possess decision authority. The abstract reports sample size, benchmark structure, confirmatory authority accuracy, amended semantic accuracy, exploratory over-selection, and a narrow interpretation.

### Experimental design and reproducibility

The report records the 24-case × 4-condition design, three planned within-protocol live replications, model snapshot, generation settings, retry policy, and raw-data integrity status. The repository contains preregistration, freeze manifests, frozen prompt hashes, run manifests, scorer, raw outputs, amendments, exploratory artifacts, final audit, replication kit, and external handoff.

### Evidence-layer discipline

The report clearly separates:

- preregistered confirmatory authority scoring;
- post-freeze semantic measurement amendment;
- exploratory error taxonomy and stratified inspection;
- unsupported causal/mechanistic/generalization claims.

This separation should be retained verbatim in any paper version.

### Limitations

The report already states that the work does not establish a T/T/E/A causal effect, universal over-selection, cross-model generality, production-agent safety, a unique ontology, or any hidden model mechanism.

## Blocking items before submission

### 1. Author and affiliation metadata

A preprint needs explicit authorship. The repository currently identifies the project but the research report does not provide a conventional author block, affiliation, corresponding-author contact, ORCID information, or contribution statement.

This is not an editorial detail that should be inferred automatically. The author list must reflect actual intellectual and experimental contributions and should be decided explicitly before submission.

### 2. Related Work section

The current report has no scholarly Related Work section. By 2026, several adjacent lines of work make this essential:

- stale-memory/state revision benchmarks such as **STALE**;
- long-term memory benchmarks with dynamic state tracking and premise awareness such as **LongMemEval-V2**;
- personalized-memory benchmarks that penalize obsolete-memory reuse such as **Memora/FAMA**;
- authority-preservation work at the memory-consolidation boundary such as **AuthMem-Bench / authority collapse**.

The paper should not claim that Zombie Memory uniquely discovered stale or authority-related memory failure. Its narrower distinction should instead be positioned explicitly:

> Zombie Memory Holdout v0.1 evaluates whether a model that can preserve both current and historical answers can identify the exact set of records that currently controls the decision.

This differs from, but is adjacent to, detecting invalidated state, preventing obsolete-memory reuse, tracking dynamic environment state, and preserving source authority during memory consolidation.

### 3. Formal references / bibliography

The report has no conventional reference list. A preprint needs citations for adjacent benchmarks, long-term-agent memory literature, stale/update handling, provenance/authority work, and any methodological tools whose concepts are relied on.

References must be checked against primary papers and exact publication/preprint metadata. Do not use repository prose or search-result snippets as the bibliography source.

### 4. Stable archival citation target

The repository already requests exact commit citation for post-v0.1 research. Before submitting a preprint, select and record one exact source commit containing the final paper-supporting artifacts. Ideally, the preprint should point to a fixed archival release/tag or DOI-backed archive rather than only mutable `main`.

This does not require changing the frozen Holdout evidence; it requires freezing the publication snapshot.

## Important items

### 5. Conventional paper structure

Convert the current report into a standard research-paper flow without changing evidence status:

1. Abstract
2. Introduction
3. Related Work
4. Problem Definition / Authority-Boundary Task
5. Benchmark Design
6. Experimental Setup
7. Confirmatory Results
8. Post-freeze Measurement Amendment
9. Exploratory Analyses
10. Discussion
11. Limitations
12. Reproducibility / Artifact Availability
13. References

The current material already covers most of these sections; the work is largely reorganization and contextualization.

### 6. Define the task formally

The report is understandable in prose, but a paper would benefit from a compact formal definition of:

- record set;
- current-authority gold set;
- current answer;
- historical answer;
- exact-set authority metric;
- over-selection / under-selection / mixed-selection categories.

The definition should describe the benchmark, not imply a general theory of model cognition.

### 7. Statistical presentation

The paper currently reports exact counts and proportions, which is appropriate and should remain primary. For scholarly presentation, consider adding uncertainty intervals for pooled and per-condition authority accuracy and clearly labeling analyses that are descriptive rather than inferential.

Do not add post-hoc significance claims merely to make the paper look more conventional. In particular, no causal condition effect should be claimed from the existing design without a separately justified analysis plan.

### 8. Methodological chronology

The semantic amendment is already documented correctly, but a paper should make the timeline visually obvious. A short table or figure could show:

- preregistration/freeze;
- three confirmatory runs;
- semantic amendment definition/freeze;
- semantic measurement;
- post-replication exploratory taxonomy;
- stratified exploratory inspection.

This would reduce the risk that readers mistake amended or exploratory results for preregistered confirmatory evidence.

### 9. Reproducibility statement

The paper should directly link or cite the following publication-snapshot artifacts:

- preregistration and execution preregistration;
- frozen prompt hashes and manifests;
- raw response archives;
- deterministic scorer and self-test;
- semantic amendment and validation;
- exploratory taxonomy artifacts;
- final audit;
- Replication Kit;
- External Replication Handoff.

State explicitly that the three completed runs are within-protocol replications and are not independent external replication.

## Nice-to-have items

### 10. One benchmark diagram

A single figure could show: historical/current records → four presentation conditions → model response → current/historical answer + authority set → separated evidence layers. This would make the task understandable without requiring readers to learn AranSoul terminology first.

### 11. One representative case

Include one synthetic benchmark example with its records, current/historical questions, and exact authority gold set. Avoid using the example to imply that all cases share the same mechanism.

### 12. Artifact badge / availability statement

Once a publication snapshot is fixed, add a compact artifact statement near the first page or end matter. A DOI-backed archive can be considered later, but is not required to draft the paper.

## Suggested scholarly positioning

The safest contribution framing is three-part:

1. **Task distinction:** separate answer correctness from exact current-authority identification in a memory-like multi-record setting.
2. **Behavioral observation:** on one fixed 24-case benchmark and one tested model snapshot, semantic answer correctness was near 98% under a post-freeze semantic measure while preregistered exact authority-set accuracy was 64.58% pooled.
3. **Open replication artifact:** publish the frozen evidence chain and provider-neutral replication kit so cross-model and independent external tests can confirm, narrow, or reject the phenomenon.

Avoid framing the paper as proving a universal "Zombie Memory" taxonomy, discovering the first stale-memory problem, or demonstrating a mechanism inside the model.

## Adjacent work that must be compared carefully

A future Related Work section should compare at least these current strands using their primary papers:

- **STALE (2026):** state resolution, premise resistance, and policy adaptation when later observations invalidate earlier memory.
- **LongMemEval-V2 (2026):** long-term environment experience including dynamic state tracking and premise awareness.
- **Memora / FAMA (2026):** personalized long-term memory with penalties for obsolete/invalidated-memory reliance.
- **AuthMem-Bench / Authority Collapse (2026):** preservation of source authority through memory consolidation and downstream authorization.

The most important distinction to articulate is that Zombie Memory Holdout v0.1 does not primarily test whether the old state is forgotten or revised at write time. It tests the decision-time boundary between information that remains remembered/relevant/supportive and information that belongs in the exact currently controlling authority set.

## Submission-readiness checklist

Before any preprint submission, require all of the following:

- [ ] Author list and contribution responsibility explicitly decided.
- [ ] Affiliation/contact metadata provided or intentionally stated as independent researcher/project affiliation.
- [ ] Related Work written against primary literature.
- [ ] Formal references/bibliography complete and verified.
- [ ] Paper structure converted from repository report to conventional scholarly form.
- [ ] Task/metric definitions stated compactly.
- [ ] Evidence chronology made explicit.
- [ ] Counts/proportions checked against frozen artifacts.
- [ ] No confirmatory/amendment/exploratory boundary drift.
- [ ] One exact repository publication snapshot selected.
- [ ] Reproducibility/artifact statement includes the replication kit.
- [ ] The manuscript never calls the three original runs independent external replication.
- [ ] Abstract/title avoid universal or causal claims.

## Final readiness judgment

**The study is ready to be converted into a preprint manuscript, but the current `RESEARCH-REPORT.md` should not yet be submitted as-is.**

The experimental record is sufficiently mature for manuscript preparation. The remaining work is primarily scholarly packaging, literature positioning, authorship metadata, and stable publication archiving—not another internal live experiment.
