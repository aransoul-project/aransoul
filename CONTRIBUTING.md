# Contributing to AranSoul

AranSoul is currently a documentation-first research and governance project for long-running human–AI collaboration.

Contributions are welcome when they improve clarity, traceability, falsifiability, or implementation realism without silently promoting historical or speculative material into the current baseline.

## Good contribution targets

Useful contributions include:

- correcting broken links, terminology drift, or contradictory status labels;
- improving functional descriptions of AranSoul-native terms;
- adding evidence, counterexamples, or alternative explanations to experimental claims;
- improving test protocols, auditability, or replication design;
- identifying places where poetic or narrative language may be mistaken for a technical or mechanistic claim;
- documenting implementation gaps between governance rules and actual software capability;
- adding historical provenance without restoring historical authority.

## Status discipline

Before proposing a change, check [STATUS.md](STATUS.md).

AranSoul distinguishes:

- **CURRENT** — part of the present public baseline;
- **CANDIDATE** — worth testing but not established;
- **HISTORICAL** — preserved for provenance;
- **RETIRED / UNVERIFIED** — should not be presented as established capability.

A newer idea does not become current merely because it is newer. A historical artifact does not regain current authority merely because it is still available.

## Evidence and wording

Please separate:

- observation from inference;
- method status from claim status;
- behavioral evidence from mechanistic claims;
- identity or poetic vocabulary from implementation claims;
- capability from authorization;
- internal completion from verified external completion.

When making a stronger claim, state what evidence would count against it and what alternative explanations remain plausible.

## Persona and architecture claims

Named perspectives, personas, councils, or symbolic groups should not be described as independently instantiated agents, autonomous wills, conscious entities, or model-internal mechanisms unless direct evidence supports that specific claim.

Functional descriptions should remain revisable unless formally fixed by the current governance baseline.

## Tests and experiments

Behavioral tests should use the current [precommit criteria](docs/experiments/precommit-criteria.md) where practical.

Green / Amber / Red / Invalid describe performance against predefined criteria. They do not by themselves describe the strength of the experimental design. Use the [evidence ladder](docs/experiments/evidence-ladder.md) to discuss evidence strength separately.

## Historical material

Do not rewrite earlier records to make the project appear to have always held its current position.

When correcting an earlier idea, prefer:

1. preserve the historical record;
2. identify what changed;
3. explain why the interpretation changed;
4. update current status separately.

## Pull requests

Keep pull requests narrow when possible. Explain:

- what problem the change addresses;
- whether it changes CURRENT, CANDIDATE, HISTORICAL, or RETIRED / UNVERIFIED material;
- what evidence or source supports the change;
- whether existing documents need a status or cross-link update.

Major changes to governance, identity, authority, irreversible history, or formal project status should not be treated as routine editorial edits.

## Licensing of contributions

By contributing material to this repository, contributors should expect the repository's content-type licensing policy in [LICENSE](LICENSE) to apply unless a contribution is explicitly accepted under different terms.

- Documentation, research text, governance specifications, experiment protocols, historical case studies, and other non-code content are contributed for distribution under **CC BY-SA 4.0** unless otherwise stated.
- Software source code and executable code are contributed for distribution under **Apache-2.0** unless otherwise stated.
- Third-party material must retain its original licensing and attribution requirements and should not be contributed unless redistribution is permitted.

Do not submit material under incompatible terms without making those terms explicit before incorporation.

Licensing a contribution does not automatically change its AranSoul governance status. A contributed document may remain Candidate, Historical, or Retired / Unverified even when it is legally reusable under the repository license.
