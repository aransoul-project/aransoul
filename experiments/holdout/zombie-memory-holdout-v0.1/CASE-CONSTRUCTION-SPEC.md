# Zombie Memory Holdout v0.1 — Case Construction Spec

Status: **design-only; no final holdout cases generated; no model execution permitted**

This specification operationalizes the holdout preregistration. It governs how candidate cases may be authored, reviewed, rejected, replaced, and frozen. It must not be tuned against model outputs because no holdout model outputs are authorized before freeze.

## 1. Fixed inventory

The final holdout contains exactly **24 independent cases**, with exactly four cases in each of six preregistered families:

1. supersession / replacement;
2. scoped exception versus general rule;
3. temporary rule with expiry or restoration;
4. descriptive/current-but-non-authoritative material;
5. conflicting sources with explicit authority hierarchy;
6. historical query where a superseded record remains the correct historical answer.

Case IDs are assigned only after a candidate passes content review. Final IDs use `ZH-01` through `ZH-24`. Rejected candidates must not be silently recycled under a new ID without re-review.

## 2. Independence from Pilot v0.1

A holdout case may test the same abstract construct as a Pilot case, but it must not copy or minimally paraphrase:

- the same surface domain plus the same authority relationship;
- the same record sequence with nouns or numbers swapped;
- the same question wording with cosmetic edits;
- the same distractor pattern solely because that Pilot case produced a known error.

A candidate fails overlap review if a reviewer can map it to a Pilot case by simple entity substitution while preserving the same record roles and logic.

Pilot results may inform *risks to avoid* but may not be used to select candidates based on an expectation that one representation condition will win.

## 3. Surface-domain diversity

The 24 cases should span ordinary fictional domains such as workplace policy, software configuration, memberships, service plans, scheduling, logistics, access control, publishing, procurement, education, facilities, or product operations.

No domain may contribute more than three final cases. No case may require outside factual knowledge; all facts required to answer must appear in the supplied records.

Real companies, current laws, medical rules, financial products, or politically sensitive rules should not be used, because external truth or changing facts would contaminate the construct.

## 4. Record-count balancing

Across the final 24 cases:

- at least 8 cases must contain exactly 2 records;
- at least 8 cases must contain exactly 3 records;
- at least 4 cases must contain 4 or more records;
- the remaining cases may use any of these counts.

Record count must serve the case logic. Extra records may not be added merely to increase difficulty.

## 5. Canonical record fields

Every record must have a stable record ID and canonical fields sufficient to derive the four renderings. At minimum:

- `id`;
- `content`;
- `time` or equivalent temporal metadata when applicable;
- `status` or lifecycle state when applicable;
- `effect` describing what the record changes, limits, restores, or leaves unchanged;
- `authority` describing whether and how the record can control the queried decision.

The canonical representation is the source of truth. Plain, Timestamp, Status, and T/T/E/A renderers must not introduce facts absent from the canonical record.

## 6. Gold-label uniqueness

Before a candidate can pass review, its author must write the gold logic independently of any model output.

Required gold fields:

- `current_answer`;
- `historical_answer`;
- `current_authority_record_ids`;
- `stale_record_ids` where applicable.

The controlling set must be unique under the written records. If two competent readers can derive different controlling sets without violating any stated rule, the candidate fails and must be repaired or replaced before freeze.

The intended answer may rely on multiple controlling records only when the case logic truly requires joint authority. Such cases must state why no proper subset is sufficient.

## 7. Answer-format discipline

Current and historical answers should be short, deterministic values whenever practical: yes/no, one named option, one numeric value, one status, or one bounded phrase.

Avoid questions whose correctness depends primarily on prose style, judgment, empathy, common sense, or open-ended explanation. The benchmark is intended to test temporal/authority governance, not writing quality.

## 8. Family-specific construction rules

### Family 1 — Supersession / replacement

A later valid record fully replaces an earlier rule for the queried scope. The old record remains historically recoverable but must not control the current answer.

At least two of the four cases must make the supersession explicit; at least one must require inferring replacement from an explicit effective rule rather than the word `superseded` itself.

### Family 2 — Scoped exception versus general rule

A general current rule remains valid, while a narrower current exception controls the queried subject or situation.

