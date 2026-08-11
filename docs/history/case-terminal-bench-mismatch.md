# Case Study: Terminal-Bench and Benchmark Mismatch

## Original assumption

At one stage of AranSoul development, external benchmark performance appeared to offer a way to validate the system objectively. Terminal-Bench was explored as a possible evaluation target for an AranSoul-style agent.

## Observed problem

Terminal-Bench primarily evaluates whether an agent can complete concrete terminal tasks inside a controlled execution environment. That is a legitimate and useful benchmark, but it measures a task-execution capability that is not equivalent to AranSoul's main research questions.

AranSoul increasingly focused on long-running human–AI collaboration, governance, memory state, evidence thresholds, selective perspective activation, and revision discipline. A low or high terminal-task score would therefore not directly establish whether those design goals were succeeding.

The earlier framing risked a common evaluation mistake: treating the availability of a benchmark as evidence that the benchmark measures the thing the project most cares about.

## Revision

Terminal-Bench is now classified as an **external evaluation environment**, not part of the AranSoul architecture and not a primary proof of system value.

Future use should begin by specifying the question the benchmark can answer. If the question is terminal execution competence, Terminal-Bench may be appropriate. If the question concerns memory governance, post-hoc rationalization, human authority, or long-context drift, a different experimental design is required.

## Current lesson

**Benchmark fit must be established before benchmark score is interpreted.**

External evaluation is valuable only when the measured capability corresponds to the claim being made.

## Still unresolved

AranSoul does not yet have a single comprehensive external benchmark suite for its present research goals. Suitable evaluation will likely require multiple task families rather than one scalar score, including governance adherence, memory-state integrity, intervention calibration, external-action verification, and resistance to self-confirming evaluation.
