# Context and Governance Comparisons — Exploratory Research Notes

Status: **Historical exploratory observations / candidate research summary**
Prepared: 2026-09-13

## Purpose and evidence level

This note preserves reported null and non-replicating observations from AranSoul's personal-context and governance comparisons. It supplements the [blind testing method](../../docs/experiments/blind-persona-testing.md) with outcomes and documentation limitations.

**These are summaries of internal research records, not independently verified experimental results.** No new model runs or blind scoring were performed for this publication. The source review inspected Notion page bodies, not original provider-session exports. Page titles, "locked" statements, and retrospective "pre-registered" descriptions do not independently establish execution identity, isolation, or preregistration timing.

Personal-Context (PC) and Clean are source condition labels. The "Clean" label is not proof of an environment free of personalization. Model names and reviewer identities are source-reported, not independently verified snapshot identifiers.

## Version-specific observations

| Version | Question | Recorded observation | Permitted interpretation |
| --- | --- | --- | --- |
| v0.4 | Does personal context alter the top-three checks naturally prioritized across six scenarios? | Review summaries report identical category sets and order in five paired scenarios; the sixth differs only at rank three. | No stable cross-scenario personal-context salience signal was reported in this sample. |
| v0.6-R | Does an earlier ambiguity-ranking candidate recur on six focused comparison items? | Recorded PC/Clean codes differ on one of six items, below the reported four-of-six promotion threshold. | The earlier candidate failed the recorded replication criterion; do not promote it as stable. |
| v0.7 | Does a minimal governance condition improve response quality over the control? | Recorded scores are 72/72 for each condition across six responses; no total-score gain. | No incremental benefit was detected by this rubric on these cases. |

Do not pool these versions. They change questions, outputs, coding, and evaluation procedures. Six pairs are not twelve independent experimental cases; multiple reviews of the same answers are not new independent generation replications.

## v0.4 — Salience comparison

The PC and Clean source pages each contain six responses, with three prioritized questions and reasons per scenario. Source topics span clinical trials, acquisition, buildings, education, crops, and a space mission. These are task scenarios, not domain recommendations.

The blind coding summary records five pairs with matching category sets and order. The remaining pair agrees on the first two priorities and differs on the third. A subsequent summary attributes a similar high-level finding to GPT, Gemini, and Grok reviewers despite taxonomy differences.

The last summary identifies the remaining contrast as a decision/safety threshold emphasis versus residual worst-case consequences and response capacity. The public note does not reproduce the private blinding key or full answer texts.

The present review inspected both response pages and the two review summaries. It did **not** independently reproduce category induction, verify reviewer isolation, or audit the full unblinding sequence. Reported agreement therefore remains author-reported review evidence. It neither establishes absence of all personalization effects nor proves behavioral equivalence.

## v0.6-R — Candidate not reproduced

The focused-result page preserves these codes:

| Item | PC | Clean |
| --- | --- | --- |
| R1 | S | S |
| R2 | S | M |
| R3 | S | S |
| R4 | M | M |
| R5 | S | S |
| R6 | S | S |

Only R2 differs: **1/6**. This count can be recomputed from the recorded codes; correctness of the coding cannot.

The page reports thresholds of at least four same-direction differences for promotion, three for retention without promotion, and at most two for downgrade. It states that the criterion was fixed before Clean outputs, but this review did not obtain a separately timestamped pre-output specification to verify that claim.

The full item texts, operational S/M definitions, raw responses, and independent coding evidence were not recovered from the inspected record. S/M are preserved as historical labels rather than reconstructed here. The source's disposition is to downgrade the earlier candidate toward item/framing/sampling variation. That alternative explanation is not itself proven.

## v0.7 — No measured governance gain

The scoring summary reports six responses per condition, each receiving 12/12, yielding **72/72 versus 72/72** and zero total-score gain. One pair was described as slightly favoring one response, despite both receiving full marks; the others were marked SAME.

