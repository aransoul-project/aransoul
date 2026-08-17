# Replication 2 Authorization

- Experiment: `zombie-memory-holdout-v0.1-blind`
- Authorized replication: `replication-2`
- Execution branch: `zombie-memory-holdout-v0.1-replication-2-live`
- Construction payload: unchanged from frozen instrument
- Prompt hashes: unchanged from execution freeze
- Model snapshot: `gpt-4.1-mini-2025-04-14`
- Temperature: `0`
- top_p: `1`
- max_output_tokens: `256`
- Retry count: `0`
- Individual retry allowed: `false`
- Semantic grader amendment: frozen before replication-2 execution
- Frozen semantic grader commit: `52450aca7988ec0377ca889a6d0db4f7c03c77fa`
- Replication-2 live API calls at authorization: `0`

This authorization preserves the previously frozen prompts and execution protocol. It changes only the authorized replication from replication-1 to replication-2. No individual-case results from replication-1 were used to alter the prompt set, model configuration, or semantic grader after its freeze.
