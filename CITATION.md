# Citing AranSoul

AranSoul is maintained as a **living documentation and research project** with stable public release points.

The first formal documentation baseline is **AranSoul v0.1 — Documentation Baseline**, published on **2026-08-13 (UTC+8)** and fixed at commit `2dea4f52fb18fbf81e8a5af32eccbc1dc592cc6e`.

## Recommended citation practice

When referring to the v0.1 project baseline as a whole, include:

- **Project:** AranSoul
- **Maintaining organization:** AranSoul Project (`aransoul-project`)
- **Repository:** `aransoul-project/aransoul`
- **Artifact type:** documentation / research baseline
- **Version:** `v0.1`
- **Release:** `AranSoul v0.1 — Documentation Baseline`
- **Release commit:** `2dea4f52fb18fbf81e8a5af32eccbc1dc592cc6e`
- **Release date:** 2026-08-13 (UTC+8)
- **Access date:** include the date on which you consulted the repository when required by your citation style

Release page: <https://github.com/aransoul-project/aransoul/releases/tag/v0.1>

For technical or research discussion, prefer citing the specific document that supports the claim—for example the governance core flow, memory lifecycle, metacognition framework, experiment protocol, or historical case study—rather than citing the repository generally.

## Citing Zombie Memory Holdout v0.1

**Zombie Memory Holdout v0.1 is a post-v0.1 research study.** It is not part of the fixed `v0.1` documentation-release contents merely because its study name also uses `v0.1`.

When citing results from this study:

- cite the exact post-release commit consulted rather than only the repository `v0.1` tag;
- prefer the study's `experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md` for the research narrative;
- use `HOLDOUT-V0.1-FINDINGS.md`, `HOLDOUT-V0.1-FINAL-AUDIT.md`, preregistration/freeze artifacts, and run/scoring artifacts when the claim requires the underlying evidence chain;
- preserve the study's evidence-layer distinctions: preregistered confirmatory results, post-freeze measurement amendment, and exploratory analyses should not be cited as though they had the same evidentiary status;
- describe the three completed live replications as **within-protocol replications**, not independent external replication.

For reproducibility, a citation to a numerical result should identify enough provenance to recover the exact report/artifact state, normally including the repository, document path, exact commit SHA, and access date where required.

## Version-sensitive citation

The `main` branch continues to evolve after v0.1. Claims about the v0.1 baseline should therefore cite the `v0.1` tag or its fixed release commit rather than the current `main` branch.

For work based on post-v0.1 changes that have not yet received another release tag, cite the exact commit SHA consulted.

A later version may refine terminology, status, or interpretation without erasing the historical state preserved by the v0.1 release.

## Licensing and citation are separate

Citation is a scholarly and provenance practice; licensing determines reuse permissions.

Repository-level licensing is defined in [LICENSE](LICENSE):

- documentation and non-code content are licensed under **CC BY-SA 4.0** unless otherwise stated;
- software code is licensed under **Apache-2.0** unless otherwise stated;
- third-party material remains subject to its own terms.

CC BY-SA 4.0 requires appropriate attribution for covered reuse. A citation may help satisfy scholarly attribution expectations, but users should consult the license terms for the legal attribution requirements that apply to their reuse.

## Machine-readable citation metadata

A `CITATION.cff` may be added in a later documentation update once the project deliberately fixes the remaining machine-readable authorship metadata. The absence of a CFF file does not change the stable identity of the v0.1 release.
