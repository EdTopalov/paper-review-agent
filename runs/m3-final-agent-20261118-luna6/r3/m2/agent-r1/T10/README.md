# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

4 model calls · 3 reads · 9.12 s · $0.001522

4 decisions · 4 tool calls · 20003 input tokens (10838 cached) · 562 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-agent’s substantive contribution is its demonstration that an LM-oriented agent-computer interface—especially integrated search, editing, feedback, and linting—can materially improve autonomous issue resolution. On SWE-bench it reports 12.47% resolution with GPT-4 Turbo, and its interface ablations on SWE-bench Lite support the claim that several design choices matter. The evidence is promising but bounded to two leading closed models and a particular benchmark and task setup.

- **strength**: The main benchmark reports a notable improvement over the listed RAG and shell-only baselines, using a large full test set.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **strength**: Interface ablations provide direct evidence for design choices; removing linting reduces Lite performance by three percentage points.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The evaluated model range is narrow: the reported main results and ablations center on two leading LMs, limiting evidence about generality across models.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **uncertainty**: The inspected excerpts do not establish how performance generalizes beyond SWE-bench’s Python repositories and this issue-resolution setup; broader transfer remains unanswered here.
  - Page 5 · citation: whitespace
  - Quote: "2,294 task instances from 12 different repositories of popular Python packages"

Unresolved questions:

- How well do the ACI design principles transfer to other programming languages, repositories, and software engineering tasks?
- Would similar gains hold for a broader range of current and open-weight language models?
- I inspected pages 1 and 3–8 plus search excerpts; I did not inspect the complete paper, appendices, or all experimental details, so uncertainties about evaluation protocol and additional limitations remain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated limitations to evaluate scope and caveats. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Read methods and benchmark setup for evidence supporting the claimed ACI contribution. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect quantitative comparisons and interface ablations to judge empirical strength. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit assessment based on inspected benchmark results, ablations, and explicitly noted coverage gaps. | review accepted | [event 20](trace.jsonl#L20) |
