#!/usr/bin/env python3
"""Bound one local, non-daemonizing command; never stop unrelated processes."""

import argparse
import json
import math
import os
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone


def utc_deadline(value):
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use an ISO-8601 deadline with a timezone") from exc
    if parsed.tzinfo is None:
        raise argparse.ArgumentTypeError("The deadline must include a timezone")
    return parsed.astimezone(timezone.utc)


def nonnegative(value):
    try:
        number = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use a finite, nonnegative number") from exc
    if not math.isfinite(number) or number < 0:
        raise argparse.ArgumentTypeError("Use a finite, nonnegative number")
    return number


def emit(state, stream=sys.stdout, **fields):
    print(json.dumps({"state": state, "at": datetime.now(timezone.utc).isoformat(),
                      **fields}), file=stream, flush=True)


def group_exists(proc):
    try:
        os.killpg(proc.pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        # macOS can report EPERM for an exited, not-yet-reaped group leader.
        proc.poll()
        try:
            os.killpg(proc.pid, 0)
            return True
        except ProcessLookupError:
            return False


def signal_group(proc, sig):
    try:
        os.killpg(proc.pid, sig)
    except ProcessLookupError:
        pass
    except PermissionError:
        proc.poll()
        try:
            os.killpg(proc.pid, sig)
        except ProcessLookupError:
            pass


def stop_group(proc, grace):
    """Only the process group created by this invocation is eligible."""
    signal_group(proc, signal.SIGTERM)
    end = time.monotonic() + max(0, grace)
    while time.monotonic() < end:
        proc.poll()
        if not group_exists(proc):
            break
        time.sleep(min(0.05, max(0, end - time.monotonic())))
    if group_exists(proc):
        signal_group(proc, signal.SIGKILL)
    proc.wait()


def run(args, work_deadline, seconds):
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        emit("start_error", sys.stderr, reason="No command supplied")
        return 125
    if os.name != "posix":
        emit("guard_error", sys.stderr, reason="Process-group isolation requires POSIX")
        return 125
    budget = min(seconds, args.max_seconds) if args.max_seconds is not None else seconds
    if budget <= 0:
        emit("expired", sys.stderr)
        return 124
    # Reserve termination time inside the budget, never beyond the work deadline.
    grace = min(args.grace_seconds, budget / 4)
    mono_end = time.monotonic() + budget
    wall_end = min(work_deadline, time.time() + budget)
    try:
        proc = subprocess.Popen(command, start_new_session=True)
    except OSError as exc:
        emit("start_error", sys.stderr, error_type=type(exc).__name__)
        return 125
    emit("started", sys.stderr, pid=proc.pid, budget_seconds=round(budget, 3))

    def interrupted(_signum, _frame):
        raise KeyboardInterrupt

    previous_term = signal.signal(signal.SIGTERM, interrupted)
    previous_int = signal.signal(signal.SIGINT, interrupted)
    timed_out = False
    was_interrupted = False
    cleanup_error = None
    exitcode = None
    try:
        while True:
            exitcode = proc.poll()
            if exitcode is not None:
                break
            remaining = min(mono_end - time.monotonic(), wall_end - time.time())
            if remaining <= grace:
                timed_out = True
                break
            time.sleep(min(0.1, remaining - grace))
    except KeyboardInterrupt:
        was_interrupted = True
    finally:
        # Ignore repeated interrupts only during bounded cleanup of our own group.
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        remaining = min(mono_end - time.monotonic(), wall_end - time.time())
        try:
            stop_group(proc, min(grace, max(0, remaining)))
        except OSError as exc:
            cleanup_error = type(exc).__name__
        finally:
            signal.signal(signal.SIGTERM, previous_term)
            signal.signal(signal.SIGINT, previous_int)
    if cleanup_error:
        emit("guard_error", sys.stderr, error_type=cleanup_error)
        return 125
    if was_interrupted:
        emit("interrupted", sys.stderr)
        return 130
    if timed_out:
        emit("timed_out", sys.stderr)
        return 124
    emit("completed", sys.stderr, returncode=exitcode)
    return exitcode if exitcode >= 0 else 128 - exitcode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="mode", required=True)
    for name in ("status", "run"):
        sub = subs.add_parser(name)
        sub.add_argument("--deadline", required=True, type=utc_deadline)
        sub.add_argument("--reserve-seconds", type=nonnegative, default=0)
        if name == "run":
            sub.add_argument("--max-seconds", type=nonnegative)
            sub.add_argument("--grace-seconds", type=nonnegative, default=2)
            sub.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    work_deadline = args.deadline.timestamp() - args.reserve_seconds
    seconds = work_deadline - time.time()
    if args.mode == "status":
        emit("open" if seconds > 0 else "expired",
             deadline_utc=args.deadline.isoformat(),
             reserve_seconds=args.reserve_seconds,
             work_seconds_remaining=round(max(0, seconds), 3))
        return 0 if seconds > 0 else 124
    return run(args, work_deadline, seconds)


if __name__ == "__main__":
    sys.exit(main())
