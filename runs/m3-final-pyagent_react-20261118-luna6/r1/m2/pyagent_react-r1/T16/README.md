# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**pyagent_react · ok**

7 model calls · 4 reads · 18.19 s · $0.002499

7 decisions · 6 tool calls · 52423 input tokens (41000 cached) · 1324 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

The paper presents a role-playing framework in which AI user and assistant agents use inception prompts to autonomously generate task-oriented conversations, along with AI Society and Code datasets and an open-source research library. Its contribution is a practical setup for studying agent cooperation and producing conversational data. Evidence is mainly descriptive and includes prompt-ablation analysis; the authors leave broad task-completion evaluation to future work.

- **strength**: The framework gives the AI user a planning role and the assistant an execution role, making their intended division of labor explicit.
  - Page 5 · citation: whitespace
  - Quote: "The AI user serves as a task planner, engaging in interactive planning to determine feasible steps for the AI assistant to execute."

- **strength**: The paper reports that two prompt modifications changed termination outcomes, providing empirical analysis of prompt design in this setup.
  - Page 12 · citation: normalized
  - Quote: "both modifications considerably increases the number of conversations that terminate with end of task token"

- **limitation**: The authors acknowledge that they do not establish how often the generated conversations actually solve their tasks, because this evaluation would require domain experts.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **uncertainty**: The experiments described here use two GPT-3.5-turbo agents; transfer to other models remains an open question in the inspected pages.
  - Page 7 · citation: whitespace
  - Quote: "We examined the AI Society and Code scenarios in particular."

Unresolved questions:

- How accurate, useful, or complete are the generated solutions when assessed by domain experts?
- How robust are the interaction patterns and prompt-ablation findings across other models and settings?
- I inspected pages 1–13 only; details and evidence elsewhere in the 34-page paper, including supplementary material, were not examined.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the framework and stated contributions. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect prompting details and experimental setup. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 10}` | Review reported outcomes and dataset evidence. | read pages [8, 9, 10] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 11, "end": 13}` | Inspect dataset analysis, evaluation, and limitations. | read pages [11, 12, 13] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Submit a balanced assessment based on the inspected framework, experiment, and limitation pages. | citation_validation_failed; #1: wrong_page (pages [5]); #4: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Correct citations using exact observed excerpts and their matching page numbers. | review accepted | [event 35](trace.jsonl#L35) |
