# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**deliberative_review · ok**

7 model calls · 3 reads · 29.98 s · $0.005174

7 decisions · 4 tool calls · 31458 input tokens (1177 cached) · 2774 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.57

CAMEL presents a role-playing framework in which two language-model agents use inception prompts to conduct task-oriented conversations, and uses the framework to generate AI Society and Code conversation datasets. Its concrete prompt designs and dataset-generation procedure make it a useful exploratory resource. However, the inspected evidence leaves task-completion effectiveness unresolved. Inspection was limited: 25 of the paper’s 34 pages were uninspected, including substantial portions of its experiments and analyses.

- **strength**: The paper provides concrete prompt instructions for assigning complementary roles and directing cooperation.
  - Page 7 · citation: exact
  - Quote: "We share a common interest in collaborating to\nsuccessfully complete a task."

- **limitation**: The authors report interaction failures, including unproductive replies. These are observed challenges, not evidence that the framework fails overall.
  - Page 9 · citation: normalized
  - Quote: "We also observed instances where the assistant agent responds with a\nflake reply"

- **uncertainty**: The authors say task-completion assessment requires domain experts; effectiveness therefore remains unresolved in the inspected material.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

Unresolved questions:

- How often do conversations complete their assigned tasks successfully, and how is that success assessed?
- How do the reported interaction failures vary across tasks, roles, or models?
- How representative and useful are the generated datasets beyond the described role and task combinations?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the paper’s method and examples to verify how inception prompting and role-playing produce autonomous cooperation, and whether the central framework claims are supported by concrete evidence.; Check later pages for experiments, evaluations, or generated-data analyses that support claims about scalability and agent capabilities; only page 1 is currently observed, so support may appear elsewhere.; Review the paper’s stated limitations and scope, then select 2–4 page-specific observations with verbatim quotes and page numbers, distinguishing demonstrated weaknesses from unanswered … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 4 matches on pages [1, 13, 21] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 5 matches on pages [1, 2, 3, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation’s quote is not verified on the cited page 7; the matching wording appears in the partial page 6 material (E9/E10). Correct the page citation or use a verbatim quote confirmed on page 7.; The draft should explicitly state the inspection gap: 25 of 34 pages were uninspected, including substantial portions of the experiments and analyses. Its qualified wording helps, but the extent of that gap is not made clear.; Target: Verify the first observation’s quote against the PDF page and revise its citation; add a concise statement that 25 pages wer … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Corrected the first observation to use a quotation verified in the observed page 7 material, and explicitly stated the inspection gap. No score change: the available evidence supports a useful exploratory contribution while leaving effectiveness uncertain. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Limitations"}` | Check whether the paper states scope limitations, and inspect evidence beyond the provided first page. | 4 matches on pages [1, 13, 21] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "inception prompting"}` | Inspect method and concrete evidence for role-playing framework claims. | 5 matches on pages [1, 2, 3, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect concrete experiments/examples and generated data evidence supporting the framework claims. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.57, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
