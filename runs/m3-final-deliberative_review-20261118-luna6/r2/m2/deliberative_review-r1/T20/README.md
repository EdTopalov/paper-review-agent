# T20: RAFT: Adapting Language Model to Domain Specific RAG

**deliberative_review · ok**

8 model calls · 3 reads · 41.47 s · $0.010113

8 decisions · 5 tool calls · 65915 input tokens (1582 cached) · 4131 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

RAFT is a post-training recipe for domain-specific RAG: fine-tune on questions paired with relevant and distractor documents, sometimes omit the relevant document, and train answers with reasoning and quoted evidence. Reported results and ablations support its usefulness on the evaluated benchmarks, while leaving questions about experimental variability and broader generalization. I inspected pages 1–8; pages 9–11 were not inspected.

- **strength**: The recipe includes training examples without an oracle document, addressing the challenge of answering despite imperfect retrieval.
  - Page 3 · citation: whitespace
  - Quote: "we include no oracle document and only include distractor documents"

- **strength**: RAFT's point scores exceed DSF + RAG on all five listed datasets, although the paper says the PubMed QA gain is not significant.
  - Page 4 · citation: whitespace
  - Quote: "for PubMed QA, since it is a binary yes/no question, we don’t observe significant gains"

- **strength**: The paper reports a CoT ablation and studies oracle-document proportions and distractor counts, providing evidence about training choices beyond aggregate comparisons.
  - Page 7 · citation: whitespace
  - Quote: "Results on various datasets show that adding CoT can significantly improve the performance of the finetuned model."

- **uncertainty**: The observed table gives point scores without variability estimates, and the inspected evidence does not isolate every recipe component. Pages 9–11 were not inspected, so whether they provide further evidence or caveats is unknown.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

Unresolved questions:

- How stable are the reported gains across random seeds or other sources of experimental variation?
- How much of the improvement comes from distractor training, quoted evidence, reasoning-style answers, or their combination?
- Do the findings extend beyond the evaluated models, datasets, and in-domain setting?
- What further analyses, caveats, or scope boundaries appear on the uninspected pages 9–11?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and experimental setup to determine what RAFT trains on, how distractor documents and quoted evidence are handled, and whether comparisons isolate the proposed recipe.; Inspect results and tables across the reported datasets and model settings to check whether the claimed improvements are supported, including relevant baselines and reported variability or limitations.; Inspect remaining pages for further analyses, caveats, and scope boundaries; only page 1 is currently observed, so do not treat uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [3, 4, 5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [6, 7, 8] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: Two observation citations are not valid as written: the first quote is not verified against page 3, and the PubMed QA quote is on page 4, not page 5. Replace them with exact source spans and correct page numbers before relying on the observations.; The third observation is verified, and the final observation’s table quote is verified. The score and summary are broadly consistent with the inspected evidence, but the draft should retain its explicit qualification that pages 9–11 were not inspected. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Corrected the first quotation to a verbatim page 3 span and corrected the PubMed QA quotation’s page number. Also corrected the table comparison: RAFT has higher point scores on all five datasets, while the paper reports no significant PubMed QA gain. Preserved the score and the qualification that pages 9–11 were not inspected. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |
| 8 | revise | Draft revised; Changes: Corrected the first observation to an observed page 3 quotation and corrected the PubMed QA citation to page 4. Retained the score and the explicit qualification that pages 9–11 were not inspected. | [event 42](trace.jsonl#L42) · [event 45](trace.jsonl#L45) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "distractor"}` | Inspect RAFT training construction and retrieve nearby method evidence. | 8 matches on pages [1, 2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 5}` | Inspect method and initial results with page-specific evidence; address how RAFT differs from baselines. | read pages [3, 4, 5] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 8}` | Inspect subsequent ablations, experimental details, and caveats for the paper evaluation. | read pages [6, 7, 8] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: not_found | [event 39](trace.jsonl#L39) |
| 8 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 47](trace.jsonl#L47) |
