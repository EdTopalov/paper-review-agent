# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 7.23 s · $0.000485

1 decisions · 0 tool calls · 23392 input tokens (23389 cached) · 502 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.56

CAMEL presents a prompt-engineered, two-agent role-playing framework for turning an initial idea into an extended assistant–user dialogue, and uses it to generate two large conversational datasets. Its clearest contribution is a practical framework and analysis of cooperation failure modes—not demonstrated autonomous task competence or alignment. The paper is an exploratory, useful dataset-and-tools contribution, with evidence mainly in generated conversation counts, termination statistics, and illustrative examples.

- **strength**: The framework’s concrete prompt structure and termination rules make the proposed interaction setup reproducible in principle, and the paper identifies several operational failure modes rather than treating dialogue as reliably cooperative.
  - Page 6 · citation: not_found
  - Quote: "The AI user continuously provides instructions and necessary inputs until you think the task is completed."

- **strength**: The authors report substantial generated corpora: 25,000 AI Society and 50,000 Code conversations. This supports the value of the work as a data-generation and exploration resource, though not by itself data quality or task success.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **limitation**: The paper explicitly says evaluating task completion at this diversity and scale would require domain experts. Consequently, the paper does not establish that generated dialogues reliably solve their stated tasks; the trading-bot example also illustrates that limitation rather than providing a validated implementation.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The demonstrated setup uses two GPT-3.5-turbo agents, so claims about broader multi-agent settings or other models remain untested in the inspected experiments.
  - Page 7 · citation: not_found
  - Quote: "we employed two gpt-3.5-turbo agents"

Unresolved questions:

- How often do generated conversations produce correct, complete, and useful task solutions under independent domain-expert evaluation?
- How robust are the reported outcomes to different underlying models, prompt variants, sampling settings, and repeated runs?
- What are the measured rates and practical consequences of harmful outputs across the datasets, beyond the included illustrative harmful conversation?
- I inspected the supplied pages, including the main methodology, experiments, conclusion, and appendices; the results are reported mainly through figures whose underlying numerical values are not transcribed here, so I cannot assess detailed rates or statistical uncertainty.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
