# Zombie Memory Replication — Evidence Label Checklist

Use the **narrowest** label supported by the actual design. A stronger label should never be inferred from a positive result alone.

## Step 1 — Is this mainly the same project lineage rerunning the same public benchmark?

If YES, start from **Reproduction**.

Changing only the date, random seed, or execution machine does not create independence.

## Step 2 — Is the tested model/provider/version meaningfully different?

If YES but benchmark construction, execution control, and evaluation lineage remain substantially the same, use **Cross-model reproduction**.

A model change tests model dependence. It does not by itself establish independent replication.

## Step 3 — Was evaluation meaningfully separated before substantive outputs were inspected?

Examples:

- independently frozen deterministic scorer;
- evaluator in a separate context without access to generation history;
- blinded human evaluation;
- model identity/condition blinding where practical.

If YES, and this separation is documented, **Evaluation-separated replication** may be justified.

If NO, do not claim Level-5-style evaluator separation.

## Step 4 — Is the replication controlled by a person/team outside the original AranSoul execution/evaluation lineage?

Check all that apply:

- [ ] External replicator chose or accepted the protocol independently.
- [ ] External replicator controls execution.
- [ ] External replicator controls or independently appoints evaluation.
- [ ] Prior exposure to original results is disclosed.
- [ ] Protocol deviations are reported without needing original-team approval.
- [ ] Raw outputs or sufficient checking artifacts are preserved.
- [ ] The external team may report Red/null/contradictory results without reinterpretation by AranSoul.

If the substantive controls above are satisfied, **Independent external replication** may be justified even when the public benchmark is reused.

If the original project still controls the decisive parts of execution/evaluation, use a weaker label.

## Step 5 — Does the replication test generalization beyond the original benchmark/environment?

Possible strengthening factors:

- different model/provider/environment;
- independently constructed unfamiliar cases;
- third-party case set;
- independent evaluator;
- different implementation that preserves the research question without copying hidden assumptions.

If independent execution is combined with meaningful cross-environment or unfamiliar-case variation, **Cross-environment / generalization replication** may be justified.

Do not use this label merely because one implementation detail changed.

## Disqualifiers / downgrades

A run should be downgraded or marked Invalid if relevant when:

- success criteria were changed after outputs were seen;
- cases were tuned to target-model failures and still presented as confirmatory;
- gold labels leaked to generation;
- factual payload differs unfairly across compared conditions;
- individual failed requests were selectively retried contrary to the freeze;
- raw outputs are missing without a justified alternative;
- evaluator rules were chosen after inspecting individual failures;
- the claimed independent evaluator relied on original-team case interpretations not available in the frozen public protocol;
- protocol deviations are hidden or silently normalized.

## Prior exposure does not automatically invalidate independence

An external researcher may know the original Holdout result and still perform an independent replication. What matters is disclosure and control of the new protocol, execution, evaluation, and reporting.

However, prior exposure limits claims of complete blindness and should be recorded.

## Result direction does not determine evidence label

The same evidence label applies whether the result is:

- positive;
- partial;
- null;
- negative;
- contradictory.

A Red independent external replication is stronger evidence about generalizability than a Green internal reproduction, even though the conclusions differ.

## Final declaration

Before publishing, complete:

- Claimed evidence label:
- Strongest satisfied criterion:
- Important shared dependencies that remain:
- Prior exposure disclosed: YES / NO
- Preregistration frozen before substantive output inspection: YES / NO
- Evaluation frozen before individual qualitative inspection: YES / NO
- Raw/checking artifacts preserved: YES / NO
- Protocol deviations disclosed: YES / NO
- Can a null/Red result stand without reinterpretation by the original AranSoul team: YES / NO

If any required condition for the claimed label is not satisfied, use the next weaker label or mark the run Invalid where appropriate.
