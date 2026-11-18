# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

8 model calls · 5 reads · 20.95 s · $0.003709

8 decisions · 8 tool calls · 57429 input tokens (37198 cached) · 1667 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

InterCode contributes a practical, extensible formulation and implementation of interactive coding benchmarks, pairing code actions with execution feedback in containerized environments. Its Bash and SQL demonstrations show that interaction can substantially improve tested models’ success rates and expose distinct task and prompting challenges. The framework is a substantial benchmark contribution, though claims about broad generality and safety are bounded by the small number of implemented environments and the preliminary scope of the evaluation.

- **strength**: The paper defines a modular interactive task formulation and makes adapting static datasets a core design goal.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: Reported comparisons provide concrete evidence that iterative feedback can improve success on the tested tasks, notably for GPT-4 on SQL.
  - Page 7 · citation: exact
  - Quote: "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"

- **limitation**: The authors explicitly bound current coverage to two action spaces and datasets; CTF evidence is especially small.
  - Page 9 · citation: whitespace
  - Quote: "Second, the CTF dataset is limited to just four task instances due to our manual curation procedure."

- **uncertainty**: The evaluated prompting strategies are tested using a specified base model for this comparison, leaving broader cross-model transfer unanswered.
  - Page 8 · citation: exact
  - Quote: "usinggpt-3.5-turbo as the base model."

Unresolved questions:

- How well do the reported benefits generalize to additional programming languages, datasets, and task designs beyond Bash and SQL?
- How robust are the results to alternative reward functions and evaluation criteria, given the environment-specific grading schemes?
- What guardrails are needed for agents trained or evaluated in these environments to avoid unsafe behavior upon transfer to real systems?
- I inspected the main framework, experiments, and conclusion/limitations, but not the full appendix, implementation details, or every trajectory; those could clarify reproducibility and evaluation choices.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and limitations. | 7 matches on pages [9, 13, 14, 26] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark design and evaluation evidence for the claimed contribution. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 9}` | Check reported model results and conclusions to assess empirical support. | invalid_page_range | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 8}` | Inspect the main experimental results and model comparisons. | read pages [6, 7, 8] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Read the paper’s concluding limitations and future directions for scope context. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | The inspected framework, benchmark results, and explicit limitations provide enough evidence for an independent assessment. | citation_validation_failed; #4: wrong_page (pages [5]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Correct the unsupported citation using an exact excerpt from the observed evaluation discussion and finalize the review. | citation_validation_failed; #4: wrong_page (pages [5]) | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Use only quotes already verified on inspected pages; replace the uncertain observation with the directly observed table caption on page 7. | review accepted | [event 43](trace.jsonl#L43) |
