# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

6 model calls · 3 reads · 16.76 s · $0.002086

6 decisions · 5 tool calls · 39770 input tokens (30314 cached) · 1203 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AGENTLESS presents a structured, non-agent alternative for repository-level issue repair: hierarchical localization followed by candidate patch generation, filtering, and ranking. Its evaluation suggests this relatively simple pipeline is competitive on SWE-bench Lite at reported low cost, and the authors identify benchmark-description problems and evaluate a filtered subset. The work offers a useful baseline and analysis, though the claims are bounded by the benchmark and comparison setup.

- **strength**: The method is a clearly specified alternative to autonomous tool-using agents, with localization decomposed into file, code-element, and edit-location stages before patching.
  - Page 2 · citation: exact
  - Quote: "AGENTLESS follows a simple two phase process: localization and repair."

- **strength**: The reported ablation results provide evidence that multiple samples and majority voting improve over a single sample.
  - Page 8 · citation: whitespace
  - Quote: "We can further improve performance to 78 fixes by sampling the LLM multiple times and selecting a patch using majority voting."

- **limitation**: On the inspected Lite-S analysis, the authors report that closed-source tools do better than AGENTLESS on problems lacking location clues, indicating a substantive challenge for this approach.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

- **uncertainty**: Lite-S excludes problematic cases, but the authors state they could not run commercial tools on the modified benchmark; consequently, the filtered comparison does not directly establish commercial-tool performance under that setting.
  - Page 10 · citation: whitespace
  - Quote: "we are not able to run commercial tools ourselves on the modified problems"

Unresolved questions:

- How would AGENTLESS compare with other approaches under matched model access, inference budgets, and evaluation conditions?
- Would the reported performance and cost hold across other repositories, benchmarks, or later benchmark versions?
- How reproducible and robust are the manual problem classifications and the resulting Lite-S subset?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the method and benchmark evaluation details. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark results and the construction and evaluation of SWE-bench Lite-S. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 11}` | Inspect Lite-S results and any stated scope boundaries or limitations. | read pages [10, 11] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using the inspected method, results, and benchmark-analysis pages. | citation_validation_failed; #2: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Resubmit with the page-8 ablation quote copied verbatim from the inspected excerpt. | review accepted | [event 30](trace.jsonl#L30) |
