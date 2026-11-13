# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

3 model calls · 2 reads · 13.11 s · $0.001853

3 decisions · 3 tool calls · 14887 input tokens (3112 cached) · 700 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

Gorilla studies LLM generation of machine-learning API calls, combining instruction fine-tuning with optional retrieval over API documentation. The paper contributes APIBench and an AST-based evaluation, and reports strong zero-shot results for its fine-tuned model plus gains from oracle-retrieval training. Evidence supports useful progress in this bounded setting, but the benchmark’s construction and evaluation differences limit broad conclusions.

- **strength**: The benchmark combines API collections from three hubs with generated instruction/API examples, and evaluates calls structurally rather than relying only on textual similarity.
  - Page 2 · citation: whitespace
  - Quote: "We also generate 10 synthetic user question prompts per API using Self-Instruct [42]."

- **strength**: Reported zero-shot Gorilla accuracy is strong in the shown benchmark results, including higher overall accuracy than the listed baselines across the three hubs.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The HuggingFace comparison uses a different correctness criterion for non-Gorilla models, complicating direct cross-model comparison on that portion of the benchmark.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names."

- **uncertainty**: Retrieval results vary substantially by retriever; the tables show drops with BM25 or GPT-Index relative to oracle retrieval, leaving practical performance dependent on retrieval quality.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

Unresolved questions:

- How well do the findings transfer to real user requests and API collections beyond these ML hubs and synthetically generated prompts?
- How would conclusions change under a common, equally detailed correctness metric for all models, especially on HuggingFace?
- I inspected pages 2–4 and 6–8 only; results and limitations elsewhere in the paper, including later experiments and appendices, remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the method, dataset construction, and evaluation setup. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect benchmark results and evaluation caveats. | read pages [6, 7, 8] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.65, "observations": 4}}` | Submit an evidence-based assessment using inspected method and results pages, while noting limits of the selective reading. | review accepted | [event 17](trace.jsonl#L17) |
