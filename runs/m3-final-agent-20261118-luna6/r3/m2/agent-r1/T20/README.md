# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

5 model calls · 3 reads · 13.02 s · $0.001563

5 decisions · 5 tool calls · 25934 input tokens (18752 cached) · 986 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT proposes supervised fine-tuning for domain-specific RAG that trains models to answer with retrieved context, quote relevant evidence, and tolerate distractor documents. Results across biomedical QA, multi-hop QA, and API documentation show strong gains over several fine-tuning and RAG baselines, though its demonstrated setting is deliberately in-domain and same-document at training and test time.

- **strength**: The training recipe directly targets retrieval imperfections by teaching the model to select useful evidence rather than treating all retrieved text as relevant.
  - Page 1 · citation: exact
  - Quote: "we train\nthe model to ignore those documents that don’t\nhelp in answering the question, which we call,\ndistractor documents."

- **strength**: Reported results show strong scores across API and QA tasks, compared with the baselines shown in the table.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors bound their intended use to the same document collection at training and test time, so generalization to changing or unseen domains is not established here.
  - Page 9 · citation: exact
  - Quote: "we only care about testing\nthe LLM on the same set of documents."

- **uncertainty**: The inspected evidence includes benchmark tables and an ablation, but does not establish uncertainty across seeds or sensitivity to reasoning-generation choices.
  - Page 7 · citation: whitespace
  - Quote: "Results on various datasets show that adding CoT can significantly improve the performance of the finetuned model."

Unresolved questions:

- How stable are the gains across random seeds and alternative training-data or reasoning-generation procedures?
- How well does the recipe transfer to document collections or domains not seen during training?
- What are the compute and data-generation costs relative to simpler RAG or fine-tuning approaches?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate reported evaluation results to assess empirical support. | 5 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect methods and quantitative results underlying the claimed gains. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect stated limitations and experimental setup details to bound assessment. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers proposal, benchmark results, scope, and an ablation; submit a bounded assessment. | citation_validation_failed; #4: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with the CoT ablation quote exactly as observed on page 7 and retain only inspected evidence. | review accepted | [event 25](trace.jsonl#L25) |
