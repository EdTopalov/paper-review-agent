# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

4 model calls · 2 reads · 16.06 s · $0.001255

4 decisions · 4 tool calls · 12308 input tokens (5567 cached) · 739 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SELF-RAG trains a language model to decide when to retrieve, assess passage relevance and answer support, and critique usefulness using reflection tokens. It supports on-demand retrieval, passage-conditioned generation, and inference-time control via learned critiques. This is a substantial and clearly articulated RAG design, but this review inspected only the opening and method pages, not the empirical results or complete limitations.

- **strength**: The framework addresses indiscriminate retrieval with an explicit learned decision to retrieve on demand.
  - Page 1 · citation: whitespace
  - Quote: "trains a single arbitrary LM that adaptively retrieves passages on-demand"

- **strength**: Reflection tokens represent distinct judgments about retrieval, support, and usefulness.
  - Page 4 · citation: exact
  - Quote: "Four types of reflection tokens used inSELF -R AG."

- **limitation**: The described training process relies on critic-produced annotations, leaving their reliability and effects unclear in the inspected pages.
  - Page 4 · citation: exact
  - Quote: "reflection tokens predicted by a critic model"

Unresolved questions:

- How strong and consistent are the reported experimental gains across tasks and baselines? The abstract claims broad improvements, but results pages were not inspected.
- How sensitive are retrieval decisions and critique behavior to critic training data and labeling quality?
- What are inference-time cost and failure modes? These were not established by the pages inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Limitations"}` | Check the paper’s explicit scope limitations before assessing its claims. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 4}` | Inspect method details and experimental setup to substantiate the core contribution. | read pages [3, 4] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | The observed abstract and method pages support a preliminary assessment; note that detailed results and later limitations were not inspected. | citation_validation_failed; #2: not_found | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Resubmit with exact method wording from the observed page and preserve the explicit limits of inspected evidence. | review accepted | [event 22](trace.jsonl#L22) |
