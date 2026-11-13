# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

3 model calls · 2 reads · 8.00 s · $0.001039

3 decisions · 3 tool calls · 7708 input tokens (1539 cached) · 523 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

OSWorld contributes a broad, executable computer-use environment and a 369-task benchmark with task setup and execution-based evaluation across real applications and workflows. Its baseline evaluations expose a substantial capability gap between tested agents and humans, making the benchmark useful for research; the inspected material also identifies constraints in the action interface.

- **strength**: The benchmark pairs diverse real-world tasks with configured starting states and custom completion checks, supporting reproducible execution-based assessment.
  - Page 2 · citation: whitespace
  - Quote: "Each task example is based on real-world computer use cases experienced by real users and often requires interactions with multiple applications and interfaces."

- **strength**: The reported baseline results and human comparison provide evidence that the tasks reveal a meaningful performance gap.
  - Page 1 · citation: whitespace
  - Quote: "While humans can accomplish over 72.36% of the tasks, the best model achieves only 12.24% success"

- **limitation**: The supported action space does not encompass all computer interactions, which the authors say can cap agent learning capabilities.
  - Page 6 · citation: whitespace
  - Quote: "they do not model all possible actions on a computer, leading to limitations when attempting actions like right-clicking and clicking with the ctrl key held to select items."

- **uncertainty**: I inspected the abstract and selected design/results discussion, not the complete evaluation protocol or all task-level evidence; the strength of the broader baseline claims cannot be fully assessed from these passages.
  - Page 3 · citation: whitespace
  - Quote: "Results also show that while additional knowledge such as the accessibility tree and Set-of-Mark (§4.1) can be helpful, it can also lead to potential misguidance and varies across models."

Unresolved questions:

- How robust are the evaluation scripts and task outcomes across repeated runs and environment versions?
- How representative are the task selection and reported human performance of ordinary computer-use workloads?
- How much do the reported agent results depend on the specific action interface and interaction limits?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors' stated scope boundaries and limitations before assessing the benchmark. | 3 matches on pages [6, 15, 23] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and task construction evidence to ground the contribution assessment. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | The inspected abstract and design/results pages support a preliminary assessment; cite the explicit action-space limitation and note uninspected detailed experiments. | review accepted | [event 16](trace.jsonl#L16) |
