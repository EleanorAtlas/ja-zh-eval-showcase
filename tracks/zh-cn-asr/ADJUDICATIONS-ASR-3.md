# ADJUDICATIONS-ASR-3.md — Three disagreement rulings for zh-CN ASR forced-alignment

**Version:** 1.0 (draft)
**Companion to:** `RUBRIC-ASR-ALIGN.md` §7, `SAMPLE-SET-ASR-20.jsonl`, `RATINGS-ASR-20.csv`
**Status:** personal R&D methodology prototype, not a client production system. No audio is hosted; all evidence is text plus millisecond offsets.

## Note on these cases

The three cases below are **constructed** for this document. They model recurring failure patterns in zh-CN普通话 (Mandarin) ASR forced-alignment and are written to the taxonomy of the 20-item sample set; they are not transcripts from a client engagement, a private corpus, or a real recording. Segment IDs are illustrative case labels. Each case follows the record structure required by `RUBRIC-ASR-ALIGN.md` §7: point of disagreement, both grounds (steelmanned), rule citations, ruling, and reasoning chain, plus the amendment note.

The adjudicator's job is not to be nice to either reviewer. It is to name the smallest disputed claim, apply the highest-priority rule that covers it, and leave a record that a third person could reproduce from the text and the millisecond values alone.

---

## ADJ-ASR-001 — Clear the warning or keep the boundary?

**Segment case:** `ASR-D009-GAP` (D009 conflict-priority archetype)
**Scores under review:** Annotator A = 1; Lead Adjudicator = 5
**Gap:** 4 points → adjudication required (`RUBRIC-ASR-ALIGN.md` §7.1)

### Evidence (frozen)

- Segment under review: two adjacent utterances separated by a `135 ms` silence.
- `warning_codes`: `WARN_MINOR_GAP` on the boundary between them.
- Golden reference: the second utterance's onset is a locked `agreement` boundary, `delta_ms = +12 ms` — inside the `±30 ms` intra-utterance tolerance and the `±50 ms` onset tolerance.
- Annotator A's action: extend the first utterance's `end_ms` forward by `135 ms` to absorb the silence, pulling the second utterance's initial consonant (`/t/`-onset of `天`) into the first segment.

### Transcript fragment (constructed)

> 前句：`……我们明天再确认。`  ｜  `135 ms` 静音  ｜  后句：`天气如果不好就改期。`

A's edited boundary puts `天气` inside the first segment.

### 1. Point of disagreement

Whether the `WARN_MINOR_GAP` is a defect that must be cleared by moving the boundary (A), or an `Other` warning that must be retained because clearing it would destroy a locked `agreement` onset (Lead). Both reviewers agree the silence is `135 ms`; they disagree on what outranks what.

### 2. Annotator A — score 1 (their proposed action)

- A treats `WARN_MINOR_GAP` as a to-do: a clean segment should have zero warnings.
- The silence is real, so A reasons that absorbing it into the preceding utterance "corrects" the segmentation.
- A cites no acoustic evidence for moving the boundary; the motive is the warning list itself.
- A's own score for the action is high because the warning count drops to zero.

### 3. Lead Adjudicator — score 5 (verified retention)

- The `135 ms` silence is verified against the waveform. It is a legitimate `Other` warning, not a transcription error.
- Absorbing it does not merely add silence: it relocates the initial consonant of `天气` into the previous utterance, breaking the locked `agreement` onset at `delta_ms = +12 ms`.
- Under Protocol D009, `disagreement` / a locked `agreement` boundary outranks any `Other` warning. The boundary must stay.
- The correct action is `RETAIN_VERIFIED_OTHER`, with `R = 1 <= 3` for this recording. Score 5: every applicable check passes and the record cites the warning code and the `R` count.

### 4. Rule citations

