# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**pyagent_react · ok**

5 model calls · 2 reads · 19.60 s · $0.002908

5 decisions · 5 tool calls · 35102 input tokens (20741 cached) · 1811 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

The paper proposes a simple zero-shot prompting variant that asks an LLM to devise and execute a plan, with PS+ adding instructions to extract variables and calculate intermediate results. Across ten datasets using GPT-3, it reports gains over Zero-shot-CoT, with mixed comparisons to few-shot and program-based baselines. The cross-task evaluation and error analysis are useful, but the inspected evidence does not establish broad generalization beyond the tested model setup.

- **strength**: The method explicitly encourages planning before solving.
  - Page 2 · citation: normalized
  - Quote: "we propose Plan-and-Solve (PS) Prompting."

- **strength**: The reported results show PS+ outperforming Zero-shot-CoT on the two listed commonsense benchmarks.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **strength**: On the sampled GSM8K error analysis, PS+ has lower reported calculation and missing-step error rates than Zero-shot-CoT.
  - Page 7 · citation: exact
  - Quote: "Zero-shot-PS+ 5% 7% 27%"

- **limitation**: The inspected main results use the public GPT-3 175B model; transfer to other model families remains unanswered, not a demonstrated defect.
  - Page 5 · citation: exact
  - Quote: "the public GPT-3 (Brown et al., 2020) (175B)"

Unresolved questions:

- Do the gains persist across other LLM families, sizes, and versions?
- How sensitive are results to prompt wording and evaluation variability?
- Does the error-type analysis generalize beyond the sampled GSM8K cases?
- Important inspection gap: pages 8–24, including appendices and any further experiments or limitations, were not read.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 5, "end": 7}` | Inspect the prompting method and quantitative evaluation results. | read pages [5, 6, 7] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed prompt formulation and evaluation setup. | read pages [2, 3, 4] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | The method, benchmark setup, main accuracy tables, and error analysis have been inspected; broader robustness evidence remains unreviewed. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #4: not_found | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Correcting the citations with verbatim excerpts from the inspected pages. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #4: hyphenation_ambiguous (pages [5]) | [event 23](trace.jsonl#L23) |
| 5 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Resubmitting with shorter exact excerpts copied from inspected pages. | review accepted | [event 29](trace.jsonl#L29) |
