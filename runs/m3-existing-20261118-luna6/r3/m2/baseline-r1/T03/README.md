# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 6.45 s · $0.000501

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 524 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

AutoGen presents a general-purpose framework for building LLM applications as conversations among customizable agents backed by models, tools, and people. Its main contribution is an accessible orchestration abstraction, illustrated through six varied applications; the report provides some task-level evaluations, but much of the evidence for general utility is illustrative or based on small, application-specific demonstrations.

- **strength**: The framework unifies agent interaction around message exchange and configurable reply behavior, offering a concrete programming abstraction for multi-agent workflows.
  - Page 5 · citation: whitespace
  - Quote: "a workflow can be represented as a sequence of inter-agent message passing and agent acting"

- **strength**: The report demonstrates breadth across coding, web interaction, retrieval, group chat, and chess, rather than focusing on only one use case.
  - Page 8 · citation: exact
  - Quote: "We showcase six applications powered by AutoGen"

- **limitation**: The math comparison is limited in scale: the main autonomous quantitative follow-up uses 12 sampled problems and one trial, so it supports a preliminary comparison rather than a broad performance claim.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial"

- **uncertainty**: The NQ result is reported on only the first 500 questions, while comparison metrics are copied from another paper; the report does not establish how robust the result is across the full dataset or under matched evaluation conditions.
  - Page 17 · citation: exact
  - Quote: "Results on the first 500 questions with GPT-3.5-turbo are shown in Table 3."

Unresolved questions:

- How do AutoGen workflows compare with simpler single-agent or scripted alternatives when evaluated on matched tasks, budgets, and model configurations?
- How reproducible are the reported application results across different prompts, model versions, task samples, and repeated trials?
- What are the operational costs and reliability tradeoffs of multi-agent conversation as workflow scale and complexity increase?
- Inspection was limited to the supplied pages; the report’s code and notebooks, and any material beyond the supplied excerpt, were not independently examined.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
