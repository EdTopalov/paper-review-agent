# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

5 model calls · 4 reads · 11.58 s · $0.001501

5 decisions · 5 tool calls · 24618 input tokens (16189 cached) · 603 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.79

OSWorld contributes an executable, extensible desktop-computer benchmark with 369 Ubuntu tasks, execution-based task-specific evaluation, and baseline assessments across multimodal and text-based agents. The evidence supports its value as infrastructure and as a demonstration of the substantial gap between current agents and human task performance, while conclusions remain bounded by the tested task set and agent setup.

- **strength**: The benchmark combines diverse computer workflows with executable evaluations rather than relying solely on matching demonstrations.
  - Page 7 · citation: whitespace
  - Quote: "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions."

- **strength**: The reported baseline and human results make the benchmark’s challenge concrete, with substantial differences across agent input configurations.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The paper acknowledges a constraint of the action representation that may limit some computer interactions and learning.
  - Page 6 · citation: whitespace
  - Quote: "they do not model all possible actions on a computer, leading to limitations when attempting actions like right-clicking and clicking with the ctrl key held to select items."

- **uncertainty**: The reported model results use a bounded interaction budget, so the evidence does not settle performance under longer or differently configured agent interactions.
  - Page 10 · citation: whitespace
  - Quote: "We heuristically request the agents to complete the tasks within a max step limit of 15, which is enough for most tasks."

Unresolved questions:

- How robust are task-specific evaluation scripts to valid solutions or application states beyond those anticipated during authoring and cross-checking?
- How well do the findings generalize beyond the selected Ubuntu tasks and tested baseline prompting/action configurations?
- I inspected benchmark construction and results pages, but not the full appendices, detailed per-task findings, or all experimental and evaluation procedures.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Inspect the paper’s explicit scope and limitations for balanced assessment. | 3 matches on pages [6, 15, 23] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Read benchmark design and task collection details, including interaction limitations. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "12.24%"}` | Locate the core benchmark results and comparative evidence. | 4 matches on pages [1, 2, 10, 11] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 11}` | Inspect model evaluation setup, baseline results, and human comparison. | read pages [9, 10, 11] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.79, "observations": 4}}` | Evidence covers benchmark construction, evaluation results, and a stated action-space constraint; submit a balanced assessment while noting uninspected details. | review accepted | [event 25](trace.jsonl#L25) |
