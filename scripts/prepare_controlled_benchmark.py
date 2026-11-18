"""Freeze synthetic scientific-appraisal pairs and explicit-brief selections.

Study records and deterministic oracles precede document rendering. This script
uses no model, network service, or pre-existing evaluation result. All examples
are hypothetical; the targets describe the supplied reports, not scientific merit.
"""

import argparse
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import statistics


ROOT = Path(__file__).resolve().parents[1]
VERSION = "controlled-scientific-appraisal-v1"
DISCLOSURE = (
    "The supplied documents are hypothetical research reports. Assess only their "
    "stated content. Document blocks are text locations, not PDF page numbers."
)
CLAIM_INSTRUCTIONS = DISCLOSURE + (
    " Judge the statement as supported, contradicted, or insufficient. Supported "
    "means the report supplies the needed evidence at the stated scope; contradicted "
    "means the report supplies incompatible facts; insufficient means the supplied "
    "evidence does not establish the statement or its negation. Return the verdict, "
    "a short explanation, and the document/block IDs used. A valid quotation alone "
    "does not establish the inference."
)
SELECTION_INSTRUCTIONS = DISCLOSURE + (
    " Apply the club brief's explicit eligibility and preference rules. Return one "
    "selected candidate ID, or null when none is eligible; return every equally "
    "preferred candidate in tied_ids, including the selected candidate when tied. "
    "For a unique choice tied_ids may be empty or contain that candidate. Explain "
    "the decisive comparison and cite document/block IDs. These rules define this "
    "controlled task, not universal paper quality."
)


def identifier(prefix, *parts):
    value = ":".join([VERSION, *map(str, parts)])
    return prefix + sha256(value.encode("utf-8")).hexdigest()[:12]


def dump_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def block(number, section, text):
    return {"id": f"b{number:04d}", "section": section, "text": text}


def claim_oracle(family, facts):
    """Return the bounded claim label, without inspecting its rendered prose."""
    if family == "confidence_interval":
        low, high = facts["interval95"]
        if low > 0:
            return "supported"
        if high < 0:
            return "contradicted"
        return "insufficient"
    if family == "total_cost":
        new_total = facts["new_preparation_usd"] + facts["new_inference_usd"]
        old_total = facts["baseline_preparation_usd"] + facts["baseline_inference_usd"]
        return "supported" if new_total < old_total else "contradicted"
    if family == "independent_evaluation":
        overlap = set(facts["tuning_ids"]) & set(facts["evaluation_ids"])
        return "contradicted" if overlap else "supported"
    if family == "language_scope":
        tested = set(facts["tested_languages"])
        return "supported" if set(facts["claimed_languages"]) <= tested else "insufficient"
    if family == "seed_aggregation":
        return "supported" if facts["headline_accuracy"] == statistics.mean(facts["seed_accuracies"]) else "contradicted"
    if family == "appendix_comparison":
        return "contradicted" if facts["additional_quantitative_problems"] > 0 else "supported"
    raise ValueError(f"Unknown controlled family: {family}")


