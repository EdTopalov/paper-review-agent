# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 4.88 s · $0.003614

1 decisions · 0 tool calls · 27075 input tokens (0 cached) · 459 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when to retrieve, assess passage relevance and output support, and use these reflection signals to guide segment-level generation and selection. Its broad benchmark results and ablations provide substantial evidence that this approach can improve factuality, task performance, and citation quality, while leaving important questions about evaluation scale and the reliability of model-generated critiques.

- **strength**: The method combines retrieval decisions, evidence assessment, and controllable decoding in one trained generator, with reflection signals also supporting inference-time trade-offs.
  - Page 6 · citation: not_found
  - Quote: "SELF-RAG tailors an LM with no additional training."

- **strength**: Across six tasks, the reported results show especially strong citation precision and recall on ASQA compared with the listed non-proprietary retrieval baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: Ablations compare training and inference components, including the effect of retrieving the top passage regardless of relevance and removing support scoring.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: The human check is small: the paper reports sampling only 50 examples from two tasks, limiting how broadly those judgments establish reflection-token reliability.
  - Page 10 · citation: whitespace
  - Quote: "we sampled 50 samples from PopQA and Bio results."

Unresolved questions:

- How robust are the reported gains across more datasets, domains, and larger or independently sampled human evaluations?
- How reliably do the critic and generator judge support when passages are misleading, incomplete, or conflict with one another?
- How do inference cost and latency compare with conventional RAG under the parallel passage processing and segment-level beam search?
- This assessment inspected the supplied pages and their reported results, but did not independently verify experiments or inspect any material beyond the supplied document.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
