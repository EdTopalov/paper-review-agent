# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 6.67 s · $0.003294

1 decisions · 0 tool calls · 23878 input tokens (0 cached) · 619 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

AutoGen presents a flexible framework for building LLM applications as conversations among customizable agents backed by models, tools, and humans. Its main contribution is an accessible orchestration design, illustrated across six applications; the evidence is promising but mostly application-specific and limited in scale.

- **strength**: The framework’s unified conversational interface and configurable auto-reply behavior offer a practical way to compose workflows with different agent roles and human or tool participation.
  - Page 5 · citation: whitespace
  - Quote: "This design also aligns well with the capabilities of chat-optimized LLM like GPT-4."

- **limitation**: The math comparison includes only 12 sampled problems and one trial per problem, so it supports a preliminary comparison rather than a robust estimate of relative performance.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial, AutoGen scores 8/12 problems"

- **uncertainty**: The reported retrieval advantage is difficult to interpret as a controlled comparison because the table combines systems using different models, and the paper says some metrics come from another paper.
  - Page 17 · citation: exact
  - Quote: "The metrics of other solutions are directly copied from the reference paper [2]."

Unresolved questions:

- How do AutoGen workflows compare with simpler single-agent or fixed-pipeline baselines when task, model, tools, and evaluation conditions are held constant?
- What are the cost, latency, and reliability tradeoffs of adding agents or allowing dynamic conversations across repeated and larger-scale evaluations?
- How effective are the proposed human-oversight and safety mechanisms when agents execute code or interact with external environments?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
