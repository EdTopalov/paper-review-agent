# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

7 model calls · 5 reads · 14.73 s · $0.003093

7 decisions · 7 tool calls · 45052 input tokens (26046 cached) · 958 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable, extensible desktop-computer benchmark with diverse cross-application tasks, per-task state setup, and execution-based evaluation, alongside baseline comparisons that expose a large gap between current agents and novice human users. The benchmark infrastructure and diagnostic results are substantial; conclusions are bounded by task and platform coverage and acknowledged residual annotation error.

- **strength**: Execution-based assessment uses task-specific scripts to handle varied outcomes rather than a single uniform metric.
  - Page 4 · citation: exact
  - Quote: "we design example-specific evaluation metrics"

- **strength**: The benchmark includes many distinct initial states and evaluation scripts.
  - Page 8 · citation: whitespace
  - Quote: "a total of 84 tasks (22.8%) are integrated from related datasets"

- **strength**: Baseline evidence shows a marked model-human performance gap, especially on workflow tasks.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors report residual risk of false positives and negatives despite multiple rounds of checking.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

Unresolved questions:

- How robust are the benchmark's task-specific evaluators to alternative but valid ways of completing tasks?
- How well do the Ubuntu-centered results generalize to Windows and macOS, and to applications beyond the selected set?
- I inspected the introduction, benchmark design/statistics, and baseline results, but not the full appendices or later analysis; implementation details and additional experimental limitations remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope and limitations for a balanced assessment. | 3 matches on pages [6, 15, 23] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 4}` | Inspect benchmark task construction and evaluation design and reported evidence. | read pages [3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Review task coverage and action-space boundaries that may limit benchmark conclusions. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect evaluation results, human comparison, and baseline experimental evidence. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 11}` | Check baseline outcomes and experimental procedures before finalizing evidence. | read pages [10, 11] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers benchmark design, evaluation scale, baseline results, and a stated validation limitation; submit a balanced review. | citation_validation_failed; #2: not_found | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the unmatched benchmark-statistics quote using exact observed text, then submit the review. | review accepted | [event 37](trace.jsonl#L37) |
