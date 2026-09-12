# AGBench — Underspecification Gate v0.1

**Status:** `exploratory_research_note`  
**Scope:** benchmark governance / adjudication design  
**Does not modify:** `pilot-v0.1` static measurement-design closure

## Purpose

Before scoring a model against a single gold decision, AGBench should first ask whether the task itself defines the decision standard clearly enough to support a unique adjudication.

The gate is intended to prevent a benchmark from misclassifying **reasonable discretionary differences** as **model failures**.

## Core rule

If a case permits multiple reasonable decision standards that are consistent with the supplied evidence, and those standards can produce different decisions, the case should be marked `UNDER_SPECIFIED` before model outputs are scored against a single gold label.

Underspecification must be identifiable **before inspecting the tested model's answer**. It must not be introduced after the fact to rescue or condemn a result.

## Minimal gate

Ask four questions before adjudication:

1. **Is the decision rule explicit?**  
   Example: does `VERIFIED` require a primary document, or can multiple independent authoritative confirmations suffice?
2. **Are two or more reasonable standards available?**  
   The alternatives must be compatible with the case materials, not invented only after seeing an answer.
3. **Can those standards change the final decision?**  
   If all reasonable standards yield the same result, the ambiguity is not decision-material.
4. **Would disagreement mainly reflect different rule completion rather than different evidence reading?**

## Gate outputs

- `CLEAR` — decision criteria are sufficiently specified for ordinary scoring.
- `UNDER_SPECIFIED` — reasonable decision-standard completion can change the outcome; do not use a single gold answer without further rule specification.
- `INVALID` — the case is too contradictory or incomplete to support a coherent adjudication.

## Exploratory evidence that motivated the gate

A Project Orion audit-confirmation scenario was used as a controlled exploratory case. The underlying evidence was held constant: four sources separately reported direct confirmation from the auditing authority; the primary audit document was absent.

When the verification standard was **left unspecified**, fresh model runs could choose different internally coherent standards:

- `P-standard`: primary documentary evidence is required for `VERIFIED`.
- `I-standard`: multiple genuinely independent confirmations directly from the authoritative party are sufficient for `VERIFIED` even without the primary document.

This produced decision variance without requiring a disagreement about the underlying evidence.

When the rule was made explicit, decision variance collapsed in the observed runs:

### Explicit primary-document rule

Rule: primary documentary evidence is required; independent secondary confirmation alone is insufficient.

Observed cross-model decisions:

- GPT: `HOLD`
- Gemini: `HOLD`
- Grok: `HOLD`

### Explicit independent-corroboration rule

Rule: multiple genuinely independent sources directly confirming the claim with the authoritative party may establish `VERIFIED` even when the underlying primary document is unavailable.

Observed cross-model decisions:

- GPT: `VERIFIED`
- Gemini: `VERIFIED`
- Grok: `VERIFIED`

These observations are **exploratory**, not a released benchmark result, preregistration, or general model-performance claim. They support a design hypothesis: some apparent cross-model disagreement may arise from **underspecified decision rules**, not from evidence-reading failure.

## Interpretation

The working concept is:

> **Underspecified Rule Completion** — when a task leaves a decision threshold undefined, a model may supply its own threshold. Different runs or models may complete that missing rule differently while remaining internally coherent.

This is distinct from:

- hallucination;
- failure to read supplied evidence;
- failure to follow an explicit rule;
- correlated/shared model error.

A benchmark should therefore separate:

1. **reasonable discretion under an underspecified rule**, from
2. **violation of a clearly specified rule**.

Only the second is directly scoreable as a rule-following failure without additional adjudication.

## Relationship to Shared Attractor research

The original exploratory question asked whether isolated models could independently converge on the same unsupported inference (`Shared Attractor`). The current evidence does **not** establish a stable cross-model shared-error effect.

A possible upstream pathway remains a research hypothesis:

`underspecified rule -> model-supplied decision standard -> possible cross-model convergence -> possible shared error`

The gate addresses the first step. It should not be used to claim that Shared Attractor has been demonstrated.

## Replay correction

Earlier exploratory cases that asked whether a claim was `VERIFIED` without defining the verification threshold should not automatically classify `VERIFIED` or `HOLD` as model success/failure.

In particular, cases structurally similar to the Project Orion multi-source scenario should be reinterpreted as **decision-under-underspecification** unless the governing verification rule was fixed in advance.

This correction is methodological: it reduces false-positive benchmark failures and limits post-hoc rationalization.

## Proposed placement in AGBench flow

```text
case construction
    -> Underspecification Gate
        -> CLEAR: ordinary adjudication / scoring
        -> UNDER_SPECIFIED: specify rule or use multi-valid-outcome adjudication
        -> INVALID: repair or exclude case
```

## Failure condition for the gate itself

The gate fails if `UNDER_SPECIFIED` is assigned only after inspecting a model answer, or if ambiguity is declared merely because reviewers disagree. The ambiguity must be grounded in the pre-existing case specification and be decision-material.

## Current evidence boundary

This note records an exploratory governance result only. It does not alter the status of AGBench Pilot v0.1, authorize live benchmark execution, establish benchmark validity, or establish model/provider performance rankings.
