# ADJUDICATIONS-ZHTW-3.md — Three double-review conflict rulings (`zh-TW` LQA)

**Version:** 1.0 (2026-11-21)
**Companion to:** `RUBRIC-ZHTW-LQA.md` (definitions, gates, and shields cited below), `SAMPLE-SET-ZHTW-20.jsonl`, `RATINGS-ZHTW-20.csv`
**Status:** public methodology sample, not a client production system

## Note on these cases

The three cases below are **constructed** for this document. The candidate translations and review notes were written to illustrate specific failure modes; they are not transcripts from a model run, a client engagement, or a public evaluation. The item archetypes correspond to `ZHTW-001`, `ZHTW-006`, and `ZHTW-012` in `SAMPLE-SET-ZHTW-20.jsonl`. Every segment is synthetic and contains no client source text, brand name, or automation code.

Each case follows the five-part record — plus reasoning chain and amendment — required for a defensible ruling:

1. Point of disagreement (the smallest disputed claim)
2. Both sides' strongest grounds, steelmanned
3. Rule citations (exact section of `RUBRIC-ZHTW-LQA.md`)
4. Ruling (one score, with the losing side's error named)
5. Reasoning chain (why the rule applies, step by step)
6. Record and amendment

The adjudicator's job is not to be agreeable. It is to name the smallest disputed claim, apply the highest-priority rule that actually covers it, and leave a record a third person can reproduce.

---

## ADJ-ZHTW-001 — Bracket-Whitespace false-positive trap

**Item archetype:** `ZHTW-001` (protected halfwidth UI tag spacing)
**Source (en-US):** `Press [Fn] + [F5] to toggle LED profile.`
**Candidate (zh-TW):** `按下 [Fn] + [F5] 以切換 LED 設定檔。`
**Scores under review:** Model A / initial reviewer = **2 / EDIT**; Model B / Lead Adjudicator = **5 / KEEP**
**Gap:** 3 points → adjudication required (§10)

### 1. Point of disagreement

Whether the spaces around `[Fn]` and `[F5]` are a **formatting error to be edited** (Model A) or **legal UI spacing to be preserved** (Model B). Both sides accept the terminology and meaning; the dispute is purely about the bracket boundary.

### 2. Model A — score 2, `EDIT`

- The source contains spaces around the bracketed tokens. The target also contains spaces. A literal diff shows "extra" spaces, which A reads as redundant whitespace in the Traditional Chinese output.
- The reviewer treats any spacing difference between source and target as a D4 style defect.
- Under the weight model, D4 style loses points; two flagged boundaries push the band down to 2, and the branch is `EDIT`.

### 3. Model B (Lead Adjudicator) — score 5, `KEEP`

- The spaces are not an artifact — they are the correct English/UI spacing convention around halfwidth bracketed keys. The target must preserve them.
- `RUBRIC-ZHTW-LQA.md` §7.1 is explicit: a spacing defect must **not** be reported for a legal halfwidth-bracket boundary. The only reportable defects are a deleted token, a fullwidth-quote substitution, an overwritten key name, or a broken tag.
- The candidate preserves `[Fn]` and `[F5]` verbatim, uses the correct Taiwan terms (`設定檔`), and reads naturally. No dimension loses points. Band 5, branch `KEEP`.
- The lock is `HARD_LOCK`: the bracket tokens are protected UI entities (§8, category 6), so preserving them is a compliance requirement, not a preference.

### 4. Rule citations

- §7.1 Bracket-Whitespace False-Positive Shield — legal halfwidth-bracket spacing is `KEEP`, never a spacing defect.
- §8 DNT category 6 (tag lifecycle protection) — the bracket tokens must not be renamed or deleted.
- §5 `KEEP` requires a reason citing the decisive dimension; the decisive dimension here is D4 (style) resolving to "no defect."
- §4 Band 5 — every must-have passes; no edit beyond personal preference.

### 5. Ruling

**`OVERRIDE → KEEP` — Score 5, `HARD_LOCK`, severity `INFO` (no defect; the `INFO` tag records the shield invocation, not an error).**

### 6. Reasoning chain

1. The smallest disputed claim is: "Are the spaces around `[Fn]` / `[F5]` a defect?"
2. §7.1 answers this before any weighing: the spaces follow normal English/UI spacing and are legal. The shield exists precisely for this pattern.
3. Because the candidate matches the "legal" example verbatim, no D4 points are lost. Model A's diff-based reasoning mistakes a protected boundary for a defect; that is the error.
4. With no dimension loss and no G1 trigger, the behavioral anchor (§4 Band 5) governs: ship as-is.
5. The lock is `HARD_LOCK` because the bracket tokens are protected entities (§8/6). Calling it `PREFERENCE_LOCK` would be wrong — a reviewer would then be allowed to "edit" them, which is the exact failure being overturned.
6. The ruling is 5, not 4. There is no non-core gap; the only issue raised was a false positive.

### 7. Record and amendment

- **Losing reviewer:** Model A. Error: treating a legal protected-token boundary as a whitespace defect (false positive).
- **Rubric action:** no new rule needed — §7.1 already names this pattern. Add this segment to the §7.1 "legal" example set so the next reviewer sees it before scoring. Version 1.0, no re-score required beyond the recorded 5.
- **κ note:** this item is a deliberate high-disagreement trap. Before adjudication it contributes a 2-vs-5 split; after the gold label is fixed to 5, reviewers who apply the shield correctly move toward agreement. It is the single most instructive item in the pilot for demonstrating why the false-positive shield raises κ.

---

## ADJ-ZHTW-002 — Four-tier authority: Official TB vs Generic TM

**Item archetype:** `ZHTW-006` (mainland-term leakage via lower-tier TM)
**Source (en-US):** `Firmware update available. Use default settings.`
**Candidate (zh-TW):** `固件更新可用。使用默认配置。`
**Scores under review:** Model R = **PASS / Score 4**; Model B / Lead Adjudicator = **FLAG → REPLACE**
**Gap:** review conclusion reversed; gate must be applied (§3)

### 1. Point of disagreement

Whether the candidate is a **passable minor terminology issue** (Model R) or a **hard-locale breach that fires the auto-reject gate** (Model B). Both sides see the same two mainland terms; they disagree on which authority tier governs.

### 2. Model R — `PASS`, score 4

- The candidate is fluent and the meaning is transferable: a reader can understand that a firmware update is available and that default settings should be used.
- The terms came from a generic translation-memory suggestion, so R treats them as an acceptable lower-tier variant rather than an error.
- Under the weight model, D3 loses a little for terminology drift; D1/D2 pass. R lands at band 4 and passes the item.

### 3. Model B (Lead Adjudicator) — `FLAG → REPLACE`

- The Official Approved Term Base (Tier 1, §6) mandates the Taiwan forms `韌體更新` and `預設設定`. A generic TM (Tier 4) can never override Tier 1.
- The candidate uses the mainland forms `固件` and `默认配置`. These are on the G1-B1 watchlist (§3, Trigger B1) — simplified/mainland vocabulary leakage into the Traditional Chinese target.
- G1-B1 is a `BLOCK`-level hard red line. It locks **Score = 1** regardless of the otherwise decent MQM total, and the branch must be `REPLACE`.
- Corrected `targetText`: `韌體更新可用。使用預設設定。`

### 4. Rule citations

- §6 four-tier precedence — Tier 1 Official Approved TB (`韌體更新` / `預設設定`) overrides Tier 4 Generic/MT output.
- §3 G1 Trigger B1 — mainland-region vocabulary leakage is a `BLOCK` hard red line → Score 1.
- §1 D3 Terminology (weight 25) and the watchlist table in §3.
- §5 `REPLACE` requires a `targetText`; §5 also states a gated item is always `REPLACE`, never `KEEP`.
- §2 severity — `BLOCK` because the locale contract is breached.

### 5. Ruling

**`FLAG → REPLACE` — Score 1 (G1-B1), `HARD_LOCK`, severity `BLOCK`.**

### 6. Reasoning chain

1. The smallest disputed claim is: "Does a Tier 4 generic-TM form override a Tier 1 Official TB form?" §6 answers no — Tier 1 wins.
2. The candidate contains `固件` and `默认配置`, both explicitly listed in the §3 watchlist as mainland forms requiring Taiwan equivalents (`韌體`, `預設設定`).
3. That makes this a G1-B1 red-line breach, not a matter of degree. G1 is applied before the band (§9 step 4) and locks Score 1.
4. Model R's error is treating a compliance breach as a small terminology deduction. The terms did not come from an approved source, so their origin in a TM is irrelevant — Tier 4 has no authority here.
5. The branch is `REPLACE` with the exact `targetText` above, because a gated item cannot be kept or deferred.
6. The lock is `HARD_LOCK`: the Taiwan terms are mandated by the locale contract. This is the opposite of a preference call.

### 7. Record and amendment

- **Losing reviewer:** Model R. Error: accepting a Tier 4 form over Tier 1 and down-grading a `BLOCK` red line to a band-4 terminology nit.
- **Rubric action:** no new rule — §3 B1 and §6 already cover it. Add this segment to the §3 watchlist examples so the next reviewer sees the exact mainland pair before scoring. Version 1.0, no re-score required beyond the recorded 1.
- **κ note:** this is the highest-stakes reconciliation in the set. Without adjudication, R's `PASS/4` and B's `REPLACE/1` disagree by 3 points and on the branch; the gold label forces the gate to be applied consistently. It tests whether reviewers treat the four-tier order as binding rather than advisory.

---

## ADJ-ZHTW-003 — `HARD_LOCK` vs `PREFERENCE_LOCK` severity split

**Item archetype:** `ZHTW-012` (correct variant vs reviewer word-order preference)
**Source (en-US):** `Connect the cable to the USB-C port on the rear panel.`
**Candidate (zh-TW):** `將纜線連接到後方面板的 USB-C 連接埠。`
**Reviewer's preferred rewrite:** `請將 USB-C 纜線接至後方面板的連接埠。`
**Scores under review:** Model R = **ISSUE / Score 3**; Model B / Lead Adjudicator = **DISPUTE → KEEP**
**Gap:** 2 points and opposing branches → adjudication required (§10)

### 1. Point of disagreement

Whether the word-order difference is a **real severity issue requiring a forced rewrite** (Model R) or a **protected translator preference that must not be scored** (Model B). Both forms are grammatically correct, terminologically compliant, and Taiwan-idiomatic; the terms `纜線` and `連接埠` are already the correct Taiwan forms in both.

### 2. Model R — `ISSUE`, score 3

- R prefers the verb-first phrasing and reads the candidate's `將...連接到...` order as slightly less natural.
- R issues an `ISSUE` and deducts to band 3, requesting the segment be rewritten to the preferred order.
- R treats the difference as a D2 fluency defect.

### 3. Model B (Lead Adjudicator) — `DISPUTE → KEEP`

- The candidate is 100% compliant: correct Taiwan terminology (`纜線`, `連接埠`, `後方面板`), correct grammar, no DNT or bracket issue, no G1 trigger.
- The only difference is word order and a minor phrasing preference. Both forms convey identical meaning and meet the locale contract.
- §7.2 is explicit: a difference not written in the rubric or authoritative term base is inadmissible as a scoring ground. `將 A 連接到 B` and `請將 A 接至 B` are both correct Traditional Chinese; neither is mandated.
- The difference is therefore `PREFERENCE_LOCK`, severity `INFO`, **no score deduction**. Band 5, branch `KEEP`.
- Forcing a rewrite would be exactly the over-editing that drives κ collapse: the translator's correct choice is preserved, and the reviewer's preference is logged, not imposed.

### 4. Rule citations

- §7.2 `HARD_LOCK` vs `PREFERENCE_LOCK` separation — preference differences are `INFO`, no deduction, `KEEP`.
- §5 `KEEP` requires a reason; §5 also warns against using unwritten rules as scoring grounds.
- §4 Band 5 — every must-have passes.
- §2 severity — `INFO` because meaning and compliance are unchanged.
- §10 adjudication — "both give a different must-have" / unwritten-rule citation triggers adjudication; decide, do not average.

### 5. Ruling

**`DISPUTE → KEEP` — Score 5, `PREFERENCE_LOCK`, severity `INFO`.**

### 6. Reasoning chain

1. The smallest disputed claim is: "Is a word-order difference a D2 fluency defect?" §7.2 answers no when both forms are correct and compliant.
2. Audit the dimensions: D1 (meaning) identical; D2 (grammar) both correct; D3 (terms) both use the Taiwan forms; D4/D5 no breach; no G1 trigger. Every must-have passes (§4 Band 5).
3. R's `ISSUE` rests on an unwritten house-style preference, which §5 declares inadmissible as a scoring ground. That is the error.
4. Classify the difference as `PREFERENCE_LOCK` (§7.2) — when in doubt, protect the correct variant. Severity is `INFO`; no points are deducted.
5. The branch is `KEEP` with a recorded `INFO` note capturing R's preferred alternative, so the preference is visible without being imposed.
6. The ruling is 5, not 4. There is no non-core gap: the candidate is complete and correct as-is. A 3 would reward a forced rewrite of a compliant segment — the precise failure mode this case exposes.

### 7. Record and amendment

- **Losing reviewer:** Model R. Error: promoting a personal word-order preference to a `HARD_LOCK`-level fluency defect and forcing an unnecessary rewrite.
- **Rubric action:** no new rule — §7.2 already protects preference variants. Add this pair to the §7.2 examples as the canonical "both correct, keep both" case. Version 1.0, no re-score required beyond the recorded 5.
- **κ note:** this case measures the opposite failure from Case 1. Case 1 punishes over-grading a legal form; Case 3 punishes over-grading a style preference. Together they bracket the two ways reviewers inject noise. A reviewer who consistently applies `PREFERENCE_LOCK` protects κ; one who forces rewrites collapses it.

---

## 4. Reproducing IAA / Cohen's κ with `KAPPA-SCRIPT.py`

The repository ships a **zero-dependency** statistics helper at the showcase root. From this directory (`tracks/zh-tw-lqa/`), run:

```
python ../../KAPPA-SCRIPT.py RATINGS-ZHTW-20.csv
```

**Input contract.** `RATINGS-ZHTW-20.csv` carries one row per item with the columns `item_id,rater_a,rater_b`, where `rater_a` and `rater_b` are 1–5 integer ordinal scores. The three cases above are the deliberately high-disagreement rows in that file; adjudication fixes their gold labels before the final κ run.

**What the script reports.** It computes:
- **Unweighted Cohen's κ** — chance-corrected agreement treating all 1–5 categories as nominal.
- **Quadratic weighted κ** — penalizes distant disagreements more than adjacent ones; the more informative statistic for an ordinal 1–5 scale.
- **Raw disagreement table and distribution** — the count of items per score and the pairwise mismatches, including item IDs.

**Interpretation framework.** Use the following as a *reading aid*, not an automatic pass/fail law:

| κ range | Conventional label | Reading for this track |
|---|---|---|
| < 0.00 | Poor | Agreement worse than chance — stop and recalibrate |
| 0.00–0.20 | Slight | Rubric is not being applied consistently |
| 0.21–0.40 | Fair | Reviewers need joint calibration on the shields and tiers |
| 0.41–0.60 | Moderate | Usable seed; investigate the highest-disagreement items |
| 0.61–0.80 | Substantial | Target band for a 20-item calibration set |
| 0.81–1.00 | Almost perfect | Check for contamination — reviewers may have seen each other's sheets |

Set the acceptance threshold **before** scoring; do not import 0.80 as a universal pass mark. With n = 20, a high κ can still be fragile and the confidence interval is wide. Always report: item count, exclusions, score distribution, both κ values, and the raw disagreement table. A κ without those is unreadable.

**How the three cases feed κ.** Before adjudication, the three rows contribute large splits (2 vs 5, 4 vs 1, 3 vs 5). After the gold labels are fixed to 5 / 1 / 5, reviewers who correctly apply §7.1 (bracket shield), §6 + §3 (tier precedence + gate), and §7.2 (preference lock) converge. Re-run the script after a calibration session and compare weighted κ before vs after — the delta is the practical value of the shields.

---

## What these three cases have in common

None was resolved by finding a more eloquent way to say "I prefer a different number." Each turned on a check written before the candidate was seen:

- **ADJ-ZHTW-001:** a protected-token boundary mistaken for a spacing defect (false positive).
- **ADJ-ZHTW-002:** a lower-tier form overriding a binding official term base (authority + gate).
- **ADJ-ZHTW-003:** a personal preference promoted to a hard defect (over-editing).

That is the point of publishing the rulings. The rubric is not interesting when two reviewers agree. It is interesting when they do not — and the record still lets a third person see exactly why the score is what it is.
