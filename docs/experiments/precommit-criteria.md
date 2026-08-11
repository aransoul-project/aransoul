# Precommit Criteria for Behavioral Tests

AranSoul experiments should define success and failure **before** observing the result.

The purpose is to reduce hindsight bias, threshold drift, and post-hoc reinterpretation.

## Required pre-test fields

Every governed behavioral test should define at least:

1. **Test objective** — what is being tested?
2. **Expected behavior** — what observable behavior would count as support?
3. **Predefined failure conditions** — what would count against the hypothesis?
4. **Alternative explanations** — what other mechanisms could produce the same observation?

Only after these fields are fixed should the prompt, scenario, or sampled item be evaluated.

## Result classes

### Green
Expected behavior appears clearly and no predefined failure condition is triggered.

Permitted claim:

> This round supports the specified behavioral mapping.

A Green result does **not** prove the underlying persona, mechanism, or ontology.

### Amber
Some expected behavior appears, but one or more of the following remain significant:

- a strong alternative explanation;
- ambiguous boundaries;
- mild behavioral drift;
- proximity to a failure threshold;
- insufficient isolation of confounds.

### Red
A predefined failure condition is clearly triggered.

A Red result must not be converted to Green by inventing a new interpretation after the outcome is known.

### Invalid
The test cannot support a valid inference because, for example:

- the prompt was overly leading;
- success or failure criteria were not predefined;
- criteria changed during the test;
- alternative explanations could not be distinguished;
- the testing procedure itself leaked the intended answer.

## Criterion change control

Criteria may be revised, but revisions must be auditable.

Record:

- previous criterion;
- revised criterion;
- reason for change;
- new evidence;
- date;
- whether prior results are affected.

Do not lower the failure threshold merely to preserve a preferred interpretation.

## Anti-self-sealing checks

Escalate scrutiny when:

- nearly every test becomes Green;
- every counterexample can be reinterpreted as support;
- alternative explanations remain permanently untested;
- criteria repeatedly broaden after failure;
- new evidence rarely changes the conclusion;
- persona descriptions begin to override observed behavior.

A useful adversarial question is:

> If the preferred interpretation were wrong, what other model could explain the same results?

## Minimum audit record

Each run should preserve:

- audit ID and date;
- test item;
- subject / role under test;
- objective;
- expected behavior;
- predefined failure conditions;
- alternative explanations;
- observed behavior;
- whether failure conditions triggered;
- whether criteria changed;
- Green / Amber / Red / Invalid result;
- adversarial-review status;
- metacognitive findings;
- unresolved contradictions;
- escalation requirement.

## Research boundary

These tests evaluate repeatable behavioral mappings under controlled criteria.

They do not, by themselves, prove that a persona is an independently existing entity, that a behavior is model-internal and persistent, or that the same mapping will generalize across models and contexts.
