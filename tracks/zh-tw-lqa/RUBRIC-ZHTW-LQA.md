# RUBRIC-ZHTW-LQA.md — 1–5 LQA scoring rubric for `en-US → zh-TW` localization

**Version:** 1.0 (2026-11-21)
**Applies to:** one zh-TW candidate translation in `SAMPLE-SET-ZHTW-20.jsonl`
**Status:** public methodology sample, not a client production system
**Companions:** `ADJUDICATIONS-ZHTW-3.md`, `SAMPLE-SET-ZHTW-20.jsonl`, `RATINGS-ZHTW-20.csv`

> This document is the public, de-identified scoring contract for Track A. All examples below are **synthetic** and were written for this sample. They contain no client source text, no brand names, and no automation-implementation code.

---

## 0. Scope and unit of analysis

This rubric scores **one candidate translation of one source segment**. It does not score a vendor, a model, or a whole file. One candidate receives one integer from 1 to 5, one decision branch, one lock type, one severity label, and one written rationale.

The scale is **ordinal**. A 4 is not "twice" a 2, and the distance between 3 and 4 is not assumed to equal the distance between 1 and 2. Do not compute means across items and present them as interval measurements without saying so. When a summary is needed, report the distribution and the median, and report disagreement alongside it.

The score is a **defect-based quality judgment**, not a verdict on whether a sentence "sounds nice." A fluent, confident translation that leaks a mainland term or breaks a placeholder is a low score.

The MQM weights in §1 are an **audit lens**, not an averaging formula. They tell the reviewer where the 100-point budget sits and which dimension is decisive. You do not add five independent ratings; you inspect five dimensions, then assign one anchored band (§4) — subject to the gate in §3.

---

## 1. The MQM 5-dimension weight model (100 points)

| # | Dimension | Weight | What it measures | Typical defect |
|---|---|---:|---|---|
| D1 | **Accuracy** | 25 | Meaning transfer: no omission, addition, inversion, or untranslated residue | Mistranslated negation; source text left untranslated |
| D2 | **Fluency** | 25 | Target-language grammar, naturalness, and readability | Calque from English syntax; broken Traditional Chinese |
| D3 | **Terminology** | 25 | Conformance to the authoritative term base and locale standard | 固件 → 韌體, 默认配置 → 預設設定 |
| D4 | **Style** | 15 | Register, UI concision, capitalization, punctuation, number/unit format | Overly literal UI label; wrong spacing around tags |
| D5 | **Brand Voice** | 10 | Product voice and tone consistency across the segment set | Wrong tone in a status or error message |

The weights are fixed for this track. D1 and D3 carry the most risk: D1 failures can make a UI actionable in the wrong way, and D3 failures are the most common source of reviewer disagreement in `zh-TW` delivery. D5 is deliberately the smallest weight so that tone preference cannot dominate a compliance decision.

**Scoring with the weights.** For each dimension, estimate the points lost to defects in that dimension (0 = no defect). The sum of the five retained points is the **MQM total** (0–100). The MQM total selects a provisional band in §4; the gate in §3 can override it.

---

## 2. Severity levels: `BLOCK` / `WARN` / `INFO`

Severity is about **consequence**, not about how many points were lost. It is recorded independently of the band.

| Severity | Meaning | Examples | Effect |
|---|---|---|---|
| **`BLOCK`** | Violates a hard locale, legal, structural, or brand-red-line rule; the segment must not ship | Simplified-character leakage, mainland-only vocabulary leakage, placeholder/tag damage, DNT mistranslation, untranslated source residue | Triggers G1 → locks Score 1; requires `REPLACE` |
| **`WARN`** | Real accuracy, terminology, or structural defect that degrades quality but does not breach a hard line | Metric-unit spacing error, terminology drift from the authoritative term base, cable/peripheral naming inconsistency | Caps band at 3; requires `REPLACE` |
| **`INFO`** | Non-core variation that does not change meaning or compliance | Word-order or phrasing preference, optional polish, stylistic note | No score deduction; pairs with `KEEP` under `PREFERENCE_LOCK` |

A reviewer who assigns `BLOCK` must name the specific red line. A reviewer who assigns `INFO` to a real `WARN` defect has under-graded; a reviewer who assigns `WARN`/`BLOCK` to a pure preference has over-graded and is the main cause of κ collapse (see §7.2).

---

## 3. G1-ZHTW — Auto-Reject Gate (one-vote veto)

