---
layout: default
permalink: /
title: Multilingual & Multimodal Eval Calibration Hub — JA · zh-TW · zh-CN ASR
---

# Multilingual & Multimodal Eval Calibration Hub

**JA · en-US→zh-TW Localization LQA · zh-CN ASR Forced Alignment**

Independent practice. Written rubric. Adjudication on the record. One repository, three tracks, one shared zero-dependency agreement engine.

[See the JA sample set](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SAMPLE-SET-JA-20.md) · [Explore Track A (zh-TW LQA)](tracks/zh-tw-lqa/README.md) · [Explore Track B (zh-CN ASR)](tracks/zh-cn-asr/README.md) · [Start a scoped conversation](mailto:eleanoratlas2502@gmail.com)

---

## 3-Track Public Calibration Matrix

| Track | Language / modality | What it calibrates | Core method highlights | Open assets |
|---|---|---|---|---|
| **Track 1 — Root / Wave 1** | `JA` Japanese adversarial LLM & translation evaluation | Register, ambiguity and factuality in Japanese model output and translation | Keigo inversion; subject omission and negation-polarity traps; **G1 factual-honesty one-veto gate** | [SAMPLE-SET-JA-20.md](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SAMPLE-SET-JA-20.md) · [ja_adversarial_seed.jsonl](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ja_adversarial_seed.jsonl) · [RUBRIC-1-5.md](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/RUBRIC-1-5.md) · [ADJUDICATIONS-3.md](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ADJUDICATIONS-3.md) |
| **Track A — Wave 2** | `en-US → zh-TW` enterprise & hardware localization LQA + accept/reject review | Bracket-spacing false positives, authority precedence and severity in Traditional Chinese UI localization | Halfwidth `[ ]` normal-spacing **false-positive shield**; `KEEP` / `REPLACE` / `REVIEW` triage; four-tier authority order (**Official TB > Project TB > Custom TM > Generic TM**); `HARD_LOCK` vs `PREFERENCE_LOCK` split; MQM 5 dimensions + `Accuracy < 18` veto gate. Measured unweighted **κ = 0.6825** (exact agreement `0.7500`). | [README](tracks/zh-tw-lqa/README.md) · [SAMPLE-SET-ZHTW-20.jsonl](tracks/zh-tw-lqa/SAMPLE-SET-ZHTW-20.jsonl) · [RATINGS-ZHTW-20.csv](tracks/zh-tw-lqa/RATINGS-ZHTW-20.csv) · [RUBRIC-ZHTW-LQA.md](tracks/zh-tw-lqa/RUBRIC-ZHTW-LQA.md) · [ADJUDICATIONS-ZHTW-3.md](tracks/zh-tw-lqa/ADJUDICATIONS-ZHTW-3.md) |
| **Track B — Wave 2** | `zh-CN` Mandarin ASR forced-alignment & disagreement-first adjudication | Millisecond boundary disputes and recording-level questionnaire edges — with zero hosted audio | Zero-audio, metadata-only offsets + warning-code validation; **disagreement-first rule** (retain a verified `Other` warning at `R <= 3` rather than destroy an aligned `agreement` word boundary); `±30 ms` (intra-utterance / short pause) and `±50 ms` (onset / offset) tolerance matrix; three-dimension recording-level questionnaire calibration (natural voice mixed with in-car / speaker TTS → `synthetic: false` to prevent discarding usable human speech). Measured unweighted **κ = 0.5105** (exact agreement `0.6500`). | [README](tracks/zh-cn-asr/README.md) · [SAMPLE-SET-ASR-20.jsonl](tracks/zh-cn-asr/SAMPLE-SET-ASR-20.jsonl) · [RATINGS-ASR-20.csv](tracks/zh-cn-asr/RATINGS-ASR-20.csv) · [RUBRIC-ASR-ALIGN.md](tracks/zh-cn-asr/RUBRIC-ASR-ALIGN.md) · [ADJUDICATIONS-ASR-3.md](tracks/zh-cn-asr/ADJUDICATIONS-ASR-3.md) |

