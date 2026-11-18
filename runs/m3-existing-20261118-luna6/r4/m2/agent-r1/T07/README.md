# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

5 model calls · 4 reads · 11.32 s · $0.001448

5 decisions · 5 tool calls · 23376 input tokens (15569 cached) · 665 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

OSWorld makes a substantial benchmark and infrastructure contribution: an executable, extensible computer-use environment paired with 369 Ubuntu tasks, task-specific execution evaluators, and baseline agent and human measurements. Its breadth and reproducibility-oriented design are valuable, and the low baseline success rates expose a meaningful capability gap. The inspected evidence supports benchmark utility, while generalization beyond the represented OS/apps and details of evaluator reliability remain open.

- **strength**: The benchmark combines real interactive tasks with executable, per-task evaluation rather than relying only on demonstrations.
  - Page 7 · citation: whitespace
  - Quote: "we implement nearly sample-specific executable evaluation scripts, resulting in a total of 134 unique evaluation functions for assessing functional correctness"

- **strength**: The evaluation demonstrates a large gap between the tested agents and human task completion, supporting the benchmark's diagnostic value.
  - Page 10 · citation: exact
  - Quote: "GPT-4 20.83% 3.58% 25.64% 26.53% 2.97% 12.24%"

- **limitation**: The central task benchmark is concentrated on Ubuntu and selected applications; Windows coverage is smaller and macOS is described as supported for development rather than represented at comparable benchmark scale.
  - Page 6 · citation: whitespace
  - Quote: "encompasses 369 real computing tasks defined and executed on Ubuntu. Additionally, we provide a set of 43 tasks for Windows"

- **limitation**: The implemented agent action interface does not cover all computer actions, which the authors identify as limiting learning capability.
  - Page 6 · citation: whitespace
  - Quote: "they do not model all possible actions on a computer, leading to limitations when attempting actions like right-clicking and clicking with the ctrl key held to select items."

Unresolved questions:

- How robust are the manually authored evaluation scripts to semantically correct but unanticipated task outcomes, beyond the described checking and review process?
- How well do findings transfer to operating systems, applications, user populations, and workflows outside the benchmark's selected Ubuntu-centered task distribution?
- I inspected pages 1, 3–4, and 6–10 and a search result on limitations; I did not inspect the full paper, appendices, or all experimental analyses, so further methodological details may qualify this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors' stated scope boundaries and limitations for a balanced assessment. | 3 matches on pages [6, 15, 23] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 4}` | Inspect benchmark construction and evaluation details to judge contribution and empirical support. | read pages [3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Check action-space restrictions and task composition to identify material scope limits. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 10}` | Inspect headline benchmark results and experimental protocol to assess strength of evidence. | read pages [9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.77, "observations": 4}}` | Evidence covers benchmark design, dataset scope, action constraints, and baseline results; submit a bounded assessment while noting uninspected sections. | review accepted | [event 25](trace.jsonl#L25) |
