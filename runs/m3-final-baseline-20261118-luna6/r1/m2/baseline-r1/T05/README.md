# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 7.14 s · $0.000451

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 569 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

WebArena contributes a self-hostable, interactive web environment and an 812-task benchmark for evaluating natural-language agents by task outcomes rather than matching action traces. Its combination of multiple web applications, tools, user roles, and programmatic checks makes it a useful testbed for long-horizon web interaction; baseline results also illustrate substantial difficulty. Evidence in the supplied pages is strongest for the environment and benchmark design, with important uncertainties around evaluation reliability and how broadly the benchmark represents real-world web use.

- **strength**: The benchmark targets outcome correctness, allowing different valid action paths, and includes programmatic checks of resulting states.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences [25, 7] but also accommodates a range of potential valid paths"

- **strength**: The environment is designed for reproducible local evaluation, with self-contained sites and reset support.
  - Page 16 · citation: whitespace
  - Quote: "The Docker images are fully self-contained with all the code of the website, database, as well as any other software dependencies."

- **limitation**: The evaluation reports only modest success for the tested agents, and reasoning offers little improvement over direct action prediction with GPT-3.5.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3.5 reasoning agent outperforms the direct agent only by successfully completing a marginal number of examples."

- **uncertainty**: The authors describe a broad realism goal, but site selection was grounded in a small, author-specific sample of browsing histories; how representative this is of users generally remains unclear.
  - Page 3 · citation: whitespace
  - Quote: "we first conducted an analysis of approximately 200 examples from the authors’ actual web browser histories."

Unresolved questions:

- How reliable are the programmatic and language-model-based evaluation functions across paraphrases, ambiguous intents, and edge cases? The supplied pages describe the methods but do not provide a systematic validation of evaluator accuracy.
- How well do benchmark performance and task coverage generalize beyond the selected sites, sampled data, northeast-US map scope, and author-derived browsing examples?
- The supplied pages do not include detailed per-category results or a broader set of agent approaches; would conclusions about agent weaknesses persist under different models, interfaces, or training setups?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
