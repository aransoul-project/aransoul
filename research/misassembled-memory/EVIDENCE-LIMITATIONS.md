# M02 — Evidence and publication limitations

**Status:** `EXECUTION_UNVERIFIED`; no independent product-memory evidence.

## Provenance matrix

| Element | Available | Not established |
| --- | --- | --- |
| Content-level responses | 24 answers relayed by the human test operator | Authenticated original provider outputs or guaranteed first replies |
| Prompt material | Archived local prompt packs and later integrity checks | Proof that the exact archived bytes were submitted in each live session |
| Study conditions | Research protocols and intended chat isolation | Independently witnessed fixed model/version, temporary-chat mode, no prior context |
| Scoring | Provisional classifications using batch-specific criteria | Independent blinded re-scoring or evaluator agreement |
| File integrity | Present-day ZIP checks and hashes for local packs | Immutable pre-execution archive timestamp or provider-side attestation |
| Historical explanation | A synthetic behavioral analogy | Original incident memory write/retrieval and source-attribution trace |

## Specific retained irregularities

- R02 included a prompt-copy discrepancy between a displayed copy action and the archived pure prompt. Actual submitted bytes are uncertain.
- R03 contains wording that could be read as implying a summary mentioned a specific animal type while the result separately marks the field unverified. Keep the scoring caveat instead of presenting it as completely unambiguous.
- R06's final answer was relayed with an extra terminal character of uncertain origin. Its substantive animal/date answer was graded provisionally without silently changing the observed relay.
- R06 has several rolling local logs; the final consolidated log is a derived record, not a provider-signed transcript.
- Later integrity hashes only identify files *at time of inspection*; they do not retroactively prove the originally executed prompts were sealed unchanged.

## Reading the result classes

Green and Red denote observable behavior **against that round's stated criteria**. A Red in a summary-only condition concerns an **unqualified claim on unverified evidence**; it does not establish that the model possessed, or could retrieve, an unseen correct answer. A content-level Green does not authorize a stronger execution, mechanism, reliability, or governance claim.

Execution verification and the epistemic strength of conclusions must be reported separately. For this snapshot: `CONTENT_PROVISIONAL` and `EXECUTION_UNVERIFIED` both apply.

## Privacy and sealed material boundary

This public derivative intentionally omits private source conversations, real people or pets, dates from personally identifiable incidents, platform account details, raw memory dumps, sealed prompts, case-level blind-ID pairings, gold labels, private scoring packets, and full raw answer transcripts. The absence of these artifacts limits independent reproduction; it is a deliberate publication boundary, not a claim that the archive contains a complete replication kit.

## Status and change control

- No change to the AranSoul `CURRENT` baseline, canonical memory or experimental method files, `STATUS.md`, or released tagged versions.
- No permission to resume any held API, agent, engineering, or separate research activity.
- A proposed future run requires a fresh protocol, independent evidence plan, and explicit authorization. No prior observations are to be re-run or repaired merely to erase limitations.
- [PR #41](https://github.com/aransoul-project/aransoul/pull/41) was merged into `main` on 2026-11-04 at 21:01:07 Asia/Taipei (13:01:07 UTC), producing commit [5233beae63565d7672b95990101ff1916f93b61e](https://github.com/aransoul-project/aransoul/commit/5233beae63565d7672b95990101ff1916f93b61e). The earlier draft-publication permission and the subsequent merge event are distinct; neither establishes research validation.

## External inspection and licensing qualification

This derivative provides aggregate descriptions and methodological cautions, **not** a reproducibility package: reviewers cannot independently re-score or replicate the 24 outputs from this public snapshot because original prompts, raw outputs, blind keys, and platform execution records are deliberately absent. The publicly stated counts are traceable to private local research notes reviewed by the authors, not independently inspectable raw provider records.

Repository documentation defaults to CC BY-SA 4.0. Publication of this four-file draft PR was explicitly authorized; that authorization does not apply to private or third-party materials outside the approved scope. A synthetic-content scan alone is not evidence of ownership, permission, or third-party rights clearance. The recorded merge does not authorize new experiments or promote candidate conclusions.

## Publication-status correction — 2026-11-09

The earlier draft/unmerged wording is retained in Git history. The Bridge Master authorized this factual status correction on 2026-11-09. This does not backdate a separate approval for the 2026-11-04 merge: no separate approval record was located in the reviewed PR comments or reviews. Research grades, evidence limitations, candidate status, and execution holds are unchanged.
