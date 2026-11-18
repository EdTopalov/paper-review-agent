# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

5 model calls · 4 reads · 13.79 s · $0.002107

5 decisions · 5 tool calls · 40025 input tokens (28455 cached) · 753 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

OSWorld contributes an executable, extensible computer-use environment and a 369-task benchmark with task-specific setup and evaluation, addressing evaluation across apps and workflows. Its baseline and human studies document a large performance gap and provide useful analyses of agent behavior. The contribution is substantial, though the inspected evidence leaves questions about benchmark coverage and the generality of results beyond the tested models and configurations.

- **strength**: The benchmark pairs diverse computer tasks with per-task setup and executable evaluation rather than relying only on demonstrations.
  - Page 2 · citation: exact
  - Quote: "a custom execution-based evaluation script to verify task completion"

- **strength**: The evaluation includes human comparison and reports markedly lower agent success, with workflow tasks particularly challenging.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors acknowledge that further quality-control effort may be needed to reduce evaluation errors; this is a disclosed limitation, not evidence that specific scripts are defective.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

- **uncertainty**: The results are informative for the tested setup, but how well they generalize to other models and interaction configurations remains open; the inspected pages do not establish broader coverage.
  - Page 10 · citation: whitespace
  - Quote: "We heuristically request the agents to complete the tasks within a max step limit of 15"

Unresolved questions:

- How robust are the benchmark conclusions to different agent architectures, prompting strategies, action interfaces, or step limits?
- How do the custom evaluators behave on a broad set of alternative valid solutions and edge cases, beyond the reported checks?
- I inspected pages 1–4, 7–13; I did not inspect the remaining methods, appendices, or full task/evaluator specifications, so their details and any further limitations remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task construction, and evaluation methodology. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect benchmark results and human-performance comparison. | read pages [8, 9, 10] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 11, "end": 13}` | Inspect detailed result analysis and robustness or limitation discussion. | read pages [11, 12, 13] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 7}` | Inspect task annotation and quality-control procedures. | read pages [7] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an assessment grounded in the inspected benchmark, results, and quality-control pages. | review accepted | [event 26](trace.jsonl#L26) |
