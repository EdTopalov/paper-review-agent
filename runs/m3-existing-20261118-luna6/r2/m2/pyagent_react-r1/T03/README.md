# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**pyagent_react · ok**

5 model calls · 4 reads · 14.88 s · $0.001640

5 decisions · 5 tool calls · 30737 input tokens (22666 cached) · 810 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

AutoGen presents a practical, extensible framework for composing LLM-, human-, and tool-backed agents through a common conversational interface. Its strongest contribution is the unification of customizable agents and interaction patterns, illustrated across diverse applications. The report includes a small comparative math evaluation, but that evidence is narrow relative to its broad claims; the authors also identify workflow design, scaling, and safety as open problems.

- **strength**: The framework's central design combines configurable agent capabilities with a common interface for interaction, supporting varied multi-agent workflows.
  - Page 2 · citation: exact
  - Quote: "Customizable agents that integrate LLMs, humans, and tools."

- **strength**: The math comparison provides concrete, though limited, evidence: in the reported 12-problem sample, AutoGen scored 8/12 versus 7/12 for each of two commercial systems.
  - Page 11 · citation: whitespace
  - Quote: "With one trial, AutoGen scores 8/12 problems, and both ChatGPT+Plugin and ChatGPT+Code Interpreter score 7/12 problems."

- **limitation**: The comparative math evidence is narrow: it reports a single trial on 12 sampled problems, so it does not establish broad or statistically robust performance advantages.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset."

- **uncertainty**: How to choose effective and cost-efficient multi-agent workflows remains an explicit open question, not a demonstrated defect of the framework.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How well do the framework's benefits generalize across tasks, models, and operating conditions beyond the presented examples and small math comparison?
- What systematic methods can select agent roles, interaction patterns, and autonomy levels while controlling cost and failure risks?
- I inspected the introduction and framework pages, selected math evaluation pages, and concluding discussion; I did not inspect all application examples, implementation details, or evaluation material, so this assessment may miss relevant evidence in those sections.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the framework design and examples of supported agent conversation patterns. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 10, "end": 12}` | Inspect application evidence and any reported evaluation or scope limitations. | read pages [10, 11, 12] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the report explicitly states scope boundaries or limitations. | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 23, "end": 24}` | Inspect the paper's stated risks and concluding scope considerations. | read pages [23, 24] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.65, "observations": 4}}` | Submit a balanced assessment grounded in the framework description, limited math evaluation, and stated future work. | review accepted | [event 26](trace.jsonl#L26) |
