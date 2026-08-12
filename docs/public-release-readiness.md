# Public Release Readiness

Status: **v0.1 release-point audit passed with minor fixes — formal tag not yet created**

Audit date: **2026-08-12**

This document tracks the difference between a repository that is publicly readable and a repository that is ready to be presented as a deliberate public release.

## Ready now

The current repository provides:

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
  - third-party material: original terms preserved;
- the full Apache-2.0 license text bundled under `LICENSES/Apache-2.0.txt`.

## 2026-08-12 final release-point audit

The final pre-release audit checked:

- repository root and recursive documentation tree;
- README / STATUS / GLOSSARY / docs-index agreement;
- canonical / companion / refinement labels;
- major internal navigation paths exposed by README and docs indexes;
- Current / Candidate / Historical / Retired wording;
- over-narration and persona-to-mechanism inflation risks;
- distinction between evaluation method status and research-claim strength;
- licensing scope and availability of the Apache-2.0 full text.

### Audit result

**No known high-impact contradiction, broken primary navigation path, authority inversion, or major capability-inflation problem remains.**

Minor issues corrected during the audit:

1. `STATUS.md` now distinguishes the **v0.1 documentation baseline candidate** from a formal Git tag / GitHub Release.
2. The full Apache-2.0 text is now bundled locally for future software-code distribution.
3. `docs/README.md` now includes release, citation, contribution, and licensing references.

The CC BY-SA 4.0 documentation license remains identified through the repository licensing notice and the canonical Creative Commons license URI.

## Remaining release blocker

### Formal release identity

The remaining step before a stable v0.1 release is to create the release identity deliberately:

- choose / confirm the tag name (`v0.1` is the current candidate);
- set the release date;
- identify the exact commit to tag;
- optionally add machine-readable `CITATION.cff` once authorship and release metadata are deliberately fixed.

No tag should be inferred merely from the words `v0.1` appearing in documentation.

## Optional community files

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

## v0.1 readiness rule

The repository is ready for a tagged documentation baseline when all of the following are true:

1. licensing has been deliberately selected and documented;
2. README / STATUS / GLOSSARY / docs index agree on scope and status;
3. canonical documents have no known high-impact contradictions;
4. historical materials are clearly prevented from regaining current authority by mere presence;
5. citation guidance points to a stable tag or commit;
6. a final over-narration and claim-strength audit finds no major mechanism or capability inflation;
7. the release point has no known high-impact broken links or licensing-scope ambiguity.

Conditions 1–4, 6, and 7 are satisfied at the 2026-08-12 audit point. Condition 5 becomes fully satisfied when the formal release tag is created and citation guidance can point to it directly.
