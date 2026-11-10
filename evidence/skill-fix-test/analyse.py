"""Unblind the skill-fix test and add up the totals. From the repository root:
python3 evidence/skill-fix-test/analyse.py evidence/skill-fix-test
"""
import json
import sys
from pathlib import Path

folder = Path(sys.argv[1])
mapping = json.loads((folder / "mapping.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
names = ["A", "B", "C", "shape", "no_title_guessing", "no_upgrading", "known_concern_used"]

for arm in ("current", "edited"):
    brief = [c for c, m in mapping.items() if m["arm"] == arm and m["case"] != "sam"]
    sam = [c for c, m in mapping.items() if m["arm"] == arm and m["case"] == "sam"]
    parts = []
    for i, n in enumerate(names):
        vals = [scores[c][i] for c in brief if scores[c][i] is not None]
        parts.append(f"{n}={sum(vals)}/{len(vals)}")
    parts.append(f"sam_stop={sum(scores[c][0] for c in sam)}/{len(sam)}")
    print(arm, " ".join(parts))
    for model in ("opus", "haiku"):
        b = [c for c in brief if mapping[c]["model"] == model]
        print(f"  {model}: shape={sum(scores[c][3] for c in b)}/{len(b)} B={sum(scores[c][1] for c in b)}/{len(b)}")
