# Zombie Memory Preprint v0.1 — Manuscript Adversarial Audit

Status: reviewer-style audit of `COMPLETE-MANUSCRIPT-DRAFT.md`; no manuscript edits in this audit.

## Overall verdict

**AMBER — scientifically coherent draft; publication-facing clarification still needed.**

The manuscript preserves the core evidence boundary correctly and no contradiction was found that changes the reported Holdout v0.1 results. The remaining concerns are primarily about publication interpretation, provenance visibility, and citation normalization rather than benchmark validity.

## Blocking

None identified that would invalidate the underlying Holdout result.

Before public preprint release, however, the manuscript still requires the human publication name and an immutable publication snapshot/tag as already acknowledged in the manuscript workspace.

## Important

### 1. Clarify the repeated-measures nature of the pooled 288 responses

The manuscript reports 288 substantive model responses and a pooled 186/288 authority exact-set result. These are valid descriptive counts, but the 288 responses are not 288 independent benchmark cases: the same 96 case-condition units were executed three times under the same frozen protocol and model snapshot.

The manuscript repeatedly labels the runs as within-protocol replications, which is good, but a reviewer could still read the pooled denominator as an independent sample size. Before publication, explicitly state that the pooled 288 are repeated observations over 96 frozen case-condition units and are not treated as 288 independent experimental units for statistical generalization.

This clarification does not change any reported percentage.

### 2. Define what `blind` means or remove the term where unnecessary

The manuscript and archived audit use the phrase `blind live replications`, but the manuscript does not define the blindness protocol. A publication reader may interpret `blind` as evaluator blinding, model blinding, author blinding, or withheld individual-output inspection.

Before publication, either define exactly what was blinded and at which stage, with a repository artifact supporting it, or use the narrower factual phrase `planned live within-protocol replications`.

### 3. Archive or weaken the Codex RED-to-GREEN handoff-audit claim

The Reproducibility section states that a Codex agentic cold-start audit first returned RED and later GREEN after handoff fixes. The repository contains the resulting fixes and replication-kit artifacts, but this audit did not locate a repository-local artifact containing both externalized audit reports themselves.

If this history remains in the paper as provenance evidence, archive the audit reports (or a concise immutable audit record) in the repository. Otherwise, rewrite the sentence as an engineering-development note without presenting the RED/GREEN sequence as independently inspectable evidence.

This issue affects handoff provenance only, not the scientific result.

### 4. Normalize Related Work against the final cited paper versions

The current Related Work positioning is conservative and appropriately avoids priority claims. Before publication, re-check each cited paper against its latest public version and normalize terminology, year/version metadata, and contribution descriptions.

One specific reason is that evolving preprints can change labels across versions (for example, memory competencies may be described differently across versions). The final bibliography should cite a clearly identified version or publication record and the prose should match that version.

### 5. Avoid inferential language unsupported by the repeated design

The manuscript currently uses mostly descriptive language, which is appropriate. Maintain that discipline during formatting: do not add confidence intervals, significance claims, or language implying population-level estimates by treating the 288 repeated responses as independent observations unless an explicit repeated-measures analysis is preregistered or transparently added as a new post-study analysis.

## Nice-to-have

### 1. Add a compact evidence-status table

A one-table summary near Results or Reproducibility could reduce reader error:

- Authority exact-set 186/288 — preregistered confirmatory structured metric.
- Current semantic 284/288 — post-freeze measurement amendment.
- Historical semantic 283/288 — post-freeze measurement amendment.
- 102/102 over-selection — exploratory structural taxonomy.
- Stratified extra-record roles — exploratory sample.

### 2. Add direct repository pointers for the central evidence chain

The Reproducibility section names directories but could point more directly to the final audit, findings, preregistration/freeze manifests, scorer contract, raw response archives, and replication kit. A publication snapshot/tag should be used for the final links.

### 3. Consider whether the phrase `authority-boundary precision` could be confused with precision as a formal metric

The manuscript uses `precision` in ordinary English. Because exact-set accuracy is the actual metric, replacing some instances with `authority-boundary exactness` or `authority-boundary identification` may avoid confusion with statistical precision/IR precision.

### 4. Keep the AI-assistance disclosure concise in the final formatted paper

The current disclosure is transparent and appropriate for the working manuscript. Venue-specific formatting may benefit from moving some implementation history to supplementary material while keeping human responsibility and substantive AI uses explicit.

## PASS areas

- Main authority result matches the final repository audit: 61/96, 63/96, 62/96; pooled 186/288 = 64.58%.
- Condition-level counts match the final repository audit.
- Semantic results remain explicitly post-freeze amendment evidence.
- The 102/102 over-selection result remains exploratory.
- Stratified exploratory counts are consistent with the archived findings.
- The manuscript explicitly distinguishes within-protocol replication from independent external replication.
- T/T/E/A condition differences are not given a causal interpretation.
- Authority is framed as a benchmark-defined construct rather than a universal ontology.
- Related Work positioning is narrow and does not claim priority over stale-memory or memory-authority research broadly.
- Limitations explicitly restrict model, benchmark, mechanism, causal, and production-system generalization claims.

## Acceptance recommendation

Do not run new live model experiments for these manuscript issues.

Recommended sequence:

1. run a cold-start Codex reviewer audit against the current complete manuscript and repository;
2. compare independent reviewer findings with this audit;
3. repair only supported manuscript/provenance issues;
4. rerun the same reviewer audit;
5. require GREEN or a documented AMBER-with-nonblocking-notes before freezing the publication snapshot.

The paper should not be frozen or submitted solely because the manuscript is complete. It should first pass a reproducible reviewer-style acceptance audit under the same evidence-boundary rules used elsewhere in the project.
