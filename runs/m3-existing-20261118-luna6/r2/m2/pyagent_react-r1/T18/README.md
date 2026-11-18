# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

4 model calls · 3 reads · 14.04 s · $0.001819

4 decisions · 4 tool calls · 27134 input tokens (17157 cached) · 801 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines instruction fine-tuning of a LLaMA-7B model with retrieval-aware training to produce API calls, and introduces APIBench from three machine-learning model hubs. Its comparative evaluations show strong performance on this benchmark, including reduced hallucination in several settings, while also exposing how much performance depends on retrieval quality. The work is useful and technically clear, but its evidence is tied to synthetic instructions, a bounded API domain, and an AST-based correctness measure.

- **strength**: APIBench provides a substantial, explicitly described collection of APIs and generated instruction–API pairs, making API-call evaluation more systematic within the chosen domain.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls. 94 from Torch Hub (exhaustive), 626 from TensorFlow Hub v2 (exhaustive) and 925 from HuggingFace"

- **strength**: The results support strong benchmark performance, while the numbers also show that Gorilla’s advantage varies across datasets and retrieval settings rather than being universal.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The evaluation equates a match to a recorded API subtree with functional correctness; the authors acknowledge that this approach does not establish semantic equivalence across valid alternatives.
  - Page 5 · citation: whitespace
  - Quote: "we compare their functional equivalence using the dataset we collected."

- **limitation**: The main benchmark evidence is restricted to ML model hubs, so the broader claim of applicability to APIs in other domains remains untested in the inspected evaluation.
  - Page 9 · citation: whitespace
  - Quote: "With the goal of wanting to have a challenging dataset, we chose ML APIs, given their functional similarity."

Unresolved questions:

- How well do the findings transfer to naturally occurring user requests, rather than the synthetic instruction–API pairs used to construct and split the benchmark?
- Do the adaptation demonstrations for changed documentation generalize beyond the illustrative examples to quantitative evaluation across diverse API changes?
- How would results change under semantic or execution-based correctness checks that recognize functionally valid calls not represented by the recorded subtree?
- I inspected pages 1–10 only; later appendix material, including any further details on data splits, training, or evaluation, was not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the method, benchmark construction, and evaluation setup. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect retrieval design and quantitative evaluation results. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Check claims about documentation updates, constraints, and further evaluation. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit a balanced assessment grounded in the inspected method, results, and stated scope. | review accepted | [event 21](trace.jsonl#L21) |
