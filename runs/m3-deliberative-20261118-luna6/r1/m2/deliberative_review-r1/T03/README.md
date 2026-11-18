# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**deliberative_review · ok**

8 model calls · 4 reads · 37.08 s · $0.008001

8 decisions · 5 tool calls · 51448 input tokens (0 cached) · 3166 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AutoGen presents a framework for building LLM applications through conversations among customizable agents backed by models, tools, and people. Its contribution is a flexible agent-and-conversation design illustrated across diverse applications. The paper includes some measured comparisons, but these do not isolate the contribution of multi-agent conversation from other system components.

- **strength**: The central abstraction is clearly described: agents with specific roles can communicate and maintain interaction state.
  - Page 3 · citation: whitespace
  - Quote: "A conversable agent is an entity with a specific role that can send and receive messages to and from other conversable agents"

- **strength**: The application evidence is not limited to demonstrations: one case reports measured results on the first 500 Natural Questions items. Retrieval-augmented Chat has higher reported recall than the listed alternatives, though the table compares whole systems rather than isolating the effect of multi-agent interaction.
  - Page 18 · citation: exact
  - Quote: "Retrieval-augmented Chat (ours) + GPT-3.5 0.2 23.73 66.61"

- **limitation**: The paper also reports a MiniWoB++ comparison, but describes MiniWobChat as comparable to prior work rather than showing a clear advantage. These application-specific results do not establish general superiority over simpler workflows.
  - Page 16 · citation: whitespace
  - Quote: "The results show that MiniWobChat achieves comparable performance with RCI."

- **uncertainty**: The authors identify workflow choice, cost-effectiveness, scale, and oversight as open issues. I inspected selected pages and fragments, not the full paper; therefore this assessment cannot characterize every application, evaluation, or implementation detail.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How much of the reported gains, such as the Natural Questions recall result, is attributable specifically to interactive multi-agent conversation rather than retrieval, prompting, or other system components?
- How often do the example workflows outperform simpler single-agent or pipeline approaches, and at what cost?
- Which design choices—agent count, roles, tools, or interaction pattern—are effective across task types, and how reliably can developers monitor and constrain complex conversations?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the framework design and implementation sections to establish what agent customization, conversation control, tool use, and human participation are actually supported.; Inspect the paper’s examples and any evaluations for evidence that multi-agent conversations improve task outcomes, and distinguish demonstrations from controlled comparisons or measured results.; Inspect discussion and limitations, and check whether claims about broad applicability and simplified workflows are qualified elsewhere; only page 1 is currently available, so the remaining 27 pages need review. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [2, 3] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [23, 24, 25] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The summary says the inspected material supports AutoGen’s value as an “implementation framework,” but the reviewed excerpts mainly describe its design and capabilities; detailed implementation sections were not inspected. Qualify this or inspect the relevant pages before retaining the claim.; The draft appropriately limits its conclusions about comparative performance, but most application and evaluation pages remain unread. A targeted read is needed to establish what evidence the paper reports, without treating the current gap as evidence that no such res … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [16, 17, 18] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Qualified the claim about implementation support, as the inspected passages chiefly establish design and example workflows. Incorporated the newly supplied measured comparisons: the Natural Questions results and the MiniWoB++ comparison. These show application-specific evidence, not a general or isolated multi-agent advantage. Preserved uncertainty because most application pages remain unread. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Limitations"}` | Inspect the paper's qualifications and limitations, counterbalancing broad claims on page 1. | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 3}` | Inspect design details on agent customization and conversation framework to support evaluation. | read pages [2, 3] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 23, "end": 25}` | Inspect the paper’s discussion, limitations, and closing claims to assess scope and risks. | read pages [23, 24, 25] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 16, "end": 18}` | Inspect application examples and outcome comparisons for measured evidence. | read pages [16, 17, 18] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
