# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 8.72 s · $0.000468

1 decisions · 0 tool calls · 23392 input tokens (23389 cached) · 468 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.56

CAMEL presents a prompt-based framework in which two LLM agents take complementary assistant and user roles to turn an initial idea into a task and produce a multi-turn conversation. It contributes a practical data-generation pipeline and two sizable conversational datasets, while documenting recurring coordination failures and prompt ablations. The evidence is primarily descriptive: the paper demonstrates generation and analyzes termination patterns, but does not establish the quality of task completion or the datasets’ value for downstream training.

- **strength**: The framework makes the interaction protocol and termination behavior concrete, and the paper identifies recognizable failure modes rather than treating autonomous cooperation as solved.
  - Page 6 · citation: whitespace
  - Quote: "The prompt designs for both roles are crucial to achieving autonomous cooperation between agents."

- **strength**: The work reports a scalable generation effort, with 25,000 AI Society and 50,000 Code conversations, alongside analysis of termination and prompt variants.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **limitation**: The authors explicitly acknowledge that they cannot evaluate task completion at scale; dataset size and breadth therefore should not be read as evidence of solution quality.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The included trading example illustrates a consequential quality concern: it presents a rudimentary, potentially unsafe trading function as a working solution, while the paper does not provide systematic task-quality evaluation in the inspected pages.
  - Page 26 · citation: not_found
  - Quote: "if sentiment_result > 0.5 and current_price > 0 and available_money > 0:"

Unresolved questions:

- How often do generated conversations provide correct, complete, and safe task solutions, under expert or other reliable evaluation?
- Do the datasets improve downstream models or analyses compared with existing instruction data, and how robust are such effects to changes in model, prompt, and sampling?
- What are the precise generation and filtering procedures, and how representative are the reported termination and prompt-ablation results? I inspected the supplied pages, including the main experiments and selected appendix examples, but not the underlying dataset or implementation details beyond what is stated here.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
