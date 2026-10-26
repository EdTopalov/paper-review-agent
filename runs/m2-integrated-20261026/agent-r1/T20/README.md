# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

7 model calls · 5 reads · 19.59 s · $0.003154

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

RAFT is a practical fine-tuning recipe for in-domain RAG: train with question/document/answer examples that include irrelevant retrieved documents, sometimes omit the oracle document, and produce quoted reasoning answers. The paper reports improvements over several fine-tuning and RAG baselines across biomedical QA, multi-hop QA, and API-document tasks. Its main value is the targeted training setup and broad task demonstrations, while claims are bounded to a same-domain/document setting and the inspected evidence leaves some evaluation details unresolved.

- **strength**: The method directly trains for imperfect retrieval by mixing relevant evidence with distractors and withholding the oracle document on some examples.
  - Page 3 · citation: whitespace
  - Quote: "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."

- **strength**: The reported benchmark table gives evidence of gains over the listed RAG and domain-specific fine-tuning baselines on several tasks, though not uniformly over every baseline and task.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The work explicitly targets a restricted deployment setting rather than domain transfer to new documents at inference time.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The pages inspected establish headline results but do not provide enough detail here to judge statistical variability or fully audit the evaluation protocol.
  - Page 4 · citation: whitespace
  - Quote: "We see that RAFT consistently and significantly outperforms the baselines."

Unresolved questions:

- How sensitive are the headline gains to random seeds, data composition, and the exact retrieval pipeline?
- How well does RAFT transfer to new documents or domains, outside the same-document setting?
- How much of the gain depends on generated chain-of-thought quality versus the distractor-aware training construction?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The method uses oracle documents alongside distractors for a portion of examples, and only distractors for the remainder (PDF p. 3).
- Observation 2: **supported** — Table 1 reports RAFT’s results against the listed baselines across five tasks, with gains on several metrics and exceptions such as Torch Hub, where DSF scores 84.94 versus RAFT’s 84.95, and PubMed, where DSF + RAG ties GPT-3.5 + RAG (PDF p. 5). The claim appropriately avoids saying every comparison is a substantial win.
- Observation 3: **supported** — The paper explicitly contrasts its setting with work testing on different domains or documents, stating that it focuses on the same set of documents (PDF p. 9).
- Observation 4: **overstated** — The cited statement on p. 4 asserts that RAFT significantly outperforms baselines, but the paper includes more than headline results: it describes datasets and baselines (PDF p. 4), provides benchmark results and a CoT ablation (PDF pp. 5–7), and examines training and test-time document variation (PDF pp. 6–8). Those reported details do not establish statistical variability, but saying the pages inspected do not provide enough detail to fully audit the protocol is broader than the evidence shown; this is an open question, not itself a demonstrated defect.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate experimental results to assess evidence for RAFT's claimed performance gains. | 5 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect the main benchmark setup, results table, and stated evaluation details. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly discusses scope constraints or limitations. | 0 matches | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 2, "end": 3}` | Inspect the method and training-data construction to understand the distinctive contribution. | read pages [2, 3] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Inspect later discussion and conclusion for scope caveats and whether the authors identify limitations. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Evidence covers the core training recipe, benchmark comparisons, and stated same-document scope; submit an assessment while noting evaluation details not inspected. | citation_validation_failed; #4: hyphenation_ambiguous (pages [4]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Correct the invalid citation using exact language already observed on page 4 and submit the completed review. | review accepted | [event 37](trace.jsonl#L37) |
