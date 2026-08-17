# Zombie Memory Preprint v0.1 — Related Work Draft

Status: manuscript-preparation draft; citations and wording require final human review before publication.

## Long-term memory evaluation for agents

Recent benchmarks have moved beyond single-turn factual recall toward long-horizon memory evaluation in interactive and changing environments. LongMemEval evaluates information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention in sustained chat histories. LongMemEval-V2 extends the emphasis toward environment experience, including dynamic state tracking and premise awareness in customized web and enterprise settings.

These benchmarks establish that long-term memory quality is not reducible to simple retrieval accuracy. They evaluate whether systems can recover, update, and reason over accumulated state. Zombie Memory is narrower: it does not attempt to provide a general long-term-memory benchmark. Instead, it isolates whether a model can identify the exact record set that currently has decision authority while still preserving current and historical information.

## Stale and obsolete memory

STALE directly studies whether later evidence implicitly invalidates earlier memories. Its evaluation separates state resolution, premise resistance, and implicit policy adaptation, asking whether an agent can recognize that an old state is no longer valid and behave consistently with the update.

Memora similarly emphasizes evolving personalized memory and introduces a forgetting-aware metric that penalizes reuse of obsolete or invalidated memories. Both lines of work are closely related to Zombie Memory because they distinguish useful memory from stale memory and evaluate failures to reconcile changing information.

Zombie Memory differs in target variable. Its primary confirmatory metric is not whether an obsolete fact is reused in the final answer, nor whether the system updates its stored state. The benchmark provides multiple records and asks for the exact set that currently controls the decision. A response can therefore be semantically correct about both current and historical states while still fail the authority-set metric by granting decision authority too broadly.

## Memory authority and provenance

AuthMem-Bench is the closest identified neighboring work in terminology and motivation. It studies authority collapse at the memory-consolidation boundary: a consolidation process may preserve a claim while losing source constraints that determine how that claim is authorized for later use. Its experiments therefore focus on whether write-time memory consolidation preserves source authority and how downstream behavior changes when authority metadata is lost or retained.

Zombie Memory studies a different boundary. The benchmark holds a set of records available at decision time and evaluates whether the model can identify exactly which records currently control the decision. It therefore targets decision-time authority resolution rather than authority preservation during memory consolidation.

The two problems are complementary rather than interchangeable. A memory system can fail before retrieval by collapsing authority during consolidation, or it can preserve the relevant records yet still fail at decision time by assigning authority to an overly broad set of remembered material.

## Dynamic state and premise awareness

LongMemEval-V2 includes dynamic state tracking and premise awareness, both of which are conceptually adjacent to Zombie Memory. Dynamic state tracking asks whether a system understands how an environment changes over time, while premise awareness evaluates whether it can reject assumptions that are invalid in the current deployment.

Zombie Memory again uses a more constrained measurement. It explicitly separates current answer, historical answer, and current authority-set identification. This allows the benchmark to observe cases in which state knowledge is preserved but authority attribution remains imprecise.

## Positioning of the present study

The contribution claimed by Zombie Memory Holdout v0.1 should therefore remain narrow.

The study does **not** claim to introduce the first benchmark for stale memory, memory updates, forgetting, dynamic state tracking, provenance, or memory authority. Existing work already addresses each of these neighboring areas.

The specific question isolated here is:

> Given multiple remembered records with different current roles, can a model identify the exact set of records that currently possesses decision authority, while still preserving current and historical state information?

This framing is useful because final-answer correctness can conceal authority-boundary error. In the completed holdout, semantic current and historical answers were much stronger than exact authority-set identification. The study therefore contributes a small behavioral probe of decision-time authority resolution, not a general theory of agent memory.

## Evidence-boundary note

Related work should not be used to retrospectively upgrade the evidence status of Zombie Memory Holdout v0.1. The manuscript must continue to distinguish:

- preregistered confirmatory authority-set scoring;
- post-freeze semantic measurement amendment;
- exploratory authority-error taxonomy and stratified analysis;
- unsupported claims about mechanism or generalization.

Similarity to later or neighboring papers is contextual evidence that the problem area is active; it is not independent replication of the Zombie Memory result.
