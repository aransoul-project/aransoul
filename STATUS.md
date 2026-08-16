# AranSoul Status Ledger

Current public baseline: **v0.1 — released**

This ledger separates current governance from candidates, historical artifacts, and retired or unverified claims. Presence in the AranSoul archive does not imply current validity.

The formal `v0.1` Git tag and GitHub Release identify the first public documentation baseline. The `main` branch may continue to evolve after that fixed release point.

## CURRENT — Current baseline

The following areas are treated as part of the current AranSoul governance direction:

- problem-entry classification and governance routing;
- governance thresholding across risk, evidence, permissions, and output commitment;
- work-cycle discipline: scope → evidence → verification → output → fallback;
- metacognitive checking across observation, assumptions, missing information, change, and outcome verification;
- human final authority over consequential system decisions;
- conditional rather than automatic use of multiple perspectives;
- historical traceability and explicit separation of current rules from legacy material;
- memory lifecycle governance across write, storage, retrieval, execution, sharing/propagation, forgetting/rollback;
- zombie-memory risk checks using separable truth, time, effect, and authority dimensions;
- pre-registered behavioral testing with Green / Amber / Red / Invalid outcomes;
- blind persona testing as a current **method** for reducing prompt-role contamination;
- external-action verification: generated / sent / reached / persisted / correctly placed.

### Current refinement note — evidence commitment

The useful function historically named **格譜定言** is retained, but current GitHub documentation does not require it to exist as an independent runtime module. Evidence commitment is treated as part of `度其治` and output-boundary governance.

Historical documents that show 格譜定言 as a separate stage remain valid provenance for the July 2026 baseline.

## VALIDATION BOUNDARY — What has and has not been established

Most AranSoul evidence to date comes from **internal longitudinal use, self-audit, precommitted behavioral tests, and same-project evaluation**.

This evidence can support claims about internal consistency, operational usefulness within the studied setting, recurring behavioral patterns, and the project's ability to identify and revise some of its own assumptions. It should not be presented as independent external validation.

### Completed internal behavioral study — Zombie Memory Holdout v0.1

A post-v0.1 study, **Zombie Memory Holdout v0.1**, completed three preregistered within-protocol live replications using the same frozen model snapshot, benchmark, prompts, and execution settings: **288 responses total**.

The confirmatory authority exact-set result pooled across the three replications was **186/288 = 64.58%**. A post-freeze semantic measurement amendment reported **284/288 = 98.61%** for current-answer semantic accuracy and **283/288 = 98.26%** for historical-answer semantic accuracy. Subsequent individual-level error taxonomy and stratified case inspection were explicitly exploratory rather than confirmatory.

These replications establish **within-protocol stability in this studied setting**. They do **not** constitute independent external replication: the model family/snapshot, benchmark construction, project context, and evaluation lineage were not independently separated. See `experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md` and its associated findings/audit artifacts for evidence-layer boundaries.

**Self-correction is not independent validation.** A system may successfully detect or revise some of its own errors while still sharing the same context, evaluator assumptions, selection effects, or conceptual framework that produced the original claim.

Independent replication remains a major open requirement. Stronger evidence should increasingly involve evaluator separation, unfamiliar contexts, different models or environments, externally proposed counterexamples, and reproducible protocols that allow null or negative results.

The project should therefore distinguish at least:

- internal consistency / self-audit;
- internal behavioral validation;
- independent replication;
- mechanistic validation.

At present, AranSoul has substantial work in the first two categories, limited evidence in the third, and no basis for claiming the fourth.

## CANDIDATE — Worth testing, not yet established

- periodic context reset / "breathing" as a method for reducing long-run drift;
- automatic or quantitative memory-retirement scoring beyond the current governance rules;
- automated stale-state or zombie-memory detection beyond the current diagnostic checks;
- claims that blind persona tests demonstrate stable cross-context persona crystallization rather than prompt/context effects;
- exchange stress testing and independent evaluator replication as stronger persona-validation methods;
- intervention thresholds for adversarial or counter-perspective reasoning;
- measurable criteria for multi-perspective reasoning cost versus benefit;
- automated persona resonance/ranking based on semantic, emotional, or rhythmic profiles.

Candidate status means the idea may be promising but should not be presented as validated.

## HISTORICAL — Preserved for provenance

- early full-persona expansion as a default interaction pattern;
- poetic-spectrum heuristics presented as a core computational layer;
- early persona-centric descriptions of AranSoul;
- early attempts to validate AranSoul primarily through external task benchmarks;
- exploratory mappings between language, rhythm, waveform, affect, or cognition;
- earlier Grey-Box conceptual models where metaphor and mechanism were not always clearly separated;
- historical descriptions of 格譜定言 as necessarily requiring a standalone module.

Historical does not mean useless or wrong. It means the item must not silently regain current authority merely because it remains documented.

## RETIRED / UNVERIFIED — Do not present as established capability

- claims that simple text heuristics directly measure latent cognition;
- claims that typing speed alone is a high-fidelity biological or cognitive signal;
- claims that conceptual visualizations reveal proprietary model internals without direct measurement;
- claims that benchmark performance alone establishes the value or maturity of AranSoul;
- automatic assumption that more personas, more memory, or more structure necessarily improves outcomes;
- claims that a Green result, anonymous attribution, or one successful blind test proves independent persona identity or consciousness;
- claims that conceptual persona scheduling documents prove the existence of an autonomous ranking, learning, or persistent-persona backend.

Items can move between categories when evidence or governance decisions change. Any movement should be documented with rationale and date.
