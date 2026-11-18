# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

6 model calls · 3 reads · 16.25 s · $0.002677

6 decisions · 6 tool calls · 53008 input tokens (40865 cached) · 1538 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when retrieval is useful, assess retrieved passages and generated segments with reflection tokens, and steer decoding toward supported outputs. Results across six tasks and component ablations support a substantial contribution in adaptive retrieval and controllable generation, with conclusions bounded by selected tasks, proxy-critic training, and retrieval setup.

- **strength**: The framework is explicitly designed to permit inference-time behavior adjustment.
  - Page 2 · citation: exact
  - Quote: "SELF -RAG further enables a customizable decoding algorithm"

- **strength**: Reported comparisons are broad and generally favorable, including retrieval baselines and proprietary models; ablations support the importance of components on selected datasets.
  - Page 8 · citation: whitespace
  - Quote: "SELF -RAG also outperforms existing RAG in many tasks, obtaining the best performance among non-proprietary LM-based models on all tasks."

- **limitation**: The authors identify the off-the-shelf retriever's limited fit for open-ended generation, bounding conclusions about retrieval quality.
  - Page 20 · citation: whitespace
  - Quote: "we observe limited effectiveness of such off-the-shelf retrieval models trained primarily on knowledge-intensive tasks for open-ended generation"

- **uncertainty**: The inspected human evaluation sampled only 50 outputs from two task settings, so generalization remains unclear.
  - Page 10 · citation: whitespace
  - Quote: "In particular, we sampled 50 samples from PopQA and Bio results."

Unresolved questions:

- How robust are gains with retrieval corpora, retrievers, and domains beyond the evaluated Wikipedia-centered setups?
- How well do critic-derived reflection labels align with independent human judgments across more tasks?
- What are the end-to-end latency and compute tradeoffs versus conventional RAG?
- I inspected the opening method pages, results and analysis, and selected appendix details; I did not inspect every experimental table, task protocol, or appendix section.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 1, "end": 3}` | Inspect the paper's framing and method details on the opening pages. | read pages [1, 2, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect experimental setup and quantitative results for support strength. | read pages [8, 9, 10] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 18, "end": 20}` | Check stated limitations and discussion for scope boundaries and unresolved issues. | read pages [18, 19, 20] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers the core framework, broad benchmark results, ablations, and a stated retrieval limitation; submit a balanced review while noting uninspected sections. | citation_validation_failed; #1: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the citation that failed exact quote validation, using a verbatim sentence from the observed page 2 excerpt. | citation_validation_failed; #1: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Replace the failed citation with a shorter exact statement copied from the observed page 2 text. | review accepted | [event 30](trace.jsonl#L30) |
