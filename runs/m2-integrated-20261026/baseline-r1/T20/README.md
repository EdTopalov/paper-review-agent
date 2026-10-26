# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 8.01 s · $0.002103

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

RAFT is a supervised fine-tuning recipe for domain-specific RAG: training examples mix answer-bearing documents with distractors, sometimes omit the answer-bearing document, and use quoted evidence in reasoning-style answers. Results across medical QA, HotpotQA, and API-documentation tasks suggest that this approach can improve a 7B model’s use of retrieved context, though the evidence is strongest within the paper’s fixed-domain setting.

- **strength**: The paper gives a concrete training design that addresses distractors and imperfect retrieval rather than training only on question-answer pairs.
  - Page 3 · citation: not_found
  - Quote: "For P fraction of the questions (qi) in the dataset, we retain the oracle document (d∗i) along with distractor documents (dk−1)."

- **strength**: The reported results show substantial gains on some tasks, particularly HotpotQA and HuggingFace, against the listed baselines.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The paper explicitly scopes its contribution to testing on the same documents used during training, limiting what these experiments establish about transfer to new domains or document collections.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The results are not uniformly better in every reported comparison: the CoT ablation is lower than RAFT on Torch Hub, and the main table’s Torch Hub gain over DSF is very small. The practical consistency and robustness of gains therefore remain unclear from these results.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

Unresolved questions:

- How well does RAFT transfer to new document collections or domains, rather than the same documents used during training?
- How sensitive are the reported gains to training-data construction, retrieval quality, and evaluation variability?
- When does adding reasoning-style answers help or hurt, given the lower Torch Hub result in the CoT ablation?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 3 describes training examples with an oracle document plus distractors for a portion of questions, and distractors only for the remainder. Page 4 adds reasoning-style answers with citations to source text. This supports the claim that the design addresses distractors and imperfect retrieval rather than using only question-answer pairs.
- Observation 2: **supported** — The results table on page 5 shows large RAFT gains over listed baselines on HotpotQA and HuggingFace—for example, 35.28 versus 6.38 on HotpotQA and 74.00 versus 61.06 on HuggingFace compared with DSF. The claim is appropriately limited to some tasks.
- Observation 3: **supported** — The paper explicitly says it studies testing on the same documents as training (page 9), and describes its focus as domain-specific open-book tasks in a known domain (page 2). That scope limits what the experiments establish about transfer to new collections or domains.
- Observation 4: **supported** — Page 7 reports a lower RAFT-without-CoT score than RAFT on Torch Hub (86.56 versus 84.95 in the table, so this comparison is actually higher without CoT), while page 5 shows only a 0.01-point RAFT-over-DSF difference on Torch Hub. The small main-table gain supports the consistency concern, but the stated CoT comparison is reversed; overall, the observation is partly grounded but inaccurate as written.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
