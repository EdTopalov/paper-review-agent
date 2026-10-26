# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 5.79 s · $0.004738

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.72

AgentBench makes a substantial benchmark contribution: it brings eight interactive environments and a shared evaluation toolkit to the assessment of LLM agents, then applies them to 25 models. The results support a marked gap between the tested commercial and medium-sized open models, while the paper also identifies meaningful limits in task coverage and evaluation reliability. The conclusions should be read as results for this benchmark’s particular task selections, prompts, model versions, and scoring procedures—not as a universal measure of agent capability.

- **strength**: The benchmark spans diverse interactive settings and reports concrete task-specific metrics, offering a broader evaluation setup than a single-environment study.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments"

- **strength**: The authors provide a reproducible evaluation design in principle, including a common toolkit interface and Docker-packaged environments.
  - Page 13 · citation: whitespace
  - Quote: "they only need to setup a model server with standard format chatting API required by AgentBench."

- **limitation**: The aggregate score depends on benchmark-specific weights derived from the evaluated models’ average task scores; comparisons beyond this evaluated set may therefore require care.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

- **limitation**: One environment’s automated evaluation has acknowledged measurement error: the host/evaluation process can be more tolerant than human judgment, particularly for open models.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation"

Unresolved questions:

- How stable are model rankings across different task samples, prompt choices, and repeated runs? The paper reports point results, but the inspected pages do not provide uncertainty estimates.
- How much do the reported performance gaps depend on model version and evaluation configuration, especially for the web-browsing setup, which the paper says differs from the source benchmark’s top-k and prompting settings?
- I inspected the supplied pages, including the main benchmark description, results, and selected appendices, but did not independently verify the datasets, toolkit, or full item-level evaluation procedures.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes eight distinct environments spanning settings such as operating systems, databases, games, household tasks, and web interaction, and reports environment-specific metrics (PDF pp. 2, 13). This supports the claim of breadth relative to a single-environment study.
- Observation 2: **supported** — The toolkit uses a standard chat API interface and packages complex environments in Docker images, and the paper says the datasets, environments, and evaluation package are released (PDF pp. 3, 13). The qualification “in principle” appropriately avoids asserting that every run is automatically reproducible.
- Observation 3: **supported** — The overall score weights each task by the reciprocal of its average score across the tested models (PDF p. 14). Because the weights are tied to that evaluated set, care is warranted when interpreting comparisons involving a different model set.
- Observation 4: **supported** — The appendix explicitly reports that automatic LTP evaluation can be more tolerant of agents than human evaluation, making SGA and QR appear better, especially for open-source models (PDF p. 30).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\"score\":0.72,\"summary\":\"AgentBench makes a substantial benchmark contribution: it brings eight interactive environments and a shared evaluation toolkit to the assessment of LLM agents, then applies them to 25 models. The results support a marked gap between the tested commercial and medium-sized open models, while the paper also identifies meaningful limits in task coverage and evaluation reliability. The conclusions should be read as results for this benchmark’s particular task selections, prompts, model versions, and scoring procedures—not as a universal measure of agent capability.\",\"observations\":[{\"kind\":\"strength\",\"claim\":\"The benchmark spans diverse interactive settings and reports concrete task-specific metrics, offering a broader evaluation setup than a single-environment study.\",\"page\":2,\"quote\":\"AgentBench encompasses 8 distinct environments\"},{\"kind\":\"strength\",\"claim\":\"The authors provide a reproducible evaluation design in principle, including a common toolkit interface and Docker-packaged environments.\",\"page\":13,\"quote\":\"they only need to setup a model server with standard format chatting API required by AgentBench.\"},{\"kind\":\"limitation\",\"claim\":\"The aggregate score depends on benchmark-specific weights derived from the evaluated models’ average task scores; comparisons beyond this evaluated set may therefore require care.\",\"page\":14,\"quote\":\"we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight.\"},{\"kind\":\"limitation\",\"claim\":\"One environment’s automated evaluation has acknowledged measurement error: the host/evaluation process can be more tolerant than human judgment, particularly for open models.\",\"page\":30,\"quote\":\"automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation\"}],\"unresolved_questions\":[\"How stable are model rankings across different task samples, prompt choices, and repeated runs? The paper reports point results, but the inspected pages do not provide uncertainty estimates.\",\"How much do the reported performance gaps depend on model version and evaluation configuration, especially for the web-browsing setup, which the paper says differs from the source benchmark’s top-k and prompting settings?\",\"I inspected the supplied pages, including the main benchmark description, results, and selected appendices, but did not independently verify the datasets, toolkit, or full item-level evaluation procedures.\"]}",
  "observation": {}
}
```

</details>
