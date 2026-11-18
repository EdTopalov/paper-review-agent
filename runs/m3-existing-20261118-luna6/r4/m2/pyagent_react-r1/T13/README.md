# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

6 model calls · 5 reads · 15.42 s · $0.002923

6 decisions · 6 tool calls · 34890 input tokens (16705 cached) · 967 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to retrieve on demand and generate segment-level self-critiques, using reflection tokens to guide evidence-aware generation and inference-time customization. The paper presents comparisons across six tasks, ablations, and analyses of retrieval and citation trade-offs. The approach is substantial and its evidence is promising, though some human evaluation is small and the inspected evidence does not establish how well results generalize beyond the tested settings.

- **strength**: The system combines adaptive retrieval with segment-level critique and controllable selection, rather than always prepending a fixed set of passages.
  - Page 2 · citation: whitespace
  - Quote: "SELF -RAG learns to retrieve, critique, and generate text passages to enhance overall generation quality, factuality, and verifiability."

- **strength**: The reported table shows gains on several tasks and particularly strong citation precision and recall versus the listed non-proprietary retrieval baselines; performance is not uniformly best on every metric or against every proprietary system.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: The human assessment is explicitly small, so it offers limited evidence about reflection-token reliability and answer support across broader populations or tasks.
  - Page 10 · citation: whitespace
  - Quote: "We conduct small human evaluations on SELF -RAG outputs, as well as the reliability of predicted reflection tokens."

- **uncertainty**: The main experiments use specified datasets and retrieval configurations; how robust the approach is under other retrieval systems or substantially different deployment conditions remains unanswered in the pages inspected.
  - Page 7 · citation: whitespace
  - Quote: "For PopQA, we use the long-tail subset, consisting of 1,399 rare entity queries whose monthly Wikipedia page views are less than 100."

Unresolved questions:

- How sensitive are the reported results to retriever quality, corpus changes, and retrieval failures beyond the configurations tested?
- How reliable are reflection-token judgments and citation support at scale, beyond the small human evaluation described?
- How do training and inference costs compare in practice, including the added retrieval and segment-level candidate processing?
- I inspected pages 1–3 and 6–10, but not the remaining main text or appendices; detailed training, annotation, and evaluation protocols may address some of these questions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and limitations. | 0 matches | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the proposed training and inference procedure. | read pages [2, 3] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "Open-domain QA"}` | Locate reported benchmark results for the main performance claims. | 6 matches on pages [1, 7, 20, 23] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 8}` | Inspect evaluation design, quantitative comparisons, and stated caveats. | read pages [6, 7, 8] | [event 21](trace.jsonl#L21) |
| 5 | read_pages `{"start": 9, "end": 10}` | Inspect further result interpretation and analysis of trade-offs. | read pages [9, 10] | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit evidence-based assessment from inspected pages 1–3 and 6–10; note the uninspected appendices and remaining uncertainty. | review accepted | [event 32](trace.jsonl#L32) |
