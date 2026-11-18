# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 6.92 s · $0.000515

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 552 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

AutoGen presents a general-purpose framework for building LLM applications as conversations among customizable agents backed by models, tools, and humans. Its main contribution is an expressive orchestration design, illustrated across six applications, with limited quantitative evaluations that suggest usefulness but do not establish broad performance gains.

- **strength**: The framework’s central design unifies agent capabilities and interaction patterns rather than targeting one task-specific workflow.
  - Page 2 · citation: exact
  - Quote: "Customizable agents that integrate LLMs, humans, and tools."

- **strength**: The paper includes concrete evidence beyond system descriptions, including a small comparison on math problems; the results are promising but narrow.
  - Page 11 · citation: whitespace
  - Quote: "With one trial, AutoGen scores 8/12 problems, and both ChatGPT+Plugin and ChatGPT+Code Interpreter score 7/12 problems."

- **limitation**: The NQ evaluation does not support the broad claim of outperforming other solutions across metrics: AutoGen has higher reported recall, but much lower exact match than several comparison systems. The comparison also draws metrics from a cited paper.
  - Page 18 · citation: exact
  - Quote: "Retrieval-augmented Chat (ours) + GPT-3.5 0.2 23.73 66.61"

Unresolved questions:

- How robust are the reported benefits across larger, repeated evaluations, different base models, and tasks beyond the selected demonstrations?
- What are the costs and failure rates of multi-agent workflows relative to simpler baselines, especially as conversations grow longer or involve more agents?
- The paper identifies safety and oversight as future concerns; what concrete safeguards and evaluations are needed to bound risks from autonomous code execution and agent interactions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
