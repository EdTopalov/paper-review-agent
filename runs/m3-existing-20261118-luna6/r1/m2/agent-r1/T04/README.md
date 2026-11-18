# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

5 model calls · 4 reads · 9.76 s · $0.001684

5 decisions · 5 tool calls · 22856 input tokens (12624 cached) · 590 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench contributes a broad interactive benchmark spanning eight text-operable environments and evaluates 25 LLMs, providing a useful common testbed and documenting marked differences across models and tasks. Its breadth and released evaluation toolkit are valuable, though the evidence inspected leaves questions about benchmark reliability and the interpretation of its aggregate score.

- **strength**: The benchmark’s distinctive contribution is a diverse set of interactive environments rather than a single agent task.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: Evaluation of 25 models gives concrete comparative evidence, including variation in GPT-4’s performance across settings.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The authors disclose modest test-set task counts, despite substantial multi-turn interaction; this is an important constraint on interpreting precision and generalization.
  - Page 13 · citation: exact
  - Quote: "One may find the total number of problems in Dev and Test are a bit small—289 and 1,141 respectively."

- **limitation**: The overall score weights each environment inversely by its average score across the evaluated models; this makes the aggregate dependent on this particular model cohort and weighting rule.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

Unresolved questions:

- How stable are per-environment rankings and overall scores across repeated runs, alternative prompts, or changes to the evaluated model cohort?
- How well do results on these text-only, benchmark-specific environments transfer to deployment settings?
- I inspected the benchmark description, selected methodology pages, results, and analysis; I did not inspect the full task construction details or all environment-specific validation, so their quality and reproducibility remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Find the paper’s stated scope and limitations to assess benchmark coverage. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Read benchmark motivation, task suite, and evaluation design. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "GPT-4"}` | Locate reported comparative evaluation results for evidence of benchmark findings. | 8 matches on pages [2, 3, 5, 14, 15] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 13, "end": 15}` | Inspect result table, evaluation methodology, and discussion of performance evidence. | read pages [13, 14, 15] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers benchmark design, split sizes, model results, and analysis; submit a calibrated assessment while noting uninspected methodological detail. | review accepted | [event 25](trace.jsonl#L25) |