def claim_record(family, index, condition):
    """Create factual records first; each pair changes only its decisive fact."""
    is_first = condition == "a"
    if family == "confidence_interval":
        shift = index * 0.2
        interval = [round(0.7 + shift, 1), round(2.3 + shift, 1)] if is_first else (
            [-1.0, 1.4] if index % 2 == 0 else [-2.4, -0.6])
        facts = {"interval95": interval, "two_sided_alpha": 0.05,
                 "same_prespecified_test_and_interval": True}
        statement = "The prespecified analysis supplies evidence of a positive effect at its two-sided 5% significance threshold."
    elif family == "total_cost":
        facts = {"evaluation_requests": 1000 + 500 * index,
                 "baseline_preparation_usd": 20, "baseline_inference_usd": 180 + 20 * index,
                 "new_preparation_usd": 30 if is_first else 240 + 20 * index,
                 "new_inference_usd": 80 + 10 * index}
        statement = "At the reported evaluation volume, the new method costs less in total, including preparation and inference."
    elif family == "independent_evaluation":
        facts = {"tuning_ids": [f"Q{index}11", f"Q{index}12", f"Q{index}13"],
                 "evaluation_ids": [f"Q{index}21", f"Q{index}22", f"Q{index}23"]}
        if not is_first:
            facts["evaluation_ids"][1] = facts["tuning_ids"][1]
        statement = "None of the reported final evaluation examples was used for prompt tuning or model selection."
    elif family == "language_scope":
        facts = {"claimed_languages": ["English", "German", "Spanish"],
                 "tested_languages": ["English", "German", "Spanish"] if is_first else ["English"],
                 "baseline_accuracy": 66 + index, "new_accuracy": 70 + index}
        statement = "For this study's task, the new method has higher accuracy than its matched baseline in each of English, German, and Spanish."
    elif family == "seed_aggregation":
        values = [66 + index, 68 + index, 70 + index, 72 + index, 74 + index]
        facts = {"seed_accuracies": values,
                 "headline_accuracy": statistics.mean(values) if is_first else max(values)}
        statement = "The headline accuracy equals the arithmetic mean across all reported random seeds."
    elif family == "appendix_comparison":
        facts = {"illustrative_examples": 2,
                 "additional_quantitative_problems": 12 + 4 * index if is_first else 0,
                 "method_correct": 8 + 2 * index if is_first else 0,
                 "baseline_correct": 7 + 2 * index if is_first else 0}
        statement = "The paper provides no numerical comparison on additional held-out problems beyond its two illustrative examples."
    else:
        raise ValueError(family)
    return facts, statement


def render_claim(family, facts):
    """Render exact study records; decisive sources retain stable block IDs."""
    overview = "We investigate a small methodological change in a controlled research setting. The report presents the study protocol, measured results, and analysis details. Claims are limited to the reported experiment."
    protocol = "The analysis plan specifies the reported comparison and records the relevant evaluation conditions. The reported numbers describe this experiment; no independent replication is claimed."
    methods = "The baseline and new method receive the same input format. The comparison changes one methodological component while recording study-specific conditions below."
    results = "The results are described together with the study record so that readers can evaluate the stated conclusion at its reported scope."
    appendix = "The appendix supplies additional analysis details. It is part of the complete supplied report and should be considered when judging broad claims about missing evidence."
    evidence = []
    if family == "confidence_interval":
        results = (f"The estimated effect is expressed in percentage points. The two-sided 95% confidence interval is "
                   f"[{facts['interval95'][0]}, {facts['interval95'][1]}]. The prespecified two-sided test uses alpha=0.05 "
                   "and is the inversion of this confidence interval under the same analysis. A nonsignificant outcome is not an equivalence finding.")
        evidence = [4]
    elif family == "total_cost":
        results = (f"For {facts['evaluation_requests']} evaluation requests, baseline inference costs USD {facts['baseline_inference_usd']} "
                   f"and new-method inference costs USD {facts['new_inference_usd']}. These are inference expenses, excluding preparation.")
        appendix = (f"One-time preparation for this experiment costs USD {facts['baseline_preparation_usd']} for the baseline "
                    f"and USD {facts['new_preparation_usd']} for the new method. The complete reported total for each method is its preparation plus inference expense; no other expense is included.")
        evidence = [4, 7]
    elif family == "independent_evaluation":
        methods = ("Prompt tuning and model selection use exactly these example identifiers: "
                   + ", ".join(facts["tuning_ids"]) + ". No other examples are used for that process.")
        appendix = ("The final evaluation uses exactly these example identifiers: "
                    + ", ".join(facts["evaluation_ids"]) + ". An identifier denotes the same example wherever it appears.")
        evidence = [3, 7]
    elif family == "language_scope":
        methods = "The report discusses possible use in English, German, and Spanish. Discussion of a language does not by itself constitute an experiment."
        results = ("Evaluation languages are exactly: " + ", ".join(facts["tested_languages"]) + ". "
                   f"In each evaluated language, baseline accuracy is {facts['baseline_accuracy']}% and the new method's accuracy is {facts['new_accuracy']}%. "
                   "No other language evaluation was conducted. These are descriptive accuracies for the supplied test examples.")
        evidence = [4]
    elif family == "seed_aggregation":
        overview = f"We report a headline accuracy of {facts['headline_accuracy']}%. The study repeats the procedure across several random seeds and supplies every seed-level result."
        appendix = ("Accuracy percentages for all five random seeds are: " + ", ".join(map(str, facts["seed_accuracies"]))
                    + ". Every reported seed has equal weight in the arithmetic mean. No seed is excluded from that definition.")
        evidence = [1, 7]
    elif family == "appendix_comparison":
        results = "The main text illustrates the method on two held-out problems and discusses their solution traces qualitatively. The examples demonstrate behavior but provide only a small illustrative comparison."
        if facts["additional_quantitative_problems"]:
            appendix = (f"Additional quantitative evaluation uses {facts['additional_quantitative_problems']} different held-out problems, excluded from the two main-text illustrations. "
                        f"With one trial, the method solves {facts['method_correct']} and the baseline solves {facts['baseline_correct']}. "
                        "This numerical follow-up is still small and does not establish broad superiority.")
        else:
            appendix = "The appendix supplies only the two main-text solution traces. The complete evaluation consists of those two illustrative problems; no additional held-out problems were evaluated quantitatively."
        evidence = [4, 7]
    blocks = [block(1, "Overview", overview), block(2, "Protocol", protocol), block(3, "Methods", methods),
              block(4, "Results", results),
              block(5, "Scope", "The experiment is intentionally narrow. Results are not evidence of performance on untested tasks or settings. An open question about generalization is different from a demonstrated implementation defect."),
              block(6, "Reproducibility", "All study-specific quantities needed for the supplied claim are disclosed in this report. The hypothetical study does not claim that a real experiment has been reproduced."),
              block(7, "Appendix", appendix)]
    return blocks, [{"document_id": "P1", "block_id": f"b{number:04d}"} for number in evidence]


