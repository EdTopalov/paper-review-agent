# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 6.90 s · $0.000541

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 540 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when to retrieve, assess passage relevance and answer support with learned reflection tokens, and use those assessments to guide segment-level decoding. Across six tasks, the reported results show strong performance against several retrieval and non-retrieval baselines, particularly for factuality and citation metrics; the paper also demonstrates inference-time trade-offs through adjustable retrieval thresholds and critique weights.

- **strength**: The method integrates retrieval decisions, evidence assessment, and generation control in one trained model, with reflection signals used during decoding.
  - Page 4 · citation: wrong_page
  - Quote: "These reflection tokens (Table 1) signal the need for retrieval or confirm the output’s relevance, support, or completeness."

- **strength**: The paper provides broad task coverage and reports competitive outcomes, including strong citation precision and recall on ASQA.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: The reflective judgments are partly distilled from GPT-4, and the paper reports noticeably lower agreement for usefulness than for some other categories; this makes that signal’s reliability less certain.
  - Page 17 · citation: whitespace
  - Quote: "Agreement was slightly lower in usefulness (80%), mostly due to the disagreement between 1 and 2 or 4 and 5."

- **uncertainty**: The reported human assessment is small: 50 sampled examples across PopQA and biography generation. How well the reflection judgments and support findings generalize beyond that sample is unresolved.
  - Page 10 · citation: whitespace
  - Quote: "In particular, we sampled 50 samples from PopQA and Bio results."

Unresolved questions:

- How robust are retrieval decisions and support judgments when the retriever returns no useful evidence or the corpus is stale or incomplete?
- How do performance and latency compare under realistic deployment settings, given parallel passage processing and segment-level beam search?
- How well do the results generalize to domains and tasks beyond the six evaluated, especially where evidence attribution is more difficult?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