G1 is applied **before** the band is assigned. It has two independent triggers. Either one is sufficient.

**Trigger A — Accuracy floor.** If the Accuracy dimension (D1) scores **below 18 / 25**, lock **Score = 1**.

**Trigger B — `BLOCK`-level hard red line.** If any of the following is present, lock **Score = 1** regardless of the MQM total:

1. **Simplified-character or mainland-region vocabulary leakage** into the Traditional Chinese target. Non-exhaustive watchlist and their Taiwan-target equivalents:

   | Leaked form (mainland) | Required Taiwan form | Meaning |
   |---|---|---|
   | 固件 | 韌體 | firmware |
   | 内存 | 記憶體 | memory |
   | 宏 | 巨集 | macro |
   | 激活 | 啟用 | activate |
   | 默认配置 | 預設設定 | default settings |
   | 软件 / 硬件 | 軟體 / 硬體 | software / hardware |
   | 端口 / 电缆 | 連接埠 / 纜線 | port / cable |

2. **Placeholder or tag damage** — a placeholder (`{0}`, `%s`), a UI tag, or a bracketed token is deleted, renamed, or overwritten.
3. **DNT mistranslation** — an entity that must remain Do-Not-Translate (§8) is translated.
4. **Untranslated-source contamination** — source-language text remains in the target output where translation was required.

**Why the gate exists.** A high MQM total cannot compensate for a red-line breach. A translation can score 82/100 on the weight model yet still be unshippable because a single mainland term violates the locale contract. G1 makes that judgment mechanical and auditable: cite the trigger, lock the score, move on.

**G1 does not create a score of 1 by averaging.** It is a veto. When G1 fires, record the trigger ID (A or B1–B4), the exact offending fragment (≤200 characters), and proceed directly to band 1.

---

## 4. Ordinal 1–5 Calibration Scale (anchored)

Each band gives an MQM-total range and a behavioral anchor. Where a candidate matches the "just outside" example, assign the lower band. Where the MQM total and the behavioral anchor disagree, the **behavioral anchor governs**, because it describes what a reviewer can actually observe. G1 (§3) overrides both.

| Band | MQM total | One-line test | Severity ceiling |
|---:|---:|---|---|
| **5 — Publication-ready** | 90–100 | Ship as-is; no edit beyond personal preference | `INFO` only |
| **4 — Usable, one pass** | 75–89 | One non-core edit; core meaning and compliance intact | `WARN` on one non-core point |
| **3 — Needs revision** | 60–74 | Core judgment present but one must-have missing or a secondary error | `WARN` |
| **2 — Not usable** | 40–59 | A core must-have fails in a locally contained way | `WARN` / `BLOCK` (non-gated) |
| **1 — Misleading / rejected** | 0–39 **or any G1 trigger** | Do not follow; materially wrong action if shipped | `BLOCK` |

### Band 5 — Publication-ready
Every must-have passes; no hard or warning defect. A reviewer could ship the segment as-is.
- **Inside:** `按下 [Fn] + [F5] 以切換 LED 設定檔。` — correct terms, legal tag spacing, natural Taiwan phrasing.
- **Just outside (→4):** Same meaning, but one optional nuance is missing from a longer UI string; one non-core polish edit remains.

### Band 4 — Usable with one minor edit
All core must-haves pass; one non-core gap remains (a terse phrasing, an optional style touch). A careful editor fixes it in one pass without re-deciding the segment.
- **Inside:** Terminology and structure fully correct; one UI line is slightly long but unambiguous.
- **Just outside (→3):** The "minor" item is actually a terminology drift from the authoritative term base — that is a `WARN` on a core dimension, so band 3.

### Band 3 — Needs substantive revision
The core judgment is present but incomplete: one must-have is missing, or a secondary error requires a careful reader to intervene before the segment is usable.
- **Inside:** Meaning is preserved but one metric-unit spacing rule is violated consistently; requires a real edit pass.
- **Just outside (→2):** The error changes the instruction the end user would follow (an inverted condition or wrong control label).

### Band 2 — Not usable
A core must-have fails in a way a careful reader would catch. The failure is real but local: a partial fix, a wrong-but-plausible term, an inconsistent placeholder.
- **Inside:** One placeholder is renamed consistently; the segment is recoverable but must not ship.
- **Just outside (→1):** The same defect crosses a G1 red line (e.g., the renamed token is a protected tag) — gate fires, band 1.

