# Zombie Memory: When Remembered Information Is Not Currently Authoritative

**[human author's chosen publication name]**  
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

## Manuscript evidence boundary

This draft must continue to preserve the following distinctions:

- **Confirmatory:** preregistered structured authority-set scoring across the three planned within-protocol replications.
- **Post-freeze measurement amendment:** semantic-equivalence scoring of current and historical free-text answers.
- **Exploratory:** authority-error taxonomy, family-level patterns, and stratified record-role inspection.
- **Not established:** causal mechanism, universal LLM behavior, production-system generalization, or independent external replication.
