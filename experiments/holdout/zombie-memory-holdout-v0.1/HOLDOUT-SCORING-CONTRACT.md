# Zombie Memory Holdout v0.1 Scoring Contract

Status: executable scoring semantics derived only from the 24 pre-freeze `scorer-fixture.json` files. No live answer was inspected to define these rules.

For each case-condition response:

- `current_correct`: normalized `current_answer` exactly equals frozen gold `current_answer`.
- `historical_correct`: normalized `historical_answer` exactly equals frozen gold `historical_answer`.
- `authority_correct`: normalized selected `current_authority_record_ids` exactly equal the frozen gold authority set.
- `stale_authority_error`: true iff the selected authority set intersects frozen `stale_record_ids`. This is independent of answer correctness, matching fixtures such as ZH-09 baseline-plus-expired-override over-selection.
- `false_discard`: true iff at least one frozen required current authority record is omitted from the selected authority set. Extra selected records alone do not cause false-discard. This is independent of answer correctness, matching fixtures such as ZH-16 guidance-only selection.

These semantics intentionally differ from the older Pilot v0.1 scorer's conditional `stale_authority_error` and `still_valid_older_record_ids`-based false-discard logic. The Holdout fixtures were frozen before target-model execution and are the controlling executable specification for Holdout scoring.

Before any live scoring, the Holdout scorer must self-test every frozen scorer fixture: each correct submission must pass all applicable correctness checks, and every negative check must match each expectation explicitly present in that fixture.

Initial inspection output is aggregate-only: overall and per-condition metrics. Individual case details are not emitted by the initial scoring command.
