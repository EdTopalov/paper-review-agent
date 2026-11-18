# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

6 model calls · 5 reads · 15.63 s · $0.003785

6 decisions · 6 tool calls · 53188 input tokens (28552 cached) · 841 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable real-computer environment and a 369-task benchmark spanning desktop/web applications, operating-system tasks, and multi-app workflows, with configured initial states and task-specific execution-based evaluation. Its baseline and human evaluations demonstrate a substantial present-day performance gap, making it a useful benchmark and diagnostic resource. The work’s breadth and practical infrastructure are compelling, though annotation and evaluation quality remain partly dependent on manually authored task-specific checks.

- **strength**: The benchmark combines realistic initial states and executable evaluation with broad task coverage; the authors describe substantial annotation and checking effort.
  - Page 7 · citation: whitespace
  - Quote: "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions."

- **strength**: The reported evaluations show low baseline success relative to human performance, including especially weak results on multi-app workflows.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors acknowledge that further quality assurance may be needed to reduce evaluation errors; this is a stated caveat, not evidence that particular benchmark labels are defective.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How consistently do the 134 custom evaluation functions accept valid alternative solutions and avoid false positives or negatives across the full task set?
- How well do the reported agent comparisons generalize beyond the evaluated models, prompts, and task configurations?
- I inspected the opening pages, selected benchmark/results pages, and one search result; I did not inspect the full appendices, implementation, or individual evaluation scripts, so their detailed validity and reproducibility remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task construction, and evaluation methodology. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 12, "end": 14}` | Inspect baseline results and the paper’s empirical comparisons. | read pages [12, 13, 14] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 9, "end": 11}` | Inspect benchmark results and reported human/model performance. | read pages [9, 10, 11] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "limitations"}` | Check the paper’s explicit scope boundaries and acknowledged limitations. | 3 matches on pages [6, 15, 23] | [event 21](trace.jsonl#L21) |
| 5 | read_pages `{"start": 6, "end": 8}` | Read benchmark task coverage and the stated action-space limitation. | read pages [6, 7, 8] | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 3}}` | Cite inspected benchmark construction, measured results, and stated quality-control caveat. | review accepted | [event 32](trace.jsonl#L32) |
