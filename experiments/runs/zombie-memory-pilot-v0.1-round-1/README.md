# Zombie Memory Pilot v0.1 — Round 1 runner

Status: **configuration pending approval; no empirical requests sent**

This directory is independent from the frozen Pilot v0.1 research instrument. The runner reads only the four frozen files under `benchmarks/zombie-memory/pilot-v0.1/generated/` and verifies their SHA-256 hashes before any run. It never reads `cases.json`, gold labels, or `scorer.py`.

## Proposed configuration

- Provider: OpenAI.
- API: Responses API.
- Model: `gpt-4.1-mini-2025-04-14` snapshot.
- Temperature: `0`.
- Top-p: `1`.
- Maximum output: 256 tokens per response.
- Structured Outputs: strict per-case JSON schema.
- Conversation state: none; every case is an independent request with only its frozen prompt.
- Retries: zero. Request, transport, and parse failures are persisted as failures.
- Storage: API request parameter `store: false`.

Temperature zero reduces sampling variation but does not guarantee bit-for-bit identical responses from a hosted model.

## Commands

Dry-run, which never calls an external API:

```powershell
python experiments/runs/zombie-memory-pilot-v0.1-round-1/runner.py --mode dry-run
```

Live mode is deliberately gated and must not be used until the experimental configuration is approved:

```powershell
python experiments/runs/zombie-memory-pilot-v0.1-round-1/runner.py --mode live --confirm-live
```

Live mode additionally requires `OPENAI_API_KEY`. It writes one JSONL record immediately after every request, including raw response, parsed response or parse error, timing, model identifiers, usage, and request metadata. Scoring is not performed by this runner.
