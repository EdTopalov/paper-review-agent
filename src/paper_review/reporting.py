"""Readable views generated from the single structured trace for each task."""

import json
from pathlib import Path

from .trace import read_events, read_result


def money(value):
    return "unknown" if value is None else f"${value:.6f}"


def decimal(value):
    return "unavailable" if value is None else f"{value:.4f}"


def interval_text(metric):
    value, interval = metric["mean_difference"], metric["ci95"]
    if value is None:
        return "unavailable"
    bounds = f" [{interval[0]:.4f}, {interval[1]:.4f}]" if interval else " [unavailable]"
    return f"{value:.4f}{bounds}; n={metric['tasks']}"


def paper_title(events):
    return next((e["paper_metadata"].get("title", "") for e in events if e["event"] == "environment"), "")


def table_cell(text):
    return " ".join(str(text).split()).replace("|", "\\|")


def action_summary(arguments):
    values = {key: value for key, value in arguments.items() if key != "reason"}
    if isinstance(values.get("review"), dict):
        review = values["review"]
        observations = review.get("observations")
        values["review"] = {"score": review.get("score"), "observations": len(observations) if isinstance(observations, list) else "invalid"}
    text = json.dumps(values, ensure_ascii=False)
    return text if len(text) <= 180 else text[:180] + " …"


def observation_summary(observation):
    if observation.get("error"):
        details = []
        for index, check in enumerate(observation.get("citation_checks", []), 1):
            if check.get("citation_verified") and check.get("observed", True):
                continue
            label = check.get("status", "invalid") if not check.get("citation_verified") else "unobserved"
            pages = check.get("matching_pages") or check.get("candidate_pages")
            details.append(f"#{index}: {label}" + (f" (pages {pages})" if pages else ""))
        return observation["error"] + ("; " + "; ".join(details) if details else "")
    if observation.get("accepted"):
        return "review accepted"
    if "matches" in observation:
        pages = sorted({match["page"] for match in observation["matches"]})
        return f"{len(observation['matches'])} matches" + (f" on pages {pages}" if pages else "")
    if "pages" in observation:
        pages = [page["page"] for page in observation["pages"]]
        truncated = any(page.get("truncated") for page in observation["pages"])
        return f"read pages {pages}" + (" (text truncated by tool)" if truncated else "")
    return "response recorded"


def render_deliberative_phases(events):
    """Summarize role decisions while keeping full drafts in the raw trace."""
    starts = [index for index, event in enumerate(events) if event["event"] == "deliberative_phase"]
    if not starts:
        return ""
    lines = ["## Deliberative phases", "",
             "Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.", "",
             "| Step | Role | Decision or outcome | Events |", "|---|---|---|---|"]
    for position, start in enumerate(starts):
        phase = events[start]
        end = starts[position + 1] if position + 1 < len(starts) else len(events)
        following = events[start + 1:end]
        results = [event for event in following if event["event"] == "phase_result"]
        errors = [event for event in following if event["event"] == "phase_error"]
        observations = [event for event in following if event["event"] == "tool_observation"]
        value = results[-1]["result"] if results else {}
        role = phase["phase"]
        details = []
        linked = [phase]
        if errors:
            for event in errors:
                diagnostic = "; ".join(str(event[key]) for key in ("error", "code", "type") if event.get(key))
                details.append(diagnostic)
            linked += errors
        if role == "plan" and value:
            details.append("Checks: " + "; ".join(value["checks"]))
        elif role == "critic" and value:
            details.append("Recommendation: " + value["recommendation"])
            if value["issues"]:
                details.append("Issues: " + "; ".join(value["issues"]))
            if value["target"]:
                details.append("Target: " + value["target"])
        elif role in ("draft", "revise") and value:
            details.append("Draft prepared" if role == "draft" else "Draft revised")
            if value["changes"]:
                details.append("Changes: " + value["changes"])
        elif value.get("action") == "finish_reading":
            details.append("Finished exploration: " + value.get("reason", ""))
        elif role in ("investigate", "targeted_read") and observations:
            observation = observations[-1]["observation"]
            outcome = observation_summary(observation)
            if observation.get("location_unit") == "source_block":
                outcome = outcome.replace("pages", "source blocks")
            details.append(outcome)
            linked += observations
        linked += results
        if not details:
            details.append("No validated phase output; inspect the trace")
        summary = table_cell("; ".join(details))
        if len(summary) > 600:
            summary = summary[:600] + " …"
        links = " · ".join(f"[event {event['seq']}](trace.jsonl#L{event['seq']})" for event in linked)
        lines.append(f"| {phase['step']} | {role} | {summary} | {links} |")
    return "\n".join(lines) + "\n"


