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
- citation guidance that recommends commit- or release-specific references;
- a deliberate content-type licensing policy:
  - documentation and non-code content: **CC BY-SA 4.0**;
  - software code: **Apache-2.0**;
  - third-party material: original terms preserved.

## Remaining release blockers

### 1. Formal release identity

**Not required for public reading; required for a stable v0.1 release.**

Before creating a formal release, determine:

- release tag / version;
- release date;
- whether the current documentation state is frozen enough to cite reproducibly;
- whether any known contradictions or stale links remain;
- which files are canonical for that release.

### 2. Final release-point audit

Before tagging v0.1, run one final repository-wide check for:

- broken or stale internal links;
- inconsistent Current / Candidate / Historical / Retired labels;
- unresolved canonical / companion ambiguity;
- wording that inflates a design concept into an implemented capability;
- wording that turns poetic identity into a mechanistic claim;
- claims whose evidence level is stronger than the documented experiment supports;
- licensing scope conflicts or imported third-party material with unclear terms.

### 3. Citation metadata

`CITATION.md` is currently sufficient for human-readable guidance.

A machine-readable `CITATION.cff` should be added only after authorship, version identity, and release date are deliberately fixed.

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

1. licensing has been deliberately selected and documented;
2. README / STATUS / GLOSSARY / docs index agree on scope and status;
3. canonical documents have no known high-impact contradictions;
4. historical materials are clearly prevented from regaining current authority by mere presence;
5. citation guidance points to a stable tag or commit;
6. a final over-narration and claim-strength audit finds no major mechanism or capability inflation;
7. the release point has no known high-impact broken links or licensing-scope ambiguity.

Licensing is no longer a release blocker. The remaining work is release identity plus a final release-point audit before any v0.1 tag is created.
