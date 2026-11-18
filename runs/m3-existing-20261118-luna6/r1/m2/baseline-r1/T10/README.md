# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 7.01 s · $0.003265

1 decisions · 0 tool calls · 23863 input tokens (0 cached) · 564 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-agent argues that language-model agents benefit from computer interfaces designed around their interaction patterns, and implements such an interface for repository-level software engineering. On SWE-bench, it reports 12.47% resolved on the full test set and uses Lite-set ablations to show meaningful gains from its editing, search, and feedback design. The paper combines a useful system contribution with empirical evidence and behavioral analysis, while its evidence for generality and causal attribution remains bounded by the tested models, tasks, and configurations.

- **strength**: The full benchmark evaluation reports a concrete improvement over the cited prior RAG result, and the system also transfers to a second model.
  - Page 2 · citation: whitespace
  - Quote: "SWE-agent solves 12.5% of the 2,294 SWE-bench test issues"

- **strength**: The Lite-set ablations provide evidence that interface components matter, including a substantial difference from the shell-only agent.
  - Page 6 · citation: wrong_page
  - Quote: "SWE-agent solves 10.7 percentage points more issues than the baseline agent that uses just the default Linux shell."

- **limitation**: The reported evaluation is tied to two closed models, and the authors say other tested models performed poorly; this limits the evidence for broad model generality.
  - Page 5 · citation: not_found
  - Quote: "we experimented with a number of additional closed and open source models, including Llama 3 and DeepSeek Coder, but found their performance in the agent setting to be subpar."

- **uncertainty**: The ACI was developed through qualitative inspection and a small development subset before testing; how robust the design and ablation effects are across broader configurations remains an open question.
  - Page 5 · citation: whitespace
  - Quote: "we arrived at the final ACI design through qualitative analysis of system behavior on small set of hand-picked easier examples"

Unresolved questions:

- How well do the ACI design principles and observed gains generalize to other model families, programming languages, and repository-level task distributions?
- How sensitive are the component ablation results to benchmark subset selection, stochastic variation, and interactions among interface components?
- This assessment is based on the supplied PDF text, including its main paper and some appendix pages; I have not independently inspected or reproduced the system, trajectories, or benchmark runs.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
