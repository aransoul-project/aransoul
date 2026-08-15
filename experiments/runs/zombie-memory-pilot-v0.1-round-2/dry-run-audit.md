# Zombie Memory Pilot v0.1 Round 2 Execution Dry-Run Audit

Status: **execution runner validated; no Round 2 live API requests sent**

- Frozen preregistration commit: `35adafbc9281c8fd0bfdc977954b169f22a38a91`
- Runner commit exercised by the dry-run: `6db83cfdd634edd17d2268cf6576116854871367`
- Dry-run replication path: `outputs/replication-1/dry-run/setup-validation-001/`
- Planned independent live output roots: `outputs/replication-1/`, `outputs/replication-2/`, and `outputs/replication-3/`
- Requests recorded: 40
- Condition distribution: Plain 10, Timestamp 10, Status 10, T/T/E/A 10
- Parsed records: 40
- Request failures: 0
- Parse failures: 0
- Retry attempts: 0
- API calls: 0
- Scoring started: no
- Authority secondary diagnostic started: no
- Raw-data integrity approval asserted: no

Frozen prompt SHA-256 validation:

- plain: `58231f0f41e190d1d11a25e1ebf9b23264e4864b250bf1b4c7b2b3b62c4bfa64`
- timestamp: `18d71f7bc1cb9ddf6d856af2ea30ca129d2e43353c5b07617352ac612fad3441`
- status: `07af858528f5a4fcee09c0e63a79319b2d7027db4d2dea58afa1b45e88fe61ec`
- ttea: `a504018d74363c574c672bbf30c0b330d4538d32932c6fe3c3f459e907a24a86`

The dry-run used only frozen generated prompts. It did not read gold, execute
the scorer, run the Authority diagnostic, or modify the preregistration or
Pilot v0.1 instrument.
