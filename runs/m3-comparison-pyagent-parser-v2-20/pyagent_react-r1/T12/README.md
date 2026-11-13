# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

5 model calls · 2 reads · 16.33 s · $0.002431

5 decisions · 4 tool calls · 28304 input tokens (15861 cached) · 1434 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes a practical, extensible framework for evaluating coding agents through execution feedback, and demonstrates its use on Bash and SQL tasks with several prompting strategies. Its central value is the shared interactive task formulation and tooling; the empirical results illustrate that interaction and strategy matter, while the benchmark remains limited in task breadth and some proposed extensions are preliminary.

- **strength**: The framework makes interactive coding tasks configurable through modular environments and reward design, rather than tying the benchmark to one task format.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: The evaluation reports meaningful differences between prompting strategies and task types, supporting the usefulness of the benchmark for comparative study.
  - Page 7 · citation: whitespace
  - Quote: "Compared to Try Again, which lacks specific guidance on leveraging multiple turns, more explicit reasoning frameworks such as ReAct and Plan & Solve policies generally achieve higher success rates (SQL: 47.3% → 58.7%) with fewer turns and a higher rate of admissible commands."

- **limitation**: The authors explicitly identify limited environment coverage and a very small manually curated CTF set; these bound claims about breadth rather than refuting the framework.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets; within the near future, we plan to expand the number of offerings to cover a wider set of programming languages and datasets"

- **uncertainty**: The reported results show prompting strategies do not improve both environments uniformly, leaving open how robustly strategy rankings generalize across tasks and settings.
  - Page 8 · citation: exact
  - Quote: "SQL 47.3 7.25 46.4 58.7 5.30 6.94 49.1 4.29 16.2\nBash 46.5 6.15 24.9 20.5 4.40 20.4 28.0 6.65 53.3"

Unresolved questions:

- How stable are the reported results across additional datasets, environments, and model versions beyond the evaluated configurations?
- How sensitive are task success rates to reward-function choices, especially where exact-match criteria may penalize valid alternative solutions?
- I inspected pages 1, 3–4, and 7–9 only; details elsewhere in the paper, including full experimental procedures and appendices, remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark design and reported evaluation results. | read pages [7, 8, 9] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 3, "end": 4}` | Inspect task construction, dataset composition, and evaluation protocol. | read pages [3, 4] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment from the inspected framework, results, and limitations pages. | citation_validation_failed; #2: wrong_page (pages [7]) | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the strategy-result citation to its observed page and submit the assessment. | review accepted | [event 27](trace.jsonl#L27) |
