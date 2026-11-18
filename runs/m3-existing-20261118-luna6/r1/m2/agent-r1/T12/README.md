# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

6 model calls · 5 reads · 9.75 s · $0.002911

6 decisions · 6 tool calls · 34594 input tokens (14756 cached) · 606 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

InterCode makes a substantial benchmark contribution by formalizing interactive coding with execution feedback as a reusable environment, providing Bash and SQL implementations, and evaluating prompting strategies across multiple language models. The reported results show that interaction can improve task success, while the paper appropriately identifies limited environment coverage and a very small CTF demonstration as scope constraints.

- **strength**: The framework has a clear modular task formulation and execution-based reward design intended to support adaptation of existing datasets.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: Results provide concrete evidence that interactive execution feedback can improve performance, including a large SQL gain for GPT-4.
  - Page 6 · citation: whitespace
  - Quote: "with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The reported benchmark implementations cover only Bash and SQL, which limits the demonstrated breadth of the general framework.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **limitation**: The CTF extension is illustrative rather than a substantial benchmark evaluation because it contains only four task instances.
  - Page 9 · citation: whitespace
  - Quote: "Second, the CTF dataset is limited to just four task instances due to our manual curation procedure."

Unresolved questions:

- How robust are the reported improvements across additional interactive coding datasets and programming languages?
- How sensitive are benchmark outcomes to the reward functions’ exact-match and output-comparison choices?
- The inspected pages do not include the full experimental protocol or detailed appendix analyses, so evaluation repeatability and further implementation details remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the authors’ stated scope and limitations to balance the benchmark’s contribution. | 7 matches on pages [9, 13, 14, 26] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect the framework and benchmark design and the reported evaluation evidence. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 9}` | Review model evaluation results and author discussion of benchmark limitations. | invalid_page_range | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 8}` | Inspect the empirical results, prompting comparisons, and performance interpretations. | read pages [6, 7, 8] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Verify specific limitations and safety caveats in the authors’ concluding discussion. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence inspected covers framework design, benchmark results, and stated limitations; submit an assessment while noting uninspected details. | review accepted | [event 31](trace.jsonl#L31) |