### Band 1 — Misleading / rejected
Use G1. The segment inverts a core judgment, leaks a mainland term, breaks a tag, mistranslates a DNT entity, or leaves source text untranslated. A reader must not follow it as-is.
- **Inside:** `固件更新可用。使用默认配置。` — two mainland terms → G1-B1 → Score 1.
- **Inside:** untranslated source residue inside a target UI string → G1-B4 → Score 1.

---

## 5. Three-branch decision protocol: `KEEP` / `REPLACE` / `REVIEW`

Every scored item carries exactly one decision branch. The branch describes the **action**, not the score.

| Branch | When to use | Required output | Typical lock / severity |
|---|---|---|---|
| **`KEEP`** | Candidate is correct as-is, including legal preference variation | A reason citing the decisive dimension and evidence | `HARD_LOCK` or `PREFERENCE_LOCK`; `INFO` if preference-only |
| **`REPLACE`** | A deterministic correction is required and the correct target is known | `targetText` (the corrected segment) + the rule cited | `HARD_LOCK`; `WARN` or `BLOCK` |
| **`REVIEW`** | Meaning or authority is genuinely ambiguous; a human decision is needed | A specific question and a recommended default | No lock until resolved; escalate |

Rules:
- `REPLACE` without a `targetText` is incomplete. A reviewer cannot flag a defect without supplying the corrected target.
- `REVIEW` is not a way to avoid a decision. Use it only when the authoritative source is missing or two tiers conflict without a resolution rule.
- `KEEP` requires a reason. "Looks fine" is not a reason; name the dimension and quote the fragment.
- A gated item (G1) is always `REPLACE` — never `KEEP`, never `REVIEW`.

---

## 6. Four-tier authority precedence (terminology conflict adjudication)

When two sources disagree on a term, the higher tier wins. Cite the winning tier in the rationale.

| Tier | Source | Authority | Example |
|---:|---|---|---|
| **Tier 1** | **Official Approved Term Base (TB)** | Binding; overrides all lower tiers | `韌體更新` / `預設設定` mandated for Taiwan target |
| **Tier 2** | **Project Context TB** | Binding within the project; yields to Tier 1 | Project-level product-name list |
| **Tier 3** | **Custom Domain TM** | Advisory; yields to Tiers 1–2 | Previously approved domain translations |
| **Tier 4** | **Generic / MT Output** | Lowest; never authoritative on its own | Raw machine translation, general bilingual glossary |

**Adjudication rule:** A generic-TM or machine-translation suggestion (Tier 4) can never override an Official Approved TB entry (Tier 1). If a reviewer accepts a Tier 4 form over a Tier 1 form, that is not a preference call — it is a terminology defect under D3 and, when the Tier 4 form is a mainland term, a G1-B1 `BLOCK`.

---

## 7. Two high-frequency false-positive shields

These two protocols exist to stop reviewers from manufacturing defects. Both protect inter-annotator agreement: an reviewer who "fixes" a legal form or a personal-preference difference injects noise that no statistical method can recover.

### 7.1 Bracket-Whitespace False-Positive Shield

Halfwidth square brackets `[ ]` are **protected UI tokens**. The spaces around them that follow normal English or UI spacing conventions are **legal** and must **not** be flagged as redundant or extra spaces.

- **Legal (must be `KEEP`):** `Press [Fn] + [F5] to toggle LED profile.` → `按下 [Fn] + [F5] 以切換 LED 設定檔。` — the spaces around `[Fn]` / `[F5]` are correct English/UI spacing.
- **Illegal (flag only these):** the bracket token is deleted, replaced with fullwidth quotation marks (`「」` / `『』`), overwritten with a translation, or the key name inside is changed.

**Red line:** Do not report a spacing defect for a legal halfwidth-bracket boundary. A `REPLACE` that only "fixes" such spacing is a false positive and will be overturned on adjudication (see Case 1 in `ADJUDICATIONS-ZHTW-3.md`).

### 7.2 `HARD_LOCK` vs `PREFERENCE_LOCK` separation

| Lock | Scope | Reviewer action | Score effect |
|---|---|---|---|
| **`HARD_LOCK`** | Compliance, terminology, structural, or DNT correctness that the locale contract requires | Must fix — `REPLACE` | `WARN` / `BLOCK`; can drive band down or fire G1 |
| **`PREFERENCE_LOCK`** | Word order, phrasing, or style where both forms are correct and Taiwan-compliant | May keep — `KEEP` | `INFO`; **no score deduction** |

