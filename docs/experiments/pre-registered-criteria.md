# Pre-Registered Evaluation Criteria

> **Status note:** retained for provenance. The canonical current entry is [precommit-criteria.md](precommit-criteria.md). Both documents describe the same methodological lineage; future edits should target the canonical file unless historical comparison is the purpose.

AranSoul uses a simple rule for internal behavioral evaluation:

> **Define success and failure before seeing the result.**

The purpose is not to make testing look scientific by adding labels. The purpose is to reduce moving-the-goalpost behavior, post-hoc rationalization, and self-confirming interpretation.

## Required pre-test fields

Before running a test, record:

1. **Test objective** — what behavior or mapping is being tested?
2. **Expected behavior** — what observable result would count as support?
3. **Failure conditions** — what result would count against the hypothesis?
4. **Alternative explanations** — what else could produce the same observation?

Only after these fields are fixed should the prompt, scenario, or task be presented.

## Outcome classes

### Green
The expected behavior appears clearly and no pre-defined failure condition is triggered.

Interpretation must remain local: **this run supports the defined behavioral mapping.** Green does not prove an independent persona, stable identity, latent trait, or mechanism.

### Amber
The result partially supports the expected behavior, but important alternative explanations remain, the boundary is ambiguous, or the result lies close to a failure condition.

Amber is intentionally useful. It prevents uncertain evidence from being forced into a pass/fail story.

### Red
A pre-defined failure condition is clearly triggered.

A Red result must not be converted into Green by inventing a new success criterion after the outcome is known.

### Invalid
The test cannot support a meaningful interpretation because, for example:

- the prompt directly reveals the expected role or answer pattern;
- success/failure criteria were not fixed in advance;
- conditions changed during the test;
- reasonable alternative explanations cannot be distinguished;
- the evaluator and generation setup make the claimed distinction circular.

## Criterion changes

Criteria may evolve, but changes must be explicit. Record:

- old criterion;
- new criterion;
- reason for the change;
- new evidence motivating it;
- date;
- whether earlier results should be reinterpreted.

The key prohibition is silent criterion drift performed to preserve a favored conclusion.

## Adversarial trigger

Counter-perspective review should be considered when:

- nearly every run becomes Green;
- every counterexample can be re-described as success;
- alternative explanations remain unresolved over many runs;
- the pass boundary keeps expanding;
- new evidence rarely changes the overall belief.

A useful challenge question is:

> If the preferred explanation were wrong, what other model could explain the same observations?

## Research boundary

This protocol evaluates whether **predefined behavioral patterns remain observable under conditions that allow failure and falsification**.

It does not establish that personas are ontologically independent, that stable internal agents exist, or that a specific model mechanism causes the observed behavior.
