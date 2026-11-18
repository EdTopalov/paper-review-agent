"""Build an offline accuracy/cost report from immutable launcher stage records.

Requires matplotlib and scipy in addition to the project dependencies. The one
plot pools exact correctness over all 76 tasks, using only complete repetitions
shared by the compared methods. No model clients or requests are constructed.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from math import isfinite, sqrt
from pathlib import Path
import statistics

from paper_review.benchmark_data import DEFAULT_BENCHMARK, load_benchmark
from paper_review.benchmark_scoring import score_predictions
from paper_review.paper import file_hash


METHODS = {"agent": ("Native ReAct", "#0072B2"),
           "pyagent_react": ("PyAgent", "#E69F00"),
           "deliberative_review": ("Deliberative", "#009E73"),
           "baseline": ("Full-text baseline", "#6B7280")}
TRACKS = {"qasper": ("QASPER", "Exact-answer accuracy (%)", "Answer F1"),
          "reviewcritique": ("ReviewCritique", "Label accuracy (%)", "Binary macro-F1"),
          "controlled": ("Controlled appraisal", "Verdict accuracy (%)", "Pair accuracy"),
          "selection": ("Selection pilot", "Acceptable-choice accuracy (%)", "Acceptable-choice accuracy")}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def read_live_records(path):
    """Ignore only an unfinished final JSONL line; reject other corruption."""
    lines = Path(path).read_bytes().splitlines(keepends=True)
    records, unfinished = [], False
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except (json.JSONDecodeError, UnicodeDecodeError):
            if index != len(lines) - 1 or line.endswith(b"\n"):
                raise ValueError(f"Malformed persisted record: {path}") from None
            unfinished = True
    return records, unfinished


def mean_interval(values):
    """Untruncated 95% Student-t interval over complete repetition means."""
    values = list(values)
    known = [value for value in values if value is not None]
    if any(not isinstance(value, (int, float)) or isinstance(value, bool) or not isfinite(value)
           for value in known):
        raise ValueError("Report metrics must be finite numbers or unknown")
    result = {"repetitions": len(values), "known_repetitions": len(known), "mean": None, "ci95": None}
    if not values or len(known) != len(values):
        return result
    result["mean"] = statistics.mean(values)
    if len(values) >= 2:
        from scipy.stats import t
        half = float(t.ppf(.975, len(values) - 1)) * statistics.stdev(values) / sqrt(len(values))
        result["ci95"] = [result["mean"] - half, result["mean"] + half]
    return result


def collect(experiments, tasks, manifest_sha256, variants=None):
    roots = [Path(path).resolve() for path in experiments]
    if len(roots) != len(set(roots)):
        raise ValueError("Do not supply an experiment directory twice")
    metadata = [(root, read_json(root / "experiment.json")) for root in roots]
    configured = {variant for _, row in metadata for variant in row["variants"]}
    variants = list(variants) if variants is not None else [name for name in METHODS if name in configured]
    if not variants or len(variants) != len(set(variants)) or set(variants) - configured:
        raise ValueError("Choose distinct methods configured in the supplied experiments")
    models = {row["model"] for _, row in metadata}
    if len(models) != 1 or not all(isinstance(model, str) and model.strip() for model in models):
        raise ValueError("Report one model block at a time")
    expected = {"core": {task["id"] for task in tasks if task["track"] != "selection"},
                "selection": {task["id"] for task in tasks if task["track"] == "selection"}}
    attempts, provenance, notes = {}, [], []
    configurations = defaultdict(set)
    source_hashes = defaultdict(set)
    m2 = {}
    m2_hashes = set()
    for root, settings in metadata:
        if settings.get("m2_sample_sha256"):
            m2_hashes.add(settings["m2_sample_sha256"])
        m2_path = root / "m2-rounds.json"
        if m2_path.exists():
            for entry in read_json(m2_path):
                for variant, summary in entry["summary"].items():
                    if variant not in variants:
                        continue
                    key = variant, entry["round"]
                    if key in m2:
                        raise ValueError(f"Ambiguous duplicate M2 method/repetition: {key}")
                    m2[key] = summary
        for stage in expected:
            for path in sorted(root.glob(f"r*/{stage}/records.jsonl")):
                round_text = path.parent.parent.name[1:]
                if not round_text.isdigit() or int(round_text) < 1:
                    raise ValueError(f"Invalid round folder: {path}")
                round_number = int(round_text)
                plan = read_json(path.parent / "plan.json")
                if (plan["manifest_sha256"] != manifest_sha256 or plan["split"] != "test"
                        or set(plan["task_ids"]) != expected[stage] or plan["repeats"] != 1):
                    raise ValueError(f"Stage does not match the complete frozen task slice: {path.parent}")
                if plan["config"]["model"] not in models:
                    raise ValueError("Stage model differs from its experiment")
                configurations[stage].add(json.dumps(plan["config"], sort_keys=True))
                for variant in set(plan["variants"]) & set(variants):
                    source_hashes[variant].add(plan["source_sha256"])
                rows, unfinished = read_live_records(path)
                if unfinished:
                    notes.append(f"Ignored unfinished final JSONL line in {path}.")
                seen = set()
                for row in rows:
                    key = row.get("id"), row.get("variant"), row.get("repeat")
                    if (key in seen or key[0] not in expected[stage] or key[1] not in plan["variants"]
                            or type(key[2]) is not int or key[2] != 1 or row.get("model") not in models
                            or row.get("status") not in {"ok", "error"}):
                        raise ValueError(f"Invalid or duplicate stage attempt: {path}")
                    seen.add(key)
                progress_path = path.parent / "progress.json"
                stage_progress = read_json(progress_path) if progress_path.exists() else {}
                provenance.append({"experiment": str(root), "stage": stage, "round": round_number,
                                   "source_sha256": plan["source_sha256"],
                                   "manifest_sha256": plan["manifest_sha256"],
                                   "config": plan["config"], "workers": plan["workers"],
                                   "seed": plan["seed"], "records": str(path),
                                   "started_at": stage_progress.get("started_at"),
                                   "updated_at": stage_progress.get("updated_at")})
                for variant in variants:
                    if variant not in plan["variants"]:
                        continue
                    selected = [row for row in rows if row["variant"] == variant]
                    key = stage, variant, round_number
                    if key in attempts:
                        raise ValueError(f"Ambiguous duplicate stage/method/repetition: {key}")
                    attempts[key] = selected
                    if {row["id"] for row in selected} != expected[stage]:
                        notes.append(f"Excluded incomplete {stage} round {round_number} for {variant}: "
                                     f"{len(selected)}/{len(expected[stage])} terminal attempts.")
    if any(len(configs) != 1 for configs in configurations.values()):
        raise ValueError("Compared stages have different per-attempt model/resource settings")
    if any(len(hashes) != 1 for hashes in source_hashes.values()):
        raise ValueError("A method changes frozen source within a model block; report it as a new block")
    if len(m2_hashes) > 1:
        raise ValueError("M2 source samples differ between experiment blocks")
    common = {}
    for stage, ids in expected.items():
        per_variant = [{round_number for (row_stage, method, round_number), rows in attempts.items()
                        if row_stage == stage and method == variant and {row["id"] for row in rows} == ids}
                       for variant in variants]
        common[stage] = sorted(set.intersection(*per_variant))
    return {"variants": variants, "model": next(iter(models)), "attempts": attempts,
            "common_rounds": common, "provenance": provenance, "notes": notes, "m2": m2,
            "source_sha256_by_method": {variant: next(iter(hashes)) for variant, hashes in source_hashes.items()}}


def summarize_stage(tasks, collected, stage):
    rounds, variants = collected["common_rounds"][stage], collected["variants"]
    if not rounds:
        return {"rounds": [], "methods": {}}
    selected_tasks = [task for task in tasks if (task["track"] == "selection") == (stage == "selection")]
    records = [{**row, "repeat": number, "source_repeat": 1, "source_round": number}
               for variant in variants for number in rounds
               for row in collected["attempts"][stage, variant, number]]
    scored = score_predictions(selected_tasks, records, variants=variants, repeats=rounds)
    output = {}
    for variant in variants:
        output[variant] = {}
        for track, summary in scored["variants"][variant]["tracks"].items():
            repetitions = [summary["per_repeat"][str(number)] for number in rounds]
            if track == "qasper":
                primary = [row["mean_answer_f1"] * 100 for row in repetitions]
            elif track == "reviewcritique":
                primary = [row["classification"]["macro_f1"] * 100 for row in repetitions]
            elif track == "controlled":
                primary = []
                for number in rounds:
                    pairs = defaultdict(list)
                    for row in scored["items"]:
                        if row["variant"] == variant and row["repeat"] == number and row["track"] == track:
                            pairs[row["pair_id"]].append(row["content_correct"])
                    if any(len(pair) != 2 for pair in pairs.values()):
                        raise ValueError("Controlled source pair is incomplete")
                    primary.append(statistics.mean(all(pair) for pair in pairs.values()) * 100)
            else:
                primary = [row["content_success_rate"] * 100 for row in repetitions]
            accuracy = [row["content_success_rate"] * 100 for row in repetitions]
            costs = [row["mean_estimated_cost_usd"] for row in repetitions]
            output[variant][track] = {"attempts": summary["attempts"], "completed": summary["completed"],
                "rounds": rounds, "accuracy_percent": mean_interval(accuracy),
                "primary_metric": TRACKS[track][2], "primary_percent": mean_interval(primary),
                "usd_per_attempt": mean_interval(costs),
                "unknown_cost_attempts": summary["unknown_estimated_cost_usd_attempts"],
                "billing_uncertain_attempts": summary["billing_uncertain_attempts"],
                "repetition_values": [{"round": number, "accuracy_percent": accuracy[index],
                                       "primary_percent": primary[index], "usd_per_attempt": costs[index]}
                                      for index, number in enumerate(rounds)]}
    return {"rounds": rounds, "methods": output}


def summarize_m2(collected):
    variants, entries = collected["variants"], collected["m2"]
    common = sorted(set.intersection(*[{number for (method, number), row in entries.items()
                                       if method == variant and row["runs"] == 20} for variant in variants]))
    methods = {}
    for variant in variants:
        rows = [entries[variant, number] for number in common]
        if not rows:
            continue
        verified = [row["all_citations_verified"] / row["runs"] * 100
                    if row["all_citations_verified"] is not None else None for row in rows]
        methods[variant] = {"attempts": sum(row["runs"] for row in rows),
            "completion_percent": mean_interval(row["completed"] / row["runs"] * 100 for row in rows),
            "all_citations_verified_percent": mean_interval(verified),
            "usd_per_attempt": mean_interval(row["mean_cost_usd"] for row in rows)}
    return {"rounds": common, "methods": methods}


def summarize_pooled(tasks, collected):
    rounds = sorted(set(collected["common_rounds"]["core"]) & set(collected["common_rounds"]["selection"]))
    if not rounds:
        return {"rounds": [], "tasks_per_repetition": len(tasks), "methods": {}}
    variants = collected["variants"]
    records = [{**row, "repeat": number, "source_repeat": 1, "source_round": number}
               for variant in variants for number in rounds for stage in ("core", "selection")
               for row in collected["attempts"][stage, variant, number]]
    scored = score_predictions(tasks, records, variants=variants, repeats=rounds)
    methods = {}
    for variant in variants:
        values = []
        for number in rounds:
            rows = [row for row in scored["items"] if row["variant"] == variant and row["repeat"] == number]
            costs = [row["usage"].get("estimated_cost_usd") for row in rows]
            values.append({"round": number, "attempts": len(rows),
                           "correct": sum(row["content_correct"] for row in rows),
                           "accuracy_percent": statistics.mean(row["content_correct"] for row in rows) * 100,
                           "usd_per_attempt": statistics.mean(costs) if all(value is not None for value in costs) else None,
                           "unknown_cost_attempts": sum(value is None for value in costs),
                           "billing_uncertain_attempts": sum(bool(row["usage"].get("billing_uncertain")) for row in rows)})
        methods[variant] = {"attempts": sum(row["attempts"] for row in values),
            "correct": sum(row["correct"] for row in values),
            "accuracy_percent": mean_interval(row["accuracy_percent"] for row in values),
            "usd_per_attempt": mean_interval(row["usd_per_attempt"] for row in values),
            "unknown_cost_attempts": sum(row["unknown_cost_attempts"] for row in values),
            "billing_uncertain_attempts": sum(row["billing_uncertain_attempts"] for row in values),
            "repetition_values": values}
    return {"rounds": rounds, "tasks_per_repetition": len(tasks), "methods": methods}


def draw_plot(report, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.ticker import FormatStrFormatter

    fig, axis = plt.subplots(figsize=(8, 5.5))
    axis.set_title("Mixed-task exact-content accuracy and cost", fontsize=13)
    axis.set_xlabel("Mean estimated USD per attempted task")
    axis.set_ylabel("Exact-content accuracy (%)")
    axis.grid(alpha=.2)
    axis.xaxis.set_major_formatter(FormatStrFormatter("%.5f"))
    any_points = False
    markers = ["o", "s", "^", "D"]
    for model_index, model_report in enumerate(report["models"].values()):
        for variant in report["variants"]:
            metrics = model_report["pooled"]["methods"].get(variant)
            if not metrics or metrics["usd_per_attempt"]["mean"] is None:
                continue
            any_points = True
            x, y = metrics["usd_per_attempt"], metrics["accuracy_percent"]
            xerr = [[x["mean"] - x["ci95"][0]], [x["ci95"][1] - x["mean"]]] if x["ci95"] else None
            yerr = [[y["mean"] - y["ci95"][0]], [y["ci95"][1] - y["mean"]]] if y["ci95"] else None
            axis.errorbar(x["mean"], y["mean"], xerr=xerr, yerr=yerr,
                          fmt=markers[model_index % len(markers)], markersize=8,
                          color=METHODS.get(variant, (variant, "#333333"))[1], capsize=5, linewidth=1.5)
    if not any_points:
        axis.text(.5, .5, "Awaiting complete comparable repetitions\nwith known costs",
                  ha="center", va="center", transform=axis.transAxes, fontsize=11)
        axis.set_ylim(0, 100)
    else:
        low, high = axis.get_ylim()
        axis.set_ylim(min(0, low), max(100, high))
    handles = [Line2D([], [], marker="o", linestyle="", color=METHODS.get(name, (name, "#333333"))[1],
                      label=METHODS.get(name, (name, "#333333"))[0]) for name in report["variants"]]
    methods_legend = axis.legend(handles=handles, loc="upper left", frameon=True, fontsize=9)
    axis.add_artist(methods_legend)
    model_handles = [Line2D([], [], marker=markers[index % len(markers)], linestyle="", color="#222222",
                           label=f"{model} (n={len(values['pooled']['rounds'])})")
                     for index, (model, values) in enumerate(report["models"].items())]
    axis.legend(handles=model_handles, loc="upper right", frameon=True, fontsize=9)
    fig.text(.5, .015, "76 cases per repetition; failures included. Bars: 95% Student-t intervals when n ≥ 2.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, .035, 1, 1))
    fig.savefig(out / "accuracy-cost.svg", bbox_inches="tight")
    fig.savefig(out / "accuracy-cost.png", dpi=170, bbox_inches="tight")
    plt.close(fig)


def format_estimate(value, decimals=2):
    if value["mean"] is None:
        return "unknown"
    text = f"{value['mean']:.{decimals}f}"
    if value["ci95"]:
        text += f" [{value['ci95'][0]:.{decimals}f}, {value['ci95'][1]:.{decimals}f}]"
    return text


def write_markdown(report, out):
    repetition_text = "; ".join(f"`{model}`: {values['pooled']['rounds'] or 'pending'}"
                                for model, values in report["models"].items())
    lines = ["# M3 comparison results", "", f"Complete repetitions shared by all methods within each model: {repetition_text}.", "",
             "![Accuracy and cost](accuracy-cost.svg)", "",
             "[Machine-readable results and provenance](results.json) · [PNG figure](accuracy-cost.png)", "",
             "Accuracy counts exact QASPER answers (normalized F1 = 1), correct expert labels "
             "and controlled verdicts, and acceptable selection/abstention over 76 tasks "
             "(20/20/24/12). Cases weigh equally; failures score zero. This descriptive aggregate "
             "does not establish overall review usefulness.", "",
             "26 development cases were excluded; test groups are disjoint by paper, study family or candidate set.", "",
             "Models remain separate; attempts per method equal 76 × included repetitions.", ""]
    columns = ["Method"]
    for model in report["models"]:
        columns.extend([f"{model}: accuracy (%)", f"{model}: USD/task"])
    lines += ["| " + " | ".join(columns) + " |", "|---|" + "---:|" * (len(columns) - 1)]
    for variant in report["variants"]:
        cells = [METHODS.get(variant, (variant,))[0]]
        for model_report in report["models"].values():
            values = model_report["pooled"]["methods"].get(variant)
            cells.extend([format_estimate(values["accuracy_percent"]), format_estimate(values["usd_per_attempt"], 6)]
                         if values else ["pending", "pending"])
        lines.append("| " + " | ".join(cells) + " |")
    lines += ["", "Brackets/error bars are untruncated 95% Student-t intervals across complete repetition "
              "means; n=1 has none. Costs include failures and retries; unknowns stay unknown. "
              "Incomplete rounds are excluded. Intervals describe run variation on these fixed tasks.", "",
              "JSON retains per-track F1/pair metrics, M2 completion/citations, source hashes and "
              "timing. Separate source/scheduling blocks and later deliberative starts prevent "
              "controlled latency comparisons. API/protocol failures also lower accuracy; this "
              "aggregate cannot isolate scientific reasoning quality.", "",
              "Rebuild offline from the repository root after installing `requirements-report.txt`:", "",
              "```shell", "python scripts/report_m3_results.py " + " ".join(report.get("experiments", []))
              + " --out " + out.as_posix(), "```", ""]
    (out / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def generate(experiments, out, *, root=DEFAULT_BENCHMARK, variants=None):
    root, out = Path(root), Path(out)
    tasks = load_benchmark(root, "test")
    if Counter(task["track"] for task in tasks) != {"qasper": 20, "reviewcritique": 20, "controlled": 24, "selection": 12}:
        raise ValueError("The report requires the frozen 76-case benchmark test split")
    by_model = defaultdict(list)
    for experiment in experiments:
        by_model[read_json(Path(experiment) / "experiment.json")["model"]].append(experiment)
    models = {}
    for model, paths in by_model.items():
        collected = collect(paths, tasks, file_hash(root / "manifest.jsonl"), variants)
        models[model] = {"model": model, "variants": collected["variants"],
                         "pooled": summarize_pooled(tasks, collected),
                         "core": summarize_stage(tasks, collected, "core"),
                         "selection": summarize_stage(tasks, collected, "selection"),
                         "m2": summarize_m2(collected), "provenance": collected["provenance"],
                         "notes": collected["notes"], "source_sha256_by_method": collected["source_sha256_by_method"]}
    report = {"schema_version": "m3-result-report-v2", "generated_at": datetime.now(timezone.utc).isoformat(),
              "variants": [name for name in METHODS if any(name in values["variants"] for values in models.values())],
              "manifest_sha256": file_hash(root / "manifest.jsonl"), "models": models,
              "experiments": [Path(path).as_posix() for path in experiments]}
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                                       encoding="utf-8", newline="\n")
    draw_plot(report, out)
    write_markdown(report, out)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiments", type=Path, nargs="+")
    parser.add_argument("--root", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--out", type=Path, default=Path("milestones/M3-results"))
    parser.add_argument("--variants", nargs="+", choices=METHODS)
    args = parser.parse_args()
    report = generate(args.experiments, args.out, root=args.root, variants=args.variants)
    print(json.dumps({"out": str(args.out), "complete_rounds": {
        model: values["pooled"]["rounds"] for model, values in report["models"].items()}, "model_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
