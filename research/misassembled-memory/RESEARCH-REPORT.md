# M02 — Cross-round exploratory findings

**Evidence label:** `CONTENT_PROVISIONAL / EXECUTION_UNVERIFIED`  
**Study type:** Human-operated, synthetic, user-relayed exploratory observations; cross-round desk review.

## Study design

Four prompt-response batches examined synthetic conflicting summaries about fictional animals and dates. Some prompts supplied an explicit original record, others supplied only a summary; the tasks ranged from auditing a summary to directly answering a question of the form "Do you remember?". R06 crossed source availability (original record present / absent) with direct-answer framing versus an extra pre-answer verification sentence. R05 was a separate retrospective desk review, not another run.

The exploratory scores follow batch-specific criteria documented before grading, subject to a retained R02 prompt-copy fidelity concern; submitted inputs, model identity, chat mode and first responses have not been independently verified. See [evidence limitations](EVIDENCE-LIMITATIONS.md).

## User-relayed answer counts

| Batch | Focus | Responses | Green (provisional) | Red (provisional) |
| --- | --- | ---: | ---: | ---: |
| R02 | Repeated erroneous summary with explicit source | 4 | 4 | 0 |
| R03 | Summary audit under source-availability conditions | 6 | 6 | 0 |
| R04 | Natural conversational question under source conditions | 6 | 2 | 4 |
| R05 | Desk review only | 0 | 0 | 0 |
| R06 | Source availability × direct vs reminder framing | 8 | 4 | 4 |
| **Total** | **Four response batches** | **24** | **16** | **8** |

The 24 answers are neither independently verified execution receipts nor statistically independent random samples. The Green/Red counts should **not** be converted into general accuracy estimates.

## Bounded observations

1. **Explicit synthetic original records:** The 12 answers that were supplied such records (R02: 4, R03: 2, R04: 2, R06: 4) were all provisionally Green. This tests source usage within text supplied to a model, *not* actual memory retrieval.
2. **Audit-task counterexample:** In R03, all four no-original-source audit answers kept summary information unconfirmed (Green). Thus missing source material does not always imply unwarranted certainty.
3. **Natural-answer framing:** In R04 and R06, eight no-original-source answers were provisionally Red for presenting unsupported summary details as established facts, without sufficient source qualification. The Red classification measures **unsupported certainty**, not whether a model could have known hidden correct values.
4. **Short verification reminder:** Within R06, both no-source direct answers (2/2) and no-source reminder answers (2/2) were Red; both source-present direct (2/2) and source-present reminder answers (2/2) were Green. No improvement appeared in this batch; this does *not* establish a general causal null effect.
5. **Repeated error presentation:** R02 did not show a difference between its one-versus-two erroneous-summary presentations in this tiny sample, and one prompt had a fidelity caveat.

## Interpretation and counterevidence

- The source-present pattern is consistent with the model correctly following visible original-record text. It does not demonstrate a repaired long-term memory mechanism.
- R03 supplies an explicit counterexample to the overly broad claim that absence of original evidence necessarily causes confident assertion.
- R03-versus-R04/R06 comparisons change multiple aspects of task framing, not just one controlled variable. Consequently, differences may stem from audit instructions, response style, salience, scenario variation, or other factors.
- R06's extra verification sentence is longer and more salient than its direct-answer counterpart; the intervention is not a clean isolation of an internal checking process.
- No product memory write/retrieval traces, provider-signed execution records, or original incident diagnostics were available. Historical root cause remains **unresolved**.

## Permitted conclusion

The synthetic cases show a **candidate risk of converting an unsupported summary into an unqualified factual answer under natural conversational prompting**, while demonstrating that more explicitly source-conscious task forms can preserve uncertainty in some conditions. More controlled, independently documented tests are necessary before attributing cause or generalizing across systems.

**Not established:** a memory-system mechanism, a real-world failure prevalence, a tested repair, statistically significant effects, an independent replication, or any change in formally adopted governance.
