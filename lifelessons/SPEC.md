# Life Lessons — Writing Spec

These stories teach a real child (who may have special needs) how to handle everyday social situations. Rosie the Rose Milk Tea is the hero; the child should be able to copy exactly what Rosie does. Each story is also a script for a ~5-minute bedtime video made with LTX (2.3 / 2.5) from image prompts.

## Teaching rules (most important)
- **Model → Practice → Do.** A coach shows the step, Rosie practices it at home (often with a coach pretending to be the other person), then Rosie does it for real.
- **Rosie's Steps**: 4–6 numbered, concrete, observable steps (e.g. "1. Look at their face. 2. Smile. 3. Say 'Hi!'"). The same steps appear three times: when taught, when practiced, and in the recap box at the end — word-for-word identical.
- **Magic sentence**: one exact sentence Rosie says. Bold it every time it appears. Repeat it at least 3 times.
- **One gentle hiccup**: something small goes differently than practiced (listed in the assignment). Rosie notices her straw drooping, does a **Rose breath** (smell the rose — in for 4; blow out the candle — out for 4), and uses a simple backup sentence. Show that surprises are okay.
- **Name feelings** plainly: "Rosie felt nervous. Her straw drooped. That's okay."
- Literal language in the teaching parts. Jokes and silliness come from the coaches, never at Rosie's expense, never confusing the steps. No sarcasm aimed at Rosie.
- Real-world accurate (what a barista/cashier actually says, where name tags are, etc.). Safety guidance must match standard child-safety advice.
- Ends with Rosie proud, a big-sister **Tori** moment (cheer, hug, or phone call) when natural, and a soft Goodnight Blessing.

## Tone & style
- Warm, playful, cozy narrator; a laugh in every scene (from coaches' personalities). Nothing scary or sad. No "getting eaten" endings in this collection.
- Rosie and friends are sentient desserts/drinks living in a friendly human-sized world (humans are kind, big, and gentle; stores serve everyone).
- Light Mandarin sprinkle: 2–4 terms, first use **bold Chinese** (pinyin) = English. Japan/Costa Rica coaches may drop one word of Japanese/Spanish with meaning given.
- Short sentences. Read-aloud length **700–900 words** for the story section (≈5 minutes of narration).

## File format (follow exactly)
```
# NN — Title

**Life skill:** ...
**Magic sentence:** "..."
**Coaches:** ...
**Setting:** ...

---

## The Story

(700–900 words. Include a "Rosie's Steps" numbered list inline where the coach teaches it.)

---

## 🌹 Rosie's Steps (Recap)
1. ...
(identical to the steps in the story)

**If something surprising happens:** Rose breath, then say: "..."

## 💬 Practice Together (for grown-ups)
- 3–4 bullets: how to role-play this at home, what to praise, a tip for real-world practice.

## 🌙 Goodnight Blessing
(4–6 soft, sleepy lines)

---

## 🎬 Video Storyboard (LTX)

**Runtime:** ~5:00 · **Shots:** 10
**Art style (use on ALL shots):** Soft whimsical storybook illustration, warm pastel palette of rose pink, cream, and honey gold, gentle rounded shapes, cozy lighting, Pixar-meets-picture-book, 16:9.
**Character reference — Rosie:** (paste the one-line Rosie description below into every shot that includes her)
**Character reference — coaches:** one line each for this story's coaches.

**LTX settings:** 1280×704 · 193 frames (~8 s) per beat · guide strength 0.75 · see `LTX_GUIDE.md`
**Negative prompt (all beats):** `blurry, jpeg artifacts, distorted hands, extra fingers, watermark, text overlay, photorealistic, flicker, character morphing, identity drift`
**ID phrases (use word-for-word in every beat):**
- Rosie → the little pink rose-milk-tea cup with the striped straw
- (one short, fixed ID phrase per coach / Tori in this story)

### Shot 1 — TITLE (0:00–0:30)
**Image prompt:** `...full standalone prompt, includes style + character descriptions (title text is added in editing, not generated)...`
**LTX 2.5 beats** (image-to-video from the still above — describe ONLY what changes, ONE action per beat):
1. `Shot: medium close-up. Scene: cozy kitchen table, warm afternoon light. Action: <one change>. Character: <ID phrase> — <expression shift>. Camera: <one concrete verb: pushes in / pulls back / tracks beside / pans / tilts / holds still>. Audio: <ambient only, no speech>.`
2. `...`
3. `...`
**Narration:** > story text covered by this shot (verbatim excerpt of The Story)

(...through Shot 10 — 3–4 beats per shot, gentle motion only, no lip sync; the last shot is the cozy goodnight scene. Narration across all 10 shots covers the whole story in order.)

### 🖼️ Sample Images (to generate first)
1. **Key scene** — `prompt`
2. **Character portrait** — `prompt` (Rosie + this story's coach(es), clean background, good as a reference image)
3. **Closing scene** — `prompt`
```

Rosie one-line reference (use verbatim in prompts):
`Rosie, a small cute cup of pale-pink rose milk tea with a clear dome lid, creamy pink swirls, three tiny dark tapioca pearls at the bottom, a pink rose petal clip on her lid, big warm brown eyes, rosy cheeks, tiny arms and legs, and a pink-striped straw`

Tori one-line reference:
`Tori, a taller cup of golden-amber rose lychee oolong tea with white lychee jelly cubes, a dark-red rose petal on her lid, a tall green straw, and a tiny phone clipped to her cup sleeve`
