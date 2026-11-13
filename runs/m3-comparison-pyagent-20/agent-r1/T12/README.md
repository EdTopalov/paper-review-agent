# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

3 model calls · 2 reads · 6.79 s · $0.001275

3 decisions · 3 tool calls · 9507 input tokens (1444 cached) · 525 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes a practical, extensible framework for treating code generation as interaction with execution environments, and instantiates it in Bash and SQL benchmarks adapted from existing datasets. Its clearest value is the standardized task interface and reproducible environment construction; the paper also reports preliminary model evaluations, though those results are not among the inspected pages here.

- **strength**: The benchmark makes interactive code generation explicit as a sequential environment, rather than only evaluating a final code output.
  - Page 4 · citation: whitespace
  - Quote: "The InterCode benchmark formalizes interactive coding with execution feedback as a partially observable Markov decision process (POMDP)"

- **strength**: The paper provides concrete task implementations and reports that each environment is compact to define.
  - Page 4 · citation: exact
  - Quote: "Each environment is defined in under 200 lines of code total."

- **limitation**: The authors identify the current language and dataset coverage as narrow; this limits generalization of the benchmark’s demonstrated reach, without negating its extensible design.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: The paper describes its model study as preliminary, but I did not inspect the results section, so I cannot assess the strength or robustness of the empirical comparisons.
  - Page 5 · citation: whitespace
  - Quote: "We perform preliminary experiments to gauge the proficiency and behavior of current large language models on interactive coding tasks with Bash and SQL."

Unresolved questions:

- How do the reported model results compare across prompting strategies and environments, and how robust are they to task/data variation?
- How well do the reward functions handle semantically correct alternative solutions, especially for Bash outputs and SQL ordering?
- I inspected pages 1, 3–5 and search excerpts from pages 9 and 26, not the full paper; empirical results and implementation details beyond those excerpts remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper’s stated scope and limitations to judge the benchmark claims. | 7 matches on pages [9, 13, 14, 26] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect the framework and evaluation sections for concrete contributions and evidence. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence inspected covers the framework, task construction, reward designs, and stated limitations; submit an independent assessment while noting evaluation details not inspected. | review accepted | [event 16](trace.jsonl#L16) |
