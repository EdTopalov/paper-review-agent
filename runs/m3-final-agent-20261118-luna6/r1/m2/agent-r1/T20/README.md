# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

9 model calls · 5 reads · 30.68 s · $0.004086

9 decisions · 9 tool calls · 68529 input tokens (47552 cached) · 2034 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT is a practical fine-tuning recipe for domain-specific, open-book QA: train on questions with relevant and distractor documents, quote supporting passages in reasoning-style answers, and sometimes omit oracle context. Reported results suggest useful gains over domain-specific fine-tuning baselines in the evaluated settings. Its contribution is strongest as an empirically explored adaptation recipe for fixed in-domain document collections, not as a general-RAG solution.

- **strength**: The paper frames RAFT as training for both domain knowledge and robustness to retrieval errors.
  - Page 2 · citation: whitespace
  - Quote: "RAFT aims to not only enable models to learn domain specific knowledge through fine-tuning, but also to ensure robustness against inaccurate retrievals."

- **strength**: The reported table shows RAFT scores above DSF + RAG across its five listed domain columns, while the inspected excerpt gives no statistical uncertainty.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors explicitly limit the setting to evaluation on the same documents as training, so this does not establish transfer to new document collections.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The best proportion of training data with oracle context varies across datasets.
  - Page 6 · citation: whitespace
  - Quote: "Our analysis reveals that the optimal proportion varies across datasets"

Unresolved questions:

- How variable are results across random seeds, and are the reported differences statistically reliable?
- How well does RAFT transfer to document collections or domains not present during training?
- I inspected the method, portions of results and sensitivity analysis, and conclusion, but not every experimental detail, appendix, or all tables and figures.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "RAFT"}` | Locate the method description and experimental evidence for assessment. | 8 matches on pages [1] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the proposed training recipe and its setup. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Table 1"}` | Find quantitative comparisons and dataset results. | 1 matches on pages [5] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 6}` | Review reported results and evaluation design. | read pages [5, 6] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 8, "end": 9}` | Inspect stated limitations and further evaluation details. | read pages [8, 9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The method, reported benchmark results, and explicit scope boundary have been inspected; submit an evidence-based assessment while noting uninspected details. | citation_validation_failed; #1: not_found; #4: hyphenation_ambiguous (pages [6]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the two citation quotes using exact observed wording from pages 3 and 6. | citation_validation_failed; #1: not_found; #4: hyphenation_ambiguous (pages [6]) | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit corrected citations using exact wording from the observed excerpts. | citation_validation_failed; #1: not_found | [event 43](trace.jsonl#L43) |
| 9 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resolve the remaining citation mismatch by citing the directly observed prose on page 2, alongside verified results and scope evidence. | review accepted | [event 49](trace.jsonl#L49) |
