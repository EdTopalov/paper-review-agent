# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

6 model calls · 5 reads · 13.38 s · $0.001863

6 decisions · 6 tool calls · 23175 input tokens (11455 cached) · 604 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

WebArena contributes a reproducible, self-hosted multi-site web environment and an 812-task benchmark that evaluates functional completion rather than matching reference action traces. Its realistic task framing and executable checks make it a useful platform for agent research; the reported low best-agent success underscores task difficulty, though evidence inspected here does not establish broader external validity.

- **strength**: The environment combines several operational website domains with utilities and knowledge resources, and is designed for reproducibility.
  - Page 2 · citation: whitespace
  - Quote: "Our environment comprises four fully operational, self-hosted web applications"

- **strength**: The benchmark has substantial task count and emphasizes checking whether the goal was achieved, allowing alternative valid paths.
  - Page 2 · citation: whitespace
  - Quote: "Along with WebArena, we release a ready-to-use benchmark with 812 long-horizon web-based tasks"

- **limitation**: Information-seeking evaluation uses an LLM-based fuzzy matcher for some tasks, making that part of the metric dependent on a separate model judgment.
  - Page 7 · citation: whitespace
  - Quote: "we usegpt-3.5-turbo-0613 to assess whether ˆa could entail each of the key concepts in a∗"

- **uncertainty**: The authors report only 10.59% best GPT-4-based end-to-end success in the inspected material; I have not inspected later experimental details, so the causes and robustness of this result remain unclear.
  - Page 2 · citation: whitespace
  - Quote: "the best GPT-4 agent performance is somewhat limited, with an end-to-end task success rate of 10.59%"

Unresolved questions:

- How do baseline results vary across task categories and observation/action configurations?
- How robust are the programmatic and language-model-based evaluation annotations to ambiguous or acceptable alternative answers?
- How well do tasks and agent rankings transfer beyond the four simulated website domains?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper's stated scope boundaries and limitations. | 2 matches on pages [2, 11] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "10.59%"}` | Locate the reported benchmark results and accompanying evaluation discussion. | 2 matches on pages [1, 2] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction, task diversity, and evaluation protocol. | read pages [2, 3, 4] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "human evaluation"}` | Find evaluation details and any caveats about task validity or benchmark coverage. | 0 matches | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark task composition and ground-truth functional evaluation. | read pages [5, 6, 7] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers environment, benchmark, results, and evaluation design; submit an assessment while noting unread later sections. | review accepted | [event 31](trace.jsonl#L31) |