**Rule:** If a difference is not written in the rubric or the authoritative term base, it is **inadmissible as a scoring ground**. A reviewer who deducts points for a `PREFERENCE_LOCK` difference is over-editing; forced rewrites on preference items are the single largest cause of κ collapse in calibration pilots. Preserve the translator's correct choice and log the preference as `INFO` (see Case 3 in `ADJUDICATIONS-ZHTW-3.md`).

When in doubt, classify as `PREFERENCE_LOCK` — protecting a correct variant is cheap; forcing an unnecessary rewrite is not.

---

## 8. DNT (Do-Not-Translate) six-category matrix

A DNT entity that is translated is a G1-B3 `BLOCK`. A DNT entity that is left untranslated when translation was required is a D1 accuracy defect. Use this matrix to decide.

| # | Category | Typical members | Default action | Boundary note |
|---:|---|---|---|---|
| 1 | **Industry standard identifiers** | IEEE / ISO / ANSI / NFPA-style standard numbers and codes | DNT | Keep the identifier verbatim; translate only the surrounding prose |
| 2 | **Program & technical entities** | Code snippets, SQL, token key names, concatenated code words, placeholders | DNT | Preserve case, spelling, and delimiters exactly |
| 3 | **User-input utterances** | Quoted end-user speech inside the source | DNT | Do not translate or "improve" quoted user text |
| 4 | **AI-assistant prompt routing** | Prompt/instruction strings embedded in source | **Context-dependent** | DNT only in the specific context where the string is an executable prompt; do not DNT an entire sentence just because it mentions a prompt |
| 5 | **File names, paths, emails, sample data** | Paths, filenames, addresses, example records | DNT | Preserve literally; localize only the descriptive label |
| 6 | **Tag lifecycle protection** | UI/format tags and their lifecycle markers | DNT | Never translate, rename, or delete a tag (overlaps G1-B2) |

Category 4 is the highest-disagreement boundary: decide by **function in context**, never by keyword. Apply the narrowest DNT scope that the context requires.

---

## 9. Scoring procedure (run in order)

1. **Pin the version.** Record the item hash and the candidate hash. A score without a version is not reproducible.
2. **Read the source and candidate together.** Identify protected tokens and DNT entities first (§7, §8).
3. **Compute the MQM totals** by dimension (§1).
4. **Apply G1** (§3). If a trigger fires, lock Score 1, cite the trigger, skip to step 8.
5. **Apply the two false-positive shields** (§7) — remove any defect that is actually a legal bracket spacing or a preference difference.
6. **Assign the band** using the behavioral anchor in §4 (not the raw average).
7. **Choose the decision branch and lock** (§5, §7.2). For `REPLACE`, supply `targetText`.
8. **Write one rationale sentence** naming the decisive dimension, the rule cited (section number), and the evidence fragment (≤200 characters). "Good" and "natural" are not evidence.
9. **Record.** Score, branch, lock, severity, rationale, item version, reviewer ID, date. No score is entered without a rationale.

Do not average dimension scores. A candidate that is excellent on D4/D5 but fails D1 is not a 3.5 — it is a failed candidate with good prose.

---

## 10. Adjudication and κ calibration (pointers)

Adjudicate when any of the following is true: the two scores differ by 2 or more points; one reviewer applies G1 and the other does not; both give the same band but cite different must-haves; or a reviewer cites a rule not in this document. Full ruling structure and three worked cases are in `ADJUDICATIONS-ZHTW-3.md`.

For IAA, run the zero-dependency script from this directory:

```
python ../../KAPPA-SCRIPT.py RATINGS-ZHTW-20.csv
```

Report unweighted Cohen's κ, quadratic weighted κ, the raw disagreement table, item count, exclusions, and the score distribution. Set the acceptance threshold **before** scoring; do not import 0.80 as a universal pass mark. See `ADJUDICATIONS-ZHTW-3.md` §4 for the interpretation framework.

---

## 11. Known limits

- **Small n.** Twenty items cannot support stable per-type estimates. Treat the set as a seed, not a benchmark.
- **Constructed examples.** All illustrative segments are synthetic and written for this sample; they are not client material.
- **Ordinal scale.** Do not compute means as interval measurements without disclosure.
- **Locale-specific examples.** The red-line watchlist and Traditional Chinese examples are `zh-TW`-specific; the frame may transfer, the vocabulary does not.
- **Prototype status.** This is a public methodology sample, not a certified or audited production system. It does not evaluate legal compliance, privacy, or safety beyond the DNT categories listed above.
