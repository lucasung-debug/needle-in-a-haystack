#!/usr/bin/env python3
"""runner.py — frozen regression gate for the compliance validator.

Runs scripts/compliance_check.py against every fixture under eval/fixtures/ and
compares its exit code to eval/expected.json. The gate holds only when the
validator catches EVERY seeded defect (detection == 1.0) and flags NONE of the
honest outputs (false-positive rate == 0) — the seedance/skill-enhancer standard.

This is the skill eating its own dog food at the eval altitude: the `good-negative`
fixture proves the NIAH signature — an honest "NEEDLE NOT FOUND" passes, while a
fabricated needle (`bad-fabricated`) is caught.

Authority: this file and the fixtures are the frozen judge — never edit them to make
a failing validator pass. To raise the bar, ADD an adversarial fixture + its expected
exit. Only scripts/compliance_check.py (the target) may be tuned.

  python ${CLAUDE_SKILL_DIR}/eval/runner.py        # exit 0 = gate holds
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKER = HERE.parent / "scripts" / "compliance_check.py"
FIXTURES = HERE / "fixtures"
EXPECTED = HERE / "expected.json"


def main():
    expected = {k: v for k, v in json.loads(EXPECTED.read_text(encoding="utf-8")).items()
                if not k.startswith("_")}

    rows = []
    for name, want in sorted(expected.items()):
        report = FIXTURES / name / "report.md"
        if not report.exists():
            report = FIXTURES / name / "report.html"   # HTML report fixtures (self-containment gate)
        if not report.exists():
            print(f"MISSING fixture: {FIXTURES / name}/report.{{md,html}}", file=sys.stderr)
            sys.exit(2)
        proc = subprocess.run(
            [sys.executable, str(CHECKER), str(report)],
            capture_output=True, text=True,
        )
        got = proc.returncode
        rows.append((name, want, got, got == want))

    bad = [r for r in rows if r[1] == 1]            # seeded-defect fixtures
    good = [r for r in rows if r[1] == 0]           # honest fixtures
    detected = sum(1 for r in bad if r[3])
    false_pos = sum(1 for r in good if not r[3])
    detection = detected / len(bad) if bad else 1.0
    fp_rate = false_pos / len(good) if good else 0.0

    width = max(len(r[0]) for r in rows)
    print("fixture".ljust(width), "expect", "got", "ok")
    for name, want, got, ok in rows:
        print(name.ljust(width), str(want).center(6), str(got).center(3), "✓" if ok else "✗")
    print()
    print(f"detection: {detection:.2f}  ({detected}/{len(bad)} seeded defects caught)")
    print(f"false_positive_rate: {fp_rate:.2f}  ({false_pos}/{len(good)} honest outputs wrongly flagged)")

    gate = detection == 1.0 and fp_rate == 0.0
    print(f"eval_pass: {1 if gate else 0}")
    sys.exit(0 if gate else 1)


if __name__ == "__main__":
    main()
