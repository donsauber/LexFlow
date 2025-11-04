# FlowLex

**FlowLex** is a human-readable, AI-interpretable format for encoding *meaning itself*.

It combines the clarity of a dictionary, the structure of a programming language, and the precision of an embedding model into one unified file type.  
Every FlowLex file (`.copr`) describes how ideas, words, or code structures connect to one another through both text and vectors.

FlowLex is part of the **FlowOS** ecosystem, designed by **Don Sauber**.

---

## 1. What FlowLex Is

At its simplest, a FlowLex file is a list of concepts.  
Each line holds:

code : word : alt_text : sign_code : speech_hint = vector_list

Example:

B1: run : to move quickly on foot : ASL_RUN : rhymes with sun = 0.12, -0.04, 0.33, 0.21, -0.10, 0.02, 0.18, -0.07

- Everything before `=` is **for humans and accessibility**.  
- Everything after `=` is **for AIs and computation**.

---

## 2. Why FlowLex Exists

Today, language and data live in two incompatible worlds.  
Text is readable but inefficient; vectors are powerful but opaque.  
FlowLex fuses them into a single, transparent layer that both people and machines can understand.

**Problems it addresses:**

| Problem | FlowLex Solution |
|----------|------------------|
| Redundant text storage | Single semantic entry replaces dozens of word forms |
| Unaligned embeddings | Vectors stored beside their meanings—no lookup errors |
| Accessibility gaps | Built-in fields for alt text, sign codes, and speech hints |
| Punctuation duplication | Unicode handled natively; no extra tokens required |
| File bloat | Variable-length codes keep data compact |
| Fragmented parsing | One universal Copper-based structure for all languages |

---

## 3. Design Principles

1. **Readability First**  
   Anyone can open and edit a FlowLex file in plain text.  
   No special IDE, no hidden binary data.

2. **Machine-Parsable by Design**  
   Each line follows one strict pattern—parsers stay tiny and robust.

3. **Accessibility as Core Infrastructure**  
   Alternative text, sign-language references, and pronunciation cues are not add-ons—they’re part of the data model.

4. **Universal Scope**  
   FlowLex doesn’t just describe human language.  
   It can represent programming syntax, scientific notation, or abstract symbols—any system where meaning has structure.

5. **Inline Vectors**  
   Embedding vectors live beside definitions, eliminating alignment errors and allowing immediate AI ingestion.

6. **Context-Scoped Headers**  
   Each file defines its language, version, and vector schema once at the top; all entries inherit that context.

---

## 4. Potential Uses

### Language Engineering
- Create open, shared semantic dictionaries for AI training.
- Compress multilingual corpora by using concept IDs instead of full words.
- Build explainable embeddings where every coordinate has a readable anchor.

### Accessibility Technology
- Enable screen readers, sign-language interfaces, and text-to-speech to share one common vocabulary layer.
- Support high-contrast color coding, haptic feedback, and audio cues for each entry.

### Programming and Data Systems
- Treat programming keywords, libraries, or templates as FlowLex units.
- Allow AI agents to “read” code and documentation in the same format.
- Use vectors to find semantically similar functions or APIs.

### Visualization
- Map meaning to color or motion, creating semantic heat maps of text and code.
- Identify patterns of tone, rhythm, or conceptual density visually.

### Education and Communication
- Simplify reading or translation for language learners.
- Build bilingual FlowLex sets with one-to-one concept mapping.
- Use FlowLex as an intermediate layer for natural-language programming.

---

## 5. Future Benefits

**Cross-AI Semantic Alignment**  
Different AI models can share FlowLex bundles to synchronize meaning, making collaboration and transfer learning trivial.

**Knowledge Portability**  
Vectors and definitions can be version-controlled like code—meaning becomes reproducible.

**Semantic Compression**  
Documents transmitted as FlowLex references become drastically smaller while retaining clarity.

**Transparency and Trust**  
Because every number lives beside its definition, FlowLex eliminates “black box” embeddings.

**Universal Accessibility**  
Every FlowLex entry can be expressed through sight, sound, text, or touch—bridging human and machine communication seamlessly.

---

## 6. Repository Layout

/spec/FlowLex_Spec.copr   # Core specification
/examples/FlowLex_English_Sample.copr
/tools/parser.py     # Minimal parser / validator
/LICENSE # CC BY-SA 4.0 + MIT for code

---

## 7. Quick Parse Example (Python)

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
    print(code, word, vector[:3])
```
---

## 8. Contributing
FlowLex is designed for open collaboration.
You can contribute by:

Proposing new spec sections in /spec/. 
Adding language or code-domain dictionaries in /examples/. 
Providing accessibility enhancements. 
Sharing averaged or consensus vector sets. 
Building visualization or editing tools.

All contributions remain open and attributed under the repository license.

---

## 9. License
Text and Data: CC BY-SA 4.0
Code Examples: MIT License
© 2025 Don Sauber

FlowLex is the beginning of a universal semantic layer —
a bridge where words, code, and meaning share the same language.
