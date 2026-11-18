# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

11 model calls · 5 reads · 31.87 s · $0.004569

11 decisions · 11 tool calls · 85025 input tokens (64458 cached) · 2776 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes zero-shot Plan-and-Solve prompting: the model first makes a plan, then carries out subtasks, with PS+ adding more detailed instructions. Evaluation across ten reasoning datasets shows improvements over zero-shot CoT and competitive results versus few-shot CoT on some tasks. This is useful prompting research with substantive benchmark evidence, though generalization beyond the tested setup remains uncertain.

- **strength**: The arithmetic results show a substantial average improvement for PS+ over zero-shot CoT, approaching the Manual-CoT average.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **strength**: The error analysis reports PS+ with lower calculation and missing-step error rates than zero-shot CoT, but a similar semantic-error rate.
  - Page 7 · citation: exact
  - Quote: "Zero-shot-PS+ 5% 7% 27%"

- **limitation**: The paper identifies prompt sensitivity as a practical constraint requiring careful prompt design.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we\nneed to carefully design the prompts."

Unresolved questions:

- Would the gains replicate with different model families or sizes? The reported results use GPT-3, and I did not inspect all appendix details.
- How robust are results to prompt wording and evaluation variation?
- Do the error-pattern differences generalize beyond the sampled GSM8K analysis?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate the paper’s main results and evaluation evidence. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect numerical evaluation tables and nearby experimental discussion. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the authors explicitly state scope limitations or caveats. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Read the complete stated limitations for an evidence-grounded assessment. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment using inspected results, methodology, and stated limitations. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the ambiguous quote by using exact, observed wording from the limitations page. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 30](trace.jsonl#L30) |
| 7 | read_pages `{"start": 9, "end": 9}` | Verify exact wording of the cited limitation to resolve the citation validation issue. | read pages [9] | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Finalize the paper review with verified excerpts and the observed scope of evidence. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 41](trace.jsonl#L41) |
| 9 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Replace disputed limitation citation with the already verified prompt-sensitivity quote and finalize assessment. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 47](trace.jsonl#L47) |
| 10 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit the final review using only validated quotes from pages 6 and 7, and acknowledge limited inspected scope. | citation_validation_failed; #3: hyphenation_ambiguous (pages [5]) | [event 53](trace.jsonl#L53) |
| 11 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Finalize with validated results excerpts only; state remaining uncertainty about generalization. | review accepted | [event 59](trace.jsonl#L59) |
