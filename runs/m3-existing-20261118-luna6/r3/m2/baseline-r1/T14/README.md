# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 6.55 s · $0.000490

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 494 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RULER is a configurable synthetic benchmark intended to reveal long-context capabilities that vanilla needle retrieval can miss. It combines varied retrieval tests with variable tracking, frequency aggregation, and QA, then evaluates long-context models across lengths and task complexities. The reported results show substantial performance degradation beyond simple retrieval and provide useful failure analyses, though the synthetic task suite and evaluation choices constrain how broadly its conclusions transfer.

- **strength**: The benchmark broadens evaluation beyond single-needle lookup and makes sequence length and task complexity adjustable.
  - Page 1 · citation: whitespace
  - Quote: "RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles."

- **strength**: The evaluation includes a sizable, systematic comparison across models and context lengths, with 500 examples per task and length.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length"

- **limitation**: The benchmark is intentionally synthetic; its results therefore do not by themselves establish performance on the full range of naturally occurring long-context use.
  - Page 2 · citation: exact
  - Quote: "RULER consists solely of synthetic tasks"

- **uncertainty**: The effective-length headline depends on a chosen baseline threshold, so it remains uncertain how the conclusions change under other thresholds or real deployment length distributions.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do RULER scores predict performance on diverse real-world long-document tasks, beyond the synthetic and augmented-QA settings tested here?
- How sensitive are effective context lengths and model rankings to alternative thresholds and to empirically measured usage-length distributions?
- The supplied pages describe task templates and report aggregate results, but do not provide full uncertainty estimates or per-task example-level analyses; how stable are the reported differences across random seeds and prompt variants?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
