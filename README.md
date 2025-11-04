# FlowLex

**FlowLex** is a compact, human-readable format for encoding meaning.  
It merges *structured text* (via the [Copper](https://github.com/yourname/copper) syntax) with *machine-learnable vectors* so both people and AIs can share the same vocabulary.

---

## What It Is

FlowLex files (`.copr`) are semantic dictionaries that describe:

| Layer | Purpose |
|-------|----------|
| **Code ID** | Stable anchor used by software and AIs. |
| **Human Word** | The readable term or phrase. |
| **Accessibility Fields** | `alt_text`, `sign_code`, and `speech_hint` for inclusive interfaces. |
| **Vector List** | Numeric embedding representing meaning in multidimensional space. |

Each entry lives on one line:

B1: run : to move quickly on foot : ASL_RUN : rhymes with sun = 0.12, -0.04, 0.33, 0.21, -0.10, 0.02, 0.18, -0.07

yaml
Copy code

Everything before `=` is for humans.  
Everything after `=` belongs to the machine.

---

## Core Design Goals

* **Readability First** – edit in any text editor without fear.  
* **Accessibility Built-In** – assistive metadata travels with every word.  
* **AI-Ready** – vectors inline with definitions remove alignment headaches.  
* **Unicode-Native** – punctuation, emoji, and symbols work out of the box.  
* **Expandable IDs** – variable-length codes (`B1`, `B2`, …) keep files lean.

---

## Repository Layout

/spec/FlowLex_Spec.copr # formal definition of the format
/examples/FlowLex_English_Sample.copr
/tools/parser.py # minimal reference parser / validator

pgsql
Copy code

---

## Quick Parse Example (Python)

```python
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
Building on FlowLex
Future directions:

Language Packs – add new .copr dictionaries (English, Python, Spanish, etc.).

Visualizer – render documents as color-coded “semantic spectra.”

Accessibility Modules – screen-reader, haptic, and sign-language output.

Consensus Embeddings – share averaged vector sets across models.

License
All specification and sample data are released under CC-BY-SA-4.0.
Code examples use the MIT License.

Author
Don Sauber – 2025
FlowLex is part of the broader FlowOS ecosystem.
