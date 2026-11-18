# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 6.09 s · $0.000530

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 575 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

RULER is a configurable synthetic benchmark that broadens long-context evaluation beyond single-needle retrieval to include multi-item retrieval, variable tracking, word-frequency aggregation, and QA with distractor documents. Across 10 models and 13 task configurations, its reported results show substantial performance degradation with longer contexts and greater task complexity, exposing a gap between claimed context windows and performance on this benchmark. The work is useful as an evaluation framework and empirical comparison, while its synthetic tasks and chosen scoring conventions limit how directly results transfer to real-world long-context use.

- **strength**: The benchmark explicitly varies both task type and difficulty, addressing the narrow scope of vanilla needle retrieval.
  - Page 1 · citation: whitespace
  - Quote: "RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles."

- **strength**: The evaluation reports broad degradation across its task suite and identifies that near-perfect vanilla NIAH performance does not ensure broader long-context capability.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The benchmark's synthetic inputs enable configuration control but constrain claims about generalization to natural long-context tasks; the paper itself frames QA as a real-world adaptation rather than a fully realistic evaluation.
  - Page 5 · citation: whitespace
  - Quote: "This category is a real-world adaptation (Ivgi et al., 2023) of NIAH"

- **uncertainty**: The headline effective-context threshold is a chosen baseline rather than a validated measure of practical adequacy, so the interpretation of “effective” depends on this convention.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do RULER scores predict performance on realistic long-document tasks, beyond the synthetic and distractor-augmented QA settings presented here?
- Would the model rankings and effective-length conclusions remain stable under different task mixtures, accuracy measures, or thresholds?
- I inspected the provided main text and appendices through page 23; I did not inspect any material beyond this supplied excerpt, so further implementation or evaluation details may be unavailable here.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