- `RUBRIC-ASR-ALIGN.md` §1.2 (Protocol D009): `disagreement` and locked `agreement` boundaries outrank `Other` warnings; never drag a correct boundary to zero out `Other`.
- `RUBRIC-ASR-ALIGN.md` §1.2: `RETAIN_VERIFIED_OTHER`, cap `R <= 3`; violation is `REJECT_D009_VIOLATION` → `Score 1`.
- `RUBRIC-ASR-ALIGN.md` §2: intra-utterance boundary `±30 ms` and onset `±50 ms` — the existing `+12 ms` is inside tolerance, so it is `NO_EDIT`.
- `RUBRIC-ASR-ALIGN.md` §1.1 (Gate G1-ASR): moving a boundary to satisfy a warning rather than the acoustics is a fidelity failure.
- `SAMPLE-SET-ASR-20.jsonl` archetype: the D009 conflict-priority family (minor-gap `warning_codes` + `gold_action` retention taxonomy).

### 5. Ruling

**Score 1 for Annotator A's action — `REJECT_D009_VIOLATION`. Restore the original boundary. Register `RETAIN_VERIFIED_OTHER (R = 1 <= 3, Score 5)`.**

### 6. Reasoning chain

1. The disputed claim is narrow: may a verified `Other` warning be cleared by moving a boundary that is already inside tolerance? D009 answers no.
2. The existing onset at `delta_ms = +12 ms` is inside both the `±30 ms` word-boundary and `±50 ms` onset tolerances. Under §2 it is `NO_EDIT`. There is no tolerance defect to repair.
3. A's `135 ms` extension crosses into the next utterance's initial consonant. That creates a new disagreement about where `天气` belongs and destroys a locked `agreement` boundary — exactly the harm D009 ranks above `Other`.
4. A's only ground is "the warning should be zero." That is cosmetic. A cosmetic goal cannot outrank a verified boundary (rule priority, §7.5).
5. The correct action is retention, not repair: keep `WARN_MINOR_GAP`, log the verification, count it as `R = 1` within the `R <= 3` cap. That action scores 5.
6. A's action is not a contained error. Its entire effect is the boundary violation, so it is `Score 1`, not 2 or 3. The clean warning list A produced is the evidence of the violation, not a mitigation.

### 7. Record and amendment

- **Losing reviewer:** A. The error is treating an advisory `Other` warning as a mandatory fix and sacrificing an `agreement` boundary to clear it.
- **State restored:** original `end_ms`; second-utterance onset back at `delta_ms = +12 ms`; `RETAIN_VERIFIED_OTHER` logged with `WARN_MINOR_GAP`, `R = 1`.
- **Rubric action:** no new rule needed — D009 already names this case. Add the `135 ms` minor-gap / `+12 ms` onset pattern to the §1.2 examples so the next annotator sees it before scoring. Version 1.0, no re-score required beyond the recorded 1 / 5.
- **Note for the item owner:** keep at least one genuine `WARN_MINOR_GAP` in the seed set as a control. A reviewer who "fixes" it has failed the control.

---

## ADJ-ASR-002 — A tolerated tail versus a missed real overlap

**Segment case:** `ASR-TOL-OVERLAP` (tolerance-matrix + questionnaire archetype)
**Scores under review:** Rechecker = 2; Lead Adjudicator = 4
**Gap:** 2 points → adjudication required (`RUBRIC-ASR-ALIGN.md` §7.1)

### Evidence (frozen)

- Utterance tail boundary: `offset` proposed at `-22 ms` relative to the golden reference.
- Elsewhere in the same recording: two speakers co-voiced for `180 ms`; the questionnaire recorded `overlap: false`.
- `warning_codes`: `WARN_MINOR_GAP` near the tail; code `58` flagged near the co-voiced stretch.

### 1. Point of disagreement

Whether the `-22 ms` tail is a penalizable boundary error (Rechecker) or an inside-tolerance `NO_EDIT` (Lead), and whether the `180 ms` co-voicing is a substantive `overlap` mislabel that the Rechecker missed. The two issues pull in opposite directions.

### 2. Rechecker — score 2

