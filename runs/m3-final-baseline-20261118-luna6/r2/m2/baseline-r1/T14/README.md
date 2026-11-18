# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 6.37 s · $0.000486

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 486 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

RULER is a configurable synthetic benchmark intended to measure long-context language-model behavior beyond simple needle retrieval. It combines varied retrieval tests with variable tracking, word-frequency aggregation, and distractor-augmented question answering, then evaluates a range of models across context lengths. Results show substantial degradation on the broader task suite despite strong vanilla NIAH scores, exposing a gap between claimed context windows and performance on these tasks.

- **strength**: The benchmark broadens evaluation beyond single-item retrieval and allows task difficulty and context length to be varied; the paper also reports a preliminary task-correlation study to guide selection of its 13 configurations.
  - Page 3 · citation: not_found
  - Quote: "RULER contains four task categories to test behaviors beyond simple retrieval from context:"

- **strength**: The main evaluation is sizeable for this synthetic benchmark: it covers ten models, 13 tasks, six context lengths, and 500 examples per task and length. The results document large performance drops on the aggregate suite even where vanilla retrieval is near-perfect.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length"

- **limitation**: The headline effective-length comparison depends on a particular baseline and threshold, so those reported lengths are operational definitions, not a universal boundary on model capability.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

- **limitation**: The benchmark’s synthetic tasks improve control and reduce parametric-knowledge dependence, but their proxies—especially word counting and variable binding—do not by themselves establish equivalent performance on natural long-document understanding.
  - Page 5 · citation: exact
  - Quote: "we introduce a new category as a proxy for summarization tasks"

Unresolved questions:

- How well do RULER scores predict performance on realistic long-context tasks, especially since most categories are synthetic and the QA component is constructed from existing short-context datasets?
- How sensitive are rankings and effective-length conclusions to the chosen baseline threshold, task mix, scoring procedure, and prompt templates?
- The inspected pages report broad results and selected failure analyses, but do not include full per-task results for every model in the main text; how much do aggregate scores conceal divergent task-specific strengths?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
