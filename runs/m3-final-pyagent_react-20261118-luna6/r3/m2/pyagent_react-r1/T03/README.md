# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**pyagent_react · ok**

5 model calls · 4 reads · 11.61 s · $0.001807

5 decisions · 5 tool calls · 34023 input tokens (24372 cached) · 715 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

AutoGen presents a configurable multi-agent conversation framework that gives LLMs, tools, and humans a shared agent interface, and illustrates it across coding, math, retrieval, and group-chat workflows. The report’s clearest contribution is a practical design and collection of demonstrations; the empirical evidence is limited and does not establish broad performance advantages.

- **strength**: The framework unifies agents with different capabilities and makes conversation behavior a configurable part of application design.
  - Page 2 · citation: whitespace
  - Quote: "developers can use Autogen to build a wide range of conversation patterns concerning conversation autonomy, the number of agents, and agent conversation topology."

- **strength**: The report includes a small direct math comparison, with AutoGen performing competitively in the reported trials.
  - Page 11 · citation: whitespace
  - Quote: "With one trial, AutoGen scores 8/12 problems, and both ChatGPT+Plugin and ChatGPT+Code Interpreter score 7/12 problems."

- **limitation**: The larger math comparison is based on only 12 sampled problems and one trial, limiting what it can establish about general comparative performance.
  - Page 11 · citation: whitespace
  - Quote: "We sample 12 level-5 problems from the MATH dataset."

- **limitation**: The retrieval comparison is not a controlled head-to-head evaluation: results for other systems are copied from another paper, and evaluation uses the first 500 questions.
  - Page 17 · citation: exact
  - Quote: "The metrics of other solutions are directly copied from the reference paper [2]."

Unresolved questions:

- How robust are the reported comparisons across larger, diverse task sets and repeated trials?
- How much of the reported task performance is attributable to the framework design versus prompts, models, tools, or application-specific engineering?
- What are the operational costs and failure rates of longer multi-agent workflows?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the framework design and concrete workflow examples. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 10, "end": 12}` | Inspect application examples and their reported evaluation evidence. | read pages [10, 11, 12] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 18, "end": 20}` | Inspect additional demonstrations and stated future-work limitations. | read pages [18, 19, 20] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 16, "end": 17}` | Inspect retrieval evaluation methodology and comparative results. | read pages [16, 17] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.58, "observations": 4}}` | Submit a balanced assessment using the framework description and inspected evaluations. | review accepted | [event 26](trace.jsonl#L26) |
