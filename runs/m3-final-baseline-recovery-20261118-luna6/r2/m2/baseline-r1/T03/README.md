# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 6.73 s · $0.000494

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 509 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

AutoGen presents a general-purpose framework for building LLM applications as conversations among customizable agents backed by models, tools, or humans. Its main contribution is an extensible interaction design, illustrated through six applications and limited comparative evaluations. The report makes a useful systems contribution, but much of its evidence is illustrative or small-scale, so it provides more support for implementation flexibility than for broad performance or reliability claims.

- **strength**: The framework's unified agent interface and configurable auto-reply mechanism give developers a general way to compose agent interactions, including dynamic workflows.
  - Page 5 · citation: whitespace
  - Quote: "This simple mechanism enables automated agent chat, i.e., the agent conversation can proceed automatically after the conversation is initialized, without any extra control plane needed."

- **strength**: The report demonstrates the framework across several distinct application types, including coding, browser interaction, retrieval, group chat, and chess, making the systems contribution concrete.
  - Page 8 · citation: exact
  - Quote: "We showcase six applications powered by AutoGen"

- **limitation**: The math comparison is narrow: the initial qualitative evaluation uses two problems with three trials each, and the follow-up uses 12 problems with one trial. This limits how broadly those results support comparative performance claims.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial, AutoGen scores 8/12 problems"

- **uncertainty**: The report itself leaves open how to choose an effective and cost-conscious agent design for a given task; it does not establish a general method for selecting workflows.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How do the framework’s performance, cost, and reliability compare across broader, repeated evaluations and varied tasks, beyond the report’s small or illustrative studies?
- What practical methods can help developers select agent roles, conversation patterns, and autonomy levels while controlling failure propagation and safety risks?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
