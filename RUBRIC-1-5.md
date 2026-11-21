# RUBRIC-1-5.md — 1–5 scoring rubric for Japanese evaluation items

**Version:** 1.1-draft (2026-11-19: §3 examples realigned with per-item keys + precedence line; owner-approved. 1.0 = 2026-11-18 draft)
**Applies to:** responses to the 20 items in `SAMPLE-SET-JA-20.md`
**Status:** personal R&D methodology prototype, not a client production system

## 0. Scope and unit of analysis

This rubric scores **one response to one item**. It does not score a model, a vendor, a dataset, or a prompt. One response receives one integer from 1 to 5 and one written rationale.

The scale is ordinal. A 4 is not "twice" a 2, and the distance between 3 and 4 is not assumed to equal the distance between 1 and 2. Do not compute means across items and present them as an interval-scale score without saying so. If a summary number is needed, report the distribution and the median, and report disagreement alongside it.

A score is not a verdict on whether the response is "good writing." A fluent, polite, confident answer that misses the item's must-have is a low score.

## 1. Scoring procedure

1. **Pin the version.** Record the item file hash and the response hash. A score without a version is not reproducible.
2. **Read the item.** Prompt, reference judgment, and `judgment_rubric_hits`.
3. **Apply the gates** (§1.1, §1.2).
4. **Audit the must-haves.** Mark each rubric hit pass or fail. Do not convert the hits into a point total.
5. **Assign the band** using §3.
6. **Write one rationale sentence.** It must name the decisive dimension (D1–D5) and the decisive evidence. "Good" and "natural" are not evidence; quote the relevant fragment.
7. **Record.** Score, rationale, item version, reviewer ID, date. No score is entered without a rationale.

Do not average dimension scores. A response that is excellent on D3 and fails D1 is not a 3.5; it is a failed response with good prose.

### 1.1 G1 — Honesty gate

If the response fabricates a fact, a source, a citation, a completed action, or a **false verification claim** (for example, claiming "within the 250-character limit" when the draft is over it), the maximum score is **2**.

If the fabrication is the centerpiece of the answer — an invented policy, a date presented as confirmed, a claim that a message was sent — the score is **1**.

A confident tone never earns a point. Hedging does not repair a fabrication; the fabrication must be removed.

### 1.2 G2 — Hard-constraint gate

Length, format, language, output type, and explicit prohibitions ("do not use keigo," "do not translate this line") are pass/fail. A failed hard constraint blocks band 5 and band 4. Assign 3 or lower according to the item key and the severity of the miss: 3 when the judgment is otherwise intact and the artifact is recoverable, 2 or 1 when the constraint is the item's central purpose and the artifact is unusable. G2 does not create the score by itself; it removes the top two bands.

A response that violates a hard constraint **and** falsely claims compliance is handled by G1 (maximum 2).

## 2. Dimensions

The dimensions describe what to look at. They are not weights.

### D1 — Instruction compliance

Does the response do what the prompt asks, in the requested form, length, language, and register? Check every explicit constraint separately. "Mostly followed" is a failure on the constraint that was not followed.

### D2 — Factual and numerical accuracy

Are the arithmetic, dates, quantities, customs, and quoted facts correct? One error that changes the answer caps the response at 2. A correct final number with a wrong intermediate step is not a 5; it is a 4 at best, and a 2 if the step reveals a method that would fail on a different input.

### D3 — Language quality and register

Would a native professional send this text in this situation? Check honorific classification (尊敬語 / 謙譲語 / 丁寧語), double keigo, `させていただく` overuse, and whether the register matches the relationship. Naturalness is judged against the situation, not against a style preference.

### D4 — Ambiguity and missing-information handling

Does the response recognize the ambiguity the item was built around? Does it preserve the ambiguity when the prompt requires preservation, resolve it only with a stated and defensible assumption, and ask only when the missing information is decision-critical? Inventing a referent is a D4 failure and often a G1 failure.

### D5 — Explanation and justification

Is the stated reason correct, specific, and proportionate? A correct answer with a wrong reason cannot be a 5. If the task is to explain (as in JA-013, JA-017, JA-018, JA-019), a wrong or missing reason is a core failure, not a cosmetic one.

## 3. Bands

Each band below has an **inside** example (clearly belongs) and a **just-outside** example (looks close but belongs one band lower). The examples cite items from `SAMPLE-SET-JA-20.md`; the quoted Japanese is illustrative, not a required verbatim output. Where an example and a per-item key differ, the per-item key governs.

### Band 5 — Ready to use

Every must-have passes. The explanation is correct and specific. No edit is needed beyond personal preference. A reviewer could publish or send the response as-is.

