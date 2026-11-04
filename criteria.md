# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->

Across three repeated trials of 10 human-written texts, no more than 1 text per trial is labeled high-confidence AI.


**Why this target:**

 A false accusation is more harmful than missing some AI-generated text, so the system should prioritize protecting human writers.


---

## 2.

<!-- Your criterion. -->

The average combined score for 10 clearly AI-generated texts is at least 0.20 higher than the average score for 10 human-written texts in each of three trials.


**Why this target:**

The detector should show a meaningful distinction between clearly different sources.


---

## 3.

<!-- Your criterion. -->

At least one test input produces each of the three labels, `human`, `unsure`, and `ai`, across the evaluation tests.


**Why this target:**

Every label represents a different user-facing outcome, so none should be impossible to reach because of incorrect thresholds.


---

## 4.

<!-- Your criterion. -->

For 5 submitted appeals, every appeal creates an append-only audit-log entry containing the content ID, creator ID, reasoning, and `under_review` status.


**Why this target:**

Writers need evidence that their appeal was received, and the original decision must remain available for accountability.


---

## 5.

<!-- Your criterion. -->

Requests with missing, empty, or overlong text return a clear client-error response, make no detector decision, and create a rejection entry in the audit log in all three trials.


**Why this target:**

Bad input should not crash the service or produce a misleading AI/human judgment. Logging rejected requests also makes failures visible for later diagnosis.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
