# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

5 model calls · 4 reads · 10.12 s · $0.001875

5 decisions · 5 tool calls · 29323 input tokens (18136 cached) · 623 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.79

SELF-RAG trains a language model to decide when retrieval is useful and to score retrieved evidence and generated segments with reflection tokens, enabling adaptive retrieval and critique-guided selection at inference. The paper presents a technically coherent framework with broad benchmark comparisons and component ablations; results are substantial, though evidence is bounded by the evaluated settings and the small human study.

- **strength**: The approach jointly targets retrieval timing, evidence relevance, support, and generation usefulness, with controllable inference-time scoring rather than fixed retrieval alone.
  - Page 6 · citation: whitespace
  - Quote: "Generating reflection tokens to self-evaluate its own output makes SELF -RAG controllable during the inference phase"

- **strength**: Across six tasks, the reported results show strong performance, including gains over non-proprietary retrieval baselines and several proprietary-model comparisons.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: Ablations provide evidence that retrieval and critique components contribute, though the analysis uses reduced training data and sampled ASQA instances.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: The method does not guarantee citation support; the authors explicitly acknowledge residual unsupported outputs despite improved factuality and citation measures.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations"

Unresolved questions:

- How robust are gains across different retrievers, domains, and current model families beyond the specific evaluated setup?
- The human evaluation samples only 50 examples from PopQA and biography generation; how reliable are the reflection judgments and support quality at larger scale?
- Appendix details and later portions of the paper were not inspected, including fuller training, prompt, and evaluation protocol specifications.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experiments"}` | Locate the paper's evaluation evidence and reported task results. | 4 matches on pages [1, 3, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect evaluation setup, outcome tables, and any noted caveats. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 10}` | Check authors' analysis of failures and stated limitations. | read pages [9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 12}` | Inspect any explicit limitations and final discussion beyond the conclusion. | read pages [11, 12] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.79, "observations": 4}}` | Evidence covers the method, main benchmark results, ablations, and an explicit safety caveat; submit a bounded assessment noting uninspected appendix details. | review accepted | [event 25](trace.jsonl#L25) |
