# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 8.22 s · $0.000612

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 683 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode introduces a modular framework and benchmark for interactive code generation, where agents execute commands in sandboxed Bash or SQL environments and use execution feedback to revise their actions. The paper provides a useful initial empirical study across models and prompting strategies, including evidence that interaction can improve task success. Its contribution is substantial as a benchmark and tool, though the demonstrated task coverage is limited and some evaluation choices warrant further validation.

- **strength**: The benchmark’s interactive setup is supported by results showing notable gains over single-turn prompting, especially for SQL; the paper also reports that the gain persists when schema information is provided.
  - Page 7 · citation: exact
  - Quote: "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"

- **strength**: The framework is presented as extensible and grounded in a concrete implementation, with a modular interface for environment execution and reward design.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **limitation**: The paper explicitly bounds the empirical scope: the principal environments are Bash and SQL, and the CTF demonstration has very few instances, limiting conclusions about broader task coverage.
  - Page 9 · citation: whitespace
  - Quote: "the CTF dataset is limited to just four task instances due to our manual curation procedure."

- **uncertainty**: The Bash reward combines several signals using weights the authors describe as arbitrary. How sensitive reported benchmark outcomes are to these weights is not established in the inspected material.
  - Page 16 · citation: exact
  - Quote: "The scalar weights for each component are arbitrarily assigned."

Unresolved questions:

- How robust are model rankings and success-rate conclusions to alternative reward definitions, especially for Bash’s blended output and filesystem score?
- Would the observed benefits of interaction generalize to a broader set of languages, environments, and task datasets beyond the implemented Bash and SQL settings?
- What agent-training methods and safeguards are effective when InterCode is used as a training platform rather than for the inference-time evaluations reported here?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
