# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

5 model calls · 3 reads · 12.22 s · $0.001887

5 decisions · 4 tool calls · 31657 input tokens (21118 cached) · 718 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

Self-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated segments with reflection tokens, and use those assessments to guide generation. Its evaluations show strong results across a range of retrieval, reasoning, and long-form tasks, with component ablations and inference-time customization analyses. The approach is substantial and promising, though evidence for reflection-token reliability includes a small human evaluation, and supported citations are not guaranteed.

- **strength**: The method integrates retrieval decisions, passage relevance, support judgments, and response usefulness into generation and decoding.
  - Page 4 · citation: whitespace
  - Quote: "For every x and preceding generation y<t, the model decodes a retrieval token to evaluate the utility of retrieval."

- **strength**: Across the reported benchmark suite, the 7B and 13B models achieve strong results against the included baselines, including high citation precision and recall on ASQA.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: The paper includes ablations of training and inference components; its sampled ASQA ablation evaluation is narrower than the full benchmark evaluation.
  - Page 9 · citation: whitespace
  - Quote: "On ASQA, we evaluate models on sampled 150 instances and exclude ablations involving adaptive or no retrieval processes."

- **limitation**: The authors explicitly caution that generated claims may not be fully supported by citations, so reflection and attribution do not ensure factual correctness.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations."

Unresolved questions:

- How reliably do the reflection-token judgments generalize beyond the small human evaluation described on page 10?
- How do performance and retrieval costs change across broader deployment conditions and retrieval sources?
- How often do unsupported claims or incorrect self-assessments occur in longer or more diverse generations?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the method and reflection-token training details. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark results and experimental comparisons. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect task-level results and the paper's stated scope boundaries. | read pages [7, 8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment using the inspected method, results, and limitations pages. | review accepted | [event 25](trace.jsonl#L25) |
