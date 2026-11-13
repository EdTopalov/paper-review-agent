# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 6.53 s · $0.002020

1 decisions · 0 tool calls · 13497 input tokens (0 cached) · 665 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT is a practical fine-tuning recipe for in-domain RAG: train on question–answer examples with oracle and distractor documents, sometimes omit the oracle, and provide answers with reasoning and source quotations. The reported results show gains over the paper’s fine-tuning and RAG baselines on several domain-specific benchmarks, while the paper’s stated focus on a fixed document collection limits how broadly those gains can be generalized.

- **strength**: The paper reports consistent gains for RAFT over its domain-specific fine-tuning baselines on the main benchmark table, including cases where adding RAG to the baseline does not help.
  - Page 5 · citation: exact
  - Quote: "RAFT consistently outperforms the existing domain specific finetuning method with or without RAG."

- **strength**: The paper examines design choices beyond the headline comparison, including chain-of-thought training and varying the share of examples with oracle context; the reported CoT ablation shows improvements on some, but not all, datasets.
  - Page 7 · citation: whitespace
  - Quote: "With a gain of 9.66% and 14.93% on the Hotpot QA and HuggingFace datasets respectively."

- **limitation**: The authors explicitly restrict their setting to testing on the same document collection used for training, so the results do not establish performance when the domain or documents change.
  - Page 9 · citation: whitespace
  - Quote: "we only care about testing the LLM on the same set of documents."

- **uncertainty**: The inspected results report benchmark scores and ablations, but do not establish how stable the comparisons are across repeated runs or how sensitive they are to the particular training-data and evaluation setup.
  - Page 5 · citation: wrong_page
  - Quote: "We see that RAFT consistently and significantly outperforms the baselines."

Unresolved questions:

- How well does RAFT transfer to new documents or domains, rather than the fixed document collection that the paper studies?
- How much of the reported benefit depends on the generated reasoning and quotation format, versus the oracle/distractor training setup?
- How stable are the reported benchmark comparisons across training runs and alternative retrieval or evaluation configurations?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
