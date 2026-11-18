# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**pyagent_react · ok**

7 model calls · 4 reads · 34.64 s · $0.003166

7 decisions · 7 tool calls · 60716 input tokens (50687 cached) · 2813 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper introduces Plan-and-Solve prompting: ask an LLM to devise a plan and then execute it, with PS+ adding instructions to extract relevant variables and calculate intermediate results. Reported tests cover ten datasets across arithmetic, commonsense, and symbolic reasoning; PS+ improves over Zero-shot-CoT on the reported comparisons and is competitive with some few-shot results. The work is practical and supported by broad benchmark coverage, while the authors acknowledge prompt-design effort and persistent semantic misunderstandings. The evidence inspected is limited to selected pages, and the reported GPT-3 evaluation does not establish generality across model families.

- **strength**: The method gives a concrete prompting intervention aimed at decomposing a task and executing its subtasks.
  - Page 3 · citation: whitespace
  - Quote: "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"

- **strength**: The reported comparison shows PS+ exceeding Zero-shot-CoT on the two inspected commonsense datasets.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **strength**: The small-sample error analysis reports lower calculation and missing-step error proportions for PS+ than for Zero-shot-CoT.
  - Page 7 · citation: exact
  - Quote: "Zero-shot-PS+ 5% 7% 27%"

- **limitation**: The paper explicitly identifies prompt design as a limitation; it also states that semantic misunderstanding remains unresolved.
  - Page 9 · citation: exact
  - Quote: "There are two limitations in this work."

Unresolved questions:

- How well does the approach transfer to model families other than the GPT-3 model evaluated in the inspected experimental setup?
- How stable are results to prompt wording and evaluation variation, given the authors’ stated sensitivity to prompt expressions?
- Would the error-type findings persist on larger or additional samples? The inspected analysis describes 100 GSM8K examples.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect the prompting method and evaluation setup. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect result tables and analyses supporting the performance claims. | read pages [6, 7, 8] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the paper states scope boundaries or limitations. | 2 matches on pages [9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 9, "end": 9}` | Inspect the stated limitations and conclusion. | read pages [9] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Synthesize the prompting contribution, reported benchmark evidence, and explicit limitations; note that only selected pages were inspected. | citation_validation_failed; #2: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct citations using verbatim excerpts from the inspected pages. | citation_validation_failed; #2: not_found | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with exact short excerpts preserved from the inspected text. | review accepted | [event 36](trace.jsonl#L36) |
