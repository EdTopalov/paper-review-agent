# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

6 model calls · 5 reads · 13.55 s · $0.001980

6 decisions · 6 tool calls · 22470 input tokens (9717 cached) · 615 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

AgentBench contributes a broad, interactive benchmark spanning eight text-operable environments and reports evaluations of 25 API and open models. Its comparative results and released evaluation toolkit make it useful for systematic LLM-agent assessment, while the authors acknowledge that coverage remains evolving and its weighted aggregate depends on the evaluated-model cohort.

- **strength**: The benchmark combines newly built and adapted environments, giving the evaluation breadth across distinct agent settings.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper provides a sizable model comparison and reports task-level outcomes supporting its headline gap between model groups.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The composite score's weighting is defined from the models evaluated, so the overall comparison may depend on the chosen cohort.
  - Page 14 · citation: whitespace
  - Quote: "utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

- **uncertainty**: The authors explicitly frame coverage as incomplete and evolving; the inspected pages do not establish how later versions or additional environments affect generality.
  - Page 3 · citation: exact
  - Quote: "there are definitely more scenarios and tasks to cover in LLM-as-agent evaluation."

Unresolved questions:

- How robust are model rankings to alternative task weights or changes in the model cohort?
- How representative and repeatable are results across task samples, prompts, and later model versions?
- I inspected pages 1–3 and 14–15 plus search snippets, not the full methodology, per-environment construction, or appendices; those details may alter confidence in individual task validity.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper's explicit scope and limitations to assess how broadly its benchmark claims are supported. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "8 environments"}` | Locate the benchmark composition and evaluation setup to ground the contribution summary. | 1 matches on pages [13] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 3}` | Read the motivation and benchmark design details on pages 2–3 to understand intended scope and environments. | read pages [2, 3] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "GPT-4"}` | Locate the central experimental findings and model-performance evidence. | 8 matches on pages [2, 3, 5, 14, 15] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 14, "end": 15}` | Inspect the reported results and analysis for concrete support and evaluation caveats. | read pages [14, 15] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | The inspected pages establish the benchmark breadth, results, scoring approach, and declared scope; submit a supported assessment while noting uninspected details. | review accepted | [event 31](trace.jsonl#L31) |
