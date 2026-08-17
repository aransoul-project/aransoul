# Zombie Memory Preprint v0.1 — Working References

Status: verified working bibliography for manuscript preparation. Final citation style and bibliographic metadata should be checked again at submission time.

## Core neighboring work

1. Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. **LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.** arXiv:2410.10813, 2024.

2. Hanxiang Chao, Yihan Bai, Rui Sheng, Tianle Li, and Yushi Sun. **STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?** arXiv:2605.06527, 2026.

3. Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, and Kai-Wei Chang. **LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues.** arXiv:2605.12493, 2026.

4. Md Nayem Uddin, Kumar Shubham, Eduardo Blanco, Chitta Baral, and Gengyu Wang. **From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents.** arXiv:2604.20006, 2026. Introduces Memora and Forgetting-Aware Memory Accuracy (FAMA).

5. Qiuyang Zhan, Rui Zhang, Sheng Guo, Lepeng Zhao, and Zhuotao Liu. **When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary.** arXiv:2608.01679, 2026. Introduces AuthMem-Bench.

## Broader benchmark context

6. Yuanzhe Hu, Yu Wang, and Julian McAuley. **Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions.** arXiv:2507.05257, 2025. Introduces MemoryAgentBench and includes selective forgetting among core memory competencies.

7. Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, and Zhenhua Dong. **MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents.** arXiv:2506.21605, 2025.

8. Weiwei Xie, Shaoxiong Guo, Fan Zhang, Tian Xia, Xue Yang, Lizhuang Ma, Junchi Yan, and Qibing Ren. **MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents.** arXiv:2604.15774, 2026.

## Citation-use notes

- LongMemEval and LongMemEval-V2 support background claims that agent memory evaluation extends beyond static recall into temporal updates, dynamic state, and premise awareness.
- STALE is the primary comparison for implicit invalidation and stale-state behavior.
- Memora/FAMA is the primary comparison for penalizing reuse of obsolete or invalidated memory.
- AuthMem-Bench is the closest comparison for explicit memory-authority terminology, but its primary boundary is memory consolidation/write-time authority preservation rather than Zombie Memory's decision-time exact authority-set identification.
- None of these papers should be described as independent replication of Zombie Memory Holdout v0.1.
- Do not claim priority over stale-memory, memory-update, forgetting, provenance, or memory-authority research as a whole.
