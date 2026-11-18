# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

7 model calls · 3 reads · 24.04 s · $0.002577

7 decisions · 5 tool calls · 50941 input tokens (39551 cached) · 1517 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

Self-RAG trains a language model to decide when to retrieve, generate responses alongside passage-level reflection tokens, and use those signals to guide output selection and controllable decoding. Its broad evaluation and component ablations support the value of this integrated approach, especially for retrieval-dependent and citation-focused tasks, while leaving questions about annotation reliability and generalization beyond the tested settings.

- **strength**: The method integrates retrieval decisions, passage relevance, support judgments, and usefulness into generation and inference-time selection.
  - Page 3 · citation: whitespace
  - Quote: "These reflection tokens (Table 1) signal the need for retrieval or confirm the output’s relevance, support, or completeness."

- **strength**: Evaluation covers six tasks and multiple outcome types; results show strong performance, including citation metrics.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: Ablations examine training and decoding components, with documented drops for some removals or retrieval strategies.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: The paper explicitly cautions that outputs may remain unsupported despite the improvements; this is an important reliability boundary, not evidence that every output fails.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations."

Unresolved questions:

- How well do reflection-token judgments and the reported gains transfer to domains, retrievers, or prompt distributions outside the evaluated benchmarks?
- How sensitive are the results to the critic’s supervision and judgments? The inspected pages mention GPT-4-derived supervision and a small human evaluation, but do not establish broad annotation reliability.
- What are the full runtime and resource costs of retrieval, parallel passage processing, and segment-level decoding relative to simpler baselines?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method details and initial evaluation claims. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 12}` | Inspect experimental results and evaluation methodology. | read pages [10, 11, 12] | [event 19](trace.jsonl#L19) |
| 5 | read_pages `{"start": 7, "end": 9}` | Check benchmark results, baselines, and comparison evidence. | read pages [7, 8, 9] | [event 24](trace.jsonl#L24) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment using inspected methods, results, and limitations. | citation_validation_failed; #1: wrong_page (pages [3]) | [event 29](trace.jsonl#L29) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the citation to the observed page containing the exact quote. | review accepted | [event 34](trace.jsonl#L34) |
