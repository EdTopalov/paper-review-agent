# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

5 model calls · 4 reads · 15.90 s · $0.001949

5 decisions · 5 tool calls · 32516 input tokens (22556 cached) · 957 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

InterCode contributes a lightweight framework for evaluating coding agents through iterative code execution and feedback, and instantiates it with Bash and SQL tasks adapted from existing datasets. Its value is both infrastructural—a modular, containerized task interface—and empirical: evaluations show that interaction and prompting strategy can substantially affect task success. The results support the benchmark’s usefulness, while the limited task domains and custom reward choices constrain how broadly they generalize.

- **strength**: The paper specifies an interactive task formulation and a modular construction pipeline, with Docker-based execution and an endpoint for custom reward definitions.
  - Page 4 · citation: whitespace
  - Quote: "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container, allowing for custom reward function definitions that can incorporate multiple signals."

- **strength**: The evaluations show large gains from multi-turn interaction on SQL, including a substantial improvement for GPT-4; the paper also reports robustness results for Bash across selected file systems.
  - Page 6 · citation: whitespace
  - Quote: "with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The authors identify a narrow set of implemented environments and a very small manually curated CTF set; these are stated scope limits, not evidence that the framework cannot be extended.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets; within the near future, we plan to expand the number of offerings"

- **uncertainty**: The benchmark uses task-specific reward designs, including lexical similarity for Bash output and ordered-output scoring for SQL. How well these measures capture semantic correctness across broader task types remains unanswered by the inspected evidence.
  - Page 5 · citation: whitespace
  - Quote: "Execution output is graded with a simple lexical similarity function."

Unresolved questions:

- How do the task-specific reward functions behave when different commands or queries produce semantically equivalent results?
- How well do the reported findings transfer to programming languages, environments, and task datasets beyond Bash and SQL?
- I inspected the paper’s task formulation, evaluation overview, selected results, robustness analysis, and stated limitations, but not the full appendix, prompts, or all experimental details; uncertainty remains about those details and broader reproducibility.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "results"}` | Locate benchmark findings and quantitative evaluation. | 8 matches on pages [1, 9, 13, 17, 19, 21] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect task construction and evaluation methodology. | read pages [4, 5, 6] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect experiment results and the authors’ stated scope and limitations. | read pages [7, 8, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 21, "end": 22}` | Check reported robustness and uncertainty analyses. | read pages [21, 22] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit a balanced assessment supported by inspected benchmark, results, and limitations pages. | review accepted | [event 26](trace.jsonl#L26) |
