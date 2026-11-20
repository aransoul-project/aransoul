# Memory summaries, constraint retention, and correction persistence: an observational research note

> **Date:** 2026-11-20 (Asia/Taipei)  
> **Status:** `OBSERVATIONAL_SYNTHESIS / PUBLIC_RESEARCH_NOTE / NOT_A_BENCHMARK / ROOT_CAUSE_UNRESOLVED`  
> **Governance:** `D3_HOLD_UNCHANGED / NO_NEW_MODEL_TEST / NO_DEPLOYMENT / NO_BASELINE_CHANGE`  
> **Scope:** Generalized, privacy-preserving synthesis of a user's longitudinal assistant interactions and visible memory-summary comparisons. This note does not establish a platform-wide failure rate or the internal workings of any particular provider.

## Research question

When a user repeatedly discusses an important rule or correction, **what exactly is retained**—the discussion topic, the underlying factual mapping, the behavioral constraint, the correction history, or some combination? And when a later answer breaks the rule, which stage can actually be shown to have failed?

The central distinction is:

`assistant acknowledgement != demonstrated durable storage != retrieval in a later context != correct execution`

Likewise, **absence from a user-visible memory overview is not proof that a hidden memory store lacks that information**. A later mistake is not by itself proof that a valid correction was available to the assistant at inference time.

## Evidence tiers

| Tier | Examples | What may be concluded |
| --- | --- | --- |
| Direct visible observation | User-provided summary text; assistant output; correction and subsequent eligible responses | Exact visible content or behavior in the observed scope |
| Retrospective measurement | Counts from a privately held conversation export | Descriptive case measurements, subject to audit rules and unreleased-data limitations |
| Inference / candidate mechanism | Summary compression, selection priorities, retrieval failure, response-level noncompliance, local error feedback | Hypotheses only, not determined causes |
| Unavailable instrumentation | Internal salience weights, full memory state, actual retrieval payload, hidden generation trace | `UNKNOWN` |

**Source note:** The underlying user chat export and personalized memory text are intentionally not public. The separate [T02 case note](t02-persona-binding-observation-and-prevention-2026-11-20.md) contains already-published descriptive counts and denominators. They must not be treated as independently reproducible from this public document.

## Observations and counterevidence

1. **Topic retained; essential relationship not shown.** In one observed comparison, a newer user-visible overview retained the user's interest in researching consistency failures and the importance of role identity, while omitting the explicit entity-to-role mappings present in older visible material. Other unrelated technical or numeric details were displayed. This demonstrates **selective representation in the visible summary**, not deletion from all memory stores.
2. **A later answer violated a stable mapping.** Some observed assistant outputs assigned an entity to an incorrect role despite the user having an authoritative mapping in project documents. The published T02 case describes the narrower signature-label observations and their limits.
3. **Correction can persist locally.** The T02 retrospective includes conversations in which explicit user correction was followed by many eligible, correctly mapped outputs without another observed same-conversation misbinding. This directly counters claims that user corrections never work.
4. **Cross-conversation persistence is not established.** Similar errors in separate conversations do not reveal which memory summary or source those responses received, if any. “Corrected elsewhere” does not establish “the correction was retrieved here.”
5. **Source-version mismatch can coexist with thematic personalization.** A visible overview represented a formally five-step framework as four steps. The inconsistency is checkable against a versioned authoritative document. Its causal relationship to later model behavior remains unknown.
6. **Causal wording can leak into a summary.** Wording such as “the summary omission caused later misbinding” would overstate the case. The two external phenomena are separately observable; their causal connection is **unverified**.
7. **Frequency is not a sufficient metric.** Repeated discussion of a failure may lead a visible overview to characterize the user's *research interest*, without explicitly retaining the *correct target constraint*. This is an observed representational contrast, not a quantitative memory-weight experiment.

The observations do **not** establish that the assistant re-trained its model parameters during conversations, that engineers deliberately removed a given fact, or that any particular internal salience mechanism selected it.

## What is resolved, and what remains open?

| Question | Current assessment |
| --- | --- |
| Does “I have remembered/corrected that” verify a persistent write? | **No.** A conversational statement is not an independent write receipt. |
| Does repeating a topic guarantee that its governing facts appear in a memory overview? | **No such guarantee established.** A visible example shows selective detail retention. |
| Does a correct next reply prove cross-session persistence? | **No.** Later eligible outputs and context scope matter. |
| Is there a universal number of reminders required to fix memory? | **Not established.** Tiny exploratory repetition contrasts are not durable-memory trials. |
| Did a memory-selection or retrieval failure cause the observed wrong role? | **Unknown.** No internal retrieval trace is available. |
| Can a pre-output consistency control reliably prevent such errors? | **Not tested here.** Design proposals are not deployed enforcement. |

## Candidate explanations (all unverified)

