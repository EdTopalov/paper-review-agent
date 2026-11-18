# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pyagent_react | 20/20 | 20/20 | 5.75 | 5.05 | 3.50 | 5.75 | 39219.2 | 1374.1 | $0.002364 | 20.35 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| pyagent_react | 1 | 20/20 | 20/20 | 5.75 | 39219.2/1374.1 | $0.002364 | 20.35 |

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
| pyagent_react | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T02 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T03 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| pyagent_react | T04 | 1/1 | 1/1 | 0.6500 | unavailable | [0.65, 0.65] |
| pyagent_react | T05 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T06 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T07 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T08 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| pyagent_react | T09 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T10 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T12 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| pyagent_react | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T14 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| pyagent_react | T15 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| pyagent_react | T16 | 1/1 | 1/1 | 0.6500 | unavailable | [0.65, 0.65] |
| pyagent_react | T17 | 1/1 | 1/1 | 0.6500 | unavailable | [0.65, 0.65] |
| pyagent_react | T18 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| pyagent_react | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T20 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 62373/805 | $0.003061 | 18.55 |
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | ok | 0.78 | 2 | no | not audited | 7 | 46382/2007 | $0.002467 | 26.56 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | ok | 0.78 | 1 | no | not audited | 7 | 58299/1348 | $0.002718 | 20.17 |
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.78 | 0 | yes | not audited | 5 | 31657/718 | $0.001887 | 12.22 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.77 | 0 | yes | not audited | 5 | 41516/2199 | $0.002800 | 30.82 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.73 | 0 | yes | not audited | 6 | 38215/793 | $0.001915 | 17.36 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.73 | 0 | yes | not audited | 6 | 48459/907 | $0.003426 | 15.06 |
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 39289/929 | $0.001896 | 19.04 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.72 | 1 | no | not audited | 6 | 41874/1352 | $0.002304 | 18.48 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 33006/1679 | $0.002099 | 21.31 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 40545/1030 | $0.002430 | 17.00 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 48481/872 | $0.003525 | 17.16 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.69 | 0 | yes | not audited | 7 | 40083/732 | $0.001853 | 14.05 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.68 | 1 | no | not audited | 7 | 48212/1456 | $0.003092 | 20.08 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.67 | 1 | no | not audited | 5 | 37814/1464 | $0.002207 | 19.46 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.66 | 0 | yes | not audited | 5 | 21903/679 | $0.001320 | 12.87 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | ok | 0.66 | 0 | yes | not audited | 6 | 32484/2391 | $0.002406 | 33.10 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | ok | 0.65 | 1 | no | not audited | 5 | 30254/2465 | $0.002318 | 27.71 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.65 | 0 | yes | not audited | 6 | 28869/762 | $0.001459 | 14.26 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | ok | 0.65 | 1 | no | not audited | 3 | 14670/2894 | $0.002091 | 31.64 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
