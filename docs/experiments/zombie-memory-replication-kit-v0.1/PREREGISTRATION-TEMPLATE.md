# Zombie Memory Replication — Preregistration Template

Status: **Template only. Complete and freeze a copy before inspecting substantive target-model outputs.**

## 1. Replication identity

- Replication title:
- Date frozen:
- Repository / artifact location:
- Preregistration commit SHA or immutable identifier:
- Responsible person/team:
- Relationship to original AranSoul project, if any:

## 2. Intended evidence label

Select one before execution:

- [ ] Reproduction
- [ ] Cross-model reproduction
- [ ] Evaluation-separated replication
- [ ] Independent external replication
- [ ] Cross-environment / generalization replication

Brief justification:

## 3. Prior exposure disclosure

Before freeze, disclose whether case constructors, generation operators, and evaluators have seen:

- the original Holdout aggregate results;
- the 102/102 over-selection exploratory result;
- individual original model responses;
- original error annotations;
- original condition-level results;
- any unpublished AranSoul replication material.

State what was known by each role and when.

## 4. Benchmark / case source

- Source repository:
- Exact source commit SHA:
- Case-set path or immutable hash:
- Public original cases / newly constructed / independently supplied:
- Number of cases:
- Case families or strata:
- Conditions:
- Expected requests per run:

For new cases, explain how gold current authority is fixed independently of target-model outputs.

## 5. Primary research question

State one narrow question that the confirmatory analysis will answer.

Example form:

> Under the frozen case set and execution conditions, how accurately does the tested model identify the exact set of records that currently has decision authority while preserving correct current and historical answers?

## 6. Confirmatory hypotheses and nulls

For each confirmatory claim, state:

- hypothesis;
- null or competing explanation;
- metric;
- success/failure criterion;
- what result would count against the hypothesis.

Do not define success thresholds after observing substantive outputs.

## 7. Model and execution settings

- Provider:
- Model name:
- Exact version/snapshot if available:
- API/SDK/version or local runtime:
- Temperature:
- Top-p:
- Max output tokens:
- Seed, if supported:
- Retry policy:
- Timeout policy:
- Parallelism/concurrency:
- Record ordering/randomization:
- Condition ordering/randomization:
- System/developer/task instructions:
- Structured-output schema or parsing contract:

## 8. Separation design

### Case construction

- Who controls case construction?
- What information may constructors see?
- When is gold frozen?

### Generation

- Who controls generation?
- What information may the generator/operator see?
- Are original individual responses hidden from generation?

### Evaluation

- Who controls evaluation?
- Is model identity blinded?
- Are condition labels blinded where practical?
- Is evaluation performed in a separate context/team/system?
- Is the scorer deterministic, human, or hybrid?

## 9. Frozen metrics

Mark each as confirmatory, secondary, or unused:

- Current-answer correctness:
- Historical-answer correctness:
- Exact current-authority-set accuracy:
- Stale-authority error count/rate:
- False-discard count/rate:
- Semantic free-text correctness:
- Other metric(s):

For every metric, specify the exact scoring rule and implementation/rubric reference.

## 10. Semantic grading rule

If free-text semantic grading is planned:

- grader type:
- grader version/rubric:
- validation procedure:
- freeze identifier:
- whether the grader can see condition/model identity:

If semantic grading is not preregistered, any later semantic analysis must be labeled a post-freeze amendment or exploratory analysis.

## 11. Error taxonomy

- [ ] No confirmatory individual-error taxonomy is planned.
- [ ] Error taxonomy is preregistered as confirmatory.

If preregistered, define categories and coding rules now. Do not use the original 102/102 over-selection result as a required target unless that is explicitly the hypothesis being tested.

## 12. Technical validity gates

Define conditions that make the run technical-invalid or non-interpretable, including as applicable:

- request/transport failure threshold;
- parse failure threshold;
- missing/duplicate request handling;
- prompt/case hash mismatch;
- unequal factual payload across conditions;
- accidental exposure to gold labels;
- scorer self-test failure;
- selective retry or cherry-picking;
- incomplete raw-output preservation.

State whether a failed run may be rerun and under what predeclared rule.

## 13. Raw-data and provenance plan

- Raw response format:
- Raw response storage location:
- Manifest format:
- Prompt/case hashes stored:
- Environment/version metadata stored:
- Redistribution restrictions, if any:
- Redaction rules, if any:

## 14. Analysis order

Predeclare the order in which data may be opened, for example:

1. transport/parse metadata only;
2. raw-data integrity gate;
3. aggregate confirmatory scoring;
4. preregistered subgroup analysis;
5. only after confirmatory completion, individual qualitative/error inspection.

## 15. Amendment rule

Any change made after substantive outputs are inspected must be logged with:

- timestamp/date;
- reason;
- what information had already been seen;
- whether the change is measurement-only, exploratory, or invalidating;
- whether original frozen metrics remain preserved.

## 16. Reporting commitment

Before running, commit to reporting:

- Green, Amber, Red, null, and Invalid outcomes;
- protocol deviations;
- failed or technical-invalid attempts where relevant;
- confirmatory and exploratory results separately;
- enough provenance to recover the exact source benchmark and scoring state.

## 17. Authorization

- Preregistration frozen: YES / NO
- Technical dry run completed: YES / NO / N/A
- Substantive live/model execution authorized: YES / NO
- Authorized by:
- Authorization date:

Until the final line is YES, this document does not authorize substantive execution.
