# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

4 model calls · 3 reads · 10.02 s · $0.001291

4 decisions · 4 tool calls · 19004 input tokens (12110 cached) · 642 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT is a practical supervised fine-tuning recipe for domain-specific RAG: train on question/context/answer examples that mix answer-bearing documents with distractors, and use cited reasoning-style answers. Evaluations across biomedical QA, Wikipedia QA, and API documentation show strong gains over the paper’s compared fine-tuning and RAG baselines, with analyses of reasoning and distractor robustness. The results support a useful contribution, though the evidence inspected is benchmark-specific and leaves broader transfer and evaluation details open.

- **strength**: The proposed training format directly targets imperfect retrieval by distinguishing oracle documents from distractors and sometimes training without the oracle context.
  - Page 3 · citation: whitespace
  - Quote: "We differentiate between two types of documents: ‘oracle’ documents (D∗) i.e. the documents from which the answer to the question can be deduced, and ‘distractor’ documents (Di) that do not contain answer-relevant information."

- **strength**: The main benchmark table reports substantial gains on some tasks against the listed baselines, including HotpotQA and HuggingFace API calls.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The paper itself reports a case where RAFT does not outperform domain-specific fine-tuning plus RAG, so the improvements are not uniform across its metrics.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **uncertainty**: The inspected pages describe benchmark comparisons and analyses but do not establish how reliably gains transfer beyond these tasks or training setups; I did not inspect the remaining pages for further evidence or limitations.
  - Page 4 · citation: whitespace
  - Quote: "We selected these datasets to represent both popular and diverse domains including Wikipedia, Coding/API documents, and question-answering on medical documents."

Unresolved questions:

- How sensitive are the results to the model size, data-generation procedure, and choices of retrieval system outside the reported benchmarks?
- Do gains persist on independently constructed domain-specific corpora and under evaluation protocols that separate memorized answers from context-grounded extraction?
- What additional methodological details or limitations appear in the uninspected pages 7–11?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate reported evaluation results to assess empirical support. | 5 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method, experimental setup, and results for concrete evidence. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Inspect dataset construction and robustness analyses for scope and caveats. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit evidence-based assessment from the inspected method, results, and robustness pages; note uninspected remainder. | review accepted | [event 20](trace.jsonl#L20) |
