# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 9.49 s · $0.003295

1 decisions · 0 tool calls · 24226 input tokens (0 cached) · 533 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

RULER is a configurable synthetic benchmark intended to test long-context language models beyond simple needle retrieval. It adds multi-needle retrieval, variable tracking, frequency aggregation, and context-augmented question answering, then evaluates ten models across multiple lengths and task settings. The reported results show substantial degradation on the broader task suite despite strong performance on vanilla NIAH, making the benchmark a useful contribution for exposing differences between nominal context windows and performance on selected long-context behaviors.

- **strength**: The benchmark broadens evaluation beyond single-item retrieval and makes task complexity and context length configurable.
  - Page 1 · citation: whitespace
  - Quote: "RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles."

- **strength**: The authors support the central motivation with a broad evaluation and report a marked gap between vanilla retrieval and the full suite.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The paper explicitly positions the benchmark as synthetic and proxy-based; its results therefore do not by themselves establish performance on natural long-context use cases.
  - Page 2 · citation: whitespace
  - Quote: "RULER consists solely of synthetic tasks, which offer the flexibility to control sequence length and task complexity."

- **uncertainty**: The effective-length conclusions depend on a particular baseline threshold, described as qualitative; how robust the rankings and length labels are to alternative thresholds is not established in the inspected pages.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do the synthetic task results predict performance on realistic long-document tasks, conversations, or other deployment settings?
- How sensitive are effective context lengths and aggregate rankings to the selected baseline threshold and weighting schemes?
- The inspected pages describe evaluation setup and results, but do not provide uncertainty intervals for the reported aggregate accuracies; how much variation arises across samples or repeated runs?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
