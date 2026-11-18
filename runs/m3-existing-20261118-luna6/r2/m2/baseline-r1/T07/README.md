# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 8.67 s · $0.000717

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 659 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes a controllable virtualized desktop environment and a 369-task Ubuntu benchmark with task-specific setup and execution-based evaluation, then uses it to measure current LLM/VLM agents and analyze their failure modes. Its breadth across applications and workflows, together with substantial annotation and evaluation work, makes it a useful research platform; the benchmark results also expose a large gap between evaluated agents and human participants.

- **strength**: The benchmark combines realistic task initialization with task-specific, execution-based checks, supporting assessment beyond matching a single demonstration.
  - Page 4 · citation: exact
  - Quote: "we design example-specific evaluation metrics including pre-setup, post-processing, and"

- **strength**: The reported evaluation shows a large performance gap for the tested agents and reveals particularly weak results on multi-app workflows.
  - Page 12 · citation: whitespace
  - Quote: "the average performance for tasks involving a single app is low, at 13.74%, but still more than double the 6.57% observed for subsets of tasks involving workflows across multiple apps."

- **limitation**: The authors identify remaining benchmark-quality risks despite multiple rounds of review; these qualify confidence in individual task labels and evaluations, though the paper does not establish their prevalence.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How well do the task-specific evaluators and reported agent rankings hold up under independent auditing, especially for tasks with multiple valid ways to complete them?
- How representative are the reported findings beyond the Ubuntu benchmark and the selected applications, given that the Windows set is smaller and the paper does not develop a macOS benchmark?
- I inspected the supplied paper, including its appendices; broader evidence on cross-lab replication and performance across newer agent systems is not provided here.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
