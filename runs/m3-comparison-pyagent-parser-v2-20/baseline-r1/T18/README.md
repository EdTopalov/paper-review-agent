# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 7.66 s · $0.002495

1 decisions · 0 tool calls · 17424 input tokens (0 cached) · 635 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

Gorilla combines instruction fine-tuning of a LLaMA-7B model with API-document retrieval, and introduces APIBench for evaluating API-call selection across three ML model hubs. On the reported benchmark, Gorilla often improves over prompted baseline models, especially without retrieval, and retrieval-aware training supports examples of adapting to changed documentation. The work is useful as a systematic study, but its evidence mainly concerns selecting API calls under a dataset-based proxy rather than whether generated calls execute correctly or generalize to unseen APIs.

- **strength**: The paper contributes a concrete benchmark and training setup, and reports broad comparisons across API hubs and retriever settings. Its results also show that retrieval is not uniformly beneficial, a useful qualification to the main claim.
  - Page 7 · citation: whitespace
  - Quote: "The result illustrates that adding a non-optimal retriever at test time will sometime misguide the model and result in more errors."

- **limitation**: The reported correctness measure matches generated calls to dataset API entries using selected AST nodes and arguments. The paper explicitly says it does not test execution results, so functional correctness in actual use is not established by this evaluation.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **uncertainty**: The described holdout splits instruction–API pairs, but the supplied text does not establish whether any APIs themselves are held out. This leaves open how much the results demonstrate generalization to new APIs rather than new prompts for known APIs.
  - Page 6 · citation: whitespace
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

Unresolved questions:

- How well does Gorilla select or correctly call APIs that were not represented during fine-tuning?
- Do the generated calls execute successfully and satisfy the user's intent, beyond matching a reference API under the AST-based metric?
- How reliably do retrieval-aware results hold with realistic, imperfect or changing documentation at larger API-catalog scale?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
