# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**agent · ok**

6 model calls · 4 reads · 16.55 s · $0.001905

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

CAMEL introduces a role-playing and inception-prompt framework for two LLM agents to collaborate with limited human guidance, alongside scalable conversation-generation pipelines and datasets for AI-society and coding scenarios. Its main contribution is a concrete research scaffold and prompt-design analysis, not evidence of robust real-world task completion.

- **strength**: The approach produces sizeable generated conversation datasets in the stated scenarios.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **strength**: Prompt modifications shift termination behavior, though the paper also reports increased flake messages.
  - Page 12 · citation: normalized
  - Quote: "both modifications considerably increases the number of conversations that terminate with end of task token, and reduce the number of messages with assistant instruction."

- **limitation**: The authors explicitly identify expert evaluation of task completion as a challenge, limiting claims about demonstrated task success.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

Unresolved questions:

- How often do generated conversations yield correct, independently verified task outcomes across domains?
- How well do findings generalize across models and settings with more than two agents?
- What is the quality of the generated conversations under independent human assessment?
- This assessment inspected experimental setup, dataset analysis, and conclusion/limitations, not the full paper or supplementary materials; additional evidence may change the assessment.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 9 reports 25,000 AI Society conversations and 50,000 Code conversations, supporting the claim that the framework generated sizeable datasets in both stated scenarios.
- Observation 2: **supported** — Page 12 reports that both prompt modifications increased end-of-task termination and reduced assistant-instruction terminations, and also reports a significant increase in flake messages. The claim accurately captures these effects.
- Observation 3: **supported** — Page 13 explicitly says that evaluating task-completion capabilities is challenging and requires numerous domain experts. This appropriately qualifies what the paper demonstrates about task success.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate evaluation evidence and reported experimental results. | 7 matches on pages [4, 5, 7, 13, 19] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 7, "end": 9}` | Inspect experiment setup, findings, and evidence for the paper's claims. | read pages [7, 8, 9] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Find the authors' stated scope boundaries and discussion of limitations. | 4 matches on pages [1, 13, 21] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 12, "end": 13}` | Read conclusions and limitations to calibrate the assessment and cite scope. | read pages [12, 13] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.63, "observations": 4}}` | Evidence covers framework, generated datasets, prompt ablations, and explicit evaluation limitations; submit independent assessment. | citation_validation_failed; #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.63, "observations": 3}}` | Resubmit with exact observed quotations and remove unsupported citation; evaluation evidence remains partial. | review accepted | [event 30](trace.jsonl#L30) |
