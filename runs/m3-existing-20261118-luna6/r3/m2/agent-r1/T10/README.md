# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

4 model calls · 3 reads · 9.25 s · $0.001515

4 decisions · 4 tool calls · 19791 input tokens (10746 cached) · 580 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-agent’s central contribution is a language-model-tailored agent-computer interface for repository navigation, editing, feedback, and context management. On SWE-bench it reports a sizable improvement over the listed RAG and shell-only baselines, with Lite-set interface ablations that support the claim that interface choices matter. Evidence is promising but bounded to two leading closed models, Python repositories, and a development-guided design process.

- **strength**: The paper identifies concrete ACI design principles and tests alternatives; the Lite ablations report notable sensitivity to search and editing design, including linting and feedback.
  - Page 7 · citation: whitespace
  - Quote: "Without SWE-agent’s file editor interface, performance drops to (10.3% ↓ 7.7)."

- **strength**: The reported full-set result is a substantial benchmark result relative to the baselines shown, and the paper also reports performance on the Lite subset.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **limitation**: Model coverage is narrow: the reported experiments and ablations center on two leading models, restricting what the evidence establishes about generality across model families.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **uncertainty**: Final interface design used qualitative analysis on hand-picked easier development examples, which raises an unanswered question about sensitivity to example selection; the inspected passages do not establish the effect of this process on test performance.
  - Page 5 · citation: exact
  - Quote: "qualitative analysis of system behavior on small set of hand-picked easier examples"

Unresolved questions:

- How robust are the ACI gains across a broader range of models and non-Python repositories?
- How sensitive is the final design and its measured gain to the hand-picked development examples and budget/configuration choices?
- I inspected pages 3–7 and a literal search result on limitations; I did not inspect the remainder of the paper, including any further limitations or expanded results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s explicit scope and limitations discussion. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect method details and reported benchmark evidence for the central contribution. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Review comparative results and interface ablations supporting the claimed performance gains. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | The observed method, benchmark, ablations, and model scope provide enough evidence for a qualified assessment. | review accepted | [event 20](trace.jsonl#L20) |
