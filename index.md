---
layout: default
permalink: /
title: Fixed-scope evaluation deliverables in Japanese & Simplified Chinese
---

# Fixed-scope evaluation deliverables in Japanese & Simplified Chinese (zh-CN) — golden sets, adversarial case sets, and written adjudication rubrics.

Independent practice. Written rubric. Adjudication on the record.

[See the sample set](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SAMPLE-SET-JA-20.md) · [Start a scoped conversation](mailto:eleanoratlas2502@gmail.com)

## Navigation

- [Overview (README)](https://github.com/EleanorAtlas/ja-zh-eval-showcase#readme)
- [20-item Japanese sample set](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SAMPLE-SET-JA-20.md)
- [1–5 rubric](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/RUBRIC-1-5.md)
- [Three adjudication notes](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ADJUDICATIONS-3.md)
- [Schema and validator](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SCHEMA.md)
- [Inter-rater agreement script](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/KAPPA-SCRIPT.py)
- [Machine-readable seed set (JSONL)](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ja_adversarial_seed.jsonl)
- [License](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/LICENSE)

---

## About

I am an independent evaluation practitioner with an MSc in Econometrics from Waseda University. My paid work has included multilingual quality assurance, machine-translation and LLM evaluation, and forced-alignment adjudication — the part of the work where two readings disagree and someone has to write down which one holds, and why. Past project experience includes evaluation and language-quality work delivered with NetEase Youdao.

Japanese, English, and Chinese (Simplified) are languages I work in natively. In evaluation that is not a line on a slide. It is the difference between catching a register error and accepting a fluent sentence that is wrong in a way the rubric has to name.

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

## Deliverables

Every deliverable ends with a short handover note: what was tested, what was not, and where the rubric is still weak. Scope is written down before the first item is authored.

### D1 — Rubric only

A 1–5 rubric written for your task: band descriptors, boundary examples drawn from your domain, a fabrication gate, and an adjudication procedure.

For teams that already have items and reviewers but no shared scale — or a scale that two reviewers read differently.

*Not included:* item writing, scoring, or agreement statistics.

### D2 — Golden set 100 + rubric + calibration

100 items with reference judgments and rubric hits, plus a calibration pass: two independent scorings, agreement statistics, and a written adjudication of every material disagreement.

For teams that need a defensible number and an audit trail, not one reviewer's impression.

*Not included:* a benchmark release, a vendor ranking, or a guarantee of model quality.

### D3 — Adversarial taxonomy + seed set + rubric

A taxonomy of failure modes for your task, a seed set built from that taxonomy, and a rubric that separates near-misses from failures.

For teams whose current evaluation is too easy to pass, or rewards a fluent wrong answer.

*Not included:* a red-team exercise, a safety audit, or a claim of full coverage.

Every engagement is **fixed-scope and flat-fee per deliverable, scoped and agreed before work starts**.

## Co-delivery & partner calibration

Two collaboration routes are open, inside the same written-scope discipline:

- **Co-delivery.** If you run an agency or an in-house localization team and need an independent evaluator for Japanese or Simplified Chinese inside a larger delivery, I join as the evaluation arm under a written scope of my own: fixed items, a frozen rubric, and findings delivered on the record — including findings that are inconvenient for the delivery.
- **Partner calibration.** If your team already runs its own review pass, I calibrate your reviewers against the rubric: a shared fixture set, a blinded double-scoring pass with unweighted and weighted κ (`KAPPA-SCRIPT.py`), and a written adjudication of every material disagreement, so your numbers and mine are readable against each other.

Neither route turns this into a team, an agency, or a lab. Capacity is arranged per scope and disclosed, and the method remains a personal R&D methodology prototype.

## Sample

The sample is 20 Japanese items, written for this page. It covers ambiguity, cultural context, instruction conflict, keigo register, numerical consistency, and negation scope. Each item has a reference judgment and a 1–5 scoring key. Three constructed adjudication notes show what happens when two reviewers disagree.

Twenty items is not a benchmark. It is enough to see how I read a case, where I put the boundary, and whether the written rubric survives contact with a disagreement.

- [Download the 20-item sample set (MIT)](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/SAMPLE-SET-JA-20.md)
- [Read the 1–5 rubric](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/RUBRIC-1-5.md)
- [Read the three adjudications](https://github.com/EleanorAtlas/ja-zh-eval-showcase/blob/main/ADJUDICATIONS-3.md)

## Contact

Write to **[eleanoratlas2502@gmail.com](mailto:eleanoratlas2502@gmail.com)** with the language pair, the task, the approximate number of items, and the decision the evaluation needs to support. If the fit is wrong, I will say so.

---

© 2026 Eleanor Chan. Independent evaluation practice. Sample set and rubric text licensed MIT.

Repository: <https://github.com/EleanorAtlas/ja-zh-eval-showcase>

Site: <https://eleanoratlas.github.io/ja-zh-eval-showcase/> · Repository: <https://github.com/EleanorAtlas/ja-zh-eval-showcase>
