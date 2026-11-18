# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

5 model calls · 4 reads · 14.83 s · $0.001253

5 decisions · 5 tool calls · 21053 input tokens (14234 cached) · 548 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

WebArena contributes a self-hostable, reproducible suite of functional web applications and 812 long-horizon natural-language tasks, with programmatic outcome checks and baseline agent evaluations. It is a substantial benchmark resource for studying web agents, while its task coverage and initial agent comparisons remain bounded.

- **strength**: The benchmark pairs realistic multi-site tasks with outcome-oriented checks rather than requiring one exact action path, making it a useful evaluation platform.
  - Page 2 · citation: whitespace
  - Quote: "We provide annotated programs designed to programmatically validate the functional correctness of each task."

- **strength**: The paper supplies meaningful task breadth and identifies the scale of the benchmark.
  - Page 7 · citation: exact
  - Quote: "In total, we curated 241 templates and 812 instantiated intents."

- **limitation**: Some benchmark intents are infeasible in the environment; the authors explicitly label this boundary rather than treating all tasks as executable.
  - Page 8 · citation: whitespace
  - Quote: "some tasks ( ∼4%) in our benchmark are not possible to complete."

- **uncertainty**: The reported agent evidence is an initial, narrow baseline comparison; it establishes difficulty for these setups, not a general ceiling on agent capability. I inspected the benchmark and baseline sections but not the full appendices or later discussion.
  - Page 9 · citation: exact
  - Quote: "The end-to-end task success rate (%) onWebArena."

Unresolved questions:

- How robust are the benchmark results to different task populations, annotators, and alternative evaluation implementations?
- How would agents using visual observations, longer interaction budgets, or different tool-use strategies perform on the same tasks?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope limitations to assess what the benchmark does and does not establish. | 2 matches on pages [2, 11] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task construction, and evaluation details beyond the abstract. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "10.59%"}` | Find the experimental results and benchmark success rates to judge evidence for the paper’s claims. | 2 matches on pages [1, 2] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect task benchmark construction and reported agent evaluation, including validation criteria and quantitative results. | read pages [7, 8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Evidence covers contribution, task/evaluation design, baseline results, and a stated unachievable-task boundary; submit a balanced assessment with explicit gaps. | review accepted | [event 25](trace.jsonl#L25) |
