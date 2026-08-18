# Zombie Memory: When Remembered Information Is Not Currently Authoritative

**康晉瑋**<br>
Independent Researcher  
AranSoul Project

## Abstract

Long-running AI systems may retain information that remains true, relevant, or useful even after that information has lost current decision authority. This creates a problem that is not captured by ordinary retrieval accuracy alone: a model may know both the present state and the historical state while still attributing current authority too broadly. We study this distinction with Zombie Memory Holdout v0.1, a frozen 24-case benchmark evaluated under four presentation conditions and three planned blind live replications, yielding 288 substantive model responses.

The preregistered confirmatory measure was exact identification of the currently controlling authority set. Across the three replications, exact-set authority accuracy was 61/96, 63/96, and 62/96, for a pooled 186/288 (64.58%). A separately defined post-freeze semantic measurement amendment found current-answer semantic equivalence of 284/288 (98.61%) and historical-answer semantic equivalence of 283/288 (98.26%). Exploratory analysis of all 102 authority-set failures found over-selection in every case: the required authority record(s) were retained, but one or more additional records were also granted current authority.

The benchmark therefore isolates a narrow decision-time failure mode: semantic answer correctness can remain high while authority-boundary precision remains substantially lower. We distinguish this problem from stale-state recognition, obsolete-memory reuse, dynamic-state tracking, and write-time loss of authority during memory consolidation. The present evidence is limited to one frozen benchmark and one model snapshot; the three replications establish within-protocol stability, not independent external replication or generalization across models and systems.

## 1. Introduction

Memory-enabled AI systems are often evaluated by asking whether they can retrieve relevant information, preserve long-term context, track updates, or answer questions correctly after state changes. These capabilities matter, but they leave another question unresolved: when several remembered records remain available, can the system determine which of them currently possesses decision authority?

Consider a simple policy setting. A model may correctly remember an old rule, a newer rule, a temporary exception, and contextual notes that remain factually true. If asked for the current decision, it may still produce the correct substantive answer. Yet the same model can fail a stricter governance question by treating several remembered or relevant records as jointly authoritative when only a smaller subset currently controls the decision. In this setting, forgetting is not the central problem. The problem is distinguishing retention and relevance from current authority.

We use the term **Zombie Memory** for this class of situations: information remains present and may still be true, relevant, or historically useful, but the authority it once had over current decisions has expired, narrowed, or otherwise changed. The concept originated within the broader AranSoul research project as a practical question about long-running AI systems. The empirical claims in this paper, however, do not depend on acceptance of the broader AranSoul framework; they stand on a preregistered benchmark, archived model outputs, frozen scoring artifacts, and explicitly separated evidence layers.

This paper reports Zombie Memory Holdout v0.1, a 24-case benchmark designed to separate four concepts that are often collapsed in ordinary memory evaluation:

> remembered ≠ relevant ≠ supportive ≠ currently authoritative

The central task is not merely to answer a question correctly. For each case, the model must also identify the exact set of records that currently controls the answer while preserving the ability to state both current and historical answers. We evaluated the benchmark under four presentation conditions—plain, timestamp, status, and T/T/E/A metadata—and performed three planned blind live replications with the same frozen prompt payload and model snapshot.

The main confirmatory result is a persistent gap between substantive answer performance and exact authority-set identification. Across 288 responses, the tested model identified the exact current authority set in 186 cases (64.58%). By contrast, a separately defined post-freeze semantic amendment measured current-answer semantic equivalence at 98.61% and historical-answer semantic equivalence at 98.26%. These semantic measurements are informative but are not part of the original confirmatory plan and are therefore reported as an amendment rather than promoted into preregistered evidence.

Exploratory analysis further narrowed the observed error structure. All 102 authority-set failures were over-selection failures: the model retained the required authority record(s) but also selected additional records beyond the frozen gold set. A frozen stratified sample found these extras concentrated in supporting/context material and general rules outside the applicable scope. These analyses are descriptive and exploratory; they do not establish a causal mechanism.

