# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**deliberative_review · ok**

6 model calls · 3 reads · 21.60 s · $0.005574

6 decisions · 4 tool calls · 38421 input tokens (1243 cached) · 1848 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

InterCode contributes a practical framework for evaluating coding agents that can execute code and use the resulting feedback across turns, alongside Bash and SQL environments and comparative model experiments. The described task construction and results make a credible case for its usefulness as a benchmark and research testbed, though the empirical results cover a limited set of environments and do not establish broad generalization.

- **strength**: The framework operationalizes interactive coding through code actions, execution observations, and task-specific reward functions; the paper describes concrete Bash and SQL implementations.
  - Page 4 · citation: whitespace
  - Quote: "Given a coding instruction u ∈ U in natural language, an agent issues code or a specialsubmit keyword as an action at ∈ A."

- **strength**: Experiments show higher success rates for multi-turn feedback than single-turn generation across the reported model tables, including a large SQL improvement for GPT-4.
  - Page 7 · citation: exact
  - Quote: "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"

- **limitation**: The demonstrated environment coverage is narrow, and the authors explicitly describe the CTF example as very small. This is a scope limitation, not evidence that the general framework cannot support more tasks.
  - Page 26 · citation: exact
  - Quote: "this demonstration currently only has four task instances."

- **uncertainty**: The reported comparisons are informative, but the inspected excerpts do not establish how robust results are to repeated runs or other sources of evaluation variability. I did not inspect the full methods appendix or all paper sections.
  - Page 8 · citation: exact
  - Quote: "usinggpt-3.5-turbo as the base model."

Unresolved questions:

- How stable are the model and prompting comparisons across repeated evaluations, and what uncertainty estimates apply to the reported success rates?
- How well do the benchmark tasks and reward functions transfer to additional languages, datasets, or less curated interactive coding settings?
- What further guardrails are needed if agents trained or evaluated in these containers are later connected to real systems?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the Bash and SQL environment/task construction and evaluation protocol to assess whether InterCode genuinely tests interactive coding with execution feedback and supports reproducible comparisons.; Review the reported model and prompting experiments, baselines, metrics, and results to check whether the evidence supports claims about benefits and benchmark difficulty.; Inspect discussion, limitations, and remaining paper sections for scope boundaries or qualifications; only page 1 is currently available, so do not treat uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 7 matches on pages [9, 13, 14, 26] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [3, 4, 5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [6, 7, 8] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Find discussion of scope and qualifications, then inspect evidence for task construction and experiments. | 7 matches on pages [9, 13, 14, 26] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 5}` | Inspect core method and benchmark results for environment construction and empirical support. | read pages [3, 4, 5] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 8}` | Inspect model experiment setup/results and discussion to assess empirical claims, using relevant adjacent pages. | read pages [6, 7, 8] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
