# Track A — `en-US → zh-TW` Enterprise & Hardware Localization LQA + A/R Adjudication

**Public calibration sample · Wave 2 · Track A**

This directory is the de-identified proof-of-work for **Track A** of a multilingual evaluation calibration hub. It demonstrates a complete, reproducible LQA (linguistic quality assurance) and A/R (adjudication / review) workflow for Traditional Chinese (`zh-TW`) localization of enterprise software and hardware UI — built for overseas and APAC LSPs, language leads, and MT/LLM evaluation teams.

The core claim this sample tests: *most `zh-TW` LQA reviewers stumble on two invisible traps — flagging legal UI bracket spacing as an error, and conflating a hard compliance lock with a translator's style preference.* The assets below let you measure that disagreement yourself with a zero-dependency Cohen's κ script.

Everything here is **100% synthetic**. No client source text, no brand names, and no automation-implementation code are included.

---

## What you can verify here

| Capability | Where |
|---|---|
| 20 synthetic bilingual items with protected-token traps, DNT boundaries, and authority conflicts | `SAMPLE-SET-ZHTW-20.jsonl` |
| 1–5 MQM-weighted rubric with an auto-reject gate and two false-positive shields | `RUBRIC-ZHTW-LQA.md` |
| Three complete double-review conflict rulings + κ reproduction guide | `ADJUDICATIONS-ZHTW-3.md` |
| Two-rater 1–5 scores for every item, ready for the κ script | `RATINGS-ZHTW-20.csv` |
| Chance-corrected inter-annotator agreement, no dependencies | `../../KAPPA-SCRIPT.py` |

---

## File structure

```
tracks/zh-tw-lqa/
├── SAMPLE-SET-ZHTW-20.jsonl   # 20 fully synthetic en-US → zh-TW items (no client text)
├── RATINGS-ZHTW-20.csv        # item_id,rater_a,rater_b — 1–5 ordinal scores
├── RUBRIC-ZHTW-LQA.md         # 1–5 MQM rubric, G1 gate, triage, tiers, shields, DNT matrix
├── ADJUDICATIONS-ZHTW-3.md    # 3 worked double-review rulings + κ interpretation framework
└── README.md                  # this file
```

- **`SAMPLE-SET-ZHTW-20.jsonl`** — one synthetic source/candidate pair per line, with domain action labels (`KEEP` / `REPLACE` / `REVIEW`), adjudication labels (`AGREE` / `FLAG` / `OVERRIDE` / `DISPUTE`), severity (`BLOCK` / `WARN` / `INFO`), lock type (`HARD_LOCK` / `PREFERENCE_LOCK`), and 1–5 gold scores.
- **`RATINGS-ZHTW-20.csv`** — the two-rater score table. Columns: `item_id,rater_a,rater_b`, each a 1–5 integer ordinal score.
- **`RUBRIC-ZHTW-LQA.md`** — the scoring contract: MQM 5-dimension weights (Accuracy 25 / Fluency 25 / Terminology 25 / Style 15 / Brand Voice 10), the `Accuracy < 18` auto-reject gate, the three-branch decision protocol, the four-tier authority order, the bracket-whitespace shield, the `HARD_LOCK`/`PREFERENCE_LOCK` split, and the DNT six-category matrix.
- **`ADJUDICATIONS-ZHTW-3.md`** — three full conflict rulings (false-positive bracket spacing, official TB vs generic TM, hard-lock vs preference-lock) plus the κ command and interpretation framework.

---

## Reproduce the IAA check

From this directory, run the repository-root zero-dependency script against the ratings file:

```
python ../../KAPPA-SCRIPT.py RATINGS-ZHTW-20.csv
```

The script returns unweighted Cohen's κ, quadratic weighted κ, and the raw disagreement table with item IDs. Report item count, exclusions, score distribution, and both κ values together; set your acceptance threshold before scoring. See `ADJUDICATIONS-ZHTW-3.md` §4 for the full interpretation framework, including how the three adjudicated items are meant to move κ.

**Suggested first exercise.** Score the 20 items blind, run the script, then read the three adjudications and re-score the matching rows with the shields applied. Compare weighted κ before and after — that delta is the practical value of the false-positive shields.

---

## How to read the sample set

Each item is a self-contained calibration case. The three adjudicated archetypes are worth opening first:

- **`ZHTW-001`** — a legal halfwidth-bracket boundary that a literal diff mistakes for a spacing defect. Correct handling: `KEEP`, `HARD_LOCK`, Score 5.
- **`ZHTW-006`** — a generic-TM mainland term set that overrides the official term base. Correct handling: `REPLACE`, `BLOCK`, Score 1 via the gate.
- **`ZHTW-012`** — a word-order variant that a reviewer tries to force-rewrite. Correct handling: `KEEP`, `PREFERENCE_LOCK`, Score 5.

They bracket the two failure modes the track is designed to expose: over-grading a legal form, and over-grading a style preference.

---

## 1-Week `zh-TW` LQA Calibration Pilot

If you run a `zh-TW` localization or MT/LLM evaluation pipeline, this sample is the opening artifact for a **1-Week `zh-TW` LQA Calibration Pilot**:

- **Week 1, Day 1** — align on the rubric and the two false-positive shields; freeze the acceptance threshold.
- **Days 2–3** — double-score a custom item set built to your domain; run `KAPPA-SCRIPT.py` for a baseline κ.
- **Days 4–5** — adjudicate every split with the five-part record; amend the rubric for the next version (never retroactively).
- **Day 5** — re-run κ, deliver a disagreement report, a versioned rubric, and a reviewer-calibration recommendation.

Indicative engagement anchor: **$1,800–$2,800** for the one-week pilot (LSP white-label and co-delivery available). Scope and commercial terms are confirmed through the main Hub contact.

---

## Back to the Hub

 [`← Main Hub — Multilingual & Multimodal Eval Calibration`](../../README.md)

A companion track, `zh-cn-asr` (Mandarin ASR forced alignment and disagreement-priority adjudication), lives alongside this one under `../zh-cn-asr/`, using the same rubric + gold-set + κ methodology.

---

## Scope and privacy

- All examples are synthetic and constructed for this sample; no client NDA text, real locales, brand names, or private endpoints are present.
- No automation-implementation source is included; only rule names, labels, weights, and de-identified examples are published.
- This is a public methodology sample, not a certified or audited production QA system.