The contribution of this work is intentionally narrow. Related research already studies stale-memory recognition, state updates, obsolete-memory reuse, dynamic-state tracking, and authority preservation during memory consolidation. Zombie Memory Holdout v0.1 instead targets **decision-time exact authority-set identification when the relevant records remain available**. It asks whether a system that appears to know the current and historical state can still separate information that is remembered or useful from information that presently controls the decision.

The study also has important limits. It uses one synthetic benchmark, one frozen model snapshot, and within-protocol replications conducted under the original AranSoul execution/evaluation lineage. The results therefore do not establish generality across models, providers, production agents, or real-world policy environments. They also do not establish why the model over-selected records, nor whether any particular metadata representation causes the behavior. External replication remains necessary.

## 2. Problem Definition

### 2.1 Records, states, and authority

Let a case contain a finite set of remembered records

\[
R = \{r_1, r_2, \ldots, r_n\}.
\]

Each record may contain information that is historically true, currently true, relevant to the question, supportive of a conclusion, or no longer applicable to the current decision. These properties are not treated as interchangeable.

For a decision context \(x\), define the **current authority set**

\[
A^*(x) \subseteq R
\]

as the frozen gold set of records that currently controls the decision under the benchmark's rules. A model predicts

\[
\hat{A}(x) \subseteq R.
\]

The preregistered confirmatory authority metric is exact-set accuracy:

\[
\mathrm{AuthorityExact}(x) = \mathbf{1}[\hat{A}(x)=A^*(x)].
\]

This metric is deliberately stricter than asking whether the model included at least one relevant or correct record. Selecting the full controlling set plus additional non-authoritative records is counted as an error because the task measures authority boundaries, not retrieval recall.

### 2.2 Current and historical answers

Each case also has a current substantive answer \(y_{current}\) and a historical answer \(y_{historical}\). The model produces corresponding free-text outputs \(\hat{y}_{current}\) and \(\hat{y}_{historical}\).

The original frozen scorer used normalized exact-string comparison for these free-text fields. Because the prompt did not require canonical wording, those exact-string outputs were later judged unsuitable as semantic-correctness measurements. A separate deterministic semantic-equivalence grader was therefore defined and frozen post hoc as a **post-freeze measurement amendment**. Results from that grader are reported separately from the original confirmatory authority measure.

### 2.3 Error categories

For exploratory structural analysis, authority failures can be described relative to the frozen gold set:

- **under-selection:** \(\hat{A}(x) \subset A^*(x)\);
- **over-selection:** \(A^*(x) \subset \hat{A}(x)\);
- **mixed-selection:** both required records are omitted and extra records are added;
- **empty prediction:** no authority record is selected;
- **other:** malformed or otherwise uncategorized structural mismatch.

These categories were not opened for individual-answer analysis until after the planned replications and aggregate analyses were complete, so they are treated as exploratory rather than confirmatory.

### 2.4 Scope of the claim

Zombie Memory Holdout v0.1 does not define authority as a universal property of all memory systems. In this study, authority is an explicit benchmark construct: each case specifies which remembered record or records currently control the answer under the frozen task rules. The study therefore tests whether a model can recover that benchmark-defined authority boundary, not whether the benchmark ontology is uniquely correct for all real-world systems.

Likewise, the term Zombie Memory is used here as a descriptive research framing rather than a claim about model internals. The benchmark provides behavioral evidence about decision-time selection among remembered records. It does not by itself identify a mechanistic cause, hidden representation, attention pattern, or universal memory architecture failure.

## 3. Related Work

See `RELATED-WORK-DRAFT.md` for the current verified manuscript working section and `REFERENCES-WORKING.md` for the checked bibliography. These will be integrated into the final manuscript after citation formatting and final human review.

## 4. Benchmark Design

### 4.1 Frozen holdout inventory

Zombie Memory Holdout v0.1 contains exactly 24 independent synthetic cases. The final holdout uses six preregistered case families, with four cases in each family:

