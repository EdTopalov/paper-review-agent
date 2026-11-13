# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**pyagent_react · ok**

4 model calls · 2 reads · 22.59 s · $0.002008

4 decisions · 4 tool calls · 16323 input tokens (7618 cached) · 1688 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

WebArena contributes a reproducible, multi-site web environment and a benchmark of long-horizon natural-language tasks, with functional task-completion evaluation and baseline agents. Its realism-oriented design and release make it useful infrastructure for studying autonomous web agents; the reported low best-agent success rate also illustrates the benchmark’s difficulty. The evidence inspected supports the environment and benchmark design, but does not establish broader validity or the robustness of the reported results.

- **strength**: The benchmark pairs its 812 examples with a functional-correctness evaluation metric.
  - Page 5 · citation: whitespace
  - Quote: "Each example comes with a metric to evaluate the functional correctness of the task execution."

- **strength**: The environment supports multiple web-observation modes and multi-tab tasks, offering varied interfaces for agent evaluation.
  - Page 4 · citation: whitespace
  - Quote: "WebArena is the first web environment to consider multi-tab web-based tasks"

- **strength**: The paper reports a challenging baseline outcome for its best GPT-4-based agent.
  - Page 1 · citation: whitespace
  - Quote: "our best GPT-4-based agent only achieves an end-to-end task success rate of 10.59%."

- **uncertainty**: The inspected task-collection description says annotators could use ChatGPT for inspiration; the possible effect on task diversity or benchmark validity remains unanswered by the pages inspected, not demonstrated as a defect.
  - Page 6 · citation: exact
  - Quote: "We additionally provided a prompt for the annotators to use to prompt ChatGPT 5 for inspiration."

Unresolved questions:

- How stable are the reported success rates across repeated runs, task subsets, and agent configurations?
- How representative are the sampled sites and annotated intents of real users’ web tasks?
- I inspected pages 1 and 4–6 and a search-result snippet, not the full paper; details of the evaluation, annotation quality controls, limitations, and additional experiments remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 4, "end": 6}` | Inspect benchmark construction and evaluation results. | read pages [4, 5, 6] | [event 6](trace.jsonl#L6) |
| 2 | search_paper `{"query": "10.59%"}` | Locate the reported agent performance results. | 2 matches on pages [1, 2] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an evidence-based assessment using the inspected pages and note the limited coverage. | citation_validation_failed; #1: not_found | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Correct the failed page-5 citation using verbatim inspected text. | review accepted | [event 23](trace.jsonl#L23) |
