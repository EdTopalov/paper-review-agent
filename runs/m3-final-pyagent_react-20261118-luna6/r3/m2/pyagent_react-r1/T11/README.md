# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

6 model calls · 4 reads · 16.94 s · $0.002591

6 decisions · 5 tool calls · 50466 input tokens (36307 cached) · 918 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, using executable Python as a unified action format for LLM agents, and evaluates it against text and JSON actions. It reports advantages on multi-tool tasks and introduces CodeActInstruct and CodeActAgent, with promising open-model results. The work is substantial and empirically supported, though its complex-task benchmark is small and some comparisons are affected by training/evaluation overlap.

- **strength**: The paper directly compares action formats on a newly constructed benchmark with tasks requiring coordinated use of multiple tools.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **strength**: Across the 17 evaluated models, CodeAct more often achieves higher success and fewer interaction turns on M3ToolEval; the paper reports a notable result for its strongest model.
  - Page 5 · citation: exact
  - Quote: "For example, the best model gpt-4-1106-preview achieves a\n20.7% absolute improvement compared to the next best action format (text) while requiring2.1 fewer\ninteraction turns on average."

- **limitation**: The results also show a large gap between the best open- and closed-source model on M3ToolEval, tempering claims of immediate practical readiness for open models.
  - Page 5 · citation: exact
  - Quote: "the best open-source model achieving 13.4%\nwhile the best closed-source model gpt-4-1106-preview 74.4%."

- **uncertainty**: The CodeActAgent evaluation includes training-domain overlap for some MINT tasks, and the paper reports separate in- and out-of-domain results; the inspected pages do not resolve how robust its conclusions are to other forms of overlap or broader evaluation.
  - Page 9 · citation: exact
  - Quote: "CodeActAgent has some training domains overlapping with MINT’s evaluation (i.e.,\nMINT includes ALFWorld and MATH), hence we report separate numbers for MINT’s in- and\nout-of-domain performance."

Unresolved questions:

- How stable are the M3ToolEval gains across a larger set of tasks and independently constructed benchmarks?
- How well do CodeAct and CodeActAgent perform under a wider range of execution environments and safety constraints?
- The inspection covered the main method, selected results, and limitations, but not the appendices, full prompts, or detailed ablation tables; those may clarify evaluation and data-generation caveats.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect the proposed CodeAct method and benchmark setup. | read pages [2, 3] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect benchmark results and evaluation methodology. | read pages [6, 7, 8] (text truncated by tool) | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 4, "end": 5}` | Review controlled comparisons and task construction. | read pages [4, 5] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Inspect model evaluation results and reported scope limitations. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment from the inspected methods, results, and limitations pages. | review accepted | [event 30](trace.jsonl#L30) |
