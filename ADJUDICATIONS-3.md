# ADJUDICATIONS-3.md — Three disagreement rulings

**Version:** 1.0 (draft)
**Companion to:** `RUBRIC-1-5.md` §5, `SAMPLE-SET-JA-20.md`
**Status:** personal R&D methodology prototype, not a client production system

## Note on these cases

The three cases below are **constructed** for this document. The responses under review were written to illustrate specific failure modes; they are not transcripts from a model run, a client engagement, or a public evaluation. The item IDs refer to `SAMPLE-SET-JA-20.md`. Each case follows the five-part record required by `RUBRIC-1-5.md` §5.8, with the amendment note from §5.9 added.

The adjudicator's job here is not to be nice to either reviewer. It is to name the smallest disputed claim, apply the highest-priority rule that actually covers it, and leave a record that a third person could reproduce.

---

## ADJ-2026-001 — Hard length limit plus a false compliance claim

**Item:** JA-012 (婉曲な断り, 150–250 characters)
**Scores under review:** Reviewer A = 2; Reviewer B = 4
**Gap:** 2 points → adjudication required (§5.1)

### Response under review (ja)

> お世話になっております。来週金曜日の打ち合わせのご依頼、ありがとうございます。大変恐縮ですが、社内の承認手続きが間に合わず、今回は開催が難しい状況です。代わりに、再来週以降で候補日を複数いただけますと幸いです。ご意向に沿えるよう調整いたしますので、引き続きよろしくお願いいたします。なお、当日は別件の対応が入っており、準備の時間が確保できません。次回はぜひ、弊社の新しい体制もご紹介させてください。その際は、今回お話しできなかった内容も含めてご説明いたします。ご多忙のところ恐れ入りますが、ご検討いただけますと幸いです。何卒ご理解のほど、よろしくお願い申し上げます。
>
> （250字以内に収めました）

### 1. Point of disagreement

Whether the response is a **usable draft with a minor overrun** (B) or a **failed constraint plus a false verification claim** (A). The reviewers agree on the content quality; they disagree on what the closing note does to the score.

### 2. Reviewer A — score 2

- The prompt sets a hard ceiling of 250 characters. The response body is 283 characters.
- The closing note says `250字以内に収めました`. That statement is false. It is not a stylistic flourish; it is a verification claim about the response itself.
- Under G1, a false verification claim caps the score at 2. Under G2, the length hit fails. Either route is enough to remove band 4 and band 5.
- The content is otherwise correct, and the false claim is not the centerpiece, so the floor is 2, not 1.

### 3. Reviewer B — score 4

- The response contains all five required elements: thanks, apology, the real reason (internal approval), an alternative (dates from the week after next), and continued intent.
- It does not invent a reason. It does not blame the counterparty. The register is appropriate.
- The overrun is small enough that a single edit could bring it under 250 without losing an element: tighten the two closing sentences. Under band 4, that is exactly "usable with a minor edit."
- The self-check note is careless, but B reads it as an annotation, not as part of the deliverable.

### 4. Rule citations

- `RUBRIC-1-5.md` §1.1 (G1): a false verification claim — "within the 250-character limit" when the text is longer — caps the score at 2.
- `RUBRIC-1-5.md` §1.2 (G2): length is a hard constraint; the item's D1 hit lists 150–250 characters.
- `RUBRIC-1-5.md` §3, band 4: "every core must-have passes"; band 2: "a core must-have fails."
- `SAMPLE-SET-JA-20.md` JA-012, rubric hits: D1 (150–250 characters), D2 (no false reason), D3, D5.

### 5. Ruling

**Score: 2.**

### 6. Reasoning chain

1. The 250-character ceiling is not an editorial preference. It is an explicit, checkable must-have in the item's D1 hit. The response exceeds it.
2. The closing note is part of the response. A reviewer cannot carve it out as "just an annotation" after the fact: the note is the only place where the response checks its own compliance, and it checks it wrongly.
3. G1 applies. The claim `250字以内に収めました` is false. The cap is 2 regardless of how good the email body is.
4. B's proposed fix — "tighten the two closing sentences" — may well work, but it is a rewrite of the submitted response, not a reason to score the submitted response higher. G1 is evaluated on what was sent, including the false check. A reviewer cannot repair the artifact and then score the repaired version.
5. The ruling is 2, not 1. The response does not invert the task, does not fabricate an external fact, and the content is recoverable by rewriting. The false claim is not the centerpiece; it is a bad self-check attached to a good draft.
6. The ruling is 2, not 4. Band 4 requires every core must-have to pass. D1 fails, and G1 independently caps at 2. Content quality cannot lift a gated response.

