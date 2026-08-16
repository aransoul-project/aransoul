# Scoring Validity Audit — Replication 1

## Scope

This audit evaluates whether the already-produced aggregate metrics measure what the frozen prompt contract actually required. It does not inspect or classify individual model answers and does not alter responses, prompts, gold labels, scorer fixtures, or frozen construction artifacts.

## Evidence

- Raw-data integrity passed before scoring: 96 parsed live responses, 96 unique case-condition pairs, all attempts = 1.
- Fixture self-test passed: 24 cases, 243 assertions.
- The model-facing prompt requires JSON fields `current_answer`, `historical_answer`, and `current_authority_record_ids`, but does not require the two free-text answer fields to reproduce canonical gold wording exactly.
- The current scorer evaluates `current_answer` and `historical_answer` using normalized exact-string equality (trim + uppercase only).
- `current_authority_record_ids` is an explicitly structured record-ID set, so exact-set comparison is aligned with the prompt contract.

## Validity determination

### Current-answer accuracy

Status: **INVALID / UNINTERPRETABLE FOR REPLICATION-1 PRIMARY INFERENCE**.

Reason: the response contract permits semantically equivalent free-text answers, while the scorer requires canonical exact wording. The observed 0.0 therefore cannot distinguish semantic error from harmless paraphrase.

### Historical-answer accuracy

Status: **INVALID / UNINTERPRETABLE FOR REPLICATION-1 PRIMARY INFERENCE**.

Reason: same measurement mismatch as current-answer accuracy.

### Authority exact-set accuracy

Status: **VALID AS CURRENTLY SCORED**.

Reason: the requested output is a structured list of record IDs and the frozen gold defines an exact controlling set. No semantic paraphrase layer is required.

### Stale-authority error / false-discard

Status: **STRUCTURALLY VALID BUT INTERPRET WITH THE AUTHORITY-SELECTION TASK**.

These metrics operate on selected record IDs rather than free-text answer wording. They are not invalidated by the exact-string answer problem.

## Replication-1 aggregate values retained

- Authority exact-set accuracy: 0.6354166666666666 (61/96).
- Plain: 0.625 (15/24).
- Timestamp: 0.6666666666666666 (16/24).
- Status: 0.7083333333333334 (17/24).
- T/T/E/A: 0.5416666666666666 (13/24).
- Stale-authority error: 0/96.
- False-discard: 0/96.

The previously generated 0.0 current-answer and historical-answer accuracies are preserved as historical scorer outputs but must not be reported as evidence that all free-text answers were semantically wrong.

## Governance decision before replication 2

**HOLD replication-2.**

Do not modify the existing replication-1 responses or retroactively tune a semantic grader against them. Before any further live replication, preregister a separate answer-evaluation amendment or explicitly narrow the experiment's primary interpretable outcomes to the structured authority metrics. Any semantic grading protocol must be defined independently of individual replication-1 answer inspection and clearly labeled as a post-freeze measurement amendment.

Individual failures inspected during this audit: **false**.
