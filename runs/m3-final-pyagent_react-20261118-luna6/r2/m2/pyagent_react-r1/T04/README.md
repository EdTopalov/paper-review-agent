# T04: AgentBench: Evaluating LLMs as Agents

**pyagent_react · ok**

5 model calls · 2 reads · 27.71 s · $0.002318

5 decisions · 5 tool calls · 30254 input tokens (23444 cached) · 2465 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

AgentBench offers a useful, broad testbed for LLM agents across eight interactive environments and evaluates 25 models. Its varied tasks and explicit interaction procedures are a meaningful contribution, while inspected details show that some environments use simplified setups or model-mediated evaluation. This assessment is limited to excerpts from pages 1–3 and 7–9; I have not inspected the full results, remaining environment descriptions, or appendices.

- **strength**: The benchmark spans diverse tasks and environments, including five introduced in this paper and three adapted from published datasets.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The evaluation specifies task interaction and scoring procedures, including answer comparisons and executable-action metrics.
  - Page 8 · citation: exact
  - Quote: "We use F1 score as the primary evaluation metric in our study"

- **limitation**: The card-game environment is deliberately simplified to accommodate current LLM performance; how this affects transfer to more complex strategic games is unresolved.
  - Page 8 · citation: exact
  - Quote: "The original design of Aquawar could be too complicated for existing LLMs."

- **uncertainty**: The lateral-puzzle host system is based on GPT-3.5 Turbo; the inspected passages do not establish how host-generated responses affect evaluation reliability.
  - Page 9 · citation: whitespace
  - Quote: "we first design an accurate LTP host system based on gpt-3.5-turbo for automatic game playing"

Unresolved questions:

- How stable are the reported model comparisons across repeated runs and prompt variations?
- How much do the benchmark scores generalize to less constrained, real-world agent tasks?
- Full aggregate results, additional environment details, and appendices were not inspected, so this assessment cannot judge those aspects.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark environments and evaluation design. | read pages [2, 3] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 7, "end": 9}` | Inspect reported evaluation results and score aggregation. | read pages [7, 8, 9] | [event 11](trace.jsonl#L11) |
| 3 | submit_review invalid arguments: `` |  | invalid_arguments | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.65, "observations": 4}}` | Assess the benchmark from the supplied paper excerpts and note inspected gaps. | citation_validation_failed; #1: wrong_page (pages [2]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.65, "observations": 4}}` | Correct the citation page for the benchmark breadth claim. | review accepted | [event 25](trace.jsonl#L25) |
