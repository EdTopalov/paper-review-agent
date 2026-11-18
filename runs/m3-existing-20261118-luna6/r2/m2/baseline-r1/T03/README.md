# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 8.10 s · $0.000573

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 668 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

AutoGen presents a flexible framework for building LLM applications as conversations among customizable agents backed by models, tools, and people. Its main contribution is an accessible orchestration design illustrated across six applications; the report offers useful implementation examples, but its empirical evidence is limited and uneven, so broad claims about performance and general utility remain preliminary.

- **strength**: The report gives a concrete, reusable abstraction for orchestrating agent interactions, including configurable reply behavior and dynamic conversation patterns.
  - Page 5 · citation: whitespace
  - Quote: "This simple mechanism enables automated agent chat, i.e., the agent conversation can proceed automatically after the conversation is initialized, without any extra control plane needed."

- **strength**: The paper demonstrates the framework in varied settings, including human participation, tool execution, retrieval, and environment interaction, making the design tangible beyond a conceptual proposal.
  - Page 8 · citation: exact
  - Quote: "We showcase six applications powered by AutoGen (depicted in Figure 5)."

- **limitation**: The math comparison is too small to support broad claims of comparative reliability: the initial comparison uses two problems and three trials per problem, while the larger follow-up uses only one trial per sampled problem.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial, AutoGen scores 8/12 problems"

- **uncertainty**: The report itself leaves workflow selection unresolved; it does not establish when multi-agent designs outperform simpler alternatives or how to choose a cost-effective design across tasks.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How much of the observed benefit comes from the framework’s orchestration design versus the chosen models, prompts, tools, and task-specific implementation?
- How do AutoGen workflows compare with well-tuned single-agent or non-conversational baselines across a broader range of tasks, repetitions, and cost or latency measures?
- What practical safeguards and oversight mechanisms are sufficient when autonomous agents can execute code or affect external environments?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
