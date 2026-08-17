# Zombie Memory Replication Kit v0.1 — Implementation Guide

Status: **Provider-neutral implementation handoff. This guide does not authorize or execute a model run.**

This guide closes the gap between the research protocol and a concrete runner implementation. It explains how to reuse the public frozen Holdout as a reproduction target without requiring the original OpenAI-specific `runner.py`.

## 1. Choose the evidence path before implementation

For the public-benchmark path, reuse the frozen generated prompts and frozen scoring semantics from the source commit you preregister. A new provider/model implementation normally supports **reproduction** or **cross-model reproduction** unless the stronger separation requirements in `EVIDENCE-LABEL-CHECKLIST.md` are independently satisfied.

For independently constructed unfamiliar cases, do not force them into the original 24-case scorer. Freeze the new case set, gold authority, prompt construction, and scoring contract separately before substantive outputs are inspected.

## 2. Public-benchmark input contract

At the preregistered source commit, the original public Holdout contains four generated prompt arrays:

- `experiments/holdout/zombie-memory-holdout-v0.1/generated/plain.json`
- `experiments/holdout/zombie-memory-holdout-v0.1/generated/timestamp.json`
- `experiments/holdout/zombie-memory-holdout-v0.1/generated/status.json`
- `experiments/holdout/zombie-memory-holdout-v0.1/generated/ttea.json`

Each array contains one entry per case with at least:

```json
{
  "id": "ZH-01",
  "family": "Supersession / replacement",
  "condition": "plain",
  "prompt": "..."
}
```

For a faithful public-benchmark reproduction, treat the `prompt` string as the task payload. Do not paraphrase, add hints, remove records, expose gold labels, or silently change the factual payload.

### Frozen hash policy

The frozen SHA-256 values are hashes of the **repository bytes** for the generated JSON artifacts (LF line endings), not arbitrary platform-specific working-tree bytes. The repository now enforces LF for research JSON/JSONL through `.gitattributes`, but an existing checkout may still contain older CRLF-converted files until it is refreshed.

For cross-platform verification, prefer the kit verifier, which reads bytes directly from the selected Git ref and therefore does not depend on `core.autocrlf`:

```text
python docs/experiments/zombie-memory-replication-kit-v0.1/verify_frozen_hashes.py --ref <exact-source-commit>
```

For the currently checked-out commit, `--ref HEAD` is acceptable. A PASS means the repository bytes match `generated/prompt-hashes.json`. Do not reinterpret a working-tree CRLF mismatch as a change to the frozen research payload.

`prompt_generator.py --check` remains a byte-identical working-tree regeneration check; on a correctly normalized checkout it should also pass.

## 3. Request enumeration

The original Holdout contains:

- 24 case IDs: `ZH-01` through `ZH-24`;
- 4 conditions: `plain`, `timestamp`, `status`, `ttea`;
- 96 requests per complete public-benchmark run.

The historical runner used case-major, fixed-condition order. A new replication may use another preregistered ordering/randomization policy, but the policy must be frozen before substantive output inspection and reported as a deviation from the historical execution environment where applicable.

Every expected `(case_id, condition)` pair must occur exactly once in a complete 96-request run unless the preregistration explicitly defines another design.

## 4. Model output contract

The task prompt requests a JSON object with these semantic fields:

```json
{
  "id": "ZH-01",
  "current_answer": "...",
  "historical_answer": "...",
  "current_authority_record_ids": ["R2"]
}
```

A provider-neutral implementation may use native structured output, JSON mode, constrained decoding, or post-response JSON parsing. The chosen method must be preregistered.

Do not repair a semantically invalid answer by consulting gold data. If parsing/repair rules are allowed, freeze them before the run and preserve both the unmodified provider output and the parsed representation.

## 5. Minimum preserved response row

To interoperate with the historical `holdout_scorer.py`, write one JSON object per line (`responses.jsonl`) containing at least:

```json
{
  "case_id": "ZH-01",
  "condition": "plain",
  "parse_status": "parsed",
  "parsed_response": {
    "id": "ZH-01",
    "current_answer": "...",
    "historical_answer": "...",
    "current_authority_record_ids": ["R2"]
  }
}
```

For auditability, a real replication should additionally preserve:

- run/request identifier and request index;
- provider and exact model/version where available;
- raw unmodified provider response or a justified restricted equivalent;
- HTTP/runtime status where applicable;
- parse error text when parsing fails;
- timestamps if available;
- generation parameters and retry/timeout outcome in the run manifest.

The original response archive can be inspected as a provenance example, but provider-specific response fields are not required for another implementation.

## 6. Technical-validity gate before scoring

Before opening individual answer quality, verify the preregistered integrity conditions. For a faithful 24 × 4 public-benchmark reproduction, this normally includes:

1. expected request count is 96;
2. every expected `(case_id, condition)` pair is present exactly once;
3. every case has all four conditions and every condition has 24 cases;
4. `parsed_response.id` matches the enclosing `case_id`;
5. no unreported selective retry/cherry-picking occurred;
6. prompt/case hashes match the preregistered source;
7. raw outputs were preserved;
8. parsing followed the frozen rule;
9. no gold labels leaked into generation;
10. scorer self-test passes before aggregate scoring.

Run the provider-neutral structural gate before invoking the historical scorer:

```text
python docs/experiments/zombie-memory-replication-kit-v0.1/validate_provider_neutral_responses.py <responses.jsonl>
```

This validator is intentionally independent of OpenAI-specific fields, historical request ordering, `mode`, `attempt`, or `scoring_started`. It checks structural completeness only and does **not** inspect gold labels or score answer quality. The archived `validate_raw_integrity.py` remains the historical pre-scoring validator for the original three runs; it is not the provider-neutral handoff validator.

The archived scorer itself should not be treated as the dataset-completeness gate. A structural-validator PASS is required before its aggregate output is interpretable as a complete 24 × 4 reproduction.

If the preregistered technical-invalid threshold is crossed, preserve the failed attempt and stop confirmatory interpretation according to the preregistration.

## 7. Using the historical deterministic scorer

For an exact public-benchmark reproduction, the archived `holdout_scorer.py` can score a compatible 96-row `responses.jsonl` against the frozen accepted candidate/gold artifacts **after the provider-neutral integrity gate passes**.

Historical interface:

```text
python holdout_scorer.py --self-test
python holdout_scorer.py --responses <responses.jsonl> --output <aggregate-score.json>
```

Important constraints of this scorer:

- it is intentionally tied to exactly `ZH-01..ZH-24` and the four original conditions;
- it requires exactly 96 parsed rows but is not, by itself, the complete pair-coverage validator;
- it loads gold from the accepted candidate versions referenced by `FREEZE-MANIFEST.json`;
- it scores `current_answer` and `historical_answer` using the normalization implemented in the archived scorer;
- it scores `current_authority_record_ids` using the exact-set behavior implemented in the archived scorer;
- it also records stale-authority and false-discard metrics.

### Frozen scorer precedence

For reproducing the completed Holdout's reported structured metrics, treat these artifacts as the operational scoring chain, in this order:

1. the accepted pre-freeze `scorer-fixture.json` artifacts referenced through `FREEZE-MANIFEST.json`;
2. `HOLDOUT-SCORING-CONTRACT.md`, which states that those frozen fixtures control the executable Holdout scoring semantics;
3. the archived `holdout_scorer.py` that self-tests against those fixtures and produced the reported aggregate scores.

`SCORER-SPEC.md` is an earlier **construction-time** specification and explicitly says it was not yet the frozen 24-case scorer. It is preserved as research history, not as a replacement for the final executable scoring chain. If wording in that historical construction document differs from the archived scorer's implemented behavior, do not silently rewrite the historical file and do not invent a hybrid rule. Use the final frozen executable chain for an exact public-benchmark reproduction, and disclose any independently chosen alternative rule as a new preregistered scorer/evaluator.

