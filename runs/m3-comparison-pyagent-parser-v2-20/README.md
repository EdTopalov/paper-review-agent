# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 16/20 | 16/20 | 3.70 | 3.70 | 2.00 | 3.70 | 14551.2 | 775.9 | $0.001552 | 11.76 |
| baseline | 20/20 | 8/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 589.3 | $0.003392 | 7.19 |
| pyagent_react | 18/20 | 18/20 | 4.40 | 3.70 | 2.00 | 4.40 | 19870.1 | 1028.8 | $0.001914 | 14.61 |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 3 | 11836/530 | $0.001554 | 10.01 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.78 | 1 | no | not audited | 4 | 11377/897 | $0.001292 | 11.07 |
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.75 | 0 | yes | not audited | 3 | 7708/523 | $0.001039 | 8.00 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.74 | 0 | yes | not audited | 3 | 14962/508 | $0.001942 | 9.37 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.74 | 0 | yes | not audited | 3 | 10962/524 | $0.001453 | 8.28 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.74 | 0 | yes | not audited | 3 | 9087/532 | $0.001215 | 8.76 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.72 | 0 | yes | not audited | 3 | 8532/464 | $0.001115 | 15.28 |
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | ok | 0.72 | 1 | no | not audited | 4 | 12308/739 | $0.001255 | 16.06 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | ok | 0.68 | 2 | no | not audited | 5 | 16142/1190 | $0.001552 | 15.98 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.68 | 0 | yes | not audited | 3 | 11240/445 | $0.001439 | 6.81 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | ok | 0.68 | 0 | yes | not audited | 3 | 7459/575 | $0.001009 | 8.25 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 3 | 10626/590 | $0.001441 | 8.18 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | ok | 0.68 | 0 | yes | not audited | 3 | 9048/460 | $0.001192 | 7.45 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.68 | 1 | no | not audited | 4 | 15140/966 | $0.001610 | 11.86 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.67 | 1 | no | not audited | 4 | 12307/888 | $0.001384 | 12.17 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.62 | 0 | yes | not audited | 3 | 8139/472 | $0.001085 | 7.40 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | error | — | 3 | no | not audited | 5 | 17818/1364 | $0.001752 | 18.97 |
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | error | — | 3 | no | not audited | 5 | 33858/1375 | $0.002729 | 19.98 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | error | — | 3 | no | not audited | 5 | 33995/1112 | $0.002592 | 15.79 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | error | — | 3 | no | not audited | 5 | 28481/1364 | $0.002399 | 15.55 |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 30789/512 | $0.004105 | 7.71 |
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 38684/587 | $0.005129 | 8.36 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.76 | 0 | yes | not audited | 1 | 16657/668 | $0.002416 | 7.28 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.76 | 0 | no | not audited | 1 | 35056/532 | $0.004648 | 6.56 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.76 | 0 | no | not audited | 1 | 36934/492 | $0.004863 | 6.46 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.76 | 0 | no | not audited | 1 | 27075/429 | $0.003599 | 5.25 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.75 | 0 | no | not audited | 1 | 23863/575 | $0.003270 | 6.95 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.73 | 0 | yes | not audited | 1 | 24226/616 | $0.003336 | 6.70 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.73 | 0 | no | not audited | 1 | 18064/649 | $0.002582 | 6.91 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 36072/555 | $0.004786 | 5.87 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 16572/718 | $0.002430 | 10.58 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 30099/521 | $0.004023 | 6.02 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 26994/444 | $0.003596 | 5.03 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 8838/640 | $0.001425 | 7.44 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 14416/674 | $0.002139 | 6.59 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 13497/913 | $0.002144 | 9.73 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.67 | 0 | yes | not audited | 1 | 33041/465 | $0.004363 | 5.79 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.66 | 0 | yes | not audited | 1 | 17424/635 | $0.002495 | 7.66 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.63 | 0 | yes | not audited | 1 | 23878/619 | $0.003294 | 6.67 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.62 | 0 | no | not audited | 1 | 23392/542 | $0.003195 | 10.15 |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.78 | 0 | yes | not audited | 4 | 16211/806 | $0.001844 | 13.13 |
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | ok | 0.78 | 0 | yes | not audited | 4 | 16941/804 | $0.001890 | 12.05 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | ok | 0.78 | 2 | no | not audited | 5 | 34676/1728 | $0.002810 | 20.61 |
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.75 | 0 | yes | not audited | 4 | 19962/577 | $0.002304 | 11.69 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.75 | 1 | no | not audited | 5 | 18931/1452 | $0.001867 | 19.93 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.75 | 0 | yes | not audited | 3 | 13664/648 | $0.001658 | 9.34 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 28887/854 | $0.002132 | 12.57 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 28304/1434 | $0.002431 | 16.33 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 4 | 16658/784 | $0.001892 | 10.66 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.72 | 1 | no | not audited | 5 | 26318/1289 | $0.002386 | 20.16 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.69 | 0 | yes | not audited | 4 | 14832/765 | $0.001626 | 17.56 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | ok | 0.69 | 0 | yes | not audited | 5 | 19452/881 | $0.001949 | 13.25 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 4 | 12322/728 | $0.001302 | 10.99 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.67 | 1 | no | not audited | 4 | 16588/1149 | $0.001663 | 15.25 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | ok | 0.66 | 2 | no | not audited | 5 | 35102/1811 | $0.002908 | 19.60 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.64 | 0 | yes | not audited | 3 | 12267/676 | $0.001511 | 8.93 |
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.63 | 1 | no | not audited | 5 | 21372/1119 | $0.001964 | 15.17 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.59 | 1 | no | not audited | 4 | 12665/1205 | $0.001395 | 17.81 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | error | — | 1 | no | not audited | 5 | 17664/1082 | $0.001382 | 14.12 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | error | — | 1 | no | not audited | 5 | 14586/784 | $0.001371 | 13.07 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
