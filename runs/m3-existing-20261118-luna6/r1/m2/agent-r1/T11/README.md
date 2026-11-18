# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

4 model calls · 3 reads · 11.42 s · $0.001809

4 decisions · 4 tool calls · 21172 input tokens (10185 cached) · 692 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes Python code as a unified, executable action format for LLM agents, arguing that it supports composing tools, control flow, and iterative interaction with execution feedback. It evaluates the format across 17 models, introduces an 82-instance multi-tool benchmark, and releases a 7k-trajectory instruction dataset with fine-tuned agents. The work offers a coherent, practically motivated contribution and broad comparative evidence, though the new benchmark is small and the results are mixed across models and settings.

- **strength**: The main evaluation spans 17 models and reports meaningful wins for CodeAct on complex tool-use tasks, including fewer turns, while also making clear that the gains do not apply uniformly.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **limitation**: The principal complex-task benchmark is compact and manually curated, limiting how confidently its results establish performance across broader task distributions.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **uncertainty**: The fine-tuning evaluation has domain overlap for some MINT tasks; the authors separate in- and out-of-domain results, but the observed improvement is not wholly attributable to generalization beyond training domains.
  - Page 9 · citation: whitespace
  - Quote: "CodeActAgent has some training domains overlapping with MINT’s evaluation (i.e., MINT includes ALFWorld and MATH), hence we report separate numbers for MINT’s in- and out-of-domain performance."

- **limitation**: The authors explicitly characterize the agent as an initial prototype and identify hallucination as a practical limitation, an important boundary on claims of reliable autonomous execution.
  - Page 10 · citation: whitespace
  - Quote: "For example, it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out), suggesting the need for subsequent alignment [ 33] for further improvements."

Unresolved questions:

- How robust are the results on larger, independently curated multi-tool benchmarks and tasks beyond the manually designed toolsets?
- What execution sandboxing and permission controls are required for safe deployment, and how effective are they against harmful or unintended code execution?
- Inspection was limited to pages 1, 3–5, and 8–10; appendices, detailed prompts, and full ablation and benchmark construction procedures were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "20%"}` | Locate the paper's quantitative claims to assess experimental support. | 2 matches on pages [1, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark design, results, and methodological details on the central evaluation. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Check training-data evaluation and reported model outcomes supporting the second contribution. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers the core comparative evaluation, benchmark scope, fine-tuning results, and stated practical limitation; submit a calibrated assessment while noting remaining inspection gaps. | review accepted | [event 20](trace.jsonl#L20) |
