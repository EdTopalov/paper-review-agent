# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

7 model calls · 5 reads · 16.54 s · $0.003832

7 decisions · 7 tool calls · 55613 input tokens (32240 cached) · 1220 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

The paper presents executable Python actions (CodeAct) as a unified, composable action interface for LLM agents, evaluates it against text and JSON across API calling and multi-tool tasks, and releases a 7k-trajectory tuning dataset with fine-tuned agents. Results support benefits on the tested tasks, while small benchmark scale, overlap in agent-training evaluation, and practical safety constraints limit broader conclusions.

- **strength**: A direct evaluation across 17 LLMs finds CodeAct often improves success and uses fewer turns on a benchmark designed around composing tools, with reported large gains for the strongest model.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The paper contributes a multi-domain interaction dataset and reports substantial improvements for fine-tuned agents, including separate in- and out-of-domain evaluation and generic task checks.
  - Page 8 · citation: whitespace
  - Quote: "On all trajectories generated, we keep 411 trajectories from gpt-4-0613 and 6728 trajectories from gpt-3.5 and claude."

- **limitation**: The principal complex-tool benchmark is relatively small and its task tools are manually crafted, limiting how confidently its scores generalize to broader real-world tool ecosystems.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **limitation**: CodeActAgent remains a prototype with a stated hallucination concern; the paper also identifies unconstrained code execution as a safety concern requiring safeguards.
  - Page 10 · citation: whitespace
  - Quote: "it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out)"

Unresolved questions:

- How robust are the comparative gains across larger, independently curated benchmarks and tool sets not manually tailored to the evaluated tasks?
- How do performance and safety change under realistic sandbox restrictions, permissions, and adversarial or malformed environment feedback?
- I inspected the paper’s core evaluation tables, fine-tuning setup, and limitations, but not the appendices’ detailed prompts, filtering criteria, or full ablation results; how sensitive are the findings to those choices?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "20%"}` | Locate the paper’s reported comparative evaluation results. | 2 matches on pages [1, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect evaluation design, benchmark scope, and reported results. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "CodeActInstruct"}` | Find evidence on instruction-tuning results and general-capability evaluation. | 8 matches on pages [1, 3, 4, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 8}` | Check dataset construction and model evaluation claims for strengths and scope. | read pages [7, 8] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Inspect fine-tuning comparisons and evaluation caveats relevant to support strength. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence inspected covers comparative benchmark results, training/evaluation setup, and the authors’ stated limitations; submit a balanced assessment. | citation_validation_failed; #2: wrong_page (pages [7]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Correct the mismatched dataset citation with exact observed wording from page 8 and resubmit the assessment. | review accepted | [event 37](trace.jsonl#L37) |
