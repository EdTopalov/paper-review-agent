# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**agent · ok**

6 model calls · 5 reads · 11.74 s · $0.002383

6 decisions · 6 tool calls · 30065 input tokens (14588 cached) · 643 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AutoGen presents a flexible multi-agent conversation framework that unifies configurable LLM, tool, and human agents behind a common interaction model, illustrated across several application domains. The framework and examples are useful systems contributions, but the empirical evidence is narrow and does not establish broad performance gains or optimal workflow design.

- **strength**: The paper articulates a coherent framework contribution: customizable agents, a unified conversational interface, and configurable patterns for complex workflows.
  - Page 2 · citation: exact
  - Quote: "F2 Conversable agents with unified conversation interface."

- **strength**: The framework is demonstrated in diverse example applications and includes a small comparative math evaluation, making the report more than a design proposal.
  - Page 11 · citation: whitespace
  - Quote: "With one trial, AutoGen scores 8/12 problems, and both ChatGPT+Plugin and ChatGPT+Code Interpreter score 7/12 problems."

- **limitation**: The comparative math evidence is explicitly small: the initial experiments use only two problems, and the follow-up has one trial per sampled problem, limiting the strength of general performance conclusions.
  - Page 10 · citation: whitespace
  - Quote: "We use two level-5 problems from the MATH dataset for the qualitative evaluation and test on each problem for 3 times."

- **uncertainty**: The authors identify workflow selection and scaling/safety as open challenges; the inspected evidence does not resolve these questions, rather than demonstrating that the framework fails on them.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How well do the example workflows generalize across tasks, models, and operating costs beyond the small math comparison?
- What systematic guidance or evaluation can identify effective multi-agent workflows and appropriate levels of human oversight?
- This assessment inspected pages 1–3, 8–11, and 23–24, not the full report; further application details and evidence may qualify these conclusions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper’s stated scope and limitations for a balanced assessment. | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Read framework design and contribution details to evaluate technical substance. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 23, "end": 24}` | Inspect discussion of risks and stated limitations, plus its evidence for caveats. | read pages [23, 24] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect application examples and evaluation approach to gauge evidence supporting framework claims. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 11}` | Review quantitative task results and methods to assess strength and boundaries of empirical support. | read pages [10, 11] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | The inspected design, evaluation, and discussion pages support a balanced framework-paper assessment; cite only observed text. | review accepted | [event 31](trace.jsonl#L31) |
