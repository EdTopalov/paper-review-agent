# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

7 model calls · 5 reads · 27.13 s · $0.003988

7 decisions · 7 tool calls · 50655 input tokens (28517 cached) · 1872 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines API-specific instruction fine-tuning with retrieval-aware training and introduces APIBench for evaluating API-call selection across three ML model hubs. The paper provides quantitative comparisons, including cases where Gorilla exceeds or matches prompting baselines, and explores retrieval quality, documentation changes, and constraints. Its contribution is useful and experimentally supported within this benchmark, but the evaluation is bounded by synthetic instruction data and API-call matching rather than execution; evidence for documentation adaptation is illustrative. Important gaps in my inspection include later appendix material and further details of the experimental protocol.

- **strength**: The paper contributes a broad, structured API benchmark and a clearly described synthetic instruction-generation pipeline.
  - Page 2 · citation: whitespace
  - Quote: "We also generate 10 synthetic user question prompts per API using Self-Instruct [42]."

- **strength**: The reported comparisons show meaningful gains in some settings, while also documenting that retrieval does not uniformly help.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The authors explicitly bound the study to API-call generation, not execution; AST matching therefore does not establish that generated code runs successfully or achieves the requested outcome.
  - Page 5 · citation: exact
  - Quote: "While we do have a system to execute these APIs, that is not a focus of this paper."

- **uncertainty**: The documentation-change evidence includes an example of adaptation, but the inspected text does not establish reliability across a broader set of API changes or tasks.
  - Page 8 · citation: exact
  - Quote: "Figure 6: Gorilla’s retriever–aware training enables it to react to changes in the APIs."

Unresolved questions:

- How well do results transfer to APIs outside the three ML model hubs, and to multi-step tool use?
- How representative are the synthetic instructions and the holdout split of independently written user requests?
- Would execution-based evaluation, including argument validity and task success, agree with AST-match accuracy?
- How robust is documentation-change adaptation across a larger, systematically varied set of changes?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "APIBench"}` | Locate the benchmark and evaluation evidence. | 3 matches on pages [1, 2, 3] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect dataset construction, model method, and evaluation design. | read pages [2, 3] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect training details, benchmark results, and evaluation limitations. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Review quantitative comparisons and evidence for documentation adaptation. | read pages [7, 8, 9] | [event 21](trace.jsonl#L21) |
| 5 | search_paper `{"query": "Limitations"}` | Check the paper’s explicitly stated scope boundaries. | 3 matches on pages [2, 9, 13] | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit a balanced assessment based on the inspected method, results, and stated scope. | citation_validation_failed; #4: not_found | [event 32](trace.jsonl#L32) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Correct the unsupported quotation using the observed figure caption on page 8. | review accepted | [event 38](trace.jsonl#L38) |
