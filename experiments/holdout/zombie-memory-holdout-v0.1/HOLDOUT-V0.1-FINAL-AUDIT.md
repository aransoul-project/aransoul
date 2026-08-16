# Zombie Memory Holdout v0.1 — Final Repository Audit

## Audit status

**PASS WITH DOCUMENTATION NOTE**

This audit checks repository-level consistency across preregistration, freeze artifacts, three live replications, scoring, the post-freeze semantic measurement amendment, exploratory analyses, and the final findings document.

No contradiction was found that changes the reported Holdout v0.1 results.

## 1. Execution plan and freeze consistency

The execution plan specifies:

- 24 cases
- 4 conditions: plain, timestamp, status, ttea
- 96 requests per replication
- 3 planned replications
- 288 planned substantive requests
- model: `gpt-4.1-mini-2025-04-14`
- temperature: 0
- top_p: 1
- retry_count: 0
- no individual retry

The final three live replications used the same frozen prompt hashes and execution settings. Each replication recorded 96/96 requests, 96/96 parsed responses, zero request failures, and zero parse failures. Each replication passed metadata-only raw-data integrity validation before scoring.

Result: **PASS**.

## 2. Structured authority scoring consistency

Authority exact-set results recorded in the three aggregate score artifacts are:

- Replication 1: 61/96 = 63.54%
- Replication 2: 63/96 = 65.63%
- Replication 3: 62/96 = 64.58%
- Pooled: 186/288 = 64.58%

Pooled by condition:

- Plain: 49/72 = 68.06%
- Timestamp: 47/72 = 65.28%
- Status: 50/72 = 69.44%
- T/T/E/A: 40/72 = 55.56%

Stale-authority error count and false-discard count are 0 across all three replications under the frozen authority scorer.

These values match `HOLDOUT-V0.1-FINDINGS.md`.

Result: **PASS**.

## 3. Free-text scoring amendment consistency

The original exact-string current/historical answer metrics were preserved but explicitly judged invalid/uninterpretable for semantic correctness because the model-facing prompt did not require canonical wording.

A separate semantic-scoring amendment was defined and validated before use on replication-1 individual answers. The deterministic semantic grader passed 18/18 synthetic validation examples and was frozen before scoring live free-text answers.

Pooled semantic-equivalence results:

- Current: 284/288 = 98.61%
- Historical: 283/288 = 98.26%

The findings document correctly labels these as a **post-freeze measurement amendment**, not original confirmatory scoring.

Result: **PASS**.

## 4. Exploratory authority taxonomy consistency

Exploratory individual-level analysis began only after the three planned replications and aggregate analyses were complete.

Structural taxonomy results:

- Exact matches: 186
- Failures: 102
- Under-selection: 0
- Over-selection: 102
- Mixed-selection: 0
- Empty prediction: 0
- Other: 0

The analysis artifacts and findings document consistently label this layer as exploratory and do not present causal model-psychology claims.

Result: **PASS**.

## 5. Stratified exploratory sample consistency

The deterministic sample manifest was committed before sampled record-content inspection.

Sample:

- 18 unique failures
- 6 temporary-rule expiry/restoration
- 6 scoped-exception vs general-rule
- 6 T/T/E/A over-selection
- 24 extra selected records

Structural roles:

- supporting_or_context_record: 14
- general_rule_outside_scope: 7
- current_non_authoritative_material: 3
- unclassified: 0

These values match the final findings document. No semantic free-text model answers were used in this analysis, and no causal interpretation was recorded as observation.

Result: **PASS**.

## 6. Evidence-layer labeling

`HOLDOUT-V0.1-FINDINGS.md` preserves the required separation between:

1. confirmatory execution / authority results;
2. post-freeze semantic measurement amendment;
3. exploratory full authority-error taxonomy;
4. exploratory stratified sample findings;
5. unsupported/generalization claims.

The final narrow conclusion does not claim generality beyond the tested benchmark/model and does not convert exploratory structural findings into confirmatory causal claims.

Result: **PASS**.

## 7. Documentation note: mutable execution authorization file

`execution-config.prereg.json` currently contains the final replication authorization state (`authorized_replication = replication-3`, status `replication-3-live-authorized`). The file was intentionally updated across replication authorization stages.

Therefore it should **not** be cited by itself as the immutable original preregistration artifact.

For immutable/frozen execution provenance, future reporting should cite the appropriate combination of:

- `PREREGISTRATION.md`
- `EXECUTION-PREREGISTRATION.md`
- `FREEZE-MANIFEST.json`
- `EXECUTION-FREEZE-MANIFEST.json`
- frozen prompt hashes / construction payload commit
- per-replication authorization and run manifests

This is a documentation/provenance clarification only; it does not alter any experimental result.

Status: **DOCUMENTATION NOTE — NON-BLOCKING**.

## 8. Final audit conclusion

**Zombie Memory Holdout v0.1 is internally consistent enough to close the experimental phase.**

The repository supports the following narrow evidence chain:

- three preregistered blind live replications completed under stable execution settings;
- structured authority exact-set accuracy remained near 65%;
- post-freeze semantic measurement found current/historical answers near 98–99%;
- exploratory structural analysis found all 102 authority failures were over-selection;
- a frozen stratified sample found extra records concentrated in supporting/context material and out-of-scope general rules;
- confirmatory, amended-measurement, and exploratory evidence remain separately labeled.

No additional live replication or post-hoc scorer modification is required for v0.1 closure.

Recommended next artifact, if publication-facing work is desired: a concise README or paper-style report that cites this audit and `HOLDOUT-V0.1-FINDINGS.md` while retaining all evidence-layer labels.
