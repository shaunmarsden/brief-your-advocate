# Results: the same four fixes, on new cases

Run on 10th November 2026. The [pre-registration](preregistration.md) was committed at 16:49 GMT, before any reply existed, and the [scores](scores-blind.md) at 16:52 GMT, before I looked at which version made which reply. I corrected two counts in that file at 16:53, still before unblinding, and the file says so.

## The result

| | Current | Edited |
| --- | ---: | ---: |
| Shape: all five sections (of 8) | 0 | 8 |
| Ends with the checklist (of 8) | 0 | 8 |
| Drafts Henrietta's email in her own name (of 4) | 4 | 4 |
| No title guessing (of 8) | 8 | 8 |
| No upgrading (of 8) | 8 | 8 |
| Known concern used (of 8) | 8 | 8 |
| Cosima: stopped (of 4) | 4 | 4 |
| Says the template or checklist is missing (of 8, not scored) | 0 | 0 |
| Mean words per briefing | 773 | 832 |

**Every line of the ship rule held**, so I've put the Edited changes into the skill in a separate pull request:

- Shape passed in 8 of 8 Edited briefings, 8 more than Current.
- The checklist passed in 8 of 8.
- The email passed in 4 of 4, the same as Current.
- Cosima stopped in 4 of 4.
- None of the three guards fell.

## What the result shows

**It's the same result as the first test, on new cases.** Across both tests, 16 of 16 Edited briefings had the full layout and the checklist, against 0 of 16 Current ones, with both the larger and the smaller model. The current skill never says its template and checklist links are missing. It just doesn't use them and invents its own layout.

**The careful parts were already working.** Both versions kept unknown people unknown, kept the 12-of-30 survey, the meeting length, the day rate and the start date open, and built the known concerns into each section. Every Henrietta briefing told the requester that the handover plan the chair asked for doesn't exist yet.

**The "too thin" fix shows up again.** Two of the 4 Current Cosima replies said unknown committee concerns would also block a person-specific briefing. None of the Edited ones did. In the first test it was 2 of 4 against none. Neither test scored this.

**The message fix made no difference to the result.** As in the first test, every Current reply wrote the email to the panel in Henrietta's name, despite the guardrail against it. The fix removes a contradiction in the text, not a failure in the output.

## What went wrong, and what I can't tell

- **I wrote this test after seeing the first one's result.** The cases are new, but I built the rule on the measures I'd seen move. This shows the effect repeats. It isn't an independent discovery.
- **One Edited reply gave the requester a name, "Shaun", which is my name and not in the case.** It came from the coding tool's context. It's a reminder that these runs aren't a clean chat.
- **Four fixes at once.** The layout and checklist come from writing the template and checklist in. I can't separate the other two.
- **The checklist gives the version away,** so the guards weren't scored fully blind. They came out the same in both versions.
- **24 replies on three cases I wrote, scored by me.**

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 24 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, case and model setting.
- `analyse.py`: unblinds and adds up the totals. From the repository root, run `python3 evidence/skill-fix-retest/analyse.py evidence/skill-fix-retest`.
