# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 6.96 s · $0.000517

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 556 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

AutoGen presents a flexible, conversation-centered framework for composing LLMs, tools, and people into multi-agent workflows, illustrated through six applications. Its main contribution is an accessible systems design and implementation pattern, rather than a general empirical demonstration that multi-agent workflows outperform alternatives. The report provides useful examples and some task-specific evaluations, but the evidence is uneven and often small-scale.

- **strength**: The unified conversational interface and registered auto-reply mechanism offer a concrete, reusable orchestration design, illustrated with both static and dynamic workflows.
  - Page 5 · citation: whitespace
  - Quote: "Once an agent receives a message from another agent, it automatically invokes generate reply and sends the reply back to the sender unless it is empty"

- **strength**: The report goes beyond a framework proposal by demonstrating applications across several domains and reporting benchmark or comparative results in some cases.
  - Page 15 · citation: wrong_page
  - Quote: "For each clicking task, we reported the success rate for ten different instances."

- **limitation**: The math comparison is narrow: the initial qualitative evaluation uses only two problems with three trials each, and the follow-up uses a single trial per sampled problem, limiting the strength of broad comparative claims.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial, AutoGen scores 8/12 problems"

- **uncertainty**: The report does not establish how much gains in the showcased applications come from the framework’s orchestration design versus the underlying models, prompts, tools, or application-specific engineering. The authors themselves identify workflow design as open work.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How robust are the reported results across larger and more diverse task sets, repeated trials, and changes in model or tool configuration?
- What are the cost, latency, and reliability trade-offs of adding agents and conversation rounds compared with simpler workflows?
- How can safety, monitoring, and human oversight be evaluated systematically as workflows become more autonomous or complex?
- Inspection was limited to the supplied pages and reported examples; several application claims are illustrative or implementation-focused rather than supported by controlled comparative evaluation.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
