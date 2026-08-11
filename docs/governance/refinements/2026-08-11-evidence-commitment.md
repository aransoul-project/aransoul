# 2026-08-11 Refinement — Evidence Commitment and 格譜定言

Status: **Current refinement note**

## Background

The formal AranSoul governance baseline published on 2026-07-17 documented `格譜定言` as a distinct stage after outcome verification and proposition separation.

Later research recorded on 2026-08-11 concluded that the main useful function of 格譜定言 is not the existence of a separate module, but the act of calibrating **how strongly the system may commit to a conclusion given the available evidence**.

## Refinement

The continuing function is:

**evidence commitment / conclusion-strength calibration**

This includes distinguishing whether a proposition may be:

- stated as supported;
- retained with uncertainty;
- withheld because evidence is insufficient;
- rejected because it cannot be derived from the available basis.

## Architectural consequence

This function may be absorbed into `度其治` as part of evidence-sensitive governance near the output boundary.

Therefore:

- the function remains current;
- the historical term `格譜定言` remains valid for provenance;
- a separate runtime module named 格譜定言 is **not architecturally required**;
- older documents that show 格譜定言 as an independent stage should be read as historical/formal baseline structure, not as proof that the independent module must remain permanent.

## Governance principle

AranSoul should preserve historical structure without allowing historical structure to silently regain present authority.

This refinement is a concrete example of that principle: the responsibility is retained while the unnecessary structural duplication is allowed to converge.
