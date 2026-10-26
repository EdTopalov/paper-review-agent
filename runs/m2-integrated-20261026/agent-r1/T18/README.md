# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

5 model calls · 3 reads · 15.31 s · $0.001798

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

Gorilla combines APIBench, AST-based API-call evaluation, and retrieval-aware fine-tuning of LLaMA to improve API selection and call generation across several model hubs. Reported results are strong on the evaluated tasks, while also revealing substantial dependence on retrieval quality and a narrower empirical scope than the paper’s broad API ambitions.

- **strength**: The paper presents a useful end-to-end benchmark and training setup for API-call generation, with a held-out evaluation.
  - Page 6 · citation: whitespace
  - Quote: "We emphasize that we have maintained a holdout test set on which we report our findings."

- **strength**: On reported zero-shot results, Gorilla exceeds listed GPT baselines for all three hub datasets, though evaluation conventions differ by dataset.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The HuggingFace evaluation uses a weaker correctness check for comparison models than for Gorilla, limiting direct cross-model comparability there.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names."

- **limitation**: Practical retrieval remains a significant bottleneck: the authors report large accuracy drops when substituting evaluated retrievers for the oracle.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

Unresolved questions:

- How well do these results transfer to APIs outside the three hubs and to real user requests or executable multi-step tool workflows?
- How representative and reproducible are the benchmark examples, generated instructions, and reported gains across API versions and stronger retrieval systems?
- The inspected passages do not establish the robustness of adaptation to documentation changes beyond illustrated examples; what systematic test-time update evaluation was performed?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes APIBench, AST-based evaluation, Gorilla fine-tuning, and a held-out test set (PDF pp. 2–6). The appendix also reports the data splits (p. 13).
- Observation 2: **supported** — In the zero-shot results, Gorilla exceeds both listed GPT baselines on TorchHub, HuggingFace, and TensorFlow Hub. The paper explicitly notes that HuggingFace uses a different, less stringent check for comparison models (PDF p. 7).
- Observation 3: **supported** — The paper states that, for HuggingFace, models other than Gorilla are checked only for correct domain names, whereas TorchHub and TensorHub use AST-tree accuracy for all models (PDF pp. 6–7).
- Observation 4: **supported** — The paper reports 29.20% accuracy degradation with GPT-Index and 52.27% with BM25 when evaluating the retrieval-aware fine-tuned model, relative to the ground-truth retrieval setting (PDF pp. 7–8).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "evaluation"}` | Locate the paper’s evaluation section to assess evidence for its claims. | 8 matches on pages [3, 6, 7] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect benchmark results and retrieval ablations, including exact passages for evidence. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 3}` | Check how the API dataset was constructed to judge benchmark scope and support. | read pages [3] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers the contribution, benchmark construction, measured performance, and an explicit retrieval caveat; submit a scoped assessment. | citation_validation_failed; #4: wrong_page (pages [7]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the citation page for the retrieval caveat using the observed page 7 text and finalize the assessment. | review accepted | [event 25](trace.jsonl#L25) |
