# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 5.66 s · $0.000511

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 480 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when to retrieve, assess passage relevance and evidential support, and score its own generated segments using learned reflection tokens. Its experiments across six task settings show strong results against the selected baselines, especially for factuality and citation metrics, while inference-time token weighting offers a mechanism for trading off support and fluency.

- **strength**: The paper combines adaptive retrieval with segment-level critique and controllable decoding, rather than treating retrieval as a fixed input-augmentation step.
  - Page 6 · citation: whitespace
  - Quote: "The weights wG in Eq. 4 are hyperparameters that can be adjusted at inference time to enable customized behaviors at test time."

- **strength**: The reported results are broad and include gains in factuality and citation measures, with a clear qualification that ChatGPT remains ahead on some ASQA measures.
  - Page 8 · citation: whitespace
  - Quote: "our model shows significantly higher citation precision and recall than all models except ChatGPT."

- **limitation**: The critic’s supervision relies substantially on GPT-4-generated judgments, and its reported agreement is lower for utility than for the other categories; this makes critic quality a meaningful dependency.
  - Page 17 · citation: whitespace
  - Quote: "Agreement was slightly lower in usefulness (80%), mostly due to the disagreement between 1 and 2 or 4 and 5."

- **uncertainty**: The evaluation covers six tasks and selected retrieval/model configurations, but the inspected results do not establish how performance transfers to other domains, retrievers, or substantially different evidence collections.
  - Page 7 · citation: whitespace
  - Quote: "In total, we use 150k instruction-output pairs."

Unresolved questions:

- How robust are reflection-token judgments and the resulting gains when the critic is trained without GPT-4-generated labels or evaluated against larger, independent human annotations?
- How do retrieval latency and total inference cost compare with standard RAG and iterative refinement at matched quality, especially as the number of passages or beam width grows?
- Do the performance and citation findings persist across different retrievers, corpus snapshots, and domains beyond the evaluated tasks?
- The inspected material includes the main paper and portions of the appendix, but not every appendix detail or underlying implementation; how sensitive are results to all training and evaluation choices?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
