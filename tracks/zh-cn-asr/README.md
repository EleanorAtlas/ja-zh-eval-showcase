# Track B — zh-CN Mandarin ASR Forced-Alignment & Disagreement-First Adjudication

A public calibration track for teams that run Mandarin speech transcription, forced alignment, or multimodal data QA. It shows how to turn "two annotators disagree about a boundary" into a written, reproducible decision — and where the tempting fix is the wrong one.

[← Back to the main Multilingual & Multimodal Eval Calibration Hub](../../README.md) · [Start a scoped conversation](mailto:eleanoratlas2502@gmail.com)

## Why this track exists

The most expensive silent failure in Chinese ASR forced alignment is not a bad transcript. It is a **good boundary destroyed to clear a cosmetic warning**: an annotator stretches an utterance tail to swallow a minor gap, cuts the next utterance's initial consonant, and breaks a previously agreed word edge. A second, equally common failure is marking an entire recording `synthetic: true` because a TTS voice is audible in the background — and throwing away the real human speech underneath.

This track publishes the written rules and the worked rulings for both failures. It is a personal R&D methodology prototype, published so the reasoning can be inspected — not a certified benchmark or a client production system.

## What is in this directory

| File | Role |
|---|---|
| `SAMPLE-SET-ASR-20.jsonl` | 20 fully constructed, de-identified Mandarin segments. Text plus millisecond offsets, warning codes, three-dimension questionnaire, and gold actions. No audio. |
| `RATINGS-ASR-20.csv` | Two independent 1–5 integer scores per item (`item_id,rater_a,rater_b`) for the zero-dependency κ audit. |
| `RUBRIC-ASR-ALIGN.md` | The 1–5 ordinal calibration scale, Protocol D009 (disagreement-first over `Other`, `R <= 3`), the 30/50 ms tolerance matrix, four task variants, the three-dimension questionnaire, and the Gate G1-ASR authenticity veto. |
| `ADJUDICATIONS-ASR-3.md` | Three full rulings: `D009` retention vs boundary destruction; a `-22 ms` tail inside tolerance paired with a missed `180 ms` real overlap; and natural voice plus in-car TTS correctly scored `synthetic: false`. Includes the κ reproduction command and interpretation. |

All item content is synthetic teaching data. Chinese transcript fragments, `start_ms` / `end_ms` / `delta_ms` values, and warning codes are constructed for this track; they are not client transcripts and do not correspond to any real recording.

## Zero-audio, metadata-only by design

No audio is hosted here — not in this directory and not behind a link. The entire adjudication problem is made checkable with **text + millisecond offsets + warning codes + questionnaire values**:

- a boundary is disputed at the level of `delta_ms`, so the number can be judged against a tolerance row without streaming a file;
- a warning (`WARN_MINOR_GAP`, `WARN_SHORT_SEGMENT`, `WARN_LONG_SEGMENT`) is a label to retain or clear, not a waveform the reader must fetch;
- a questionnaire value (`multiSpeaker` / `overlap` / `synthetic`) is a recording-level decision recorded as data.

This keeps the sample set legally clean (no voice data, no speaker identity, no third-party audio) and lets a reviewer reproduce a ruling from the text alone. It also reflects the actual discipline: the pre-filled ASR text is a **timeline locator**, never authority over what was said. Numbers, code-mixed English, singing, and medical terms are not "fixed" by semantic fluency.

The trade-off is stated plainly: a reader cannot verify acoustics from metadata. The rubric therefore requires any real edit to cite an acoustic observation, and it marks unverifiable guesses as gate failures rather than pretending the text could settle them.

## The four rules a reader should take away

1. **`disagreement` outranks cosmetic `Other`.** If clearing a gap/short/long warning would damage a locked `agreement` boundary or create a new disagreement, keep the boundary, keep the warning, and log `RETAIN_VERIFIED_OTHER` with `R <= 3`. Moving the boundary for a clean warning list is `REJECT_D009_VIOLATION` → `Score 1`.
2. **Tolerance depends on boundary class.** Intra-utterance word boundaries `±30 ms`; utterance onset/offset `±50 ms` (never clip the initial consonant breath or the final vowel coda); short-pause bridges `<= 120 ms` `±30 ms`. Inside tolerance is `NO_EDIT`.
3. **Overlap is sustained co-voicing, not any gap.** `> 120 ms` of coexistence is overlap; adjacent turn-taking with a `<= 120 ms` bridge is not. Warning codes are hints to inspect, not automatic values.
4. **Audible TTS does not make a natural voice synthetic.** Natural human speech plus a background TTS source → `synthetic: false`; keep the human transcript and mark the non-target span. Marking `true` and discarding the recording is the false-kill this track is built to prevent.

## Reproduce the agreement statistic

The shared reporter is a single zero-dependency Python 3.8+ script at the repository root. From this directory:

```bash
python ../../KAPPA-SCRIPT.py RATINGS-ASR-20.csv
```

It reports unweighted Cohen's κ, linear and quadratic weighted κ, the confusion matrix, score distributions, the difference summary, and the item-level disagreement table. For machine-readable output, add `--json`; to verify the script itself, run `python ../../KAPPA-SCRIPT.py --selftest`.

Read every κ together with n, exclusions, the score distribution, and the disagreement table. On 20 items the coefficient is fragile, `0.80` is a convention rather than a law, and the threshold should be fixed before scoring. The three adjudication cases are the ones designed to split reviewers; if nobody disagrees on them, re-check the controls before trusting the number.

## Collaboration: 1-Week ASR IAA Calibration Pilot

If your team runs Mandarin ASR transcription, forced alignment, or speech-data QA, this track is the visible part of a fixed-scope engagement:

- **1-Week ASR Annotation & IAA Calibration Pilot** — a shared frozen fixture set, a blinded double-scoring pass with unweighted and weighted κ, and a written adjudication of every material disagreement. Deliverables: the rubric tuned to your boundary policy, a calibration report with n / exclusions / distribution / item-level table, and a D009-based conflict-priority protocol your annotators can apply without a supervisor.
- **Fractional Speech QA Adjudicator** — ongoing, fixed-scope review of disputed segments and questionnaire edge cases, delivered on the record, including findings that are inconvenient for the delivery.

Both routes stay inside a written scope agreed before work starts. This is one evaluator, not an agency or a lab; when a scope exceeds what one person can honestly cover, that is said before the scope is agreed.

Write to **[eleanoratlas2502@gmail.com](mailto:eleanoratlas2502@gmail.com)** with the task, the approximate number of segments, the boundary policy you currently use, and the decision the calibration needs to support. If the fit is wrong, I will say so.

---

Related: [Main Hub](../../README.md) · Rubric: [`RUBRIC-ASR-ALIGN.md`](RUBRIC-ASR-ALIGN.md) · Rulings: [`ADJUDICATIONS-ASR-3.md`](ADJUDICATIONS-ASR-3.md)

© 2026 Eleanor Chan. Independent evaluation practice. Sample set and rubric text licensed MIT.
