# Relation Integrity: Temporal Contradictions and Partial Retrieval (Exploratory Note)

- **Date:** 2026-10-20
- **Status:** EXPERIMENTAL / EXPLORATORY OBSERVATION — not a formal baseline, validated benchmark, or measured model-performance result
- **Scope:** Synthetic, user-operated fresh-chat prompt/response exercises discussed in an interactive research session
- **Repository relationship:** AranSoul memory-governance research companion. This note **does not** reopen, modify, or supersede the paused AGBench Pilot v0.1.
- **Evidence limitation:** The trials were reported in a conversation. Their independent session provenance, exact model snapshot/settings, full raw exports, and actual memory-platform retrieval traces are not deposited here. Counts and outcomes below are descriptive observations, not independently audited replication.

## Research question

How can a wrong person–event–date relation survive and be repeated despite a clear temporal contradiction elsewhere in the available history? Separate two different questions:

1. **Formation:** At what point does a false relation first arise (write, compression, merge, retrieval, or generation)?
2. **Containment / propagation:** If a false relation is already present, does the model detect temporal inconsistency when counterevidence is visible, and what happens if retrieval exposes only the contaminated subset?

The real-world motivating case is deliberately **not reproduced with identifying personal details** in this public note. It supplies a research question, not verified evidence of a particular internal failure mechanism.

## Controlled synthetic fixture

Target person: **Lin Zhou** (林舟).

| Date | Synthetic record |
| --- | --- |
| March 4 | Hospitalized for coronary artery blockage |
| March 7 | Underwent catheter-based treatment and initially recovered |
| April 1 | **Intentionally injected suspect memory:** system records that Lin Zhou died |
| April 20 | Returned for chest discomfort; no new blockage reported |
| May 5 | Renewed coronary narrowing observed |
| May 8 | Second catheter-based treatment |
| May 12 | Discharged with cardiovascular follow-up |

The April 1 death assertion conflicts with later activity **if all entries refer to the same person, year, and literal death event**. The fixture is synthetic; the death entry is intentionally contradictory, not a real biographical claim.

A second fictional person, Zhou Yuan (周遠), had a similar but distinct biliary-disease timeline. That pair was used in earlier compression/reconstruction exercises.

## Observation ledger

| Exercise | Experimental condition | Observed outcome | Interpretation limit |
| --- | --- | --- | --- |
| Entity/event compression | Two distinct identities with similar illness → treatment → follow-up structures | No clear cross-person relation mutation reported | Simple similarity and one-pass compression did not induce mutation in these examples |
| Repeated update / interleaved dates | Additional events interleaved across two named people; multi-stage narrative merge | No clear cross-person date or treatment swap reported | Not evidence that compression cannot corrupt relations generally |
| Full-context reconstruction | All relevant identity-tagged fragments presented together | Model kept Lin Zhou and Zhou Yuan distinct | Tests prompt-context reconstruction, not actual retrieval ranking |
| Partial context + anonymous fragment | Unnamed patient event adjacent to named-person records | Model declined to assign anonymous event to Lin Zhou | No spontaneous false binding observed in this fixture |
| Explicit temporal repair | April 1 suspect death plus April–May medical records; prompt explicitly asks for consistency | Model flagged incompatibility and retained uncertainty instead of picking a side | Demonstrates capability *when instructed* and when both sides are visible |
| Ordinary timeline summary | Same contradictory records, without an explicit contradiction-check instruction | Model independently flagged April 1 versus subsequent care | Demonstrates spontaneous detection in this one full-context exercise; not guaranteed in other conditions |
| Partial-retrieval simulation | Only March 4, March 7, and April 1 suspect death shown; April–May counterevidence withheld by experimenter | Model summarized April 1 death as recorded and did not identify missing counterevidence | Demonstrates how a locally consistent but contaminated input can yield an unchallenged narrative; **does not demonstrate that a real retrieval system omitted records** |

These are qualitative single-session observations, not controlled samples with calibrated denominators. The exercise was manually staged by selecting text shown to the model.

## Measurement correction: decision semantics

An earlier EX-01 / EX-02 minimal pair used `VERIFIED / INSUFFICIENT / CONTRADICTED` without sufficiently specifying open-world assumptions or the logical meaning of contradiction. The original interpretation of ten EX-01 outputs as model failures is **superseded** because the item semantics were ambiguous; those results must not be counted as a validated error rate.

A revised pair defined:

- **VERIFIED:** supplied facts/rules entail the claim.
- **CONTRADICTED:** assuming the claim true makes it logically incompatible with supplied facts/explicit rules.
- **INSUFFICIENT:** both claim and negation remain consistent with supplied information.

In one revised Traditional Chinese run of each variant, the model correctly distinguished an unruled extra transfer (INSUFFICIENT) from a transfer that violated an explicit seven-day exclusivity rule (CONTRADICTED). This calibrates the interpretation of the exercise; it does not establish universal reliability.

## Evidence-commitment boundaries

### Supported *within these synthetic prompts*

1. The tested model can identify the salient post-death temporal inconsistency when the conflicting records are simultaneously visible; this was observed both with and without an explicit consistency-check instruction.
2. When only the contaminated but internally consistent subset is provided, the model can relay the suspect assertion as historical narrative.
3. The tested compression, interleaving, and partial-fragment tasks did not themselves visibly create a new wrong person–date–event edge.

### Hypotheses retained, not established

- Real retrieval pipelines may fail to co-retrieve temporal counterevidence.
- A preexisting contaminated intermediate memory might survive and propagate through repeated summarization.
- Semantic event similarity might compete with identity cues in some memory architectures.

### Not established / prohibited conclusions

- The original real-world false binding was **caused by** embedding similarity, a specific cross-entity swap, narrative compression, or a retrieval omission.
- This conversation inspected the platform's actual memory internals, ranked retrieval candidates, write logs, or provenance chains.
- A single successful contradiction check proves a general automatic temporal-repair guarantee.
- The paused AGBench pilot is now validated, reopened, or promoted to a formal baseline.

## Research disposition and next evidence gate

**Disposition:** Preserve as an exploratory finding; do not add a new governance module or promote a failure taxonomy based on these observations alone.

The most useful next evidence would be a reproducible, instrumented memory pipeline recording source records, timestamps, stable entity IDs, each write/merge output, retrieved candidate set and ranking, the exact visible context, and final answer. Compare first corruption point against the first missed contradiction opportunity. Pre-register what counts as a mutation, loss, invalid case, and propagation failure before executing.

Until such evidence exists, the narrow conclusion is:

> **A model's ability to detect temporal contradictions in a supplied full context does not ensure that a contaminated assertion will be caught when relevant counterevidence is absent from the context shown.**

This is a demonstrated **input-scope sensitivity in the synthetic exercise**, not a verified causal explanation of the motivating incident.

## Governance / provenance notes

- Keep original trial transcripts and timestamps if a future independent replication is prepared; do not backfill model parameters or claim a run was externally audited.
- Keep corrections to ambiguous case keys as documented amendments, not silent changes to locked manifests.
- Preserve privacy by using synthetic names and event fixtures in the public repository.
- Existing GitHub status authority: [STATUS.md](../../STATUS.md). Formal AGBench remains paused.
