# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 5.56 s · $0.000533

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 463 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a general agent action interface in which an LLM emits executable Python and receives execution results as observations across turns. It evaluates action formats on atomic API calls and a new multi-tool benchmark, then introduces a 7k-trajectory tuning dataset and CodeActAgent models. The evidence is promising, especially for complex tool-use tasks, but the benchmark is small and some agent results are mixed.

- **strength**: The central design combines composable code actions with iterative feedback, and the paper evaluates both action-format choice and trained agents across several tasks.
  - Page 4 · citation: whitespace
  - Quote: "CodeAct employs Python code to consolidate all actions for agent-environment interaction."

- **strength**: On the authors’ 82-instance M3ToolEval benchmark, CodeAct has the highest success rate for 12 of 17 evaluated models, with fewer average turns for 12 of 17.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **limitation**: M3ToolEval is a compact, human-curated evaluation, so the reported gains leave open how well they transfer to broader task distributions.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The trained-agent results are not uniformly positive: the LLaMA-2 variant shows no M3ToolEval improvement, and the paper offers possible explanations rather than resolving the cause.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

Unresolved questions:

- How robust are the action-format comparisons to different benchmark construction choices, tool sets, and larger or independently curated task suites?
- Which factors explain the divergent M3ToolEval outcomes between the LLaMA-2- and Mistral-based CodeActAgent models?
- What execution restrictions and safety evaluations are needed for CodeAct beyond the paper’s stated sandbox concern?
- Assessment is based on the supplied pages; the full experimental appendices and implementation details were not inspected beyond the included excerpts.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
