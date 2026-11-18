# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

6 model calls · 5 reads · 10.81 s · $0.002593

6 decisions · 6 tool calls · 27785 input tokens (10123 cached) · 606 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench contributes a broad interactive benchmark spanning eight environments and evaluates 25 LLMs, with released evaluation tooling. Its comparative results offer a useful snapshot of agent performance, while heterogeneous tasks and some model-mediated evaluation procedures leave questions about score interpretation and robustness.

- **strength**: The benchmark covers varied interactive settings, including five newly created environments and three recompiled datasets, making breadth a central contribution.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper reports results across 25 models and finds a substantial performance gap; the per-task table makes variation across environments visible.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: Overall scoring uses weights derived from the tested models' average task scores, a choice that may complicate comparisons if the evaluated model pool changes.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

- **limitation**: At least one task's automatic evaluation relies on GPT-3.5 responses and keyword-based checking, leaving the reliability of this metric an important concern rather than a demonstrated failure.
  - Page 10 · citation: whitespace
  - Quote: "For automatic evaluation, we set up some key words for gpt-3.5-turbo to answer"

Unresolved questions:

- How sensitive are rankings and aggregate conclusions to alternative, fixed task weights?
- How well do the automatic evaluation procedures agree with independent human judgments, especially for lateral-thinking puzzles?
- I did not inspect the full appendix or all environment-specific result and validation details, so uncertainty remains about task-level robustness and reproducibility.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope and limitations for a balanced assessment. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "eight environments"}` | Find the benchmark task coverage and evaluation setup. | 0 matches | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Read framing, benchmark design and task descriptions to assess novelty and scope. | read pages [2, 3, 4] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 10}` | Inspect evaluation results and methodology for evidence quality and important caveats. | read pages [8, 9, 10] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 14, "end": 16}` | Review comparative results and scoring procedures to judge empirical support. | read pages [14, 15, 16] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The inspected pages establish the benchmark scope, comparative results, and evaluation caveats; submit an evidence-based review while noting uninspected details. | review accepted | [event 31](trace.jsonl#L31) |