Every track ships a frozen rubric, a synthetic gold/seed set and a written adjudication record. All examples are fully synthetic and de-identified: no client source text, no brand names and no automation-implementation source are published.

---

## Unified Zero-Dependency Statistical IAA Engine

One root-level script reproduces the inter-annotator agreement statistic for **all three tracks**. `KAPPA-SCRIPT.py` needs only the Python 3.8+ standard library and reports unweighted, linear and quadratic Cohen's κ, the score distributions and the item-level disagreement table.

From the repository root:

```bash
python KAPPA-SCRIPT.py --selftest
python KAPPA-SCRIPT.py tracks/zh-tw-lqa/RATINGS-ZHTW-20.csv
python KAPPA-SCRIPT.py tracks/zh-cn-asr/RATINGS-ASR-20.csv
```

- `--selftest` verifies the reporter itself against a known fixture (unweighted `0.7500` / linear `0.8649` / quadratic `0.9412`) — a sanity check, not a track result.
- **Track A** (`RATINGS-ZHTW-20.csv`): n = 20, 0 exclusions — unweighted **κ = 0.6825**, exact agreement `0.7500` (linear `0.5789`, quadratic `0.5276`).
- **Track B** (`RATINGS-ASR-20.csv`): n = 20, 0 exclusions — unweighted **κ = 0.5105**, exact agreement `0.6500` (linear `0.3780`, quadratic `0.2033`).

κ is prevalence-sensitive and fragile at n = 20. Always report it together with the item count, exclusions, score distribution and the item-level disagreement table; fix the acceptance threshold before scoring. See the track adjudication notes for the full interpretation framework. Script: [KAPPA-SCRIPT.py](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/KAPPA-SCRIPT.py) · [Schema and validator](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SCHEMA.md).

---

## Navigation

