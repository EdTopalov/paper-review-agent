# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 4.50 s · $0.002445

1 decisions · 0 tool calls · 17424 input tokens (0 cached) · 535 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

Gorilla presents an API-call benchmark spanning three machine-learning model hubs and a LLaMA-7B model fine-tuned on synthetic instruction/API pairs, including examples with retrieved documentation. Its experiments show strong zero-shot API matching and reduced hallucination on the evaluated benchmark, and illustrate how retrieval-aware training can support responses to documentation changes. The work is a useful early empirical study, though its conclusions are bounded by synthetic data, a narrow code-generation task, and an AST-based proxy for correctness.

- **strength**: The paper contributes a sizable, structured benchmark and a reproducible task setup for API-call generation across three hubs.
  - Page 4 · citation: whitespace
  - Quote: "For each of our 1,645 API datapoints, we sample 3 of 6 corresponding instruction examples to generate a total of 10 instruction-api pairs"

- **strength**: On the authors’ AST-based metric, Gorilla substantially exceeds the compared models in zero-shot accuracy for HuggingFace and TensorFlow Hub, while reducing hallucinated API calls in those settings.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The evaluation establishes API identification/matching, not that generated code executes successfully or fulfills the user’s task; the appendix explicitly says execution results were not tested for example code.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **uncertainty**: The reported gains may depend on the synthetic instruction-generation process and the particular split of instruction/API pairs; the inspected evaluation does not establish generalization to independently authored user requests or unseen APIs.
  - Page 6 · citation: whitespace
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

Unresolved questions:

- How well does Gorilla perform on independently written user requests, APIs outside the three model hubs, or APIs not represented during fine-tuning?
- Do AST matching scores predict executable, semantically appropriate API use, including valid arguments, dependencies, and runtime behavior?
- How robust are the test-time documentation-change examples across a broader and systematically evaluated set of API changes?
- The inspected pages do not provide confidence intervals or repeated-run variability; how sensitive are the reported results to data splits, training seeds, and baseline prompting choices?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
