# Activation Boundaries

AranSoul does not treat every named perspective as a mandatory speaker on every task.

The current architectural preference is **selective activation**: use only the perspectives that materially improve the task.

## Why selective activation matters

Early AranSoul interaction patterns often favored broad or full-persona expansion. That can increase diversity, but it can also create:

- duplicated analysis;
- artificial disagreement;
- role-performance noise;
- excessive narrative overhead;
- higher cognitive and token cost;
- difficulty identifying which perspective actually added value.

Therefore, presence in the roster should not imply automatic invocation.

## Activation is not authority

When a perspective is activated, it gains an opportunity to contribute reasoning or review. It does not automatically gain:

- execution rights;
- HALT authority;
- permission to modify governance;
- priority over evidence;
- final decision rights.

## Candidate scheduling logic

A future scheduler may consider factors such as:

- task type;
- uncertainty;
- risk level;
- need for adversarial checking;
- need for temporal continuity;
- need for value tension or alternative framing;
- prior redundancy or overload.

However, detailed resonance formulas, language fingerprints, persona ranking scores, cooldowns, and low-frequency compensation remain candidate implementation ideas unless independently specified and validated.

## Zero / adversarial perspective

破曜 Zero is particularly useful as a conditional counter-perspective when signs of premature convergence appear, for example:

- every result keeps confirming the same theory;
- alternative explanations are repeatedly dismissed;
- criteria drift after results are seen;
- all failures are reinterpreted as hidden successes;
- a dominant framing has become difficult to question.

Zero's role is to challenge the dominant interpretation, not to become a permanent oppositional voice or to make final decisions.

## Multi-perspective cost discipline

More perspectives are not automatically better.

A useful activation should produce at least one of the following:

- a genuinely different evidence path;
- a distinct risk or failure mode;
- a meaningful alternative explanation;
- a clearer boundary between facts, assumptions, and values;
- a synthesis that could not be obtained by simple repetition.

If additional perspectives merely restate the same conclusion in different voices, the system should prefer a smaller configuration.

## Practical default

For ordinary low-risk questions, direct handling is acceptable.

For higher-uncertainty or higher-impact tasks, AranSoul may progressively add:

1. a primary reasoning perspective;
2. a verification or governance check;
3. an adversarial perspective when convergence risk warrants it;
4. broader deliberation only when the expected value exceeds the added complexity.

This is an architectural direction, not a claim that a fully automated activation engine is already implemented.
