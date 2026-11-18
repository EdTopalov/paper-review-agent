# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 11.68 s · $0.000521

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 693 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

Gorilla presents an API-call benchmark built from three ML model hubs and fine-tunes a LLaMA-based model to select and format API calls, optionally using retrieved documentation. Results show strong performance on the authors’ AST-based benchmark and illustrate adaptation to documentation changes. The work is useful as an early systematic study of API selection, though its evaluation primarily measures matching API identifiers and arguments rather than whether generated calls execute successfully or accomplish the requested task.

- **strength**: The paper contributes a sizable, structured dataset and evaluates several model and retrieval configurations across three API sources.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls."

- **limitation**: The reported holdout is split at the instruction–API-pair level. Whether API identities are held out is not established, so the results may primarily measure generalization to new prompts for APIs represented in training.
  - Page 6 · citation: whitespace
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

- **limitation**: The core metric checks AST matches against the collected API dataset, not end-to-end execution or task success; the appendix explicitly says execution results were not tested.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **uncertainty**: The documentation-change examples illustrate plausible adaptation, but the supplied results do not establish how reliably this works across a broader set of changes or with imperfect retrieval.
  - Page 8 · citation: exact
  - Quote: "For instance, consider the scenario illustrated in Figure 6"

Unresolved questions:

- How well does Gorilla generalize to APIs that are entirely absent from its training set, rather than to new instructions for APIs seen during training?
- Do generated calls execute successfully and satisfy users’ requested tasks when evaluated end to end?
- How robust is adaptation to documentation updates when the retriever returns incomplete, stale, or irrelevant material?
- The supplied paper is an early preprint; its reported measurements and implementation details are assessed as presented, not independently verified.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
