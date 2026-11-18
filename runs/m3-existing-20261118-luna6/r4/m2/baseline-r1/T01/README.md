# T01: ReAct: Synergizing Reasoning and Acting in Language Models

**baseline · ok**

1 model calls · 0 reads · 8.47 s · $0.000672

1 decisions · 0 tool calls · 30789 input tokens (30786 cached) · 727 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

ReAct interleaves language-model reasoning with environment-directed actions and observations, using a small number of human-written in-context trajectories. Across knowledge-intensive reasoning and interactive decision-making benchmarks, the paper reports gains over action-only prompting and, in some settings, competitive or improved performance against reasoning-only and trained-agent baselines. Its strongest contribution is the unified prompting paradigm and empirical demonstration across varied tasks; the results also expose concrete failure modes and scope limits.

- **strength**: The paper evaluates the approach across four distinct benchmarks and reports substantial interactive-task gains over trained baselines, while also comparing against reasoning-only and action-only prompts.
  - Page 3 · citation: whitespace
  - Quote: "On ALFWorld and WebShop, two or even one-shot ReAct prompting is able to outperform imitation or reinforcement learning methods"

- **strength**: The analysis usefully distinguishes ReAct's grounding advantage from its reasoning and retrieval failures, rather than presenting aggregate scores alone.
  - Page 6 · citation: normalized
  - Quote: "Non-informative search results, which counts for 23% of the error cases, derail the model thinking trajectory"

- **limitation**: The authors acknowledge that the prompting setup can be constrained by context length and the need for demonstrations; this bounds claims about scaling to more complex tasks.
  - Page 10 · citation: whitespace
  - Quote: "complex tasks with large action spaces require more demonstrations to learn well, which unfortunately can easily go beyond the input length limit of in-context learning."

- **uncertainty**: The evidence supports promise rather than a broad claim of dependable real-world utility: the paper identifies a gap to human performance on WebShop and leaves more systematic evaluation of human-in-the-loop correction for future work.
  - Page 8 · citation: whitespace
  - Quote: "existing methods are still far from the performance of expert humans"

Unresolved questions:

- How robust are the reported gains to different prompt authors, demonstration sets, and model families? The paper reports prompt variation for ALFWorld, but the supplied results do not establish broad robustness across models.
- How would ReAct compare with stronger retrieval systems or more capable learned agents, beyond the deliberately simple Wikipedia API and the baselines used here?
- Does the improved interpretability of reasoning traces reliably help human users detect and correct errors? The paper presents a correction example, while describing systematic study as future work.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
