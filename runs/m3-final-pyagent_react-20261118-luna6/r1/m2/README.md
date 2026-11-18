# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pyagent_react | 20/20 | 20/20 | 5.60 | 5.25 | 3.65 | 5.60 | 40279.7 | 1165.0 | $0.002293 | 18.65 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| pyagent_react | 1 | 20/20 | 20/20 | 5.60 | 40279.7/1165.0 | $0.002293 | 18.65 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| pyagent_react | 20 / 0 / 0 | k=1: 1.000 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| pyagent_react | T01 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| pyagent_react | T02 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T03 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T05 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T06 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T07 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T08 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| pyagent_react | T09 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| pyagent_react | T10 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T11 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| pyagent_react | T12 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| pyagent_react | T13 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T14 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| pyagent_react | T15 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T16 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| pyagent_react | T17 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T18 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| pyagent_react | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T20 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | ok | 0.78 | 1 | no | not audited | 6 | 41905/1176 | $0.001988 | 16.87 |
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.76 | 1 | no | not audited | 6 | 63234/1501 | $0.003379 | 18.61 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.76 | 0 | yes | not audited | 5 | 30201/763 | $0.001820 | 17.03 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | ok | 0.75 | 0 | yes | not audited | 5 | 37776/741 | $0.002100 | 11.76 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | ok | 0.75 | 1 | no | not audited | 6 | 48552/1166 | $0.002551 | 15.23 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.74 | 0 | yes | not audited | 4 | 31939/813 | $0.002171 | 11.95 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.74 | 0 | yes | not audited | 5 | 32516/957 | $0.001949 | 15.90 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.73 | 1 | no | not audited | 6 | 49741/1192 | $0.002301 | 19.98 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 57559/973 | $0.004461 | 20.95 |
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 34681/1032 | $0.001834 | 17.62 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 42654/1444 | $0.002440 | 16.82 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 28665/1261 | $0.001916 | 17.62 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.69 | 0 | yes | not audited | 6 | 42814/846 | $0.002187 | 14.70 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 34176/838 | $0.001751 | 17.80 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 35705/1155 | $0.002766 | 21.95 |
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.68 | 1 | no | not audited | 3 | 13095/1981 | $0.001542 | 27.36 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | ok | 0.68 | 2 | no | not audited | 7 | 49353/1914 | $0.002499 | 28.54 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.66 | 0 | yes | not audited | 6 | 37523/850 | $0.001874 | 19.76 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.66 | 1 | no | not audited | 7 | 41082/1373 | $0.001842 | 24.47 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.62 | 1 | no | not audited | 7 | 52423/1324 | $0.002499 | 18.19 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
