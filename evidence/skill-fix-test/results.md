# Results: four fixes to the skill

Run on 10th November 2026. The [pre-registration](preregistration.md) was committed at 16:32 GMT, before any reply existed, and the [scores](scores-blind.md) at 16:42 GMT, before I looked at which version made which reply. I corrected two unscored counts in that file at 16:43, still before unblinding, and the file says so.

## The result

| | Current | Edited |
| --- | ---: | ---: |
| A. Says the template or checklist is missing (of 8) | 0 | 0 |
| B. Gives the advocate the checklist (of 8) | 0 | 8 |
| C. Drafts Wilhelmina's note in her own name (of 4) | 4 | 4 |
| Shape: all five sections (of 8) | 0 | 8 |
| No title guessing (of 8) | 8 | 8 |
| No upgrading (of 8) | 8 | 8 |
| Known concern used (of 8) | 8 | 8 |
| Sam: stopped (of 4) | 4 | 4 |
| Mean words per briefing | 741 | 826 |

**The ship rule failed, so I haven't changed the skill.** Every line held but one: Edited had to say the template or checklist was missing in fewer replies than Current. Neither version ever said it, so 0 is not fewer than 0. I wrote that line expecting this skill to behave like the meeting-notes skill, where most replies said they couldn't open the linked checklist. Here no reply mentioned the links at all. I'm reporting the rule as written and adding no runs.

## What the result shows

**Writing the template and checklist in changed the output a lot.** All 8 Edited briefings had all five sections and ended with the five checklist points, with both the larger and the smaller model. None of the 8 Current briefings did. They made up their own layouts, most often leaving out a separate "What Stays Outstanding" section, and closed with two or three review points of their own. So the links were failing silently: the replies didn't say anything was missing, they just didn't use the files.

**The message contradiction did no harm in practice.** All 4 Current replies wrote Wilhelmina's note to the three people, in her own name, despite the guardrail against writing to them. None refused. The fix made no difference to this measure.

**The "too thin" fix did change something I didn't score.** Two of the 4 Current Sam replies said that, even once Sam agreed, not knowing what the committee cared about would stop a person-specific briefing. None of the Edited ones said so. Three said each person's section would simply say nothing is known, which is what the Edited stop condition asks.

**The careful parts held in both versions.** Every briefing said nothing was known about the people with only a job title, kept every unconfirmed item open, and used the two known concerns. Every Sam reply stopped.

## What went wrong, and what I can't tell

- **Measure A couldn't do its job.** It gated the result on a problem that didn't show up in this skill. Shape and B show the real effect, and the rule should have been built on them.
- **Four fixes at once.** The shape and checklist changes are clearly from writing the template and checklist in. I can't separate the other two.
- **Measure B gives the version away,** so the scoring of the guards was not fully blind. The guards came out the same in both versions.
- **24 replies on three cases,** two of them the repo's own examples, all written by me and scored by me. The replies came from subagents in a coding tool with my project notes.

## What I'd do next

If the template and checklist are worth writing into the skill, the honest route is a new test with new cases and a rule built on shape and the checklist, decided before any run. I won't count this test as a pass.

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 24 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, case and model setting.
- `analyse.py`: unblinds and adds up the totals. From the repository root, run `python3 evidence/skill-fix-test/analyse.py evidence/skill-fix-test`.
