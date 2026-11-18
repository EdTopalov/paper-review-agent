# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

5 model calls · 1 reads · 23.22 s · $0.001897

5 decisions · 4 tool calls · 27790 input tokens (22755 cached) · 2081 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT proposes retrieval-augmented fine-tuning: train a language model to answer with retrieved context while learning to ignore distractors, including through quoted evidence and reasoning-style responses. The reported results show substantial gains over comparison fine-tuning approaches on several domain-specific RAG benchmarks, with analyses of reasoning and distractor-document choices. The contribution is practically relevant, but the inspected evidence does not establish how robust the gains are beyond the reported settings.

- **strength**: The reported benchmark table supports the claim that RAFT can outperform domain-specific fine-tuning with RAG across the listed tasks, although gains vary substantially by dataset.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The CoT ablation does not uniformly improve the reported scores: Torch Hub is lower for RAFT than for RAFT without CoT, despite the table caption's broad improvement claim.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21\nRAFT 73.30 35.28 74.00 84.95 86.86"

- **uncertainty**: The authors state that their training setup matters for preparing models for varied retrieval scenarios; the inspected passage does not establish how large or stable the claimed benefit is.
  - Page 7 · citation: whitespace
  - Quote: "This finding underscores the importance of a well-calibrated training environment"

Unresolved questions:

- How sensitive are the reported gains to training data construction, retrieval quality, and choices of evaluation metric?
- Do results generalize to domains or retrieval settings beyond those reported in the paper?
- What accounts for the Torch Hub decrease in the CoT ablation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 5, "end": 7}` | Inspect the evaluation setup and reported results. | read pages [5, 6, 7] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Submit an evidence-based assessment from the abstract and inspected results and analysis pages. | citation_validation_failed; #3: hyphenation_ambiguous (pages [6]) | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Resubmit with a verbatim quote that avoids the ambiguous line-break hyphenation. | citation_validation_failed; #3: hyphenation_ambiguous (pages [7]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Resubmit using a short page 7 quote without ambiguous hyphenation. | review accepted | [event 25](trace.jsonl#L25) |
