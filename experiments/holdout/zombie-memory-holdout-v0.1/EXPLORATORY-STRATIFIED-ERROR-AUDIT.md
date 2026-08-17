# EXPLORATORY — NOT PREREGISTERED CONFIRMATORY ANALYSIS

- Sample manifest commit: `b0e3dc1ade094789b93f2641cf6beddea2ca8d8f`
- Sample manifest frozen before content inspection: `true`
- Analysis: `exploratory`
- Sampling deterministic: `true`
- Semantic free-text answers inspected: `false`
- Causal interpretation performed: `false`
- New live API calls: `0`

## Sample aggregate

- Unique sampled failures: `18`
- Sampled failures — Temporary rule with expiry/restoration: `6`
- Sampled failures — Scoped exception vs general rule: `6`
- Sampled failures — condition=ttea over-selection: `6`
- Extra records classified: `24`

## Extra-record structural roles

| Structural role | Count |
| --- | ---: |
| expired_temporary_rule | 0 |
| restored_general_rule | 0 |
| general_rule_outside_scope | 7 |
| scoped_exception | 0 |
| superseded_record | 0 |
| current_non_authoritative_material | 3 |
| supporting_or_context_record | 14 |
| other_structural_role | 0 |
| unclassified | 0 |

## Structural roles by sampling stratum

| Stratum | General outside scope | Current non-authoritative | Supporting/context | All other roles |
| --- | ---: | ---: | ---: | ---: |
| Temporary rule with expiry/restoration | 0 | 2 | 6 | 0 |
| Scoped exception vs general rule | 5 | 0 | 3 | 0 |
| condition=ttea over-selection | 2 | 1 | 5 | 0 |

The labels describe frozen record roles only. No claim about model psychology, attention, confusion, metadata load, or reasoning failure is made.
