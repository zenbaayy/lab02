# CSE325-2026-L02-M4RB-T1
"""BEFORE version: deliberately messy stand-in for 'cold' code.
Replace with YOUR OWN old code (40+ lines) for the real submission."""

QUALITY_BASELINE = "before"


def run(rows, verbose, flag, mode, extra, path):
    d = {}
    for r in rows:
        p = r.split(",")
        if len(p) < 2:
            continue
        name = p[0].strip()
        marks = [int(x) for x in p[1:]]
        d[name] = marks
    out = []
    for name in d:
        m = d[name]
        avg = sum(m) / len(m)
        if avg >= 85:
            g = "A"
        elif avg >= 70:
            g = "B"
        elif avg >= 55:
            g = "C"
        else:
            g = "F"
        out.append((name, avg, g))
    for name, avg, g in out:
        if avg >= 85:
            lg = "A"
        elif avg >= 70:
            lg = "B"
        elif avg >= 55:
            lg = "C"
        else:
            lg = "F"
        print(f"{name}: {avg:.1f} ({lg})")
    passed = 0
    for name, avg, g in out:
        if avg >= 85:
            x = "A"
        elif avg >= 70:
            x = "B"
        elif avg >= 55:
            x = "C"
        else:
            x = "F"
        if x != "F":
            passed += 1
    print(f"Passed: {passed}/{len(out)}")
