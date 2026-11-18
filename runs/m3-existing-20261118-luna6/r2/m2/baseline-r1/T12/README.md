# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 6.89 s · $0.000513

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 485 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.7

InterCode contributes an extensible benchmark and environment framework for interactive code generation, pairing executable Bash and SQL tasks with feedback, Docker-based execution, and task-specific rewards. Its evaluations show that interaction often improves model success over single-turn generation, while also revealing challenges in using feedback and planning. This is a useful benchmark contribution, though the empirical scope is limited to two environments and the evidence for broad generality is preliminary.

- **strength**: The paper gives a concrete, modular formulation that supports interactive tasks and custom reward design; it implements the framework for two distinct action spaces.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: Reported comparisons show substantial gains from interaction for several models, with a schema-controlled SQL comparison also retaining a Try Again advantage.
  - Page 20 · citation: whitespace
  - Quote: "while Single Turn performance improves drastically, a non-trivial difference in favor of Try Again remains."

- **limitation**: The authors explicitly bound the current benchmark’s coverage to Bash and SQL, so claims of universal applicability are framework-level aspirations rather than evidence across languages.
  - Page 26 · citation: whitespace
  - Quote: "The InterCode codebase currently features two tasks with Bash and SQL programming languages as action spaces."

- **uncertainty**: The SQL reward requires exact record ordering for full credit; how this choice affects scores when a task’s answer is semantically order-insensitive remains unclear from the inspected discussion.
  - Page 19 · citation: not_found
  - Quote: "only a correctly ordered list with the exact set of records found in the gold output would receive a max score of 1"

Unresolved questions:

- How well does the framework and its interaction gains generalize to other languages, environments, and task types beyond Bash and SQL?
- How sensitive are the reported results to reward and evaluation choices, including output lexical similarity in Bash and ordering penalties in SQL?
- What are the empirical effects of Docker isolation and added command guardrails under broader or more adversarial agent behavior?
- I inspected the supplied pages, including the main experiments and selected appendix sections; I did not independently verify implementation or dataset artifacts, and the full supplementary details referenced by the paper are not all available in the supplied text.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
