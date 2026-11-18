# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 8.99 s · $0.000510

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 671 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines instruction fine-tuning of LLaMA-7B with retrieval-aware training to generate calls to documented ML APIs. The paper introduces APIBench and reports strong in-domain API-selection accuracy and reduced hallucinations versus prompted models in several settings. Its results support the approach as a useful benchmark and method, while the evaluation focuses on matching API identifiers and arguments rather than executing calls or validating their end-to-end behavior.

- **strength**: The paper contributes a sizable API benchmark spanning three model hubs and describes how its instruction/API pairs were constructed.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls. 94 from Torch Hub (exhaustive), 626 from TensorFlow Hub v2 (exhaustive) and 925 from HuggingFace"

- **strength**: On the reported zero-shot benchmark, Gorilla substantially exceeds the listed baselines on HuggingFace and TensorFlow Hub, with lower hallucination rates than most comparisons.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The main evaluation identifies calls by AST matching against the dataset, so its accuracy does not establish that generated code executes successfully or behaves correctly.
  - Page 5 · citation: exact
  - Quote: "we adopt the AST tree-matching strategy."

- **limitation**: The paper explicitly leaves execution testing of example code outside its evaluation, limiting evidence for end-to-end API use.
  - Page 13 · citation: whitespace
  - Quote: "we haven’t tested the execution result of the code."

Unresolved questions:

- How well does Gorilla perform when API selection and arguments are evaluated by actually executing calls, including handling dependencies, runtime errors, and outputs?
- How robust are the reported gains to test splits that hold out APIs or documentation, rather than splitting instruction/API pairs for APIs that appear in training?
- How reproducible are the test-time documentation-change and constraint results across broader sets of API changes and constraints? The inspected pages report examples and aggregate scores, but do not establish broad real-world generalization.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