### 7. Record and amendment

- **Losing reviewer:** B. The error is treating a hard constraint as a minor edit and treating a false self-check as outside the response.
- **Rubric action:** no new rule is needed; G1 already names false verification claims. Add JA-012's closing-note pattern to the G1 examples so the next reviewer sees it before scoring. Version 1.1, no re-score required for this item beyond the recorded 2.
- **Note for the item owner:** the reference email is comfortably under 250 characters; the overrun here comes from added closing sentences, not from the five required elements. If the ceiling changes, re-measure the reference and keep at least 20 characters of headroom.

---

## ADJ-2026-002 — The artifact presumes the answer

**Item:** JA-015 (「結構です」の両義)
**Scores under review:** Reviewer A = 3; Reviewer B = 1
**Gap:** 2 points → adjudication required (§5.1)

### Response under review (ja)

> 「結構です」は承諾にも辞退にも取れます。商談の文脈では、辞退の意味で使われることが多い印象です。確認の返信案はこちらです。
>
> 「お見積もりの件、今回は見送りとのこと、承知いたしました。またの機会によろしくお願いいたします。」

### 1. Point of disagreement

Whether the correct analysis in the first two sentences can hold the score at 3, or whether the drafted reply — which treats the ambiguous `結構です` as a decline — pulls the response to 1.

### 2. Reviewer A — score 3

- The response correctly identifies both readings. That is the item's central trap, and it is not missed.
- It also gives a concrete next step, which the prompt asks for (`どう確認しますか`).
- The drafted reply is too presumptuous, but it is one edit away from a neutral confirmation: change `今回は見送りとのこと` to `進めさせていただいてよろしいでしょうか`.
- Under band 3, the core judgment is present and the artifact needs substantive revision. That is a 3.

### 3. Reviewer B — score 1

- The only sendable artifact is the reply. The analysis is commentary; the reply is what the user would put in the mail.
- The reply states `今回は見送りとのこと` as if the counterparty had said it. They did not. The response converts an open question into a decision and attributes that decision to the other side.
- If sent, the reply closes a live negotiation on a guess. That is the band 1 definition: an answer that would cause a materially wrong action if used as-is.
- The analysis paragraph does not cure the artifact. A reader who trusts the analysis will still send the wrong mail.

### 4. Rule citations

- `RUBRIC-1-5.md` §3, band 1: "inverts a core judgment … or would cause a materially wrong action if used as-is."
- `RUBRIC-1-5.md` §1.1 (G1): a fabricated commitment attributed to the counterparty, when it is the centerpiece of the artifact, is a 1.
- `RUBRIC-1-5.md` §3, band 3: "the core judgment is present but incomplete … a secondary error that a careful reader must fix."
- `RUBRIC-1-5.md` §2, D1: the response must do what the prompt asks, in the requested form. The prompt asks how to confirm, not how to concede.
- `SAMPLE-SET-JA-20.md` JA-015, rubric hits: D4 (both readings), D1 (do not presume either), D3 (neutral confirmation).

### 5. Ruling

**Score: 1.**

### 6. Reasoning chain

1. The prompt's deliverable is a confirmation strategy. The response's deliverable is the drafted reply. When an item produces a user-facing artifact, the artifact governs; commentary is D5 evidence, not a substitute for D1.
2. The reply asserts `今回は見送りとのこと`. That proposition is not in the source. It is a fabricated commitment attributed to the counterparty. The fact that the analysis warns about ambiguity does not make the assertion true.
3. The consequence is material: sending the reply ends the negotiation. Band 1 is written for exactly this — an answer a reader must not follow.
4. A's proposed one-line fix is real, but it changes the speech act of the artifact, not a word choice. Scoring the response as a 3 would require treating a different reply — one that asks rather than concedes — as a minor edit of this one. It is not.
5. The ruling is 1, not 2. Band 2 covers a contained failure that a careful reader would catch. A careful reader might catch this, but the artifact is designed to be sent without a second reader. The action consequence is the distinguishing feature.
6. The ruling is 1, not 3. A 3 would reward the analysis while ignoring what the user would actually send. That is the failure mode this case is meant to expose.

### 7. Record and amendment

- **Losing reviewer:** A. The error is scoring the commentary instead of the artifact.
- **Rubric action:** add an explicit "artifact governs" rule to §2 (D1) and §4: when the item asks for a user-facing text, the sendable text is the primary object; analysis is scored under D5 only. Version 1.1. Re-score JA-015 with both reviewers under the new text; the expected score remains 1.
- **Note for the item owner:** the reference judgment should include a neutral reply template, so a reviewer has a concrete positive example of "confirm without presuming."

