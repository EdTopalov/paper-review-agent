"""Stop registered benchmark launcher trees at an aware ISO timestamp.

Windows only. Process creation timestamps and command-line hashes prevent PID
reuse from targeting another process. No model APIs or project source are used.
"""

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import time


REPOSITORY = Path(__file__).resolve().parents[1]
LAUNCHER = "run_existing_benchmark.py"


def aware_deadline(value):
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use an ISO timestamp with an explicit UTC offset") from exc
    if parsed.utcoffset() is None:
        raise argparse.ArgumentTypeError("The deadline must include a UTC offset")
    return parsed.astimezone(timezone.utc)


def positive_pid(value):
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("PIDs must be positive integers")
    return parsed


def journal(path, event, **fields):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **fields}
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def query_processes(pids):
    condition = " OR ".join(f"ProcessId={int(pid)}" for pid in pids)
    command = (
        f"$rows=@(Get-CimInstance Win32_Process -Filter '{condition}' -ErrorAction Stop | "
        "ForEach-Object { [pscustomobject]@{pid=[int]$_.ProcessId; "
        "created_at=$_.CreationDate.ToUniversalTime().ToString('o'); "
        "command_line=[string]$_.CommandLine} }); "
        "ConvertTo-Json -InputObject $rows -Compress"
    )
    result = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", command],
                            capture_output=True, text=True, check=True, timeout=15)
    rows = json.loads(result.stdout)
    return {row["pid"]: row for row in rows}


def launcher_matches(process, repository):
    command = process.get("command_line", "").replace("/", "\\").casefold()
    root = str(Path(repository).resolve()).replace("/", "\\").rstrip("\\").casefold()
    launcher = re.search(r'(?:^|[\\\s"\'])' + re.escape(LAUNCHER) + r'(?:$|[\s"\'])', command)
    return bool(process.get("created_at") and root + "\\" in command and launcher)


def identity(process):
    return {"created_at": process["created_at"],
            "command_sha256": sha256(process["command_line"].encode("utf-8")).hexdigest()}


def watch(deadline, pids, out, *, repository=REPOSITORY, dry_run=False):
    if deadline.utcoffset() is None:
        raise ValueError("The deadline must include a UTC offset")
    pids = list(dict.fromkeys(pids))
    if not pids or any(type(pid) is not int or pid < 1 for pid in pids):
        raise ValueError("Register positive integer launcher PIDs")
    journal(out, "watchdog_started", deadline=deadline.isoformat(), pids=pids, dry_run=dry_run)
    current = query_processes(pids)
    registered = {}
    refused = False
    for pid in pids:
        process = current.get(pid)
        if process is None:
            journal(out, "natural_finished", pid=pid, detail="not_running_at_registration")
        elif not launcher_matches(process, repository):
            journal(out, "registration_refused", pid=pid, detail="repository_or_launcher_mismatch")
            refused = True
        else:
            registered[pid] = identity(process)
            journal(out, "registered", pid=pid, launcher=LAUNCHER, **registered[pid])
    if refused:
        return 2
    if dry_run:
        journal(out, "dry_run_complete", registered=list(registered))
        return 0
    failed = False
    while registered:
        try:
            current = query_processes(registered)
        except Exception as exc:
            journal(out, "query_failed", error_type=type(exc).__name__)
            if datetime.now(timezone.utc) >= deadline:
                journal(out, "cutoff_unverified", pids=list(registered))
                return 2
            time.sleep(min(5, max(0, (deadline - datetime.now(timezone.utc)).total_seconds())))
            continue
        for pid, original in list(registered.items()):
            process = current.get(pid)
            if process is None:
                journal(out, "natural_finished", pid=pid)
                del registered[pid]
            elif not launcher_matches(process, repository) or identity(process) != original:
                journal(out, "original_process_finished", pid=pid, detail="pid_identity_changed; replacement_not_stopped")
                del registered[pid]
            elif datetime.now(timezone.utc) >= deadline:
                # Recheck this PID immediately before stopping it, including
                # when another registered process tree took time to terminate.
                live = query_processes([pid]).get(pid)
                if live is None or not launcher_matches(live, repository) or identity(live) != original:
                    journal(out, "original_process_finished", pid=pid, detail="finished_or_replaced_before_cutoff; replacement_not_stopped")
                    del registered[pid]
                    continue
                journal(out, "cutoff_requested", pid=pid, **original)
                try:
                    result = subprocess.run(["taskkill.exe", "/PID", str(pid), "/T", "/F"],
                                            capture_output=True, text=True, timeout=15)
                    if result.returncode == 0:
                        journal(out, "stopped", pid=pid, returncode=0)
                    else:
                        remaining = query_processes([pid]).get(pid)
                        if remaining is None or identity(remaining) != original:
                            journal(out, "natural_finished", pid=pid, detail="finished_during_cutoff")
                        else:
                            journal(out, "stop_failed", pid=pid, returncode=result.returncode)
                            failed = True
                except Exception as exc:
                    journal(out, "stop_failed", pid=pid, error_type=type(exc).__name__)
                    failed = True
                del registered[pid]
        if registered:
            time.sleep(min(5, max(0, (deadline - datetime.now(timezone.utc)).total_seconds())))
    journal(out, "watchdog_finished", status="error" if failed else "complete")
    return 2 if failed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deadline", required=True, type=aware_deadline)
    parser.add_argument("--pid", required=True, action="append", type=positive_pid)
    parser.add_argument("--out", required=True, type=Path, help="Append-only JSONL watchdog journal")
    parser.add_argument("--dry-run", action="store_true", help="Verify identities and exit without waiting or stopping processes")
    args = parser.parse_args()
    try:
        return watch(args.deadline, args.pid, args.out, dry_run=args.dry_run)
    except Exception as exc:
        journal(args.out, "watchdog_failed", error_type=type(exc).__name__)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
