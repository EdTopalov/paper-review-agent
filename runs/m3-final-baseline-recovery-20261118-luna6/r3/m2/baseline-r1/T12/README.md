# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 5.65 s · $0.000525

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 510 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes an extensible framework and benchmark for interactive code generation, with Docker-based Bash and SQL environments that provide execution feedback and task-specific rewards. Its experiments show higher success rates for multi-turn interaction than single-turn generation and compare prompting strategies, while illustrating the framework’s potential for new tasks. The evidence supports a useful benchmark and empirical case study, though the environments and CTF demonstration remain limited in scope.

- **strength**: The paper gives a concrete, modular formulation for interactive coding tasks and implements two environments using existing datasets.
  - Page 4 · citation: whitespace
  - Quote: "InterCode decomposes the construction of an interactive coding task into three modular parts: (1) environment construction, (2) data collection, and (3) reward design."

- **strength**: Reported results consistently favor interaction over single-turn generation across the evaluated models and tasks; the appendix also reports robustness checks for Bash.
  - Page 7 · citation: wrong_page
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The benchmark’s implemented language and task coverage is narrow, and the CTF example is too small to support broad performance conclusions.
  - Page 26 · citation: whitespace
  - Quote: "The Capture the Flag toy dataset showcases InterCode’s serviceability for developing novel tasks with new code understanding challenges that can easily be used for training and evaluating models. With that said, this demonstration currently only has four task instances."

- **uncertainty**: The paper presents Docker as a safe execution sandbox, but acknowledges that the environments do not strictly constrain actions and that transfer to real systems can be risky.
  - Page 26 · citation: whitespace
  - Quote: "the Bash and SQL InterCode environments currently do not explicitly impose any strict limitations on the action space."

Unresolved questions:

- How well do the interaction benefits generalize beyond Bash and SQL, beyond the selected datasets, and to larger or more diverse interactive tasks?
- How sensitive are success rates to reward-function choices, especially Bash’s lexical-output similarity and SQL’s exact record/order scoring?
- What safety guarantees and containment properties hold for untrusted actions beyond the paper’s stated Docker isolation and optional designer-defined guardrails?
- I inspected the supplied pages, including the main experiments and selected appendix material; I did not independently inspect the linked code, data, or full trajectories, so implementation and reproduction details remain unverified.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
