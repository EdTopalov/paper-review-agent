# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 20/20 | 20/20 | 5.70 | 5.70 | 4.00 | 5.70 | 33055.0 | 934.3 | $0.002120 | 13.54 |
| baseline | 20/20 | 10/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 612.5 | $0.000554 | 7.82 |
| pyagent_react | 20/20 | 20/20 | 5.35 | 4.95 | 3.50 | 5.35 | 37188.9 | 1217.8 | $0.002278 | 19.30 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 20/20 | 20/20 | 5.70 | 33055.0/934.3 | $0.002120 | 13.54 |
| baseline | 1 | 20/20 | 10/20 | 1.00 | 24778.5/612.5 | $0.000554 | 7.82 |
| pyagent_react | 1 | 20/20 | 20/20 | 5.35 | 37188.9/1217.8 | $0.002278 | 19.30 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 20 / 0 / 0 | k=1: 1.000 | unavailable | 0 |
| baseline | 10 / 0 / 10 | k=1: 0.500 | unavailable | 0 |
| pyagent_react | 20 / 0 / 0 | k=1: 1.000 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|
| agent − baseline | 0.5000 [0.3000, 0.7000]; n=20 | 0.0255 [0.0125, 0.0385]; n=20 | 0.0305 | 0.0016 [0.0012, 0.0019]; n=20 | 5.7201 [3.9468, 7.5480]; n=20 |
| agent − pyagent_react | 0.0000 [0.0000, 0.0000]; n=20 | 0.0135 [0.0030, 0.0230]; n=20 | 0.0225 | -0.0002 [-0.0006, 0.0003]; n=20 | -5.7628 [-8.5574, -3.4187]; n=20 |
| baseline − pyagent_react | -0.5000 [-0.7000, -0.3000]; n=20 | -0.0120 [-0.0230, -0.0025]; n=20 | 0.0200 | -0.0017 [-0.0021, -0.0014]; n=20 | -11.4829 [-14.3376, -8.8663]; n=20 |

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T01 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T02 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| agent | T03 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| agent | T04 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T05 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T06 | 1/1 | 1/1 | 0.7900 | unavailable | [0.79, 0.79] |
| agent | T07 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T08 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T09 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T10 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| agent | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T12 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T14 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| agent | T15 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T16 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| agent | T17 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T18 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T19 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| agent | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T01 | 1/1 | 0/1 | 0.7500 | unavailable | [0.75, 0.75] |
| baseline | T02 | 1/1 | 0/1 | 0.6500 | unavailable | [0.65, 0.65] |
| baseline | T03 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| baseline | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T05 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| baseline | T06 | 1/1 | 0/1 | 0.7500 | unavailable | [0.75, 0.75] |
| baseline | T07 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T08 | 1/1 | 0/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T09 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| baseline | T10 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| baseline | T11 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T12 | 1/1 | 0/1 | 0.7000 | unavailable | [0.7, 0.7] |
| baseline | T13 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T14 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| baseline | T15 | 1/1 | 0/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T16 | 1/1 | 0/1 | 0.5800 | unavailable | [0.58, 0.58] |
| baseline | T17 | 1/1 | 0/1 | 0.6900 | unavailable | [0.69, 0.69] |
| baseline | T18 | 1/1 | 0/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T20 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T01 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| pyagent_react | T02 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| pyagent_react | T03 | 1/1 | 1/1 | 0.6500 | unavailable | [0.65, 0.65] |
| pyagent_react | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T05 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T06 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T07 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T08 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T09 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| pyagent_react | T10 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T11 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| pyagent_react | T12 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T13 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T14 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| pyagent_react | T15 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T16 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| pyagent_react | T17 | 1/1 | 1/1 | 0.7100 | unavailable | [0.71, 0.71] |
| pyagent_react | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T20 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | ok | 0.79 | 1 | no | not audited | 5 | 22318/1005 | $0.001457 | 12.63 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.78 | 0 | yes | not audited | 5 | 20302/602 | $0.001264 | 9.21 |
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.78 | 1 | no | not audited | 7 | 45052/958 | $0.003093 | 14.73 |
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | ok | 0.78 | 2 | no | not audited | 7 | 53961/1717 | $0.002746 | 19.40 |
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.76 | 0 | yes | not audited | 4 | 27198/608 | $0.001583 | 9.13 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | ok | 0.76 | 0 | yes | not audited | 6 | 22470/615 | $0.001980 | 13.55 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.75 | 0 | yes | not audited | 4 | 18845/547 | $0.001380 | 11.17 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.75 | 1 | no | not audited | 7 | 43220/1174 | $0.003133 | 17.89 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.74 | 0 | yes | not audited | 4 | 19078/630 | $0.001330 | 9.45 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | ok | 0.74 | 2 | no | not audited | 8 | 57429/1667 | $0.003709 | 20.95 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 35576/626 | $0.002756 | 11.77 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 46219/661 | $0.003575 | 11.00 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | ok | 0.72 | 3 | no | not audited | 8 | 46885/2007 | $0.002449 | 22.61 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | ok | 0.72 | 2 | no | not audited | 6 | 41267/1260 | $0.002125 | 14.13 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 29150/613 | $0.001671 | 9.95 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 42552/1161 | $0.002437 | 14.05 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | ok | 0.69 | 0 | yes | not audited | 6 | 23267/726 | $0.001751 | 12.88 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 21657/585 | $0.001327 | 13.18 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.66 | 0 | yes | not audited | 4 | 14551/545 | $0.001040 | 8.62 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.66 | 1 | no | not audited | 6 | 30103/979 | $0.001602 | 14.43 |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 38684/659 | $0.000717 | 8.67 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 27075/752 | $0.000647 | 8.35 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.77 | 0 | yes | not audited | 1 | 16657/529 | $0.000431 | 6.36 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.76 | 0 | yes | not audited | 1 | 23863/641 | $0.000559 | 7.68 |
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.75 | 0 | no | not audited | 1 | 30789/586 | $0.000601 | 8.38 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.75 | 0 | no | not audited | 1 | 35056/543 | $0.000622 | 6.78 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.75 | 0 | yes | not audited | 1 | 24226/643 | $0.000564 | 7.15 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 36072/505 | $0.000613 | 8.35 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 36934/579 | $0.000659 | 6.98 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 33041/550 | $0.000606 | 6.48 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.7 | 0 | no | not audited | 1 | 26994/485 | $0.000513 | 6.89 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.69 | 0 | yes | not audited | 1 | 16572/731 | $0.000531 | 9.27 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 18064/675 | $0.000518 | 7.97 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 30099/552 | $0.000577 | 6.59 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 17424/712 | $0.000531 | 8.60 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 13497/676 | $0.000473 | 8.91 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.66 | 0 | yes | not audited | 1 | 23878/668 | $0.000573 | 8.10 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.65 | 0 | no | not audited | 1 | 14416/683 | $0.000486 | 12.09 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.62 | 0 | no | not audited | 1 | 8838/537 | $0.000357 | 6.64 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.58 | 0 | no | not audited | 1 | 23392/545 | $0.000507 | 6.10 |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.78 | 0 | yes | not audited | 5 | 36310/751 | $0.001892 | 13.15 |
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.76 | 0 | yes | not audited | 3 | 22577/1368 | $0.002033 | 22.65 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.76 | 0 | yes | not audited | 6 | 41935/737 | $0.001925 | 14.47 |
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | ok | 0.75 | 1 | no | not audited | 3 | 14754/2878 | $0.002111 | 33.18 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | ok | 0.75 | 0 | yes | not audited | 7 | 45790/924 | $0.003083 | 18.18 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.75 | 0 | yes | not audited | 6 | 39467/825 | $0.001922 | 16.64 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | ok | 0.75 | 0 | yes | not audited | 5 | 45176/808 | $0.002197 | 13.28 |
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.75 | 2 | no | not audited | 8 | 57661/1894 | $0.002582 | 24.12 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.74 | 0 | yes | not audited | 5 | 31856/1038 | $0.001848 | 18.65 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.73 | 0 | yes | not audited | 4 | 36948/1607 | $0.002846 | 22.63 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 58724/1086 | $0.004581 | 18.88 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 37670/1275 | $0.002116 | 19.72 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 37743/860 | $0.002878 | 19.81 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | ok | 0.71 | 0 | yes | not audited | 4 | 17030/1190 | $0.001426 | 18.33 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | ok | 0.68 | 1 | no | not audited | 6 | 37988/1541 | $0.002117 | 22.92 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 4 | 27134/801 | $0.001819 | 14.04 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 30820/829 | $0.001804 | 14.35 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.67 | 0 | yes | not audited | 5 | 24357/711 | $0.001389 | 14.23 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.65 | 0 | yes | not audited | 5 | 30737/810 | $0.001640 | 14.88 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.62 | 2 | no | not audited | 8 | 69101/2424 | $0.003346 | 31.88 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
