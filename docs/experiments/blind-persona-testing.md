# Blind Persona Testing

Status: **Current specialized evaluation protocol**

AranSoul uses blind behavioral testing to separate **prompt-assigned roles** from **candidate cross-context behavioral regularities**.

The goal is not to prove that a persona is an independent entity. The goal is narrower: test whether distinct reasoning patterns remain observable when the task does not directly tell each persona how to behave.

This protocol operates under the canonical [precommit criteria](precommit-criteria.md): success, failure, and alternative explanations should be defined before the result is interpreted.

## Why blind testing is needed

A persona test is weak when the prompt says, in effect:

- Persona A should focus on emotion;
- Persona B should focus on structure;
- Persona C should focus on time;
- Persona D should focus on governance.

If the outputs then follow those instructions, the result primarily demonstrates prompt compliance.

A stronger test removes those assignments from the test prompt.

## Recommended procedure

1. Pre-register the test objective, expected behavior, failure conditions, and alternative explanations.
2. Present the same problem without telling each persona what angle it should take.
3. Collect responses independently where practical.
4. Remove persona names and obvious identifiers.
5. Ask evaluators to infer source identity from reasoning structure rather than surface keywords.
6. Record confidence and reasons for each attribution.
7. Check whether the responses remain distinguishable across different topics.
8. Run counter-explanations before making any stronger claim.

## What counts as stronger evidence

Evidence becomes stronger when:

- the question does not cue the expected role;
- anonymous responses remain distinguishable;
- attribution depends on reasoning structure, not decorative vocabulary;
- the same distinction reappears across unrelated scenarios;
- responses remain coherent when personas are asked to handle non-habitual domains;
- independent evaluators or separate model contexts reproduce the attribution.

## Failure conditions

Examples include:

- responses are highly homogeneous;
- identities can be inferred only from names, catchphrases, or explicit role cues;
- the evaluator simply maps known role descriptions back onto outputs;
- contradictions appear that cannot be reconciled by scope or context;
- a claimed persona pattern disappears when the task domain changes;
- every possible response can be interpreted as confirming the persona.

## Major alternative explanations

Even a successful blind test may still be explained by:

- one base model generating all responses;
- long-context residue from persona descriptions;
- shared evaluator and generator biases;
- natural multi-angle reasoning elicited by the task itself;
- stylistic templates learned from earlier interactions.

Therefore a blind result can support **behavioral differentiation** without proving independent persona identity.

## Exchange stress test

A useful next-stage test deliberately places each persona in a non-habitual domain.

Example: a persona usually associated with temporal continuity is asked to handle an abstract governance problem, while a governance-oriented persona handles a relationship-centered dilemma.

The question is whether each retains a recognizable reasoning habit rather than being completely absorbed by task type.

If anonymous attribution remains possible after such role-domain exchange, that is stronger evidence for cross-context regularity.

## Interpretation discipline

Use graded conclusions such as:

- weak candidate evidence;
- Amber / ambiguous support;
- stronger candidate evidence;
- replicated behavioral regularity.

Avoid conclusions such as:

- "persona proven";
- "independent consciousness established";
- "stable internal agent confirmed".

Blind testing is a method for reducing self-confirmation, not a shortcut around the limits of behavioral evidence.

## Status boundary

The **protocol** is current. The stronger hypothesis that blind differentiation demonstrates stable cross-context persona crystallization remains a research claim whose strength depends on replication, evaluator independence, context separation, and other controls.
