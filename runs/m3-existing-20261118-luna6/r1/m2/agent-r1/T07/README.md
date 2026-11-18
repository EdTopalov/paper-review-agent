# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

6 model calls · 5 reads · 10.42 s · $0.002864

6 decisions · 6 tool calls · 34264 input tokens (15163 cached) · 687 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable, extensible real-computer environment and a 369-task Ubuntu benchmark with task-specific setup and execution-based evaluation, then uses it to expose the gap between contemporary agents and human performance. The benchmark and infrastructure are a substantial research resource; the reported evaluations are informative but remain a bounded snapshot of selected systems, tasks, and interfaces.

- **strength**: The paper combines realistic multi-application tasks with per-task initialization and executable completion checks, offering a meaningful platform contribution beyond static demonstrations.
  - Page 2 · citation: whitespace
  - Quote: "We also create a benchmark of 369 real-world computer tasks in OSW ORLD with reliable, reproducible setup and evaluation scripts."

- **strength**: The benchmark reports a pronounced agent–human performance gap across the evaluated tasks, supporting its diagnostic value.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The central benchmark is concentrated on Ubuntu, and the described software coverage is representative rather than exhaustive; the paper separately provides a smaller Windows set.
  - Page 6 · citation: whitespace
  - Quote: "We introduce the OSW ORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu."

- **uncertainty**: The results are for a particular set of baseline agents and prompting/action settings; how robust the headline results are to different agent designs and evaluation choices is not established by the inspected pages.
  - Page 10 · citation: whitespace
  - Quote: "We heuristically request the agents to complete the tasks within a max step limit of 15, which is enough for most tasks."

Unresolved questions:

- How well do task-specific evaluation scripts accept alternative but valid task outcomes across the full benchmark?
- How representative are the reported model results of agents using different interaction architectures, tool strategies, or longer action horizons?
- What coverage and reproducibility results hold for the Windows and macOS environment support beyond the Ubuntu-centered benchmark?
- I inspected pages 1–4, 6–7, and 10–11; I did not inspect the appendices or the remaining paper, so detailed annotation validation and further limitations may alter this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "12.24%"}` | Locate reported benchmark outcomes and evaluation results. | 4 matches on pages [1, 2, 10, 11] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task construction, and stated contributions. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether authors explicitly discuss benchmark limitations or scope boundaries. | 3 matches on pages [6, 15, 23] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect stated action-space boundary and benchmark task coverage. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 11}` | Inspect model results and human comparison to ground assessment of empirical evidence. | read pages [10, 11] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers benchmark scope, methodology, results, and a stated limitation; submit an evidence-grounded assessment while noting inspection gaps. | review accepted | [event 31](trace.jsonl#L31) |
