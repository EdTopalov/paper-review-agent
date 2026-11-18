# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 6.00 s · $0.000551

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 500 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a multi-turn agent framework in which executable Python is the action format, and contributes a 7k-trajectory instruction dataset and fine-tuned open-source agents. Its benchmark comparisons and model evaluations provide useful evidence that code actions can improve complex tool use and reduce interaction turns, while also showing substantial variability across models and tasks.

- **strength**: The central comparison is supported by a newly curated benchmark with 82 tasks and reports higher success rates for CodeAct across most tested LLMs, alongside fewer turns for most models.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The paper contributes a multi-domain interaction dataset and reports large improvements for the Mistral-based agent on out-of-domain agent tasks, as well as gains on several general-task metrics.
  - Page 9 · citation: exact
  - Quote: "CodeActAgent (both variants) performs better on generic LLM tasks we tested"

- **limitation**: The authors acknowledge that the agent is an early prototype and may hallucinate environment state, limiting confidence in autonomous use.
  - Page 10 · citation: exact
  - Quote: "it may suffer from hallucination commonly seen in LLMs"

- **uncertainty**: The benchmark evidence is based on a small, curated task set; the paper does not establish from the inspected material how well the gains transfer to broader or less manually specified real-world tasks.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

Unresolved questions:

- How robust are the CodeAct gains to substantially larger and independently constructed task sets, beyond the curated M3ToolEval benchmark?
- Which features of CodeActInstruct and its training mixture explain the differing M3ToolEval outcomes between the LLaMA-2- and Mistral-based agents?
- What execution safeguards and permission boundaries are needed for deploying agents that can run arbitrary Python code?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
