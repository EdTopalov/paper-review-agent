# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

5 model calls · 2 reads · 20.16 s · $0.002386

5 decisions · 4 tool calls · 26318 input tokens (13461 cached) · 1289 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT is a domain-specific RAG fine-tuning recipe: train on questions with relevant and distractor documents, and use cited reasoning-style answers to teach context use. The inspected experiments report gains over several fine-tuning and RAG baselines, with analyses of oracle-context proportion and distractors. The evidence supports a useful, practically motivated contribution, but the inspected portion does not establish how broadly the results generalize beyond the reported setups.

- **strength**: The training formulation directly addresses imperfect retrieval by mixing answer-bearing and distractor documents, sometimes training without the oracle document.
  - Page 2 · citation: exact
  - Quote: "RAFT aims to not only enable models to learn\ndomain specific knowledge through fine-tuning, but also\nto ensure robustness against inaccurate retrievals."

- **strength**: Reported benchmark results show RAFT outperforming the listed DSF + RAG figures on several tasks, though not uniformly across every comparison or metric.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **uncertainty**: The reported analysis indicates the optimal proportion of oracle-containing training instances varies by dataset, leaving this hyperparameter task-dependent.
  - Page 6 · citation: exact
  - Quote: "This indicates\nthat training your LLM without the correct corresponding\ncontext at times can be beneficial for the downstream task of\nanswering questions related to the documents."

- **limitation**: The inspected evaluation centers on selected datasets and model comparisons; whether gains extend to other retrievers, training budgets, or model scales remains unanswered here.
  - Page 4 · citation: whitespace
  - Quote: "In our experiments, we use the following datasets\nto evaluate our model and all baselines."

Unresolved questions:

- How robust are the reported gains across different model sizes, retrievers, and independently constructed domain datasets?
- How sensitive are results to the quality and consistency of generated reasoning and citations?
- I inspected pages 1–6 only; later sections, including any additional experiments, limitations, and conclusions, were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect RAFT method details and the first experimental evidence. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Check result tables, evaluation details, and reported limitations. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Synthesize inspected method and results while noting uninspected later pages. | citation_validation_failed; #1: not_found; #3: hyphenation_ambiguous (pages [6]) | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Replace unverified wording with exact excerpts observed on pages 2–6. | review accepted | [event 27](trace.jsonl#L27) |
