# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 8.83 s · $0.000712

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 650 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an interactive virtual-machine environment and a 369-task benchmark for evaluating computer-use agents across desktop applications, operating-system tasks, and multi-app workflows. Its central contribution is the combination of configurable initial states with task-specific execution-based evaluation; experiments with contemporary-for-the-paper agents show a large gap from human performance and identify grounding and operational knowledge as major challenges. The work is a substantial benchmark and infrastructure contribution, though its evidence is bounded by its task and platform coverage and by the evaluation choices described in the paper.

- **strength**: The benchmark pairs realistic, configurable task states with execution-based checks, supporting evaluation beyond fixed action demonstrations.
  - Page 2 · citation: not_found
  - Quote: "Each task example is based on real-world computer use cases and often requires interactions with multiple applications and interfaces."

- **strength**: The reported results quantify a substantial performance gap and include human evaluation as a useful reference point.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors identify remaining quality-control risk: despite multiple checks, further red-teaming may uncover evaluation errors.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

- **uncertainty**: The main benchmark is Ubuntu-based; the paper offers a smaller Windows set, while macOS is discussed as supported in the environment but is not part of the main benchmark evidence presented here.
  - Page 6 · citation: not_found
  - Quote: "We create a benchmark suite of 369 real computing tasks defined and executed on Ubuntu."

Unresolved questions:

- How robust are the task-specific evaluators to valid alternative solutions and edge cases not anticipated by their authors?
- How well do the benchmark’s task mix and human-performance estimates generalize beyond the selected applications and student participants?
- How much do the reported agent results depend on the particular interaction limits, prompts, and model versions used in the experiments?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
