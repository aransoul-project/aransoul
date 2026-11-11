# Cross-environment memory authority reconciliation — observational case (2026-11-12)

> **Status:** `OBSERVATIONAL_CASE / USER_RELAYED_CODEX_AUDIT / NOT_INDEPENDENTLY_VALIDATED`  
> **Scope:** ChatGPT conversation context versus local Codex memory summaries, with read-only checks against authoritative Notion and GitHub documents.  
> **Not:** a benchmark, prevalence estimate, memory synchronization implementation, proof of autonomous governance, or authorization for model/API/agent experiments.  
> **Safety:** `D3_HOLD_UNCHANGED / LIVE_MODEL_EXPERIMENT_NOT_AUTHORIZED`.

## Abstract / 摘要

A user operating a long-running AI governance research project observed that a local Codex environment retained an earlier snapshot of a study while a ChatGPT conversation had access to later project decisions. The Codex-reported local memory search did not find several relevant governance records. When explicitly instructed to check the formal sources, Codex reported the newer status and respected the existing hold. This is an **instruction-assisted, user-relayed document reconciliation observation**, not evidence that Codex will autonomously retrieve or apply the latest authority in future tasks.

**核心觀察：** 不同 AI 工作環境可以保留不相同、但各自具有歷史依據的記憶。問題不一定在於「記錯」，而在於**舊記憶是否被誤用為現行決策權威**。本案例只觀察到在明確查核指令下的文件核對表現，尚未驗證自發性、穩定性或完整的產品記憶機制。

## 1. What was compared

The comparison was **asymmetric**:

- **ChatGPT side:** context available in this conversation, prior document checks, and accessible project references. **No full underlying ChatGPT Memory snapshot, retrieval trace, or history versions were inspected.**
- **Codex side:** a user-relayed read-only inventory of locally visible Codex memory Markdown, summaries, and extracted memory records. The report distinguished `MEMORY` (stored local summary), `TASK_CONTEXT` (instructions in the current task), and `CURRENT_DOCUMENT` (freshly fetched authoritative source). **The raw local memory files and complete execution logs were not independently inspected for this note.**
- **Authority side:** formally adopted Notion governance documents and the GitHub `STATUS.md` ledger. Authority depends on adoption, supersession, scope, and date; a recently edited draft does not supersede an effective decision merely by being newer.

The inventory included a reported 13 visible Markdown documents and 6 extracted memory records across two local stores. These counts describe **the Codex-reported search scope**, not all memories or all sources available to the account.

## 2. Case observations (reported, not independently replicated)

| Topic | Codex local memory, as reported | Current documentary state used for reconciliation | Classification |
| --- | --- | --- | --- |
| Governance baseline | General retention/authorization patterns present; no explicit full governance v1.0 or six-stage lifecycle found in scoped local-memory search | Notion governance v1.0, effective 2026-07-17, contains six lifecycle stages and a defined authority hierarchy | Scoped omission / stale coverage |
| D3 safety contract | Historical D3/HOLD context present, with engineering blockers | Formal D3 decision dated 2026-10-30 retains engineering and live-model HOLD; evidence truth, execution safety, and verifiability remain separate | Broadly consistent |
| R07 / M02 | Scoped Codex memory search returned `NOT_FOUND` | R07 is `PAUSED_DUPLICATIVE / DESIGN_ONLY / NOT_RUN`; M02 results are provisional and their execution is unverified | Missing decision context, **not** a demonstrated incorrect Codex action |
| Zombie Memory Holdout | Earlier 96-response `responses_complete_unreviewed` state retained | Public `STATUS.md` reports three within-protocol replications / 288 responses; 186/288 authority exact-set matches | Historical snapshot versus later project progress |

**Key distinction:** The earlier 96-response state need not be a false memory. It is consistent with the reported earlier research phase, but the original local-memory and execution artifacts were not independently rechecked for this note. The decision risk arises **if that historical state is treated as the project's current state without verifying later evidence**.

The user then requested a read-only reconciliation against four named documents. Codex reported `STALE` overall, identified R07 as paused, maintained D3 HOLD, and treated the later GitHub study state as current. The operation was explicitly guided: **this case provides no evidence of spontaneous authority checking**.

## 3. Practical decision pattern illustrated

A minimal governance workflow for consequential research operations is:

1. Use local AI memory **as a locator / historical context**, not as automatically effective authority.
2. Identify whether the proposed task depends on a formal rule, current research state, supersession, or an execution permit.
3. If yes, obtain the controlling source and compare its **authority, effective time, scope, and evidence status** against the remembered claim.
4. Preserve old records as historical evidence; do not silently rewrite the past or collapse distinct phases.
5. If the controlling document is unavailable, conflicting, or unverified, report `UNKNOWN` / `CONFLICT` and avoid turning an old summary into execution permission.
6. Distinguish allowed **read-only analysis** from disallowed experiment setup, API calls, writes, or changes to an existing HOLD.

