# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

4 model calls · 3 reads · 10.28 s · $0.001932

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

Introduces CodeAct, using executable Python as a unified, multi-turn action format, and releases a 7k-trajectory tuning set with CodeActAgent models. Controlled comparisons across 17 LLMs and downstream evaluations provide meaningful evidence that code actions can improve complex tool use and enable useful local agents, though gains vary by model and the central benchmark is small and manually curated.

- **strength**: The multi-turn tool benchmark reports higher success and fewer turns for CodeAct in most tested models, with a notable GPT-4 result.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The finetuned Mistral-based agent shows broad improvements in agent evaluations and several general tasks over the tested open-source baselines.
  - Page 9 · citation: whitespace
  - Quote: "CodeActAgent (both variants) perform better than all evaluated open-source LLMs on both the in-domain and out-of-domain subsets of MINT."

- **limitation**: M3ToolEval's modest, manually curated task set limits how broadly its results establish real-world generality.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **limitation**: The authors identify hallucination and safety of executing code as practical concerns; these are not resolved by the reported evaluations.
  - Page 10 · citation: whitespace
  - Quote: "it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out)"

Unresolved questions:

- How robust are the benchmark gains across larger, independently constructed task sets and different tool/environment designs?
- What sandboxing and safety controls are necessary for real deployments, and how effectively do they constrain harmful or unintended code execution?
- How much of CodeActAgent’s gains comes from the action format versus differences in dataset scale, data composition, and training? I inspected pages 1–5 and 8–10, not the full appendices or all methodological details.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 5 reports CodeAct as best on success rate for 12 of 17 models and on average turns for 12 of 17. It also highlights GPT-4-1106-preview’s 20.7 percentage-point success improvement and 2.1 fewer turns.
- Observation 2: **supported** — Page 9 reports both CodeActAgent variants outperforming evaluated open-source models on MINT’s in-domain and out-of-domain subsets. The table on page 8 also shows gains on several tested general tasks, with results varying by baseline and task.
- Observation 3: **supported** — Page 5 describes M3ToolEval as 82 human-curated instances across several domains. The claim that this modest curated set limits how broadly its results establish real-world generality is a reasonable, appropriately scoped inference.
- Observation 4: **supported** — Page 10 identifies hallucination as a limitation and says future work should design better safety mechanisms for code execution in a sandbox. The reported evaluations do not establish that these concerns are resolved.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "success rate"}` | Locate main quantitative evaluation claims and benchmark results. | 8 matches on pages [1, 2, 3, 5, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect framing, benchmark setup, and results supporting the claimed action-format gains. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review training-data and downstream agent evaluation evidence and scope. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers core proposal, benchmark comparisons, downstream tuning evaluation, and explicit limitations; submit a balanced assessment. | review accepted | [event 20](trace.jsonl#L20) |
