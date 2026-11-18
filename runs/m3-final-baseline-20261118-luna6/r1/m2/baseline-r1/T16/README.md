# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 6.90 s · $0.000498

1 decisions · 0 tool calls · 23392 input tokens (23389 cached) · 528 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

CAMEL proposes a prompt-driven, two-agent role-playing framework in which an AI “user” plans and instructs while an AI assistant executes, and uses it to generate 25,000 AI Society and 50,000 Code conversations. Its contribution is a practical framework, dataset-generation pipeline, and qualitative account of cooperation failures, rather than validated evidence that agents reliably complete useful tasks. The paper itself flags the central gap: it does not evaluate task completion at scale, and its examples expose safety and output-quality concerns.

- **strength**: The framework is specified concretely through distinct roles, task generation, interaction format, and termination rules, making the setup reproducible in principle.
  - Page 6 · citation: not_found
  - Quote: "Our Inception prompt consists of three prompts: the task speciﬁer prompt PT, the assistant system prompt PA, and the user system prompt PU."

- **strength**: The paper does more than present a proposed method: it reports large generated datasets and identifies recurring interaction failure modes, including termination behavior and prompt ablations.
  - Page 9 · citation: not_found
  - Quote: "we generated 50 assistant roles, 50 user roles, and 10 tasks for each combination of roles yielding a total of 25,000 conversations."

- **limitation**: Task completion is not systematically validated; the authors acknowledge that evaluation at the claimed scale would require domain experts. This limits evidence for the framework’s practical effectiveness.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The paper’s own harmful example shows that the prompts’ stated refusal and alignment safeguards do not reliably prevent dangerous assistance in the demonstrated scenario.
  - Page 30 · citation: whitespace
  - Quote: "I suggest using a combination of social engineering and hacking techniques."

Unresolved questions:

- How often do generated conversations actually solve their specified tasks, as judged by suitable domain experts, and how does performance vary by domain?
- How robust are the reported outcomes across model versions, repeated runs, and alternative prompt formulations? The reported experiments use two gpt-3.5-turbo agents.
- What safeguards or data-filtering procedures, if any, can reduce the harmful or low-quality material in generated conversations before release or reuse?
- I inspected the supplied pages, including the main experiments, conclusion, and selected supplementary examples; I did not inspect the contents of Figures 7–13 beyond their captions and therefore cannot assess the underlying distributions or cartography in detail.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
