# Resume Conditions

AGBench Pilot v0.1 remains paused after static measurement-design closure.

Before any later phase begins, create a new explicit decision record covering the intended phase and evidence boundary.

At minimum:

1. **Freeze / preregistration:** define immutable candidate set, metrics, exclusions, hashes, and amendment policy before claiming preregistration.
2. **Implementation:** separately authorize provider-neutral adapters or scorers; keep private evaluation material inaccessible to model-facing execution paths.
3. **Live execution:** explicitly authorize provider/model, budget, settings, retry policy, logging, and privacy boundary.
4. **Scoring:** freeze the scoring contract before interpreting live outputs as benchmark results.
5. **Release:** perform a fresh leakage/provenance audit and explicitly authorize a release/tag.

The existence of this GitHub-safe snapshot satisfies none of those later authorizations automatically.
