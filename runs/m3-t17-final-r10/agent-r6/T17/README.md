# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

7 model calls · 4 reads · 17.06 s · $0.002436

7 decisions · 7 tool calls · 50237 input tokens (39526 cached) · 1448 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes Plan-and-Solve prompting: zero-shot instructions that ask an LLM to devise a plan and carry it out, with PS+ adding detailed guidance. Across ten datasets and three reasoning categories, experiments with GPT-3 show gains over zero-shot CoT and competitive arithmetic results against few-shot CoT. The work is a useful, well-supported prompting contribution, though evidence is limited to the tested model setup and semantic errors remain.

- **strength**: The main arithmetic table reports PS+ ahead of zero-shot CoT on all six listed benchmarks, with a higher average accuracy.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **strength**: The results are not confined to math: PS+ exceeds zero-shot CoT on both reported commonsense datasets.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **limitation**: The inspected main-paper evaluation specifies one GPT-3 engine, so generalization across model families remains untested in the inspected evidence.
  - Page 5 · citation: whitespace
  - Quote: "text-davinci-003 engine for GPT-3 in the main paper."

- **limitation**: The authors acknowledge that semantic misunderstanding persists, despite addressing calculation and missing-step errors.
  - Page 9 · citation: whitespace
  - Quote: "the proposed plan-and-solve prompting can help ad- dress the calculation errors and missing-reasoning- step errors, but the semantic misunderstanding er- rors are still remain."

Unresolved questions:

- Would the gains replicate on other model families and with different prompt formulations?
- How stable are the error-type findings beyond the 100 sampled GSM8K problems and tested model configuration?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experimental Setup"}` | Inspect the evaluation setup and model details to assess support. | 1 matches on pages [4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Read benchmark and results pages to judge breadth and empirical evidence. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect error analysis and stated constraints for demonstrated limitations. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers method, multi-dataset results, error analysis, and author-stated limitations; submit concise assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [4]); #2: not_found; #3: not_found; #4: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with exact observed quotations from pages 5, 6, and 9 after citation validation feedback. | citation_validation_failed; #1: not_found; #2: not_found | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 6, "end": 6}` | Copy exact result-table wording from the observed page for valid citations. | read pages [6] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit assessment with validated verbatim citations and clearly scoped unresolved questions. | review accepted | [event 35](trace.jsonl#L35) |
