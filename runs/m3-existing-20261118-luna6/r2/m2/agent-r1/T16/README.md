# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**agent · ok**

6 model calls · 4 reads · 14.43 s · $0.001602

6 decisions · 6 tool calls · 30103 input tokens (22881 cached) · 979 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

CAMEL presents a prompt-driven role-playing framework for two LLM agents to cooperate with limited human intervention, alongside scalable pipelines and datasets for AI-society and coding conversations. Its useful contribution is a practical framework and empirical analysis of role-play failures and prompt-design tradeoffs, but evidence emphasizes generated-conversation behavior rather than verified real-world task completion.

- **strength**: The work specifies role prompts and constructs large conversational datasets in two settings, making the framework useful for studying multi-agent interaction.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **strength**: Prompt ablations change termination outcomes, while the discussion also reports an adverse tradeoff in flake messages.
  - Page 12 · citation: normalized
  - Quote: "both modifications considerably increases the number of conversations that terminate with end of task token"

- **limitation**: The authors note that assessing task completion across generated tasks requires domain expertise; dialogue scale is not equivalent to validated task success.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **uncertainty**: Inspected experiments use GPT-3.5-turbo agents; broader models and settings remain unestablished by the passages reviewed. Important gaps: I inspected the setup, dataset analysis, and conclusion/limitations, not the full paper's detailed figures or supplemental conversations.
  - Page 7 · citation: exact
  - Quote: "In our experiments, we employed twogpt-"

Unresolved questions:

- How often do generated conversations yield correct, useful outcomes under independent domain-expert evaluation?
- Do the findings generalize beyond GPT-3.5-turbo and two-agent assistant-user scenarios?
- What quantitative sample sizes and uncertainty estimates support the prompt-ablation comparisons?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate evaluation results to assess evidence for the proposed agent framework. | 7 matches on pages [4, 5, 7, 13, 19] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 7, "end": 9}` | Inspect experimental setup and reported observations for concrete evidence and methodological limits. | read pages [7, 8, 9] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check the authors' explicit scope boundaries and unresolved constraints. | 4 matches on pages [1, 13, 21] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 12, "end": 13}` | Read conclusions and limitations verbatim to ground the final assessment. | read pages [12, 13] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Evidence covers the framework, dataset-scale experiments, prompt ablation, and author-stated evaluation limitations. | citation_validation_failed; #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Correct citation mismatches using exact observed page text and retain explicit scope caveats. | review accepted | [event 30](trace.jsonl#L30) |
