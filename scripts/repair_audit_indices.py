"""Normalize saved 1-based audit indices without new API calls or changed verdicts.

Preserves the original error result and appends a repair event to its trace.
"""

from datetime import datetime, timezone
import json
from pathlib import Path
import sys

import jsonschema

from paper_review.audit import AUDIT_SCHEMA, normalize_indices


def main():
    root = Path(sys.argv[1])
    repaired = []
    for path in sorted((root / "audits").glob("*/*/audit.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record["status"] != "error" or record.get("error", {}).get("type") != "ValueError":
            continue
        trace_path = path.with_name("trace.jsonl")
        # Iterate physical JSONL lines: PDF text can contain Unicode separators
        # that str.splitlines() would incorrectly split inside JSON strings.
        with trace_path.open(encoding="utf-8") as stream:
            events = [json.loads(line) for line in stream]
        response = next(row for row in reversed(events) if row["event"] == "model_response")
        texts = [content["text"] for item in response["response"]["output"]
                 for content in item.get("content", []) if content.get("type") == "output_text"]
        audit = json.loads("".join(texts))
        jsonschema.validate(audit, AUDIT_SCHEMA)
        result_path = root / path.parent.parent.name / path.parent.name / "result.json"
        source = json.loads(result_path.read_text(encoding="utf-8"))
        normalized, operation = normalize_indices(audit, len(source["review"]["observations"]))
        if operation is None:
            continue
        original_path = path.with_name("audit-initial-error.json")
        if original_path.exists():
            raise ValueError(f"Initial error already preserved at {original_path}")
        original_path.write_bytes(path.read_bytes())
        record.update(status="ok", audit=normalized, normalization=operation,
                      initial_status="error", repair_source_model_response_seq=response["seq"])
        record.pop("error", None)
        repair = {"seq": events[-1]["seq"] + 1, "timestamp": datetime.now(timezone.utc).isoformat(),
                  "event": "audit_repair", "operation": operation,
                  "source_model_response_seq": response["seq"], "record": record,
                  "note": "No new model call. Verdicts/explanations unchanged; original error result retained."}
        with trace_path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(repair, ensure_ascii=False) + "\n")
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        repaired.append(f"{record['variant']} {record['task_id']}")
    print(json.dumps({"repaired_without_model_calls": repaired}))


if __name__ == "__main__":
    main()
