"""Append-only, flushed structured events. Never pass credentials to this logger."""

from datetime import datetime, timezone
import json
from pathlib import Path
import time


class Trace:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.file = Path(path).open("x", encoding="utf-8")
        self.started = time.perf_counter()
        self.seq = 0

    def write(self, event, **payload):
        self.seq += 1
        row = {"seq": self.seq, "timestamp": datetime.now(timezone.utc).isoformat(),
               "elapsed_seconds": round(time.perf_counter()-self.started, 6),
               "event": event, **payload}
        self.file.write(json.dumps(row, ensure_ascii=False) + "\n")
        self.file.flush()

    def close(self):
        self.file.close()
