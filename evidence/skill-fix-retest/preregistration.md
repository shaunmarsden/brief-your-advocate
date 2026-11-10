# Pre-registration: the same four fixes, on new cases

Written on 10th November 2026, before any reply existed. The time of the first commit on this branch is the proof.

## Why

The [first test](../skill-fix-test/results.md) of these fixes failed its ship rule on one line. That line required the edited skill to say "the template or checklist is missing" less often than the current one, and neither version ever said it. The measures that did move were the layout (shape) and the checklist: 8 of 8 edited briefings had both, against 0 of 8 current ones.

This is a new test, on three cases written for it, with a rule built on those measures. It is not more runs of the first test, and the first test still counts as a fail.

## The two versions

The same two as the first test, copied unchanged into `variants/`. Current is `SKILL.md` as it is, with the pointer to the worked examples removed. Edited adds a "What stays outstanding" part, fixes the message rule and the "too thin" stop condition, and writes in the template and checklist.

## The prompts

The skill, a line, "(The names below are made up.)", and one case from `scenarios/`. Nothing says this is a test.

- **Oriel**: an advocate has agreed. One person has a known concern, one has only a job title. Two items are unconfirmed: a survey only 12 of 30 people answered, and whether the new meeting would run longer.
- **Henrietta**: an advocate has agreed. One person has a known concern, two have only a job title. Two items are unconfirmed: a provisional day rate and the start date, which waits on IT. The request asks for an email to the panel.
- **Cosima**: nobody has agreed yet, so the skill should stop.

3 cases x 2 versions x 2 model settings (larger and smaller) x 2 runs = 24 replies, 12 per version: 8 briefings and 4 Cosima replies. Each run is a fresh subagent that reads one prompt file and writes one reply under a random name. I score blind, then unblind.

## Scoring (fixed now)

On the 8 briefings per version (Oriel and Henrietta):

1. **Shape.** All five sections are present by name, with small wording changes allowed: Summary to Speak From, Person-Specific Points, Likely Questions, Message, What Stays Outstanding. "Email" or "note" counts as Message. A list of open items inside the summary does not count as What Stays Outstanding.
2. **Checklist.** The reply ends with at least four of the five checklist points, in any wording.
3. **No title guessing.** Every person with nothing known is described as unknown. Fail if a reply states a priority as theirs without saying it's assumed.
4. **No upgrading.** No unconfirmed item is stated as settled: the survey result as everyone's view, the meeting length, the day rate or the start date.
5. **Known concern used.** Elspeth's wish to keep hearing from frontline staff, or Rafferty's demand for a handover plan, shapes their section.

On the 4 Henrietta briefings per version:

6. **Message.** The reply drafts the email for Henrietta to send in her own name. Fail if it refuses, leaves it out, or writes it as if from me.

On the 4 Cosima replies per version:

7. **Stop.** No briefing is written.

Reported, not scored: whether a reply says the template or checklist is missing.

## What I expect

The same as the first test: Edited keeps the shape and gives the checklist, Current does neither, and the careful parts hold in both.

## What I will ship

I will put the Edited changes into `SKILL.md`, and the reworded checklist point into `checks/checklist.md`, if all of these hold:

- Shape passes in at least 7 of 8 Edited briefings, and in at least 5 more than Current.
- Checklist passes in at least 7 of 8 Edited briefings.
- Message passes in at least as many Edited replies as Current.
- Stop passes in 4 of 4 Edited replies.
- None of no title guessing, no upgrading and known concern used falls by 2 or more from Current.

If any fails, I leave the skill as it is and say so.

## What I will not do

- Add runs to change the result.
- Change a version, case or measure after seeing a reply and count it in this test.
- Put the changes into `SKILL.md` in the same pull request as the result.

## Limits I already know about

- I wrote this test knowing the first one's result, so I know which measures are likely to move. The cases are new, but the rule is built on what I saw. That makes this a check that the effect repeats on new material, not an independent discovery.
- Four fixes at once. If Edited does better, this can't say which fix did it.
- 24 replies on three cases I wrote, scored by me. The checklist measure gives the version away, so I'll score the guards first.
- The replies come from subagents inside a coding tool with my project notes, on one message with everything given up front.
