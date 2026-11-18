# T20: RAFT: Adapting Language Model to Domain Specific RAG

**deliberative_review · ok**

7 model calls · 3 reads · 35.05 s · $0.010279

7 decisions · 4 tool calls · 70547 input tokens (0 cached) · 2940 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT is a fine-tuning recipe for in-domain RAG that trains models on questions with oracle and distractor documents, sometimes omitting the oracle, and answers containing reasoning and quoted evidence. The reported benchmark results and CoT ablation support gains on several tasks, but performance varies by task and the paper’s stated scope is testing on the same document collection used for training.

- **strength**: The training recipe deliberately mixes answer-bearing and distractor documents, and sometimes omits the oracle document, directly addressing imperfect retrieval during training.
  - Page 3 · citation: whitespace
  - Quote: "Then, for P fraction of the questions (qi) in the dataset, we retain the oracle document"

- **strength**: The paper reports a CoT ablation, with results varying across datasets: the RAFT row improves several scores over the no-CoT row, but not all.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

- **limitation**: The paper explicitly scopes its study to testing on the same document collection used for training; this is a scope boundary, not a demonstrated defect.
  - Page 9 · citation: whitespace
  - Quote: "we only care about testing the LLM on the same set of documents."

Unresolved questions:

- How much improvement is attributable individually to distractor training, oracle omission, reasoning, and quoted evidence? The observed comparisons do not isolate all these components.
- How stable are the gains across random seeds, alternative retrievers, and document collections not used for fine-tuning?
- Pages 1–10 were inspected, but page 11 was not. Data-split, run-variance, and metric details were not fully assessed in the observed pages, and the uninspected page may contain additional relevant evidence or caveats.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and experimental pages to verify what RAFT trains on, how distractor documents and evidence citations are handled, and whether the reported comparisons isolate its contribution.; Check results and evaluation details across PubMed, HotpotQA, and Gorilla—including baselines, metrics, data splits, and ablations—to assess whether the claimed gains are supported and how broadly they hold.; Review the remaining pages for stated limitations, caveats, and additional evidence; currently only page 1 has been inspected, so do not treat unobserved material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | read pages [2, 3, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [5, 6, 7] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [8, 9, 10] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation’s quote is not an exact match to the source: page 3 begins the sentence with “Then, for P fraction…”, so the cited fragment as written is not verbatim. Replace it with an exact, contiguous excerpt.; The second observation cites page 5, but the quoted table row appears on page 7 in the supplied archive. Correct the page number to 7.; The draft and ledger correctly flag that page 11 was not inspected, but the remaining-pages obligation is therefore still unresolved. Avoid treating the inspected pages as the complete account of limitations or  … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Corrected the page 3 quotation to an exact contiguous excerpt and moved the CoT table quotation to page 7. Preserved the qualification that page 11 remains uninspected. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method/training construction and initial evaluation details, including counterevidence to the paper's framing. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect empirical results, ablations, and robustness evidence beyond the supplied excerpts. | read pages [5, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 10}` | Inspect remaining discussion/conclusion and experimental details for stated limitations and counterevidence. | read pages [8, 9, 10] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
