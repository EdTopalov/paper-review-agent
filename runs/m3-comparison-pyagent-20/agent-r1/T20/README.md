# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

3 model calls · 2 reads · 6.47 s · $0.001229

3 decisions · 3 tool calls · 9550 input tokens (1783 cached) · 500 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

RAFT is a post-training recipe for open-book, domain-specific RAG: fine-tune on questions and retrieved contexts, including distractors, while training the model to cite relevant passages and provide reasoning. The paper reports gains across biomedical QA, Wikipedia QA, and API-documentation benchmarks, though the inspected evidence leaves uncertainty about evaluation breadth and reproducibility.

- **strength**: The paper evaluates across varied domains and compares against retrieval and domain-specific fine-tuning baselines.
  - Page 4 · citation: whitespace
  - Quote: "We selected these datasets to represent both popular and diverse domains including Wikipedia, Coding/API documents, and question-answering on medical documents."

- **strength**: The reported table shows substantial gains on some benchmarks, while also showing limited gains on others.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The paper explicitly reports that RAFT does not significantly improve over a key baseline on binary PubMed QA.
  - Page 4 · citation: whitespace
  - Quote: "for PubMed QA, since it is a binary yes/no question, we don’t observe significant gains when we compare our model with DSF + RAG."

- **uncertainty**: The inspected evaluation pages state headline performance claims but do not establish statistical uncertainty or variation across runs; this assessment did not inspect the remaining sections for such evidence.
  - Page 4 · citation: whitespace
  - Quote: "We see that RAFT consistently and significantly outperforms the baselines."

Unresolved questions:

- How much do results vary across training runs and random seeds?
- How sensitive are the gains to the synthetic reasoning-and-citation data generation process?
- What further limitations or evaluation details are presented in the uninspected pages 6–11?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate the paper's evaluation results to assess empirical support. | 5 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Read core results and experimental setup for evidence and scope. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | The abstract, evaluation setup, results table, and discussion were inspected; submit an evidence-based assessment while noting that later sections were not read. | review accepted | [event 16](trace.jsonl#L16) |
