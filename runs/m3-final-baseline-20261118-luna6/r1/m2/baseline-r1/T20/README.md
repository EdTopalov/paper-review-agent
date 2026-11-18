# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 8.34 s · $0.000492

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 714 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

RAFT fine-tunes language models for domain-specific retrieval-augmented question answering using contexts that mix relevant and distractor documents, sometimes omitting the relevant document, and answers that include reasoning and citations. The reported results suggest this recipe can improve in-domain RAG performance over several fine-tuning and prompting baselines, though the evaluation is explicitly limited to testing on the same document collection used for training.

- **strength**: The paper gives a clear, practical training recipe that directly targets handling noisy retrieved context.
  - Page 3 · citation: whitespace
  - Quote: "we prepare the training data such that each data point contains a question (Q), a set of documents (Dk), and a corresponding Chain-of-though style answer"

- **strength**: The reported benchmark results support gains over the listed baselines on several tasks, including HotpotQA and HuggingFace; the table also shows weaker or mixed gains on other tasks.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors explicitly restrict the setting to testing on the same documents used in training, so the results do not establish transfer to new collections.
  - Page 9 · citation: whitespace
  - Quote: "we only care about testing the LLM on the same set of documents."

- **uncertainty**: The inspected pages report point estimates but do not establish whether the benchmark differences are statistically reliable; the supplied excerpt also does not provide enough training and evaluation detail to assess reproducibility fully.
  - Page 5 · citation: wrong_page
  - Quote: "We see that RAFT consistently and significantly outperforms the baselines."

Unresolved questions:

- How sensitive are the results to training-data construction, answer-generation quality, and random seed? The supplied pages do not report uncertainty estimates or repeated-run results.
- Would the gains persist when the test document collection differs from the training collection, or when the retriever and document distribution change?
- What are the full training and evaluation details needed to reproduce the reported results, including data splits, metrics, and hyperparameters?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
