# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 7.97 s · $0.004806

1 decisions · 0 tool calls · 36072 input tokens (0 cached) · 595 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AgentBench introduces an eight-environment interactive benchmark for evaluating language models as agents and reports results for 25 API-based and open-source models. Its breadth, executable environments, and released evaluation toolkit make it a useful contribution, while heterogeneous task metrics and some reliance on model-based evaluation complicate interpretation of aggregate results. The assessment is based on the supplied paper text, including its appendices; I have not independently inspected or run the released code or datasets.

- **strength**: The benchmark spans varied interactive settings and the paper describes concrete task construction and evaluation procedures across them, rather than relying on a single agent domain.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The evaluation covers a broad set of models and reports both overall and environment-specific results, supporting comparisons within the benchmark’s chosen setup.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The paper itself notes that automatic evaluation of the lateral-puzzle host can be more tolerant than human evaluation, which weakens confidence in some LTP metrics, especially for open models.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation"

- **limitation**: The overall score combines different task metrics using weights derived from the evaluated models’ average scores; this gives a standardized summary, but its interpretation depends on this particular model set and weighting rule.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

Unresolved questions:

- How robust are the model rankings to alternative overall-score aggregation choices, and to changes in which models are included when computing the weights?
- How much do LTP results and the reported cross-model comparisons change under human evaluation or a separately validated host and scoring system?
- How stable are results across repeated runs or alternative prompts, particularly for tasks involving stochastic environments or gameplay? The supplied text does not establish this uncertainty.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
