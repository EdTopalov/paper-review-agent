# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 9.89 s · $0.002076

1 decisions · 0 tool calls · 13497 input tokens (0 cached) · 777 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

RAFT is a fine-tuning recipe for domain-specific, open-book question answering: train on questions, retrieved documents that may include distractors, and answers with quoted evidence and reasoning. Results across medical QA, HotpotQA, and API-document benchmarks suggest it can improve over the paper’s fine-tuning and RAG baselines. The contribution is practical and supported by several comparisons and ablations, but its claims are explicitly scoped to in-domain use, and the supplied pages leave important details about experimental reliability and transfer unresolved.

- **strength**: The paper evaluates RAFT across several task domains and reports gains over the listed baselines, with a separate ablation examining the contribution of chain-of-thought responses.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors define a narrow target setting: testing on the same documents used during training. This is an explicit scope boundary, so the results do not establish performance when the domain or documents change.
  - Page 9 · citation: whitespace
  - Quote: "we only care about testing the LLM on the same set of documents."

- **uncertainty**: The reported comparisons give point scores, but the supplied pages do not establish how stable those scores are across runs or evaluation samples. This limits how confidently small differences, such as the Torch Hub scores, can be interpreted.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

Unresolved questions:

- How much do the reported gains vary across random seeds or evaluation samples?
- How well does RAFT transfer to new documents or domains, beyond the same-document setting the paper studies?
- What training-data construction and evaluation details are needed to reproduce the reported comparisons?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
