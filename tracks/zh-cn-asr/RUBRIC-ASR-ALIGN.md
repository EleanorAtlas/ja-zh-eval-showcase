# RUBRIC-ASR-ALIGN.md — Ordinal 1–5 rubric for zh-CN ASR forced-alignment & transcription-QA adjudication

**Version:** 1.0 (2026-11-21 draft)
**Applies to:** the 20 constructed items in `SAMPLE-SET-ASR-20.jsonl` and the paired integer scores in `RATINGS-ASR-20.csv`
**Companion:** `ADJUDICATIONS-ASR-3.md`
**Status:** personal R&D methodology prototype, not a client production system. No audio is hosted; every claim is checkable against text plus millisecond offsets.

## 0. Scope and unit of analysis

This rubric scores **one adjudication action on one recording segment**. It does not score a model, a vendor, a transcription engine, or a whole dataset. One action receives one integer from 1 to 5 and one written rationale.

The scale is ordinal. A 5 is not "five times" a 1, and the distance between 4 and 5 is not assumed to equal the distance between 2 and 3. Do not compute means across items and present them as interval-scale measurements without saying so. If a summary number is needed, report the distribution, the median, and the raw disagreement table together.

A score is not a verdict on whether an annotator was "careful." A confident, well-formatted boundary edit that breaks a verified agreement boundary is a low score.

All worked examples below are **constructed** from a synthetic zh-CN普通话 (Mandarin) sample set. Chinese transcript fragments and `delta_ms` / `start_ms` / `end_ms` values are illustrative teaching data, not client transcripts.

---

## 1. Scoring procedure

1. **Pin the version.** Record the item file hash and the action hash. A score without a version is not reproducible.
2. **Read the item.** Segment ID, competing transcriptions, proposed boundary edit, `delta_ms`, `warning_codes`, and the three-dimension questionnaire.
3. **Apply the gates** in this order: Gate G1-ASR (§1.1), then Protocol D009 (§1.2). A failed gate removes the top bands before any dimension is considered.
4. **Audit the must-haves.** Mark each relevant check from §2–§4 pass or fail. Do not convert the checks into a point total.
5. **Assign the band** using §6.
6. **Write one rationale sentence.** It must name the decisive check and the decisive evidence (a millisecond value, a warning code, or a quoted transcript fragment). "Looks cleaner" is not evidence.
7. **Record.** Score, rationale, gate outcomes, item version, reviewer ID, date. No score is entered without a rationale.

Do not average dimension scores. An action that is excellent on tolerance compliance but violates D009 is not a 3.5; it is a gated failure.

### 1.1 Gate G1-ASR — evidence authenticity and acoustic fidelity (one-vote veto)

The pre-filled ASR text is **a timeline locator only**. It tells the annotator where sounds probably are; it is not authority over what was said.

If an action does any of the following, the maximum score is **2**:

- guesses an **unuttered syllable** to make a transcript read smoothly (`按语义通顺度补字`);
- **rewrites a number's reading form** without acoustic evidence (e.g., switching between `二〇二六` / `两千零二十六` / `2026` to match expectation);
- **fabricates or rounds a timestamp** that was not verified against the waveform (`捏造未核验的时间戳`);
- **clips or invents** a boundary to satisfy a warning code rather than the recorded acoustics.

If the fabrication is the centerpiece of the action — the action's whole value is a guessed transcript or an invented boundary — the score is **1**.

High-risk loci where G1-ASR bites hardest: digits and dates, English code-mixing (`英文混读`), singing (`歌声`), medical and proper nouns. For these, "the sentence makes more sense this way" is inadmissible. Only a checkable acoustic observation justifies an edit.

A confident tone earns no point. Hedging does not repair a fabrication; the fabricated element must be removed.

### 1.2 Protocol D009 — disagreement-first over cosmetic `Other` warnings (iron rule)

This is the protocol that separates a defensible alignment workflow from a cosmetic one.

**Severity order (a lower line never overrides a higher line):**

1. `disagreement` / a newly created disagreement between competing readings;
2. an already **locked `agreement` word boundary**;
3. `Other` warnings — `WARN_MINOR_GAP`, `WARN_SHORT_SEGMENT`, `WARN_LONG_SEGMENT`.

`Other` warnings are **advisory**, not defects to be cleared at any cost. A minor gap, a short segment, or a long segment that is *verified* against the audio may be legitimately retained.

**The rule.** When clearing an `Other` warning would damage a locked `agreement` boundary or create a new `disagreement`:

