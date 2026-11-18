# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 7.21 s · $0.000535

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 529 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

InterCode introduces a reusable framework and benchmark formulation for interactive code generation, treating code as actions and execution results as observations. Its Bash and SQL environments adapt existing datasets, and experiments across several language models and prompting strategies show that interaction can improve task success while exposing challenges in context discovery and error correction. The work is a substantial benchmark contribution, though its empirical scope and some evaluation choices limit how broadly its results support claims about interactive coding.

- **strength**: The modular environment, data, and reward design makes the benchmark practical to extend beyond the two included tasks.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: The evaluation includes a meaningful comparison: interactive feedback improves success on both tasks for the reported models, with a large SQL gain for GPT-4.
  - Page 6 · citation: whitespace
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The paper acknowledges that the benchmark covers only Bash and SQL, and that the CTF demonstration is too small for robust evaluation.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: The main comparisons do not isolate interaction from all differences in prompt setup; the schema ablation addresses one SQL information disparity, but the evidence presented does not establish how broadly the gains generalize across alternative interaction budgets or task constructions.
  - Page 20 · citation: whitespace
  - Quote: "while Single Turn performance improves drastically, a non-trivial difference in favor of Try Again remains"

Unresolved questions:

- How stable are the interactive-versus-single-turn gains across different task datasets, reward designs, and environments beyond the adapted Bash and Spider tasks?
- How much do the reported results depend on prompt templates, model API versions, and the maximum of ten turns?
- Do continuous reward scores reliably reflect partial task correctness, especially for Bash lexical similarity and SQL output ordering?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
