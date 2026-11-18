# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**pyagent_react · ok**

6 model calls · 3 reads · 23.73 s · $0.002529

6 decisions · 6 tool calls · 47721 input tokens (37984 cached) · 1864 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SELF-RAG trains a language model to decide when retrieval is useful, generate with retrieved passages, and emit reflection tokens to assess relevance, support, and utility. Its inference procedure uses those tokens to guide selection and permits test-time adjustment of retrieval and critique preferences. Reported results across several task types and component ablations support its value, though the inspected human assessment is small and some evaluation evidence is limited in scale.

- **strength**: The method combines adaptive retrieval with token-based critique and makes the critique usable during inference for controllable selection.
  - Page 6 · citation: whitespace
  - Quote: "Generating reflection tokens to self-evaluate its own output makes SELF -RAG controllable during the inference phase"

- **strength**: The paper reports strong comparisons across multiple tasks, while not winning every individual metric.
  - Page 8 · citation: exact
  - Quote: "outperforms existing RAG in many tasks"

- **limitation**: Some ablation evidence is narrow: the authors report evaluating ASQA ablations on a sampled subset, limiting the scale of those comparisons.
  - Page 9 · citation: whitespace
  - Quote: "On ASQA, we evaluate models on sampled 150 instances"

- **limitation**: The human evaluation is small, constraining how broadly its findings about outputs and reflection-token reliability can be generalized.
  - Page 10 · citation: whitespace
  - Quote: "we sampled 50 samples from PopQA and Bio results"

Unresolved questions:

- How reliably do reflection-token judgments transfer to tasks and domains beyond those tested, particularly when the critic disagrees with evidence?
- How stable are the reported gains under broader human evaluation and larger evaluation samples for long-form tasks?
- How much of the benefit depends on GPT-4-generated reflection-token training data versus the model and inference procedure?
- Inspection was limited to pages 1 and 5–10; I did not inspect the remaining methodology appendices, detailed task protocols, or all results, so further caveats and robustness evidence may be present.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 5, "end": 7}` | Inspect the training method and reflection-token design. | read pages [5, 6, 7] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect reported evaluation results and comparisons. | read pages [8, 9, 10] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states scope boundaries or limitations. | 0 matches | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an evidence-based assessment using the inspected method and results pages. | citation_validation_failed; #2: not_found | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Resubmit with the comparison quote copied from the inspected page. | citation_validation_failed; #2: not_found | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Resubmit using a short exact comparison quote from page 8. | review accepted | [event 31](trace.jsonl#L31) |