- **Inside — JA-003.** The response identifies `伺わせていただきます` as double keigo, rewrites it to `弊社の田中が、明日そちらへ伺います。`, and names the mechanism: `伺う` is already humble, so `させていただく` stacks a second humility marker. All three hits pass; the rationale teaches why the fix is right.
- **Just outside — JA-003 (→4).** The correction is right, but the rationale is only `二重敬語なので冗長です。` It does not name 謙譲語 or the stacking mechanism. The response is usable, but the explanation would not let a junior reviewer reproduce the judgment; that is one non-core gap.

### Band 4 — Usable with a minor edit

Every core must-have passes. One non-core gap remains: a terse rationale, an unstated but harmless assumption, a missing optional polish. A careful editor can fix it in one pass without re-deciding the item.

- **Inside — JA-006.** The response reports 100 → 138, +38, and correctly says `5ポイント増`. It omits the check that `5%増` would be 26.25%, so the rationale is thinner than the item's D5 hit asks. The core numbers pass; one non-core gap.
- **Just outside — JA-006 (→3).** The same numbers, but the answer selects `5%増`. That is not a thinner explanation; it is a wrong label on the exact metric the item was built to test. A core must-have fails.

### Band 3 — Needs substantive revision

The core judgment is present but incomplete: one must-have is missing, or a secondary error appears that a careful reader must fix before use. The response is not ready, but it is not a failure of understanding either.

- **Inside — JA-015.** The response recognizes both readings and drafts a confirmation, but the draft is `確認させていただければと思います` with no actual question and no fallback. The core judgment is present; the artifact needs a substantive rewrite.
- **Just outside — JA-015 (→2).** The response recognizes both readings, then drafts `ご承知おきください。来週から作業を進めます。` — it commits to work on the assumption of acceptance. The analysis cannot cure the artifact; that is band 2.

### Band 2 — Not usable

A core must-have fails, or the response is wrong in a contained way that a careful reader would catch. The failure is real but local: a partial correction, a wrong pick with a plausible rationale, a definitive answer to an item that required a question. A G1 fabrication that is not central also lands here.

- **Inside — JA-008.** The response fixes `おっしゃられた` but misses both `させていただく` issues. The partial fix is real, and the response makes no claim that the sentence is clean.
- **Just outside — JA-008 (→1).** Same item, but the response also asserts `この文に誤りはありません。` after changing nothing. That is not a contained miss; it inverts the task and would leave a known error in an internal report to a senior manager.

### Band 1 — Misleading

The response inverts a core judgment, fabricates the centerpiece, or would cause a materially wrong action if used as-is. This is not "a low-quality answer"; it is an answer that a reader must not follow.

- **Inside — JA-002.** The response rewrites `必ずしも全員が参加する必要はありません` as `全員が参加しなくてよい。` This inverts partial negation into total negation. A reader would act on the wrong instruction about who must attend.
- **Inside — JA-015.** The response recognizes both readings, then drafts `今回は見送りという前提で、社内の準備を止めておきます。` It asserts a refusal the counterparty did not state; sending it ends the negotiation. Band 1 (consistent with ADJ-2026-002).
- **Just outside — JA-019 (→2).** The response selects ③ instead of ②. The answer is wrong, but it does not invert the meaning of the sentence or invite a harmful action: a careful reader would catch the wrong pick. The failure is contained, which is band 2, not band 1.

### Band summary

| Band | One-line test | Typical defect |
|---|---|---|
| 5 | Send as-is | None |
| 4 | One-pass edit | Non-core gap |
| 3 | Re-decide one element | Missing must-have or secondary error |
| 2 | Do not use | Core failure, contained |
| 1 | Do not follow | Inversion, central fabrication, wrong action |

## 4. Item-specific overrides

The bands are general. The item's `judgment_rubric_hits` are specific. When they conflict, the item-specific hit wins, because it was written before the response was seen.

Two rules keep this from becoming ad hoc:

1. **A hit must be written before scoring.** Adding a must-have after seeing the response is not scoring; it is rationalization. If a reviewer believes a new hit is needed, the case goes to adjudication and the rubric is amended for the next version (§5.9).
2. **A hit must be checkable.** `D2: 4,724円` is checkable. `D3: 丁寧` is not. Rewrite vague hits before the first scoring pass.

**Core vs non-core, v1.0.** The band definitions use "core" but v1.0 does not formalize it. The working reading, applied in `ADJUDICATIONS-3.md` ADJ-2026-003, is: a hit is core when failing it changes the item's answer or the action a reader would take; it is non-core when the action survives and only the explanation or a transparency note is missing. When in doubt, treat the hit as core. Formalizing this is a v1.1 amendment, not a retroactive rule.

## 5. Adjudication when two reviewers disagree

The purpose of adjudication is not to produce agreement. It is to produce a **defensible record** of why one reading prevails, or to record that the rubric cannot yet decide.

### 5.1 Trigger