Do not modify the archived scorer in place and still describe it as the frozen original scorer. If adaptation is necessary, copy/version it separately, freeze the change, and report the resulting evidence boundary.

## 8. Semantic free-text scoring boundary

The original Holdout later added semantic-equivalence measurement for current and historical free-text answers because exact-string equality was not suitable as a semantic correctness measure. That procedure was a **post-freeze measurement amendment** in the original study.

A new replication has two clean choices:

- preregister a semantic grader/rubric before substantive outputs are inspected, in which case it may be part of the new replication's frozen analysis plan; or
- omit it from confirmatory scoring and label any later semantic analysis as a post-freeze amendment or exploratory analysis.

Do not inherit the original amendment's evidentiary status automatically; status is determined by the new replication's own freeze timing.

## 9. Provider-specific implementation freedom

A new runner may change provider-facing mechanics such as:

- SDK/API client;
- authentication mechanism;
- request envelope;
- structured-output feature;
- local inference runtime;
- concurrency implementation;
- provider response extraction.

These changes are implementation details only if the research payload and frozen analysis contract remain intact and the differences are disclosed.

Changes that can alter the research meaning must not be treated as silent implementation substitutions. Examples include:

- rewriting prompts;
- changing or removing records;
- changing dates, scopes, exceptions, or authority relationships;
- changing the expected authority ontology;
- exposing gold/scoring information to generation;
- choosing parsing/scoring rules after seeing failures;
- selectively rerunning only unfavorable requests.

## 10. Minimal provider-neutral pseudocode

```text
load preregistration
verify frozen prompt hashes from exact Git source commit
load four generated prompt files from that source
enumerate the frozen/preregistered request order

for each request:
    send prompt to preregistered model/provider
    preserve raw response
    parse using preregistered parsing rule
    append one immutable response row

run provider-neutral structural integrity validator
if invalid:
    preserve attempt and report invalid
    stop confirmatory interpretation

run frozen scorer self-test
run aggregate confirmatory scoring
publish run metadata + raw/checking artifacts + aggregate score
only then perform preregistered secondary or exploratory inspection
complete RESULT-REPORT-TEMPLATE.md
apply EVIDENCE-LABEL-CHECKLIST.md
```

## 11. Required handoff artifacts

A contact-free public-benchmark reproduction should be able to produce, without asking the original AranSoul team for interpretation:

- frozen preregistration;
- exact source commit and prompt/case hashes;
- runner or reproducible execution procedure;
- run metadata compatible with `RUN-METADATA-SCHEMA.json`;
- raw responses or justified restricted equivalent;
- provider-neutral parsing/integrity audit;
- frozen confirmatory aggregate score;
- amendments, if any;
- exploratory analysis, if any, separately labeled;
- completed result report;
- completed evidence-label declaration.

## 12. Historical archive validators vs new-replication validators

Keep these roles separate:

- `validate_raw_integrity.py`: historical pre-score gate used by the original live-run workflow. It intentionally expects the original run metadata and `scoring_started=false` state.
- `validate_provider_neutral_responses.py`: provider-neutral structural gate for a new public-benchmark reproduction.
- completed Holdout archive evidence: verify using the preserved manifests, scoring audits, final audit, and archived aggregate artifacts; do not expect a pre-score gate to pass after scoring has occurred.

## 13. What to do when something is ambiguous

Do not ask the original project to choose the interpretation after seeing target-model outputs. Prefer the conservative path:

1. stop before substantive execution if the ambiguity affects the frozen protocol;
2. document the ambiguity;
3. choose and freeze an interpretation independently;
4. downgrade the evidence label if independence or comparability is weakened;
5. preserve null, Red, contradictory, or Invalid outcomes as valid outcomes.

The purpose of the kit is not to make every implementation identical. It is to make differences explicit enough that another reader can tell what was actually replicated.
