# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 8.18 s · $0.005125

1 decisions · 0 tool calls · 38684 input tokens (0 cached) · 580 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an interactive virtual-machine environment and a 369-task benchmark for evaluating computer-use agents across desktop and web applications, with task-specific setup and execution-based evaluation. Its broad task scope and baseline study make it a useful research platform; experiments show a large gap between tested agents and humans, while also exposing challenges in GUI grounding and multi-app workflows.

- **strength**: The benchmark’s combination of varied tasks and customized executable evaluation is a substantive contribution for studying agents in realistic computer environments.
  - Page 2 · citation: not_found
  - Quote: "Each task example is based on real-world computer use cases and often requires interactions with multiple applications and interfaces."

- **strength**: The reported evaluation gives a clear, substantial performance gap between the tested models and human participants, and breaks results down by task category.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors acknowledge that benchmark quality is not fully settled: further checks may be needed to reduce evaluation errors. This is a stated limitation, not evidence that a particular result is invalid.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

Unresolved questions:

- How robust are the task-specific evaluators to alternative valid ways of completing a task, and how often do false positives or negatives affect reported success rates?
- How well do the benchmark’s task mix and results generalize beyond the selected Ubuntu applications and the smaller Windows subset?
- The paper reports human performance and model baselines, but how would rankings and conclusions change with more participants or repeated runs to account for human and model variability?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
