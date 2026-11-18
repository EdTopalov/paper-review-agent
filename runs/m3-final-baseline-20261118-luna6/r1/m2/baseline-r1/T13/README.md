# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 6.39 s · $0.000520

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 498 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when retrieval is useful, assess retrieved passages and generated segments with learned reflection tokens, and use those assessments to guide decoding. Across six tasks, its 7B/13B models show strong results against the reported baselines, with especially notable citation precision and recall on long-form QA. The paper’s central contribution is an integrated, controllable retrieval-and-generation framework, supported by task evaluations, ablations, and human checks of selected judgments.

- **strength**: The framework combines on-demand retrieval with segment-level relevance, support, and utility assessments, and uses these signals to control output selection at inference.
  - Page 6 · citation: whitespace
  - Quote: "The weights wG in Eq. 4 are hyperparameters that can be adjusted at inference time to enable customized behaviors at test time."

- **strength**: The reported results are broad and include strong citation metrics: SELF-RAG 13B reaches 70.3 citation precision and 71.3 recall on ASQA, while SELF-RAG 7B has the highest listed FactScore.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: The paper acknowledges that citation-linked self-assessment does not ensure factual support; users still need to verify outputs.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations."

- **uncertainty**: The human evaluation is small and selective, so the reported agreement and support judgments leave uncertainty about reliability at broader scale and across tasks.
  - Page 10 · citation: whitespace
  - Quote: "we sampled 50 samples from PopQA and Bio results."

Unresolved questions:

- How do reflection-token judgments and resulting gains hold up under larger, independently sampled human evaluations across all six tasks?
- How sensitive are results to the retrieval corpus, retriever quality, and changing or stale evidence?
- What are the comparative latency and compute costs of parallel passage processing and segment-level beam search versus conventional RAG?
- I inspected the supplied pages, including the main results and selected appendix material; I did not inspect every experimental detail or reproduce the experiments.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
