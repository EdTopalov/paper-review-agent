# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**agent · ok**

5 model calls · 4 reads · 10.00 s · $0.001724

5 decisions · 5 tool calls · 26262 input tokens (15835 cached) · 557 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.64

CAMEL introduces a prompt-based two-agent role-playing framework that turns a human’s preliminary idea into task-oriented conversations and releases generated AI Society and Code datasets. Its most defensible contribution is a practical, scalable method and an analysis of recurring coordination failures and prompt variations, rather than validated autonomous task-solving performance.

- **strength**: The framework gives the two agents complementary user/assistant roles and automates task specification and turn-taking, providing a concrete setup for studying cooperation.
  - Page 4 · citation: exact
  - Quote: "a task-speciﬁer agent will provide a detailed description to make the idea speciﬁc"

- **strength**: The paper reports sizable generated corpora and analyzes termination behavior and prompt changes, offering useful empirical characterization of the pipeline.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations"

- **limitation**: The central task-completion capability is not established by systematic expert evaluation; the authors identify this evaluation challenge themselves.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts"

- **limitation**: The demonstrated scope is limited to a two-agent cooperative setting, and the paper acknowledges that its coverage of AI society is preliminary.
  - Page 13 · citation: whitespace
  - Quote: "this work only touches the tip of the iceberg of the AI society"

Unresolved questions:

- How often do the generated conversations produce correct, useful task outcomes under domain-expert assessment?
- How robust are the findings to different base models, prompt settings, and multi-agent or non-cooperative scenarios?
- I inspected the opening, methodology and selected dataset-analysis/conclusion pages, but not all figures, supplemental materials, or the full evaluation details; those could clarify quantitative effect sizes and reproducibility.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s stated scope limits to assess contribution fairly. | 4 matches on pages [1, 13, 21] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect framework design and setup for substantive methodological details. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review experimental results and evidence for the claimed agent behavior and generated datasets. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 13}` | Inspect quantitative analysis, conclusions, and authors’ explicit limitations. | read pages [11, 12, 13] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.64, "observations": 4}}` | Evidence reviewed includes framework, dataset construction, analysis and stated limits; submit an evidence-based reading-club assessment. | review accepted | [event 25](trace.jsonl#L25) |
