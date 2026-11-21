# SCHEMA.md — JSONL schema for the Japanese seed set

**Version:** 1.0 (draft)
**Applies to:** `data/ja_adversarial_seed.jsonl`
**Status:** personal R&D methodology prototype, not a client production system

## 1. File format

- UTF-8, no BOM.
- One JSON object per line. No blank lines, no comments, no trailing commas.
- LF line endings. The final line ends with a newline.
- One object per item; `id` is unique across the file.
- Field names are fixed and case-sensitive. Unknown fields are an error, not an extension point.

## 2. Fields

| Field | Type | Required | Constraints | Meaning |
|---|---|---|---|---|
| `id` | string | yes | `^JA-[0-9]{3}$`; unique; stable across versions | Item identifier. Never reused for a different item. |
| `type` | string | yes | one of the six codes below | The primary failure mode the item is designed to expose. |
| `prompt` | string | yes | non-empty; Japanese | The exact user-facing task. Preserve punctuation and line breaks. No rubric text, no hidden instructions. |
| `reference` | string | yes | non-empty; Japanese | The gold judgment. States the facts and the decision; it is not a required verbatim answer. |
| `judgment_rubric_hits` | array of strings | yes | 2–5 entries; each `"D<n>: <criterion>"`, where `n` is 1–5 | The decisive checks for this item. These are must-haves, not a scoring formula. |
| `notes` | string | yes | may be empty; English or Japanese; no PII | Provenance, designed trap, or known limitation. Never contains a client name, an employer name, or a real person's data. |

### `type` enum

| Code | Japanese label | Use for |
|---|---|---|
| `ambiguity` | 曖昧性 | Two-way readings, relative time, zero anaphora, soft refusals |
| `cultural_context` | 文化文脈 | Customs, seasonal mail, refusal etiquette, honorific vocabulary |
| `instruction_resolution` | 指示消解 | Competing constraints, register rules, length vs. information |
| `keigo_register` | 敬語級差 | Double keigo, respectful/humble swapping, `させていただく` overuse |
| `numerical_consistency` | 数値整合 | Tax, percentages, break-even, date arithmetic |
| `negation_scope` | 否定スコープ | Partial negation, `P以外` entailment |

### `judgment_rubric_hits` convention

The prefix names the dimension in `RUBRIC-1-5.md`:

- `D1` — instruction compliance
- `D2` — factual and numerical accuracy
- `D3` — language quality and register
- `D4` — ambiguity and missing-information handling
- `D5` — explanation and justification

A hit must be checkable against the response. "Good tone" is not a hit; "uses `伺います`, not `伺わせていただきます`" is.

## 3. Invariants

1. `id` values are unique and never repurposed.
2. `type` is one of the six codes; there is no `other`.
3. `prompt` and `reference` are non-empty and in Japanese.
4. `judgment_rubric_hits` has 2–5 entries and every entry starts with `D1:`–`D5:`.
5. `notes` contains no personal data, client material, or employer name.
6. The line is valid JSON on its own; no reliance on the previous line.
7. The file contains exactly 20 lines in version 1.0.

## 4. Example lines

