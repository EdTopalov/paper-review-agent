# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

4 model calls · 3 reads · 11.17 s · $0.001380

4 decisions · 4 tool calls · 18845 input tokens (10752 cached) · 547 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-agent’s central contribution is a tailored agent-computer interface for repository-level software engineering, with simple search/edit tools, informative feedback, and editing guardrails. On SWE-bench it reports substantially higher issue-resolution rates than the presented RAG and shell-only baselines, and interface ablations provide evidence that multiple design choices matter. The contribution is substantial, while the inspected evaluation is bounded to two leading models and offers limited basis for conclusions beyond its benchmark setting.

- **strength**: The main evaluation reports a sizeable improvement over the listed baselines on the full benchmark.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: Interface ablations provide direct evidence that editing guardrails and feedback help performance on the Lite set.
  - Page 7 · citation: exact
  - Quote: "This intervention improves performance considerably (Without Linting, 15.0% ↓ 3.0)."

- **limitation**: The reported experiments use two leading language models, so evidence for broader model generality is limited.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **uncertainty**: Configuration selection included qualitative development examples and a hyperparameter sweep; the inspected pages do not establish how robust results are to alternative selection procedures or broader task distributions.
  - Page 5 · citation: whitespace
  - Quote: "we arrived at the final ACI design through qualitative analysis of system behavior on small set of hand-picked easier examples"

Unresolved questions:

- How well does the ACI transfer to other model families, programming languages, and repository/task distributions?
- How sensitive are results to alternative development-set selection procedures and evaluation budgets?
- I inspected pages 1 and 3–7, not the remainder of the paper; further analyses, caveats, or limitations may change this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated limitations to assess scope and caveats. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect method, benchmark evaluation, and ACI design evidence. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Check main comparative results and ablation evidence for strength and experimental support. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Evidence from the abstract and inspected methods/results supports an assessment; note limited pages reviewed. | review accepted | [event 20](trace.jsonl#L20) |
