# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 9.22 s · $0.004910

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.74

τ-bench contributes a benchmark for evaluating agents across simulated user conversations, API use, domain rules, and repeated-trial consistency. Its two customer-service domains, annotated database outcomes, and pass^k metric make agent reliability testable at scale. Reported experiments show substantial failure rates for the tested agents, though the benchmark’s simulated users, narrow domain coverage, and outcome-based reward constrain how broadly those results transfer.

- **strength**: The benchmark combines conversational interaction, tool use, and domain-policy adherence, while its database-state evaluation enables automated scoring across varied dialogue trajectories.
  - Page 4 · citation: wrong_page
  - Quote: "This allows for objective measurement of the agent’s decision making"

- **strength**: The evaluation includes repeated trials to measure consistency, and the experiments show that success can decline notably across trials for the strongest tested agent.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%"

- **limitation**: The authors acknowledge that matching the expected database state does not fully establish policy compliance, so the automated reward can miss some rule violations.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

- **limitation**: The reported evaluation is limited to two customer-service domains, and the authors describe broader, more complex domains as future work; transfer to those settings remains untested here.
  - Page 5 · citation: whitespace
  - Quote: "more advanced domains (e.g., medical, tax, or legal) with more complex data and rules can be studied"

Unresolved questions:

- How closely do the LM-simulated users and synthetic tasks predict agent performance in interactions with real users?
- How would the benchmark’s rankings or pass^k results change under additional domains, user simulators, or real-user evaluation?
- Can systematic checks reliably detect policy violations that leave the expected database state unchanged?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The benchmark is described as combining interaction with simulated users, API tools, and domain-specific policies, and its reward compares the final database state and user-facing responses with annotated outcomes. The paper also says dialogue wording may vary while reaching the same database outcome (PDF pp. 1–4).
- Observation 2: **supported** — The paper defines pass^k over repeated trials and reports that the best-performing gpt-4o function-calling agent has pass^8 below 25% in τ-retail (PDF pp. 4–5, 7).
- Observation 3: **supported** — The authors explicitly state that reward r = 1 may be necessary but not sufficient for success, giving failure to obtain explicit user confirmation as an example of a policy violation the reward may not capture (PDF p. 4).
- Observation 4: **supported** — The evaluation covers τ-retail and τ-airline; the authors describe medical, tax, and legal domains as possible future work. Thus, transfer to those broader settings is not evaluated in this paper (PDF pp. 2, 5–6).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\n  \"score\": 0.74,\n  \"summary\": \"τ-bench contributes a benchmark for evaluating agents across simulated user conversations, API use, domain rules, and repeated-trial consistency. Its two customer-service domains, annotated database outcomes, and pass^k metric make agent reliability testable at scale. Reported experiments show substantial failure rates for the tested agents, though the benchmark’s simulated users, narrow domain coverage, and outcome-based reward constrain how broadly those results transfer.\",\n  \"observations\": [\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The benchmark combines conversational interaction, tool use, and domain-policy adherence, while its database-state evaluation enables automated scoring across varied dialogue trajectories.\",\n      \"page\": 4,\n      \"quote\": \"This allows for objective measurement of the agent’s decision making\"\n    },\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The evaluation includes repeated trials to measure consistency, and the experiments show that success can decline notably across trials for the strongest tested agent.\",\n      \"page\": 7,\n      \"quote\": \"pass^8 drops to < 25%\"\n    },\n    {\n      \"kind\": \"limitation\",\n      \"claim\": \"The authors acknowledge that matching the expected database state does not fully establish policy compliance, so the automated reward can miss some rule violations.\",\n      \"page\": 4,\n      \"quote\": \"r = 1 might be a necessary but not sufficient condition for a successful episode\"\n    },\n    {\n      \"kind\": \"limitation\",\n      \"claim\": \"The reported evaluation is limited to two customer-service domains, and the authors describe broader, more complex domains as future work; transfer to those settings remains untested here.\",\n      \"page\": 5,\n      \"quote\": \"more advanced domains (e.g., medical, tax, or legal) with more complex data and rules can be studied\"\n    }\n  ],\n  \"unresolved_questions\": [\n    \"How closely do the LM-simulated users and synthetic tasks predict agent performance in interactions with real users?\",\n    \"How would the benchmark’s rankings or pass^k results change under additional domains, user simulators, or real-user evaluation?\",\n    \"Can systematic checks reliably detect policy violations that leave the expected database state unchanged?\"\n  ]\n}",
  "observation": {}
}
```

</details>
