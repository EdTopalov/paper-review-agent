# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

8 model calls · 5 reads · 21.34 s · $0.003359

8 decisions · 8 tool calls · 51704 input tokens (33408 cached) · 1526 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper introduces Plan-and-Solve prompting: elicit a plan, then execute its subtasks, with PS+ adding more detailed instructions. Results on ten reasoning benchmarks using GPT-3 show consistent improvements over zero-shot CoT and competitive performance against other prompting baselines. This is a useful, well-supported prompting contribution, but the evidence is limited to the evaluated model setup; the authors identify prompt-design effort and semantic misunderstanding as remaining limitations.

- **strength**: The reported PS+ average on the six math datasets is higher than zero-shot CoT, and the tables also show improvements over zero-shot CoT on the other reasoning categories.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **strength**: On commonsense reasoning, PS+ improves over zero-shot CoT on both reported benchmarks, while remaining below manual few-shot CoT.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **limitation**: The authors state that semantic misunderstanding errors remain despite the method's focus on calculation and missing-step errors.
  - Page 9 · citation: exact
  - Quote: "the semantic misunderstanding er-\nrors are still remain."

- **uncertainty**: The main experiments use one GPT-3 engine, so the inspected evidence does not establish transfer to other model families.
  - Page 5 · citation: exact
  - Quote: "We report the results us-\ning text-davinci-003 engine for GPT-3 in\nthe main paper."

Unresolved questions:

- Would the gains persist across other model families, model sizes, and instruction-tuned systems?
- How sensitive are the results to prompt wording and evaluation variability across repeated runs?
- I inspected the main benchmark tables, setup, and explicit limitations, but not the full appendix or complete error-analysis results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate the experimental results to assess evidence across the stated benchmark tasks. | 4 matches on pages [2, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect benchmark setup, headline results, and reported self-consistency comparisons. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check the paper’s explicit limitations or scope discussion before judging generality. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Read the explicit limitations and conclusion verbatim to characterize remaining scope. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers method evaluation, benchmark results, and stated limitations; submit a balanced assessment noting the single-model scope. | citation_validation_failed; #1: not_found; #2: not_found; #3: hyphenation_ambiguous (pages [9]); #4: hyphenation_ambiguous (pages [5]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with verbatim page text copied from the inspected excerpts, preserving citation wording and page numbers. | citation_validation_failed; #1: not_found; #2: not_found | [event 30](trace.jsonl#L30) |
| 7 | read_pages `{"start": 6, "end": 6}` | Retrieve exact result-table wording and quote lines for citation-validated observations. | read pages [6] | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit the assessment using validated exact quotations from observed benchmark-table, limitations, and setup passages. | review accepted | [event 41](trace.jsonl#L41) |
