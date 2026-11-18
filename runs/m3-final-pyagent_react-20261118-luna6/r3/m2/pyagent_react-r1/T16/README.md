# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**pyagent_react · ok**

6 model calls · 4 reads · 18.15 s · $0.002279

6 decisions · 6 tool calls · 47265 input tokens (36834 cached) · 1215 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

CAMEL proposes a prompt-driven assistant–user role-playing framework in which two language-model agents collaborate on tasks, and uses it to generate AI Society and Code conversation datasets. Its useful contribution is a concrete workflow and a candid taxonomy of cooperation failures, with preliminary prompt ablations. Evidence supports dataset generation and analysis more directly than task-solving capability or broad claims about autonomous cooperation; expert evaluation of task completion is explicitly left open.

- **strength**: The paper specifies a usable interaction protocol, including roles, message formats, and a task-completion token, making the framework concrete enough to inspect and extend.
  - Page 6 · citation: whitespace
  - Quote: "Once the conversation phase commences, the AI assistant and AI user prompt each other automatically in a loop until termination."

- **strength**: The authors report generating two sizeable datasets from model-generated task parameters, supporting the proposed workflow’s ability to produce conversational data at scale.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **limitation**: The paper identifies recurring failure modes and describes termination rules, but these controls do not themselves demonstrate that conversations successfully solve their tasks.
  - Page 12 · citation: whitespace
  - Quote: "the main termination reasons for AI Society dataset is Assistant Instruct whereas for Code it is Token Limit ."

- **uncertainty**: The authors acknowledge that task-completion evaluation was not established; consequently, the evidence inspected does not establish the quality or correctness of generated solutions across domains.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

Unresolved questions:

- How often do conversations produce correct, useful task outcomes when judged by independent domain experts?
- How robust are the framework and prompt ablations across model versions, alternative providers, or tasks outside the two reported scenarios?
- What proportion of generated conversations contain substantive instruction–solution pairs rather than role errors, incomplete work, or token-limit terminations?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed role-playing framework and its stated contributions. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 11, "end": 13}` | Inspect dataset generation and the paper's empirical evaluation. | read pages [11, 12, 13] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect experimental scale, dataset construction, and reported evidence. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 7}` | Check model and generation settings relevant to interpreting the reported dataset results. | read pages [6, 7] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Submit an assessment grounded in the inspected framework, dataset, and evaluation passages. | citation_validation_failed; #1: not_found | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Replace the unverified page 6 excerpt with its exact observed wording. | review accepted | [event 31](trace.jsonl#L31) |
