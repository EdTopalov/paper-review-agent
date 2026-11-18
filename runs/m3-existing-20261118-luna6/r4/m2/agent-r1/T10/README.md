# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

6 model calls · 4 reads · 18.61 s · $0.002195

6 decisions · 6 tool calls · 40586 input tokens (30171 cached) · 1221 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-agent’s central contribution is a language-model-tailored agent-computer interface for repository-level software engineering, with concise search and navigation, integrated editing and feedback, lint-based guardrails, and context management. On SWE-bench, it reports 12.47% resolved with GPT-4 Turbo, substantially above the listed interactive shell-only and RAG baselines; Lite-set interface ablations provide evidence that several design choices matter. The contribution is practically and experimentally substantial, though demonstrated on a narrow benchmark/model setup and not a general account of autonomous software engineering.

- **strength**: The paper makes a focused interface-design contribution, grounded in observed agent behavior and configuration experiments rather than merely proposing a new agent wrapper.
  - Page 3 · citation: whitespace
  - Quote: "We use two ap- proaches to enhance the ACI on a development set: We manually inspect the behaviour of the agent to identify difficulties and propose improvements, and we run a grid search over ACI configurations."

- **strength**: The reported headline results outperform the included baselines, and the Lite-set ablations offer quantitative evidence that editing and linting choices affect performance.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: The paper gives concrete, interpretable evidence for a proposed mechanism: syntax-error guardrails are associated with a performance gain over the no-linting variant.
  - Page 7 · citation: exact
  - Quote: "This intervention improves performance considerably (Without Linting, 15.0% ↓ 3.0)."

- **limitation**: The empirical scope is bounded: experiments focus on two large-context models and SWE-bench tasks, so the results do not establish transfer to broader software-engineering settings.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs, GPT-"

Unresolved questions:

- How robust are the gains across additional language models, benchmark types, languages, and less curated real-world engineering tasks?
- How sensitive are the headline results to repeated runs and stochasticity? I inspected the main results and ablation pages but not the paper’s later variance analysis or appendices.
- What are the practical tradeoffs in maintenance and reliability when integrating the ACI tools into diverse repositories and workflows?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Find the paper’s stated scope and limitations to assess claims fairly. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect core methods and experimental setup/results for substantiated contribution. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Inspect quantitative comparisons and interface ablations supporting the performance claims. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "budget"}` | Check stated evaluation constraints and budget behavior for scope qualifications. | 8 matches on pages [5, 7, 8, 20] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers the proposed ACI, main benchmark results, ablations, and evaluation limits; submit an independently grounded assessment. | citation_validation_failed; #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the unsupported verbatim quote using the inspected page 5 model-scope wording and resubmit the assessment. | review accepted | [event 30](trace.jsonl#L30) |