- **NEVER** drag a correct boundary to zero out the warning;
- **MUST** execute `RETAIN_VERIFIED_OTHER`: keep the verified boundary, keep the warning, and log the reason;
- **CAP:** at most `R <= 3` retained `Other` warnings per recording;
- **VIOLATION:** any action that sacrifices an `agreement` boundary — or manufactures a `disagreement` — for the sake of an `Other` warning is `REJECT_D009_VIOLATION` and receives **Score = 1**, regardless of how clean the warning list looks afterward.

Worked pattern (Case 1 in `ADJUDICATIONS-ASR-3.md`): a `135 ms` silence triggers `WARN_MINOR_GAP`; stretching the preceding utterance's tail to swallow it cuts the next utterance's initial consonant into the previous segment and destroys a golden `agreement` boundary of `delta_ms = +12 ms`. The correct ruling is `Score 1 / REJECT_D009_VIOLATION`; restore the boundary and register `RETAIN_VERIFIED_OTHER (R = 1 <= 3, Score 5)`.

`RETAIN_VERIFIED_OTHER` is not a licence to hoard warnings. Beyond `R = 3`, the segment returns to adjudication: the boundary claim must be re-verified before a fourth warning is retained.

---

## 2. Forced-alignment timing tolerance matrix

Tolerances apply to the **boundary under review**, not to the segment as a whole. A boundary inside tolerance is `NO_EDIT`; a boundary outside tolerance is `EDIT_WITH_EVIDENCE` and must cite an acoustic observation.

| Boundary class | Tolerance (免改容差) | Inside tolerance | Outside tolerance |
|---|---|---|---|
| Intra-utterance word boundary — 句中词切分边界 | `±30 ms` | `NO_EDIT`; do not split or merge words for cosmetic symmetry | `EDIT_WITH_EVIDENCE`; cite the consonant/vowel onset |
| Utterance onset / offset — 句首/句尾起止边界 | `±50 ms` | `NO_EDIT`; **never cut the initial consonant breath (首辅音气音) or the final vowel coda (句尾韵母尾音)** | `EDIT_WITH_EVIDENCE`; quote the clipped or padded sound |
| Short-pause bridge — 跨短停顿桥接 (`pause <= 120 ms`) | `±30 ms` | `NO_EDIT`; keep the bridge inside the single utterance | `EDIT_WITH_EVIDENCE`; re-check VAD against the waveform |

Two consequences that reviewers repeatedly miss:

- A boundary at `-22 ms` on an utterance **offset** is inside the `±50 ms` tail tolerance. It is `NO_EDIT`. It is not a defect to be penalized (see Case 2).
- A short silence of `<= 120 ms` between words is a **bridge**, not a reason to split the utterance. Splitting it creates a new boundary and risks violating D009 if the split touches a locked agreement edge.

The tolerances are symmetric and inclusive at the limits: `30 ms` and `50 ms` exactly are inside. They are decision thresholds, not measurement uncertainties — do not widen them "because the ASR looked approximately right."

---

## 3. Four task variants (口径)

The same segment can be visited under different task variants. The variant determines what counts as evidence and what the annotator is allowed to change.

| Variant | Mandate | Evidence rule | Common failure |
|---|---|---|---|
| `ANNOTATION` | Produce or repair transcript and boundaries within the authorized scope; save and submit | ASR is a locator; every edit cites acoustics | "Fixing" a smooth-sounding transcript by guessing syllables |
| `ADJUDICATION` | Decide between competing readings; the **current root draft and its base points (BPs)** are the evidence | A prior `own completion` does **not** substitute for current evidence | Reusing an earlier self-completion as if it still held |
| `RECHECK` | Reconcile **the entire authorized scope item by item** | No sampling; each boundary and each questionnaire dimension is checked | Spot-checking a few rows and declaring the batch clean |
| `SYNTHETIC_AUDIT` | Decide whether the **target speech itself** is machine-generated | Natural voice plus background/non-target TTS is **not** synthetic; see §4 | Marking a whole recording `synthetic: true` because a TTS bed is audible |

A variant mismatch is itself a finding. If a reviewer applies `ANNOTATION` standard of proof to an `ADJUDICATION` decision, record the error; do not blend the two standards.

---

## 4. Three-dimension recording-level questionnaire

Each recording carries three questionnaire dimensions. They are recording-level judgments, independent of transcript word choice.

### 4.1 `multiSpeaker`

True when more than one **distinct natural talker** is present in the target speech. A single talker plus a TTS bed is `multiSpeaker: false` — the TTS is a source, not a second natural speaker. A change in channel or recording quality is not a second speaker.

