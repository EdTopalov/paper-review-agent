# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 7.30 s · $0.000495

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 656 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hosted, interactive web environment and an 812-task benchmark for evaluating agents on realistic, multi-step web tasks. Its functional evaluation and reproducible setup make it a useful platform for agent research, while baseline results illustrate the difficulty of the tasks. The evidence is bounded by the selected websites, benchmark construction, and a small set of baseline agents.

- **strength**: The benchmark pairs realistic, multi-step tasks with programmatic checks of task outcomes, rather than requiring an agent to reproduce a single action sequence.
  - Page 2 · citation: exact
  - Quote: "accommodates a range of potential valid paths to achieve the same goal"

- **strength**: The authors support reproducible evaluation with a standalone environment and a stated reset procedure.
  - Page 16 · citation: whitespace
  - Quote: "the image is easy to distribution containing all the pre-populated websites for reproducible evaluation"

- **limitation**: The environment covers a deliberately selected set of site categories and a geographically limited map, so its representativeness beyond that scope is not established.
  - Page 16 · citation: exact
  - Quote: "confining our focus to the northeast US region due to data storage constraints."

- **uncertainty**: One information-seeking evaluation uses an LLM-based fuzzy match, but the supplied paper does not establish how reliable that judge is or how sensitive benchmark results are to it.
  - Page 7 · citation: not_found
  - Quote: "we utilize a language model to assess whether ˆa accurately captures the key concepts presented in a∗."

Unresolved questions:

- How robust are the benchmark scores to alternative evaluation choices, especially the LLM-based fuzzy matching and recall-oriented criteria?
- How well do the tasks and results generalize to other web domains, regions, user roles, or agents beyond the reported text-based GPT-3.5 and GPT-4 baselines?
- The paper reports a GPT-4 success rate of 10.59% in the abstract and Table 3, but 10.63% in the Results prose; which value is correct?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
