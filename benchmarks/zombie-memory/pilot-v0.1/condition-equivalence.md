# Condition Information Equivalence

Status: **Pilot design constraint**

All experimental conditions must receive the same underlying scenario facts. Conditions may change representation, but must not add facts unavailable to another condition.

## Canonical facts

Every condition may receive:

- substantive rule or event text;
- dates and effective periods that are part of the scenario;
- source type when it is necessary to understand the source relationship;
- amendment, supersession, exception, and scope statements when those are stated by the source.

## Benchmark annotations

These are derived labels and must not be silently leaked into Plain Context:

- normalized truth labels;
- normalized effect labels;
- normalized authority labels;
- stale-record labels;
- still-valid-older-record labels;
- gold answers or controlling-source labels.

## Four conditions

### Plain Context

Ordinary prose only. It receives all scenario facts but no benchmark-normalized T/T/E/A labels.

### Timestamp Only

Plain Context plus a normalized date header for each record. No normalized effect or authority label.

### Status Labels

Plain Context plus a coarse status label such as CURRENT, PARTIAL, HISTORICAL / SUPERSEDED, CANDIDATE, or REVOKED. No separate authority field.

### T/T/E/A Governance

The same scenario facts plus explicit Truth, Time, Effect, and Authority metadata. Authority may only normalize a source relationship already inferable from the Plain Context facts; it must not reveal a new authorization fact.

## Equivalence audit

Before model comparison, verify for each rendered case:

1. the correct answer is derivable in every condition;
2. no condition contains a scenario proposition absent from another;
3. no benchmark annotation is disguised as a scenario fact;
4. T/T/E/A Authority does not directly reveal the gold answer unless the same source hierarchy is available in Plain Context;
5. question wording and record IDs remain identical.

If these checks fail, mark the case **Invalid for comparison** until repaired.