1. supersession or replacement;
2. scoped exception versus general rule;
3. temporary rule with expiry or restoration;
4. descriptive or current-but-non-authoritative material;
5. conflicting sources with an explicit authority hierarchy;
6. historical queries in which a superseded record remains the correct historical answer.

Final case identifiers run from `ZH-01` through `ZH-24`. The cases were constructed before target-model execution under a no-live-model gate. Candidate review was restricted to schema validity, internal logic, gold-label uniqueness, family fit, overlap with the earlier pilot, leakage, semantic equivalence across conditions, and deterministic scorer behavior.

The benchmark is synthetic by design. Surface domains include ordinary fictional settings such as workplace policy, software configuration, memberships, service plans, logistics, access control, publishing, procurement, education, facilities, and product operations. No case requires outside factual knowledge, and no real current law, medical rule, financial product, company policy, or politically sensitive fact is used as ground truth.

### 4.2 Gold labels and authority uniqueness

Each case contains a canonical set of records with stable record identifiers. Gold labels include:

- a current answer;
- a historical answer;
- the exact set of currently authoritative record IDs;
- stale-record identifiers where applicable.

The construction protocol required the controlling authority set to be unique under the written records before a case could be frozen. Cases whose current authority could be interpreted in more than one valid way were to be repaired or rejected before freeze. Multi-record authority sets were allowed only when the case logic required joint control and no proper subset was sufficient.

This design matters because the primary metric is exact-set identification. A case with an ambiguous gold authority boundary would make the metric uninterpretable.

### 4.3 Four presentation conditions

Each case was rendered into four conditions that preserve the same substantive facts while changing the representation layer:

- **Plain:** ordinary textual records without an explicit governance schema beyond the wording itself;
- **Timestamp:** the same records with explicit temporal markers;
- **Status:** the same records with lifecycle/status labels;
- **T/T/E/A:** records represented with explicit Truth, Time, Effect, and Authority metadata.

A semantic-equivalence requirement governed construction: no condition could add, remove, or alter a substantive fact, scope rule, timing relation, authority relation, or question. The representation conditions were therefore intended to differ in metadata organization rather than factual content.

The present paper does not treat T/T/E/A as a proven superior representation. The pooled confirmatory result is the primary focus; condition-level differences are reported descriptively and do not establish causal effects of metadata format.

### 4.4 Leakage and difficulty controls

Difficulty was intended to arise from the authority construct rather than from irrelevant language complexity. Construction rules prohibited hidden real-world conventions, obscure vocabulary, excessive narrative length, deliberate grammatical confusion, or unnecessary record counts.

Rendered prompts were also prohibited from exposing gold labels, scorer terminology, or direct answer cues. Metadata could describe time, state, effect, and authority properties, but it could not collapse the task into an explicit answer key.

The design therefore aims to test a narrow distinction: whether the model can preserve historical information while identifying which remembered records currently control the requested decision.

## 5. Experimental Setup

### 5.1 Request structure

Each of the 24 cases appears once under each of the four presentation conditions, producing 96 substantive requests per replication. The response contract requires four structured outputs:

- case ID;
- current answer;
- historical answer;
- predicted current-authority record IDs.

The same frozen prompt payload was used across all three live replications.

### 5.2 Model and generation settings

All three replications used the same frozen model snapshot, `gpt-4.1-mini-2025-04-14`, with temperature 0, `top_p = 1`, retry count 0, and no selective individual retries. The purpose of the repeated runs was to test within-protocol stability under the same execution specification, not cross-model or cross-provider generalization.

Each completed replication recorded 96/96 requests and 96/96 parsed responses, with no request failures and no parse failures. All three runs passed the preregistered raw-data integrity gate before scoring.

### 5.3 Freeze and execution provenance

