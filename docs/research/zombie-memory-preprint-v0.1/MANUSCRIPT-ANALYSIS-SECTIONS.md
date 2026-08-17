# Zombie Memory Preprint v0.1 — Analysis Sections Draft

This file contains the manuscript-ready draft for the post-freeze measurement amendment, exploratory analysis, discussion, and limitations. It must be integrated into `MANUSCRIPT-DRAFT.md` without changing the evidence status of any result.

## 7. Post-Freeze Measurement Amendment

### 7.1 Why the original free-text metric was not semantically interpretable

The frozen scorer compared `current_answer` and `historical_answer` using normalized exact-string equality. The prompt contract, however, did not require canonical wording. A semantically correct answer could therefore differ from the frozen gold string while expressing the same substantive result.

The resulting exact-string outputs were consequently judged unsuitable for semantic-correctness interpretation. They remain preserved as historical scorer artifacts, but they are not used to support a claim that the model's free-text answers were semantically incorrect.

### 7.2 Amendment procedure

A deterministic semantic-equivalence grader was defined after freeze as a measurement amendment. The amendment was specified without inspecting replication-1 individual answers, validated on 18 synthetic examples with 18/18 pass, and frozen before scoring the live free-text responses.

Because this measurement was not part of the original confirmatory scoring plan, its results are reported separately and are not promoted into preregistered confirmatory evidence.

### 7.3 Semantic-equivalence results

Across all 288 responses, the amended semantic measurements were:

| Measure | Equivalent | Rate |
| --- | ---: | ---: |
| Current answer | 284/288 | 98.61% |
| Historical answer | 283/288 | 98.26% |

By replication:

| Replication | Current | Historical |
| --- | ---: | ---: |
| 1 | 95/96 | 94/96 |
| 2 | 95/96 | 95/96 |
| 3 | 94/96 | 94/96 |

The T/T/E/A condition scored 72/72 for both current and historical semantic equivalence across the three replications. This observation should not be interpreted as evidence that T/T/E/A is generally superior, nor does it resolve the lower exact authority-set accuracy observed in that condition.

### 7.4 Interpretation boundary

The semantic amendment supports a narrow descriptive contrast: on this benchmark, substantive current and historical answers were almost always semantically correct under the amended grader, while exact authority-set identification remained much lower.

This contrast is informative because it shows that final-answer correctness and authority-boundary precision can diverge. It does not convert the semantic scores into original confirmatory evidence, and it does not establish a causal explanation for the authority errors.

## 8. Exploratory Analysis

### 8.1 Full structural error taxonomy

Individual authority failures were opened for exploratory inspection only after all three planned replications and aggregate analyses were complete.

Of the 288 responses, 186 exactly matched the frozen authority set and 102 did not. All 102 failures were classified as `over_selection`:

| Error category | Count |
| --- | ---: |
| Under-selection | 0 |
| Over-selection | 102 |
| Mixed-selection | 0 |
| Empty prediction | 0 |
| Other | 0 |

The pattern was stable across replications: 35, 33, and 34 over-selection failures respectively.

This result is exploratory. It was not a preregistered individual-level hypothesis and must not be described as confirmatory evidence that all authority failures generally take this form.

### 8.2 Family-level patterns

Exploratory failure rates differed across the six frozen case families:

| Family | Failures | Rate |
| --- | ---: | ---: |
| Explicit authority hierarchy | 3/48 | 6.25% |
| Supersession / replacement | 8/48 | 16.67% |
| Current but non-authoritative material | 14/48 | 29.17% |
| Historical superseded-but-correct answer | 15/48 | 31.25% |
| Scoped exception vs general rule | 29/48 | 60.42% |
| Temporary rule with expiry/restoration | 33/48 | 68.75% |

The largest failure rates occurred when a generally valid rule remained available but a narrower scope or temporal boundary determined current control. These differences are descriptive only. The experiment was not designed to identify a causal reason for family-level variation.

### 8.3 Frozen stratified sample of extra records

A deterministic sample of 18 failures was frozen before inspecting record content. It included six temporary-rule failures, six scoped-exception failures, and six T/T/E/A over-selection failures.

The sampled failures contained 24 extra selected records. Their structural roles were:

| Structural role | Extra records |
| --- | ---: |
| Supporting/context record | 14 |
| General rule outside scope | 7 |
| Current non-authoritative material | 3 |
| Other / unclassified | 0 |

Within the sampled temporary-rule failures, no extra record was the expired temporary rule itself. Within the scoped-exception sample, out-of-scope general rules were prominent. The T/T/E/A sample also contained supporting/context and out-of-scope general-rule extras.

The sampled pattern therefore points more specifically to over-broad authority attribution than to wholesale resurrection of expired records. This interpretation remains exploratory and benchmark-specific.

## 9. Discussion

### 9.1 Correct answers can coexist with imprecise authority boundaries

The central empirical contrast is between high semantic answer equivalence under the amended measurement and substantially lower exact authority-set accuracy. On this benchmark, the model usually produced the correct current and historical substantive answers while failing to identify the exact set of records that should currently control the decision.

