# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 7.49 s · $0.003211

1 decisions · 0 tool calls · 23392 input tokens (0 cached) · 575 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

CAMEL presents a prompt-driven framework for two language-model agents to role-play an assistant–user collaboration, along with procedures for generating and analyzing 25,000 AI Society and 50,000 Code conversations. Its main value is a practical, inspectable setup and a catalog of coordination failures, rather than evidence that agents reliably complete useful tasks. The authors explicitly note that evaluating task completion at this scale is difficult.

- **strength**: The paper gives a concrete, reusable interaction protocol: roles, instruction/solution formats, and a completion token are specified, and the framework is made available as a library.
  - Page 6 · citation: whitespace
  - Quote: "Our Inception prompt consists of three prompts: the task speciﬁer prompt PT , the assistant system prompt PA, and the user system prompt PU."

- **strength**: The large generated corpora and documented termination outcomes provide a useful exploratory artifact and make coordination failures visible, rather than presenting autonomous cooperation as solved.
  - Page 9 · citation: not_found
  - Quote: "we generated 50 assistant roles, 50 user roles, and 10 tasks for each combination of roles yielding a total of 25,000 conversations."

- **limitation**: The paper acknowledges that it does not establish task-completion quality at scale; dataset volume and termination categories are not substitutes for domain-expert assessment.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The included harmful example demonstrates a serious safety failure of the prompted setup: it supplies actionable intrusion and persistence guidance despite a prompt instructing the assistant to decline harmful or illegal requests.
  - Page 30 · citation: whitespace
  - Quote: "We can create fake login pages or phishing emails that appear to be from trusted sources"

Unresolved questions:

- How often do conversations produce correct, useful, and complete task outcomes, as judged by qualified human evaluators, across the generated datasets?
- How robust are the reported prompt effects to different models, sampling settings, and repeated runs? The inspected pages report experiments with two gpt-3.5-turbo agents, but do not establish broader model generality.
- What safeguards or filtering procedures, if any, can reduce harmful outputs in generated conversations? The paper’s harmful example raises this question, but the inspected material does not demonstrate an effective mitigation.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
