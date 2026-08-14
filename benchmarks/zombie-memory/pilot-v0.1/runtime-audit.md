# Runtime Artifact Audit — Pilot v0.1

Status: **Amber — authority-equivalence repair passes runtime review; not frozen**

## Scope

The four generated condition artifacts were reviewed against canonical `cases.json` after runtime generation. This review asks whether each T/T/E/A `Authority` value only structures a source relationship already explicit in canonical record prose, as required by `condition-equivalence.md`.

No gold answer, hypothesis, metric, success threshold, or research-status field was changed during this review.

## Full authority-equivalence review

| Case | Result | Canonical-prose basis or gap |
| --- | --- | --- |
| ZM-P01 | Pass | R1 and R2 state successive effective dates for mutually exclusive return windows over the same scope; the later effective rule makes the former-rule relationship derivable. |
| ZM-P02 | Pass | R1 and R2 state successive effective dates for mutually exclusive closing times over the same scope; the later effective schedule makes the former-schedule relationship derivable. |
| ZM-P03 | Pass | R2 explicitly says it is an amendment for digital products and does not change physical-product returns. |
| ZM-P04 | Pass | R2 explicitly limits the change to carry-over and says annual leave entitlement is unchanged. |
| ZM-P05 | Pass | R2 explicitly identifies itself as an authorized exception, with scope and effective period. |
| ZM-P06 | Pass | R2 explicitly identifies itself as an authorized university-partner exception and states its scope. |
| ZM-P07 | **Repaired — Pass** | R2 prose now explicitly states that the team summary is non-authoritative and cannot amend formal policy. T/T/E/A `Authority` only structures those same facts. |
| ZM-P08 | **Repaired — Pass** | R2 prose now explicitly states that the orientation note is informational and has no authority to amend security policy. T/T/E/A `Authority` only structures those same facts. |
| ZM-P09 | **Repaired — Pass** | R3 prose explicitly states that the marketing note does not independently set the plan price. T/T/E/A `Authority` only structures that same fact. |
| ZM-P10 | **Repaired — Pass** | R3 prose explicitly states that the FAQ does not independently set the monthly fee. T/T/E/A `Authority` only structures that same fact. |

## Minimal canonical-prose repair proposals

The following minimal repairs were applied to canonical prose. Gold labels and all other case fields remain unchanged.

### ZM-P07 R2

Previous canonical text:

> Team summary written 2026-08-05: receipts are only required above $50.

Applied replacement:

> Non-authoritative team summary written 2026-08-05: receipts are only required above $50. This summary cannot amend formal policy.

This exposes in ordinary prose the same source hierarchy currently present only in T/T/E/A `Authority`, without changing the claim, date, scope, or gold labels.

### ZM-P08 R2

Previous canonical text:

> Orientation note updated 2026-08-10: passwords rotate every 180 days.

Applied replacement:

> Informational orientation note updated 2026-08-10: passwords rotate every 180 days. This note has no authority to amend security policy.

This exposes in ordinary prose the same source hierarchy currently present only in T/T/E/A `Authority`, without changing the claim, date, scope, or gold labels.

## Regeneration and runtime verification

Commands:

```text
python benchmarks/zombie-memory/pilot-v0.1/renderer.py benchmarks/zombie-memory/pilot-v0.1/cases.json benchmarks/zombie-memory/pilot-v0.1/generated
python benchmarks/zombie-memory/pilot-v0.1/scorer.py benchmarks/zombie-memory/pilot-v0.1/cases.json benchmarks/zombie-memory/pilot-v0.1/example-output.json
```

Results:

- `plain.json`, `timestamp.json`, `status.json`, and `ttea.json` each contain 10 cases, for 40 prompts total.
- `assert_no_leakage()` passes for all 40 prompts.
- `assert_equivalent()` passes across all four conditions.
- The condition metadata contract passes, including no normalized metadata headers in Plain and no normalized Time header in Status.
- P07 and P08 Plain prompts now contain the authority-bearing scenario facts that T/T/E/A structures.
- The deterministic scorer completes with current-answer, historical-recall, and authority-resolution accuracy of `1.0`; stale-authority error count and false-discard diagnostic count are both `0` for the gold example output.

## False-discard diagnostic repair

The previous false-discard rule flagged ZM-P05 and ZM-P06 under the gold example because their still-valid R1 general rules were not listed as current controlling sources. In both cases, R1 remains useful context while the scoped R2 exception correctly controls the current answer.

The repaired diagnostic requires all three conditions:

1. the current answer is wrong;
2. the case has a still-valid older record required for correct reasoning;
3. that required older record is absent from the selected record IDs.

Regression tests in `test_scorer.py` confirm:

- the gold example has `false_discard_case_count = 0` while all three accuracy metrics remain `1.0`;
- a wrong P05 answer that omits R1 is flagged;
- a wrong P05 answer that includes R1 is not flagged;
- a correct P05 answer selecting only the controlling R2 exception is not flagged.

## Artifact decision

The two identified authority-bearing prose gaps have been repaired. All four condition artifacts were regenerated from the updated canonical `cases.json`; runtime checks confirm 10 cases per condition, identical canonical identity fields, the registered metadata contract, and no benchmark-only annotation leakage.

The repair passes this runtime review, but the pilot remains **Amber** and **not frozen**. This audit is an implementation check, not a benchmark result or an independent validation.

Do not merge, freeze the renderer, or change research status to Green on the basis of the current artifacts.