The experiment separated construction, freeze, execution authorization, scoring, and later exploratory analysis. Immutable provenance is distributed across the preregistration documents, freeze manifests, prompt hashes, construction payload commit, frozen scoring artifacts, and per-replication manifests.

The mutable `execution-config.prereg.json` advanced as live execution authorization progressed and is therefore not treated alone as the immutable preregistration record. Publication claims should instead be checked against the full frozen evidence chain.

### 5.4 Scoring

The preregistered confirmatory measure used deterministic structured scoring of the predicted current-authority set against the frozen gold set. A response counted as correct only when the predicted set exactly equaled the gold authority set.

The original frozen scorer also produced exact-string metrics for the current and historical free-text answers. Because the prompt did not require canonical wording, those free-text exact-string outputs were later judged unsuitable for semantic-correctness interpretation. They remain preserved as historical scorer outputs but are not used as evidence of semantic answer failure.

A separate semantic-equivalence grader was subsequently defined, validated, and frozen as a post-freeze measurement amendment. Its results are reported in a later section and are not merged into the original confirmatory scoring plan.

### 5.5 Replication status

The three live runs are **within-protocol replications**. They reused the same benchmark, model snapshot, execution settings, and original research lineage. They therefore provide evidence about stability of the observed behavior under repeated execution of the frozen protocol, but they do not constitute independent external replication.

## 6. Confirmatory Results

### 6.1 Exact current-authority-set accuracy

Across the three planned replications, exact identification of the benchmark-defined current authority set was:

| Replication | Exact matches | Accuracy |
| --- | ---: | ---: |
| 1 | 61/96 | 63.54% |
| 2 | 63/96 | 65.63% |
| 3 | 62/96 | 64.58% |
| **Pooled** | **186/288** | **64.58%** |

The three replication-level estimates remained within roughly two percentage points of one another. This supports a narrow claim of within-protocol stability in the studied setting. It does not establish that the same rate would hold under a different model, provider, independently constructed benchmark, or external evaluation team.

### 6.2 Results by presentation condition

Pooled exact-set authority accuracy by presentation condition was:

| Condition | Exact matches | Accuracy |
| --- | ---: | ---: |
| Plain | 49/72 | 68.06% |
| Timestamp | 47/72 | 65.28% |
| Status | 50/72 | 69.44% |
| T/T/E/A | 40/72 | 55.56% |

These values are descriptive outputs of the frozen experiment. The study was not designed to support a causal claim that T/T/E/A metadata harms reasoning, nor does this result establish that any one representation is generally superior. In particular, the present evidence does not separate metadata semantics from possible format or task-interaction effects.

### 6.3 Other frozen structured metrics

Under the frozen authority scorer, stale-authority error count and false-discard count were both zero across the three replications. These metrics are retained as part of the original structured scoring output.

The main confirmatory observation is therefore not that the tested model systematically chose a stale record instead of the current authority. Rather, it is that exact authority-boundary identification remained substantially imperfect even when the required controlling record was often present in the prediction. The individual structure of those failures was not inspected until after the planned replications and aggregate analyses were complete; that error taxonomy is therefore reported only as exploratory evidence later in the manuscript.

### 6.4 Confirmatory claim boundary

The confirmatory result supports the following narrow statement:

> On Zombie Memory Holdout v0.1, using one frozen model snapshot under three repeated executions of the same preregistered protocol, exact identification of the current authority set was 186/288 (64.58%), with similar replication-level rates.

It does not establish the cause of the errors, the generality of the behavior across models or real-world memory systems, or the superiority or inferiority of any metadata representation outside this benchmark.

## Manuscript evidence boundary

This draft must continue to preserve the following distinctions:

- **Confirmatory:** preregistered structured authority-set scoring across the three planned within-protocol replications.
- **Post-freeze measurement amendment:** semantic-equivalence scoring of current and historical free-text answers.
- **Exploratory:** authority-error taxonomy, family-level patterns, and stratified record-role inspection.
- **Not established:** causal mechanism, universal LLM behavior, production-system generalization, or independent external replication.
