"""Unblind the retest and add up the totals. From the repository root:
python3 evidence/skill-fix-retest/analyse.py evidence/skill-fix-retest
"""
import json
import sys
from pathlib import Path

folder = Path(sys.argv[1])
mapping = json.loads((folder / "mapping.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
names = ["shape", "checklist", "no_title_guessing", "no_upgrading", "known_concern_used", "message"]

for arm in ("current", "edited"):
    brief = [c for c, m in mapping.items() if m["arm"] == arm and m["case"] != "cosima"]
    stop = [c for c, m in mapping.items() if m["arm"] == arm and m["case"] == "cosima"]
    parts = []
    for i, n in enumerate(names):
        vals = [scores[c][i] for c in brief if scores[c][i] is not None]
        parts.append(f"{n}={sum(vals)}/{len(vals)}")
    parts.append(f"cosima_stop={sum(scores[c][0] for c in stop)}/{len(stop)}")
    print(arm, " ".join(parts))
    for model in ("opus", "haiku"):
        b = [c for c in brief if mapping[c]["model"] == model]
        print(f"  {model}: shape={sum(scores[c][0] for c in b)}/{len(b)} checklist={sum(scores[c][1] for c in b)}/{len(b)}")
