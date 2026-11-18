# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

8 model calls · 5 reads · 18.34 s · $0.002990

8 decisions · 8 tool calls · 48669 input tokens (33007 cached) · 1455 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes a simple zero-shot prompting refinement: ask the model to devise a plan, execute it step by step, and in PS+ explicitly identify variables and calculate intermediate results. Across ten datasets and three reasoning areas, GPT-3 results generally improve over Zero-shot-CoT, with especially strong arithmetic results. The contribution is useful and empirically broad for prompting research, though evidence is bounded to GPT-3 and the authors acknowledge prompt-design effort and persistent semantic errors.

- **strength**: The proposed method’s novel framing is to build and then execute a plan for the problem.
  - Page 3 · citation: whitespace
  - Quote: "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"

- **strength**: Results show gains over Zero-shot-CoT beyond arithmetic, including both reported commonsense and symbolic datasets.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **limitation**: The main-paper results use GPT-3 text-davinci-003, so other model families are not established by the inspected evaluation.
  - Page 5 · citation: whitespace
  - Quote: "text-davinci-003 engine for GPT-3 in the main paper."

- **limitation**: The authors state that prompt development requires care because GPT-3 is sensitive to prompt expressions.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts"

Unresolved questions:

- How well does this prompting approach transfer to other model families or newer model versions?
- How robust are the results to alternative prompt wording and evaluation variation?
- I inspected the method, main quantitative results, and limitations, but not the complete appendix or all error-analysis details.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate reported evaluation evidence to assess support for the proposed prompting method. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the method definition and stated error categories to characterize the contribution and its rationale. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Inspect quantitative comparisons and evaluation setup for the central empirical claims. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states limitations or scope boundaries relevant to assessing generalizability. | 2 matches on pages [9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Read the complete stated limitations passage before finalizing the assessment. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The method, quantitative results, and stated limitations have been inspected; submitting a balanced assessment with page-grounded evidence. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correcting citation mismatches using exact observed phrases and retaining the supported findings. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #4: not_found | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Replacing the remaining ambiguous citations with exact, uninterrupted quotes already observed in the inspected pages. | review accepted | [event 43](trace.jsonl#L43) |
