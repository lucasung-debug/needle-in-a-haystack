#!/usr/bin/env python3
"""Validate the research.md compliance block in a research output.

Usage:
    python3 scripts/validate_compliance.py <output-file>
    cat output.txt | python3 scripts/validate_compliance.py

Checks that the output contains the mandatory compliance block defined in
research.md (Enforcement section):

    [C]:    ... [PASS|FAIL|N/A]
    [L1]:   ... [PASS|FAIL|N/A]
    [L2]:   ... [PASS|FAIL|N/A]   (N/A allowed when no vault is configured)
    [L3]:   ... [PASS|FAIL|N/A]
    [L4]:   ... [PASS|FAIL|N/A]
    [COST]: Paid sources used? [YES|NO]  (if YES, consent recorded [YES|NO])
    [FINAL]: VALID | INVALID

Failure conditions (exit code 1):
    - any required line is missing
    - a gate line has no recognizable PASS/FAIL/N/A verdict
    - [COST] reports paid sources used without recorded consent
    - [FINAL] is VALID while any gate line is FAIL or paid use lacks consent
    - [FINAL] is INVALID (the output must be redone before shipping)

Exit code 0 means the block is well-formed and internally consistent.
Only Python 3 standard library is used.
"""

import re
import sys

GATE_TAGS = ["C", "L1", "L2", "L3", "L4"]

VERDICT_RE = re.compile(r"\[?\b(PASS|FAIL|N/A)\b\]?\s*$")
COST_RE = re.compile(
    r"\[COST\]:.*?\[?\b(YES|NO)\b\]?", re.IGNORECASE
)
CONSENT_RE = re.compile(
    r"consent[^\[]*\[?\b(YES|NO)\b\]?", re.IGNORECASE
)
FINAL_RE = re.compile(r"\[FINAL\]:\s*(VALID|INVALID)\b", re.IGNORECASE)


def find_line(lines, tag):
    prefix = f"[{tag}]:"
    for line in lines:
        if line.strip().startswith(prefix):
            return line.strip()
    return None


def validate(text):
    """Return a list of error strings; empty list means the block is valid."""
    errors = []
    lines = text.splitlines()

    verdicts = {}
    for tag in GATE_TAGS:
        line = find_line(lines, tag)
        if line is None:
            errors.append(f"missing line: [{tag}]:")
            continue
        m = VERDICT_RE.search(line)
        if not m:
            errors.append(f"[{tag}] line has no PASS/FAIL/N/A verdict: {line}")
            continue
        verdicts[tag] = m.group(1)

    cost_line = find_line(lines, "COST")
    paid_without_consent = False
    if cost_line is None:
        errors.append("missing line: [COST]:")
    else:
        m = COST_RE.search(cost_line)
        if not m:
            errors.append(f"[COST] line has no YES/NO answer: {cost_line}")
        elif m.group(1).upper() == "YES":
            consent = CONSENT_RE.search(cost_line)
            if not consent or consent.group(1).upper() != "YES":
                paid_without_consent = True
                errors.append(
                    "[COST] reports paid sources used without recorded consent"
                )

    final_line = find_line(lines, "FINAL")
    if final_line is None:
        errors.append("missing line: [FINAL]:")
    else:
        m = FINAL_RE.search(final_line)
        if not m:
            errors.append(f"[FINAL] must state VALID or INVALID: {final_line}")
        else:
            final = m.group(1).upper()
            failed_gates = [t for t, v in verdicts.items() if v == "FAIL"]
            if final == "VALID" and failed_gates:
                errors.append(
                    "[FINAL] is VALID but these gates are FAIL: "
                    + ", ".join(failed_gates)
                )
            if final == "VALID" and paid_without_consent:
                errors.append(
                    "[FINAL] is VALID but paid use lacks recorded consent"
                )
            if final == "INVALID":
                errors.append(
                    "[FINAL] is INVALID: the output must be redone before shipping"
                )

    return errors


def main(argv):
    if len(argv) > 1:
        with open(argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    errors = validate(text)
    if errors:
        print("compliance block: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("compliance block: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
