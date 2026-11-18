# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

5 model calls · 4 reads · 9.28 s · $0.001548

5 decisions · 5 tool calls · 27078 input tokens (18659 cached) · 649 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

InterCode contributes a practical framework for treating code generation as interactive action and execution-feedback, with Docker-backed Bash and SQL benchmarks adapted from existing datasets. Its evaluations show that interaction and reasoning-oriented prompts can materially improve success on these tasks, while exposing persistent failure modes. The framework is a useful benchmark contribution, though the evaluated task coverage is narrow and some claims about safety and generality remain bounded by the implementations tested.

- **strength**: The work defines a modular interactive benchmark and provides automatic execution-based task evaluation, allowing existing instruction/code datasets to be adapted while retaining customizable rewards.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: The experiments provide concrete evidence that feedback can improve model performance; for GPT-4 on SQL, success rises substantially in the multi-turn setting.
  - Page 6 · citation: whitespace
  - Quote: "with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The demonstrated benchmark coverage is restricted to Bash and SQL; the paper itself identifies this as a limitation, so broad language-agnostic applicability is primarily a framework claim rather than a demonstrated evaluation result.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **limitation**: The showcased CTF task is too small to support broad evaluation conclusions about that task family.
  - Page 9 · citation: whitespace
  - Quote: "Second, the CTF dataset is limited to just four task instances due to our manual curation procedure."

Unresolved questions:

- How robust are the benchmark scores to reward-function choices, especially lexical similarity and exact-match components, and to alternative valid solutions?
- How well do the framework’s safety and reproducibility claims hold under broader environments and adversarial actions? The inspected pages do not establish this beyond the tested Docker tasks.
- How representative are the benchmark tasks of interactive coding beyond the adapted datasets? I inspected the benchmark design, selected results, and explicit limitations, not all appendix details or the full experimental analysis.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ discussion of benchmark scope and limitations to assess remaining gaps. | 7 matches on pages [9, 13, 14, 26] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark design and evaluation evidence supporting the paper’s central claims. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Review model evaluation results and experimental setup for strength and caveats. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Check the paper’s explicit limitations and scope boundaries before assigning a score. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit an evidence-grounded assessment based on the inspected design, results, and limitations pages. | review accepted | [event 25](trace.jsonl#L25) |
