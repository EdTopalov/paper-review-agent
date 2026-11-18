# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

5 model calls · 4 reads · 9.48 s · $0.001603

5 decisions · 5 tool calls · 32310 input tokens (23557 cached) · 578 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

OSWorld contributes an executable, extensible real-computer environment and a 369-task benchmark with task-specific setup and execution-based evaluation, then uses it to expose substantial weaknesses in current multimodal computer agents. The integrated environment and task construction are the main research value; the reported baseline evidence is useful, though the benchmark’s task and platform coverage remains bounded.

- **strength**: The benchmark couples varied real-computer tasks to explicit setup and completion checks, supporting reproducible assessment across applications and workflows.
  - Page 2 · citation: whitespace
  - Quote: "Each task example is based on real-world computer use cases experienced by real users and often requires interactions with multiple applications and interfaces."

- **strength**: The agent results demonstrate a pronounced gap on this benchmark, with analysis that identifies concrete failure modes rather than reporting only aggregate scores.
  - Page 15 · citation: exact
  - Quote: "more than 75% exist mouse click inaccuracies, which is the most common error."

- **limitation**: The main benchmark is concentrated on Ubuntu and selected applications; the smaller Windows set does not establish broad cross-platform coverage.
  - Page 6 · citation: whitespace
  - Quote: "we mainly focus on eight representative applications as well as the basic ones the system provides"

- **uncertainty**: The reported human comparison and extensive task-specific evaluators lend support, but I did not inspect the full annotation protocol, evaluator validation, or detailed human-study methodology, so reliability and generalization of those comparisons remain unclear.
  - Page 2 · citation: whitespace
  - Quote: "9 authors with computer science backgrounds carefully annotate each example"

Unresolved questions:

- How robust are task-specific evaluators to valid alternative completion paths and edge cases across the benchmark?
- How representative are the benchmark tasks and reported human performance of broader computer use beyond the selected applications and operating systems?
- I inspected only pages 1–6 and 14–16 plus a search excerpt; methodology and results elsewhere, including detailed annotation and human-study procedures, remain unreviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task composition, and evaluation methodology. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 6}` | Review evaluation scoring design and task benchmark statistics. | read pages [5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 14, "end": 16}` | Inspect baseline results and human comparison supporting claims. | read pages [14, 15, 16] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check the paper’s explicit scope limitations before final assessment. | 3 matches on pages [6, 15, 23] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers contribution, evaluation design, and baseline results; submit concise paper assessment. | review accepted | [event 25](trace.jsonl#L25) |
