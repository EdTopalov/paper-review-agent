# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

5 model calls · 2 reads · 15.17 s · $0.001964

5 decisions · 4 tool calls · 21372 input tokens (11017 cached) · 1119 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

Self-RAG trains a language model to decide when to retrieve, assess passage relevance and output support, and use reflection tokens to guide generation and selection. The inspected pages describe a coherent, controllable approach to retrieval-augmented generation, but I did not inspect the experimental results or later sections, so the paper’s empirical support and limitations remain uncertain.

- **strength**: The framework combines retrieval decisions and generation critique in one model, allowing retrieval to be invoked on demand rather than indiscriminately.
  - Page 1 · citation: whitespace
  - Quote: "adaptively retrieves passages on-demand"

- **strength**: The method specifies separate reflection signals for retrieval, relevance, support, and usefulness, giving its control mechanism a concrete structure.
  - Page 4 · citation: exact
  - Quote: "Four types of reflection tokens used inSELF -R AG."

- **uncertainty**: The overview reports broad task improvements, but I did not inspect the evaluation design, comparisons, or results tables; the strength of this evidence is therefore not established here.
  - Page 2 · citation: exact
  - Quote: "Empirical results on six tasks"

Unresolved questions:

- How robust are the reported gains across the six tasks, baselines, and evaluation measures?
- How reliable are the critic-generated reflection labels, and how sensitive is performance to errors in those labels?
- What are the retrieval and decoding costs in practice, and how do they compare with the claimed quality gains?
- I inspected only pages 1–4 and searched for the literal term “limitations,” which returned no matches. I did not inspect the remaining paper, so important evidence, caveats, and scope boundaries may be present elsewhere.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the method and evaluation evidence. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Locate the paper’s explicit scope limitations. | 0 matches | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.63, "observations": 3}}` | Submit a provisional assessment based on the inspected overview and method pages. | citation_validation_failed; #2: not_found; #3: not_found | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.63, "observations": 3}}` | Resubmit using short verbatim excerpts from the inspected pages. | review accepted | [event 27](trace.jsonl#L27) |