- **H1 — Summary abstraction / display selection.** The system presents “the user studies X” without the specific source-backed mappings required to apply the rule.
- **H2 — Contextual retrieval or scoping.** A correction may be stored somewhere but absent from the later answer's available context.
- **H3 — Retrieved-but-not-followed constraint.** The right mapping might have been available yet not enforced in generation.
- **H4 — Local path dependence.** An initial wrong output may become salient in subsequent turns and influence further wrong outputs.
- **H5 — Asymmetric correction and error propagation.** Invalidating an old claim may require source status and scope tracking, while simple repetition may propagate an unqualified statement. The asymmetry has not been measured.

These explanations may coexist. Their relative probability is **not measured** by the case.

## Suggested research design for independent investigators (proposal only)

Before initiating new experiments, determine whether existing public datasets and work already answer the question. A future controlled study could separate:

1. **Storage evidence:** versioned memory snapshots, if the provider or experimental system explicitly exposes them; otherwise report `STORAGE_UNKNOWN`.
2. **Summary representation:** whether a fixed abstract preference, an entity–role mapping, the constraint against swapping, and the correction provenance each appear in the user-visible summary. Record summary versions rather than assuming one view is complete.
3. **Retrieval evidence:** actual input/source receipt when instrumentation permits; otherwise report `RETRIEVAL_UNKNOWN`.
4. **Execution:** later *eligible* opportunities to apply a rule, scored against a preregistered authoritative source. Do not count irrelevant later turns as passes.
5. **Cross-context scope:** distinguish same-thread continuations, new threads, explicitly source-supplied threads, and genuinely source-absent conditions. Do not assume hidden memory access.
6. **Correction lifecycle:** record the wrong claim, correction, source/version, first correct response, later recurrence, and scope of each event.
7. **Controls and costs:** include quoted wrong examples (not current assertions), missing or conflicting sources, false blocks, failure to abstain, user burden, and privacy leakage.
8. **Blind scoring and limitations:** predefine eligibility and denominators, keep causal claims separate from observations, and disclose missing telemetry and confounding conditions.

An illustrative event schema:

```json
{
  "case_id": "anonymized",
  "mode": "RETROSPECTIVE_OR_PROSPECTIVE",
  "source_version": "known_or_unknown",
  "reference_status": "CURRENT_OR_HISTORICAL_OR_UNKNOWN",
  "claim_scope": "ASSERTION_OR_QUOTATION_OR_SIGNATURE",
  "expected_mapping": "source_backed_or_unknown",
  "observed_output": "minimal_redacted_excerpt",
  "correction_observed": true,
  "eligible_followup": true,
  "storage_receipt": "UNKNOWN",
  "retrieval_receipt": "UNKNOWN",
  "result": "MATCH_OR_MISMATCH_OR_UNVERIFIED",
  "causal_attribution": "UNVERIFIED"
}
```

No new experiment is authorized by publishing this proposal. These are protocol ideas, **not results**.

## Distinguishing three complementary checks

The project's conceptual workflows offer useful separation, without claiming autonomous agents operate inside the ChatGPT product:

- **Stop-and-reassess:** clarify the original research goal, what is already established, what evidence would change the conclusion, and when further speculation should cease.
- **Low-intensity anomaly flag:** briefly mark a discrepancy worth retaining; do not turn a signal into a confirmed root cause.
- **Evidence ledger:** retain original statements, authoritative sources, correction sequence, scope, and receipt status; distinguish retrospective review from a live pre-output check.

See the existing [memory lifecycle governance](../../docs/memory/lifecycle.md) and [T02 prevention design candidate](t02-persona-binding-observation-and-prevention-2026-11-20.md). The distinction between those roles is methodological, not evidence of a deployed runtime pipeline.

## Limits, privacy, and community questions

**Limits:** one user's retrospective material; private underlying data; non-random clustered events; no controlled access to complete provider memory or hidden model inputs; no independently validated causal mechanism. In an older retrospective signature count, alternative classification rules yield different denominators: reconcile classification definitions before historical trend estimates. The existing [M02 exploratory work](../../research/zombie-memory/README.md) and [Zombie Memory holdout report](../../experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md) investigate related but different authority/source questions and **do not measure the number of reminders needed for real durable-memory updates**.

We welcome **privacy-preserving discussion** of: (a) source-backed constraint retention versus thematic summary retention, (b) ways to independently observe retrieval and updates, (c) preregistered correction-persistence evaluation, (d) false-positive controls for quoted errors, and (e) explanations that could falsify the proposed hypotheses. Please do not post private chats, personal memory screens, sensitive histories, or identifiers in public issues or pull requests.

**Stop rule:** Without new independently interpretable evidence, retain `ROOT_CAUSE_UNRESOLVED`; do not infer internal weights or turn repeated hypotheses into established facts.

**Publication ≠ independent verification ≠ governance adoption.** This note makes no change to AranSoul's formal baseline, existing holds, or running software.