def controlled_cases():
    cases = []
    families = [("confidence_interval", "dev", 2), ("total_cost", "dev", 2),
                ("independent_evaluation", "test", 3), ("language_scope", "test", 3),
                ("seed_aggregation", "test", 3), ("appendix_comparison", "test", 3)]
    for family, split, count in families:
        for index in range(count):
            pair_id = identifier("PAIR-", family, index)
            for condition in ("a", "b"):
                task_id = identifier("CB-", family, index, condition)
                facts, statement = claim_record(family, index, condition)
                blocks, evidence = render_claim(family, facts)
                public = {"id": task_id, "kind": "claim", "instructions": CLAIM_INSTRUCTIONS,
                          "statement": statement,
                          "documents": [{"id": "P1", "title": "Research report " + task_id[-6:], "blocks": blocks}]}
                reference = {"id": task_id, "verdict": claim_oracle(family, facts), "evidence": evidence,
                             "pair_id": pair_id, "family": family, "condition": condition, "facts": facts,
                             "label_origin": "programmatic_oracle"}
                cases.append((split, "controlled:" + family, public, reference))
    return cases


REPLICATION_BRIEF = (
    "The club wants a retrieval question-answering method to reproduce. Eligible candidates must evaluate retrieval question answering in both English and German; "
    "use no more than 24 GB peak GPU memory; use final evaluation examples not used during tuning; and report all five planned random seeds. "
    "Among eligible candidates prefer the larger lower bound of the reported 95% effect interval, then lower peak GPU memory. "
    "Candidates equal on both preference quantities tie. Select null if none is eligible. This is an explicit selection policy, not a universal scientific-merit rating."
)
CRITIQUE_BRIEF = (
    "The club wants a documented seed-selection error for a discussion of experimental methodology. Eligible candidates must disclose at least five seed accuracies, "
    "call the headline their mean accuracy, but set that headline to the best seed rather than the actual arithmetic mean. Peak GPU memory must be no more than 24 GB. "
    "Among eligible candidates prefer the larger headline-minus-mean gap, then lower peak GPU memory. Equal quantities tie. Select null if no candidate qualifies. "
    "A flawed report is useful for this explicitly stated discussion goal; this is not a universal scientific-merit rating."
)


