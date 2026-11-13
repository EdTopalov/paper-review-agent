# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 9.73 s · $0.002144

1 decisions · 0 tool calls · 13497 input tokens (0 cached) · 913 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT proposes fine-tuning language models for domain-specific retrieval-augmented question answering using retrieved contexts that mix relevant documents with distractors, and sometimes omit the answer-bearing document. It also trains on answers with cited evidence and reasoning. Results across biomedical, multi-hop QA, and API-document tasks suggest this recipe can improve in-domain RAG performance, though the evidence is bounded by the paper’s setting and reporting.

- **strength**: The paper gives a clear, practical training recipe that directly targets distractor robustness and imperfect retrieval.
  - Page 3 · citation: exact
  - Quote: "P % of data: Q + D∗ + D2 + . . . + Dk → A∗"

- **strength**: Reported benchmark results show substantial gains over the base model and several fine-tuning baselines, particularly on HotpotQA and HuggingFace.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors explicitly limit the study to evaluation on the same document collection used during training, so the results do not establish transfer to new domains or document sets.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The supplied results report point estimates, but do not establish how stable the gains are across training runs or evaluation samples; the magnitude and reliability of some improvements therefore remain unclear.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

Unresolved questions:

- How much do the reported improvements vary across random seeds and evaluation samples, especially where the advantage over a baseline is small?
- Would the recipe retain its benefits when evaluated on documents or domains not used during fine-tuning?
- How sensitive are the results to the retriever and to the quality of the generated reasoning-and-citation training targets?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
