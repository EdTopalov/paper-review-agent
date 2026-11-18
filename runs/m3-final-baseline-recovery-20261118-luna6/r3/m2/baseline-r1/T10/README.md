# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 6.04 s · $0.000512

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 546 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent makes a practical and empirically supported case that tailoring the tools and feedback used by language-model agents can improve repository-level software engineering. Its custom interface combines file navigation, editing, search, context management, and edit guardrails; tests on SWE-bench show stronger results than the reported RAG and shell-only baselines, with ablations indicating that several interface choices matter. The work’s evidence is substantial for its setting, though claims about generality are bounded by the evaluated models, benchmark, and task split.

- **strength**: The main benchmark results show a sizable gain over the listed RAG baseline and a positive result with a second model.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: Ablations on SWE-bench Lite support the claim that interface design contributes to performance: the full setup outperforms shell-only, and removing linting or changing the viewer window also lowers results.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The authors acknowledge a recurring weakness in error recovery: agents often continue an unproductive approach rather than recognizing a dead end.
  - Page 8 · citation: whitespace
  - Quote: "they rarely recognize dead ends or reset their problem solving approach."

- **uncertainty**: The interface-design evidence is strongest for GPT-4 Turbo on the 300-instance Lite subset; the paper reports transfer to Claude, but the inspected material does not establish whether the specific ablation effects generalize across models or the full benchmark.
  - Page 5 · citation: whitespace
  - Quote: "we perform a hyperparameter sweep over the window size, history processing, and decoding temperature."

Unresolved questions:

- Do the relative effects of search, editing, linting, and context-management choices persist across different model families and on the full SWE-bench test set?
- How much of the reported performance depends on the provided demonstration and the hand-selected development examples used in interface design?
- What interface or agent changes can reliably help recover from unproductive trajectories, beyond the edit-time syntax guardrail?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
