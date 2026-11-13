# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

4 model calls · 2 reads · 11.86 s · $0.001610

4 decisions · 4 tool calls · 15140 input tokens (6549 cached) · 966 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT is a post-training recipe for in-domain RAG: train models on question/context pairs to cite useful source passages, reason from them, and tolerate distractor documents. Reported comparisons across biomedical QA, Wikipedia QA, and API documentation show substantial gains on several tasks, but the pages inspected do not establish the full rigor or generality of the evidence.

- **strength**: The paper proposes a clear RAG-specific training idea: respond using evidence from relevant retrieved documents rather than treating all retrieved context as equally useful.
  - Page 1 · citation: whitespace
  - Quote: "we train the model to ignore those documents that don’t help in answering the question, which we call,\ndistractor documents."

- **strength**: The evaluation spans multiple task families and reports strong gains on some, while acknowledging limited gains over a RAG baseline on PubMed.
  - Page 4 · citation: whitespace
  - Quote: "for PubMed QA, since it is a binary yes/no question, we don’t observe significant gains when we compare our model with DSF + RAG."

- **limitation**: The displayed scores are uneven across benchmarks; RAFT is nearly tied with DSF on Torch Hub and lower on TensorFlow Hub.
  - Page 5 · citation: exact
  - Quote: "DSF 59.7 6.38 61.06 84.94 86.56\nDSF + RAG 71.6 4.41 42.59 82.80 60.29\nRAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

Unresolved questions:

- How stable are the reported results across random seeds, data splits, and alternative retrieval settings? The inspected pages do not establish this.
- I inspected the abstract and pages 4–5 only; training-data construction details, resource costs, and later robustness or ablation analyses remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate the empirical evaluation section to assess supporting evidence and performance claims. | 5 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect the main comparison table and experimental setup/limitations to ground the assessment. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | The inspected abstract and evaluation pages provide the central method and headline comparisons; submit a provisional assessment while noting limited coverage of methodology and later analyses. | citation_validation_failed; #2: hyphenation_ambiguous (pages [4]) | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Correct the rejected quote with an exact table excerpt from the observed page, keeping the provisional score and explicit inspection limits. | review accepted | [event 22](trace.jsonl#L22) |
