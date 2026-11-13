# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**baseline · ok**

1 model calls · 0 reads · 5.23 s · $0.003281

1 decisions · 0 tool calls · 23878 input tokens (0 cached) · 592 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

AutoGen presents a general-purpose framework for composing LLM-, human-, and tool-backed agents through a unified conversation interface, automated replies, and configurable conversation patterns. Its main contribution is an implementation-oriented framework and a collection of application demonstrations, rather than a controlled study establishing general benefits of multi-agent workflows. The examples make the design concrete, but the empirical evidence is limited and uneven across applications.

- **strength**: The framework offers a coherent abstraction for implementing varied workflows: agents share a conversation interface, while registered auto-replies connect actions and subsequent interactions. The paper illustrates this with several application patterns.
  - Page 5 · citation: exact
  - Quote: "The auto-reply mechanism provides a decentralized, modular and unified way to define the workflow."

- **strength**: The report includes quantitative results for specific tasks, including a small comparison on MATH problems and a MiniWoB++ evaluation. This provides some empirical support beyond illustrative examples, though it does not establish broad superiority.
  - Page 15 · citation: wrong_page
  - Quote: "For each clicking task, we reported the success rate for ten different instances."

- **limitation**: The autonomous math comparison is narrow: the initial qualitative evaluation uses two problems with three trials each, and the follow-up uses 12 problems with one trial. This supports only a limited comparison, not a reliable general claim about accuracy.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset. With one trial, AutoGen scores 8/12 problems"

- **uncertainty**: The report gives examples of reduced code and interaction burden, but the inspected evidence does not establish whether these improvements generalize across developers, applications, or implementation choices. The paper itself identifies workflow selection as an open problem.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How do the framework’s benefits and costs compare with simpler single-agent or hand-coded workflows across a broader, controlled set of tasks?
- What evaluation methods can distinguish genuine gains from extra inference, tool use, or human feedback in multi-agent applications?
- How can developers reliably select agent roles, conversation patterns, and autonomy levels while controlling cost and preventing cascading failures?
- I inspected the supplied pages, including the applications, discussion, and appendix tables, but did not independently validate the reported experiments or inspect external code and linked materials.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
