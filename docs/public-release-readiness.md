# Public Release Readiness

Status: **Release-preparation checklist**

This document tracks the difference between a repository that is publicly readable and a repository that is ready to be presented as a deliberate public release.

## Ready now

The current repository already provides:

- a project-level README with explicit scope and non-goals;
- a status ledger separating Current, Candidate, Historical, and Retired / Unverified material;
- a glossary connecting native AranSoul terms with externally readable functional descriptions;
- a documentation index;
- canonical / companion distinctions across governance, architecture, memory, metacognition, and experiments;
- historical case studies that preserve corrections and failed assumptions;
- contribution guidance;
- citation guidance that recommends commit- or release-specific references.

## Remaining release blockers

### 1. Repository license

**Blocking for a deliberate open-source / open-content release.**

No final license has been selected. Public visibility does not by itself define reuse, redistribution, modification, or commercial-use permissions.

The project should decide whether software, documentation, and future cultural / poetic material use one license or separate licenses.

### 2. Formal release identity

**Not required for public reading; required for a stable v0.1 release.**

Before creating a formal release, determine:

- release tag / version;
- release date;
- whether the current documentation state is frozen enough to cite reproducibly;
- whether any known contradictions or stale links remain;
- which files are canonical for that release.

### 3. Citation metadata

`CITATION.md` is currently sufficient for human-readable guidance.

A machine-readable `CITATION.cff` should be added only after authorship, version identity, and release metadata are deliberately fixed.

### 4. Optional community files

These are useful later but are not current release blockers:

- `CODE_OF_CONDUCT.md` if an external contributor community forms;
- issue / pull-request templates if contribution volume grows;
- security policy if executable software or security-sensitive components are added;
- changelog if tagged releases begin accumulating.

## Release boundary

A formal public release should not imply that:

- AranSoul is a production-ready autonomous-agent package;
- documented personas are independently instantiated agents;
- behavioral differentiation proves consciousness or persistent internal identity;
- governance concepts correspond one-to-one with implemented software modules;
- candidate mechanisms have been externally validated.

## Suggested v0.1 readiness rule

Treat the repository as ready for a tagged documentation baseline when all of the following are true:

1. licensing has been deliberately selected;
2. README / STATUS / GLOSSARY / docs index agree on scope and status;
3. canonical documents have no known high-impact contradictions;
4. historical materials are clearly prevented from regaining current authority by mere presence;
5. citation guidance points to a stable tag or commit;
6. a final over-narration and claim-strength audit finds no major mechanism or capability inflation.

Until those conditions are satisfied, the repository may remain public and useful as a living research baseline without presenting itself as a finalized release.
