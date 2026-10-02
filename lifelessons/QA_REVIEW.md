# Life Lessons Collection Quality Review

The Life Lessons folder contains 41 stories: 16 originals and 25 additions numbered 17–41. The review covered every Life Lessons story, including its narration, teaching steps, character appearances, and storyboard. Stories 17–41 follow the collection's writing format and measured five-minute budget rather than the longer adventure-story format.

## Results

- All 41 stories pass `check_storyboard.py` and `check_collection.py`.
- Every story includes Cat the penguin in its narration and at least two stills, plus Tori in the narration and at least one still.
- The 25 additions have 535–580 story words, a four-line blessing, 19 stills, and 37–41 narration beats each. Estimated runtimes are 4:10–4:29 using the documented Kokoro settings; actual audio must still be timed when rendered.
- Every new story has five identical steps in teaching, practice, and recap. The magic sentence occurs at least three times. Narration beats reproduce the story and blessing in order.
- The additions use 22 established coaches from Taiwan, Japan, and Costa Rica, with no coach in consecutive new stories. Lulu, Guagua, and Tang recur as friends.
- The additions have 25 different practice locations and 25 different real outing locations. They rotate palettes, props, camera compositions, Cat's nap spots, and Tori's encounter points. The early original stories retain their established kitchen practice settings.

## Duplicate and theme review

All 820 pairs within the 41-story collection were compared. There are no identical stories or near-duplicate prose flags. The highest five-word phrase-set overlap after excluding teaching scaffolding is 3.1%, between original stories 06 and 11. This text comparison supports the editorial review; it does not establish that moral themes never recur.

The new plots and real-life tasks differ from the originals. Some related themes deliberately build on earlier skills:

| Related stories | Distinct lesson in the addition |
|---|---|
| 03/08 ordering drinks → 24 diner lunch | Choosing from a table menu, waiting for a server, and clarifying an unfamiliar noodle choice |
| 06 joining play → 34 invitation / 39 inclusion | Inviting a friend on a specific day through grown-ups / offering a newcomer space and a choice of participation |
| 07 waiting for a librarian → 23 queue / 38 conversation | Finding and keeping a queue position / recognizing an ordinary conversational pause and an urgent need |
| 10 paying → 27 kite budget / 32 apron exchange | Comparing price with savings / asking about permitted exchange options with an item and receipt |
| 12 cheering a friend's catch / 15 a missed toss → 28 bowling | Losing a completed shared game, congratulating the friend, and choosing a break before deciding to replay |
| 16 art-class spill → 18 marble apology / 21 ribbon honesty | Owning a bump and offering repair / truthfully reporting damage and uncertainty so a grown-up can repair it |
| 25 hug boundary / 33 quiet friend / 40 different favorites | Speaking for one's own comfort / respecting another person's support needs / respecting taste without pressure |

Broad themes such as kindness, patience, and persistence also occur in the other adventure collections. These additions use new Rosie plots and concrete social steps rather than retelling those adventures.

## Corrections made during review

Story 06 now puts Cat on a bench beside the playground slide, with a wave instead of a collision. Story 07 describes a raised finger as a possible request to wait, without promising an exact minute. Story 08 now speaks its exact magic sentence during practice. Narration-word metadata was corrected in stories 06, 08, 09, and 13.

For the additions, overly full scenes were shortened, missing on-screen human reference designs were added, and narration boundaries were adjusted to favor complete sentences or clauses. Still prompts keep Rosie as a tea cup and Cat as a blue penguin; action prompts name only characters in the corresponding still.

## Reproduce the checks

```bash
python3 lifelessons/check_storyboard.py lifelessons/stories/*.md
python3 lifelessons/check_collection.py
git diff --check
```

These are script and prompt checks. Images, voices, and animation clips have not been generated or visually reviewed. The LTX guide explains how to reuse the prose prompts with other generators while retiming changed narration.
