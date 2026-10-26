# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

5 model calls · 4 reads · 12.22 s · $0.001657

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

Self-RAG trains language models to decide when to retrieve, assess retrieved evidence and generated segments with reflection tokens, and use those signals for controllable decoding. Across six tasks, its reported results and ablations provide substantial evidence of gains over several retrieval and non-retrieval baselines, especially in factuality and citation measures, though evidence is scoped to particular models, datasets, and evaluation choices.

- **strength**: The framework integrates on-demand retrieval, tokenized critique, and customizable decoding, rather than treating retrieval as a fixed input step.
  - Page 2 · citation: whitespace
  - Quote: "our inference-time algorithm enables us to (1) flexibly adjust retrieval frequency for different downstream applications and (2) customize models’ behaviors to user preferences"

- **strength**: The reported results show competitive or leading performance across varied tasks, including large citation-precision and recall results on ASQA relative to listed retrieval baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: Ablations test multiple components and report deterioration when retrieval or critique is removed, or when only the top passage is used.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: The evaluation relies partly on previously reported results where implementations were unavailable, limiting direct comparability and independent verification within this study.
  - Page 7 · citation: exact
  - Quote: "We report numbers using the results reported in the paper as the implementations are not available."

Unresolved questions:

- How robust are the reported gains across additional model families, retrievers, and datasets beyond the evaluated setup?
- How do the reflection-token labels and critic supervision affect reliability when the proprietary-LM-generated supervision is imperfect?
- I inspected pages 1–3 and 7–9, not the remaining paper; training details, further analyses, and stated limitations elsewhere may qualify this assessment.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 2 describes on-demand retrieval, reflection tokens for critique, and inference-time decoding that adjusts retrieval frequency and user-preference tradeoffs.
- Observation 2: **supported** — Page 8 reports results across six tasks and shows ASQA citation precision and recall of 70.3 and 71.3 for Self-RAG 13B. The text says these exceed all listed models except ChatGPT, and Self-RAG exceeds ChatGPT on citation precision.
- Observation 3: **supported** — Pages 9–10 describe training and inference ablations, including removing the retriever, critic, retrieval, or ISSUP, and using only the top passage. The paper reports performance drops for several of these comparisons, including top-1 retrieval on PopQA and ASQA.
- Observation 4: **supported** — Page 7 states that results for some baselines are taken from their papers because implementations were unavailable, supporting the qualified comparability and independent-verification limitation.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experimental Setup"}` | Locate the evaluation setup to assess how the paper supports its claimed gains. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "Results"}` | Find reported experiment results for evaluating the evidence behind the abstract's performance claims. | 8 matches on pages [2, 7, 8, 9] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect evaluation comparisons and ablation analysis to judge empirical support and caveats. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 2, "end": 3}` | Inspect the framework description and training signal to assess novelty and methodological substance. | read pages [2, 3] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers method, benchmark setup, results, and ablations; submit a provisional assessment while noting inspection gaps. | review accepted | [event 25](trace.jsonl#L25) |
