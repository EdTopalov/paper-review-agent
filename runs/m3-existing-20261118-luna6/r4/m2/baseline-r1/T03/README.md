# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 8.04 s · $0.000491

1 decisions · 0 tool calls · 23878 input tokens (23875 cached) · 504 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

AutoGen presents a flexible, conversation-centric framework for composing LLMs, tools, and humans into multi-agent workflows, illustrated through six applications. Its contribution is chiefly an implementation framework and practical design pattern, supported by concrete examples and a few task-specific evaluations rather than a systematic study of when multi-agent designs improve outcomes.

- **strength**: The unified agent interface and configurable auto-reply mechanism provide a clear implementation approach for orchestrating varied workflows.
  - Page 5 · citation: whitespace
  - Quote: "Once an agent receives a message from another agent, it automatically invokes generate reply and sends the reply back to the sender unless it is empty"

- **strength**: The paper includes an empirical comparison for math problem solving, with a larger sample than its initial qualitative trials, though still limited in scale.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial, AutoGen scores 8/12 problems"

- **limitation**: The NQ comparison uses only the first 500 questions and compares against metrics copied from another paper, limiting the strength of the claim that this system outperforms alternatives.
  - Page 17 · citation: whitespace
  - Quote: "Results on the first 500 questions with GPT-3.5-turbo are shown in Table 3. The metrics of other solutions are directly copied from the reference paper"

- **uncertainty**: The report explicitly leaves open how to choose an effective and cost-efficient multi-agent workflow; its demonstrations do not establish general selection rules.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- Across application types, when do additional agents improve task outcomes enough to justify their extra inference, coordination, and maintenance costs?
- How robust are the reported application results to different models, prompts, task distributions, and repeated trials?
- What safeguards and oversight mechanisms reliably prevent unsafe actions or cascading failures in autonomous workflows?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
