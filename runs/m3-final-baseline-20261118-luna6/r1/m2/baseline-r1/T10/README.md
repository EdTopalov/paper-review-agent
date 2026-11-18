# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 7.85 s · $0.000567

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 656 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent argues that language-model agents benefit from interfaces designed for their interaction patterns, and presents a software-engineering agent with tailored search, file viewing, editing, feedback, and context management. On SWE-bench, it reports 12.47% resolved with GPT-4 Turbo; ablations on the 300-instance Lite split provide evidence that several interface choices improve performance over a shell-only agent.

- **strength**: The full-test-set evaluation provides a concrete benchmark result, and the paper also reports transfer to a second language model.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: The Lite-set ablations give evidence for the value of the interface, including editing and linting, though individual comparisons do not isolate every design choice.
  - Page 7 · citation: whitespace
  - Quote: "Without SWE-agent’s file editor interface, performance drops to (10.3% ↓ 7.7)."

- **limitation**: The main results are pass@1, so the headline resolution rates do not describe the potential of repeated sampling; the appendix reports a higher pass@6 result on Lite.
  - Page 20 · citation: whitespace
  - Quote: "we perform, all results, unless otherwise stated, are reported using a pass@1 metric (% Resolved)."

- **uncertainty**: The paper’s empirical support for interface design is centered on GPT-4 Turbo and a 300-instance Lite ablation; how well these conclusions generalize to other models and broader software-engineering settings remains open.
  - Page 5 · citation: whitespace
  - Quote: "We report our main agent results on the full SWE-bench test set and ablations and analysis on the SWE-bench Lite test set"

Unresolved questions:

- How robust are the reported interface gains across newer or substantially different language models, beyond the two models evaluated here?
- Which individual ACI components, or interactions between them, account for the gains across a wider range of repositories and issue types?
- How do resolution rates change under repeated sampling or different cost budgets on the full SWE-bench test set?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
