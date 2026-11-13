# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

4 model calls · 2 reads · 21.90 s · $0.002437

4 decisions · 4 tool calls · 21638 input tokens (10012 cached) · 1767 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

OSWorld contributes an interactive virtualized computer environment and a benchmark of real-app tasks evaluated through task-specific execution scripts. Its breadth across GUI, CLI, files, and multi-app workflows, plus reproducible task setup, makes it a useful evaluation platform. The inspected pages support the design and task-construction claims, but do not include the later experimental results or enough detail to judge evaluator reliability and benchmark coverage fully.

- **strength**: The benchmark uses many task-specific evaluation functions, supporting assessment of varied outcomes rather than a single demonstration path.
  - Page 2 · citation: exact
  - Quote: "Our benchmark has a total of 134 unique evaluation functions"

- **strength**: The environment is designed to support open-ended interactions across applications and operating systems, including raw keyboard and mouse control.
  - Page 2 · citation: whitespace
  - Quote: "This executable environment allows free-form raw keyboard and mouse control of real computer applications and supports initial task state configuration, execution-based evaluation, and interactive learning across mainstream operating systems (e.g., Ubuntu, Windows, macOS)."

- **limitation**: Ubuntu receives the extensive examples described here, while the inspected text does not establish comparable task coverage across operating systems.
  - Page 6 · citation: whitespace
  - Quote: "For development purposes, we offer an extensive set of examples on Ubuntu and its open-source applications"

- **uncertainty**: The evaluation design requires substantial task-specific engineering, including software-specific preparation and potentially reverse-engineering assistance; how this affects reproducibility across evaluators is not established in the inspected pages.
  - Page 5 · citation: whitespace
  - Quote: "Occasionally, this process may also require assistance from reverse engineering tools, such as for decrypting account information in Thunderbird."

Unresolved questions:

- How do the full benchmark results and human-performance comparisons support the abstract's reported performance gap? Those results were not inspected.
- How robust are the task-specific evaluators to alternative valid completion states, and how consistently can independent contributors implement them?
- How representative are the selected tasks and applications of computer use beyond the collected sources and Ubuntu-focused suite?
- Only the abstract and pages 2–6 were inspected; later experimental methods, detailed results, limitations, and appendices remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and evaluation evidence. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 6}` | Inspect evaluation methods and benchmark composition. | read pages [5, 6] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit a provisional assessment based on the abstract and inspected pages 2–6; later results and limitations were not inspected. | citation_validation_failed; #1: wrong_page (pages [1]); #3: hyphenation_ambiguous (pages [6]) | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Correct the mismatched and ambiguous citations using exact text from inspected pages. | review accepted | [event 23](trace.jsonl#L23) |
