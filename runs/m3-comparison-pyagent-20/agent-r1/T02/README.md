# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

5 model calls · 2 reads · 18.24 s · $0.001617

5 decisions · 5 tool calls · 15218 input tokens (8261 cached) · 1361 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.64

Reflexion adds language-based self-reflection and dynamic memory to an existing agent loop, using task feedback to improve behavior across trials without model fine-tuning. The AlfWorld results are a notable demonstration, while HotPotQA results are useful but benchmark-specific; the inspected evidence supports promise rather than broad generality.

- **strength**: AlfWorld results show substantial cross-trial performance improvement.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **strength**: The HotPotQA experiment uses a binary exact-match reward and resets between attempts, so its reported gain is specific to this evaluation setup.
  - Page 6 · citation: whitespace
  - Quote: "EM was used as the binary reward model."

- **limitation**: The paper identifies reliance on an emergent model ability; this is a stated scope boundary, not by itself a demonstrated failure.
  - Page 10 · citation: whitespace
  - Quote: "Reﬂexion relies on the emergent property of self-reﬂection that is present in several large language models."

- **uncertainty**: The authors mention an inconclusive WebShop attempt, but its details were not inspected.
  - Page 10 · citation: whitespace
  - Quote: "In addition, we include an inconclusive attempt to improve performance on the WebShop benchmark"

Unresolved questions:

- How sensitive are results to the language model, prompt examples, and reflection procedure?
- What are the detailed WebShop findings and remaining limitations?
- How well does the approach transfer beyond the reported benchmarks?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper’s stated scope limits and caveats before assessing it. | 2 matches on pages [10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 6}` | Inspect the benchmark setup and reported results for evidence supporting the claimed performance. | read pages [5, 6] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.64, "observations": 4}}` | The observed abstract, benchmark results, and limitations provide enough evidence for a qualified paper assessment; report remaining evidence gaps. | citation_validation_failed; #2: hyphenation_ambiguous (pages [6]) | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.64, "observations": 4}}` | Correct the HotPotQA citation to a verbatim sentence from the observed page and finalize the assessment. | citation_validation_failed; #2: hyphenation_ambiguous (pages [6]) | [event 22](trace.jsonl#L22) |
| 5 | submit_review `{"review": {"score": 0.64, "observations": 4}}` | The second HotPotQA quotation triggered ambiguous hyphenation validation; resubmit with a short exact excerpt from the observed setup passage. | review accepted | [event 28](trace.jsonl#L28) |
