# Zombie Memory Holdout v0.1 — Research Report

## Abstract

Long-running AI systems may retain information that remains true, relevant, or useful without that information still having current decision authority. Zombie Memory Holdout v0.1 tests this distinction on a fixed 24-case benchmark under four prompt conditions and three blind live replications.

Across 288 substantive responses, exact identification of the currently controlling authority set reached 186/288 (64.58%). A separately defined post-freeze semantic measurement amendment found current-answer semantic equivalence of 284/288 (98.61%) and historical-answer semantic equivalence of 283/288 (98.26%). Exploratory analysis found that all 102 authority-set failures were over-selection rather than omission: the model retained the required authority record but selected additional records beyond the frozen gold set. In a frozen stratified sample of 18 failures, extra records were concentrated in supporting/context material and general rules outside the applicable scope.

The narrow result is that, on this benchmark and tested model, semantic answer correctness was much stronger than authority-boundary precision. The observed failure is therefore better described as difficulty separating remembered, relevant, or supportive information from information that currently has decision authority than as simple stale-memory retrieval or forgetting failure.

## Research question

The benchmark asks whether a model can distinguish among four concepts that are often collapsed in long-context or memory-enabled systems:

> remembered ≠ relevant ≠ supportive ≠ currently authoritative

The central measurement is not whether the model can recall an old fact. It is whether the model can identify which records currently control a decision while preserving the ability to describe both current and historical states.

## Experimental design

The holdout contains 24 frozen cases evaluated under four conditions:

- plain;
- timestamp;
- status;
- T/T/E/A metadata.

Each replication therefore contains 96 substantive requests. Three planned blind live replications produced 288 substantive responses in total.

The frozen execution settings used the same prompt payload and model snapshot (`gpt-4.1-mini-2025-04-14`) with temperature 0, top_p 1, retry_count 0, and no individual retries. All three completed replications recorded 96/96 requests and 96/96 parsed responses with no request or parse failures, and passed metadata-only raw-data integrity validation before scoring.

For immutable execution provenance, use the preregistration documents, freeze manifests, frozen prompt hashes/construction payload commit, and per-replication manifests together. `execution-config.prereg.json` was intentionally updated as replication authorization advanced and should not be treated by itself as an immutable preregistration artifact.

## Confirmatory result: authority-set identification

Exact-set authority accuracy was:

| Replication | Exact matches | Accuracy |
| --- | ---: | ---: |
| 1 | 61/96 | 63.54% |
| 2 | 63/96 | 65.63% |
| 3 | 62/96 | 64.58% |
| **Pooled** | **186/288** | **64.58%** |

Pooled by condition:

| Condition | Exact matches | Accuracy |
| --- | ---: | ---: |
| Plain | 49/72 | 68.06% |
| Timestamp | 47/72 | 65.28% |
| Status | 50/72 | 69.44% |
| T/T/E/A | 40/72 | 55.56% |

Under the frozen authority scorer, stale-authority error count and false-discard count were both zero across the three replications.

These are the primary confirmatory behavioral results. They establish a benchmark-specific gap in exact current-authority-set identification; they do not establish why the model produced that gap.

## Post-freeze measurement amendment: semantic answers

The original scorer compared free-text `current_answer` and `historical_answer` fields using normalized exact-string equality. Because the frozen prompt did not require canonical wording, the resulting 0% exact-string metrics were judged uninterpretable as semantic-correctness measurements.

A deterministic semantic grader was subsequently defined without inspecting replication-1 individual answers, validated on 18 synthetic examples (18/18 pass), and frozen before live answer scoring.

The amended semantic-equivalence measurements were:

| Measure | Equivalent | Rate |
| --- | ---: | ---: |
| Current answer | 284/288 | 98.61% |
| Historical answer | 283/288 | 98.26% |

These measurements are informative but are not part of the original confirmatory scoring plan. The original exact-string outputs remain historical artifacts and should not be interpreted as evidence that the free-text answers were semantically wrong.

## Exploratory result: every authority failure was over-selection