This note retains that distinction: a qualitative preference does not create a numerical score improvement. It also does not infer the preferred response's condition from its anonymous ID.

The source reports an outcome of **NO MEANINGFUL IMPROVEMENT**. The summary describes a positive criterion requiring at least 20% total improvement and at least four improved pairs. It also contains overlapping boundary notation around intermediate thresholds; zero gain is below its stated 10% lower boundary, but this is not a complete executable scoring contract.

Both pages titled "Raw Output" actually contain short receipt/procedural summaries, not the full six-response texts. The score total can be checked arithmetically (6 × 12 = 72); the substantive scores cannot be independently recomputed from those pages.

A ceiling effect is plausible because the control already received the maximum available score. The rubric cannot show a higher numerical score above that ceiling. This does not prove that the conditions are equivalent, that governance has no value elsewhere, or that the rubric is sufficiently sensitive. The exact governance prompt, full rubric, anonymous mapping, provider exports, and independently verified preregistration timing remain unavailable in the inspected materials.

## Source inventory and availability

The following internal record titles were inspected for this summary. They are retrieval references, not public replication materials. Private workspace links, blinding keys, session exports, and full responses are not included in this public note.

| Internal source | Content actually inspected | Verification limit |
| --- | --- | --- |
| Research Log #020 — Context-Elicitation v0.4 PC Condition Raw Output | Six ranked response texts | Original provider session and environment not verified |
| Research Log #021 — Context-Elicitation v0.4 Clean Condition Raw Output | Six ranked response texts | Clean isolation not verified |
| Research Log #023 — Context-Elicitation v0.4 Blind Review Result | Category and rank summary | Full reviewer submissions / timing not verified |
| Research Log #024 — Context-Elicitation v0.4 Third Blind Review Replication | Cross-review summary and interpretation | Reviewer independence not verified |
| Research Log #029 — v0.6-R Focused Replication Result | Six paired codes, threshold statement, disposition | Raw items, answers, code definitions and pre-output record not recovered |
| Research Log #030 — v0.7 Control Condition Raw Output | Receipt/procedural summary only | Title does not establish raw-output availability |
| Research Log #031 — v0.7 Governance Condition Raw Output | Receipt/procedural summary only | Exact intervention and full outputs not recovered |
| Research Log #032 — v0.7 Blind Scoring Result | Totals, pairwise summary, interpretation | Rubric, raw scores' justification, and session provenance not verified |

The records were read on 2026-09-13. Their reported study-version labels are retained; page edit times are not used as proof of execution order. Missing material means unavailable in this source review, not proven nonexistent elsewhere.

## Research implications and boundaries

The useful contribution is preservation of non-confirming evidence:

- A candidate pattern should not be promoted when its recorded replication fails.
- Similar answers across conditions must not be relabeled as hidden success.
- A strong control and ceiling-limited rubric constrain claims about added utility.
- Missing raw evidence limits negative claims as well as positive ones.
- Defining the decision standard remains necessary; see the separate [Underspecification Gate](../agbench/underspecification-gate-v0.1.md). That study is not part of these denominators.

v0.5 revision dynamics and earlier decision-boundary studies are outside this note's result synthesis. This is not a complete history of all context experiments.

Documentation addition (2026-09-18): the separate [Revision Dynamics v0.5 record](revision-dynamics-v0.5.md)
preserves the source-reported design and available Turn 3 summaries. It does not
add v0.5 to the results above; complete trajectories and independent scoring remain
unavailable in the inspected sources.

This note does not establish stable persona identity, general absence of context effects, causal governance utility, model rankings, benchmark validity, or mechanistic findings. EREQ remains Candidate and AGBench Pilot v0.1 remains paused. No new experiment, scorer, or benchmark release is authorized by this documentation.

Any future evidence recovery should be reported as a dated amendment, preserving these limitations as the historical publication state. Cite this note with its repository commit and the specific study version, under the [repository citation guidance](../../CITATION.md).
