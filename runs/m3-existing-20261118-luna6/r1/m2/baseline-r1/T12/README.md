# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 6.31 s · $0.003621

1 decisions · 0 tool calls · 26994 input tokens (0 cached) · 494 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes a reusable framework and benchmark for evaluating language models as interactive coding agents, with execution feedback rather than one-shot code generation. Its Bash and SQL environments, extensible task interface, and comparisons across models and prompting strategies provide a useful empirical starting point. The evidence supports the value of interaction on these tasks, but the benchmark’s limited task coverage and bespoke reward designs constrain how broadly its results generalize.

- **strength**: The paper specifies a modular environment interface and describes containerized execution, task data, and reward design, making the benchmark’s construction concrete and extensible.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: On the reported benchmarks, multi-turn feedback improves success rates over single-turn evaluation; an SQL schema ablation also preserves an interaction advantage, offering evidence beyond the initial comparison.
  - Page 20 · citation: whitespace
  - Quote: "while Single Turn performance improves drastically, a non-trivial difference in favor of Try Again remains."

- **limitation**: The paper acknowledges narrow task coverage and a very small CTF demonstration, so the broad claims of generality are not yet matched by broad empirical coverage.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: Docker is presented as providing safe execution, but the authors also note that the environments lack strict action restrictions and caution against transferring agents directly to real systems. The degree of isolation and residual risk is not established in the inspected text.
  - Page 26 · citation: whitespace
  - Quote: "the Bash and SQL InterCode environments currently do not explicitly impose any strict limitations on the action space."

Unresolved questions:

- How well do the observed interaction benefits transfer to additional programming languages, environments, and task types beyond Bash and SQL?
- How sensitive are the reported success rates to the particular reward definitions, especially Bash’s lexical-output component and SQL’s ordering treatment?
- What safety guarantees and threat model apply to the Docker execution sandbox, including risks from container escape or unsafe configuration?
- The supplied pages reference appendices for experimental details and uncertainty estimates; how do those details affect interpretation of the main comparisons? I did not inspect any material beyond the supplied pages.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