### 4.2 `overlap`

True when two voices are **co-voiced** — their voiced intervals coexist across the short-pause ceiling (`> 120 ms` of sustained coexistence is the operating threshold). Distinguish this from **adjacent turn-taking**, where one voice ends and the other begins with a gap or a `<= 120 ms` bridge: that is `overlap: false`.

Case 2 illustrates the split: a `180 ms` real acoustic overlap left as `overlap: false` is a substantive mislabel; a `<= 120 ms` adjacent gap is correctly `false`. Warning codes `3 / 4 / 58 / 62 / 64` are hints to inspect, not automatic `true` values — the waveform decides.

### 4.3 `synthetic` — the anti-false-kill rule

`synthetic` asks whether the **target utterance** is machine-generated. It does **not** ask whether any synthetic sound appears anywhere in the file.

**Rule (防误杀 / anti-false-kill):** when a natural human voice is mixed with background TTS broadcast (e.g., a driver's spoken command followed by an in-car navigation TTS prompt), the correct value is **`synthetic: false`**. Retain the natural-voice transcript and mark the boundary of the background / non-target source; do **not** discard the whole recording as synthetic.

Marking `synthetic: true` in that situation is a high-severity error: it deletes genuine human speech from the corpus. Under this rubric it is a Gate G1-ASR failure and, when it drives bulk exclusion, **Score 1** (see Case 3).

Conversely, a fully machine-generated target utterance with no natural human target voice is `synthetic: true`, even if the file also contains incidental room noise.

No questionnaire dimension has a default answer. Blank is not `false`; it is missing and must be resolved by evidence.

---

## 5. Dimensions

The dimensions describe what to inspect. They are not weights and are not summed.

### D1 — Boundary fidelity

Are the edited boundaries inside the applicable tolerance matrix (§2), with the onset/offset protections respected? A boundary that clips a 首辅音气音 or a 句尾韵母尾音 fails D1 even if the numeric delta is small.

### D2 — Conflict priority

Was Protocol D009 (§1.2) honored? Was the `agreement` boundary preserved when an `Other` warning tempted an edit? Did retained warnings stay within `R <= 3`?

### D3 — Transcript fidelity

Was Gate G1-ASR (§1.1) honored? Are numbers, code-mixed English, singing, and medical terms supported by acoustics rather than semantic fluency?

### D4 — Questionnaire correctness

Are `multiSpeaker`, `overlap`, and `synthetic` each supported by the recording-level evidence in §4, including the natural-plus-TTS rule?

### D5 — Procedure and record

Was the correct task variant applied (§3), was the authorized scope fully reconciled, and is the rationale specific enough for a third person to reproduce the decision?

---

## 6. Bands (1–5, ordinal anchors)

Each band has an **inside** example (clearly belongs) and a **just-outside** example (looks close, belongs one band lower). Where an example and an item key differ, the item key governs.

### Band 5 — Ready to submit

All applicable checks pass; no gate fires; rationale names a concrete millisecond value or warning code.

- **Inside — D009 retention.** A `135 ms` minor gap is verified; the golden `delta_ms = +12 ms` agreement boundary is preserved; `RETAIN_VERIFIED_OTHER (R = 1 <= 3)` is logged with reason. `Score 5`.
- **Just outside — Band 4.** Same correct retention, but the rationale only says "kept the original" without citing the warning code or the `R` count. The action is right; the record is too thin to reproduce.

### Band 4 — Usable with a minor record edit

All core checks pass; one non-core transparency gap remains — a terse rationale, an unstated but harmless assumption, a missing `R` count. A careful reviewer fixes it in one pass without re-deciding the segment.

- **Inside — tolerance no-edit.** An utterance offset of `-22 ms` is correctly left untouched as inside `±50 ms`; the rationale states the tolerance but omits the explicit "did not clip the final vowel" note.
- **Just outside — Band 3.** The same offset is left untouched, but the segment also contains a `180 ms` real overlap that was never examined. A core check (`overlap`) is missing.

### Band 3 — Needs substantive revision

The core judgment is present but incomplete: one must-have fails or a secondary error requires rework before the action is usable.

- **Inside — overlap missed.** Boundaries and transcript are sound, but `overlap: false` was recorded on a `180 ms` co-voiced stretch. The segment must be re-reviewed under §4.2.
- **Just outside — Band 2.** The reviewer also "fixed" the transcript by guessing an unuttered syllable to smooth the line. That is a Gate G1-ASR failure, not a contained secondary error.

### Band 2 — Not usable

A core must-have fails, or a G1-ASR fabrication is real but local: a wrong questionnaire value, a guessed syllable, a fabricated timestamp that does not drive the whole action.

- **Inside — number reading rewritten.** A digits/reading-form change was made with no acoustic basis. The rest of the boundaries are intact; the edit itself must be reverted.
- **Just outside — Band 1.** The fabricated syllable is the centerpiece of the submitted transcript, or an invented boundary defines the segment. That is a 1.

### Band 1 — Misleading / vetoed

The action inverts a core judgment, fires a gate at its center, or would cause a materially wrong outcome if applied.

- **Inside — D009 violation.** Stretching a boundary to clear `WARN_MINOR_GAP` cuts the next utterance's initial consonant and destroys a locked `agreement` boundary (`delta_ms = +12 ms`). `REJECT_D009_VIOLATION → Score 1`.
- **Inside — false synthetic kill.** A natural human command plus in-car TTS is marked `synthetic: true` and the whole recording is discarded. Genuine human speech is lost. `Score 1`.

### Band summary

| Band | One-line test | Typical defect |
|---|---|---|
| 5 | Submit as-is | None |
| 4 | One-pass record edit | Thin rationale / missing `R` count |
| 3 | Re-review one element | Missed overlap, incomplete scope |
| 2 | Do not use | Local fabrication, wrong questionnaire value |
| 1 | Vetoed | D009 violation, false synthetic kill, invented boundary |

---

## 7. Adjudication when two reviewers disagree

The purpose is a **defensible record** of why one reading prevails, or a recorded statement that the rubric cannot yet decide.

1. **Trigger.** Adjudicate when scores differ by `>= 2`, when one reviewer fires a gate and the other does not, when both pick the same band for different reasons, or when a cited rule is not in this document.
2. **Freeze the evidence.** Collect segment ID and item hash, competing transcripts, proposed boundaries with `delta_ms`, `warning_codes`, questionnaire values, and both score sheets. No new evidence after this point.
3. **Steelman restatement.** Each reviewer restates the other's position in one sentence. If neither can, the disagreement is about the rubric, not the segment.
4. **Check audit.** Build a pass/fail table for D1–D5 and the two gates. This moves the argument from adjectives to checks.
5. **Rule priority.** G1-ASR → D009 → tolerance matrix → questionnaire rules → item key → band definition → reviewer preference. A lower rule cannot override a higher one.
6. **Decide, do not average.** Choose the band supported by the highest-priority rule actually in dispute. A 1 and a 5 do not become a 3. If two bands remain defensible after a blind third score, mark the item **indeterminate**, exclude it from agreement statistics, and open a rubric defect.
7. **Record.** Five parts: point of disagreement, both grounds (steelmanned), rule citation, ruling (one band, with the losing error named), and reasoning chain. The three cases in `ADJUDICATIONS-ASR-3.md` are the template.
8. **Amend, not retrofit.** If the split exposes a missing rule, amend **after** the ruling and **for the next version**; never apply the new rule retroactively to the case that exposed it.

---

## 8. Calibration

- **First pass:** double-score 100% of items. Agreement cannot be estimated from items only one person scored.
- **Steady state:** double-score 10–20% at random, plus every item that has ever split and every control.
- **Controls:** include known-good and known-bad segments in each batch — one clean D009 retention, one deliberate D009 violation, one natural-plus-TTS segment. A reviewer who cannot separate the controls is not calibrated for that batch.
- **Statistics:** report unweighted Cohen's κ, linear and quadratic weighted κ, the raw disagreement table, n, exclusions, and the score distribution. `KAPPA-SCRIPT.py` produces all of these; the reproduction command is in `ADJUDICATIONS-ASR-3.md` and `README.md`.
- **Threshold:** set the acceptance threshold **before** scoring. Do not import `0.80` as a universal pass mark. On 20 items a wide confidence interval is expected; a high κ can still be fragile.
- **Drift:** re-run the controls after any rubric edit, any new scorer, or any change to the item file.

---

## 9. Known limits

- **Small n.** Twenty synthetic items cannot support stable per-type estimates. Report the set as a seed, not a benchmark.
- **Constructed data.** Transcripts and millisecond offsets are synthetic teaching values, not real recordings. No audio is hosted with this set.
- **Ordinal scale.** Do not compute means and treat them as interval measurements without disclosure.
- **No production authority.** This is a personal R&D methodology prototype, not a client production system; it has not been certified or audited.
- **Out of scope.** This rubric does not evaluate privacy handling, legal compliance, or speaker identity claims.
