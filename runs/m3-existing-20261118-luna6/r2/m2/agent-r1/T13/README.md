# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

7 model calls · 4 reads · 19.40 s · $0.002746

7 decisions · 7 tool calls · 53961 input tokens (42049 cached) · 1717 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains language models to decide when to retrieve and to emit reflection tokens assessing passage relevance, answer support, and usefulness; those signals guide segment generation and selection. Across six tasks, the paper reports strong results against multiple retrieval and non-retrieval baselines, with ablations supporting the role of its components. Its empirical scope is task- and setup-specific, and the authors acknowledge that citations can still fail to support generated claims.

- **strength**: The central design unifies adaptive retrieval and fine-grained self-critique in one trained generator, with inference-time control over retrieval and output selection.
  - Page 3 · citation: whitespace
  - Quote: "These reflection tokens (Table 1) signal the need for retrieval or confirm the output’s relevance, support, or completeness."

- **strength**: The reported benchmark table shows competitive gains on several tasks and markedly higher ASQA citation precision than the listed retrieval baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: Ablations give evidence that training with retrieved passages and critique, and using support scores at inference, contribute to performance on the tested datasets.
  - Page 9 · citation: whitespace
  - Quote: "removing ISSUP during the beam search results hurts performance on ASQA."

- **limitation**: The authors explicitly warn that improved factuality and citation accuracy do not guarantee that citations support every output; this is an acknowledged reliability boundary, not a demonstrated failure rate.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations."

Unresolved questions:

- How reliably do the reflection-token judgments generalize beyond the tested datasets and domains?
- What is the end-to-end retrieval and decoding cost relative to the baselines under comparable serving conditions?
- The inspected excerpts include only a small human evaluation sample; how stable are human-judged support and reflection-token reliability at larger scale?
- I inspected pages 1–4 and 8–12, not the intervening training/data details or appendices; those portions may clarify reproducibility, dataset construction, and broader evaluation limitations.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope or limitations for a balanced assessment. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method details and experimental setup to evaluate what the paper actually demonstrates. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review benchmark results and evaluation evidence supporting the claimed gains. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 12}` | Check stated ethical, evaluation, or methodological caveats to distinguish acknowledged scope from open concerns. | read pages [11, 12] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | The inspected method, benchmark results, ablations, and ethical caveat provide enough evidence for a qualified assessment. | citation_validation_failed; #1: wrong_page (pages [3]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the citation to quote exact observed text on page 4 and resubmit the assessment. | citation_validation_failed; #1: wrong_page (pages [3]) | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | The citation validator indicates the first quote is on page 3; use that page number while retaining the other verified citations. | review accepted | [event 35](trace.jsonl#L35) |
