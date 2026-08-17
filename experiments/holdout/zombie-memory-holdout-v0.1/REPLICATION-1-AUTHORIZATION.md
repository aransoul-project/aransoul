# Zombie Memory Holdout v0.1 — Replication 1 Live Authorization

Status: **AUTHORIZED FOR ONE COMPLETE BLIND LIVE REPLICATION ONLY**

Authorization scope:

- replication: `replication-1`
- request count: exactly 96 planned requests
- branch: `zombie-memory-holdout-v0.1-replication-1-live`
- execution source: `zombie-memory-holdout-v0.1-execution-frozen`
- frozen execution instrument remains unchanged
- no case-level selective retries
- transport/provider failure makes the whole replication technical-invalid and stops the run
- no scoring before the raw-data integrity gate
- no authorization is granted for replication-2 or replication-3

This authorization records an explicit user decision made after the execution-ready freeze. It changes only the run authorization state; model snapshot, prompts, prompt hashes, ordering, sampling parameters, retry policy, scorer, gold labels, and construction payload remain frozen.

Authorized command:

`python experiments/holdout/zombie-memory-holdout-v0.1/runner.py --replication replication-1 --mode live --confirm-live --run-id replication-1-blind-live`

If the exact frozen model snapshot is unavailable or a provider/transport failure occurs, preserve the incomplete artifacts and stop. Do not substitute another model and do not selectively retry an individual case.
