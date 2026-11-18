# T20: RAFT: Adapting Language Model to Domain Specific RAG

**deliberative_review · ok**

7 model calls · 3 reads · 35.02 s · $0.007692

7 decisions · 4 tool calls · 50002 input tokens (1582 cached) · 3267 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT is a post-training recipe for in-domain, open-book question answering: fine-tune on questions paired with oracle and distractor documents, sometimes omit the oracle document, and train answers with cited reasoning. Reported comparisons and ablations provide promising evidence across several QA and API-documentation benchmarks. The assessment is limited by the supplied excerpts: pages 8–11 were not inspected, and page 2 was only partially inspected.

- **strength**: The method trains on relevant and irrelevant context, and sometimes omits the oracle document, aiming to prepare models for in-domain RAG.
  - Page 3 · citation: whitespace
  - Quote: "we include no oracle document and only include distractor documents"

- **strength**: The table reports improvements over DSF + RAG across its listed datasets, although the paper notes that the PubMed comparison is not significant.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors report no significant gain over DSF + RAG on PubMed QA, qualifying the broader improvement claim without showing that RAFT fails overall.
  - Page 4 · citation: whitespace
  - Quote: "for PubMed QA, since it is a binary yes/no question, we don’t observe significant gains when we compare our model with DSF + RAG."

- **strength**: The CoT ablation reports improved results on several datasets, though the table also shows lower RAFT scores than the no-CoT variant on Torch Hub.
  - Page 7 · citation: whitespace
  - Quote: "With a gain of 9.66% and 14.93% on the Hotpot QA and HuggingFace datasets respectively."

Unresolved questions:

- How sensitive are the gains to the training data, oracle/distractor construction, and reasoning-generation process?
- Do the gains persist beyond these benchmarks and the in-domain training assumptions?
- What implementation and evaluation details, and what further limitations, are presented on uninspected pages 8–11?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and experimental-results pages to verify how RAFT is trained, what baselines and datasets are compared, and whether reported results support the claim of consistent improvement.; Check later pages for ablations, implementation and evaluation details, and stated limitations that could qualify the abstract’s claims; only page 1 is currently inspected, so evidence elsewhere remains unknown.; Prepare an independent score and concise assessment grounded only in the supplied paper, with 2–4 observations each supported by a short verbatim quote and 1-based PDF page number,  … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [5, 6, 7] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [3, 4] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation’s page 3 quotation is not verified as verbatim by the citation check. Replace it with a short exact span from E13, such as “we include no oracle document and only include distractor documents,” and retain page 3.; The fourth observation’s page 7 quotation reports a robustness finding, but does not support the observation’s point about uninspected pages. Keep the coverage caveat, but make clear it is based on the supplied coverage record rather than the quoted passage, or refocus the observation on the reported finding. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the unverified method quotation with an exact span from page 3. Refocused the final observation on the CoT ablation, which its quotation supports, and stated the inspection gaps separately. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "distractor"}` | Locate method and evidence on training setup and results. | 8 matches on pages [1, 2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect experimental results and evaluation details to substantiate claims and identify counterevidence. | read pages [5, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 3, "end": 4}` | Inspect method, experiment setup, and core results supporting the claims. | read pages [3, 4] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
