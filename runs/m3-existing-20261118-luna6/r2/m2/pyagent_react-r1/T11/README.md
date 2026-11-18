# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

4 model calls · 3 reads · 22.63 s · $0.002846

4 decisions · 4 tool calls · 36948 input tokens (22397 cached) · 1607 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

The paper proposes CodeAct, using executable Python as a general action interface for LLM agents, and evaluates it against text and JSON actions. It also introduces a 7k-trajectory instruction dataset and finetuned agents. The experiments provide meaningful evidence for gains on selected multi-tool tasks, while the benchmark’s limited size, overlap in agent-training and evaluation domains, and acknowledged prototype limitations constrain claims about practical generality.

- **strength**: On the curated complex-task benchmark, CodeAct improves success rates for many evaluated models and can reduce interaction turns; gains vary substantially by model.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The paper reports a broad evaluation of the finetuned agents and separates overlapping MINT training domains from out-of-domain results.
  - Page 9 · citation: whitespace
  - Quote: "hence we report separate numbers for MINT’s in- and out-of-domain performance."

- **limitation**: M3ToolEval is a modest-sized, human-curated benchmark, so the observed results do not by themselves establish performance across a broad range of real deployments.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **limitation**: The authors explicitly characterize CodeActAgent as a prototype and identify hallucination as a practical concern; safe execution and containment also remain unresolved in the paper’s account.
  - Page 10 · citation: whitespace
  - Quote: "For example, it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out), suggesting the need for subsequent alignment [ 33] for further improvements."

Unresolved questions:

- How robust are the reported comparisons to alternative benchmark compositions, broader environments, or repeated evaluation runs?
- How much of CodeActAgent’s improvement is attributable specifically to CodeActInstruct versus the added conversation data and training setup?
- What sandboxing, permission controls, and safety evaluations would be needed before allowing agents to execute code in consequential settings?
- Inspection was limited to the first ten PDF pages; appendices, detailed ablations, and other later-page evidence were not reviewed. I therefore cannot assess those details.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the method definition and benchmark setup. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect complex benchmark results and evaluation details. | read pages [5, 6, 7] (text truncated by tool) | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect dataset construction and finetuning evaluation evidence. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit an evidence-based assessment using the inspected methods, results, and limitations pages. | review accepted | [event 21](trace.jsonl#L21) |
