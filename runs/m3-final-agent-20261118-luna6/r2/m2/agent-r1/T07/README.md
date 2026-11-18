# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

6 model calls · 4 reads · 13.42 s · $0.001714

6 decisions · 6 tool calls · 31203 input tokens (23150 cached) · 989 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.79

OSWorld contributes a real, interactive desktop environment and a 369-task benchmark spanning common applications, cross-app workflows, and execution-based task-specific evaluation. Its breadth and human-performance study make it useful research infrastructure; the inspected evidence leaves questions about evaluation reliability, benchmark representativeness, and baseline comparisons.

- **strength**: The benchmark pairs realistic initial states with task-specific executable evaluation rather than only static demonstrations.
  - Page 1 · citation: whitespace
  - Quote: "Each task example is derived from real-world computer use cases and includes a detailed initial state setup configuration and a custom execution-based evaluation script for reliable, reproducible evaluation."

- **strength**: The benchmark includes broad task coverage and many evaluation functions, including multi-application workflows.
  - Page 8 · citation: exact
  - Quote: "OSW ORLD contains a total of 369 tasks (and an additional 43 tasks on Windows for analysis)"

- **limitation**: The principal benchmark is Ubuntu-based; Windows coverage is supplementary and subject to activation requirements.
  - Page 6 · citation: whitespace
  - Quote: "369 real computing tasks defined and executed on Ubuntu. Additionally, we provide a set of 43 tasks for Windows"

- **uncertainty**: The authors acknowledge residual evaluation-label risk after substantial checking; the remaining false-positive/negative rate is not established in inspected evidence.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

Unresolved questions:

- How do the detailed baseline comparisons and agent results support the headline performance claims?
- How robust are task-specific evaluation scripts to alternative valid completions and edge cases?
- How representative are the tasks collected from authors and selected sources of broader real-world computer use?
- I did not inspect the full baseline-results section, most task-construction details, or appendices; assessment of those aspects remains uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper’s stated scope boundaries and limitations. | 3 matches on pages [6, 15, 23] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark motivation, design, and task construction details. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Review action-space constraints and benchmark task scope. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect human and model evaluation evidence and benchmark results. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.79, "observations": 4}}` | Evidence inspected covers environment and task design, known scope constraints, dataset statistics, and human performance; model-result tables were not inspected. | citation_validation_failed; #1: wrong_page (pages [1]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.79, "observations": 4}}` | Correct the first citation to quote the abstract text on the observed first page. | review accepted | [event 30](trace.jsonl#L30) |
