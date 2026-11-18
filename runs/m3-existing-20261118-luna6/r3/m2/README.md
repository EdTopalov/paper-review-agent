# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 19/20 | 19/20 | 5.25 | 5.25 | 3.75 | 5.25 | 30657.1 | 830.8 | $0.001862 | 11.58 |
| baseline | 20/20 | 13/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 593.9 | $0.000545 | 7.31 |
| pyagent_react | 20/20 | 20/20 | 5.55 | 4.85 | 3.25 | 5.55 | 38792.3 | 1326.1 | $0.002182 | 18.82 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 19/20 | 19/20 | 5.25 | 30657.1/830.8 | $0.001862 | 11.58 |
| baseline | 1 | 20/20 | 13/20 | 1.00 | 24778.5/593.9 | $0.000545 | 7.31 |
| pyagent_react | 1 | 20/20 | 20/20 | 5.55 | 38792.3/1326.1 | $0.002182 | 18.82 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 19 / 0 / 1 | k=1: 0.950 | unavailable | 0 |
| baseline | 13 / 0 / 7 | k=1: 0.650 | unavailable | 0 |
| pyagent_react | 20 / 0 / 0 | k=1: 1.000 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|
| agent − baseline | 0.3000 [0.1000, 0.5000]; n=20 | 0.0242 [0.0116, 0.0379]; n=19 | 0.0274 | 0.0013 [0.0010, 0.0016]; n=20 | 4.2685 [2.6288, 5.9907]; n=20 |
| agent − pyagent_react | -0.0500 [-0.1500, 0.0000]; n=20 | 0.0179 [0.0047, 0.0316]; n=19 | 0.0295 | -0.0003 [-0.0008, 0.0001]; n=20 | -7.2370 [-9.7953, -4.7254]; n=20 |
| baseline − pyagent_react | -0.3500 [-0.5500, -0.1500]; n=20 | -0.0080 [-0.0215, 0.0045]; n=20 | 0.0220 | -0.0016 [-0.0020, -0.0013]; n=20 | -11.5056 [-14.3114, -9.0506]; n=20 |

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T01 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| agent | T02 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T03 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| agent | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T05 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| agent | T06 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T07 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T08 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T09 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T10 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T12 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T14 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T15 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T16 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| agent | T17 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| agent | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| agent | T19 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| agent | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T01 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T02 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T03 | 1/1 | 1/1 | 0.6300 | unavailable | [0.63, 0.63] |
| baseline | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T05 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| baseline | T06 | 1/1 | 0/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T07 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T08 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T09 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T10 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| baseline | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T12 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T14 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T15 | 1/1 | 0/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T16 | 1/1 | 0/1 | 0.5800 | unavailable | [0.58, 0.58] |
| baseline | T17 | 1/1 | 0/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T18 | 1/1 | 0/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T19 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T20 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T02 | 1/1 | 1/1 | 0.7000 | unavailable | [0.7, 0.7] |
| pyagent_react | T03 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T04 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| pyagent_react | T05 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T06 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T07 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T08 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T09 | 1/1 | 1/1 | 0.7000 | unavailable | [0.7, 0.7] |
| pyagent_react | T10 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| pyagent_react | T11 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T12 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T13 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| pyagent_react | T14 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| pyagent_react | T15 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| pyagent_react | T16 | 1/1 | 1/1 | 0.5700 | unavailable | [0.57, 0.57] |
| pyagent_react | T17 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T18 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| pyagent_react | T19 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| pyagent_react | T20 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | ok | 0.78 | 1 | no | not audited | 5 | 24355/1017 | $0.001599 | 13.34 |
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | ok | 0.78 | 2 | no | not audited | 6 | 53008/1538 | $0.002677 | 16.25 |
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.77 | 0 | yes | not audited | 4 | 22409/600 | $0.001578 | 8.27 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.77 | 1 | no | not audited | 6 | 24335/949 | $0.001333 | 11.73 |
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.76 | 0 | yes | not audited | 5 | 32310/578 | $0.001603 | 9.48 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.76 | 0 | yes | not audited | 4 | 19791/580 | $0.001515 | 9.25 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.76 | 0 | yes | not audited | 5 | 26488/653 | $0.001566 | 10.27 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.74 | 3 | no | not audited | 8 | 68980/1917 | $0.003087 | 20.97 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.74 | 0 | yes | not audited | 5 | 27455/651 | $0.001661 | 9.48 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | ok | 0.74 | 0 | yes | not audited | 5 | 23780/640 | $0.001280 | 9.63 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | ok | 0.72 | 0 | yes | not audited | 6 | 41841/718 | $0.002914 | 11.58 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 22848/596 | $0.001534 | 10.04 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 29119/667 | $0.001962 | 10.65 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 28570/917 | $0.001602 | 13.23 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.72 | 0 | yes | not audited | 4 | 19004/642 | $0.001291 | 10.02 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.69 | 0 | yes | not audited | 6 | 29380/590 | $0.002251 | 10.54 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | ok | 0.69 | 0 | yes | not audited | 4 | 15717/568 | $0.001143 | 9.01 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 4 | 18679/594 | $0.001252 | 8.13 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.62 | 0 | yes | not audited | 5 | 28982/598 | $0.001639 | 9.64 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | error | — | 3 | no | not audited | 8 | 56091/1603 | $0.003746 | 20.11 |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 30789/541 | $0.000579 | 7.60 |
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 38684/719 | $0.000747 | 8.94 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 27075/480 | $0.000511 | 5.66 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.76 | 0 | yes | not audited | 1 | 16657/599 | $0.000466 | 6.73 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.75 | 0 | yes | not audited | 1 | 23863/577 | $0.000527 | 6.84 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.74 | 0 | no | not audited | 1 | 35056/473 | $0.000587 | 5.73 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 36072/529 | $0.000625 | 7.05 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 36934/512 | $0.000626 | 6.73 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 30099/500 | $0.000551 | 6.00 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 26994/520 | $0.000530 | 5.66 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 24226/494 | $0.000490 | 6.55 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 16572/684 | $0.000508 | 8.05 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 8838/852 | $0.000515 | 10.13 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 18064/723 | $0.000542 | 7.69 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 17424/690 | $0.000520 | 8.72 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 33041/510 | $0.000586 | 7.47 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 13497/750 | $0.000510 | 10.16 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.63 | 0 | yes | not audited | 1 | 23878/524 | $0.000501 | 6.45 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.62 | 0 | yes | not audited | 1 | 14416/756 | $0.000522 | 8.38 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.58 | 0 | no | not audited | 1 | 23392/444 | $0.000456 | 5.72 |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 62290/891 | $0.003101 | 15.22 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | ok | 0.78 | 0 | yes | not audited | 5 | 31660/797 | $0.001814 | 14.00 |
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.78 | 0 | yes | not audited | 5 | 30390/701 | $0.001721 | 12.27 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | ok | 0.77 | 0 | yes | not audited | 7 | 52052/1030 | $0.003811 | 16.24 |
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.75 | 2 | no | not audited | 8 | 60347/2387 | $0.002959 | 31.08 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | ok | 0.75 | 0 | yes | not audited | 5 | 31530/673 | $0.001866 | 11.78 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.74 | 1 | no | not audited | 7 | 50147/1833 | $0.002668 | 25.75 |
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | ok | 0.72 | 0 | yes | not audited | 3 | 10362/1817 | $0.001446 | 21.70 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.72 | 2 | no | not audited | 8 | 77654/1776 | $0.003328 | 23.29 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | ok | 0.72 | 2 | no | not audited | 7 | 60716/2813 | $0.003166 | 34.64 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 4 | 21338/841 | $0.001442 | 13.42 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.7 | 0 | yes | not audited | 6 | 36187/779 | $0.001742 | 14.43 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.7 | 1 | no | not audited | 6 | 36952/1599 | $0.002197 | 20.45 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 34197/823 | $0.001782 | 14.37 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.68 | 0 | yes | not audited | 2 | 5736/1524 | $0.001019 | 17.96 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.68 | 0 | yes | not audited | 4 | 27882/772 | $0.001424 | 12.37 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | ok | 0.68 | 2 | no | not audited | 7 | 52991/1532 | $0.002381 | 22.71 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.68 | 2 | no | not audited | 5 | 27790/2081 | $0.001897 | 23.22 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.66 | 0 | yes | not audited | 5 | 29899/1121 | $0.002034 | 18.97 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.57 | 0 | yes | not audited | 5 | 35727/732 | $0.001850 | 12.49 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