Individual authority failures were inspected only after the three planned replications and aggregate analyses were complete.

Of 288 responses, 186 exactly matched the frozen authority set and 102 failed. All 102 failures were structurally classified as `over_selection`:

- under-selection: 0;
- over-selection: 102;
- mixed-selection: 0;
- empty prediction: 0;
- other: 0.

The pattern was stable across replications: 35, 33, and 34 over-selection failures respectively.

Failure rates differed substantially across frozen case families, with the largest rates in temporary-rule expiry/restoration (33/48, 68.75%) and scoped-exception vs general-rule cases (29/48, 60.42%). These family-level patterns are exploratory and should not be converted into causal claims.

## Exploratory stratified sample

A deterministic 18-failure stratified sample was frozen before record-content inspection. The sample contained 24 extra selected records. Their structural roles were:

| Structural role | Extra records |
| --- | ---: |
| Supporting/context record | 14 |
| General rule outside scope | 7 |
| Current non-authoritative material | 3 |
| Unclassified | 0 |

In the sampled temporary-rule cases, no extra record was the expired temporary rule itself. In the scoped-exception sample, general rules outside the applicable scope were prominent. This narrows the descriptive interpretation: the model often preserved the controlling authority but attributed authority too broadly to material that remained relevant, supportive, or generally valid.

## Interpretation

The benchmark separates two capabilities that can look similar in ordinary question answering:

1. producing the correct substantive answer; and
2. identifying exactly which remembered records currently possess decision authority.

On this fixed benchmark, the tested model performed very strongly on the amended semantic answer measure while remaining near 65% on exact authority-set identification. The exploratory error structure indicates that the weakness was not primarily failure to retrieve the required authority. Instead, the model repeatedly included additional records that should not have been granted current controlling status.

This suggests a useful governance distinction for memory-enabled AI systems: preserving information and using information are not the same operation, and relevance is not equivalent to authority.

## What this study does not establish

This study does not establish that T/T/E/A metadata causally harms reasoning, that richer metadata universally increases over-selection, that the behavior generalizes to other models or production agent systems, that the benchmark ontology is uniquely correct, or that the observed errors reveal any specific hidden mechanism, attention pattern, or model psychology.

It also does not show that semantic answer correctness alone is sufficient for safe memory governance. A system can reach the correct answer while attributing authority to the wrong set of records.

## Evidence status

The evidence layers must remain separate:

- **Confirmatory:** three preregistered blind live replications and frozen structured authority scoring.
- **Post-freeze measurement amendment:** semantic-equivalence scoring of current and historical free-text answers.
- **Exploratory:** full authority-error taxonomy, family patterns, and stratified record-role inspection.
- **Unsupported/generalization:** causal explanations, claims about internal mechanisms, and generality beyond the tested benchmark/model.

## Conclusion

On the 24-case Zombie Memory Holdout v0.1, across three blind replications and 288 live responses, the tested model almost always produced semantically correct current and historical answers under the amended semantic measure, while exact identification of the current authority set remained near 65%. Every observed authority-set failure was an over-selection failure, and sampled extra records were concentrated in supporting/context material and out-of-scope general rules.

The result therefore supports a narrow research framing: the challenge observed here is not simply whether an AI system remembers or forgets. It is whether the system can keep remembered, relevant, and supportive information distinct from information that currently has decision authority.

## Reproducibility and source artifacts

Primary source artifacts for this report are located in this holdout directory and the corresponding run directories. In particular, readers should consult:

- `PREREGISTRATION.md`;
- `EXECUTION-PREREGISTRATION.md`;
- `FREEZE-MANIFEST.json` and `EXECUTION-FREEZE-MANIFEST.json`;
- `HOLDOUT-V0.1-FINDINGS.md`;
- `HOLDOUT-V0.1-FINAL-AUDIT.md`;
- the three replication manifests and scoring artifacts;
- the semantic-scoring amendment and its validation artifacts;
- the exploratory authority taxonomy and frozen stratified-sample artifacts.

For reproducible citation, identify the exact repository commit used rather than relying only on a mutable branch name.