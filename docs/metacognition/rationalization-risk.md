# Rationalization Risk

Large language models are good at producing coherent explanations after an answer already exists. Coherence, however, is not proof that the explanation reflects the real cause of the answer.

AranSoul therefore treats **post-hoc rationalization** as a separate risk from ordinary factual error.

## The problem

A model can:

1. make an early mistake or accept a wrong premise;
2. continue reasoning from that premise;
3. produce a fluent explanation that makes the resulting path look intentional;
4. reinterpret later evidence so it fits the established narrative.

The danger is strongest when the first answer becomes part of the subsequent context. A later self-check may then inspect a context already contaminated by the earlier conclusion.

## First-answer contamination

An early answer can acquire disproportionate influence because later turns treat it as context rather than as an unverified hypothesis.

This creates a sequence like:

`initial guess → contextual fact → explanatory support → apparent consistency`

The system may then mistake consistency with its own previous statement for independent confirmation.

## Mitigations

AranSoul uses several design responses:

- separate observation from assumption before building an explanation;
- ask what evidence would falsify the current interpretation;
- preserve alternative explanations long enough to compare them;
- distinguish new evidence from reinterpretation of existing evidence;
- use fresh external evidence when the first answer may have polluted the context;
- when testing persona or reasoning behavior, define success and failure criteria before seeing the result;
- use blind or anonymized evaluation when labels could bias interpretation.

## Precommitment over retrospective fit

A strong safeguard is to define evaluation criteria before observing the output.

This changes the question from:

> "Can I explain why this result makes sense?"

into:

> "Did this result satisfy the conditions that were specified before it was seen?"

Precommitment does not eliminate interpretation, but it reduces the freedom to redefine success after the fact.

## Metacognition is not immunity

The five-step metacognitive framework can reduce rationalization risk, but it cannot guarantee escape from a contaminated premise.

A self-check that uses the same assumptions, same context, and same framing may reproduce the original error with greater eloquence.

When error cost is high, use independent evidence, alternative framing, or a reset to an earlier verified state rather than relying only on self-explanation.

## Status

This document describes a current AranSoul governance concern and a set of mitigation patterns. It does not claim access to hidden model reasoning or that any textual explanation is a faithful transcript of internal computation.
