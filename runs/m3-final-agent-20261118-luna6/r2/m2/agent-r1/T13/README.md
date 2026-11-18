# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

7 model calls · 5 reads · 15.83 s · $0.003701

7 decisions · 7 tool calls · 53336 input tokens (30529 cached) · 1134 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.82

Self-RAG trains language models to retrieve on demand and emit reflection signals that assess passage relevance, evidential support, and usefulness, then uses those signals to guide inference-time selection. Multi-task comparisons and component ablations support a substantial, practically meaningful contribution, while the evidence remains bounded by evaluated settings and a small human study.

- **strength**: The proposed framework pairs on-demand retrieval with generated reflection tokens that also allow test-time control.
  - Page 1 · citation: exact
  - Quote: "Our framework trains a single arbitrary LM that adaptively\nretrieves passages on-demand, and generates and reflects on retrieved passages\nand its own generations using special tokens, called reflection tokens."

- **strength**: Evaluation covers six tasks and reports strong results, although the model does not lead on every metric.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 7B 54.9 66.4 72.4 67.3 81.2 30.0 35.7 74.3 66.9 67.8"

- **strength**: Ablations support the value of critique-guided selection over indiscriminately using top-ranked passages.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: The paper explicitly notes that the method does not guarantee citations fully support generated outputs.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations."

Unresolved questions:

- How well do retrieval decisions and reflection-token judgments generalize beyond the tested tasks, datasets, and retriever configuration?
- The human evaluation sampled 50 examples from two settings; how stable are those judgments on larger, more diverse samples?
- I inspected the abstract and selected evaluation, analysis, and ethical-concerns pages, but not the full method details or appendices; training-data construction and detailed evaluation procedures remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate the paper’s evaluation section and reported empirical results. | 4 matches on pages [1, 3, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect empirical setup, main results, and evaluation scope. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 10}` | Inspect robustness analyses and the authors’ stated limitations or caveats. | read pages [9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 12}` | Check for explicit limitations, ethical caveats, or broader conclusions. | read pages [11, 12] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.82, "observations": 4}}` | Evidence covers proposed framework, broad evaluation, ablations, and acknowledged citation shortcomings; submit a balanced assessment noting the limited inspected scope. | citation_validation_failed; #1: not_found | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 1, "end": 1}` | Retrieve exact abstract wording for a verified contribution quote. | read pages [1] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.82, "observations": 4}}` | Resubmit with an exact verified abstract quotation; prior evidence supports the score and balanced observations. | review accepted | [event 36](trace.jsonl#L36) |
