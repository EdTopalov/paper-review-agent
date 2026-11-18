# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 7.52 s · $0.000559

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 578 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode presents a reusable framework and Bash/SQL benchmarks for evaluating code agents that interact with execution environments. Its experiments show substantial gains from interaction on several model/task settings and illustrate how prompting strategies affect behavior. The work is a useful benchmark contribution, though the evaluation covers a limited set of environments and does not establish broad generalization or training benefits.

- **strength**: The paper makes the benchmark’s interactive, modular design concrete through a task formulation, Docker-based execution, and customizable rewards.
  - Page 4 · citation: wrong_page
  - Quote: "generated code is treated as actions, which are executed to reveal observations."

- **strength**: The experiments provide evidence that interaction can improve task success, including a large SQL gain for GPT-4; the appendix also reports robustness results for Bash.
  - Page 6 · citation: whitespace
  - Quote: "notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The demonstrated benchmark coverage is narrow, and the authors explicitly identify both the limited action spaces and the very small CTF set as current boundaries.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: Docker provides isolation, but the paper cautions that the environments do not strictly constrain actions; the safety of transferring agents to real systems is therefore not established.
  - Page 26 · citation: exact
  - Quote: "do not explicitly impose any strict limitations on the action space."

Unresolved questions:

- How well do the observed interaction gains transfer to additional languages, environments, and task datasets beyond Bash and SQL?
- Would these environments produce measurable benefits when used to train agents, rather than only evaluate prompted models?
- How sensitive are the reported success rates to reward-design choices, especially the lexical-output and file-system components of the Bash reward?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
