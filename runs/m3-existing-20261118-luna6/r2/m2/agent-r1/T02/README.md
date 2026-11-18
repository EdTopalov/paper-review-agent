# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

6 model calls · 5 reads · 12.88 s · $0.001751

6 decisions · 6 tool calls · 23267 input tokens (13052 cached) · 726 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

Reflexion adds trial-level natural-language reflection and dynamic memory, triggered by simple failure heuristics, to an existing LLM agent rather than training a new policy. Its reported AlfWorld and HotPotQA results support the usefulness of this mechanism in these settings, while the modest WebShop result and narrow model/benchmark coverage temper the broader claims.

- **strength**: The paper specifies a lightweight mechanism for triggering reflection based on repeated action cycles or an action limit, making its central intervention concrete and compatible with existing agents.
  - Page 3 · citation: normalized
  - Quote: "h is designed to replace the role of a human-in-the-loop in which a human trainer monitors the running trajectory to detect signs of hallucination or inefficient planning."

- **strength**: The AlfWorld evaluation tests 134 tasks and compares reflection against a baseline using a shared setup; the 97% result is meaningful evidence of improvement across trials, though not a general performance guarantee.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The reported WebShop run showed little improvement and unhelpful reflections, a concrete counterexample to broad claims of reliable improvement across task types.
  - Page 10 · citation: normalized
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reflexion run"

- **uncertainty**: The observed evidence is bounded to a small set of benchmarks and GPT-3-family models; whether the method generalizes to other models and environments remains unanswered here.
  - Page 10 · citation: whitespace
  - Quote: "In this study, we used GPT-3.0 and GPT 3.5 to power a ReAct agent (Yao et al., 2023) to learn from its past mistakes."

Unresolved questions:

- How robust are the gains across other LLMs, agent architectures, and tasks beyond AlfWorld, HotPotQA, and the inconclusive WebShop run?
- How much of the reported improvement depends on repeated trials, chosen reflection prompts, and the heuristic thresholds?
- I inspected selected sections (pages 2–3, 5, and 10), not the full paper; details elsewhere, including the complete HotPotQA results and any additional analyses, could change this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "97%"}` | Locate the reported benchmark results and their evaluation context. | 3 matches on pages [1, 2, 5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the method description and experimental setup for evidence and scope. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check the authors’ stated scope boundaries and limitations. | 2 matches on pages [10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 5}` | Inspect benchmark protocol and comparison details behind reported performance. | read pages [5] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 10}` | Review explicit limitations to distinguish scope constraints from demonstrated weaknesses. | read pages [10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence covers the proposed approach, AlfWorld protocol and results, and the authors’ stated limitation; submit a balanced assessment. | review accepted | [event 31](trace.jsonl#L31) |
