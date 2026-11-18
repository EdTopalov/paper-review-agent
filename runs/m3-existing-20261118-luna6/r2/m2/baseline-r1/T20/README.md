# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 8.91 s · $0.000473

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 676 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT proposes fine-tuning language models for domain-specific retrieval-augmented question answering using relevant and distractor documents, with quoted evidence and reasoning-style answers. Results across medical, multi-hop QA, and API-document tasks suggest benefits over the reported baselines, while the paper explicitly limits its focus to evaluation on the same document collection used for training.

- **strength**: The reported results show substantial gains over several baselines on some tasks, including HotpotQA and HuggingFace API questions.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **strength**: The paper includes an ablation indicating that reasoning-style answers improve results on some datasets, though not uniformly across all listed tasks.
  - Page 7 · citation: whitespace
  - Quote: "With a gain of 9.66% and 14.93% on the Hotpot QA and HuggingFace datasets respectively."

- **limitation**: The authors define a narrow evaluation scope: performance on the same documents used during training, rather than generalization to new domains or document collections.
  - Page 9 · citation: whitespace
  - Quote: "we only care about testing the LLM on the same set of documents."

Unresolved questions:

- How well does RAFT generalize to new or changing document collections, beyond the same-document setting identified as the paper’s focus?
- The supplied pages do not provide enough detail to assess sensitivity to training-data construction and implementation choices, such as dataset sizes and the full fine-tuning configuration.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
