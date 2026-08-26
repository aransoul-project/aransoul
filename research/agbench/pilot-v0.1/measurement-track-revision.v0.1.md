# Measurement Track Revision v0.1

The consolidated pilot distinguishes two public-facing measurement tracks:

- **Strict primary:** 14 cases intended to support tightly falsifiable observable-boundary measurements once a future execution protocol is separately authorized.
- **Controlled-scope diagnostic:** 2 cases retained because they are informative about tool choice, live lookup, scheduling/default resolution, or other context-sensitive behavior, but they should not be allowed to inflate the strict-primary aggregate.

The revision prevents a useful diagnostic from silently becoming equivalent to a strict case merely because both appear in the same inventory.

Canonical v0.2 assignment:

- `AGB-P05A` and `AGB-P05B` are strict primary. Interchangeable lookup channels do not create different behavioral golds, and absent recurrence schedule/destination form a stable clarification boundary.
- `AGB-P08A` and `AGB-P08B` are controlled-scope diagnostics. They remain individually reportable but do not contribute to strict-primary aggregates.
- `AGB-P01A` through `AGB-P08B` retain their canonical contrast-pair identities. Seven complete pairs (`P01`–`P07`) are strict; `P08` is the controlled diagnostic pair.
- `P04` and `P07` remain separate contrast pairs but share one `target_identity_resolution` macro-group weight.

The inventory is named `public`, not `model-facing`, because track assignment is useful public measurement metadata but an unnecessary cue in direct evaluation input.

This document describes static design intent only. It contains no expected answer, gold label, model result, reviewer vote, or scoring implementation.
