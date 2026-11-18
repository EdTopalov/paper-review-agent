# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

6 model calls · 5 reads · 13.25 s · $0.003072

6 decisions · 6 tool calls · 39119 input tokens (18897 cached) · 749 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

Self-RAG trains a language model to decide when to retrieve, assess passage relevance and answer support, and use reflection-token scores to guide generation. Its reported results across factual QA, reasoning, and citation-focused long-form tasks show substantial improvements over numerous retrieval and non-retrieval baselines, with the strongest evidence in the inspected quantitative table being citation precision/recall and several task accuracy scores.

- **strength**: The central contribution is an integrated, controllable retrieval-and-critique generation procedure, with reflection tokens used both during generation and segment-level selection.
  - Page 4 · citation: whitespace
  - Quote: "SELF -RAG enables an arbitrary LM to generate text with reflection tokens by unifying them as next token predictions from the expanded model vocabulary"

- **strength**: The evaluation covers six tasks and reports competitive results against a range of retrieval and non-retrieval systems; on ASQA, the table shows markedly higher citation metrics for Self-RAG than the listed non-proprietary retrieval baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: Some comparisons are not direct reruns: the paper explicitly reports certain concurrent methods using previously published results, limiting the uniformity of those comparisons.
  - Page 7 · citation: exact
  - Quote: "We report numbers using the results reported in the paper as the implementations are not available."

- **uncertainty**: The inspected pages do not establish how sensitive the gains are to the critic’s judgments, retrieval configuration, or alternative scoring choices; those details may be addressed elsewhere in the paper, which was not inspected.
  - Page 7 · citation: whitespace
  - Quote: "For the retriever model R, we use off-the-shelf Contriever-MS MARCO (Izacard et al., 2022a) by default and retrieve up to ten documents for each input."

Unresolved questions:

- How robust are reflection-token assessments when the critic-generated training labels or model self-assessments are wrong?
- How do retrieval frequency, segment-level search cost, and performance vary under alternative retrievers or decoding settings?
- I inspected pages 1–8 and 13–15; the remaining results/analysis and appendices were not reviewed, so claims about full ablations, efficiency, or broader limitations remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s explicit scope and limitation discussion to balance assessment. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method details and the stated training/inference procedure on the next pages. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 13, "end": 15}` | Inspect experimental results and evaluation details that support the contribution claims. | read pages [13, 14, 15] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "Our experiments"}` | Find the results section to inspect headline quantitative evidence and evaluation scope. | 2 matches on pages [3, 6] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 6, "end": 8}` | Read the experimental results, comparisons, and any reported evaluation caveats. | read pages [6, 7, 8] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Observed method, evaluation design, headline results, and baseline caveats; submit a supported assessment while noting that later analysis and appendix were not inspected. | review accepted | [event 31](trace.jsonl#L31) |
