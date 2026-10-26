# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 5.55 s · $0.003616

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.68

InterCode contributes an extensible framework for evaluating coding agents through iterative code execution and environment feedback, with Bash and SQL benchmarks adapted from existing datasets. Its experiments demonstrate that interaction and prompting strategies can improve success rates over single-turn generation, while exposing context-discovery and long-horizon reasoning challenges. This is useful benchmark infrastructure and an empirical demonstration, though the task coverage and evaluation setups are limited.

- **strength**: The paper provides a modular task-construction interface and concrete Bash and SQL implementations, making its framework more than a conceptual proposal.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: The reported experiments show substantial gains for some models in the interactive setting; for example, GPT-4’s SQL success rate rises from 9.1% to 73.7%.
  - Page 6 · citation: whitespace
  - Quote: "with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The benchmark’s breadth is limited in this version: its implemented environments cover Bash and SQL, and the CTF demonstration has very few instances.
  - Page 9 · citation: whitespace
  - Quote: "the CTF dataset is limited to just four task instances due to our manual curation procedure."

- **uncertainty**: Reported reward and success depend on environment-specific grading choices, including exact ordering for SQL outputs and lexical similarity for Bash output. How these choices affect comparisons with alternative correct solutions remains an open question.
  - Page 5 · citation: whitespace
  - Quote: "only a correctly ordered list with the exact set of records found in the gold output receives a score of 1."

Unresolved questions:

- How well do findings from these adapted Bash and SQL tasks generalize to other languages, environments, and interactive coding tasks?
- How sensitive are model rankings and success rates to the custom reward definitions and to acceptable equivalent outputs?
- Can the benchmark support reproducible comparisons across model/API changes and varied interaction budgets?
- I inspected the supplied pages, including the main experiments and selected appendices, but did not independently verify the linked code or inspect every supplemental prompt, trajectory, and appendix analysis.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a modular construction workflow with environment, data, and reward components (PDF p. 4), and the appendix specifies the interface and concrete Bash and SQL implementations (PDF pp. 14–19).
- Observation 2: **supported** — The reported SQL results show GPT-4 rising from 9.1% in Single Turn to 73.7% in Try Again (PDF pp. 6–7), supporting the stated example and the qualified claim of gains for some models.
- Observation 3: **supported** — The paper says its current environments cover Bash and SQL and that the CTF dataset has four instances (PDF p. 9); it reiterates both limitations in the appendix (PDF p. 26).
- Observation 4: **supported** — The paper specifies lexical similarity for Bash output grading (PDF pp. 5, 16) and an SQL reward that penalizes incorrect record ordering, with full reward only for the exact ordered result (PDF pp. 5, 19). The question about how these choices affect comparisons with alternative correct outputs is appropriately framed as unresolved.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\"score\":0.68,\"summary\":\"InterCode contributes an extensible framework for evaluating coding agents through iterative code execution and environment feedback, with Bash and SQL benchmarks adapted from existing datasets. Its experiments demonstrate that interaction and prompting strategies can improve success rates over single-turn generation, while exposing context-discovery and long-horizon reasoning challenges. This is useful benchmark infrastructure and an empirical demonstration, though the task coverage and evaluation setups are limited.\",\"observations\":[{\"kind\":\"strength\",\"claim\":\"The paper provides a modular task-construction interface and concrete Bash and SQL implementations, making its framework more than a conceptual proposal.\",\"page\":4,\"quote\":\"This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting.\"},{\"kind\":\"strength\",\"claim\":\"The reported experiments show substantial gains for some models in the interactive setting; for example, GPT-4’s SQL success rate rises from 9.1% to 73.7%.\",\"page\":6,\"quote\":\"with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task.\"},{\"kind\":\"limitation\",\"claim\":\"The benchmark’s breadth is limited in this version: its implemented environments cover Bash and SQL, and the CTF demonstration has very few instances.\",\"page\":9,\"quote\":\"the CTF dataset is limited to just four task instances due to our manual curation procedure.\"},{\"kind\":\"uncertainty\",\"claim\":\"Reported reward and success depend on environment-specific grading choices, including exact ordering for SQL outputs and lexical similarity for Bash output. How these choices affect comparisons with alternative correct solutions remains an open question.\",\"page\":5,\"quote\":\"only a correctly ordered list with the exact set of records found in the gold output receives a score of 1.\"}],\"unresolved_questions\":[\"How well do findings from these adapted Bash and SQL tasks generalize to other languages, environments, and interactive coding tasks?\",\"How sensitive are model rankings and success rates to the custom reward definitions and to acceptable equivalent outputs?\",\"Can the benchmark support reproducible comparisons across model/API changes and varied interaction budgets?\",\"I inspected the supplied pages, including the main experiments and selected appendices, but did not independently verify the linked code or inspect every supplemental prompt, trajectory, and appendix analysis.\"]}",
  "observation": {}
}
```

</details>
