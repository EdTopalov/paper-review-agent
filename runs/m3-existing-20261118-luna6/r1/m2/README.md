# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 19/20 | 19/20 | 5.45 | 5.45 | 4.05 | 5.45 | 29577.3 | 806.0 | $0.002176 | 11.70 |
| baseline | 20/20 | 12/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 577.5 | $0.003386 | 8.02 |
| pyagent_react | 18/20 | 18/20 | 5.45 | 4.85 | 3.35 | 5.45 | 38050.4 | 1199.4 | $0.002218 | 18.86 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 19/20 | 19/20 | 5.45 | 29577.3/806.0 | $0.002176 | 11.70 |
| baseline | 1 | 20/20 | 12/20 | 1.00 | 24778.5/577.5 | $0.003386 | 8.02 |
| pyagent_react | 1 | 18/20 | 18/20 | 5.45 | 38050.4/1199.4 | $0.002218 | 18.86 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 19 / 0 / 1 | k=1: 0.950 | unavailable | 0 |
| baseline | 12 / 0 / 8 | k=1: 0.600 | unavailable | 0 |
| pyagent_react | 18 / 0 / 2 | k=1: 0.900 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|
| agent − baseline | 0.3500 [0.1500, 0.5500]; n=20 | 0.0237 [0.0074, 0.0426]; n=19 | 0.0289 | -0.0012 [-0.0017, -0.0007]; n=20 | 3.6828 [2.1290, 5.3498]; n=20 |
| agent − pyagent_react | 0.0500 [0.0000, 0.1500]; n=20 | 0.0106 [-0.0089, 0.0306]; n=18 | 0.0361 | -0.0000 [-0.0004, 0.0004]; n=20 | -7.1638 [-9.6132, -4.7532]; n=20 |
| baseline − pyagent_react | -0.3000 [-0.5000, -0.1000]; n=20 | -0.0111 [-0.0300, 0.0050]; n=18 | 0.0278 | 0.0012 [0.0007, 0.0017]; n=20 | -10.8466 [-13.2794, -8.3460]; n=20 |

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T01 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T02 | 1/1 | 1/1 | 0.6500 | unavailable | [0.65, 0.65] |
| agent | T03 | 1/1 | 1/1 | 0.6300 | unavailable | [0.63, 0.63] |
| agent | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T05 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T06 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T07 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T08 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| agent | T09 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T10 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| agent | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T12 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T13 | 1/1 | 1/1 | 0.7900 | unavailable | [0.79, 0.79] |
| agent | T14 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T15 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T16 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| agent | T17 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| agent | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| agent | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T20 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T02 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T03 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| baseline | T04 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T05 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| baseline | T06 | 1/1 | 0/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T07 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T08 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T09 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T10 | 1/1 | 0/1 | 0.7500 | unavailable | [0.75, 0.75] |
| baseline | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T12 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T13 | 1/1 | 0/1 | 0.7700 | unavailable | [0.77, 0.77] |
| baseline | T14 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T15 | 1/1 | 0/1 | 0.5800 | unavailable | [0.58, 0.58] |
| baseline | T16 | 1/1 | 0/1 | 0.5800 | unavailable | [0.58, 0.58] |
| baseline | T17 | 1/1 | 0/1 | 0.6900 | unavailable | [0.69, 0.69] |
| baseline | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T19 | 1/1 | 0/1 | 0.6900 | unavailable | [0.69, 0.69] |
| baseline | T20 | 1/1 | 1/1 | 0.6700 | unavailable | [0.67, 0.67] |
| pyagent_react | T01 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T02 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T03 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T04 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T05 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T06 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| pyagent_react | T07 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T08 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T09 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| pyagent_react | T10 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| pyagent_react | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T12 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T13 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T14 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T15 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T16 | 1/1 | 1/1 | 0.5700 | unavailable | [0.57, 0.57] |
| pyagent_react | T17 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| pyagent_react | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T19 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | ok | 0.79 | 0 | yes | not audited | 5 | 29323/623 | $0.001875 | 10.12 |
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | ok | 0.78 | 1 | no | not audited | 7 | 38947/1046 | $0.002767 | 15.34 |
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 34264/687 | $0.002864 | 10.42 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.77 | 0 | yes | not audited | 4 | 19917/583 | $0.001706 | 7.95 |
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.76 | 0 | yes | not audited | 4 | 20022/619 | $0.001729 | 9.82 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.76 | 0 | yes | not audited | 5 | 24355/613 | $0.001608 | 10.74 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | ok | 0.76 | 0 | yes | not audited | 6 | 34594/606 | $0.002911 | 9.75 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.75 | 1 | no | not audited | 5 | 30690/1003 | $0.002045 | 13.22 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.74 | 0 | yes | not audited | 4 | 26427/581 | $0.001906 | 8.31 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 22856/590 | $0.001684 | 9.76 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 30425/725 | $0.002629 | 12.27 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 4 | 21172/692 | $0.001809 | 11.42 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | ok | 0.72 | 1 | no | not audited | 6 | 28944/1276 | $0.001943 | 14.80 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 30334/596 | $0.002676 | 10.11 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 23146/625 | $0.002149 | 10.28 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 29129/662 | $0.001866 | 10.06 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.68 | 2 | no | not audited | 8 | 48082/1617 | $0.003453 | 18.86 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | ok | 0.65 | 0 | yes | not audited | 4 | 23127/623 | $0.001726 | 11.57 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.63 | 0 | yes | not audited | 5 | 21056/578 | $0.001384 | 9.26 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | error | — | 4 | no | not audited | 8 | 54736/1774 | $0.002783 | 19.94 |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 30789/495 | $0.004096 | 9.55 |
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 38684/580 | $0.005125 | 8.18 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.77 | 0 | no | not audited | 1 | 27075/479 | $0.003624 | 5.78 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.76 | 0 | yes | not audited | 1 | 16657/512 | $0.002338 | 8.96 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.75 | 0 | no | not audited | 1 | 23863/564 | $0.003265 | 7.01 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.74 | 0 | yes | not audited | 1 | 36934/503 | $0.004868 | 5.79 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.74 | 0 | yes | not audited | 1 | 24226/533 | $0.003295 | 9.49 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 35056/498 | $0.004631 | 6.47 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 16572/648 | $0.002395 | 11.24 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 30099/541 | $0.004033 | 6.78 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 26994/494 | $0.003621 | 6.31 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 18064/597 | $0.002556 | 7.19 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 33041/462 | $0.004361 | 8.63 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 36072/595 | $0.004806 | 7.97 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 17424/694 | $0.002525 | 9.11 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.67 | 0 | yes | not audited | 1 | 13497/777 | $0.002076 | 9.89 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.66 | 0 | yes | not audited | 1 | 23878/695 | $0.003332 | 8.65 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.62 | 0 | yes | not audited | 1 | 14416/769 | $0.002186 | 9.67 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.58 | 0 | no | not audited | 1 | 8838/539 | $0.001374 | 6.16 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.58 | 0 | no | not audited | 1 | 23392/575 | $0.003211 | 7.49 |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.78 | 0 | yes | not audited | 5 | 25702/831 | $0.001620 | 14.79 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.78 | 1 | no | not audited | 6 | 49469/1725 | $0.002647 | 25.28 |
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.75 | 2 | no | not audited | 6 | 62690/2368 | $0.003456 | 30.06 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | ok | 0.75 | 0 | yes | not audited | 5 | 40025/753 | $0.002107 | 13.79 |
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.75 | 2 | no | not audited | 6 | 47721/1864 | $0.002529 | 23.73 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.75 | 0 | yes | not audited | 5 | 29189/784 | $0.001945 | 17.21 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | ok | 0.74 | 0 | yes | not audited | 8 | 55598/938 | $0.002548 | 18.87 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.73 | 0 | yes | not audited | 4 | 26387/758 | $0.001737 | 13.65 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 34135/832 | $0.001831 | 14.07 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 4 | 23217/765 | $0.002004 | 12.98 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 30282/1012 | $0.001614 | 17.31 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 30982/790 | $0.001750 | 13.01 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | ok | 0.68 | 1 | no | not audited | 5 | 37314/1429 | $0.002347 | 20.35 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.68 | 0 | yes | not audited | 3 | 12416/1375 | $0.001488 | 18.67 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 37423/887 | $0.001871 | 15.73 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.68 | 1 | no | not audited | 7 | 50655/1872 | $0.003988 | 27.13 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.68 | 0 | yes | not audited | 4 | 21786/1097 | $0.001686 | 17.62 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.57 | 0 | yes | not audited | 4 | 23728/619 | $0.001520 | 13.32 |
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | error | — | 2 | no | not audited | 8 | 52027/1367 | $0.002505 | 23.45 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | error | — | 3 | no | not audited | 8 | 70263/1922 | $0.003177 | 26.24 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
