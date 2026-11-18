# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**deliberative_review · ok**

7 model calls · 3 reads · 33.15 s · $0.008215

7 decisions · 4 tool calls · 53270 input tokens (0 cached) · 3133 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

τ-bench introduces a modular benchmark for evaluating agents that converse with simulated users, use domain APIs, and follow written policies in retail and airline tasks. It scores annotated database outcomes and user-facing information, and proposes pass^k to measure repeated-trial reliability. Results across tested models reveal low task success and substantial consistency challenges.

- **strength**: The benchmark combines tool outcomes with user-facing response requirements in its scoring, giving a concrete evaluation target for multi-turn tasks.
  - Page 4 · citation: whitespace
  - Quote: "The reward of a task episode r = raction × routput ∈ {0, 1} is based on (1) whether the final database is identical to the unique ground truth outcome database (raction), and (2) whether the agent’s responses to the user contain all necessary information (routput)."

- **strength**: The tested agents show meaningful failure and reliability challenges: even the strongest reported agent has low airline success, and repeated success falls substantially in retail.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: The authors explicitly bound the benchmark’s realism: its schemas, APIs, and rules are simplified. The benchmark also covers two domains and 165 tasks, so the supplied evidence does not establish broad domain coverage.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

- **uncertainty**: The paper uses an LM-simulated user, but the observed pages do not establish how well those interactions represent real users. Only pages 1–8 were supplied for inspection; pages 9–50, including later discussion and appendices, remain uninspected.
  - Page 3 · citation: whitespace
  - Quote: "We use a language model (gpt-4-0613) to simulate a human user interacting with the agent."

Unresolved questions:

- How do results change with real users or an independently developed user simulator?
- Do the two domains and 165 tasks generalize to substantially different domains and interaction patterns?
- What additional validation, caveats, or experiments are discussed on pages 9–50? Those pages were not available for inspection here.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark design and task/policy construction sections to verify that the airline and retail environments meaningfully test user interaction, tool use, and domain-rule following, and to identify scope boundaries.; Inspect evaluation methodology and results, including state comparison, simulated-user setup, baselines, and pass^k, to assess whether evidence supports the reported success and reliability claims.; Check later discussion, limitations, and appendices for validation of benchmark realism, simulator or metric caveats, and additional experiments; only page 1 is curren … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 4, 5, 6] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [6, 7, 8] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [3, 4, 5] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The page 6 limitation observation says the benchmark has few tasks relative to broad real-world deployment settings, but its quoted passage only supports that the domains are simplified. The draft does not cite evidence for the task-count comparison. The paper reports 115 retail and 50 airline tasks (page 5), so qualify or substantiate this claim.; The required later discussion and appendix inspection remains outstanding. The draft appropriately acknowledges this gap, but the evaluation should not imply the unresolved questions are settled without that targeted  … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Qualified the scope observation: the paper reports two domains and 165 tasks, rather than claiming an unsupported comparison to broad deployment settings. Updated the ledger to reflect the actual supplied coverage. The requested pages 9–50 were not included among the observed sources, so I preserve uncertainty about their contents rather than treating the earlier draft’s uncertainty as settled. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "pass^k"}` | Locate evaluation and results evidence addressing reliability claims. | 8 matches on pages [1, 2, 4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect benchmark construction, simulator/evaluation details, and results to substantiate claims and limitations. | read pages [6, 7, 8] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark construction and evaluation details, including simulator and pass^k definition. | read pages [3, 4, 5] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
