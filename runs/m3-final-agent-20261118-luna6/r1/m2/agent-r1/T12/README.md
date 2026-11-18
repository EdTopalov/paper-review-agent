# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

6 model calls · 5 reads · 11.68 s · $0.002906

6 decisions · 6 tool calls · 34860 input tokens (15048 cached) · 596 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

InterCode makes a useful benchmark contribution by formalizing interactive coding with execution feedback as a reusable environment framework and applying it to Bash and SQL. Its evaluations show substantial gains from interaction and compare prompting approaches across tasks. The evidence is promising but preliminary: the implemented environments cover only two action spaces, and reward design and task adaptation shape what success measures.

- **strength**: The paper presents a modular interactive benchmark design and concrete Bash and SQL implementations adapted from existing datasets.
  - Page 4 · citation: exact
  - Quote: "Each environment is defined in under 200 lines of code total."

- **strength**: Across tested models, interactive execution feedback is associated with improved success rates, with a particularly large SQL gain for GPT-4.
  - Page 6 · citation: whitespace
  - Quote: "notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The implemented task coverage is narrow, a scope boundary the authors explicitly acknowledge.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **limitation**: Docker mitigates command harms but does not itself establish strict action restrictions or safe transfer to real systems.
  - Page 26 · citation: whitespace
  - Quote: "the Bash and SQL InterCode environments currently do not explicitly impose any strict limitations on the action space."

Unresolved questions:

- How well do the benchmark's findings and framework generalize to additional programming languages, environments, and task distributions?
- How sensitive are model rankings and measured gains to reward definitions and the dataset transformations used to ground tasks?
- I inspected the abstract, framework and implementation sections, selected evaluation results, and limitations; I did not inspect every experiment, appendix detail, or full trajectory, so uncertainty remains about robustness beyond the reported evidence.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate evaluation results and quantitative evidence for the benchmark. | 8 matches on pages [1, 9, 13, 17, 19, 21] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the stated contributions and framework design after the introduction. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 5}` | Review environment implementation and benchmark setup details. | read pages [4, 5] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect model evaluation findings and reported performance patterns. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states scope limitations or caveats. | 7 matches on pages [9, 13, 14, 26] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers framework design, experimental results, and explicitly stated scope and safety limitations; submit a calibrated assessment. | review accepted | [event 31](trace.jsonl#L31) |
