# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**deliberative_review · ok**

7 model calls · 3 reads · 32.41 s · $0.008113

7 decisions · 4 tool calls · 53889 input tokens (1299 cached) · 3072 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

τ-bench introduces a benchmark for evaluating tool-using agents in simulated, multi-turn user interactions where agents must follow domain policies. It pairs database-state and response checks with pass^k, a metric for reliability across repeated trials. Reported baselines reveal substantial task-success and consistency challenges, while the two-domain scope and simulated users leave real-world generalization uncertain.

- **strength**: The benchmark combines user interaction, API use, domain policies, and annotated outcomes, with an automated reward based on database changes and required response information.
  - Page 4 · citation: whitespace
  - Quote: "The reward of a task episode r = raction × routput ∈ {0, 1} is based on (1) whether the final database is identical to the unique ground truth outcome database (raction), and (2) whether the agent’s responses to the user contain all necessary information (routput)."

- **strength**: The repeated-trial metric targets reliability, and reported results show a marked gap between average task success and consistent success.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: The benchmark is instantiated in two synthesized domains; the inspected evidence does not establish generalization to a broader range of real-world settings.
  - Page 5 · citation: exact
  - Quote: "Using the above procedures, we modularly construct two domains, τ-retail and τ-airline."

- **uncertainty**: The authors acknowledge limitations of LM-simulated users, but the inspected material does not establish how well simulator behavior or benchmark outcomes correspond to interactions with real users.
  - Page 9 · citation: whitespace
  - Quote: "The simulated user can have some limitations:"

Unresolved questions:

- How do benchmark results change with real human users, or with user simulators other than the one used in the reported experiments?
- How robust are the task annotations and reward checks to alternative valid dialogue and policy-compliant outcomes?
- The supplied excerpts cover only pages 1–9 of a 50-page paper. Detailed appendices and other evaluation material were not inspected, so conclusions about full validation and results remain incomplete.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark design and task construction for the retail and airline domains, including how user simulators, APIs, policies, and goal states are specified; the supplied excerpt establishes the motivation but not these implementation details.; Check the evaluation results and methodology for the claims that leading agents succeed on fewer than half of tasks and have low pass^8 reliability, including baselines, trial counts, and how pass^k is computed.; Inspect the paper’s discussion of validation, limitations, and scope to determine what evidence supports realism and generaliza … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 4, 5, 6] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [7, 8, 9] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [3, 4, 5] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The third observation says the reported evaluation covers only retail and airline, but its page 9 quote supports the separate claim about possible curation bias, not the two-domain scope. Replace the quote with a page 5 quote about constructing two domains, or remove that clause. The other observations are appropriately qualified and their quotes match the supplied pages.; The ledger incorrectly lists E10 as counterevidence for C2 and E15 as counterevidence for C3; both sources support the corresponding findings. Correct those entries. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the mismatched page 9 quotation for the two-domain scope claim with a directly supporting page 5 quotation. Corrected ledger source classifications: E10 and E15 support their respective findings, not counterevidence. The score is unchanged; the limited inspected coverage remains explicit. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "pass^k"}` | Locate evaluation methodology and results for reliability claims. | 8 matches on pages [1, 2, 4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark construction details and evidence for validation/limitations. | read pages [7, 8, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark construction and pass-k methodology, including counterevidence for scope. | read pages [3, 4, 5] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
