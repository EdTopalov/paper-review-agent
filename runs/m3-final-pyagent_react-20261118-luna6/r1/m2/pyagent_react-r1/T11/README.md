# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

4 model calls · 3 reads · 11.95 s · $0.002171

4 decisions · 4 tool calls · 31939 input tokens (19371 cached) · 813 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

The paper proposes CodeAct, using executable Python as a unified action format for LLM agents, and supports it with comparisons across 17 models, a curated multi-tool benchmark, and a fine-tuned agent. Its strongest evidence is for complex tool-use tasks, where CodeAct often improves success and reduces interaction turns. The work also contributes a training dataset and discusses practical prototype limitations.

- **strength**: The multi-tool benchmark reports higher success rates and fewer turns for CodeAct across most evaluated models, with especially large results for some closed-source models.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2. Moreover, using CodeAct requires a lower average number of turns (12 out of 17 evaluated LLMs)."

- **limitation**: M3ToolEval is a modest, manually curated benchmark with 82 instances and manually crafted tools, so its results establish evidence on this benchmark rather than broad real-world coverage.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing. Each domain is accompanied by a unique set of manually crafted tools."

- **strength**: The agent evaluation explicitly separates overlapping training domains and tests text-action generalization, while reporting a mixed result for one trained model on M3ToolEval.
  - Page 9 · citation: whitespace
  - Quote: "CodeActAgent has some training domains overlapping with MINT’s evaluation (i.e., MINT includes ALFWorld and MATH), hence we report separate numbers for MINT’s in- and out-of-domain performance."

- **limitation**: The paper identifies hallucination and sandbox safety as unresolved practical concerns; these are stated risks, not demonstrated failures in the reported experiments.
  - Page 10 · citation: whitespace
  - Quote: "CodeActAgent is an initial prototype of an autonomous agent and still has several practical limitations. For example, it may suffer from hallucination commonly seen in LLMs"

Unresolved questions:

- How well do the reported gains carry over to broader, less curated environments and tasks beyond the benchmark toolsets?
- How can executable-code permissions and sandbox protections be made reliable enough for practical deployment?
- How stable are the findings across repeated runs and changes in prompts, model versions, or execution environments?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect the proposed CodeAct method and evaluation setup. | read pages [2, 3] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 4, "end": 6}` | Check benchmark construction, baselines, and quantitative results. | read pages [4, 5, 6] (text truncated by tool) | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 9, "end": 11}` | Inspect CodeActInstruct training and agent evaluation evidence. | read pages [9, 10, 11] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | The inspected method, benchmark results, fine-tuning evaluation, and stated limitations support a balanced assessment. | review accepted | [event 21](trace.jsonl#L21) |