This distinction matters for memory-enabled systems because final-answer accuracy can hide provenance or governance errors. A system may reach the right answer while assigning controlling status too broadly to remembered material. If downstream actions, explanations, or policy checks depend on which source is treated as authoritative, answer correctness alone may therefore be insufficient as an evaluation target.

### 9.2 Retention, relevance, support, and authority are different roles

The exploratory error structure motivates the descriptive framing:

> remembered ≠ relevant ≠ supportive ≠ currently authoritative

The sampled extra records were often not nonsense or obviously obsolete. Many remained useful as context, support, or generally valid background. Their error was narrower: they were selected as currently controlling records when the frozen benchmark specified a smaller authority set.

This suggests that a long-running system may need more than retrieval and recency handling. It may need an explicit mechanism for tracking whether a remembered item is still allowed to control a decision, at what scope, and under which temporal or exception conditions.

The present study does not establish what that mechanism should be. It only provides behavioral evidence that the distinction is measurable and that one tested model did not consistently preserve the boundary.

### 9.3 Relationship to stale-memory research

The observed failures should not be reduced to simple stale-memory retrieval. In the frozen scorer, stale-authority error count was zero, and the exploratory sample did not show expired temporary rules being broadly resurrected as controlling evidence. Instead, the common pattern was inclusion of additional records that remained relevant, supportive, current, or generally valid but were not the controlling authority for the specific query.

This differentiates the present task from asking only whether an agent recognizes that an old state is obsolete. Zombie Memory Holdout v0.1 focuses on decision-time exact authority selection when multiple remembered records remain available.

### 9.4 Metadata conditions are not yet an intervention result

The four presentation conditions produced different exact-set accuracies, including a lower pooled rate for T/T/E/A than for the other conditions. The study does not establish why these differences occurred. They may reflect metadata semantics, formatting effects, prompt interaction, model-specific behavior, or other factors not isolated by the design.

Accordingly, the present manuscript does not claim that richer authority metadata helps or harms reasoning in general. Testing representation effects causally would require a study designed specifically around that question, ideally with ablations, multiple models, and independently controlled evaluation.

### 9.5 Practical implication for evaluation

A useful implication is methodological rather than architectural: evaluations of persistent or memory-enabled agents may benefit from separating at least two questions.

1. Did the system produce the correct substantive answer?
2. Did it identify or use the correct currently controlling evidence?

A system can perform well on the first while remaining weaker on the second. Benchmarks that score only final answers may therefore miss authority-boundary failures that are visible when source roles are explicitly evaluated.

## 10. Limitations

This study has several important limitations.

First, the benchmark is small and synthetic: 24 cases across six constructed families. Its gold authority sets are deliberately explicit and deterministic. Real environments may contain ambiguity, incomplete authority metadata, contested policies, distributed organizational authority, or uncertain scope boundaries that are not represented here.

Second, the live evidence comes from one frozen model snapshot, `gpt-4.1-mini-2025-04-14`. The three replications reused the same benchmark, model, execution settings, and research lineage. They establish within-protocol stability only; they do not establish cross-model, cross-provider, or independent external replication.

Third, the semantic answer measurements are post-freeze amendments rather than part of the original confirmatory plan. Although the semantic grader was specified without inspecting replication-1 individual answers and frozen before live answer scoring, these results should remain separately labeled.

Fourth, the full authority-error taxonomy and stratified content inspection are exploratory. The fact that all 102 failures were over-selection may be specific to this benchmark, model, prompt contract, or scoring ontology. It requires independent replication before being treated as a stable general pattern.

Fifth, the benchmark's authority ontology is a research construct rather than a universal theory of authority. Exact-set scoring assumes that each case has one frozen controlling set. Real-world decision systems may permit multiple defensible authority interpretations or require confidence, abstention, escalation, or human adjudication.

Sixth, the study is behavioral. It does not reveal an internal causal mechanism, representation, attention pattern, or model psychology. Terms such as `authority-boundary failure` describe observed outputs relative to the benchmark, not hidden model processes.

Seventh, the four representation conditions were not designed as a definitive causal intervention study. Condition-level differences should not be generalized into claims about the value of timestamps, lifecycle labels, or T/T/E/A metadata without dedicated follow-up experiments.

Finally, the benchmark does not establish that authority-boundary precision is independently safety-critical in every application. Its relevance is strongest for settings in which agents act on evolving rules, exceptions, provenance, permissions, or state transitions. Demonstrating real-world operational consequences remains future work.

## Evidence-status reminder

The manuscript should preserve the following labels in all later integration and publication steps:

- **Confirmatory:** preregistered structured authority-set scoring across three within-protocol replications.
- **Post-freeze measurement amendment:** semantic-equivalence scoring of current and historical answers.
- **Exploratory:** authority-error taxonomy, family patterns, and stratified inspection.
- **Not established:** causal mechanism, universal generalization, production safety impact, or independent external replication.