def render_run(path):
    path = Path(path)
    events = read_events(path)
    result = read_result(path)
    if result is None:
        raise ValueError(f"No terminal result in {path}")
    review = result.get("review")
    lines = [f"# {result['task_id']}: {paper_title(events)}", "",
             f"**{result['variant']} · {result['status']}**", "",
             f"{result['api_calls']} model calls · {result['reading_actions']} reads · "
             f"{result['latency_seconds']:.2f} s · {money(result['estimated_cost_usd'])}", "",
             f"{result.get('decision_steps') or 0} decisions · {result.get('tool_calls') or 0} tool calls · "
             f"{result.get('input_tokens', 0)} input tokens "
             f"({result.get('cached_input_tokens', 0)} cached) · {result.get('output_tokens', 0)} output tokens", "",
             "[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. "
             "This page shows the review once and summarizes each decision.", ""]
    if review:
        lines += [f"## Review · score {review['score']}", "", review["summary"], ""]
        for observation, check in zip(review["observations"], result.get("citation_checks", [])):
            status = check.get('status', 'strict match' if check.get('quote_matches') else 'no strict match')
            lines += [f"- **{observation['kind']}**: {observation['claim']}",
                      f"  - Page {observation['page']} · citation: {status}",
                      f"  - Quote: {json.dumps(observation['quote'], ensure_ascii=False)}", ""]
        if review["unresolved_questions"]:
            lines += ["Unresolved questions:", "", *[f"- {q}" for q in review["unresolved_questions"]], ""]
    else:
        lines += [f"Error: `{json.dumps(result.get('error'))}`", ""]
    audit = read_result(path, audit=True)
    if audit:
        lines += ["## Evidence audit", "", "Provisional model judgments, not human-validated accuracy.", ""]
        if audit["status"] == "ok":
            lines += [f"- Observation {o['index'] + 1}: **{o['verdict']}** — {o['explanation']}"
                      for o in audit["audit"]["observations"]]
        else:
            lines += [f"Audit error: `{json.dumps(audit.get('error'))}`"]
        lines += [""]
    run_events = events[:next(i for i, e in enumerate(events) if e["event"] == "run_end") + 1]
    phase_report = render_deliberative_phases(run_events)
    if phase_report:
        lines += [phase_report, ""]
    lines += ["## Decisions", "",
              "| Step | Action and key arguments | Purpose | Outcome | Event |",
              "|---|---|---|---|---|"]
    # Audit decisions are displayed above, separately from the review trajectory.
    for event in run_events:
        if event["event"] in ("model_error", "retry", "run_error"):
            detail = json.dumps(event.get('error', event.get('next_attempt')))
            lines += [f"| — | {event['event']} | | {table_cell(detail)} | [event {event['seq']}](trace.jsonl#L{event['seq']}) |"]
        if event["event"] != "decision":
            continue
        raw_arguments = event.get("arguments", "{}")
        try:
            arguments = json.loads(raw_arguments)
        except (json.JSONDecodeError, TypeError):
            arguments = None
        outcome = next((e["observation"] for e in run_events if e["event"] == "tool_observation"
                        and e["seq"] > event["seq"] and e["call_id"] == event.get("call_id")), {})
        if isinstance(arguments, dict):
            detail = f" `{action_summary(arguments)}`" if arguments else ""
            purpose = table_cell(arguments.get("reason", ""))
        else:
            detail = f" invalid arguments: `{str(raw_arguments)[:180]}`"
            purpose = ""
        outcome = table_cell(observation_summary(outcome) if "arguments" in event else "final response recorded")
        lines += [f"| {event['step']} | {event['action']} {table_cell(detail)} | {purpose} | {outcome} | "
                  f"[event {event['seq']}](trace.jsonl#L{event['seq']}) |"]
    lines += [""]
    path.with_name("README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def render_experiment(root, summary, records, audits):
    root = Path(root)
    lines = ["# Experiment results", "",
             "Open a task to read its review, decisions, tool outcomes, and optional evidence audit. "
             "[Settings](experiment.json) · [Evaluated source](source.zip)", "",
             "Completion means the workflow returned an accepted review. The agent also blocks invalid "
             "citations; the one-call baseline does not. Verified citations match source text, not necessarily "
             "the meaning of a claim. Summary rates include failed attempts.", "",
             "An evidence audit is a separate model judgment of claim support; supported counts are "
             "provisional verdicts. A first submission is the review proposed before citation repair.", "",
             "| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |",
             "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for name, row in summary.items():
        verified = row['all_citations_verified']
        lines += [f"| {name} | {row['completed']}/{row['runs']} | "
                  f"{verified if verified is not None else 'unavailable'}/{row['runs']} | "
                  f"{row['mean_decision_steps']:.2f} | {row['mean_tool_calls']:.2f} | "
                  f"{row['mean_reading_actions']:.2f} | {row['mean_model_calls']:.2f} | "
                  f"{row['mean_input_tokens']:.1f} | {row['mean_output_tokens']:.1f} | "
                  f"{money(row['mean_cost_usd'])} | {row['mean_latency_seconds']:.2f} |"]
    repeated = {name: row["repetition_statistics"] for name, row in summary.items()
                if "repetition_statistics" in row}
    if repeated:
        lines += ["", "## Repetition variation", "",
                  "Verified success requires both a completed review and all quotations verified. "
                  "It measures citation compliance, not assessment quality. Every planned attempt, including "
                  "a failed attempt, stays in the denominator. Model IDs are not pooled.", "",
                  "| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |",
                  "|---|---:|---:|---:|---:|---|---:|---:|"]
        for name, row in repeated.items():
            for attempt in row["per_repeat"]:
                verified = attempt["verified_successes"]
                lines += [f"| {name} | {attempt['repeat']} | {attempt['completed']}/{attempt['attempts']} | "
                          f"{verified if verified is not None else 'unavailable'}/{attempt['attempts']} | "
                          f"{attempt['mean_model_calls']:.2f} | "
                          f"{attempt['mean_input_tokens']:.1f}/{attempt['mean_output_tokens']:.1f} | "
                          f"{money(attempt['mean_cost_usd'])} | {attempt['mean_latency_seconds']:.2f} |"]
        lines += ["", "### Reliability across repetitions", "",
                  "pass^k estimates success on every one of k independent attempts: "
                  "mean over papers of C(s,k)/C(n,k), where s is the number of verified successes "
                  "and n the number of attempts for that paper. It is not success at least once. "
                  "Independence is an assumption; few repetitions give limited precision.", "",
                  "| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |",
                  "|---|---|---|---:|---:|"]
        for name, row in repeated.items():
            powers = "; ".join(f"k={k}: {value:.3f}" for k, value in (row["pass_power_k"] or {}).items()) or "unavailable"
            consistency = (f"{row['tasks_always_verified']} / {row['tasks_sometimes_verified']} / {row['tasks_never_verified']}"
                           if row["tasks_always_verified"] is not None else "unavailable")
            difference = row["within_task_mean_absolute_score_difference"]
            lines += [f"| {name} | {consistency} | {powers} | "
                      f"{decimal(difference)} | {row['within_task_score_pairs']} |"]
        lines += ["", "### Paired differences between methods", "",
                  "Each paper contributes its mean over observed repetitions. Differences are left minus right. "
                  "The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's "
                  "repetitions together (seed 20261118). These exploratory intervals describe this convenience "
                  "sample conditional on the observed repetitions; they do not capture future API model drift. "
                  "A single paper has no interval. Scores use only completed reviews from papers completed by "
                  "both methods and are not validated quality labels.", "",
                  "| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |",
                  "|---|---|---|---:|---:|---:|"]
        for name, row in repeated.items():
            for other, comparison in row["paired_comparisons"].items():
                absolute = comparison["mean_absolute_task_score_difference"]
                lines += [f"| {name} − {other} | {interval_text(comparison['verified_success_rate'])} | "
                          f"{interval_text(comparison['mean_score'])} | "
                          f"{decimal(absolute)} | "
                          f"{interval_text(comparison['mean_cost_usd'])} | "
                          f"{interval_text(comparison['mean_latency_seconds'])} |"]
        lines += ["", "### Per-paper consistency", "",
                  "Score spread excludes failed attempts; completion counts retain them. "
                  "Compare within-paper score variation above with between-method differences before interpreting small gaps.", "",
                  "| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |",
                  "|---|---|---:|---:|---:|---:|---|"]
        for name, row in repeated.items():
            for task_id, task in row["per_task"].items():
                score = task["mean_score"]
                spread = task["score_sample_sd"]
                lines += [f"| {name} | {task_id} | {task['completed']}/{task['attempts']} | "
                          f"{task['verified_successes'] if task['verified_successes'] is not None else 'unavailable'}/{task['attempts']} | "
                          f"{decimal(score)} | {decimal(spread)} | {task['score_range'] or 'unavailable'} |"]
    for variant in sorted({r['variant'] for _, r in records}):
        lines += ["", f"## {variant}", "",
                  "Completed papers are ordered by absolute score, then task ID; errors follow.", "",
                  "| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |",
                  "|---|---|---:|---:|---|---|---:|---|---:|---:|"]
        subset = [(p, r) for p, r in records if r['variant'] == variant]
        subset.sort(key=lambda item: (item[1]['status'] != 'ok', -(item[1].get('review') or {}).get('score', 0), item[1]['task_id'], str(item[0])))
        for path, result in subset:
            review = result.get('review') or {}
            first = result.get('first_submission_checks')
            first_ok = ('yes' if all(c.get('citation_verified', False) for c in first) else 'no') if first else 'unavailable'
            audit = audits.get(path)
            verdict = 'not audited'
            if audit:
                verdict = audit['status']
                if verdict == 'ok':
                    counts = audit['audit']['observations']
                    verdict = f"{sum(o['verdict'] == 'supported' for o in counts)}/{len(counts)} supported"
            link = path.parent.relative_to(root).as_posix() + '/README.md'
            title = paper_title(read_events(path)).replace('|', '\\|').replace('\n', ' ')
            lines += [f"| [{path.parent.parent.name}/{result['task_id']}: {title}]({link}) | {result['status']} | "
                      f"{review.get('score', '—')} | {result.get('rejected_submissions', 0)} | {first_ok} | {verdict} | "
                      f"{result['api_calls']} | {result.get('input_tokens', 0)}/{result.get('output_tokens', 0)} | "
                      f"{money(result['estimated_cost_usd'])} | {result['latency_seconds']:.2f} |"]
    if audits:
        costs = [a['estimated_cost_usd'] for a in audits.values()]
        cost = sum(costs) if all(c is not None for c in costs) and not any(a.get('billing_uncertain') for a in audits.values()) else None
        lines += ["", f"Evidence audit cost: {money(cost)}. These are provisional model verdicts; failed "
                  "reviews are not audited. Costs are estimates; unknown billing must be inspected in traces."]
    uncertain = sum(r['billing_uncertain_runs'] for r in summary.values())
    if uncertain:
        lines += ["", f"Billing is uncertain for {uncertain} review attempts; token estimates may omit charges."]
    lines += ["", "Per-task cost/time includes unsuccessful attempts; audit cost is separate.", ""]
    (root / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
