# T19: A Survey on Large Language Model based Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 6.48 s · $0.000606

1 decisions · 0 tool calls · 33041 input tokens (33038 cached) · 550 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

This survey organizes LLM-based autonomous-agent research around construction, applications, and evaluation. Its four-module architecture and broad catalogs of learning strategies, application domains, evaluation approaches, and open challenges provide a useful map of an emerging field. The contribution is primarily a structured synthesis rather than new empirical evidence.

- **strength**: The four-part framework offers a clear organizing structure for comparing diverse agent designs.
  - Page 3 · citation: whitespace
  - Quote: "composed of a profiling module, a memory module, a planning module, and an action module."

- **strength**: The survey covers evaluation as well as architectures and applications, including both human-centered and quantitative approaches.
  - Page 19 · citation: whitespace
  - Quote: "we present two commonly used evaluation strategies for assessing AI agents: subjective and objective evaluation."

- **uncertainty**: The inspected text does not explain how the literature was searched, selected, or coded, so the comprehensiveness and consistency of the survey's coverage are difficult to assess.
  - Page 22 · citation: whitespace
  - Quote: "we have compiled 100 relevant works on LLM-based Agents"

Unresolved questions:

- What search and selection process determined which works were included in the survey and its tables?
- How consistently can the proposed categories be applied to agents that combine multiple memory, planning, or learning approaches?
- How should the surveyed evaluation strategies be combined to assess agent capabilities across different application settings?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
