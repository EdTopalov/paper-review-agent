# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**pyagent_react · ok**

5 model calls · 4 reads · 12.49 s · $0.001850

5 decisions · 5 tool calls · 35727 input tokens (25923 cached) · 732 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.57

CAMEL presents a prompt-based framework for two LLM agents to collaborate through assigned user and assistant roles, and uses it to generate large conversational datasets and examine recurring cooperation failures. Its value is as a practical research scaffold and a descriptive exploration of multi-agent prompting, rather than as evidence that agents reliably complete tasks: task completion is not systematically evaluated, and the authors identify this as a limitation.

- **strength**: The work operationalizes the framework at scale, generating two sizable conversation corpora through automated role, task, and domain construction.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **strength**: The paper identifies concrete failure patterns and reports prompt ablations that alter termination outcomes, providing useful descriptive evidence about prompt sensitivity.
  - Page 12 · citation: whitespace
  - Quote: "both modiﬁcations considerably increases the number of conversations that terminate with end of task token"

- **limitation**: The authors explicitly state that task-completion evaluation is difficult and requires domain experts; therefore, generated conversations and termination tokens do not establish task correctness.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **uncertainty**: The inspection covered pages 3–13, not the rest of the paper; the strength of the quantitative analysis and details of its dataset-quality assessment remain uncertain.
  - Page 12 · citation: exact
  - Quote: "We provide an ablation study of the AI Society dataset."

Unresolved questions:

- How often do conversations marked complete produce correct and useful task outcomes under independent domain-expert assessment?
- How robust are the reported prompt effects across models, repeated runs, and task types?
- What dataset-quality checks or filtering procedures are detailed in the uninspected portions of the paper?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect the proposed role-playing framework and its experimental evidence. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect the reported study design, task samples, and evaluation measures. | read pages [8, 9, 10] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 11, "end": 13}` | Inspect quantitative results and any evaluation caveats. | read pages [11, 12, 13] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 7}` | Check the agent prompting procedure and model configuration. | read pages [6, 7] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.57, "observations": 4}}` | Submit an evidence-based assessment using the inspected framework, dataset, and limitation passages. | review accepted | [event 26](trace.jsonl#L26) |
