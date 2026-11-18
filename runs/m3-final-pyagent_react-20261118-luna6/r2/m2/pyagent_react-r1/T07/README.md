# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

7 model calls · 4 reads · 20.17 s · $0.002718

7 decisions · 6 tool calls · 58299 input tokens (45593 cached) · 1348 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes a substantial, executable benchmark for evaluating agents on open-ended computer tasks across applications, with configurable initial states and task-specific execution-based evaluation. Its task diversity and baseline/human comparisons make agent shortcomings concrete. The main contribution is benchmark infrastructure and measurement rather than a demonstrated solution to the agent capability gap.

- **strength**: The benchmark combines real computer interaction with varied tasks, intermediate setup states, and task-specific evaluation, supporting a broader evaluation target than isolated-app settings.
  - Page 2 · citation: whitespace
  - Quote: "a benchmark with 369 real-world computer tasks that involve widely-used web and desktop apps in open domains, OS file I/O, and multi-app workflows through both GUI and CLI."

- **strength**: The authors describe substantial task review and evaluation development, including cross-checks and multiple rounds of scrutiny; this supports, but does not establish perfect evaluator validity.
  - Page 7 · citation: whitespace
  - Quote: "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions."

- **strength**: Reported baseline and human results demonstrate a large performance gap under the tested setup, while category-level outcomes reveal that workflow tasks are particularly challenging.
  - Page 11 · citation: whitespace
  - Quote: "the success rate of the model is only 5.26% to 5.80% even with the strongest VLMs GPT-4V and Gemini-Pro-vision."

- **limitation**: The authors acknowledge that further red teaming could reduce evaluator errors; this is an explicit remaining quality concern, not evidence that the reported evaluations are invalid.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How well do the task-specific evaluators handle valid solutions not anticipated by their authors, especially across the full task suite?
- How representative are the results beyond the main Ubuntu benchmark and the particular agent prompts, action limits, and models tested?
- I inspected the introduction, environment/task construction, a portion of the baseline results, and human-performance material, not the full paper or appendices; additional analysis and implementation details could affect these judgments.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design and task construction details. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark evaluation results and human comparison. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 8}` | Inspect task coverage, annotation process, and evaluation safeguards. | read pages [6, 7, 8] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 8, "end": 9}` | Inspect human-performance protocol and benchmark limitations. | read pages [8, 9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment using the inspected benchmark, methods, and results pages. | citation_validation_failed; #1: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Resubmit with the first observation quote copied exactly from inspected page 2. | review accepted | [event 35](trace.jsonl#L35) |
