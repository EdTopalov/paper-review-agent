# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 9.03 s · $0.000484

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 618 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

Gorilla combines instruction fine-tuning of a LLaMA-7B model with retrieval-aware training to generate API calls, and introduces APIBench across Torch Hub, TensorFlow Hub, and HuggingFace. Its experiments show strong benchmark accuracy and reduced hallucination in several settings, while also revealing that imperfect retrieval can substantially hurt performance. The work offers a useful benchmark and practical method, but its evaluation focuses on matching API-call structure rather than execution or end-to-end task success.

- **strength**: The benchmark experiments show Gorilla achieves high zero-shot accuracy on the reported test splits, especially for HuggingFace and TensorFlow Hub, while reporting hallucination and wrong-API errors separately.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The main correctness metric identifies calls through selected AST nodes and arguments, so it does not establish that generated calls execute successfully or accomplish the requested task. The paper explicitly leaves execution results untested.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **uncertainty**: The dataset size is reported inconsistently: the main text gives 94 Torch Hub APIs and 626 TensorFlow Hub APIs, whereas the appendix gives 95 and 696. This makes the exact composition behind the reported benchmark results unclear from the supplied paper.
  - Page 2 · citation: whitespace
  - Quote: "We exhaustively include every API call in TorchHub (94 API calls) and TensorHub (696 API calls)"

Unresolved questions:

- How well do Gorilla’s structurally matched API calls execute in practice, and how often do they complete the user’s intended task?
- How much do the reported results depend on the synthetic instruction generation and the particular train/test split of instruction–API pairs?
- What accounts for the differing Torch Hub and TensorFlow Hub API counts reported in the main text and appendix?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
