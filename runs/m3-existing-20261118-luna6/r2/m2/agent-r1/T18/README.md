# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

5 model calls · 4 reads · 9.95 s · $0.001671

5 decisions · 5 tool calls · 29150 input tokens (19686 cached) · 613 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

Gorilla presents an end-to-end approach to API-call generation: a curated ML API benchmark with synthetic instruction pairs, a fine-tuned LLaMA model, and retrieval-aware training. Its quantitative results support improved API selection in several evaluated settings, while highlighting that outcomes depend on retrieval quality and that the benchmark and evaluation cover a bounded task.

- **strength**: The paper combines a substantial curated API dataset with a systematic evaluation setup and reports a held-out split.
  - Page 6 · citation: whitespace
  - Quote: "We emphasize that we have maintained a holdout test set on which we report our findings."

- **strength**: On the reported zero-shot benchmark, Gorilla substantially exceeds the listed GPT-4 overall accuracy on HuggingFace and TensorFlow Hub, though not on every dataset or setting.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The authors' evaluation reduces HuggingFace scoring for most comparison models to domain selection because its dataset is not exhaustive, limiting direct comparability.
  - Page 7 · citation: whitespace
  - Quote: "since the dataset is not exhaustive, for all the models except Gorilla, we only check if they can provide the correct domain names."

- **limitation**: The work focuses on ML APIs and explicitly says API execution is outside its focus; real-world execution reliability and broader API domains therefore remain unestablished here.
  - Page 5 · citation: exact
  - Quote: "While we do have a system to execute these APIs, that is not a focus of this paper."

Unresolved questions:

- How robust are results to independently authored user requests, rather than the synthetic instruction pairs used for the benchmark?
- How well do the retrieval and model combination generalize to non-ML APIs or to executing multi-step API workflows?
- What is the practical performance under evolving documentation beyond the illustrative test-time change examples?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect method and dataset construction to assess the paper's central contribution. | read pages [2, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Review training, retrieval, and benchmark evaluation details for evidentiary support. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect reported quantitative results and compare baselines to judge empirical support. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Check benchmark split and baseline evaluation details before judging generality and reliability. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The inspected method, evaluation, and limitations provide sufficient evidence for a balanced assessment. | review accepted | [event 25](trace.jsonl#L25) |
