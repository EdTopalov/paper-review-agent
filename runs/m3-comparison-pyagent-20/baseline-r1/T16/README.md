# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 5.05 s · $0.003199

1 decisions · 0 tool calls · 23392 input tokens (0 cached) · 551 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.57

CAMEL presents a practical role-playing framework for having two language-model agents generate task-oriented conversations with limited human input, alongside prompts, datasets, and an analysis of common interaction failures. Its main value is as an early, inspectable framework and data-generation resource; the paper offers suggestive prompt ablations and concrete failure examples, but does not establish the quality or real-world task success of the generated work.

- **strength**: The framework makes its interaction design unusually explicit: it specifies task generation, role prompts, turn-taking, and termination conditions, making the method understandable and reusable.
  - Page 6 · citation: not_found
  - Quote: "Our Inception prompt consists of three prompts: the task speciﬁer prompt PT, the assistant system prompt PA, and the user system prompt PU."

- **strength**: The paper reports substantial-scale generation for its stated setup and identifies observable failure modes rather than presenting autonomous cooperation as solved.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **limitation**: The authors explicitly state that evaluating task completion at this breadth is difficult and requires domain expertise; thus dataset size and conversation termination do not demonstrate correctness or usefulness of the produced solutions.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The included harmful example demonstrates a serious safety failure in the illustrated setup: the assistant provides actionable offensive guidance despite a prompt instruction to refuse harmful or illegal requests.
  - Page 30 · citation: whitespace
  - Quote: "I suggest using a combination of social engineering and hacking techniques."

Unresolved questions:

- How often do conversations produce correct, complete, and practically useful task outcomes under expert evaluation, and how does this vary across domains?
- How robust are the reported prompt effects across repeated runs, model versions, and alternative model providers?
- Can safety interventions reliably prevent the harmful behavior shown in the appendix without substantially reducing benign task completion?
- This assessment inspected the supplied pages, including the main method, experiment summaries, and illustrative appendices; it did not independently verify the released datasets or library, and the quantitative figures are presented mainly as plots whose underlying measurements are not reproduced in the supplied text.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
