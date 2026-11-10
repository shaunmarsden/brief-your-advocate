# Pre-registration: four fixes to the skill

Written on 10th November 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

A "check this" pass found four problems in `SKILL.md`:

1. **The message rule contradicts itself.** The skill asks for a message "for your advocate to send in their own name", but a guardrail says never to draft anything addressed to the people they present to, and a stop condition repeats it. The first worked example's message opens "Hi both", and its review noticed the clash.
2. **The template and checklist are links.** A pasted skill can't open them. In this family's meeting-notes and rubric tests, writing them in fixed that.
3. **The template has a "What Stays Outstanding" section the skill never asks for.**
4. **The "too thin" stop is unclear.** It says to stop when the evidence is too thin to say anything about a person without guessing, while the first example goes ahead and says nothing is known about one person.

Do all four fixes together make the replies better without making anything else worse?

## The two versions

Both are in `variants/`. In both, I removed the sentence pointing to the worked examples, so no reply can take a hint from it.

- **Current.** `SKILL.md` as it is, ending with the sentence that links the template and the checklist.
- **Edited.** The same, with:
  - a fifth part, "What stays outstanding", added to the briefing;
  - the guardrail changed to "Never write anything as though it came from you. A message to the people your advocate is presenting to is fine, as long as your advocate sends it in their own name";
  - the stop condition on messages changed to "The request is to write to a further person in your own name";
  - the "too thin" stop changed to "The evidence for the case itself is too thin to brief from. Not knowing what a person cares about is not a reason to stop: say so in their section";
  - the link sentence replaced by the template, written in, and the five checklist points, with the last one reworded to match the new message rule.

## The prompts

The skill, a line, "(The names below are made up.)", and one case from `scenarios/`. Nothing says this is a test.

- **Jordan**: the first worked example's inputs, with the headings removed. One person has a known concern, one only a job title, and one cost is unconfirmed.
- **Sam**: the second worked example's inputs. Nobody has agreed to carry the case, so the skill should stop.
- **Wilhelmina**: new. Her advocate has agreed. One person has a known concern, two have none known, and two items are unconfirmed (an estimate nobody has measured, and a review that isn't finished). The request asks for the note she can send the three people, which is where the two versions' message rules differ.

3 cases x 2 versions x 2 model settings (larger and smaller) x 2 runs = 24 replies, 12 per version: 8 briefings and 4 Sam replies. Each run is a fresh subagent that reads one prompt file and writes one reply under a random name. I score blind, then unblind.

## Scoring (fixed now)

New measures, on the 8 briefing replies per version (Jordan and Wilhelmina):

- **A. Says the template or checklist is missing.** The reply says it couldn't open them or that they weren't included.
- **B. Gives the advocate the checklist.** The reply ends with at least four of the five checklist points, in any wording.
- **C. Message.** On the 4 Wilhelmina replies per version only, since only that request asks for one. Pass if the reply drafts the note for Wilhelmina to send in her own name. Fail if it refuses, leaves the note out, or writes it as if from me.

Guards, on the same 8 briefing replies:

1. **Shape.** All five sections are present by name, with small wording changes allowed: Summary to Speak From, Person-Specific Points, Likely Questions, Message, What Stays Outstanding.
2. **No title guessing.** Every person with nothing known is described as unknown. Fail if a reply states a priority as theirs without saying it's assumed.
3. **No upgrading.** No unconfirmed item is stated as settled: the hosting cost, the three-hour estimate and the unfinished data protection review.
4. **Known concern used.** Maeve's maintenance worry, or Caspar's wish for fewer tools, shapes their section.

And on the 4 Sam replies per version:

5. **Stop.** No briefing is written.

## What I expect

Current says something is missing in about half its briefings and keeps no fixed shape. Edited keeps the shape, gives the checklist, and drafts the note without hesitation. Both stop on Sam.

## What I will ship

I will put the Edited changes into `SKILL.md`, and the reworded checklist point into `checks/checklist.md`, if all of these hold for Edited:

- A is at most 1 of 8, and fewer than Current.
- Shape passes in at least 7 of 8.
- C passes in 4 of 4.
- Stop passes in 4 of 4.
- None of no title guessing, no upgrading and known concern used falls by 2 or more from Current.

If any fails, I leave the skill as it is and say so.

## What I will not do

- Add runs to change the result.
- Change a version, case or measure after seeing a reply and count it in this test.
- Put the changes into `SKILL.md` in the same pull request as the result.

## Limits I already know about

- Four fixes at once. If Edited does better, this can't say which fix did it.
- 24 replies on three cases, two of them the repo's own examples, all written by me. I score by reading, and measure B gives the version away, so I'll score the guards first.
- The replies come from subagents inside a coding tool with my project notes, on one message with everything given up front.
