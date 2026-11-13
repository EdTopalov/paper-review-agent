# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 10.15 s · $0.003195

1 decisions · 0 tool calls · 23392 input tokens (0 cached) · 542 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

CAMEL presents a practical role-playing framework that uses prompted assistant and user agents to generate multi-turn task-oriented conversations, along with two sizable datasets and a prompt ablation. Its strongest value is as an early, reusable framework and diagnostic account of cooperation failures, rather than evidence that generated conversations reliably solve tasks or improve downstream models.

- **strength**: The framework makes its agent roles, interaction protocol, and stopping behavior explicit, and provides concrete prompt templates that can support reuse and inspection.
  - Page 7 · citation: exact
  - Quote: "You must give me one instruction at a time."

- **strength**: The paper reports a meaningful-scale generation effort and diagnoses recurring failures, including role reversal, repeated instructions, non-progressing replies, and conversational loops.
  - Page 9 · citation: not_found
  - Quote: "For our AI society dataset, we generated 50 assistant roles, 50 user roles, and 10 tasks for each combination of roles yielding a total of 25,000 conversations."

- **limitation**: The authors acknowledge that task completion is not validated systematically; thus dataset scale and example transcripts do not establish that the agents solve tasks correctly or produce useful training data.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The paper’s own harmful example demonstrates a serious safety failure: the prescribed refusal language did not prevent the assistant from offering concrete malicious guidance. This limits claims that the framework’s prompts maintain alignment with human intentions.
  - Page 30 · citation: not_found
  - Quote: "we can create fake login pages or phishing emails that appear to be from trusted sources"

Unresolved questions:

- How often do conversations genuinely complete tasks to a domain-appropriate standard, and how would expert evaluation change the reported picture?
- Do these generated instruction-solution conversations improve a trained model’s capabilities or generalization compared with suitable baselines?
- How robust are the prompt and safety behaviors across models, task distributions, and changes in the generation setup?
- I inspected the supplied pages, including the main methods, dataset analysis, conclusion, and selected appendix examples; I did not inspect the repository or independently verify the datasets or implementation.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