- The tail is not exactly on the reference; any deviation should be corrected and penalized.
- The segment therefore is not clean, and a low score is warranted.
- The `overlap: false` entry was not re-examined: the reviewer focused on the boundary numbers that were explicitly proposed.

### 3. Lead Adjudicator — score 4

- `-22 ms` on an **offset** is inside the `±50 ms` utterance end tolerance. It is `NO_EDIT`; the final vowel coda must not be trimmed. Penalizing it is a false finding.
- The `180 ms` co-voicing is a genuine overlap (`> 120 ms` sustained coexistence), so `overlap: false` is wrong. This is one missed core check.
- Tolerance compliance passes, transcript fidelity is unaffected, but D4 (`overlap`) fails — one substantive element needs re-review. Under band 3/4 logic, a single missed element with otherwise sound work is not a 2.
- Score 4: usable with a substantive-but-contained recheck of the questionnaire; the disputed `-22 ms` penalty is rejected.

### 4. Rule citations

- `RUBRIC-ASR-ALIGN.md` §2: utterance onset/offset `±50 ms`; `-22 ms` is inside → `NO_EDIT`; never cut the 句尾韵母尾音.
- `RUBRIC-ASR-ALIGN.md` §4.2: `overlap = true` for sustained co-voicing beyond the `<= 120 ms` short-pause ceiling; `180 ms` qualifies.
- `RUBRIC-ASR-ALIGN.md` §4.2: warning codes are hints to inspect, not automatic values — code `58` triggers inspection, the waveform decides.
- `RUBRIC-ASR-ALIGN.md` §6, band 4: core checks pass, one non-core/secondary gap; band 3: one must-have missing.
- `SAMPLE-SET-ASR-20.jsonl` archetype: the tolerance / overlap family (`delta_ms` values paired with questionnaire `overlap` values).

### 5. Ruling

**Score 4. Reject the `-22 ms` penalty (`NO_EDIT`, inside `±50 ms`). Correct `overlap: false → true` for the `180 ms` co-voicing.**

### 6. Reasoning chain

1. The two disputed claims are separated first. Claim one is a boundary-quality claim; claim two is a questionnaire claim. They are independent and scored separately.
2. Claim one: `-22 ms` is compared against the **offset** row of the matrix (`±50 ms`), not the intra-utterance row (`±30 ms`). It is inside. The Rechecker used the wrong row. No edit and no penalty are due.
3. Claim one also has a fidelity component: the proposed trim would cut the tail vowel's coda. §2 forbids this outright. The Rechecker's finding is rejected on both magnitude and acoustic grounds.
4. Claim two: `180 ms` of coexistence exceeds the `<= 120 ms` short-pause ceiling, so it is genuine overlap, not adjacent turn-taking. Code `58` was a correct hint that went unused. `overlap: false` is wrong.
5. The ruling is 4, not 2: the only live defect is one questionnaire value; boundaries and transcript are sound. A 2 would imply a core failure or a contained fabrication, neither of which is present.
6. The ruling is 4, not 5: `overlap` is an explicit must-have (D4) and it fails. A 5 would reward the segment while ignoring the mislabel the case was built to test.
7. The number follows the two-row audit — tolerance pass, questionnaire fail — not the midpoint between the reviewers' scores.

### 7. Record and amendment

- **Losing reviewer:** Rechecker. Two errors: applying the `±30 ms` word-boundary tolerance to an utterance offset, and omitting the questionnaire dimension from a full-scope `RECHECK`.
- **State corrected:** keep `delta_ms = -22` as `NO_EDIT`; set `questionnaire.overlap = true`; log code `58` as inspected.
- **Rubric action:** add an explicit note to §2 that the tolerance row is chosen by **boundary class** (word boundary vs onset/offset vs bridge), and to §3 that `RECHECK` must visit all three questionnaire dimensions, not only proposed boundaries. Version 1.1 (next version); re-score the affected items with both reviewers.
- **Note for the item owner:** keep a `<= 120 ms` adjacent-turn example in the seed set as the negative control for `overlap`; without it, reviewers learn "flag every gap as overlap."

