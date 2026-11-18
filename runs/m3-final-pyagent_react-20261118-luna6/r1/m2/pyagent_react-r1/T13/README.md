# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

3 model calls · 1 reads · 27.36 s · $0.001542

3 decisions · 3 tool calls · 13095 input tokens (9436 cached) · 1981 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Self-RAG trains a language model to retrieve selectively, generate in segments, and emit reflection tokens for assessing relevance, support, and output quality. Reflection-guided decoding also enables adjustments to retrieval and generation behavior. The supplied pages establish a coherent design, but do not include detailed results needed to verify comparative performance claims.

- **strength**: The framework addresses fixed retrieval by deciding whether retrieval is useful for a given input.
  - Page 1 · citation: whitespace
  - Quote: "whether retrieval is necessary, or passages are relevant"

- **strength**: Reflection tokens let the model assess its own predictions during generation.
  - Page 2 · citation: whitespace
  - Quote: "uses critique tokens to assess its own predictions after each generated segment"

- **limitation**: The described supervision pipeline relies in part on examples collected by prompting GPT-4.
  - Page 2 · citation: whitespace
  - Quote: "collected by prompting a propriety LM (i.e., GPT-4; OpenAI 2023)."

- **uncertainty**: The supplied pages report comparative results but do not provide quantitative measurements to assess their magnitude or reliability.
  - Page 2 · citation: exact
  - Quote: "Empirical results on six tasks, including reasoning and long-form generation"

Unresolved questions:

- What are the quantitative results, evaluation protocols, and uncertainty estimates for individual tasks and baselines?
- How do decoding choices and reflection-token quality affect performance and inference cost?
- How robust are self-assessments when retrieved evidence is misleading or conflicting?
- Important inspection gap: only pages 1–3 were supplied; detailed methods, experiments, and later limitations were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect the framework and training procedure. | read pages [2, 3] | [event 6](trace.jsonl#L6) |
| 2 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Use the supplied excerpts from pages 1–3 to assess the proposal and state what remains uninspected. | citation_validation_failed; #4: not_found | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Correct the unmatched citation by using a shorter exact excerpt from the supplied page. | review accepted | [event 16](trace.jsonl#L16) |
