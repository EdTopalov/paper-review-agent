# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 8.63 s · $0.000597

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 653 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

InterCode proposes a reusable framework for evaluating interactive code generation with execution feedback, implementing Bash and SQL environments adapted from existing datasets. Its experiments show that interaction and reasoning-oriented prompts can improve task success, while also documenting persistent model failures. The work is a useful benchmark and systems contribution, though its empirical conclusions are bounded by the two environments and the evaluated settings.

- **strength**: The paper gives a concrete, modular task formulation and implementation approach that supports execution feedback, custom rewards, and extensible environments.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: The reported comparisons support the claim that interaction can improve performance in the studied settings; the appendix also reports robustness results across several Bash models.
  - Page 7 · citation: wrong_page
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The authors explicitly bound the current benchmark’s coverage to Bash and SQL and note that the CTF demonstration is very small, so broad generalization is not established.
  - Page 26 · citation: whitespace
  - Quote: "The Capture the Flag toy dataset showcases InterCode’s serviceability for developing novel tasks with new code understanding challenges that can easily be used for training and evaluating models. With that said, this demonstration currently only has four task instances."

- **uncertainty**: The experiments establish results for selected models and prompting configurations, but leave open how well the findings extend to other interactive tasks and agent approaches.
  - Page 6 · citation: wrong_page
  - Quote: "We perform preliminary experiments to gauge the proficiency and behavior of current large language models on interactive coding tasks with Bash and SQL."

Unresolved questions:

- How well do the benchmark’s task design and interaction-related findings generalize to additional programming languages, environments, and task types?
- Would the observed benefits persist under broader comparisons of agent methods, model families, and task samples beyond the evaluated setups?
- How should continuous reward scores be interpreted across Bash and SQL tasks, given that their reward functions use different task-specific criteria?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
