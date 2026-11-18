# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 8.29 s · $0.000714

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 653 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an interactive, VM-based desktop environment and a 369-task benchmark for evaluating computer-use agents across applications, interfaces, and multi-app workflows. Its task-specific initialization and execution-based evaluators support realistic, reproducible assessment, while baseline and human studies expose a substantial performance gap and concrete GUI-grounding challenges. The work is a strong benchmark and infrastructure contribution; its claims are bounded by the task and OS coverage and by the acknowledged possibility of evaluator errors.

- **strength**: The benchmark combines broad task coverage with substantial evaluation infrastructure, including custom execution-based evaluators and intermediate task states.
  - Page 8 · citation: not_found
  - Quote: "the OSWORLD benchmark provides example-wise, execution-based evaluation for tasks."

- **strength**: The experiments provide a useful, interpretable measure of the gap between current agents and people on these tasks.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors explicitly acknowledge that benchmark quality checks may not eliminate false positives and negatives, leaving evaluator reliability as a meaningful limitation.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

- **uncertainty**: The central benchmark contains 369 Ubuntu tasks; Windows is represented by a smaller supplementary set, and macOS is supported in principle but is not part of the main benchmark. How well conclusions generalize beyond the tested environment remains open.
  - Page 6 · citation: exact
  - Quote: "We create a benchmark suite of 369 real-world computer tasks on Ubuntu environment"

Unresolved questions:

- How robust are the task-specific evaluation scripts to alternative valid solutions and unintended side effects, particularly where evaluators inspect application-internal files or state?
- Do the reported agent weaknesses and performance levels persist on larger, independently curated task sets and a broader range of OS versions, applications, and hardware?
- How much do baseline results depend on the specific prompts, action limits, model versions, and observation preprocessing used in these experiments?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