This is a **candidate operational pattern**, not a claim that an assistant reliably follows these steps unprompted. It is not necessary to synchronize every personal conversation, persona description, or engineering debug note across tools. The practical need is to **reconcile decision authority at use time**.

## 4. Broader relevance: is this common?

This case is **plausibly relevant** to users who work across multiple assistants, coding agents, repositories, and persistent context files. More independent state stores and longer project histories create more opportunities for stale summaries and differing scope. However:

- **No evidence here measures the share of users affected.** It would be unjustified to state that “most users experience cross-tool memory divergence.”
- Existing research on long-term assistant memory tests knowledge updating and temporal reasoning, which are related **capabilities**, not a direct census of ChatGPT–Codex divergence.
- Research on persistent agent context documents identifies outdated guidance and downstream costs. These studies concern **instruction files or repositories**, not necessarily the private memory stores compared in this case.
- Risk is likely more consequential when an old summary is used to authorize real actions than when it merely describes a historical phase. That is a **risk hypothesis**, not an observed incidence estimate.

### Related external work (distinct from this case)

- **LongMemEval** (ICLR 2025): evaluates multi-session reasoning, temporal reasoning, knowledge updates, and abstention. [Conference abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html).
- **Context Rot in AI-Assisted Software Development** (arXiv, 2026-06): documents potential staleness in AI configuration context files and preliminary evidence of outdated references in repositories. Its reported repository percentage is **not** a user prevalence estimate. [Paper](https://arxiv.org/abs/2606.09090).
- **When Instruction Files Go Stale** (arXiv, 2026-11): studies how coding agents may act on outdated repository instructions and the cost of stale guidance. Again, this is not a direct test of cross-product memory synchronization. [Paper](https://arxiv.org/abs/2611.09802).

## 5. Relation to existing AranSoul studies — no duplicated claim

- [M02](../misassembled-memory/RESEARCH-REPORT.md) concerns evidence attribution and over-certainty in user-relayed synthetic answers; its execution provenance remains unverified. **This case does not repeat M02's trials.**
- [Zombie Memory Holdout](../../experiments/holdout/zombie-memory-holdout-v0.1/RESEARCH-REPORT.md) measures current-authority-set identification within a frozen synthetic benchmark; its primary 186/288 result is distinct from this operational case. **This case adds no new holdout response or replication.**
- [AGBench Pilot](../agbench/pilot-v0.1/README.md) is development-only static measurement design; **this note does not change its status**.
- [R07 Notion revision](https://app.notion.com/p/41454b485b6c81369d8eddbc161ad234) records an overlapping candidate that was paused. **No R07 experiment was run or reopened**.

## 6. Evidence and limitations

| Evidence layer | What it supports | What it does not support |
| --- | --- | --- |
| User-relayed Codex inventory and reconciliation tables | A specific reported local-memory/document version gap and an instructed reconciliation | Independent verification of the local memory corpus or autonomous behavior |
| Directly inspectable Notion / GitHub documents | Current recorded governance and public study status at inspection time | Full provider-side memory retrieval, hidden prompts, and future consistency |
| External publications | Context for memory updating and stale AI instructions | Percentage of users affected by this specific ChatGPT–Codex pattern |
| Unrun six-cell governance candidate | A pre-specified possible comparison of decisions under different instructions | Any measured performance, safety improvement, or causal effect |

Further verification, if separately authorized, would require raw time-stamped inputs and first outputs, independent authority adjudication, known source versions, and a distinction between prompted versus unprompted checks. **No such new experiment is authorized or reported here.**

## 7. Source-of-truth links and status preservation

- [Notion formal AranSoul governance v1.0](https://app.notion.com/p/3a054b485b6c8144a604d6dddc563272) — effective 2026-07-17; six-stage memory lifecycle and human final authority.
- [Notion D3 safety contract](https://app.notion.com/p/40954b485b6c81b3b1f4febb4a5efb19) — adopted 2026-10-30; HOLD remains.
- [Notion R07 pause](https://app.notion.com/p/41454b485b6c81369d8eddbc161ad234) — `PAUSED_DUPLICATIVE / DESIGN_ONLY / NOT_RUN`.
- [GitHub STATUS.md](../../STATUS.md) — public v0.1 release lineage, evolving `main` status, and subsequent Holdout findings.

**Versioning note:** Notion *formal governance v1.0* and GitHub *public documentation release v0.1* describe different versioned artifacts; their numbers should not be treated as competing effective versions.

**Publication does not adopt a new formal governance rule, change benchmark outcomes, authorize memory modification, or release D3 HOLD.**

---

**One-sentence takeaway:** Different assistants need not have identical memories; they need a defensible way to distinguish historically remembered information from sources that currently have decision authority.
