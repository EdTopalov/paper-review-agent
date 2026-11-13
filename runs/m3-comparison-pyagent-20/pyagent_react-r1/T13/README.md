# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

4 model calls · 2 reads · 14.33 s · $0.002053

4 decisions · 3 tool calls · 17080 input tokens (5777 cached) · 1166 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

Self-RAG trains a language model to decide when retrieval is useful, generate with retrieved passages, and emit reflection tokens that assess passage relevance, support, and answer utility. Its central contribution is integrating these decisions into a controllable generation process and reporting broad task evaluations; the inspected evidence also indicates reliance on model-generated supervision and limited human evaluation.

- **strength**: The inference procedure makes retrieval conditional and uses relevance, support, and utility signals to guide selection among passage-conditioned outputs.
  - Page 4 · citation: exact
  - Quote: "Rank yt based on ISREL , ISSUP , ISUSE"

- **strength**: The training pipeline distills reflection-token judgments from GPT-4 into a critic, then uses that critic to construct training data for the generator.
  - Page 5 · citation: whitespace
  - Quote: "We create supervised data by prompting GPT-4 to generate reflection tokens and then distill their knowledge into an in-houseC."

- **limitation**: The reported human assessment is small and excludes some outputs from the plausibility-and-support analysis, limiting what that evaluation establishes.
  - Page 10 · citation: whitespace
  - Quote: "we sampled 50 samples from PopQA and Bio results."

- **limitation**: The paper explicitly acknowledges that improved factuality and citation metrics do not ensure every output is supported by its citations.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations."

Unresolved questions:

- How robust are retrieval decisions and critique tokens when the critic's labels are wrong or the test domain differs from the training data?
- How do latency and retrieval costs compare with conventional RAG at matched quality?
- I inspected pages 1, 4–5, and 10–12 only; detailed benchmark tables, comparisons, and the full appendix were not examined, so the breadth and statistical strength of the reported results remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect the training method and reflection-token design. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark results and stated evaluation scope. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit a balanced assessment based on the inspected method, training, evaluation, and ethics pages. | review accepted | [event 21](trace.jsonl#L21) |
