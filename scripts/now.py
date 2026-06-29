#!/usr/bin/env python3
"""now.py — print the current ISO-8601 UTC timestamp for a `[retrieved … Z]` source line. Stdlib only, portable.

    python ${CLAUDE_SKILL_DIR}/scripts/now.py   ->   2026-06-29T12:34:56Z

Stamp each source at the moment you retrieve it instead of hand-typing the time (hand-typing invites fabrication and
drift). The format matches exactly what scripts/compliance_check.py accepts as a LAW 0 retrieval timestamp.
"""
from datetime import datetime, timezone


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


if __name__ == "__main__":
    print(now_iso())
