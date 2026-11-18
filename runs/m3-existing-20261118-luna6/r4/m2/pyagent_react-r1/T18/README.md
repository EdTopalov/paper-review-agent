# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

6 model calls · 3 reads · 15.56 s · $0.001941

6 decisions · 4 tool calls · 36894 input tokens (26851 cached) · 835 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

Gorilla combines synthetic instruction–API training with retrieval-aware fine-tuning to generate API calls, and introduces APIBench across three ML model hubs. The paper offers a useful benchmark and evidence that fine-tuning can improve API selection and reduce some forms of hallucination, while also showing retrieval quality matters. The evidence is promising but scoped: the benchmark is ML-focused, the correctness measure is AST-based, and results vary substantially by dataset and retrieval setting.

- **strength**: APIBench covers three hubs and documents a transparent sampling boundary: HuggingFace uses top models per task, whereas the other hubs are described as exhaustive after filtering.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls. 94 from Torch Hub (exhaustive), 626 from TensorFlow Hub v2 (exhaustive) and 925 from HuggingFace (Top 20 in each domain)."

- **strength**: The reported held-out comparisons show strong zero-shot performance for Gorilla on these benchmark partitions, though the gains are not uniform across all settings.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The evaluation operationalizes correctness and hallucination through AST matching and explicitly limits the study to one API call, so semantic equivalence and multi-step tool use are not established by this measure.
  - Page 5 · citation: whitespace
  - Quote: "Since we only consider one API call in this paper, checking if the AST of the candidate API call is a sub-tree of the reference API call reveals which API is being used in the dataset."

- **uncertainty**: Results demonstrate that retrieval can help or hurt; the paper identifies current retriever performance as a gap, leaving the practical value dependent on retrieval quality.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

Unresolved questions:

- How well do the results transfer beyond the selected ML model hubs to general-purpose or non-ML APIs?
- How robust are the conclusions to semantic correctness measures and to tasks requiring multiple API calls?
- How reproducible are the reported gains across other prompts, dataset splits, and model or retriever configurations? The inspected pages do not resolve this.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark construction and model training approach. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation protocol and reported comparative results. | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) |
| 5 | read_pages `{"start": 8, "end": 10}` | Check remaining experiments, adaptation claims, and stated limitations. | read pages [8, 9, 10] | [event 24](trace.jsonl#L24) |
| 6 | submit_review `{"review": {"score": 0.67, "observations": 4}}` | Submit a balanced assessment grounded in the inspected dataset, evaluation, and limitations pages. | review accepted | [event 29](trace.jsonl#L29) |