---

## ADJ-ASR-003 — Natural voice plus in-car TTS is not a synthetic recording

**Segment case:** `ASR-TTS-MIX` (questionnaire / anti-false-kill archetype)
**Scores under review:** Annotator A = 1 (their `synthetic: true` action); Lead Adjudicator = 5 (`synthetic: false`)
**Gap:** 4 points → adjudication required (`RUBRIC-ASR-ALIGN.md` §7.1)

### Evidence (frozen)

- Recording: a driver speaks a natural command — `导航到最近的充电站。` — followed immediately by an in-car navigation TTS prompt `前方路口右转，继续直行两百米。`
- The target of the task is the **driver's natural utterance**; the navigation prompt is a background / non-target source.
- Annotator A's action: mark the whole recording `synthetic: true` and exclude it from the human-speech corpus.

### 1. Point of disagreement

Whether the presence of audible TTS makes the recording `synthetic: true` (A), or whether the target natural human voice governs and the TTS is merely a non-target background source (Lead). Both reviewers agree a TTS voice is audible; they disagree on which voice the question asks about.

### 2. Annotator A — score 1 (their proposed action)

- A applies a literal test: synthetic speech is audible in the file, therefore `synthetic: true`.
- Marking `true` is conservative, A argues — it avoids contaminating the human-speech set with machine audio.
- A does not separate the target utterance from the background source and does not retain the natural transcript.
- The consequence is that a genuine human command is dropped from the corpus.

### 3. Lead Adjudicator — score 5 (corrected action)

- The questionnaire asks whether the **target utterance** is machine-generated. The driver's command is natural human speech. `synthetic: false`.
- The anti-false-kill rule in §4.3 is explicit: natural voice mixed with background TTS → `synthetic: false`; retain the natural transcript and mark the background/non-target source boundary.
- A's action conflates "a synthetic source is present" with "the target is synthetic," then converts that conflation into bulk exclusion. This is a Gate G1-ASR failure with a material consequence: human speech is destroyed.
- Corrected action: `synthetic: false`, natural-voice transcript retained, TTS span annotated as non-target background. Score 5.

### 4. Rule citations

- `RUBRIC-ASR-ALIGN.md` §4.3: natural human voice + background TTS → **`synthetic: false`**; retain natural transcript; annotate the background source boundary.
- `RUBRIC-ASR-ALIGN.md` §4.3: "no questionnaire dimension has a default answer" — neither `true` nor `false` is a safe default; the target source is decided by evidence.
- `RUBRIC-ASR-ALIGN.md` §3, `SYNTHETIC_AUDIT`: separate natural/TTS mixing from pure synthetic speech.
- `RUBRIC-ASR-ALIGN.md` §1.1 (Gate G1-ASR): a decision that discards verified human speech on a misapplied rule is a centerpiece fidelity failure → `Score 1`.
- `SAMPLE-SET-ASR-20.jsonl` archetype: the synthetic-mixing family (natural target voice + background source span, retention action).

### 5. Ruling

**Score 1 for Annotator A's action — false synthetic kill. Correct to `synthetic: false`, retain the natural-voice transcript, and annotate the TTS span as background / non-target source. Corrected action: Score 5.**

### 6. Reasoning chain

1. The smallest disputed claim: "does any audible TTS make the whole recording synthetic?" No — the question is about the target source, per §4.3.
2. The driver's command is natural human speech. It is the target. The navigation prompt is a background, non-target source. The correct value is `synthetic: false`.
3. A's literal test ("TTS is audible → true") is the exact false-kill pattern §4.3 forbids. It is not a conservative error; it deletes the very data the task exists to collect.
4. Under rule priority, Gate G1-ASR and the §4.3 questionnaire rule outrank A's house habit of "mark true to be safe." Habit is not a written rule (§7.5).
5. A's action is a `Score 1`, not a 2: its entire effect is the erroneous exclusion of verified human speech — a materially wrong outcome if applied at scale.
6. The corrected action is a `Score 5`: `synthetic: false`, natural transcript kept, background TTS bounded. Every applicable check passes and the record names the decisive evidence (the target voice, not the audible bed).

