# Zombie Memory Preprint v0.1 — Release Checklist

Status: **publication-preparation checklist; not a publication claim.**

This checklist records the remaining release-facing work after the manuscript adversarial audits. It does not change the Holdout evidence, scorer, or results.

## Scientific-content status

The current manuscript audits found no remaining defect that requires a new live experiment. Before release, preserve the following evidence boundaries exactly:

- authority exact-set result: preregistered structured evidence;
- semantic current/historical equivalence: post-freeze measurement amendment;
- full authority-error taxonomy and stratified sample: exploratory;
- three live runs: within-protocol repeated executions, not independent external replication;
- pooled 288 responses: repeated observations over 24 distinct synthetic case units under four conditions and three executions, not 288 independent statistical samples;
- scorer chronology: record-level scoring expectations/fixtures were fixed before live execution, while the final fixture-derived executable scorer/scoring contract were committed later; preserve this implementation-timing deviation in the manuscript.

## Required human decisions before release

- [x] Publication name recorded as `康晉瑋` in manuscript author fields.
- [x] Final affiliation wording confirmed as `Independent Researcher`, with `AranSoul Project` as project context.
- [ ] Human-review every substantive claim, citation, table, and limitation.
- [ ] Confirm the final AI-assistance disclosure against the target preprint/venue policy.

## Bibliography normalization

- [ ] Record the arXiv version or verification date used for each evolving preprint.
- [ ] Re-check author order, title, identifier, and year immediately before release.
- [ ] Do not silently change Related Work positioning based on a title-only revision.

As checked on **2026-08-18**, the arXiv record for `2604.15774` displays:

**MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents**

If that record changes before release, cite the exact version used by the manuscript rather than relying on an unversioned title memory.

## Terminology cleanup for final formatting

- [ ] Prefer `24 distinct synthetic case units` over `24 independent synthetic cases` unless `independent` is explicitly defined as distinct case identity rather than statistical sampling independence.
- [ ] Keep `within-protocol replication` as the primary execution label.
- [ ] If `blind` is retained, use the manuscript's narrow procedural definition and do not imply conventional single-/double-blind design.
- [ ] Prefer `authority-set exactness`, `exact authority-set identification`, or equivalent wording over `precision` when `precision` could be misread as the formal information-retrieval metric.

## Reproducibility and artifact links

- [ ] Link the final manuscript to immutable versions of the preregistration, freeze artifacts, raw evidence archive, scoring contract, final audit, and replication kit.
- [ ] For a historical execution-ready public-benchmark prompt source, the replication kit documents commit `878b21f62faa9d999793b731198caac88a97bf62` in `PUBLIC-BENCHMARK-SOURCE.md`.
- [ ] Do not rely on mutable `main` as the sole publication artifact reference.

## Publication snapshot

Only after the manuscript and bibliography pass final acceptance:

1. choose the exact release commit;
2. create an immutable publication tag or equivalent release ref;
3. update manuscript artifact links to that snapshot;
4. run the final cold-start acceptance audit against the frozen snapshot;
5. do not change scientific content under the same release identifier after the snapshot is declared.

## Release criterion

The preprint package is ready to freeze when all remaining issues are publication mechanics or explicitly documented limitations, not unresolved empirical or provenance contradictions.
