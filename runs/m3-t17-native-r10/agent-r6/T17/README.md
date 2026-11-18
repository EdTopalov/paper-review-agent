# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

8 model calls · 5 reads · 20.47 s · $0.003780

8 decisions · 8 tool calls · 58483 input tokens (36853 cached) · 1465 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper introduces a simple zero-shot Plan-and-Solve prompt that asks an LLM to devise and execute a plan, plus PS+ instructions emphasizing variables and intermediate calculations. On ten reasoning datasets using GPT-3, it generally improves over zero-shot CoT, with particularly strong arithmetic results; it is a practical prompting contribution, though evidence is bounded by the tested model and its stated limitations.

- **strength**: The approach concretely asks the model to break a task into subtasks and execute its plan.
  - Page 2 · citation: normalized
  - Quote: "first, devising a plan to divide the entire task into smaller subtasks"

- **strength**: The results table reports PS+ with a 76.7 arithmetic average, versus 70.4 for zero-shot CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The paper acknowledges semantic misunderstanding errors remain unresolved by this approach.
  - Page 9 · citation: exact
  - Quote: "There are two limitations in this work."

- **uncertainty**: The main reported setup uses GPT-3 text-davinci-003; I did not inspect the full paper or appendix for further model-family or robustness evidence.
  - Page 5 · citation: exact
  - Quote: "text-davinci-003 engine for GPT-3"

Unresolved questions:

- How robust are the gains across other model families and prompt phrasings?
- Do results generalize beyond the included benchmark datasets?
- How reproducible are reported differences across multiple runs or evaluation samples?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate the evaluation results to assess empirical support and scope. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect motivation, method definition, and prompt design. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Review quantitative comparisons and experiment details. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 10}` | Check the authors' stated limitations and discussion of generality. | read pages [9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence covers method, results, and stated limitations; submit a balanced assessment while noting the limited pages inspected. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: hyphenation_ambiguous (pages [9]); #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 2, "end": 2}` | Retrieve exact lines for citations flagged as ambiguous in the prior validation. | read pages [2] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Resubmit the assessment with exact excerpts verified from the PDF pages. | citation_validation_failed; #3: hyphenation_ambiguous (pages [9]); #4: not_found | [event 36](trace.jsonl#L36) |
| 8 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Use only quotes validated verbatim by the citation checker and finish the paper review. | review accepted | [event 42](trace.jsonl#L42) |
