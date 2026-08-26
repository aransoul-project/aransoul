# Artifact Index

| Artifact | Public-safe purpose |
|---|---|
| `README.md` | Entry point and evidence boundary |
| `RESEARCH-REPORT.md` | Research purpose, design state, limitations |
| `FINAL-STATUS.md` | Machine-readable-in-spirit status boundary |
| `ARTIFACT-INDEX.md` | Snapshot contents |
| `RESUME-CONDITIONS.md` | Conditions required before later phases |
| `candidate-inventory.v0.2.public.json` | Canonical P01A–P08B identities, tracks, scenarios, and observable context; not direct model input |
| `canonical-content-fingerprints.v0.2.public.json` | Fixed non-gold SHA-256 fingerprints for all 16 canonical public case payloads |
| `aggregation-policy.v0.2.public.json` | Reproducible public-safe canonical v0.2 aggregation derivative; no answer key |
| `measurement-track-revision.v0.1.md` | Primary vs diagnostic treatment |
| `schemas/candidate-inventory.public.schema.json` | Draft 2020-12 public-inventory schema |
| `schemas/aggregation-policy.schema.json` | Offline schema |
| `validators/validate_snapshot.py` | Executed schema, canonical fidelity, aggregation, leakage, and negative self-tests |
| `validators/negative-self-tests.json` | Static negative mutations and fixed expected-error oracles, including content drift and aggregation fidelity |
| `validators/requirements.txt` | Offline validator dependency declaration |
| `VALIDATION-RESULTS.md` | Validation record produced for this snapshot |

## Not present by design

Reviewer packets, reviewer responses, blind mappings, adjudicator packets/submissions, sealed generation material, private answer keys, gold labels, expected behavior fields, scorer fixtures, scorer implementations, provider adapters, and live-run harnesses.