Adjudicate when any of the following is true:

- The two scores differ by 2 or more points.
- One reviewer applies G1 or G2 and the other does not.
- Both reviewers give the same band but cite different must-haves.
- A reviewer cites a rule that is not in this document or the item's hits.

A one-point gap with the same cited must-have may be logged without full adjudication; it still counts in the agreement statistics.

### 5.2 Freeze the evidence

Collect, before discussion:

- item ID and item file hash;
- response text and hash;
- both score sheets, each with its rationale;
- the reviewer's cited dimension and must-have;
- any control items the reviewer scored in the same batch.

No new evidence is introduced after this point. If the response was edited, it is a new response and a new scoring event.

### 5.3 Steelman restatement

Each reviewer restates the other's position in one sentence, without rebuttal. If a reviewer cannot restate the other's position, the disagreement is probably about the item or the rubric, not the response. Fix that first.

### 5.4 Must-have audit

Build a pass/fail table for every `judgment_rubric_hits` entry. This resolves most disagreements, because it moves the argument from adjectives to checks.

| Hit | Reviewer A | Reviewer B | Evidence |
|---|---|---|---|
| D3: corrects `伺わせていただきます` | fail | pass | A quotes the primary sentence; B quotes an alternative in a note |

### 5.5 Boundary comparison

Compare the response to the band's **inside** and **just-outside** examples in §3. Ask: which example is this response closer to, and on which specific feature? "Closer to 4 than to 3" is not enough; name the feature.

### 5.6 Rule priority

Apply the rules in this order. A lower rule cannot override a higher one.

1. G1 honesty gate.
2. G2 hard-constraint gate.
3. The item's explicit must-haves.
4. The band definition.
5. The dimension notes.
6. Reviewer preference or house style.

A reviewer's preference for a different but equally correct phrasing is not a scoring ground. If it is not written in the rubric, it is inadmissible.

### 5.7 Decide, do not average

Choose the band supported by the highest-priority rule that is actually in dispute. Do not split the difference. A 2 and a 4 do not become a 3 because 3 is the midpoint; they become whichever band the rule supports.

If two bands remain defensible after the audit, escalate to a third reviewer who scores blind to the first two. If the third score does not resolve the split, mark the item **indeterminate**, exclude it from the agreement statistics, and open a rubric defect. Forced consensus is worse than a recorded gap: it hides the defect and poisons the next calibration.

### 5.8 Record

Every adjudication produces a note with five parts:

1. **Point of disagreement** — the smallest disputed claim, not the whole item.
2. **Both grounds** — each reviewer's strongest case, steelmanned.
3. **Rule citation** — the exact section, band, or must-have.
4. **Ruling** — one band, with the losing reviewer's error named.
5. **Reasoning chain** — why the rule applies to this response, step by step.

The three worked examples in `ADJUDICATIONS-3.md` follow this structure. They are the template.

### 5.9 Amend, do not retrofit

If the split exposed a missing rule, amend the rubric **after** the ruling and **for the next version**. Do not apply the new rule retroactively to the case that exposed it; that would make the record look cleaner than the judgment was.

Record the amendment, bump the version, and re-score the affected items with both reviewers. A rubric that never changes is either perfect or unused.

## 6. Calibration

- **First pass:** double-score 100% of items. You cannot estimate agreement from a sample that was never independently scored.
- **Steady state:** double-score 10–20% at random, plus every item that has ever split.
- **Controls:** include known-good and known-bad responses in each batch. A reviewer who cannot separate the controls is not calibrated for that batch, regardless of their agreement with the other reviewer.
- **Statistics:** report unweighted Cohen's κ and quadratic weighted κ, plus the raw disagreement table. `KAPPA-SCRIPT.py` produces both. Report the number of items, the number excluded, and the score distribution; a κ without those is unreadable.
- **Threshold:** set the acceptance threshold **before** scoring. Do not import 0.80 as a universal pass mark; it is a convention, not a law. For a small seed set, a wide confidence interval is expected, and a high κ on 20 items can still be fragile.
- **Drift:** re-run the controls after any rubric edit, any new scorer, and any change to the item file. A shift in control performance invalidates the batch before the agreement number is computed.

## 7. Known limits

- **Small n.** Twenty items cannot support stable per-type estimates. Report the set as a seed, not a benchmark.
- **Single author.** The reference judgments are one person's reading. Native-speaker review and a second author are still required.
- **Ordinal scale.** Do not compute means and treat them as interval measurements without disclosure.
- **Japanese-specific examples.** The frame may transfer to other languages; the examples do not.
- **No safety or PII scope.** This rubric does not evaluate harmful content, privacy handling, or legal compliance. Do not use it for those decisions.
- **Prototype status.** This is a personal R&D methodology prototype, not a client production system. It has not been certified, audited, or validated in a production environment.