---

## ADJ-2026-003 — A standard abbreviation and an unstated trade-off

**Item:** JA-016 (40-character summary, proper nouns retained)
**Scores under review:** Reviewer A = 5; Reviewer B = 3
**Gap:** 2 points → adjudication required (§5.1)

### Response under review (ja)

> 2026年4月から都内3拠点で平日・事前予約制の中小企業向け無料相談窓口を開設（39字）

### 1. Point of disagreement

Whether `都内` satisfies the instruction to retain proper nouns (`固有名詞は必ず残す`), and whether the absence of a note about the compression is a must-have failure or a minor gap.

### 2. Reviewer A — score 5

- The summary is 39 characters, under the 40-character ceiling.
- Every required element is present: 2026, April, three sites, weekdays, advance reservation, SMEs, free, and Tokyo.
- `都内` is the standard shorthand for `東京都内`. In a Tokyo-context sentence, no reader would understand a different prefecture. No information is lost.
- The response even reports its own length, which is a useful check. Under band 5, this is ready to use.

### 3. Reviewer B — score 3

- The instruction does not say "retain the referent"; it says "retain the proper nouns." `東京都` is the proper noun; `都内` is a substitution.
- The response silently makes that substitution. It does not say that `東京都内` would push the summary to 41 characters, and it does not ask whether the abbreviation is acceptable.
- The item's D5 hit asks for an explanation of the length-versus-information trade-off. That explanation is absent.
- Under band 3, one must-have is missing. The summary is otherwise correct, so it is not a 2.

### 4. Rule citations

- `RUBRIC-1-5.md` §3, band 5: every must-have passes; band 4: every core must-have passes, one non-core gap; band 3: one must-have missing.
- `RUBRIC-1-5.md` §2, D2: facts and names must be correct; D5: the reason must be specific.
- `SAMPLE-SET-JA-20.md` JA-016, rubric hits: D1 (40 characters), D2 (2026年4月・3拠点・東京・中小企業・無料), D5 (the trade-off note).
- The item does not define whether an accepted abbreviation counts as "retaining" the proper noun. That is the gap this case exposes.

### 5. Ruling

**Score: 4.**

### 6. Reasoning chain

1. D2 asks whether the identifying fact survives. `都内` in this sentence identifies Tokyo unambiguously; the referent is preserved. B's claim that Tokyo is lost is not supported by the text. D2 passes.
2. D5 asks for the trade-off to be explained. The response gives the character count but not the trade-off: it does not say that `東京都内` would be 41 characters, nor that `都内` was chosen to fit. D5 fails.
3. Is D5 core or non-core? The rubric does not formalize "core"; §4 records the working reading: a hit is core when failing it changes the item's answer or the action a reader would take. D5 here changes neither: the summary still says the right thing, and the only loss is the note about how it fit. That makes D5 non-core. Band 4 is the band for "core must-haves pass, one non-core gap." Formalizing that reading is a v1.1 amendment.
4. A's 5 is wrong because D5 is an explicit hit and it fails. B's 3 is wrong because it treats a preserved referent as a lost fact. The ruling is 4 on the merits, not because 4 is between 5 and 3.
5. The case also shows why "do not average" needs care in practice: 4 happens to be the midpoint of 3 and 5, so the ruling can look like a compromise. It is not. The band came from a two-row audit — D2 pass, D5 fail. Had the audit produced two passes, the score would be 5; two fails, 3 or lower. The number follows the audit, not the distance between the reviewers.

### 7. Record and amendment

- **Losing reviewers:** A (over-credits, ignores D5) and B (misreads D2, treats abbreviation as information loss).
- **Rubric action:** amend JA-016's hits to define proper-noun retention as "the referent remains uniquely identifiable," add an explicit abbreviation policy (`東京都内 → 都内` is accepted, but the response must note the compression when the limit forces it), and formalize the working core/non-core reading in §4. Version 1.1. Re-score JA-016 with both reviewers; expected 4.
- **Item-owner choice:** if verbatim `東京都内` is required, raise the limit to 41 characters. That is a content change, not a scoring fix, and it must be versioned separately.

---

## What these three cases have in common

None of the three was resolved by finding a more eloquent way to say "I prefer 4." Each turned on a check that was written before the response was seen:

- **ADJ-001:** a hard constraint plus a false self-check.
- **ADJ-002:** the difference between the artifact and the commentary about it.
- **ADJ-003:** a missing definition at the item–rubric boundary, which became an amendment rather than a retroactive rule.

That is the point of publishing the adjudications. The rubric is not interesting when two reviewers agree. It is interesting when they do not, and the record still lets a third person see why the score is what it is.
