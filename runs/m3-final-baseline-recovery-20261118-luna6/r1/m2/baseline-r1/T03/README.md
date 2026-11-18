# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 10.85 s · $0.000609

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 739 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

AutoGen presents a general framework for building LLM applications as conversations among customizable agents backed by models, tools, and humans. Its unified messaging and auto-reply design is illustrated across six applications, with limited quantitative evaluations in math problem solving, browser tasks, and retrieval-augmented QA. The report makes a useful systems contribution and offers concrete implementation patterns, but the evidence is uneven: many applications are demonstrations, and the quantitative evaluations cover narrow settings.

- **strength**: The framework’s central contribution is a unified conversation interface that supports configurable agents and automated interaction patterns; the report gives concrete examples of how these elements compose into workflows.
  - Page 5 · citation: whitespace
  - Quote: "a workflow can be represented as a sequence of inter-agent message passing and agent acting"

- **limitation**: The math comparison is small: the initial evaluation uses two problems with three trials each, and the follow-up uses 12 problems with one trial. These results support a preliminary comparison, not a robust estimate of comparative performance.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial"

- **uncertainty**: The retrieval-augmented QA results are reported on only the first 500 questions, while several comparison metrics are copied from another paper. It remains unclear how sensitive the result is to evaluation-set selection and differences in systems or evaluation conditions.
  - Page 17 · citation: exact
  - Quote: "Results on the first 500 questions with GPT-3.5-turbo are shown in Table 3."

- **limitation**: The report explicitly identifies unresolved challenges in selecting effective workflows and ensuring safe operation as systems become more complex. Most application examples are demonstrations, so the supplied evidence does not establish broad effectiveness or safety across settings.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How do AutoGen workflows compare with simpler, single-agent or non-conversational alternatives when evaluated on matched tasks, budgets, and execution conditions?
- How do performance, cost, reliability, and error propagation change as the number of agents and interaction rounds increase?
- What safeguards and human-oversight practices reliably prevent unsafe actions in applications that execute code or affect external environments?
- How reproducible are the reported results across broader task samples, model configurations, and independent evaluations?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
