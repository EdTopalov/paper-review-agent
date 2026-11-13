# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 6.02 s · $0.004023

1 decisions · 0 tool calls · 30099 input tokens (0 cached) · 521 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a general-purpose agent action interface in which an LLM emits executable Python and receives execution results as observations, and introduces a 7k-trajectory instruction dataset plus fine-tuned open models. Its controlled format comparisons and agent evaluations provide evidence that code actions can improve success and reduce interaction turns, particularly on tasks requiring composed tool use. The results are promising but uneven across models, and the complex-task benchmark is small and human-curated. Assessment is based on the supplied pages (1–29); I did not inspect the referenced supplementary sections beyond the excerpts included here.

- **strength**: The paper makes the action-format comparison concrete across 17 models and reports a substantial CodeAct advantage on its complex-task benchmark, while also measuring interaction cost.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The work extends the interface proposal with an open-model training artifact and reports gains on agent tasks, including out-of-domain settings; the ablation table also helps distinguish dataset contributions.
  - Page 8 · citation: not_found
  - Quote: "CodeActInstruct consists of 7,139 instances"

- **limitation**: The main newly curated benchmark has only 82 instances, and the paper itself reports a large gap between open- and closed-source model performance, limiting the strength and breadth of generalization claims.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The reported agent results vary substantially by backbone: the authors explicitly find no M3ToolEval improvement for the LLaMA-2 variant, while Mistral improves. What causes this difference is unresolved in the inspected results.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

Unresolved questions:

- How robust are the M3ToolEval gains to a larger, independently constructed benchmark and to variation in task composition or tool definitions?
- How sensitive are results to model prompting, interaction limits, and benchmark-specific formatting or exact-match evaluation?
- Can the authors isolate why the LLaMA-2 and Mistral fine-tuned variants differ, and how well do the reported gains transfer to other backbones and real environments?
- What safeguards and execution restrictions are required for dependable deployment when generated code can access packages and external resources?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
