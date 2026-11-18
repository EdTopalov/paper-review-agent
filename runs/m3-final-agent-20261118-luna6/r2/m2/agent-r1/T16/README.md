# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**agent · ok**

6 model calls · 5 reads · 17.82 s · $0.002829

6 decisions · 6 tool calls · 36268 input tokens (17234 cached) · 592 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

CAMEL presents a practical role-playing and inception-prompting framework for having two LLM agents generate task-oriented conversations from a minimal human idea. Its main value is a reusable experimental setup, two large generated datasets, and a concrete catalog of cooperation failures; claims about autonomous task-solving remain preliminary because task completion was not validated at scale.

- **strength**: The framework makes its agent roles and interaction procedure explicit, and packages the approach for reuse.
  - Page 2 · citation: whitespace
  - Quote: "Our library, which we make publicly available, provides modular functionality, implementations of different agents, well-crafted prompts, and data explorers"

- **strength**: The authors generate datasets at substantial scale and examine how prompt changes affect termination outcomes, rather than relying only on illustrative conversations.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations"

- **limitation**: The paper identifies common breakdowns in role-play, and the reported termination pattern shows these issues are not merely hypothetical.
  - Page 12 · citation: whitespace
  - Quote: "the main termination reasons for AI Society dataset is Assistant Instruct whereas for Code it is Token Limit"

- **limitation**: Whether generated conversations actually complete tasks is not established at scale; the authors identify expert evaluation as a major obstacle.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts"

Unresolved questions:

- How often do conversations judged complete produce correct, useful task outcomes under domain-expert evaluation?
- How well do the framework and its findings transfer beyond two cooperating agents and the particular model/API setting?
- The inspected pages did not include the complete figures and supplemental materials; finer-grained dataset quality and failure-rate evidence therefore remains uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s explicit scope and limitations for balanced assessment. | 4 matches on pages [1, 13, 21] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect framework design and stated methodological contributions beyond the abstract. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review experimental setup and evidence for generated datasets and agent performance. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 13}` | Inspect reported analyses and authors’ explicit limitations and future work. | read pages [11, 12, 13] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "GPT-3.5"}` | Check the reported model and experimental implementation details for context. | 1 matches on pages [12] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Evidence inspected covers the framework, dataset scale, observed failure modes, prompt ablation findings, and stated evaluation limitations; submit a balanced review. | review accepted | [event 31](trace.jsonl#L31) |
