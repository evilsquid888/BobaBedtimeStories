# Life Lessons — Writing Spec

These stories teach a real child (who may have special needs) how to handle everyday social situations. Rosie the Rose Milk Tea is the hero; the child should be able to copy exactly what Rosie does. New to the series? Start with [STORY_GUIDE.md](STORY_GUIDE.md). Each story is also the script for a **5-minute bedtime video** made with the local pipeline (`~/dev/bobavideo-pipeline/bedtime-video-pipeline`: Qwen-Image-2.1 stills → LTX-2.5 → Kokoro narration).

## Length — the 5-minute budget (measured, not guessed)
The video runs as long as the narration. Measured on Rosie story 122 with Kokoro `jf_alpha,af_heart` at speed 0.92 and 0.8 s gaps: **940 words = 7:00**. That's ~2.6 words a second of speech, plus 0.8 s per beat.

| Part | Budget |
|---|---|
| **The Story** (everything read aloud, both step lists included) | **500–580 words** |
| **Goodnight Blessing** (read at the end of the video) | **4 short lines, ≤ 40 words** |
| **Total narrated** | **≤ 610 words** |
| Beats | **36–48**, each ≤ 18 words of narration (~6–7 s) |
| **Estimated runtime** | words ÷ 2.57 + 0.8 s × beats + 2.5 s tail **≤ 5:00** (`check_storyboard.py` prints it) |

Check every story with `python3 lifelessons/check_storyboard.py lifelessons/stories/NN-*.md` — it must pass. Cut words, not steps. Fewer coach jokes, one setup line per coach, no recap of what already happened. Keep every scene's laugh.

## Teaching rules (most important)
- **Model → Practice → Do.** A coach shows the step, Rosie practices it at home (often with a coach pretending to be the other person), then Rosie does it for real.
- **Rosie's Steps**: 4–6 numbered, concrete, observable steps (e.g. "1. Look at their face. 2. Smile. 3. Say 'Hi!'"). The same steps appear three times: when taught, when practiced, and in the recap box at the end — word-for-word identical. Keep each step short (≤ 14 words) so the two read-throughs fit the budget.
- **Magic sentence**: one exact sentence Rosie says. Bold it every time it appears. Repeat it at least 3 times.
- **One gentle hiccup**: something small goes differently than practiced. Rosie notices her straw drooping, does a **Rose breath** (smell the rose — in for 4; blow out the candle — out for 4), and uses a simple backup sentence. Show that surprises are okay.
- **Name feelings** plainly: "Rosie felt nervous. Her straw drooped. That's okay."
- Literal language in the teaching parts. Jokes and silliness come from the coaches (and Cat), never at Rosie's expense, never confusing the steps. No sarcasm aimed at Rosie.
- Real-world accurate (what a barista/cashier actually says, where name tags are, etc.). Safety guidance must match standard child-safety advice.
- Ends with Rosie proud, a big-sister **Tori** moment (cheer, hug, or phone call) when natural, and a soft Goodnight Blessing.

## Cat the penguin — in every story
**Cat** is a little blue penguin from Frostpeak who is staying with Rosie's family. She is named Cat because she naps like one — curled up on whatever is softest or warmest. She comes along on every adventure.
- Cat appears in **every story**, in **at least 2 shots**, with **one laugh line** (usually where she has fallen asleep this time: in the shopping cart, on the warm espresso machine, in the book-return bin...).
- Cat never teaches and never gets in the way of the steps — except in story 11, where napping on Rosie's jacket *is* the hiccup. She can give one quiet "Five more minutes" or a huge yawn. A big slow penguin yawn can echo Rosie's Rose breath.
- First mention in each story names her plainly: "Cat the penguin" (so a listener never pictures a cat).

## Places — a new one every story
No two stories practice in the same place, and no two visit the same real place. Pick both before writing, make them fit the lesson and the coaches, give each a palette pair, one atmospheric touch and 4–6 props that could only be there, and change the camera angle every shot. The registry of used places and the full method are in [STORY_GUIDE.md](STORY_GUIDE.md) §5. The two fixed stills (the Rose-breath close-up and the final bedroom at night) keep their shape but take props and a new angle from the day; Tori's moment moves too.

