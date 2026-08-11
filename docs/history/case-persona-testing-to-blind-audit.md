# Case Study: From Persona Confirmation to Blind Behavioral Audit

## Original assumption

Early persona tests often asked named roles to answer questions while their expected functions were already visible in the prompt or surrounding context. If the resulting answers matched those descriptions, the system could appear to show stable differentiated personas.

## Observed problem

That design confounded several explanations:

- direct prompt compliance;
- long-context residue from role descriptions;
- evaluator expectation;
- one base model producing stylistic variants;
- natural multi-angle reasoning caused by the task itself.

A test could therefore look successful while mainly confirming the instructions used to generate it.

## Revision

AranSoul adopted pre-registered criteria and blind behavioral testing.

Before observing results, each test should define:

- objective;
- expected behavior;
- failure conditions;
- alternative explanations.

Responses are then collected without assigning the expected angle in the test prompt, anonymized where practical, and evaluated by reasoning structure rather than names or catchphrases.

Results use Green / Amber / Red / Invalid classifications, but these grades describe the evidence from a specific test rather than proving persona ontology.

A stronger evidence ladder now distinguishes prompt compliance from blind attribution, cross-context repetition, exchange stress testing, independent evaluation, cross-model replication, and mechanistic evidence.

## Current lesson

**A system should make it possible for its own preferred interpretation to fail.**

If every result can be explained as confirmation, the test is not discriminating enough.

## Still unresolved

Current AranSoul blind tests still cannot fully remove shared-model effects, long-context contamination, and self-evaluation bias. Stronger evidence would require evaluator separation, cleaner context isolation, replication across models or environments, and eventually mechanistic measurements if mechanistic claims are made.
