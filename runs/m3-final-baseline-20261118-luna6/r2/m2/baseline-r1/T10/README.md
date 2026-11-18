# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 6.21 s · $0.000511

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 545 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-agent presents an LM-oriented agent-computer interface for repository-level software engineering and evaluates it on SWE-bench. Its results and interface ablations offer substantial evidence that interface design can affect agent performance, while the paper also documents persistent failure to recover from unproductive approaches.

- **strength**: The system achieves a substantial improvement over the reported retrieval baseline on the full benchmark, and the results include a second model.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59"

- **strength**: Lite-set ablations provide evidence that several interface choices—editing, search, file-window size, and context handling—contribute to performance.
  - Page 6 · citation: exact
  - Quote: "Shell-only 10.3 ↓ 7.7"

- **limitation**: The authors report that agents often persist with an approach that is not working, indicating a meaningful limitation in error recovery.
  - Page 8 · citation: whitespace
  - Quote: "they rarely recognize dead ends or reset their problem solving approach."

Unresolved questions:

- How robust are the main full-test-set results to run-to-run variation? The paper reports pass@k analysis for SWE-bench Lite, but the supplied results do not establish comparable variance for the full test set.
- How well do the ACI findings transfer beyond the tested models and this Python-issue benchmark? Evidence inspected here covers GPT-4 Turbo and Claude 3 Opus, with interface ablations reported on the Lite subset.
- The review is based on the supplied 25 pages; I inspected the reported methodology, results, and appendix tables, but not underlying code, trajectories, or independently reproduced experiments.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
