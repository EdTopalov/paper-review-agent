# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 18/20 | 18/20 | 5.75 | 5.75 | 4.10 | 5.75 | 34097.1 | 940.7 | $0.002174 | 14.40 |
| baseline | 20/20 | 9/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 631.9 | $0.000564 | 8.16 |
| pyagent_react | 19/20 | 19/20 | 5.35 | 4.90 | 3.55 | 5.35 | 36401.2 | 1202.0 | $0.002279 | 17.87 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 18/20 | 18/20 | 5.75 | 34097.1/940.7 | $0.002174 | 14.40 |
| baseline | 1 | 20/20 | 9/20 | 1.00 | 24778.5/631.9 | $0.000564 | 8.16 |
| pyagent_react | 1 | 19/20 | 19/20 | 5.35 | 36401.2/1202.0 | $0.002279 | 17.87 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 18 / 0 / 2 | k=1: 0.900 | unavailable | 0 |
| baseline | 9 / 0 / 11 | k=1: 0.450 | unavailable | 0 |
| pyagent_react | 19 / 0 / 1 | k=1: 0.950 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|
| agent − baseline | 0.4500 [0.2000, 0.7000]; n=20 | 0.0339 [0.0200, 0.0478]; n=18 | 0.0383 | 0.0016 [0.0012, 0.0020]; n=20 | 6.2392 [4.3769, 8.4705]; n=20 |
| agent − pyagent_react | -0.0500 [-0.2000, 0.1000]; n=20 | 0.0371 [0.0147, 0.0606]; n=17 | 0.0453 | -0.0001 [-0.0007, 0.0004]; n=20 | -3.4707 [-8.2516, 0.1760]; n=20 |
| baseline − pyagent_react | -0.5000 [-0.7000, -0.3000]; n=20 | -0.0011 [-0.0205, 0.0221]; n=19 | 0.0337 | -0.0017 [-0.0021, -0.0014]; n=20 | -9.7099 [-13.7325, -7.0413]; n=20 |

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T01 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| agent | T02 | 1/1 | 1/1 | 0.6300 | unavailable | [0.63, 0.63] |
| agent | T03 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| agent | T04 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| agent | T05 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T06 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T07 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| agent | T08 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T09 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T10 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T11 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T12 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T13 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| agent | T14 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T15 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T16 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| agent | T17 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| agent | T18 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| agent | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T02 | 1/1 | 0/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T03 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T05 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T06 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| baseline | T07 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T08 | 1/1 | 0/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T09 | 1/1 | 0/1 | 0.7100 | unavailable | [0.71, 0.71] |
| baseline | T10 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T11 | 1/1 | 0/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T12 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T13 | 1/1 | 0/1 | 0.7600 | unavailable | [0.76, 0.76] |
| baseline | T14 | 1/1 | 0/1 | 0.7300 | unavailable | [0.73, 0.73] |
| baseline | T15 | 1/1 | 0/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T16 | 1/1 | 1/1 | 0.5800 | unavailable | [0.58, 0.58] |
| baseline | T17 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T19 | 1/1 | 0/1 | 0.6600 | unavailable | [0.66, 0.66] |
| baseline | T20 | 1/1 | 0/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T02 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T03 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T05 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T06 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| pyagent_react | T07 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| pyagent_react | T08 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T09 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T10 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T11 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T12 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T14 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T15 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| pyagent_react | T16 | 1/1 | 1/1 | 0.5700 | unavailable | [0.57, 0.57] |
| pyagent_react | T17 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| pyagent_react | T18 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| pyagent_react | T19 | 1/1 | 1/1 | 0.7000 | unavailable | [0.7, 0.7] |
| pyagent_react | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | ok | 0.78 | 0 | yes | not audited | 4 | 23536/569 | $0.001463 | 8.60 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.78 | 1 | no | not audited | 6 | 40586/1221 | $0.002195 | 18.61 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 33765/684 | $0.002992 | 10.58 |
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.77 | 0 | yes | not audited | 5 | 33094/547 | $0.001843 | 12.55 |
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.77 | 0 | yes | not audited | 5 | 23376/665 | $0.001448 | 11.32 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.76 | 0 | yes | not audited | 6 | 23175/604 | $0.001863 | 13.38 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.76 | 0 | yes | not audited | 4 | 20305/540 | $0.001438 | 10.66 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | ok | 0.76 | 0 | yes | not audited | 5 | 27078/649 | $0.001548 | 9.28 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.74 | 1 | no | not audited | 7 | 54379/1245 | $0.004090 | 15.96 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.74 | 1 | no | not audited | 7 | 55613/1220 | $0.003832 | 16.54 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | ok | 0.73 | 0 | yes | not audited | 6 | 24088/603 | $0.001966 | 11.18 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | ok | 0.72 | 3 | no | not audited | 7 | 58482/2071 | $0.002899 | 24.60 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 19324/596 | $0.001142 | 10.05 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.72 | 1 | no | not audited | 6 | 36206/1121 | $0.001968 | 16.95 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.69 | 0 | yes | not audited | 4 | 19053/682 | $0.001346 | 11.73 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.67 | 0 | yes | not audited | 5 | 21363/605 | $0.001291 | 13.61 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.66 | 0 | yes | not audited | 6 | 30127/633 | $0.002385 | 15.50 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | ok | 0.63 | 0 | yes | not audited | 5 | 23505/601 | $0.001383 | 9.89 |
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | error | — | 3 | no | not audited | 8 | 51389/1634 | $0.003363 | 20.28 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | error | — | 5 | no | not audited | 8 | 63498/2324 | $0.003032 | 26.75 |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 30789/727 | $0.000672 | 8.47 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 16657/656 | $0.000495 | 7.30 |
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 38684/675 | $0.000725 | 8.83 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.76 | 0 | no | not audited | 1 | 27075/845 | $0.000694 | 10.56 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.75 | 0 | yes | not audited | 1 | 35056/516 | $0.000609 | 6.28 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.74 | 0 | yes | not audited | 1 | 26994/529 | $0.000535 | 7.21 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.73 | 0 | no | not audited | 1 | 24226/613 | $0.000549 | 8.66 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 36072/615 | $0.000668 | 8.50 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 36934/683 | $0.000711 | 8.29 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 23863/685 | $0.000581 | 9.33 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.71 | 0 | no | not audited | 1 | 16572/655 | $0.000493 | 9.61 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 30099/587 | $0.000595 | 7.56 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 18064/735 | $0.000548 | 7.84 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 17424/671 | $0.000510 | 8.99 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 13497/835 | $0.000553 | 10.70 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.66 | 0 | no | not audited | 1 | 33041/422 | $0.000542 | 5.23 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.62 | 0 | no | not audited | 1 | 14416/656 | $0.000472 | 8.22 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.62 | 0 | yes | not audited | 1 | 23878/504 | $0.000491 | 8.04 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.62 | 0 | no | not audited | 1 | 8838/518 | $0.000348 | 6.41 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.58 | 0 | yes | not audited | 1 | 23392/511 | $0.000490 | 7.25 |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 77763/903 | $0.005285 | 14.85 |
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 34890/967 | $0.002923 | 15.42 |
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.75 | 0 | yes | not audited | 6 | 34493/843 | $0.001739 | 15.75 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.75 | 0 | yes | not audited | 4 | 22256/1786 | $0.002072 | 23.98 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.75 | 0 | yes | not audited | 4 | 27822/741 | $0.001775 | 12.09 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 27175/1140 | $0.002167 | 18.44 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.72 | 1 | no | not audited | 6 | 46777/1427 | $0.002553 | 18.41 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.7 | 0 | yes | not audited | 6 | 43324/716 | $0.002274 | 14.37 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | ok | 0.69 | 1 | no | not audited | 6 | 38826/1328 | $0.002021 | 17.91 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 34139/879 | $0.001770 | 13.73 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 32879/995 | $0.001759 | 17.62 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.68 | 1 | no | not audited | 6 | 39770/1203 | $0.002086 | 16.76 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | ok | 0.68 | 0 | yes | not audited | 3 | 17905/1448 | $0.001834 | 18.88 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.68 | 0 | yes | not audited | 4 | 33491/716 | $0.001841 | 12.73 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 28215/764 | $0.001674 | 13.27 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | ok | 0.67 | 1 | no | not audited | 6 | 46024/1295 | $0.002119 | 18.14 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.67 | 0 | yes | not audited | 6 | 36894/835 | $0.001941 | 15.56 |
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | ok | 0.62 | 1 | no | not audited | 3 | 12004/4512 | $0.002753 | 48.39 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.57 | 0 | yes | not audited | 5 | 32892/652 | $0.001690 | 11.19 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | error | — | 0 | unavailable | not audited | 8 | 60485/891 | $0.003293 | 19.95 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
