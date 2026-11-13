# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 6.04 s · $0.002375

1 decisions · 0 tool calls · 16657 input tokens (0 cached) · 585 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

WebArena contributes a self-hosted, interactive web environment and an 812-task benchmark for evaluating agents on multi-step, realistic web tasks. Its functional-outcome evaluation and reproducible setup make it a useful research platform, while baseline results and failure analysis illustrate the difficulty of the tasks. The evidence supports the benchmark’s utility, though the paper’s agent comparisons are limited and some evaluation and reporting details leave questions about how reliably scores reflect task success.

- **strength**: The environment combines functional websites, multiple observation modes, and task checks based on outcomes rather than requiring a particular action sequence. This supports more realistic and flexible agent evaluation.
  - Page 4 · citation: whitespace
  - Quote: "The accessibility tree is a subset of the DOM tree with elements that are relevant and useful for displaying the contents of a web page."

- **limitation**: Some information-seeking outcomes rely on an LLM-based fuzzy judge, so evaluation may depend on the judge’s reliability. The paper describes the method but does not report a validation of its judgments in the inspected pages.
  - Page 7 · citation: not_found
  - Quote: "we utilize a language model to assess whether ˆa accurately captures the key concepts presented in a∗."

- **uncertainty**: The reported GPT-4 success rate is inconsistent between the results table and accompanying prose, making the precise headline result unclear.
  - Page 9 · citation: whitespace
  - Quote: "The reasoning agent powered by GPT-4 achieves a relatively modest end-to-end task success rate of 10.63%."

Unresolved questions:

- Which GPT-4 success rate is correct: the 10.59% in Table 3 or the 10.63% in the results prose?
- How well do the LLM-based fuzzy-match judgments agree with human judgments across the benchmark?
- How representative are the tasks and website interactions beyond the authors’ browser-history analysis and the sampled sites described in the paper?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