```jsonl
{"id":"JA-001","type":"ambiguity","prompt":"来週の打ち合わせを、火曜か水曜の午後でお願いしたいです。所要は1時間です。先方には「来週前半」とだけ伝えてあります。先方への返信メールの下書きを作ってください。","reference":"「来週前半」の範囲を保ったまま、日時を確定しない返信文を作る。本文では「来週の前半で調整中」とし、火曜・水曜の具体的な日付を書かない。依頼者には、(1) 火曜と水曜のどちらを優先するか、(2) 週の起算日（月曜始まりか日曜始まりか）と「来週」が指す具体的な週、を確認する。カレンダー情報がないため、日付を補って書かない。","judgment_rubric_hits":["D4: 曖昧さを2点とも認識し、断定しない","D1: 下書きに未確定の日時を書かない","D3: 自然なビジネス敬語"],"notes":"Designed trap: relative time with no calendar anchor; original seed item."}
{"id":"JA-003","type":"keigo_register","prompt":"取引先へのメールで使う文です。敬語の誤りを指摘し、自然な文に直してください。\n\n「弊社の田中が、明日そちらに伺わせていただきます。」","reference":"誤りは「伺わせていただきます」。「伺う」がすでに謙譲語であるため、「させていただく」を重ねると二重敬語になる。修正例は「弊社の田中が、明日そちらへ伺います。」。「そちらに」を「そちらへ」とするのは任意だが、より自然。自社の者に敬称を付けない点も維持する。","judgment_rubric_hits":["D3: 二重敬語を特定し、謙譲語＋させていただくの重複を説明","D1: 修正後の文に誤りを残さない","D2: 自社の者に「様」を付けない"],"notes":"Designed trap: double keigo in a common business phrase; original seed item."}
```

## 5. Validation

The following check is intentionally dependency-free. Run it from the repository root before publishing or after any edit.

```python
import json
import re
import sys

PATH = "data/ja_adversarial_seed.jsonl"
TYPES = {
    "ambiguity", "cultural_context", "instruction_resolution",
    "keigo_register", "numerical_consistency", "negation_scope",
}
FIELDS = {"id", "type", "prompt", "reference", "judgment_rubric_hits", "notes"}
ID_RE = re.compile(r"^JA-[0-9]{3}$")

seen = set()
with open(PATH, encoding="utf-8", newline="") as fh:
    for lineno, line in enumerate(fh, 1):
        if not line.strip():
            sys.exit(f"line {lineno}: blank line")
        row = json.loads(line)
        if not isinstance(row, dict):
            sys.exit(f"line {lineno}: expected a JSON object")
        if set(row) != FIELDS:
            sys.exit(f"line {lineno}: field mismatch {sorted(set(row) ^ FIELDS)}")
        if not ID_RE.match(row["id"]) or row["id"] in seen:
            sys.exit(f"line {lineno}: bad or duplicate id {row['id']!r}")
        seen.add(row["id"])
        if row["type"] not in TYPES:
            sys.exit(f"line {lineno}: bad type {row['type']!r}")
        for key in ("prompt", "reference"):
            if not isinstance(row[key], str) or not row[key].strip():
                sys.exit(f"line {lineno}: empty {key}")
        hits = row["judgment_rubric_hits"]
        if not isinstance(hits, list) or not 2 <= len(hits) <= 5:
            sys.exit(f"line {lineno}: hits must be a list of 2-5 entries")
        for hit in hits:
            if not isinstance(hit, str) or not re.match(r"^D[1-5]: .+", hit):
                sys.exit(f"line {lineno}: bad hit {hit!r}")
        if not isinstance(row["notes"], str):
            sys.exit(f"line {lineno}: notes must be a string")
if len(seen) != 20:
    sys.exit(f"expected 20 items, found {len(seen)}")
print(f"OK: {len(seen)} items")
```

## 6. Versioning

The schema has no per-line version field. The version is carried by the repository tag (`v1.0.0`, `v1.1.0`, …) and by `CHANGELOG.md`. Any change to a field name, a type code, or an invariant is a breaking change and requires a major version bump plus a migration note. Adding a new type code is a minor version bump. Editing an item's `reference` or hits is a content change: bump the patch version and record the affected `id` values.

## 7. Why these six fields

- `id` and `type` make disagreement analyzable by failure mode instead of by anecdote.
- `prompt` and `reference` keep the item self-contained, so a scorer never needs a private brief.
- `judgment_rubric_hits` makes the must-haves explicit before scoring, which is what prevents the band from drifting after the output is seen.
- `notes` is the only free-text field, and it is deliberately narrow: provenance and limitations, not persuasion.

A schema with more fields would invite scoring by checklist. The point of the set is judgment, not field-counting.