def selection_oracle(candidates, profile):
    eligible = []
    for candidate in candidates:
        disclosed_seeds = candidate["seed_accuracies"][:candidate["reported_seeds"]]
        if profile == "replication":
            valid = (candidate["task"] == "retrieval question answering"
                     and {"English", "German"} <= set(candidate["languages"])
                     and candidate["peak_gpu_gb"] <= 24 and candidate["independent_test"]
                     and candidate["reported_seeds"] == candidate["planned_seeds"] == 5
                     and len(disclosed_seeds) == 5)
            preference = (-candidate["effect_interval95"][0], candidate["peak_gpu_gb"])
        elif profile == "critique":
            mean = statistics.mean(disclosed_seeds) if disclosed_seeds else 0
            valid = (len(disclosed_seeds) >= 5 and candidate["peak_gpu_gb"] <= 24
                     and candidate["headline_label"] == "mean accuracy"
                     and candidate["headline_accuracy"] == max(disclosed_seeds)
                     and candidate["headline_accuracy"] != mean)
            preference = (-(candidate["headline_accuracy"] - mean), candidate["peak_gpu_gb"])
        else:
            raise ValueError(profile)
        if valid:
            eligible.append((candidate["id"], preference))
    best = min((score for _, score in eligible), default=None)
    return {"eligible_ids": sorted(task_id for task_id, _ in eligible),
            "acceptable_ids": sorted(task_id for task_id, score in eligible if score == best)}


def candidate_record(base_id, index):
    return {"id": identifier("P-", base_id, index), "task": "retrieval question answering",
            "languages": ["English", "German"], "peak_gpu_gb": 12 + 2 * (index % 4),
            "independent_test": True, "reported_seeds": 5, "planned_seeds": 5,
            "effect_interval95": [1 + (index % 3), 5 + (index % 3)],
            "seed_accuracies": [66, 68, 70, 72, 74], "headline_accuracy": 70,
            "headline_label": "mean accuracy"}


def selection_records(base_id, count, profile, special):
    candidates = [candidate_record(base_id, index) for index in range(count)]
    if profile == "critique":
        for index, candidate in enumerate(candidates):
            candidate["headline_accuracy"] = max(candidate["seed_accuracies"])
            candidate["seed_accuracies"] = [60, 62, 64, 66, 70] if index == 0 else [66, 68, 70, 72, 74]
            candidate["headline_accuracy"] = max(candidate["seed_accuracies"])
        candidates[-1]["headline_accuracy"] = statistics.mean(candidates[-1]["seed_accuracies"])
    else:
        candidates[0]["effect_interval95"] = [6, 9]
        if special == "tie":
            candidates[1]["effect_interval95"] = list(candidates[0]["effect_interval95"])
            candidates[1]["peak_gpu_gb"] = candidates[0]["peak_gpu_gb"]
        elif special == "none":
            for index, candidate in enumerate(candidates):
                if index % 3 == 0:
                    candidate["peak_gpu_gb"] = 40
                elif index % 3 == 1:
                    candidate["independent_test"] = False
                else:
                    candidate["reported_seeds"] = 1
        elif special == "scope":
            candidates[1]["effect_interval95"] = [10, 14]
            candidates[1]["languages"] = ["English"]
            candidates[2]["effect_interval95"] = [12, 16]
            candidates[2]["task"] = "code repair"
        else:
            candidates[-1]["effect_interval95"] = [11, 15]
            candidates[-1]["peak_gpu_gb"] = 48
    return candidates


def render_candidate(candidate):
    tuning = "T11, T12, T13"
    evaluation = "E21, E22, E23" if candidate["independent_test"] else "E21, T12, E23"
    return {"id": candidate["id"], "title": "Candidate report " + candidate["id"][-6:], "blocks": [
        block(1, "Overview", f"The study evaluates {candidate['task']}. Its headline is described as {candidate['headline_label']}: {candidate['headline_accuracy']}%."),
        block(2, "Evaluation scope", "The evaluated languages are exactly " + ", ".join(candidate["languages"]) + ". No other task or language is evaluated in this report."),
        block(3, "Resources", f"Peak GPU memory is {candidate['peak_gpu_gb']} GB. This is the peak memory needed for the reported procedure, rather than total device capacity."),
        block(4, "Seed results", f"The plan called for {candidate['planned_seeds']} seeds and the report supplies {candidate['reported_seeds']}. Reported accuracy percentages are "
              + ", ".join(map(str, candidate["seed_accuracies"][:candidate["reported_seeds"]]))
              + f". The 95% confidence interval for the effect is [{candidate['effect_interval95'][0]}, {candidate['effect_interval95'][1]}] percentage points."),
        block(5, "Tuning", f"Prompt tuning and model selection use exactly these identifiers: {tuning}. The same identifier denotes the same example wherever it appears."),
        block(6, "Appendix: evaluation identities", f"Final evaluation uses exactly these identifiers: {evaluation}. This completes the disclosure of study-specific selection facts.")
    ]}


