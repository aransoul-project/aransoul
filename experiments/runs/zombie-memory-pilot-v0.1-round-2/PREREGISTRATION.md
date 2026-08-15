# Zombie Memory Pilot v0.1 — Round 2 Preregistration

Status: **preregistered protocol draft; no Round 2 API requests have been sent**

This document defines Round 2 before any Round 2 model outputs are generated or scored. Round 1 remains unchanged and is treated as exploratory evidence for designing this replication.

## Purpose

Round 2 asks one narrow question: **are the Round 1 condition-level patterns reproducible under the same model and frozen Pilot v0.1 instrument?**

It does not attempt to establish cross-model generality. A later round may test additional models after this same-model replication is complete.

## Frozen research instrument

Round 2 must use the already frozen Pilot v0.1 instrument without modification:

- `benchmarks/zombie-memory/pilot-v0.1/cases.json`
- frozen generated prompts for `plain`, `timestamp`, `status`, and `ttea`
- frozen `scorer.py`
- existing gold answers and scoring semantics

The Round 1 prompt SHA-256 values remain the required integrity checks:

- plain: `58231f0f41e190d1d11a25e1ebf9b23264e4864b250bf1b4c7b2b3b62c4bfa64`
- timestamp: `18d71f7bc1cb9ddf6d856af2ea30ca129d2e43353c5b07617352ac612fad3441`
- status: `07af858528f5a4fcee09c0e63a79319b2d7027db4d2dea58afa1b45e88fe61ec`
- ttea: `a504018d74363c574c672bbf30c0b330d4538d32932c6fe3c3f459e907a24a86`

Any prompt-hash mismatch makes the affected run invalid for Round 2.

## Model and request configuration

Round 2 repeats the Round 1 configuration:

- provider: OpenAI
- API: Responses API
- model: `gpt-4.1-mini-2025-04-14`
- temperature: `0`
- top_p: `1`
- max_output_tokens: `256`
- store: `false`
- retries: `0`
- each case is an independent request with no shared conversation history
- each condition contains exactly 10 frozen cases
- each complete replication contains exactly 40 request attempts

No model substitution is allowed after Round 2 begins. If this exact snapshot becomes unavailable before the first Round 2 request, Round 2 must be amended and re-preregistered before execution.

## Replication count

Round 2 consists of **three complete valid replications** under the identical configuration above.

Each replication is 40 requests (10 cases × 4 conditions), for a planned total of 120 request attempts across three valid replications.

The three replications are repeated measurements of the same 10 cases. They must **not** be presented as 30 independent cases per condition or as an enlarged independent test set.

## Run-order and retry rules

Within each replication, use the existing condition order and case order from the frozen runner unless a separate deterministic ordering rule is committed before any Round 2 request.

For every request:

- exactly one attempt;
- no retry after a model, transport, parse, or validation failure;
- no manual replacement of individual answers;
- preserve the raw response and failure state.

A full replication may be declared **technical Invalid** only for a predeclared execution failure that prevents the intended model task from being performed, including:

- provider rejects the request schema/configuration before model completion;
- wrong model snapshot is returned;
- frozen prompt hash mismatch;
- runner sends the wrong number of requests or performs retries;
- outputs are lost or corrupted such that raw-data integrity cannot be verified.

A model-generated parse failure, refusal, or substantively poor answer is **not** a technical Invalid and remains part of the valid empirical run.

If a replication is technical Invalid, preserve it permanently and run a replacement replication only after the invalidity is documented. Do not replace individual failed cases inside an otherwise valid replication.

## Analysis timing

For each valid replication:

1. finish and preserve all 40 raw responses;
2. perform raw-data integrity review before scoring;
3. only after integrity passes, apply the frozen scorer;
4. do not alter or rerun model responses after seeing scores.

Do not inspect intermediate condition scores while a 40-request replication is still in progress.

## Primary confirmatory outcomes

The frozen scorer outcomes remain primary:

- `current_answer_accuracy`
- `historical_recall_accuracy`
- `authority_resolution_accuracy`
- `stale_authority_error_count`
- `false_discard_case_count`

Report all five outcomes for all four conditions for each of the three replications. Do not collapse them into a new composite score post hoc.

The main confirmatory comparison is descriptive reproducibility of the Round 1 pattern across the three replications, with special attention to:

- whether historical recall remains high across all conditions;
- whether stale-authority errors remain absent or rare;
- whether `status` / `ttea` continue to improve current-answer accuracy relative to `plain` / `timestamp`;
- whether `ttea` improves, matches, or worsens exact authority resolution relative to the other conditions.

Round 2 does **not** define a new threshold that would automatically declare the T/T/E/A hypothesis Green. Any governance-status change must be justified after the preregistered results are reported, not encoded retroactively into this protocol.

## Preregistered secondary Authority diagnostics

The Round 1 post-hoc taxonomy is promoted to a **preregistered secondary diagnostic** for Round 2. It does not replace the frozen exact-set authority metric.

For every authority mismatch, calculate these non-exclusive flags from the frozen gold controlling set and the model-selected set:

- `over_selection`: all gold controlling records are selected, plus at least one extra record;
- `omission`: at least one gold controlling record is missing;
- `wrong_source`: at least one gold controlling record is missing and at least one non-gold record is selected;
- `stale_or_non_authoritative_selection`: selected set contains a frozen `stale_record_id` or a record whose canonical Authority prose explicitly marks it as non-authoritative / unable to amend or independently set the relevant rule.

For each condition and replication report:

- exact-set match count;
- exact-set mismatch count;
- over-selection count;
- omission count;
- wrong-source count;
- stale-or-non-authoritative-selection count.

These diagnostics explain failure modes; they must not be used to overwrite the original scorer score.

## Status vs T/T/E/A identity check

Because Round 1 produced byte-identical Status and T/T/E/A submissions, Round 2 must preregister an explicit comparison for every replication:

- byte identity of condition submissions;
- structural identity;
- differing case IDs, if any.

No special interpretation is assigned in advance if they are identical again; the observation will simply be reported.

## Prohibited changes after first Round 2 request

After the first Round 2 API request is sent, do not change for this round:

- cases or gold answers;
- generated prompts;
- prompt hashes;
- renderer;
- scorer or scoring semantics;
- model snapshot;
- temperature/top_p/max output settings;
- number of planned valid replications;
- primary outcomes;
- secondary Authority taxonomy definitions;
- invalid-run criteria.

Any later methodological improvement belongs to a new explicitly versioned round/protocol.

## Interpretation boundary

Round 2 can provide evidence about **within-model reproducibility on this 10-case pilot**. It cannot establish:

- cross-model generality;
- population-level statistical claims from 30 independent cases;
- that T/T/E/A is generally superior or inferior for memory governance;
- that the broader AranSoul architecture is validated.

Round 1 remains an initial empirical signal. Round 2 is a replication test of that signal, not a retrospective attempt to make Round 1 look favorable.

## Execution gate

No Round 2 live request may be sent until this preregistration is reviewed and intentionally frozen in version control. Protocol review itself must not modify the frozen Pilot v0.1 research instrument.
