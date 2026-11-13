# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 6.34 s · $0.005157

1 decisions · 0 tool calls · 38684 input tokens (0 cached) · 643 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable desktop-computer environment and a 369-task Ubuntu benchmark spanning applications, operating-system operations, and multi-app workflows. Its task-specific setup and execution-based evaluators enable reproducible assessment of real GUI/CLI interactions. Baseline results expose a large gap between the tested agents and human participants, while analyses identify grounding, operational knowledge, and workflow handling as persistent challenges.

- **strength**: The benchmark’s combination of configurable intermediate states and task-specific execution evaluators is a substantial contribution to evaluating varied computer-use tasks.
  - Page 7 · citation: exact
  - Quote: "a total of 134 unique evaluation functions"

- **strength**: The evaluation provides a clear empirical signal: tested agents perform far below participants on the benchmark, and multi-app tasks are especially difficult for the strongest reported baseline.
  - Page 12 · citation: whitespace
  - Quote: "the average performance for tasks involving a single app is low, at 13.74%, but still more than double the 6.57% observed for subsets of tasks involving workflows across multiple apps."

- **limitation**: The benchmark is broad in task type but its main evaluated set is concentrated on Ubuntu and a selected set of applications; the Windows set is smaller and has access restrictions.
  - Page 6 · citation: whitespace
  - Quote: "we mainly focus on eight representative applications"

- **uncertainty**: The authors report remaining evaluator-quality concerns, so the extent to which task-specific scripts consistently accept all valid solutions remains an open issue.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

Unresolved questions:

- How reliably do the task-specific evaluators recognize valid alternative outcomes and workflows, particularly for open-ended tasks?
- How well do the findings generalize beyond the selected Ubuntu applications and the comparatively small Windows task set?
- How much do baseline rankings and success rates vary across repeated runs, given stochastic generation and the paper’s reported use of a single benchmark setup?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
