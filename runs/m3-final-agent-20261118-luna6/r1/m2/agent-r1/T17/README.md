# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

5 model calls · 3 reads · 14.59 s · $0.001622

5 decisions · 5 tool calls · 25829 input tokens (18273 cached) · 1022 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes Plan-and-Solve prompting, which asks an LLM to devise and execute a subtask plan; PS+ adds instructions to track variables and calculations. Experiments on ten datasets across arithmetic, commonsense, and symbolic reasoning report gains over Zero-shot-CoT and competitive baseline results. This practical prompting contribution is motivated by identifiable reasoning errors, but evidence inspected is limited to one backbone and the paper notes prompt sensitivity and persistent semantic misunderstanding.

- **strength**: The method explicitly structures solving as planning followed by execution, with PS+ expanding the prompt to target reasoning quality.
  - Page 3 · citation: whitespace
  - Quote: "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"

- **strength**: The reported arithmetic results show PS+ consistently improves over Zero-shot-CoT across the evaluated datasets.
  - Page 5 · citation: normalized
  - Quote: "our PS+ prompting (i.e., PS prompting with more detailed instructions) consistently outperforms Zero-shot-CoT across all arithmetic reasoning datasets by a large margin."

- **limitation**: The authors identify prompt sensitivity and the need for careful prompt design as a practical limitation.
  - Page 9 · citation: exact
  - Quote: "The GPT-3 models\nare sensitive to the expressions in prompts, thus we\nneed to carefully design the prompts."

- **limitation**: The method does not address semantic misunderstanding errors, limiting its coverage of reasoning failures.
  - Page 9 · citation: whitespace
  - Quote: "the proposed plan-and-solve prompting can help ad-\ndress the calculation errors and missing-reasoning-\nstep errors, but the semantic misunderstanding er-\nrors are still remain."

Unresolved questions:

- How robust are the gains across different model families, prompt phrasings, and repeated or stochastic evaluations?
- How much of PS+’s effect comes from planning versus its added variable-extraction and calculation instructions? Detailed result tables and ablations were not inspected here.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate reported evaluation findings to assess empirical support. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect method definition and initial evaluation setup and findings. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 11}` | Inspect broader results and paper-stated limitations for scope and support. | read pages [9, 10, 11] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Evidence covers the prompt method, benchmark setup, headline findings, and stated limitations; submit a balanced assessment while noting unchecked detailed tables. | citation_validation_failed; #1: not_found; #4: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Resubmit assessment using exact observed wording for the failed citations. | review accepted | [event 25](trace.jsonl#L25) |
