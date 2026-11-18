# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 6.81 s · $0.000493

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 508 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent introduces an agent-computer interface (ACI) tailored to language models and evaluates it on repository-level issue resolution. With GPT-4 Turbo it resolves 12.47% of the full SWE-bench test set; controlled Lite-set ablations indicate that interface choices such as summarized search, a bounded file viewer, and lint-guarded editing materially affect performance. The work’s strongest contribution is its concrete, experimentally probed interface-design framework, while the results remain bounded to a small set of models and benchmark settings.

- **strength**: The paper reports a sizable improvement over the interactive shell-only baseline on the 300-instance Lite subset, and separately reports full-set results.
  - Page 6 · citation: whitespace
  - Quote: "SWE-agent w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: Component ablations support the central claim that interface design matters: the reported rates vary with search strategy, viewer window, and editing setup.
  - Page 6 · citation: exact
  - Quote: "Iterative 12.0 ↓ 6.0"

- **limitation**: The authors acknowledge a recurring recovery weakness: agents often continue along unproductive approaches rather than recognizing dead ends.
  - Page 8 · citation: whitespace
  - Quote: "they rarely recognize dead ends or reset their problem solving approach."

- **uncertainty**: The ACI’s generality is not established beyond the two evaluated model families and the software-issue benchmark; broader transfer is an open question, not a demonstrated defect.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

Unresolved questions:

- Would the observed ACI gains persist across a broader range of language models, software ecosystems, and repository-level task benchmarks?
- How much of the improvement comes from the specialized commands themselves versus prompt, demonstration, and history-management choices considered together?
- Can adaptive recovery mechanisms reduce the repeated-edit and dead-end behavior identified in the trajectory analysis?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