- [Overview (README)](https://github.com/EleanorAtlas/ja-zh-eval-showcase#readme)
- [20-item Japanese sample set](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SAMPLE-SET-JA-20.md)
- [1–5 rubric](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/RUBRIC-1-5.md)
- [Three adjudication notes](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ADJUDICATIONS-3.md)
- [Schema and validator](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SCHEMA.md)
- [Inter-rater agreement script](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/KAPPA-SCRIPT.py)
- [Machine-readable seed set (JSONL)](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ja_adversarial_seed.jsonl)
- [Track A — zh-TW LQA](tracks/zh-tw-lqa/README.md)
- [Track B — zh-CN ASR](tracks/zh-cn-asr/README.md)
- [License](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/LICENSE)

---

## About

I am Eleanor Chan, an independent evaluation practitioner with an M.A. in Econometrics from Waseda University. My paid work has included multilingual quality assurance, machine-translation and LLM evaluation, and forced-alignment adjudication — the part of the work where two readings disagree and someone has to write down which one holds, and why. Past project experience includes evaluation and language-quality work delivered with NetEase Youdao.

Japanese, English, Simplified Chinese and Traditional Chinese (`JA / EN / zh-CN / zh-TW`) are languages I work in. In evaluation that is not a line on a slide. It is the difference between catching a register error and accepting a fluent sentence that is wrong in a way the rubric has to name.

I work independently. I do not present a team, an agency, or a lab. When a scope needs more capacity than one evaluator can honestly cover, I say so before the scope is agreed, not after.

## Method

The method below is **a personal R&D methodology prototype, not a client production system**. I publish it so the reasoning can be inspected, not because it has been certified.

**1. Pre-registered corpus snapshot.**
The item set, the reference judgments, and the scoring rules are frozen and hashed before any output is scored. Items are not swapped after results are seen. If an item turns out to be defective, it is retired in public with the reason and a version number.

**2. Blinded multi-arm comparison.**
System identity is stripped, output order is randomized, and every arm is scored against the same frozen items with the same rubric. A scorer does not know which model produced which response.

**3. Deterministic positive and negative controls.**
Each batch includes items with known-good and known-bad responses. If a scorer cannot separate the controls, that scorer's batch is not used. This catches drift that a raw agreement number hides.

**4. Adversarial regression.**
Every failure found in a review becomes a permanent case. New model versions re-run the full regression set, including the cases that used to fail. A score that only goes up is a reason to check the harness, not a reason to celebrate.

> **What this is not.** It is not a certified benchmark, not a production client system, and not a claim of statistical validity at scale. It is a documented, reproducible starting point — useful precisely because its limits are written down.

## Services

Three fixed-scope service cuts, mapped to the three public tracks above:

- **Custom Rubric & Gate Design.** A 1–5 band rubric written for your task: boundary examples from your domain, fabrication / G1 one-veto gates, false-positive shields, lock tiers and alignment-tolerance matrices, plus a written adjudication procedure. For teams that already have items and reviewers but no shared scale — or a scale two reviewers read differently.
- **Golden Calibration Set (JSONL).** A frozen, fully synthetic item set with reference judgments and rubric hits, in the same de-identified format as the three published sets. For teams whose current evaluation is too easy to pass, or rewards a fluent wrong answer.
- **Inter-Annotator Agreement κ Audit & Lead Adjudication.** A blinded double-scoring pass, unweighted / linear / quadratic κ via `KAPPA-SCRIPT.py`, and a written adjudication of every material disagreement. For teams that need a defensible number and an audit trail, not one reviewer's impression.

Every engagement is **fixed-scope and flat-fee per deliverable, scoped and agreed before work starts**. Each ends with a short handover note: what was tested, what was not, and where the rubric is still weak.

### 1-Week Calibration Pilot Scope

- **Day 1** — align on the rubric and the error shields (bracket spacing / lock tiers for Track A, disagreement-first precedence for Track B); freeze the acceptance threshold.
- **Days 2–3** — double-score a custom item set built to your domain; run `KAPPA-SCRIPT.py` for a baseline κ.
- **Days 4–5** — adjudicate every split with the five-part record; amend the rubric for the next version, never retroactively.
- **Day 5** — re-run κ and deliver a disagreement report, a versioned rubric, and a reviewer-calibration recommendation.

## Co-delivery & partner calibration

Two collaboration routes are open, inside the same written-scope discipline:

- **Co-delivery.** If you run an agency or an in-house localization team and need an independent evaluator for Japanese or a Chinese language inside a larger delivery, I join as the evaluation arm under a written scope of my own: fixed items, a frozen rubric, and findings delivered on the record — including findings that are inconvenient for the delivery.
- **Partner calibration.** If your team already runs its own review pass, I calibrate your reviewers against the rubric: a shared fixture set, a blinded double-scoring pass with unweighted and weighted κ (`KAPPA-SCRIPT.py`), and a written adjudication of every material disagreement, so your numbers and mine are readable against each other.

Neither route turns this into a team, an agency, or a lab. Capacity is arranged per scope and disclosed, and the method remains a personal R&D methodology prototype.

## Sample

The root sample is 20 Japanese items, written for this page. It covers ambiguity, cultural context, instruction conflict, keigo register, numerical consistency, and negation scope. Each item has a reference judgment and a 1–5 scoring key. Three constructed adjudication notes show what happens when two reviewers disagree. Track A and Track B publish their own 20-item synthetic sets with the same structure.

Twenty items is not a benchmark. It is enough to see how I read a case, where I put the boundary, and whether the written rubric survives contact with a disagreement.

- [Download the 20-item Japanese sample set (MIT)](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SAMPLE-SET-JA-20.md)
- [Read the 1–5 rubric](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/RUBRIC-1-5.md)
- [Read the three adjudications](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ADJUDICATIONS-3.md)

## Contact

Write to **[eleanoratlas2502@gmail.com](mailto:eleanoratlas2502@gmail.com)** with the language pair or track, the task, the approximate number of items or segments, and the decision the evaluation needs to support. If the fit is wrong, I will say so.

---

© 2026 Eleanor Chan. Independent evaluation practice. Sample set and rubric text licensed MIT.

Repository: <https://github.com/EleanorAtlas/ja-zh-eval-showcase>

Site: <https://eleanoratlas.github.io/ja-zh-eval-showcase/> · Repository: <https://github.com/EleanorAtlas/ja-zh-eval-showcase>
