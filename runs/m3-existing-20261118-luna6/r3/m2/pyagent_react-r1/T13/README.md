# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

5 model calls · 3 reads · 12.27 s · $0.001721

5 decisions · 4 tool calls · 30390 input tokens (21114 cached) · 701 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

Self-RAG trains a language model to decide when to retrieve and to generate segment-level reflections about passage relevance, factual support, and response usefulness. The reported six-task comparisons and component ablations provide substantial evidence for adaptive retrieval and reflection-guided selection, alongside controllable trade-offs in citation support and fluency. The approach is promising, though conclusions are bounded by the reported benchmarks and limited human evaluation.

- **strength**: The framework combines on-demand retrieval, parallel passage-conditioned generation, and reflection-guided selection in one trained model.
  - Page 4 · citation: whitespace
  - Quote: "To generate each segment, SELF -R AG processes multiple passages in parallel and uses its own generated reflection tokens to enforce soft constraints"

- **strength**: The benchmark table reports broad gains over non-proprietary retrieval baselines, while also showing that performance is not uniformly best across metrics or compared with proprietary systems.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: Ablations examine training and inference components, and report drops from removing retrieval-related or critique mechanisms on selected tasks.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: Human validation is small and samples only two task settings, limiting the breadth of the reported human assessment.
  - Page 10 · citation: whitespace
  - Quote: "In particular, we sampled 50 samples from PopQA and Bio results."

Unresolved questions:

- How well do the reflection-token predictions and citation support generalize beyond the reported datasets and evaluation settings?
- How robust are results to alternative retrievers, passage collections, and domains?
- I inspected pages 1–4 and 8–12, not the full 30-page paper or its appendices; details of data construction, prompting, and additional evaluations remain unchecked.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the framework and training method. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark results and evaluation evidence. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Check comparative task results and reported evaluation scope. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit assessment using the inspected method, results, and limitations. | review accepted | [event 25](trace.jsonl#L25) |
