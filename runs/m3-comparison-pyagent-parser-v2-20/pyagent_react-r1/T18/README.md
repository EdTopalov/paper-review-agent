# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

4 model calls · 2 reads · 10.99 s · $0.001302

4 decisions · 3 tool calls · 12322 input tokens (5233 cached) · 728 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines fine-tuning with retrieval-aware training to select and generate calls to APIs, and introduces APIBench spanning three ML model hubs. Results report strong API-call accuracy and lower hallucination in several settings, while examples and constraint experiments explore test-time documentation changes and constraint-aware selection. The work offers a useful pipeline and benchmark, but the evidence inspected here is confined to ML APIs and leaves key evaluation details and the breadth of change-adaptation testing unresolved.

- **strength**: The comparison reports substantial gains from an oracle retriever for Gorilla on two hubs, with low reported hallucination rates.
  - Page 8 · citation: exact
  - Quote: "HuggingFace (overall)↑ 71.68 11.28 28.10 45.58 0 17.04 47.46 91.26"

- **strength**: The paper evaluates constraint-aware API selection, including a stated subset restriction and results across models and retrieval settings.
  - Page 9 · citation: whitespace
  - Quote: "For Table 3, we filtered a subset of the Torch Hub dataset that had accuracy defined for at least one- dataset in its model card (65.26% of TorchHub dataset in Table 1)."

- **limitation**: The authors explicitly delimit the benchmark to ML APIs; transfer to other API domains is not established by the inspected evidence.
  - Page 9 · citation: whitespace
  - Quote: "With the goal of wanting to have a challenging dataset, we chose ML APIs, given their functional similarity."

- **uncertainty**: The documentation-change section provides illustrative cases, but the inspected pages do not establish how broadly or quantitatively adaptation was tested.
  - Page 8 · citation: whitespace
  - Quote: "For instance, consider the scenario illustrated in Figure 6, where the training of Gorilla has al- lowed it to react effectively to changes in APIs."

Unresolved questions:

- How were the evaluation examples, train/test splits, and API overlap controlled, and how sensitive are results to those choices?
- How often and across what range of documentation changes does retrieval-aware adaptation work beyond the illustrated examples?
- Do the reported gains transfer to non-ML APIs or real API execution outcomes?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | search_paper `{"query": "APIBench"}` | Locate the dataset and evaluation evidence. | 3 matches on pages [1, 2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect quantitative results and evaluation details. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using the inspected results and stated scope. | review accepted | [event 21](trace.jsonl#L21) |
