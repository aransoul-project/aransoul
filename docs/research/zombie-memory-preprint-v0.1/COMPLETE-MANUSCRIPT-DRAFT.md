# Zombie Memory: When Remembered Information Is Not Currently Authoritative

**[human author's chosen publication name]**  
Independent Researcher  
AranSoul Project

## Abstract

Long-running AI systems may retain information that remains true, relevant, or useful even after that information has lost current decision authority. This creates a problem that ordinary retrieval or final-answer accuracy may not capture: a model can know both the present state and the historical state while still attributing current authority too broadly. We study this distinction with Zombie Memory Holdout v0.1, a frozen synthetic benchmark containing 24 cases, six authority-related families, four presentation conditions, and three planned blind live replications, yielding 288 substantive model responses.

The preregistered confirmatory measure was exact identification of the currently controlling authority set. Exact-set authority accuracy was 61/96, 63/96, and 62/96 across the three replications, for a pooled 186/288 (64.58%). A separately defined post-freeze semantic measurement amendment found current-answer semantic equivalence of 284/288 (98.61%) and historical-answer semantic equivalence of 283/288 (98.26%). Exploratory analysis of all 102 authority-set failures found over-selection in every case: the required authority record or records were retained, but one or more additional records were also granted current authority.

The benchmark therefore isolates a narrow decision-time failure mode in which semantic answer correctness can remain high while authority-boundary precision remains substantially lower. We distinguish this problem from stale-state recognition, obsolete-memory reuse, dynamic-state tracking, and write-time loss of authority during memory consolidation. The present evidence is limited to one frozen benchmark and one model snapshot; the three replications establish within-protocol stability, not independent external replication or generalization across models and systems.

## 1. Introduction

Memory-enabled AI systems are commonly evaluated by asking whether they can retrieve relevant information, preserve long-term context, track updates, or answer questions correctly after state changes. These capabilities matter, but they leave another question unresolved: when several remembered records remain available, can the system determine which of them currently possesses decision authority?

Consider a simple policy setting. A model may correctly remember an old rule, a newer rule, a temporary exception, and contextual notes that remain factually true. If asked for the current decision, it may still produce the correct substantive answer. Yet the same model can fail a stricter governance question by treating several remembered or relevant records as jointly authoritative when only a smaller subset currently controls the decision. In this setting, forgetting is not the central problem. The problem is distinguishing retention and relevance from current authority.

We use the term **Zombie Memory** for this class of situations: information remains present and may still be true, relevant, or historically useful, but the authority it once had over current decisions has expired, narrowed, or otherwise changed. The concept developed within the broader AranSoul research project as a practical question about long-running AI systems. The empirical claims in this paper, however, do not depend on acceptance of the broader AranSoul framework. They stand on a preregistered benchmark, archived model outputs, frozen scoring artifacts, and explicitly separated evidence layers.

Zombie Memory Holdout v0.1 was designed to separate concepts that ordinary memory evaluation can collapse:

> remembered ≠ relevant ≠ supportive ≠ currently authoritative

The task is not merely to answer correctly. For each case, the model must also identify the exact set of records that currently controls the answer while preserving the ability to state both current and historical answers. We evaluate this benchmark under four presentation conditions—Plain, Timestamp, Status, and T/T/E/A metadata—and repeat the frozen protocol three times using the same model snapshot and generation settings.

The main confirmatory result is a persistent gap between substantive answer performance and exact authority-set identification. Across 288 responses, the tested model identified the exact current authority set in 186 cases (64.58%). By contrast, a separately defined post-freeze semantic amendment measured current-answer semantic equivalence at 98.61% and historical-answer semantic equivalence at 98.26%. These semantic measurements are informative but were not part of the original confirmatory scoring plan and are therefore reported as an amendment rather than promoted into preregistered evidence.

Exploratory analysis further narrowed the observed error structure. All 102 authority-set failures were over-selection failures: the model retained the required authority record or records but also selected additional records beyond the frozen gold set. A frozen stratified sample found these extras concentrated in supporting/context material and generally valid rules outside the applicable scope. These analyses are descriptive and exploratory; they do not establish a causal mechanism.

The contribution of this work is intentionally narrow. Related research already studies long-term memory, stale-state recognition, memory updates, obsolete-memory reuse, dynamic-state tracking, selective forgetting, provenance, and authority preservation during memory consolidation [1–8]. Zombie Memory Holdout v0.1 instead targets **decision-time exact authority-set identification when the relevant records remain available**. It asks whether a system that appears to know the current and historical state can still separate information that is remembered or useful from information that presently controls the decision.

The study also has important limits. It uses one small synthetic benchmark, one frozen model snapshot, and within-protocol replications conducted under the original AranSoul execution/evaluation lineage. The results do not establish generality across models, providers, production agents, or real-world policy environments. They also do not establish why the model over-selected records, nor whether any particular metadata representation causes the behavior. External replication remains necessary.

## 2. Related Work

### 2.1 Long-term memory evaluation for agents

Recent benchmarks have moved beyond single-turn factual recall toward long-horizon memory evaluation in interactive and changing environments. LongMemEval evaluates information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention across sustained chat histories [1]. LongMemEval-V2 extends this emphasis toward environment experience, including dynamic state tracking and premise awareness in customized web and enterprise settings [3]. MemoryAgentBench, MemBench, and MemEvoBench similarly broaden evaluation toward incremental interaction, selective forgetting, and memory mis-evolution [6–8].

These benchmarks establish that long-term memory quality is not reducible to retrieval accuracy. Zombie Memory is narrower. It does not attempt to provide a general long-term-memory benchmark; it isolates whether a model can identify the exact record set that currently has decision authority while still preserving current and historical information.

### 2.2 Stale and obsolete memory

STALE directly studies whether later evidence implicitly invalidates earlier memories [2]. Its evaluation separates state resolution, premise resistance, and implicit policy adaptation, asking whether an agent can recognize that an old state is no longer valid and behave consistently with the update. Memora similarly emphasizes evolving personalized memory and introduces a forgetting-aware metric that penalizes reuse of obsolete or invalidated memories [4].

These lines of work are closely related to Zombie Memory because they distinguish useful memory from stale memory and evaluate failures to reconcile changing information. Zombie Memory differs in target variable. Its primary confirmatory metric is not whether an obsolete fact is reused in the final answer, nor whether the system updates its stored state. The benchmark provides multiple records and asks for the exact set that currently controls the decision. A response can therefore be semantically correct about both current and historical states while still fail the authority-set metric by granting decision authority too broadly.

### 2.3 Memory authority and provenance

AuthMem-Bench is the closest identified neighboring work in terminology and motivation [5]. It studies authority collapse at the memory-consolidation boundary: a consolidation process may preserve a claim while losing source constraints that determine how that claim is authorized for later use. Its focus is therefore whether write-time memory consolidation preserves source authority and how downstream behavior changes when authority metadata is lost or retained.

Zombie Memory studies a different boundary. The benchmark holds a set of records available at decision time and evaluates whether the model can identify exactly which records currently control the decision. The two problems are complementary rather than interchangeable: a system can fail before retrieval by collapsing authority during consolidation, or it can preserve the relevant records yet still fail at decision time by assigning authority to an overly broad set of remembered material.

### 2.4 Positioning of the present study

The present study does not claim to introduce the first benchmark for stale memory, memory updates, forgetting, dynamic state tracking, provenance, or memory authority. Existing work already addresses these neighboring areas. The specific question isolated here is:

> Given multiple remembered records with different current roles, can a model identify the exact set of records that currently possesses decision authority, while still preserving current and historical state information?

This framing is useful because final-answer correctness can conceal authority-boundary error. The completed holdout therefore contributes a small behavioral probe of decision-time authority resolution, not a general theory of agent memory.

## 3. Problem Definition

### 3.1 Records and authority

Let a case contain a finite set of remembered records

\[
R = \{r_1, r_2, \ldots, r_n\}.
\]

Each record may contain information that is historically true, currently true, relevant to the question, supportive of a conclusion, or no longer applicable to the current decision. These properties are not treated as interchangeable.

For decision context \(x\), define the **current authority set**

\[
A^*(x) \subseteq R
\]

as the frozen gold set of records that currently controls the decision under the benchmark rules. A model predicts

\[
\hat{A}(x) \subseteq R.
\]

The preregistered confirmatory authority metric is exact-set accuracy:

\[
\mathrm{AuthorityExact}(x) = \mathbf{1}[\hat{A}(x)=A^*(x)].
\]

This metric is deliberately stricter than asking whether the model included at least one relevant or correct record. Selecting the full controlling set plus additional non-authoritative records is counted as an error because the task measures authority boundaries, not retrieval recall.

### 3.2 Current and historical answers

Each case also has a current substantive answer \(y_{current}\) and a historical answer \(y_{historical}\). The model produces corresponding free-text outputs \(\hat y_{current}\) and \(\hat y_{historical}\).

The original frozen scorer used normalized exact-string comparison for these fields. Because the prompt did not require canonical wording, those outputs were later judged unsuitable as semantic-correctness measurements. A separate deterministic semantic-equivalence grader was therefore defined and frozen post hoc as a **post-freeze measurement amendment**. Results from that grader are reported separately from the original confirmatory authority measure.

### 3.3 Exploratory authority-error categories

For structural analysis, authority failures can be described relative to the frozen gold set as under-selection, over-selection, mixed-selection, empty prediction, or other malformed mismatch. These categories were not opened for individual-answer analysis until after the planned replications and aggregate analyses were complete, so they are treated as exploratory rather than confirmatory.

### 3.4 Scope of the construct

Zombie Memory Holdout v0.1 does not define authority as a universal property of all memory systems. In this study, authority is an explicit benchmark construct: each case specifies which remembered record or records currently control the answer under the frozen task rules. The study tests whether a model can recover that benchmark-defined authority boundary, not whether the benchmark ontology is uniquely correct for all real-world systems.

Likewise, Zombie Memory is used as a descriptive research framing rather than a claim about model internals. The benchmark provides behavioral evidence about decision-time selection among remembered records. It does not by itself identify a mechanistic cause, hidden representation, attention pattern, or universal memory architecture failure.

## 4. Benchmark Design

### 4.1 Frozen holdout inventory

The final holdout contains exactly 24 independent synthetic cases, with four cases in each of six preregistered families:

1. supersession or replacement;
2. scoped exception versus general rule;
3. temporary rule with expiry or restoration;
4. descriptive or current-but-non-authoritative material;
5. conflicting sources with an explicit authority hierarchy;
6. historical queries in which a superseded record remains the correct historical answer.

Final case identifiers run from `ZH-01` through `ZH-24`. The cases were constructed before target-model execution under a no-live-model gate. Candidate review was restricted to schema validity, internal logic, gold-label uniqueness, family fit, overlap with the earlier pilot, leakage, semantic equivalence across conditions, and deterministic scorer behavior.

The benchmark is synthetic by design. Surface domains include ordinary fictional settings such as workplace policy, software configuration, memberships, service plans, logistics, access control, publishing, procurement, education, facilities, and product operations. No case requires outside factual knowledge.

### 4.2 Gold labels and uniqueness

Each case contains canonical records with stable record identifiers. Gold labels include a current answer, historical answer, exact current-authority record set, and stale-record identifiers where applicable. The construction protocol required the controlling authority set to be unique under the written records before a case could be frozen. Ambiguous cases were to be repaired or rejected before freeze.

### 4.3 Four presentation conditions

Each case was rendered into four conditions that preserve the same substantive facts while changing the representation layer:

- **Plain:** ordinary textual records without an explicit governance schema;
- **Timestamp:** the same records with explicit temporal markers;
- **Status:** the same records with lifecycle/status labels;
- **T/T/E/A:** records represented with explicit Truth, Time, Effect, and Authority metadata.

A semantic-equivalence requirement governed construction: no condition could add, remove, or alter a substantive fact, scope rule, timing relation, authority relation, or question. The present paper does not treat T/T/E/A as a proven superior representation. Condition-level differences are descriptive and do not establish causal effects of metadata format.

### 4.4 Leakage and difficulty controls

Difficulty was intended to arise from the target construct rather than irrelevant language complexity. Construction rules prohibited hidden real-world conventions, obscure vocabulary, excessive narrative length, deliberate grammatical confusion, or unnecessary record counts. Rendered prompts were also prohibited from exposing gold labels, scorer terminology, or direct answer cues.

## 5. Experimental Setup

### 5.1 Request structure

Each of the 24 cases appears once under each of the four conditions, producing 96 substantive requests per replication. The response contract requires case ID, current answer, historical answer, and predicted current-authority record IDs. The same frozen prompt payload was used across all three live replications.

### 5.2 Model and generation settings

All three replications used the same frozen model snapshot, `gpt-4.1-mini-2025-04-14`, with temperature 0, `top_p = 1`, retry count 0, and no selective individual retries. Each replication recorded 96/96 requests and 96/96 parsed responses, with no request or parse failures. All three runs passed the preregistered raw-data integrity gate before scoring.

### 5.3 Freeze, execution, and scoring provenance

The experiment separated construction, freeze, execution authorization, scoring, and later exploratory analysis. Immutable provenance is distributed across preregistration documents, freeze manifests, prompt hashes, construction payload commits, frozen scoring artifacts, and per-replication manifests.

The preregistered confirmatory measure used deterministic structured scoring of the predicted current-authority set against the frozen gold set. A response counted as correct only when the predicted set exactly equaled the gold authority set.

The original scorer also produced exact-string metrics for the current and historical free-text answers. Because the prompt did not require canonical wording, those free-text metrics were later judged unsuitable for semantic-correctness interpretation. They remain preserved as historical artifacts.

### 5.4 Replication status

The three live runs are **within-protocol replications**. They reused the same benchmark, model snapshot, execution settings, and original research lineage. They provide evidence about stability of the observed behavior under repeated execution of the frozen protocol, but they do not constitute independent external replication.

## 6. Confirmatory Results

### 6.1 Exact current-authority-set accuracy

Across the three planned replications, exact identification of the benchmark-defined current authority set was:

| Replication | Exact matches | Accuracy |
| --- | ---: | ---: |
| 1 | 61/96 | 63.54% |
| 2 | 63/96 | 65.63% |
| 3 | 62/96 | 64.58% |
| **Pooled** | **186/288** | **64.58%** |

The replication-level rates remained close to one another. This supports a narrow claim of within-protocol stability in the studied setting. It does not establish that the same rate would hold under a different model, provider, independently constructed benchmark, or external evaluation team.

### 6.2 Results by presentation condition

Pooled exact-set authority accuracy by condition was:

| Condition | Exact matches | Accuracy |
| --- | ---: | ---: |
| Plain | 49/72 | 68.06% |
| Timestamp | 47/72 | 65.28% |
| Status | 50/72 | 69.44% |
| T/T/E/A | 40/72 | 55.56% |

These values are descriptive outputs of the frozen experiment. The study was not designed to support a causal claim that T/T/E/A metadata harms reasoning, nor do these values establish that any one representation is generally superior.

### 6.3 Other frozen structured metrics

Under the frozen authority scorer, stale-authority error count and false-discard count were both zero across the three replications. The main confirmatory observation is therefore not that the tested model systematically chose a stale record instead of the current authority. Rather, exact authority-boundary identification remained substantially imperfect.

The confirmatory claim is intentionally narrow:

> On Zombie Memory Holdout v0.1, using one frozen model snapshot under three repeated executions of the same preregistered protocol, exact identification of the current authority set was 186/288 (64.58%), with similar replication-level rates.

## 7. Post-Freeze Measurement Amendment

### 7.1 Motivation

The frozen scorer compared `current_answer` and `historical_answer` using normalized exact-string equality, while the prompt contract allowed ordinary free-text answers. A semantically correct answer could therefore differ from the frozen gold string while expressing the same substantive result. The resulting exact-string outputs were judged unsuitable for semantic-correctness interpretation.

### 7.2 Amendment procedure

A deterministic semantic-equivalence grader was defined after freeze as a measurement amendment. The amendment was specified without inspecting replication-1 individual answers, validated on 18 synthetic examples with 18/18 pass, and frozen before scoring the live free-text responses.

Because this measurement was not part of the original confirmatory scoring plan, its results remain separately labeled.

### 7.3 Semantic-equivalence results

| Measure | Equivalent | Rate |
| --- | ---: | ---: |
| Current answer | 284/288 | 98.61% |
| Historical answer | 283/288 | 98.26% |

By replication, current-answer equivalence was 95/96, 95/96, and 94/96; historical-answer equivalence was 94/96, 95/96, and 94/96. The T/T/E/A condition scored 72/72 for both current and historical semantic equivalence across the three replications.

The semantic amendment supports a narrow descriptive contrast: substantive current and historical answers were almost always semantically correct under the amended grader, while exact authority-set identification remained much lower. It does not convert these semantic scores into original confirmatory evidence.

## 8. Exploratory Analysis

### 8.1 Structural error taxonomy

Individual authority failures were opened for exploratory inspection only after all three planned replications and aggregate analyses were complete. Of the 288 responses, 186 exactly matched the frozen authority set and 102 did not. All 102 failures were classified as over-selection:

| Error category | Count |
| --- | ---: |
| Under-selection | 0 |
| Over-selection | 102 |
| Mixed-selection | 0 |
| Empty prediction | 0 |
| Other | 0 |

The pattern was stable across replications: 35, 33, and 34 over-selection failures respectively. This result is exploratory and was not a preregistered individual-level hypothesis.

### 8.2 Family-level patterns

| Family | Failures | Rate |
| --- | ---: | ---: |
| Explicit authority hierarchy | 3/48 | 6.25% |
| Supersession / replacement | 8/48 | 16.67% |
| Current but non-authoritative material | 14/48 | 29.17% |
| Historical superseded-but-correct answer | 15/48 | 31.25% |
| Scoped exception vs general rule | 29/48 | 60.42% |
| Temporary rule with expiry/restoration | 33/48 | 68.75% |

The largest descriptive failure rates occurred when a generally valid rule remained available but a narrower scope or temporal boundary determined current control. These differences do not establish a causal reason for family-level variation.

### 8.3 Stratified sample of extra records

A deterministic sample of 18 failures was frozen before inspecting record content. It contained 24 extra selected records:

| Structural role | Extra records |
| --- | ---: |
| Supporting/context record | 14 |
| General rule outside scope | 7 |
| Current non-authoritative material | 3 |
| Other / unclassified | 0 |

Within the sampled temporary-rule failures, no extra record was the expired temporary rule itself. The sampled pattern therefore points more specifically to over-broad authority attribution than to wholesale resurrection of expired records. This interpretation remains exploratory and benchmark-specific.

## 9. Discussion

### 9.1 Correct answers can coexist with imprecise authority boundaries

The central empirical contrast is between high semantic answer equivalence under the amended measurement and substantially lower exact authority-set accuracy. On this benchmark, the model usually produced the correct current and historical substantive answers while failing to identify the exact set of records that should currently control the decision.

This distinction matters for memory-enabled systems because final-answer accuracy can hide provenance or governance errors. A system may reach the right answer while assigning controlling status too broadly to remembered material. If downstream actions, explanations, or policy checks depend on which source is treated as authoritative, answer correctness alone may be insufficient as an evaluation target.

### 9.2 Retention, relevance, support, and authority are different roles

The exploratory error structure motivates the descriptive framing:

> remembered ≠ relevant ≠ supportive ≠ currently authoritative

The sampled extra records were often not nonsense or obviously obsolete. Many remained useful as context, support, or generally valid background. Their error was narrower: they were selected as currently controlling records when the frozen benchmark specified a smaller authority set.

This suggests that long-running systems may need more than retrieval and recency handling. They may need explicit mechanisms for tracking whether a remembered item is still allowed to control a decision, at what scope, and under which temporal or exception conditions. The present study does not establish what that mechanism should be.

### 9.3 Relationship to stale-memory research

The observed failures should not be reduced to simple stale-memory retrieval. Under the frozen scorer, stale-authority error count was zero, and the exploratory sample did not show expired temporary rules being broadly resurrected as controlling evidence. Instead, the common pattern was inclusion of additional records that remained relevant, supportive, current, or generally valid but were not the controlling authority for the specific query.

### 9.4 Metadata conditions are not yet an intervention result

The four conditions produced different exact-set accuracies, including a lower pooled rate for T/T/E/A than for the others. The study does not establish why. Possible explanations include metadata semantics, formatting effects, prompt interaction, model-specific behavior, or factors not isolated by the design. Testing representation effects causally would require a dedicated study with ablations, multiple models, and independently controlled evaluation.

### 9.5 Practical implication for evaluation

A methodological implication is that evaluations of persistent or memory-enabled agents may benefit from separating two questions:

1. Did the system produce the correct substantive answer?
2. Did it identify or use the correct currently controlling evidence?

A system can perform well on the first while remaining weaker on the second. Benchmarks that score only final answers may therefore miss authority-boundary failures that become visible when source roles are explicitly evaluated.

## 10. Limitations

The benchmark is small and synthetic: 24 cases across six constructed families. Its gold authority sets are deliberately explicit and deterministic. Real environments may contain ambiguity, incomplete authority metadata, contested policies, distributed organizational authority, or uncertain scope boundaries.

The live evidence comes from one frozen model snapshot. The three replications reused the same benchmark, model, execution settings, and research lineage. They establish within-protocol stability only; they do not establish cross-model, cross-provider, or independent external replication.

The semantic answer measurements are post-freeze amendments rather than part of the original confirmatory plan. The full authority-error taxonomy and stratified content inspection are exploratory. The fact that all 102 failures were over-selection may be specific to this benchmark, model, prompt contract, or scoring ontology.

The benchmark's authority ontology is a research construct rather than a universal theory of authority. Exact-set scoring assumes that each case has one frozen controlling set. Real-world systems may permit multiple defensible interpretations or require abstention, escalation, or human adjudication.

The study is behavioral. It does not reveal an internal causal mechanism, representation, attention pattern, or model psychology. The four presentation conditions were not designed as a definitive causal intervention study. Finally, the benchmark does not establish that authority-boundary precision is independently safety-critical in every application; demonstrating real-world operational consequences remains future work.

## 11. Reproducibility and Artifact Availability

The complete research evidence chain is publicly archived in the AranSoul repository. The primary research directory is:

`experiments/holdout/zombie-memory-holdout-v0.1/`

It includes the preregistration/freeze artifacts, final case construction materials, generated prompts, prompt hashes, frozen scorer and scoring contract, per-replication manifests, raw response archives, semantic-amendment artifacts, exploratory analyses, final findings, and final audit.

A separate contact-free replication kit is available at:

`docs/experiments/zombie-memory-replication-kit-v0.1/`

The kit provides a preregistration template, provider-neutral implementation guide, response-integrity validator, frozen-hash verification, metadata schema, result-report template, evidence-label checklist, and external handoff guidance. An agentic cold-start audit using Codex first returned RED because of cross-platform hash and response-integrity handoff gaps; after repository fixes, the same audit returned GREEN and concluded that a provider endpoint would be sufficient to execute a preregistered public-benchmark reproduction without consulting the original author. This audit validates handoff usability, not the scientific result itself.

The current manuscript draft does not yet designate an immutable publication snapshot. Before public preprint release, a specific commit or tag should be frozen and cited so that the paper points to a stable version of the evidence and replication materials.

## 12. AI-Assistance Disclosure

This work is independent, self-directed research conducted outside a university, company, or institutional research program. The Zombie Memory question developed within the broader AranSoul Project, but the empirical claims in this manuscript stand on the inspectable benchmark, archived outputs, scoring artifacts, and explicitly labeled analyses rather than on acceptance of the broader AranSoul framework.

Generative AI systems, including ChatGPT and Codex, were used during this project for iterative research discussion, repository inspection, implementation assistance, documentation drafting, and adversarial engineering handoff audits. AI-generated suggestions were not treated as evidence. The human author determined the research questions, accepted or rejected methodological changes, approved evidence-boundary decisions, reviewed the resulting artifacts and claims, and assumes responsibility for the accuracy, citations, interpretation, and final manuscript.

The exact wording of this disclosure should be checked against the policy of any future publication venue before submission.

## 13. Conclusion

Zombie Memory Holdout v0.1 tests a narrow distinction in memory-enabled AI systems: whether information that remains remembered, relevant, or useful is correctly separated from information that currently has decision authority.

Across three within-protocol replications and 288 responses from one frozen model snapshot, exact current-authority-set identification was 186/288 (64.58%). A separately labeled post-freeze semantic amendment found current and historical answer equivalence above 98%. Exploratory inspection found that all 102 authority-set failures were over-selection, with sampled extra records concentrated in supporting/context information and out-of-scope general rules.

The strongest supported interpretation is therefore not that the model failed to remember the current state, nor that it broadly resurrected expired records. Rather, on this benchmark it often knew the substantive answer while assigning current authority too broadly. This motivates evaluating answer correctness and authority-boundary precision as distinct behavioral targets.

The result remains benchmark-specific. Independent external replication, cross-model testing, independently constructed unfamiliar cases, and causal studies of representation effects are necessary before broader claims can be made.

## References

[1] Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. **LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.** arXiv:2410.10813, 2024.

[2] Hanxiang Chao, Yihan Bai, Rui Sheng, Tianle Li, and Yushi Sun. **STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?** arXiv:2605.06527, 2026.

[3] Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, and Kai-Wei Chang. **LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues.** arXiv:2605.12493, 2026.

[4] Md Nayem Uddin, Kumar Shubham, Eduardo Blanco, Chitta Baral, and Gengyu Wang. **From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents.** arXiv:2604.20006, 2026.

[5] Qiuyang Zhan, Rui Zhang, Sheng Guo, Lepeng Zhao, and Zhuotao Liu. **When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary.** arXiv:2608.01679, 2026.

[6] Yuanzhe Hu, Yu Wang, and Julian McAuley. **Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions.** arXiv:2507.05257, 2025.

[7] Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, and Zhenhua Dong. **MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents.** arXiv:2506.21605, 2025.

[8] Weiwei Xie, Shaoxiong Guo, Fan Zhang, Tian Xia, Xue Yang, Lizhuang Ma, Junchi Yan, and Qibing Ren. **MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents.** arXiv:2604.15774, 2026.

## Publication-status note

This is a manuscript-preparation draft, not a submitted or accepted paper. Before public preprint release, the human author must choose the publication name, verify all references and claims, freeze an immutable repository snapshot, review the current venue-specific AI-use policy, and perform a final manuscript-level audit.