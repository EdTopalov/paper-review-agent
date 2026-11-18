# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**pyagent_react · ok**

5 model calls · 3 reads · 19.58 s · $0.002279

5 decisions · 5 tool calls · 39680 input tokens (29608 cached) · 1448 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes zero-shot Plan-and-Solve prompting: ask an LLM to devise a plan, execute its subtasks, and—in PS+—extract variables and attend to intermediate calculations. Across ten reasoning datasets, reported results generally improve on Zero-shot-CoT, with PS+ near or above few-shot CoT on some tasks. The work offers a simple, practically relevant prompting method and supporting comparisons, but evidence is limited to GPT-3 experiments and does not establish that planning itself explains the gains independently of the added instructions.

- **strength**: The method is specified as an actionable prompt strategy, with PS+ adding concrete guidance intended to reduce omissions and arithmetic mistakes.
  - Page 3 · citation: whitespace
  - Quote: "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"

- **strength**: The reported math results show broad gains over Zero-shot-CoT, though PS+ does not outperform every comparator on every dataset.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The authors identify prompt design effort as a limitation, relevant to the practicality and robustness of the approach.
  - Page 9 · citation: exact
  - Quote: "First, it takes\neffort to design the prompt"

- **limitation**: The paper states that semantic misunderstanding errors remain, delimiting the method's demonstrated error reductions.
  - Page 9 · citation: exact
  - Quote: "the semantic misunderstanding er-\nrors are still remain."

Unresolved questions:

- Do PS+ gains persist on other model families, beyond the GPT-3 setting reported here?
- How much of the improvement comes from explicit planning versus the additional variable-extraction and calculation instructions?
- How robust are the results to prompt wording, given the authors' stated sensitivity of GPT-3 to prompt expressions?
- I inspected the method, main results, selected analyses, and stated limitations, but not the full appendix or all reported experimental details; uncertainties about those details remain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect the prompting method and evaluation design. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect reported comparative results and any explicit scope limitations. | read pages [6, 7, 8] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 9, "end": 10}` | Inspect the conclusion and stated limitations for scope and caveats. | read pages [9, 10] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a balanced assessment using observed method, results, and limitation evidence. | citation_validation_failed; #3: not_found; #4: not_found | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the two citations using verbatim limitation text from observed page 9. | review accepted | [event 26](trace.jsonl#L26) |
