# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

6 model calls · 4 reads · 13.82 s · $0.002056

6 decisions · 6 tool calls · 38357 input tokens (28374 cached) · 1087 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT proposes a practical fine-tuning recipe for domain-specific open-book QA: train with relevant and distractor documents, sometimes omit the answer-bearing document, and produce answers with cited quotations and reasoning. Results across QA and API-document benchmarks suggest this can substantially improve a 7B model’s in-domain RAG performance, though the paper’s claims are scoped to testing on the document collection used for adaptation.

- **strength**: The training design directly targets distractor robustness while preserving document-grounded answers.
  - Page 3 · citation: whitespace
  - Quote: "We differentiate between two types of documents: ‘oracle’ documents (D∗) i.e. the documents from which the answer to the question can be deduced, and ‘distractor’ documents (Di) that do not contain answer-relevant information."

- **strength**: The reported benchmark results are strong on several tasks, but gains are not uniform: PubMed is close to domain-specific fine-tuning with RAG, and Torch Hub is essentially tied with DSF.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The paper explicitly studies in-domain reuse rather than a shift to different documents at test time, limiting the generality of its conclusions.
  - Page 9 · citation: whitespace
  - Quote: "we only care about testing the LLM on the same set of documents."

- **uncertainty**: The inspected evidence does not establish how reliably the recipe transfers across independently assembled domains or how sensitive its gains are to training-data construction; those remain open questions.
  - Page 3 · citation: whitespace
  - Quote: "RAFT is independent of the retriever used."

Unresolved questions:

- How do RAFT gains hold when the test document collection changes or expands beyond the documents used during adaptation?
- How sensitive are results to the generated reasoning/citations and to variation in training-data construction?
- I inspected pages 2–5 and 9–10; other experimental details and limitations elsewhere in the paper were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate the empirical evaluation section to assess reported evidence. | 5 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect method and main results for experimental design and quantitative support. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 3}` | Review the training recipe and its stated scope to characterize the contribution accurately. | read pages [2, 3] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 10}` | Check paper's stated limitations and conclusion for explicit scope boundaries and remaining gaps. | read pages [9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers core recipe, benchmark table, and stated same-document scope; submit a balanced assessment noting unchecked implementation details. | citation_validation_failed; #1: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the first citation with a verbatim excerpt from the observed methods page and finalize the review. | review accepted | [event 30](trace.jsonl#L30) |