The general rule must remain genuinely valid outside the exception. The case must distinguish `still current` from `controlling this query`.

### Family 3 — Temporary rule with expiry or restoration

A temporary change applies for a bounded interval and then expires, restores, or hands control back to another rule.

The queried current time and historical time must be unambiguous. At least one case must test restoration after expiry rather than simple replacement by a new permanent rule.

### Family 4 — Descriptive/current-but-non-authoritative material

At least one record is current and relevant but explicitly lacks independent decision authority, such as a FAQ, dashboard note, marketing summary, advisory memo, or descriptive status page.

The non-authoritative record must contain meaningful information rather than obvious nonsense. Selecting it should be a plausible over-selection error, not a trick.

### Family 5 — Conflicting sources with explicit authority hierarchy

Two or more records conflict in content, but the records themselves supply a deterministic authority hierarchy or tie-break rule.

The hierarchy must be contained in the case and must not depend on assumed real-world organizational rank. At least one case should require using an explicit tie-break rule rather than merely choosing the newest record.

### Family 6 — Historical query with superseded-but-correct historical answer

The current answer and historical answer must differ, and the historical answer must require recovering a record that no longer controls the present.

The case must still contain a well-defined current controlling set. This family tests preservation without current re-authorization, not simple archival lookup alone.

## 9. Difficulty controls

Difficulty must come from the target construct, not from irrelevant language complexity.

Prohibited difficulty inflation includes:

- long irrelevant narratives;
- obscure vocabulary;
- arithmetic beyond simple comparison;
- hidden real-world conventions;
- ambiguous pronouns or entity names;
- deliberate grammatical confusion;
- excessive record counts without logical necessity.

At least one case per family should be relatively simple and at least one should contain a legitimate competing cue, such as recency versus scope, status versus authority, or current relevance versus controlling power.

## 10. Leakage controls

No rendered prompt may expose gold labels, scorer terminology, or phrases such as `correct authority`, `gold`, `stale_record_ids`, or `the answer is`.

Metadata wording must describe the record, not instruct the model which record to select. T/T/E/A fields may state factual time, status, effect, and authority information but may not collapse the task into a direct answer key.

## 11. Semantic-equivalence requirement

All four conditions must present the same substantive facts. Differences are limited to the preregistered representation layer.

A semantic-equivalence audit must verify, case by case, that no condition:

- omits a fact present in another condition;
- adds a new substantive fact;
- changes scope, timing, authority, or lifecycle meaning;
- changes the question being asked.

If equivalence cannot be achieved, the candidate is rejected rather than condition-specifically rewritten after model testing.

## 12. Candidate review without model behavior

Candidate quality review may use deterministic scripts and human/LLM textual inspection, but **must not run any target evaluation model on candidate cases**.

Review is limited to:

- schema validity;
- internal logic;
- gold uniqueness;
- family fit;
- overlap with Pilot;
- leakage;
- semantic equivalence;
- scorer determinism.

A candidate cannot be accepted or rejected because someone predicts it will help or hurt Plain, Timestamp, Status, or T/T/E/A.

## 13. Replacement policy during construction

Candidates may be repaired or replaced before freeze only for documented construction reasons such as ambiguity, duplicate logic, leakage, invalid gold, failed equivalence, or quota imbalance.

Every rejected candidate should receive a short rejection reason in the construction audit. No model score may appear in that audit because model execution is prohibited.

## 14. Freeze checklist

Before holdout freeze, the repository must contain and validate together:

- exactly 24 final cases with fixed IDs;
- six-family quota of 4 each;
- record-count quota compliance;
- surface-domain diversity check;
- Pilot-overlap audit;
- gold-uniqueness audit;
- semantic-equivalence audit;
- leakage audit;
- deterministic scorer tests;
- generated Plain / Timestamp / Status / T/T/E/A files;
- SHA-256 hashes for all frozen generated inputs;
- final schema, renderer, scorer, gold labels, and construction audit;
- final preregistration replacing the current skeleton status.

Only after a dedicated freeze review passes may an execution protocol authorize model calls.

## 15. Current gate

**STOP: case-construction rules only.**

This specification does not authorize generation of final holdout cases, model API calls, scoring, or empirical interpretation. The next permitted step is candidate-generation planning or candidate construction under this specification, followed by pre-freeze review.