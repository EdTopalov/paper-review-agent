# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

5 model calls · 3 reads · 14.05 s · $0.002437

5 decisions · 5 tool calls · 42552 input tokens (29976 cached) · 1161 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT proposes fine-tuning models for domain-specific open-book QA using relevant and distractor documents, sometimes omitting the oracle context, and answers with quoted evidence and reasoning. Results across biomedical QA, HotpotQA, and API documentation benchmarks suggest this recipe can improve in-domain RAG over several fine-tuning and prompting baselines, though its stated same-document evaluation scope limits claims about transfer to new collections.

- **strength**: The recipe explicitly trains on oracle and distractor documents, and also includes examples without the oracle document to teach answering despite imperfect retrieval.
  - Page 3 · citation: whitespace
  - Quote: "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."

- **strength**: The main comparison reports gains over its listed baselines on multiple tasks, with a notable exception on PubMed versus DSF+RAG; the results support promise but not universal superiority.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors explicitly delimit the work to testing on the same document collection used in training, so evidence here does not establish generalization to unseen domains or collections.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The CoT ablation is informative but mixed: reported gains on several benchmarks coexist with lower Torch Hub accuracy, and the inspected passages do not resolve variability or statistical significance.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

Unresolved questions:

- How much do results vary across random seeds, and are the reported differences statistically reliable?
- How sensitive are the outcomes to data-generation choices, retrieval quality, and scaling beyond the evaluated LLaMA-2-7B setup?
- I inspected the method, selected evaluation pages and tables, and conclusion; I did not inspect all training details or the complete supplementary/implementation evidence, so those aspects remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect method and experimental setup/results to assess the paper's contribution and support. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Check quantitative tables, comparison details, and sensitivity analyses to judge empirical strength. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect final discussion, limitations, and conclusion for stated scope and caveats. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers the method, main comparisons, ablation, stated domain boundary, and conclusion; submit an assessment while noting experimental details not inspected. | citation_validation_failed; #1: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the first citation using an exact method sentence observed on page 3; retain the verified evidence and limitations. | review accepted | [event 25](trace.jsonl#L25) |
