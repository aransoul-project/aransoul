# Zombie Memory External Replication — Outreach Template

Status: **Optional outreach wording. This is not a replication result or protocol amendment.**

Use this only to invite an external researcher or engineering team to inspect or replicate the public Zombie Memory benchmark. Keep the invitation neutral and do not imply that a positive result is expected.

## Short invitation

AranSoul has published a small behavioral benchmark on a narrow question: whether an LLM can distinguish information that is remembered or relevant from the records that currently have decision authority.

The completed internal Holdout v0.1 used 24 cases, four conditions, and three within-protocol replications. The repository now includes a contact-free replication kit with preregistration, frozen prompt/hash verification, provider-neutral response validation, deterministic scoring, reporting templates, and explicit rules separating reproduction from independent external replication.

We are looking for an external researcher or engineer who is willing to test the benchmark under their own control. A positive result is not required; Red, null, contradictory, or Invalid outcomes are equally acceptable if reported according to the frozen protocol.

Repository:
https://github.com/aransoul-project/aransoul

Suggested starting points:

- `docs/experiments/zombie-memory-external-replication-handoff-v0.1.md`
- `docs/experiments/zombie-memory-replication-kit-v0.1/README.md`
- `experiments/holdout/zombie-memory-holdout-v0.1/README.md`

If you choose to replicate it, you should independently control the preregistration, provider/model selection, execution, evaluation, deviations, and final interpretation. You do not need AranSoul approval for a negative or contradictory result.

## Independence note

Do not describe a run as independent external replication merely because it uses a different model. The evidence label should follow the repository's `EVIDENCE-LABEL-CHECKLIST.md` and reflect who actually controls execution and evaluation.

## What we are not asking for

- No endorsement of AranSoul is requested.
- No predetermined conclusion is expected.
- No modification of the original frozen evidence is needed.
- No requirement exists to use the original provider.
- The external work may remain in the replicator's own repository or publication workflow.
