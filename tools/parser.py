from pathlib import Path
import numpy as np

for line in Path("examples/FlowLex_English_Sample.copr").read_text().splitlines():
    if "=" not in line or line.strip().startswith("#"):
        continue
    left, vec = line.split("=", 1)
    fields = [f.strip() for f in left.split(":", 4)]
    code, word, alt, sign, speech = (fields + [None]*5)[:5]
    vector = np.fromstring(vec, sep=",")
    print(code, word, vector[:3])  # preview first 3 dims
