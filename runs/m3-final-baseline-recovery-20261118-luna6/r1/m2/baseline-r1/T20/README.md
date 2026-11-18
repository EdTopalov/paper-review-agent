# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 8.53 s · $0.000508

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 746 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT is a fine-tuning recipe for domain-specific, open-book question answering: train on questions with relevant and distractor documents, and sometimes omit the relevant document, while using answers with reasoning and quotations. Results across medical QA, HotpotQA, and API documentation suggest the approach can improve in-domain RAG performance, though gains vary by task and its stated scope is testing on the same document collection used for training.

- **strength**: The paper gives a concrete training design that explicitly models imperfect retrieval, including examples without the oracle document.
  - Page 3 · citation: whitespace
  - Quote: "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."

- **strength**: The reported results show substantial gains on some tasks, while also showing that performance is not uniformly better across all comparisons.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The paper explicitly limits its target setting to in-domain evaluation on the same documents, so the evidence does not establish transfer to new collections.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The preferred share of training examples with oracle context varies by dataset; the supplied pages do not establish how to select this value for a new domain.
  - Page 6 · citation: hyphenation_ambiguous
  - Quote: "Our analysis reveals that the optimal proportion varies across datasets, with figures ranging from 40%, 60%, and 100%."

Unresolved questions:

- How well does RAFT transfer when the test collection differs from the training collection, a setting the paper distinguishes from its own?
- What practical procedure should be used to choose the oracle-context proportion and distractor count for a new domain?
- How sensitive are the reported results to the retrieval setup and data-generation choices? The supplied pages do not provide enough detail to assess this fully.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
