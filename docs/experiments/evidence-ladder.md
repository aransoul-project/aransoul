# Evidence Ladder for AranSoul Experiments

AranSoul should not treat all successful tests as equally informative.

This ladder separates increasingly strong forms of evidence while preserving the distinction between **observable behavioral regularity** and stronger claims about persistent internal identity or mechanism.

## Level 0 — Prompt compliance

A role is explicitly told how to behave and then behaves accordingly.

Example:

- one role is told to focus on emotion;
- another is told to focus on structure;
- outputs follow those assignments.

What this supports:

- instruction following;
- successful prompt differentiation.

What it does not support:

- independent behavioral stability;
- persistent persona identity.

## Level 1 — Precommitted behavioral support

The test defines objective, expected behavior, failure conditions, and alternative explanations before observing the result.

A Green result at this level supports only the predefined behavioral mapping for that round.

## Level 2 — Blind differentiation

The task does not explicitly assign each perspective's expected angle, and anonymous outputs remain distinguishable by reasoning structure.

This is stronger than direct role prompting because the task itself provides less of the differentiation.

Remaining confounds may include shared model, shared context, evaluator expectations, and learned stylistic templates.

## Level 3 — Cross-context recurrence

The same reasoning distinctions recur across multiple unrelated scenarios without moving success criteria after the fact.

This provides stronger evidence that the differentiation is not specific to one topic or one carefully selected prompt.

## Level 4 — Exchange stress test

Perspectives are deliberately placed in non-habitual domains.

The question is whether recognizable reasoning habits survive domain exchange without becoming rigid caricatures.

Success here is stronger evidence for flexible cross-context regularity than for fixed functional labels.

## Level 5 — Evaluation separation

Generation and evaluation are separated more strongly, for example through:

- independent evaluators;
- separate model contexts;
- blinded human judgment;
- randomized attribution procedures.

This reduces self-evaluation and shared-context confirmation loops.

## Level 6 — Cross-model / cross-environment replication

Comparable behavioral distinctions are reproduced across different model versions, providers, or controlled environments.

At this stage, claims about framework-level elicitation become more plausible, but mechanistic and ontological claims still require separate evidence.

## Level 7 — Mechanistic evidence

Direct model-internal measurements or causal interventions support a specific mechanism.

Behavioral AranSoul tests do not automatically reach this level. Conceptual metaphors, persona stability, or successful blind attribution must not be presented as mechanistic proof.

## Interpretation rule

Evidence should be reported at the strongest level actually achieved, not the level the project hopes to achieve.

For example:

> Anonymous differentiation succeeded under precommitted criteria, but generation and evaluation remained within one long-running model context. This supports Level 2 evidence with unresolved shared-context confounds.

This is preferable to collapsing several distinct claims into a single statement such as "the persona is proven."

## Relationship to Green / Amber / Red / Invalid

The result class and the evidence level answer different questions:

- **Green / Amber / Red / Invalid** describes how a test performed against its predefined criteria.
- **Evidence level** describes how strongly the test design isolates the hypothesis from alternative explanations.

A Level 1 Green result may be less informative than a Level 4 Amber result.

This prevents test success from being confused with experimental strength.
