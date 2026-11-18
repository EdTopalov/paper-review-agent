# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

7 model calls · 5 reads · 18.18 s · $0.003083

7 decisions · 6 tool calls · 45790 input tokens (26974 cached) · 924 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

OSWorld contributes an executable desktop-computer environment and a benchmark of open-ended tasks spanning applications and GUI/CLI workflows, with task-specific state setup and execution-based evaluation. Baseline results expose a large gap between tested agents and human participants and support the benchmark’s value for diagnosing computer-use capabilities. The evidence inspected is strongest for Ubuntu tasks; the paper describes Windows examples and broader OS support, but I did not inspect the full paper, appendices, or all evaluation details.

- **strength**: The benchmark pairs real-computer tasks with custom initialization and execution-based checks, giving the suite concrete and reproducible evaluation machinery.
  - Page 2 · citation: whitespace
  - Quote: "Each task example is based on real-world computer use cases experienced by real users and often requires interactions with multiple applications and interfaces."

- **strength**: The reported baseline table shows a substantial performance gap, while also making performance differences across task categories visible.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The benchmark’s empirical task coverage is concentrated on Ubuntu, even though the environment is described as supporting more operating systems; this bounds what the inspected results establish about cross-platform performance.
  - Page 6 · citation: whitespace
  - Quote: "We introduce the OSW ORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu. Additionally, we provide a set of 43 tasks for Windows built onOSW ORLD envi- ronment"

Unresolved questions:

- How representative are the 369 tasks of computer-use requests beyond the selected applications and task sources?
- How well do the benchmark tasks and evaluation scripts transfer across Windows and macOS in practice?
- I did not inspect the full paper, appendices, or detailed human-study and annotation procedures; what additional evidence there might provide remains uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark design, task coverage, and evaluation setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Human"}` | Locate reported human evaluation results for comparison with agent performance. | 8 matches on pages [1, 2] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark results, baseline comparisons, and evaluation caveats. | read pages [10, 11, 12] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states scope limitations or evaluation caveats. | 3 matches on pages [6, 15, 23] | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 6, "end": 6}` | Inspect benchmark scope and stated action-space limitations. | read pages [6] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.75, "observations": 3}}` | Synthesize the inspected benchmark design, empirical results, and stated platform scope. | review accepted | [event 36](trace.jsonl#L36) |