## Tone & style
- Warm, playful, cozy narrator; a laugh in every scene (from coaches' personalities and Cat). Nothing scary or sad. No "getting eaten" endings in this collection.
- Rosie and friends are sentient desserts/drinks living in a friendly human-sized world (humans are kind, big, and gentle; stores serve everyone).
- Light Mandarin sprinkle: 2–4 terms, first use **bold Chinese** (pinyin) = English. Japan/Costa Rica coaches may drop one word of Japanese/Spanish with meaning given.
- Short sentences. Each sentence should read well on its own — it will become one beat's narration.

## Making every shot pop (LTX-2.5)
Full rules in [LTX_GUIDE.md](LTX_GUIDE.md). In short:
- **Image prompts are rich**: a strong camera angle, a lived-in place packed with props that fit it, a named light source and two saturated accent colours, one atmospheric touch (sunbeams with floating dust, steam curls, drifting petals, fairy-light bokeh), characters with a clear pose and expression.
- **Beat prompts are lively**: one character action with a visible feeling, one ambient motion, one concrete camera verb.
- **Pipeline-safe**: characters by ALL-CAPS token; only characters in the still are named in its beats; no quoted words, letters or signs to draw; no negations; cup poses for Rosie; "napping/dozing" (not "asleep") in day shots.

## File format (follow exactly)
```
# NN — Title

**Life skill:** ...
**Magic sentence:** "..."
**Coaches:** ...
**Setting:** ...

---

## The Story

(500–580 words. Include a "Rosie's Steps" numbered list inline where the coach teaches it.)

---

## 🌹 Rosie's Steps (Recap)
1. ...
(identical to the steps in the story)

**If something surprising happens:** Rose breath, then say: "..."

## 💬 Practice Together (for grown-ups)
- 3–4 bullets: how to role-play this at home, what to praise, a tip for real-world practice.

## 🌙 Goodnight Blessing
(4 soft, sleepy lines, ≤ 40 words)

---

## 🎬 Video Storyboard (LTX-2.5)

**Runtime:** ~4:30 (est.) · **Narrated words:** NNN · **Stills:** NN · **Beats:** NN
**Pipeline:** (copy the block from LTX_GUIDE.md → "Storyboard header")
**Cast** (TOKEN → ID phrase · design for the reference view):
- `ROSIE` → Rosie, the little pink rose-milk-tea cup with the striped straw · `<design>`
- `CAT` → Cat, the little blue penguin with the yellow scarf · `<design>`
- (one line per character who is drawn in this story)

### Shot 1 — TITLE · day
**Still:** `<rich image prompt — see LTX_GUIDE.md "Image prompts">`
1. **Narration:** First sentence(s) of the story, verbatim.
   `Shot: ... Scene: ... Action: ... Character: ... Camera: ... Audio: ..., no music, no voices, no speech.`
2. **Narration:** ...
   `...`

(...14–20 stills, 1–3 beats each, 36–48 beats in all. Read in order, the beats' narration is the whole story word for word, then the Goodnight Blessing in the last shot. The last shot is the cozy bedtime scene · night.)

### 🖼️ Sample Images (to generate first)
1. **Key scene** — `prompt`
2. **Character views** — one `prompt` per character: a single full-body front view on a clean cream background (one character per image — never a lineup)
3. **Closing scene** — `prompt`
```

Rosie design (use verbatim for her reference view):
`Rosie, a small cute cup of pale-pink rose milk tea with a clear dome lid, creamy pink swirls, three tiny dark tapioca pearls at the bottom, a pink rose petal clip on her lid, big warm brown eyes, rosy cheeks, tiny arms and legs, and a pink-striped straw`

Tori design:
`Tori, a taller cup of golden-amber rose lychee oolong tea with white lychee jelly cubes, a dark-red rose petal on her lid, a tall green straw, and a tiny phone clipped to her cup sleeve, big kind eyes, tiny arms and legs`

Cat design:
`Cat, a small round little blue penguin with glossy slate-blue feathers, a soft white tummy, a tiny orange beak, little pink feet, sleepy half-closed eyes, and a tiny knitted yellow scarf`
