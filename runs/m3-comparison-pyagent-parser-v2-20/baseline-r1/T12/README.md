# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 5.03 s · $0.003596

1 decisions · 0 tool calls · 26994 input tokens (0 cached) · 444 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

InterCode presents a reusable, Docker-based framework for evaluating interactive code generation, instantiates it for Bash and SQL, and reports baseline comparisons suggesting that execution feedback and structured prompting can improve task success. Its main value is as benchmark infrastructure and an empirical starting point, rather than a new model or a broad demonstration of generality.

- **strength**: The paper defines a modular interface for tasks with executable actions, observations, and customizable rewards, and implements Bash and SQL environments.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: Across the reported model and task settings, multi-turn feedback is associated with higher success than single-turn generation; the paper also reports robustness results for Bash.
  - Page 7 · citation: wrong_page
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The benchmark’s implemented task coverage is narrow, and the authors explicitly describe the CTF demonstration as very small; broad claims of universality are therefore prospective rather than demonstrated here.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **limitation**: Execution is sandboxed, but the paper warns that its environments do not strictly restrict commands and that transferring agents to real systems could be risky.
  - Page 26 · citation: whitespace
  - Quote: "a direct sim-to-real transfer of an InterCode-trained agent to a real system may put the system at risk."

Unresolved questions:

- How well does the framework and its evaluation design generalize to additional languages, environments, and task types beyond the two implemented benchmarks?
- How sensitive are the reported success rates to dataset grounding and reward-function choices, particularly the Bash lexical-output and file-diff criteria?
- The inspected pages include reported standard errors for Bash, but do not provide enough detail here to assess uncertainty or significance for every comparison, including SQL and prompting strategies.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
