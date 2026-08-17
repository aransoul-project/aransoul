# Zombie Memory Replication — Result Report Template

Status: **Template only. Complete after execution without rewriting the preregistration history.**

## 1. Replication identity

- Title:
- Evidence label claimed:
- Preregistration identifier / commit:
- Source benchmark / case-set identifier:
- Source commit SHA:
- Execution date(s):
- Responsible person/team:
- Relationship to original AranSoul project:

## 2. Executive summary

In 3–6 sentences, state:

- what was tested;
- what model/environment was used;
- whether the run was technically valid;
- the primary preregistered result;
- whether the result supports, weakens, or fails to reproduce the prior finding;
- the evidence label justified by the design.

Do not include exploratory causal explanations in this summary unless clearly labeled exploratory.

## 3. Evidence label justification

Explain why this run is best described as one of:

- reproduction;
- cross-model reproduction;
- evaluation-separated replication;
- independent external replication;
- cross-environment / generalization replication.

State which dependencies remained shared with the original AranSoul lineage.

## 4. Prior exposure and separation disclosure

Report what case constructors, generation operators, and evaluators knew before freeze, including exposure to:

- prior aggregate results;
- the 102/102 over-selection finding;
- individual original responses;
- original error annotations;
- condition-level results.

Describe any blinding or evaluation separation actually achieved.

## 5. Frozen protocol

Summarize the preregistered:

- case set and conditions;
- model/provider/version;
- generation parameters;
- ordering/randomization;
- retry policy;
- scoring implementation/rubric;
- technical validity gates;
- primary/secondary metrics;
- success/failure criteria.

Link to the immutable preregistration rather than reproducing or silently editing it.

## 6. Execution integrity

Report:

- expected request count;
- recorded request count;
- request failures;
- parse failures;
- duplicates/missing rows;
- case/prompt hash checks;
- scorer/rubric validation status;
- raw-output preservation status;
- technical-invalid attempts, if any.

Final execution status:

- [ ] Valid for planned confirmatory analysis
- [ ] Technical-invalid
- [ ] Invalid for another reason

If invalid, stop confirmatory interpretation here and explain why.

## 7. Confirmatory results

Report only metrics frozen as confirmatory before substantive target-model outputs were inspected.

Suggested table fields:

| Metric | Numerator / denominator | Rate | Preregistered interpretation |
|---|---:|---:|---|
| Exact current-authority-set accuracy |  |  |  |
| Current-answer correctness |  |  |  |
| Historical-answer correctness |  |  |  |
| Stale-authority error rate |  |  |  |
| False-discard rate |  |  |  |

If condition/family analyses were preregistered, report them separately.

### Confirmatory decision

- [ ] Green
- [ ] Amber
- [ ] Red / null
- [ ] Invalid

Explain the decision using only preregistered criteria.

## 8. Comparison with prior Holdout v0.1

Compare cautiously with the original public result:

- Holdout v0.1 pooled authority exact-set: 186/288 = 64.58%.
- Post-freeze semantic measurement in Holdout v0.1: current 284/288 = 98.61%; historical 283/288 = 98.26%.
- Original exploratory taxonomy: 102/102 authority failures were over-selection.

Do not treat numerical difference as causal evidence unless the design supports that inference.

State whether the new result:

- broadly reproduces the authority-boundary gap;
- partially reproduces it;
- does not reproduce it;
- cannot be compared cleanly because the benchmark/model/evaluator changed materially.

## 9. Post-freeze amendments

List every procedure or metric added after the preregistration freeze.

For each amendment report:

- date/time;
- reason;
- what substantive data had already been inspected;
- exact new procedure;
- whether the original frozen result remains preserved;
- evidence status: amendment / exploratory / invalidating.

If none: state `None` explicitly.

## 10. Exploratory analysis

Only after confirmatory reporting is complete, report any:

- authority-error taxonomy;
- over-selection / under-selection / mixed patterns;
- subgroup/family patterns;
- qualitative case inspection;
- newly proposed mechanisms or explanations;
- new candidate metrics.

These findings must remain labeled exploratory unless independently preregistered.

## 11. Alternative explanations

List plausible explanations that remain compatible with the observed result, including as applicable:

- benchmark familiarity;
- provider/model-specific behavior;
- representation effects;
- scorer ontology choices;
- case-construction bias;
- shared evaluator expectations;
- synthetic-task artifacts;
- instruction-following rather than general memory governance.

## 12. Claim boundary

State what the replication supports and what it does not establish.

At minimum, do not claim from one replication that:

- Zombie Memory is a universal taxonomy;
- T/T/E/A is necessary or mechanistically causal;
- one hidden internal mechanism explains authority errors;
- AranSoul has solved AI memory;
- synthetic benchmark success establishes production-agent safety.

## 13. Artifact index

Provide exact paths/links/immutable identifiers for:

- preregistration;
- case set and hashes;
- run metadata/manifest;
- raw responses;
- confirmatory scores;
- semantic scores, if any;
- amendments;
- exploratory analysis;
- scorer/rubric implementation;
- this report.

## 14. Reproducibility statement

Answer explicitly:

1. Can another reader recover the exact case set used?
2. Can they recover the exact model/version/parameters?
3. Can they recover raw outputs or a justified restricted equivalent?
4. Can they rerun the scorer or reproduce the evaluator procedure?
5. Can they distinguish preregistered, amended, exploratory, and invalid evidence?

If any answer is NO, explain the limitation.

## 15. Final conclusion

Use the narrowest conclusion justified by the design and evidence label.

A clean null, Red, or contradictory result is an acceptable final conclusion and should not be softened to preserve the original AranSoul interpretation.
