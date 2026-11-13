# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**agent · ok**

3 model calls · 2 reads · 7.40 s · $0.001085

3 decisions · 3 tool calls · 8139 input tokens (1378 cached) · 472 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

CAMEL proposes a role-playing, inception-prompt framework for two LLM agents to cooperate on tasks, and presents it as both a research tool for studying agent interactions and a way to generate conversational datasets. It is a useful, concrete framework contribution, but the inspected evidence is primarily methodological and illustrative rather than a strong quantitative validation of autonomous task success.

- **strength**: The paper gives explicit system prompts that operationalize reciprocal roles and task-oriented cooperation, making the method concrete and inspectable.
  - Page 7 · citation: whitespace
  - Quote: "We share a common interest in collaborating to successfully complete a task."

- **strength**: The experimental setup and intended outputs are identified: two GPT-3.5-turbo agents, two scenarios, and named conversation datasets.
  - Page 7 · citation: whitespace
  - Quote: "We examined the AI Society and Code scenarios in particular."

- **limitation**: The paper explicitly bounds the scenarios to cooperative assistant-user interactions with shared interests, limiting what this setup alone can establish about broader multi-agent interaction.
  - Page 4 · citation: whitespace
  - Quote: "we focus on studying communicative agents under AI-AI cooperative scenarios where they share pure common interests."

- **uncertainty**: The pages inspected do not establish dataset scale or provide quantitative measures of task completion; fuller results and evaluation detail were not inspected.
  - Page 7 · citation: exact
  - Quote: "We also gathered conversational data, named CAMEL AI Society and CAMEL Code"

Unresolved questions:

- How large and diverse are the released datasets, and what quality-control or filtering was applied?
- What quantitative or independent evaluations establish that agents complete tasks reliably rather than merely produce plausible conversations?
- How sensitive are outcomes to model choice, prompt variations, and the two-agent cooperative setup?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate the paper's evaluation evidence and reported results. | 7 matches on pages [4, 5, 7, 13, 19] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 7, "end": 8}` | Inspect experiments and data claims to assess evidence quality. | read pages [7, 8] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Evidence inspected covers the framing, prompt design, and start of experiments; submit a calibrated review while noting limited inspection. | review accepted | [event 16](trace.jsonl#L16) |
