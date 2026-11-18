# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

7 model calls · 5 reads · 20.78 s · $0.003512

7 decisions · 7 tool calls · 48086 input tokens (26139 cached) · 1059 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench contributes a broad interactive benchmark spanning eight text-operable environments and evaluates 25 API and open models, with a reusable toolkit. Its breadth and concrete environment designs make it useful for studying agent behavior, though task-specific evaluation procedures—especially model-assisted judging—leave measurement-validity questions unresolved in the portions inspected.

- **strength**: The benchmark’s principal contribution is substantial breadth: it combines newly created environments with reformulated existing ones and tests models across diverse agent tasks.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper reports a broad model evaluation and provides an integrated evaluation toolkit, supporting use beyond a conceptual proposal.
  - Page 3 · citation: exact
  - Quote: "We perform a thorough evaluation of 25 different LLMs using AgentBench"

- **limitation**: The LTP host system is GPT-3.5 based, and automatic checking also uses GPT-3.5 outputs, making evaluation quality dependent on that component.
  - Page 9 · citation: whitespace
  - Quote: "In this dataset, we first design an accurate LTP host system based on gpt-3.5-turbo for automatic game playing"

- **uncertainty**: The authors acknowledge the benchmark remains an evolving coverage effort; I did not inspect the full quantitative results or validation analyses, so strength and robustness of model comparisons remain uncertain here.
  - Page 3 · citation: exact
  - Quote: "Lastly, there are definitely more scenarios and tasks to cover in LLM-as-agent evaluation."

Unresolved questions:

- How robust are aggregate model rankings to task-specific scoring choices and model-assisted LTP judging?
- What quantitative uncertainty estimates or repeated-run analyses support the reported comparisons?
- How well do these environments and scores generalize to agents operating in real-world settings?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope limits and caveats for a balanced assessment. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark rationale and environment design to assess contribution and scope. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review evaluation setup and reported quantitative results for evidence quality. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "GPT-3.5"}` | Check evaluation dependence on a model-based judge or host, relevant to measurement limitations. | 8 matches on pages [3, 6, 9, 10] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 16, "end": 18}` | Inspect aggregate results and discussion to connect benchmark design with empirical support. | read pages [16, 17, 18] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers the benchmark’s design, sample evaluation methods, and conclusion; submit a provisional assessment noting quantitative results were not inspected. | citation_validation_failed; #3: not_found | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with verbatim evaluation-procedure evidence from page 9 after citation validation rejected the paraphrased page-10 quote. | review accepted | [event 37](trace.jsonl#L37) |
