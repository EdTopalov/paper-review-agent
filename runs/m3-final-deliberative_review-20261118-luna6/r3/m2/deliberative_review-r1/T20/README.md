# T20: RAFT: Adapting Language Model to Domain Specific RAG

**deliberative_review · ok**

8 model calls · 3 reads · 38.64 s · $0.009879

8 decisions · 5 tool calls · 64307 input tokens (1582 cached) · 4065 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT fine-tunes a language model on questions paired with relevant and distractor documents, sometimes omitting the relevant document, and trains it to answer with cited reasoning. The reported results show substantial gains on several domain-specific RAG benchmarks, although improvements vary by dataset. Only pages 1–7 were inspected; results and discussion on pages 8–11 remain unknown.

- **strength**: The training recipe directly targets open-book answering with irrelevant retrieved material by distinguishing documents that contain answer-relevant information from distractors.
  - Page 3 · citation: whitespace
  - Quote: "‘distractor’ documents (Di) that do not contain answer-relevant information."

- **limitation**: The CoT ablation is mixed: RAFT with CoT scores higher on four listed datasets but lower on Torch Hub (84.95 versus 86.56). This is a dataset-specific result, not evidence that CoT is generally harmful.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

- **uncertainty**: The inspected pages report a CoT ablation but do not separately isolate the effect of verbatim evidence citation. Pages 8–11 were not inspected, so additional evidence or qualifications there are unknown.
  - Page 7 · citation: exact
  - Quote: "Table 2: Ablation on Chain-of-Thought: The numbers of RAFT and RAFT without CoT."

Unresolved questions:

- How do pages 8–11 qualify the results, discuss limitations, or report additional experiments?
- How much of the reported benefit comes specifically from distractor training, verbatim citations, and reasoning traces considered separately?
- How sensitive are the gains to training-data construction and evaluation choices across domains beyond the inspected benchmarks?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and experimental setup to establish what RAFT changes, which baselines and datasets are compared, and whether the comparisons support the claimed gains.; Check results and analyses on the remaining pages for the size and consistency of improvements, including whether evidence supports the proposed roles of distractor handling and verbatim evidence citation.; Review discussion, limitations, and any additional experiments for scope boundaries or caveats; only page 1 is currently inspected, so do not treat unobserved material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [2, 3, 4] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation’s quote is not verified against the observed source, so it does not meet the requirement for a verbatim page quote.; The second observation says the CoT ablation is “lower than RAFT without CoT,” which compares the ablation to itself. The table instead shows that RAFT with CoT is lower on Torch Hub than RAFT without CoT; on the other listed datasets, RAFT with CoT scores higher. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the unverified quotation with a verbatim excerpt from page 3. Corrected the CoT comparison: RAFT with CoT scores below the no-CoT ablation on Torch Hub, not the other way around. Kept the score and scope uncertainty; later pages were not available for inspection. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |
| 8 | revise | Draft revised; Changes: Replaced the unverified first quotation with an exact observed quote. Clarified that the CoT comparison is lower on Torch Hub specifically; the ablation favors CoT on the other four datasets. Kept the score and uncertainty about the uninspected pages unchanged. | [event 42](trace.jsonl#L42) · [event 45](trace.jsonl#L45) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "RAFT"}` | Find method and results passages across supplied paper to ground assessment. | 8 matches on pages [1] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect RAFT method and experimental setup for what is changed, datasets, and comparison baselines. | read pages [2, 3, 4] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect core results, ablations, and discussion to assess evidence for distractor handling and citations. | read pages [5, 6, 7] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: not_found | [event 39](trace.jsonl#L39) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 47](trace.jsonl#L47) |
