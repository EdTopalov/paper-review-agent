# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

5 model calls · 4 reads · 9.29 s · $0.001590

5 decisions · 5 tool calls · 25831 input tokens (16812 cached) · 621 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-agent’s central contribution is to treat the agent-computer interface as a design variable: it provides LM-oriented repository search, file viewing/editing, and feedback rather than relying on a human-oriented shell. On the reported SWE-bench evaluation, it substantially outperforms the paper’s interactive shell baseline, and ablations support the importance of several interface choices. The results are meaningful but bounded by the evaluated models, benchmark composition, and development process.

- **strength**: The paper reports strong benchmark performance and transfer across two tested models, with full-set evaluation for GPT-4 Turbo.
  - Page 2 · citation: whitespace
  - Quote: "SWE-agent solves 12.5% of the 2,294 SWE-bench test issues"

- **strength**: The ablation comparisons provide evidence that interface components matter, including linting and editing choices, rather than attributing the gain only to the overall system.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The empirical scope is concentrated on two large-context closed models and a benchmark of Python repositories; broad generalization beyond this setup is not established here.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **uncertainty**: The ACI was refined partly through qualitative inspection of a small, hand-picked development set; the inspected evidence does not establish how sensitive the design conclusions are to that selection or development process.
  - Page 5 · citation: exact
  - Quote: "qualitative analysis of system behavior on small set of hand-picked easier examples"

Unresolved questions:

- How well do the ACI design principles transfer to other model families, programming languages, and software engineering tasks beyond the studied benchmark?
- How sensitive are the selected interface configuration and reported gains to the hand-picked development examples and the benchmark's repository/task mix?
- I inspected pages 1–3 and 5–8 plus search snippets, not the full paper; details in other sections and appendices may qualify these findings.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope and limitations for a balanced assessment. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect method and ACI design details underlying the claimed contribution. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Check quantitative results and ablation evidence for strength and scope. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 8}` | Inspect further analysis or stated failure boundaries before finalizing. | read pages [7, 8] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | The observed methods, benchmark results, ablations, and behavior analysis suffice for an evidence-based review; note inspected-page limits. | review accepted | [event 25](trace.jsonl#L25) |
