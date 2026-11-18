# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**agent · ok**

5 model calls · 4 reads · 9.64 s · $0.001639

5 decisions · 5 tool calls · 28982 input tokens (19716 cached) · 598 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

CAMEL proposes an inception-prompted role-playing setup in which AI user and assistant agents collaborate on tasks, and releases large generated conversation datasets for studying these interactions. Its contribution is a useful, reproducible-looking research framework and descriptive analysis of cooperation failures, but evidence for task competence or generality is limited: the evaluation primarily characterizes generated conversations and termination behavior, rather than independently establishing task success.

- **strength**: The paper clearly specifies a practical cooperative-agent setup and prompt structure, making its method concrete enough to study and extend.
  - Page 4 · citation: whitespace
  - Quote: "a task-speciﬁer agent will provide a detailed description to make the idea speciﬁc and then the AI assistant and AI user will cooperate on completing the speciﬁed task through multi-turn conversations until the AI user determines the task is done."

- **strength**: The work demonstrates generation at substantial scale for two task-oriented corpora, supporting its data-generation contribution.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **limitation**: The authors explicitly identify the difficulty of evaluating whether generated conversations actually complete diverse tasks, limiting claims about capability.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The empirical analysis inspected reports termination distributions and prompt ablations, but does not establish task quality through expert assessment in the passages reviewed.
  - Page 12 · citation: exact
  - Quote: "We provide an ablation study of the AI Society dataset."

Unresolved questions:

- How often do the conversations produce correct, useful task outcomes under independent domain-expert evaluation?
- How robust are the findings across models, prompt variations, and settings with more than two agents?
- I inspected pages 1–4 and 7–13; I did not inspect the remaining paper or supplementary materials, so other evaluations or caveats may be present.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed framework and its method details to assess contribution and evidence. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "limitations"}` | Find the authors’ stated limitations to distinguish scope boundaries from unresolved concerns. | 4 matches on pages [1, 13, 21] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect experiment design and reported results supporting the claimed scale and utility. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 13}` | Check analysis results, evaluation basis, and author-identified limitations before scoring. | read pages [11, 12, 13] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Sufficient inspected evidence supports an assessment of the framework, dataset-scale demonstration, and evaluation limitations. | review accepted | [event 25](trace.jsonl#L25) |
