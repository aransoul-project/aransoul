# Executable Renderer Specification

Status: **Implementation spec — code not yet landed**

The renderer must take one canonical `cases.json` file and emit four condition files: `plain.json`, `timestamp.json`, `status.json`, and `ttea.json`.

For every case, the renderer must preserve the same case id, family, record ids, substantive record prose, current question, historical question, and output contract.

## Plain

Render only record id plus substantive record prose.

## Timestamp

Render the same Plain content plus one normalized `Date` field derived from the record time.

## Status

Render the same Plain content plus one normalized effect-only status label derived from the record effect: CURRENT, SUPERSEDED, PARTIAL, CANDIDATE, HISTORICAL, or REVOKED.

Do not expose a separate authority field.

## T/T/E/A

Render the same Plain content plus normalized Truth, Time, Effect, and Authority fields. Scope may be rendered when it is already stated by the canonical scenario.

## Forbidden leakage

The renderer must never expose benchmark-only gold annotations, including gold answers, stale-record ids, still-valid-older-record ids, historical gold ids, or current controlling-source gold labels.

## Freeze condition

The renderer is not frozen until executable code generates all four condition views from one canonical dataset and a leakage audit confirms that no forbidden annotation appears in generated prompts.
