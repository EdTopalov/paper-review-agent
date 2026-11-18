# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 6.04 s · $0.000540

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 540 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes an extensible framework and benchmark for interactive code generation, with execution feedback, containerized environments, and task-specific reward functions. Its Bash and SQL implementations and evaluations illustrate how interaction changes model behavior and performance, while the small CTF demonstration suggests broader applicability. The contribution is useful and supported by substantial experiments, but evidence is concentrated in two environments and a limited set of tasks and prompting baselines.

- **strength**: The framework provides a concrete, modular recipe for building interactive coding tasks, including sandboxed execution and customizable scoring.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: Across the evaluated models and both task families, the reported results show higher success rates with iterative feedback than with single-turn generation.
  - Page 7 · citation: wrong_page
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The implemented benchmark coverage is narrow relative to the framework’s general-purpose claims, and the authors explicitly identify both limited language coverage and a tiny CTF set.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: How well the benchmark’s conclusions generalize beyond these implementations remains open; the paper describes broader coverage as future work rather than presenting evidence from additional programming-language environments.
  - Page 26 · citation: whitespace
  - Quote: "We plan to expand the number of InterCode based tasks to cover more programming languages"

Unresolved questions:

- How robust are the interaction benefits across additional languages, execution environments, and task types beyond Bash and SQL?
- How sensitive are success rates to reward-function choices, especially Bash’s lexical-output and file-diff scoring and SQL’s ordering penalty?
- Can the benchmark support reproducible comparisons across newer agent architectures and training approaches, not just the evaluated prompting strategies?
- This assessment is based on the supplied pages; I did not inspect any material beyond them, including repository contents or external replications.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
