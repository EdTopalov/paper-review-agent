# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**pyagent_react · ok**

5 model calls · 4 reads · 11.19 s · $0.001690

5 decisions · 5 tool calls · 32892 input tokens (23891 cached) · 652 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.57

CAMEL presents a prompting framework for two language-model agents to cooperate in an assistant–user role-play, along with procedures for generating and analyzing large conversational datasets. It is useful as an exploratory framework and data-generation contribution, but its evidence establishes conversation-level behaviors and termination patterns more clearly than the correctness or real-world usefulness of completed tasks.

- **strength**: The work operationalizes the role-play setup and reports dataset scale: 25,000 AI Society conversations and 50,000 Code conversations.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **strength**: Prompt ablations provide evidence that design choices affect termination behavior, while also surfacing a countervailing increase in unproductive replies.
  - Page 12 · citation: normalized
  - Quote: "both modifications considerably increases the number of conversations that terminate with end of task token"

- **limitation**: The authors explicitly identify task-completion evaluation as a major constraint, so the dataset scale should not be mistaken for demonstrated task quality.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

Unresolved questions:

- How often do agents actually complete tasks correctly, as judged by qualified human evaluators, across the generated task range?
- How robust are the reported behaviors to different underlying models, prompt formulations, or interaction settings?
- I inspected the supplied first page and pages 2–14, not the remaining paper or supplemental materials; detailed evidence elsewhere, including additional analyses, may affect this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed agent framework and how its operation is evaluated. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 12, "end": 14}` | Inspect dataset scale, evaluation evidence, and reported outcomes. | read pages [12, 13, 14] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Check model setup, dataset quantities, and empirical support for scalability claims. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect model selection and experimental procedure before assessing the evidence. | read pages [6, 7] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.57, "observations": 3}}` | Submit a balanced assessment grounded in observed framework, dataset, and limitation passages. | review accepted | [event 26](trace.jsonl#L26) |
