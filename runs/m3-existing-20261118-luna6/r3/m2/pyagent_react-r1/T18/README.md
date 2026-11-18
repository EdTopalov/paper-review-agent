# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

5 model calls · 3 reads · 18.97 s · $0.002034

5 decisions · 4 tool calls · 29899 input tokens (19681 cached) · 1121 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

Gorilla combines instruction fine-tuning of a LLaMA-7B model with retrieval-aware training for selecting and generating ML API calls. The paper contributes APIBench and an AST-based evaluation, and reports gains over prompted baselines in several settings. Its results also show that retrieval quality can substantially change performance. The evidence supports a useful, focused contribution, but the benchmark’s synthetic instruction split and narrow API-call evaluation leave broader generalization and practical execution unresolved.

- **strength**: The paper assembles a sizable benchmark spanning three model hubs and reports a held-out evaluation, providing a concrete testbed for API-call generation.
  - Page 4 · citation: exact
  - Quote: "a total of 10 instruction-api pairs"

- **strength**: On the reported zero-shot benchmark, Gorilla scores above GPT-4 across all three hubs; the paper also reports gains with oracle retrieval.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The holdout is formed by splitting generated instruction–API pairs, so the reported setup does not establish generalization to unseen APIs or independently authored user requests.
  - Page 6 · citation: whitespace
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

- **uncertainty**: The documentation-change evidence inspected is presented through illustrative examples, not quantitative evaluation of adaptation across a broader set of changes.
  - Page 8 · citation: exact
  - Quote: "Figure 6: Gorilla’s retriever–aware training enables it to react to changes in the APIs."

Unresolved questions:

- How well does the approach perform on real user requests and APIs absent from training, rather than held-out generated instructions for the collected API set?
- How do the reported documentation-change examples generalize across a larger, systematically evaluated set of documentation updates?
- How often do generated calls execute successfully and satisfy user intent in an end-to-end tool-use setting?
- I inspected pages 1–10, not the remainder of the paper; details or evidence elsewhere may qualify these questions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed model, dataset construction, and evaluation setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect retrieval training details and quantitative comparisons. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 10}` | Inspect test-time documentation-change experiments and stated scope limitations. | read pages [8, 9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Submit an evidence-based assessment using the inspected methods, results, and limitations pages. | review accepted | [event 25](trace.jsonl#L25) |
