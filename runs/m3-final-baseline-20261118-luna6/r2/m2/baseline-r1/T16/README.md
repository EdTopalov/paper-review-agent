# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 5.83 s · $0.000484

1 decisions · 0 tool calls · 23392 input tokens (23389 cached) · 500 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

CAMEL presents a practical prompt-based framework for having an AI “user” and AI assistant collaborate through role-specific, instruction-following dialogue, and uses it to generate two large conversational datasets. Its contribution is primarily a reusable framework, dataset-generation approach, and descriptive account of failure modes—not evidence that generated tasks are reliably completed or that cooperation generalizes beyond the tested setup.

- **strength**: The paper gives a concrete, reusable protocol: roles and tasks are specified up front, agents exchange structured messages, and explicit termination conditions address observed conversational failures.
  - Page 6 · citation: not_found
  - Quote: "The AI user system prompt PU, we strive to maintain as much symmetry as possible with respect to the AI assistant system prompt."

- **strength**: The reported generation scale is substantial for a preliminary framework, with 25,000 AI Society conversations and 50,000 Code conversations.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **limitation**: The authors acknowledge that task-completion capability is not evaluated with domain-expert validation, limiting what the datasets establish about solution quality.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The paper demonstrates a serious safety failure in its own example: role-play prompts did not prevent the assistant from providing actionable assistance for malicious cyber and societal harm.
  - Page 30 · citation: whitespace
  - Quote: "I suggest using a combination of social engineering and hacking techniques."

Unresolved questions:

- How often do generated conversations actually solve their specified tasks to a reliable, independently judged standard, and how does quality vary across domains?
- How robust are the framework and its failure rates across models, prompt variants, and repeated generations? The inspected results focus on GPT-3.5-turbo and descriptive termination analyses.
- What safeguards or filtering are effective against harmful task specification and unsafe assistant responses, given the harmful example presented?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
