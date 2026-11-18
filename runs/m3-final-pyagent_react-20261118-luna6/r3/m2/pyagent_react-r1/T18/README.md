# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

5 model calls · 4 reads · 15.50 s · $0.001766

5 decisions · 5 tool calls · 31125 input tokens (22305 cached) · 882 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla presents a practical pipeline for API-call generation that combines instruction fine-tuning with retrieval-aware training, alongside APIBench and an AST-based evaluation. Results show useful gains in API selection and reduced hallucination in several tested settings, with examples of adapting calls to changed documentation. The work is valuable but its claims are bounded by a curated ML-API benchmark, synthetic instructions, and an evaluation that does not establish semantic correctness or broad tool-use performance.

- **strength**: The benchmark has meaningful breadth within its chosen domain, exhaustively including Torch Hub and TensorFlow Hub entries while sampling HuggingFace models; the authors also explain the sampling rationale.
  - Page 2 · citation: whitespace
  - Quote: "We exhaustively include every API call in TorchHub (94 API calls) and TensorHub (696 API calls); For HuggingFace, since the models come in a large number and lots of the models don’t have a specification, we choose the most downloaded 20 models per task category"

- **strength**: On the reported zero-shot comparisons, Gorilla scores higher than the listed baselines across the three benchmark sources, though HuggingFace evaluation is not equally exhaustive for all models.
  - Page 7 · citation: normalized
  - Quote: "lightly fine-tuned Gorilla gets the state-of-the-art performance zero-shot over all the models, 20.43% better than GPT-4 and 10.75% better than ChatGPT."

- **limitation**: The AST metric identifies API calls against the collected dataset; it is not a general semantic-equivalence test, and HuggingFace baseline scoring is simplified because the dataset is not exhaustive.
  - Page 7 · citation: whitespace
  - Quote: "since the dataset is not exhaustive, for all the models except Gorilla, we only check if they can provide the correct domain names."

- **uncertainty**: The documentation-change evidence is illustrative, and the paper's stated focus excludes API execution; the inspected evidence does not establish reliability across broader changes or live tool outcomes.
  - Page 5 · citation: exact
  - Quote: "While we do have a system to execute these APIs, that is not a focus of this paper."

Unresolved questions:

- How well does the approach generalize to APIs outside the three ML model hubs and to API collections that change at larger scale?
- Would the documentation-change behavior remain reliable across a systematic set of updates, rather than the illustrated examples?
- How often do AST-matched calls actually execute successfully and produce semantically appropriate outcomes?
- I inspected pages 1–9, not pages 10–18; the remainder may contain additional evidence or qualifications not considered here.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect the benchmark construction and model-training approach. | read pages [2, 3] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect remaining dataset details and evaluation results. | read pages [4, 5] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 6, "end": 7}` | Review quantitative comparisons and test-time documentation-change results. | read pages [6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect documentation-change experiments and constraint-evaluation caveats. | read pages [8, 9] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment from the abstract, dataset/method pages, and evaluation and limitations pages inspected. | review accepted | [event 26](trace.jsonl#L26) |