def selection_cases():
    bases = [("small_replication", "dev", 3, "replication", "unique"),
             ("equal_candidates", "dev", 6, "replication", "tie"),
             ("long_replication", "test", 9, "replication", "unique"),
             ("methodology_discussion", "test", 9, "critique", "unique"),
             ("no_eligible_candidate", "test", 6, "replication", "none"),
             ("domain_boundaries", "test", 3, "replication", "scope")]
    cases = []
    for base_id, split, count, profile, special in bases:
        candidates = selection_records(base_id, count, profile, special)
        middle = count - count // 2
        orders = [list(range(count)), list(range(middle, count)) + list(range(middle)), list(reversed(range(count)))]
        for order_id, order in enumerate(orders):
            task_id = identifier("SB-", base_id, order_id)
            ordered = [deepcopy(candidates[index]) for index in order]
            public = {"id": task_id, "kind": "selection", "instructions": SELECTION_INSTRUCTIONS,
                      "brief": REPLICATION_BRIEF if profile == "replication" else CRITIQUE_BRIEF,
                      "documents": [render_candidate(candidate) for candidate in ordered]}
            reference = {"id": task_id, **selection_oracle(candidates, profile), "facts": candidates,
                         "profile": profile, "family": base_id, "order_id": order_id, "base_set_id": base_id,
                         "candidate_order": [candidate["id"] for candidate in ordered],
                         "label_origin": "programmatic_oracle"}
            cases.append((split, "selection:" + base_id, public, reference))
    return cases


def write_track(root, track, cases):
    target = root / track
    target.mkdir(parents=True, exist_ok=True)
    rows = []
    for split, group_id, public, reference in cases:
        task_id = public["id"]
        paths = {"input": Path(track) / "inputs" / f"{task_id}.json",
                 "reference": Path(track) / "references" / f"{task_id}.json"}
        row = {"id": task_id, "track": track, "kind": public["kind"], "split": split, "group_id": group_id}
        for name, value in (("input", public), ("reference", reference)):
            content = dump_bytes(value)
            path = root / paths[name]
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists() and path.read_bytes() != content:
                raise ValueError(f"Existing frozen artifact differs: {path}; use a fresh output directory")
            path.write_bytes(content)
            row[name + "_path"] = paths[name].as_posix()
            row[name + "_sha256"] = sha256(content).hexdigest()
        rows.append(row)
    rows.sort(key=lambda row: row["id"])
    manifest = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows).encode("utf-8")
    path = target / "manifest.jsonl"
    if path.exists() and path.read_bytes() != manifest:
        raise ValueError(f"Existing manifest differs: {path}")
    path.write_bytes(manifest)
    source = {"version": VERSION, "track": track, "label_origin": "programmatic_oracle",
              "generator": "scripts/prepare_controlled_benchmark.py", "randomness": "none; identifiers are SHA-256-derived",
              "license": "CC0-1.0", "source": "Original hypothetical study records and rendered reports",
              "cases": len(rows), "counts_by_split": {split: sum(row["split"] == split for row in rows) for split in ("dev", "test")},
              "manifest_sha256": sha256(manifest).hexdigest(),
              "split_unit": "scientific family" if track == "controlled" else "candidate base set including all order permutations"}
    (target / "source.json").write_bytes(dump_bytes(source))
    return source


def prepare(out):
    out = Path(out)
    return {"controlled": write_track(out, "controlled", controlled_cases()),
            "selection": write_track(out, "selection", selection_cases())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "data/benchmark/v1")
    args = parser.parse_args()
    print(json.dumps(prepare(args.out), indent=2))


if __name__ == "__main__":
    main()
