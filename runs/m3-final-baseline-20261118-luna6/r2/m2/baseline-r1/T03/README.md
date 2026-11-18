# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 7.61 s · $0.000573

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 667 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

AutoGen presents a general framework for building LLM applications from configurable, conversable agents, with support for human participation, tools, automated replies, and static or dynamic conversation patterns. Its main contribution is an accessible design and a diverse set of demonstrations; the report offers some task-level evidence, but much of the case for general effectiveness rests on examples and limited evaluations.

- **strength**: The framework’s unified agent interface and configurable auto-reply mechanism provide a concrete, flexible approach to orchestrating multi-agent workflows. The paper illustrates this design across several application types.
  - Page 5 · citation: whitespace
  - Quote: "This simple mechanism enables automated agent chat, i.e., the agent conversation can proceed automatically after the conversation is initialized, without any extra control plane needed."

- **limitation**: The math comparison is narrow: the qualitative study uses two problems with three trials each, and the follow-up uses 12 problems with one trial. This supports a preliminary comparison, not a broad claim of reliability or superiority.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial, AutoGen scores 8/12 problems"

- **uncertainty**: The NQ results show a high reported recall for Retrieval-augmented Chat, but the paper says its results are on the first 500 questions and compares against systems with different training setups. How robust and directly comparable the advantage is remains unclear.
  - Page 18 · citation: exact
  - Quote: "Retrieval-augmented Chat (ours) + GPT-3.5 0.2 23.73 66.61"

Unresolved questions:

- How do AutoGen workflows compare with simpler single-agent or hand-coded alternatives when evaluated on matched tasks, budgets, and success criteria?
- How do cost, latency, and failure rates change as the number of agents, conversation length, or task complexity grows?
- What safeguards and evaluation methods reliably detect unsafe or incorrect actions in autonomous workflows, beyond the application-specific examples described?
- The assessment here is based on the supplied report; the paper’s linked code and notebooks and any additional evaluation materials were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
