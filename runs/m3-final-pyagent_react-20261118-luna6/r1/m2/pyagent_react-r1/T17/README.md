# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**pyagent_react · ok**

5 model calls · 3 reads · 16.82 s · $0.002440

5 decisions · 5 tool calls · 42654 input tokens (31419 cached) · 1444 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes zero-shot Plan-and-Solve (PS) prompting, asking an LLM to devise and execute a plan, and PS+ adds instructions to extract variables and calculate intermediate results. Results across ten datasets show consistent gains over Zero-shot-CoT for the reported GPT-3 setup, with PS+ competitive with few-shot CoT on arithmetic. This is a useful, clearly tested prompting contribution, though its evidence is bounded to the tested model and settings and does not isolate every component of the richer prompt.

- **strength**: The evaluation covers arithmetic, commonsense, and symbolic reasoning, with PS+ outperforming Zero-shot-CoT on each reported dataset; the paper also reports competitive arithmetic performance against few-shot baselines.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **strength**: The prompt comparison offers evidence that results improve with more detailed instructions, though the prompt variants change multiple instructions together and do not isolate each instruction's effect.
  - Page 6 · citation: whitespace
  - Quote: "The reason is that Prompt 3 doesn’t include instructions for devise and complete a plan."

- **limitation**: The authors explicitly identify prompt design as effortful and note that semantic misunderstanding remains unresolved; these are acknowledged boundaries, not evidence that the reported gains fail.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **uncertainty**: The inspected experimental evidence reports results with GPT-3, leaving open whether the gains generalize to other model families or sizes.
  - Page 2 · citation: exact
  - Quote: "The results of our experiments\nwith GPT-3 show"

Unresolved questions:

- Do PS and PS+ yield similar improvements on other model families and sizes?
- How much of PS+’s gain comes from planning versus its additional variable-extraction and calculation instructions?
- How reproducible are the error-type estimates under independent annotators or a specified annotation protocol?
- How sensitive are results to prompt wording, given the authors’ stated concern about prompt sensitivity?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 5, "end": 7}` | Inspect the prompting methods and principal experimental comparisons. | read pages [5, 6, 7] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed prompting procedure and experimental framing. | read pages [2, 3, 4] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect later analysis and the authors' stated scope or limitations. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment using inspected methods, results, and limitations. | citation_validation_failed; #2: wrong_page (pages [6]); #4: hyphenation_ambiguous (pages [5]) | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the page references and use verbatim excerpts already inspected. | review accepted | [event 26](trace.jsonl#L26) |
