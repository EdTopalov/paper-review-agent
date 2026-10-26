"""Append-only, flushed structured events. Never pass credentials to this logger."""

from datetime import datetime, timezone
from copy import deepcopy
import json
from pathlib import Path
import time


# Keep model output, usage, and failure diagnostics; discard echoed API settings.
RESPONSE_FIELDS = {"id", "model", "service_tier", "status", "output", "output_text", "usage", "error", "incomplete_details"}


def read_events(path):
    """Expand changed settings and input prefixes into complete model requests."""
    previous = []
    previous_request = {}
    events = []
    with Path(path).open(encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["event"] == "model_request":
                request = {**previous_request, **row["request"]} if row.get("request_delta") else row["request"]
                for key in row.get("removed_request_fields", []):
                    request.pop(key, None)
                prefix = row.get("input_prefix", 0)
                if not 0 <= prefix <= len(previous):
                    raise ValueError("Invalid conversation prefix in trace")
                request["input"] = previous[:prefix] + request["input"]
                previous = request["input"]
                previous_request = request
                row["request"] = request
            events.append(row)
    return events


def read_result(path, *, audit=False):
    endings = ("audit_end", "audit_repair") if audit else ("run_end",)
    key = "record" if audit else "result"
    return next((row[key] for row in reversed(read_events(path)) if row["event"] in endings), None)


class Trace:
    def __init__(self, path, *, append=False):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        events = read_events(path) if append else []
        self.file = Path(path).open("a" if append else "x", encoding="utf-8", newline="\n")
        elapsed = (datetime.now(timezone.utc) - datetime.fromisoformat(events[0]["timestamp"])).total_seconds() if events else 0
        self.started = time.perf_counter() - elapsed
        self.seq = events[-1]["seq"] if events else 0
        self.previous_input = []
        self.previous_request = {}

    def write(self, event, **payload):
        if event == "model_request":
            full_request = deepcopy(payload["request"])
            inputs = full_request["input"]
            prefix = len(self.previous_input) if inputs[:len(self.previous_input)] == self.previous_input else 0
            request = {key: value for key, value in full_request.items()
                       if key == "input" or key not in self.previous_request or self.previous_request[key] != value}
            request["input"] = inputs[prefix:]
            removed = sorted(self.previous_request.keys() - full_request.keys())
            payload = {**payload, "request": request, "input_prefix": prefix,
                       "request_delta": bool(self.previous_request)}
            if removed:
                payload["removed_request_fields"] = removed
            self.previous_input = inputs
            self.previous_request = full_request
        elif event == "model_response":
            payload = {**payload, "response": {key: value for key, value in payload["response"].items()
                                               if key in RESPONSE_FIELDS}}
        self.seq += 1
        row = {"seq": self.seq, "timestamp": datetime.now(timezone.utc).isoformat(),
               "elapsed_seconds": round(time.perf_counter()-self.started, 6),
               "event": event, **payload}
        self.file.write(json.dumps(row, ensure_ascii=False) + "\n")
        self.file.flush()

    def close(self):
        self.file.close()
