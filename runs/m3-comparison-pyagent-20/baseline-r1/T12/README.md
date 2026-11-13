# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 4.59 s · $0.003626

1 decisions · 0 tool calls · 26994 input tokens (0 cached) · 503 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes a modular, Docker-based benchmark framework for interactive code generation, instantiated with Bash and SQL tasks adapted from existing datasets. Its evaluations show that execution feedback and structured prompting can improve task success over single-turn generation, while exposing persistent challenges in context discovery and multi-step reasoning. The paper’s strongest value is its benchmark design and empirical characterization; its scope and some evaluation choices limit how broadly to generalize the results.

- **strength**: The framework provides a reusable formulation and implementation path for interactive coding, with code actions, execution observations, and customizable rewards.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: Across the tested models, the reported SQL and Bash success rates generally improve in the Try Again setting; the paper also reports a schema-controlled SQL comparison in the appendix.
  - Page 7 · citation: wrong_page
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The benchmark’s demonstrated task coverage is narrow, and the paper explicitly notes that the CTF example is too small to support broad performance conclusions.
  - Page 9 · citation: whitespace
  - Quote: "the CTF dataset is limited to just four task instances due to our manual curation procedure."

- **uncertainty**: The paper reports strong improvements for interactive evaluation, but the inspected material does not establish how well these results transfer beyond the selected datasets, environments, prompts, and model versions.
  - Page 6 · citation: wrong_page
  - Quote: "We perform preliminary experiments to gauge the proficiency and behavior of current large language models on interactive coding tasks with Bash and SQL."

Unresolved questions:

- How robust are the reported advantages to alternative task datasets, execution environments, reward definitions, and interaction budgets?
- Would results persist with current model versions and with a broader, independently curated set of programming tasks?
- How safe and reproducible is execution in practice under adversarial or unusually costly commands? The authors note that the environments do not strictly limit action spaces and that Docker mitigates, rather than eliminates, risk.
- I inspected the supplied pages, including the main experimental results and selected appendix material; I did not inspect every appendix prompt, trajectory, or implementation detail, so conclusions about those sections are limited.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