### 7. Record and amendment

- **Losing reviewer:** A. The error is conflating the presence of a synthetic source with the nature of the target utterance, then acting on the conflation by dropping human speech.
- **State corrected:** `questionnaire.synthetic = false`; driver transcript retained; TTS span labelled background / non-target; recording kept in the human-speech corpus.
- **Rubric action:** add the "audible TTS ≠ synthetic target" line to the §4.3 examples and require `SYNTHETIC_AUDIT` to record which span is the target before assigning the value. Version 1.1; re-score affected items with both reviewers.
- **Note for the item owner:** keep the natural-plus-TTS segment as a mandatory control. A reviewer who marks it `synthetic: true` has failed the control, exactly as a reviewer who "fixes" the minor gap in ADJ-ASR-001 has failed theirs.

---

## Reproducing Cohen's κ with the zero-dependency script

The shared reporter lives at the repository root: `../../KAPPA-SCRIPT.py`. It needs only the Python 3.8+ standard library. The ratings file is a UTF-8 CSV with the header `item_id,rater_a,rater_b`, where both scores are integers in `1..5`; blank scores are excluded and reported, and extra columns are ignored. `RATINGS-ASR-20.csv` carries `rater_a_score` / `rater_b_score` values in that exact wide form so the script runs unmodified.

From this directory (`tracks/zh-cn-asr/`), run:

```bash
python ../../KAPPA-SCRIPT.py RATINGS-ASR-20.csv
```

JSON form and the built-in self-check, for reproducible capture:

```bash
python ../../KAPPA-SCRIPT.py RATINGS-ASR-20.csv --json
python ../../KAPPA-SCRIPT.py --selftest
```

**How to read the report:**

- `items scored` / `items excluded` — n and listwise exclusions. Report both; a κ without n is unreadable.
- `exact agreement` / `expected agreement` — observed and chance-expected exact agreement.
- `unweighted kappa` — chance-corrected exact agreement. Sensitive to prevalence and to small n.
- `linear weighted` / `quadratic weighted` — partial credit for near misses; quadratic is the usual choice for an ordinal 1–5 scale, but it is a choice.
- `Score distribution` (rater A / B) — means, SDs, min, max. Two reviewers who never use the same band can still produce a misleading κ if prevalence is skewed; inspect the marginals.
- `Differences (A − B)` — mean, mean absolute, max absolute, variance, SD, count of disagreements, and count of gaps `>= 2`. Gaps `>= 2` here are the adjudication triggers from `RUBRIC-ASR-ALIGN.md` §7.1.
- `Items with disagreement` — the item-level table to take into adjudication. Work the largest `|d|` first.

**Interpretation discipline:**

- Do not treat `0.80` as a universal pass mark. Set the acceptance threshold before scoring; on 20 items the confidence interval is wide and a high κ is fragile.
- κ is prevalence-sensitive. A set where both raters almost always choose 5 can score high while hiding the few segments that matter. Read the distribution and the disagreement table with the coefficient.
- The three cases above are exactly the rows you should expect to disagree on: a D009 boundary vs warning conflict, a tolerance-row error paired with a missed overlap, and a natural-plus-TTS false kill. If reviewers agree on all three, the controls have failed to separate the failure modes — re-check calibration before celebrating κ.
- `--selftest` is a sanity check of the script itself (known fixture values `unweighted 0.7500 / linear 0.8649 / quadratic 0.9412`), **not** a result for this track. Run it to confirm the reporter is intact; never quote its numbers as the sample-set κ.

**What is not reproduced here:** this document does not publish a κ value for `RATINGS-ASR-20.csv`. The ratings file is generated alongside the sample set, and a coefficient is only meaningful after the two scoring passes are actually recorded. Run the command above on the frozen CSV to obtain the report; quote it with n, exclusions, distribution, and the item-level disagreement table attached.
