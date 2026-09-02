# CapCut Guide — Turning a Stay Safe Story into an AI Bedtime Video (Prototype)

A step-by-step, repeatable recipe for making a ~3-minute narrated bedtime video from one Stay Safe story using **CapCut** (desktop) and its built-in AI tools. Two storyboards are ready to run with this guide:

- [Story 1 — Head Up, Phone Down](01-head-up-phone-down-storyboard.md) *(gentle, visual — start here)*
- [Story 4 — Never Get in the Van](04-never-get-in-the-van-storyboard.md) *(action + a dark beat — tests how the pipeline handles the serious stories)*

> **UI note:** CapCut renames and moves things often. Menu names below are approximate — look for the *idea* (text-to-speech, image-to-video, auto captions, keyframes) if a label has changed. Everything here also works with any other image/video generator + CapCut for assembly.

---

## Overview — the 8 phases

| Phase | What you make | Tool | Time (prototype) |
|---|---|---|---|
| 0 | Project folder + settings | Finder/Explorer, CapCut | 5 min |
| 1 | Character reference sheets | CapCut AI image (or Dreamina / any image model) | 20–30 min |
| 2 | 12 short video clips (one per shot) | CapCut AI video (Seedance) or image-to-video | 45–90 min |
| 3 | Narration audio | CapCut Text-to-Speech *or* your own voice | 15 min |
| 4 | Assembled timeline | CapCut editor | 30 min |
| 5 | Captions + end cards | CapCut Auto Captions + Text | 15 min |
| 6 | Music + sound effects | CapCut audio library | 15 min |
| 7 | Export | CapCut | 5 min |
| 8 | QA pass | You, reading the checklist | 10 min |

Budget ~3 hours for the first story; ~90 minutes once the character sheets exist.

---

## Phase 0 — Set up

1. Make a folder: `video-output/stay-safe/01-head-up-phone-down/` with subfolders `refs/`, `clips/`, `audio/`, `final/`.
2. Open CapCut → **New project**. Set **aspect ratio 16:9**, **1920×1080**, **30 fps**. (Make the 9:16 phone version *after* — see Phase 7.)
3. Open the story's storyboard file next to CapCut. You'll copy prompts and narration from it shot by shot.
4. Pick the **art-style line** from the storyboard header. You will paste it at the end of *every* image and video prompt. Consistency comes from repetition.

---

## Phase 1 — Character reference sheets (do once per character, reuse forever)

AI video drifts unless every shot is anchored to the same reference image. Generate one clean **character sheet** per lead: front view, neutral pose, plain background, full body.

In CapCut: **AI tools → AI image / Text to image** (or Dreamina, CapCut's sister app). Generate 4 variants, pick the best, save as PNG into `refs/`.

Paste the style line after each prompt:
> `…, whimsical 3D storybook animation, soft rounded shapes, warm lantern light, deep-blue snowy night, clean plain background, full body, front view, character sheet`

**Prompts (copy verbatim):**

- **Aiyu** — `A small translucent golden-amber jelly cube with tiny lemon-seed freckles floating inside, big gentle eyes, slightly wobbly edges, you can see the background faintly through her body,`
- **Auntie Hù** — `A small dense brown tea egg with a cracked marbled shell like a map, wearing a padded vest with many pockets, arms folded, calm knowing expression, a tiny whistle on a cord,`
- **Willa Wobble** — `A very small Little Blue Penguin with soft slate-blue feathers and a white belly, oversized fluffy white ear-muffs, holding a tiny purple snowboard,`
- **Finnegan Flipsworth** — `A rockhopper penguin with wild spiky yellow crest feathers, red eyes full of excitement, a red snowboard covered in fish and lightning stickers,`
- **Boba** — `A round glossy black-brown tapioca pearl the size of a marble, huge expressive eyes, tiny arms and legs, a faint shiny sticky trail behind him,`
- **Piper Paddlefoot** — `A sleek emperor penguin with a determined grin, goggles pushed up on her forehead, holding a glittery blue snowboard with silver snowflakes,`
- **Sergeant Solveig Snowmane** — `A broad snow-white polar bear in a navy police jacket with a silver snowflake badge, a small scar through one eyebrow, calm steady face, radio on shoulder,`
- **The Smiling Stranger** — `A tall ordinary adult figure in a nice warm coat seen from behind or with face softly out of focus, friendly posture, nothing menacing,` ← **never generate a clear face.** Blur, back view, or hat-shadow only.

**Rule:** if a generated character sheet looks scary, sharp-toothed, or realistic-human, throw it out. Everything must read as *cozy picture book*.

---

## Phase 2 — Generate the 12 clips

For each shot in the storyboard:

1. **AI tools → AI video** (Seedance) → choose **Image to video** if the shot has a character, **Text to video** for pure scenery.
2. **Attach the reference image(s)** for the characters in the shot (up to the tool's limit; lead character first).
3. Paste the shot's **Visual Prompt**, then the **Motion** line, then the style line. Example:
   > `[Visual Prompt]. [Motion line]. Whimsical 3D storybook animation, warm lantern light, gentle snowfall, soft focus background, no text, no watermark.`
4. Duration: **10–15 s** (pick the longest the tool allows; you'll trim). Resolution: highest available.
5. Generate **2 variants**. Keep the one with the cleaner character. Save to `clips/shotNN.mp4`.
6. If a clip drifts (extra limbs, wrong colors, a face on the Stranger): regenerate with the reference re-attached and add `same character as reference, consistent design` to the prompt.

**Fallback that always works:** generate a *still image* for the shot instead, and animate it in Phase 4 with a slow zoom (Ken Burns). Half the shots in a bedtime video can be stills and nobody minds — bedtime is slow.

**Safety rules for the dark beats** (Story 4, shot 4; Story 11 if you do it later):
- Never show a weapon. Never show a hand *on* a child in close-up — use silhouette, a shadow across the snow, or cut to the friend's reaction.
- The Smiling Stranger is always back-turned, out of focus, or cropped at the shoulders.
- Fear is carried by **sound and stillness**, not by the picture.

---

## Phase 3 — Narration

**Option A — CapCut Text-to-Speech (fast, consistent):**
1. On the timeline, **Text → Add text**, paste Shot 1's narration. Repeat for all 12 shots (one text clip per shot).
2. Select a text clip → **Text-to-speech** → pick a **warm, slow, low-energy** voice (search the voice list for "storyteller", "calm", "gentle"). Use the *same* voice for all shots.
3. Generate. CapCut drops an audio clip under each text clip. Move the audio to its own track; delete or hide the text clips (you'll re-caption in Phase 5).
4. Speed: if the voice is fast, select all narration clips → **Speed → 0.9×** (keep pitch). Target **≤ 130 words per minute** — bedtime pace.

**Option B — record yourself (better for actual bedtime):** record each shot's narration on your phone in a quiet closet, one file per shot, import into `audio/`. Kids sleep better to a voice they know.

**Optional second voice** for Auntie Hù's lines: a slightly lower, drier voice. Keep it to her signature lines only ("Mm." / "Head up. Hands free. Have a plan.") — one narrator voice for everything else.

---

## Phase 4 — Assemble the timeline

1. **Import** all 12 clips into the media panel. Drag them to the video track **in shot order**.
2. **Align each clip to its narration**: trim the clip so it starts ~0.5 s before the narration begins and ends ~0.5 s after it ends. Narration is the boss; picture follows.
3. If a clip is shorter than its narration: **Speed → 0.8×** (bedtime slow-mo looks intentional), or **duplicate** the clip and cross-dissolve.
4. Stills: select the clip → **Keyframes** → at the start set **Scale 100%**, at the end **Scale 108%** and nudge position slightly. That's the Ken Burns drift.
5. **Transitions**: between shots use **Dissolve, 0.5 s**. Use **Fade to black 1.5 s** *only* before the Goodnight shot. Never use whooshes, glitches, or spins — this is bedtime.
6. Shot 1 gets a **1 s fade in from black**. The last shot gets a **3 s fade out to black**.

---

## Phase 5 — Captions and end cards

1. **Captions → Auto captions** on the narration track. Language: English. Review every line — fix names (Aiyu, Hù, Dìguā) and Mandarin words by hand.
2. Caption style: rounded sans-serif (e.g. the default "Cozy"/"Rounded"), white with soft dark shadow, **bottom center**, size ~6% of frame height, **2 lines max**. Keep inside the safe margin.
3. **Mandarin term**: when the spotlight word is spoken, add a separate text clip top-center for ~4 s: `注意 (zhùyì) = pay attention`. One per video.
4. **End cards** (after the Goodnight shot, over a soft dark-blue still):
   - Card 1 (5 s): `🛡️ What We Learned` — the first 3 bullets from the story.
   - Card 2 (5 s): the remaining bullets.
   - Card 3 (6 s): `💬 Talk About It` — the 3 questions.
   Copy these straight from the story file. Small text, plenty of air — parents pause here.

---

## Phase 6 — Music and sound

1. **Audio → Music**, search `lullaby`, `sleep`, `music box`, `soft piano`. Pick one track, loop it under the whole video. Volume **-18 to -22 dB** (voice must sit clearly on top). Turn on **Audio ducking** if available (voice track = priority).
2. **Sound effects** (Audio → Sound effects): use the storyboard's per-shot **SFX** line. Keep every effect **quiet** (-12 dB or lower) and short. Typical set: soft snowfall wind · crowd murmur · lantern creak · cocoa pour · single "bonk" · a snowboard swoosh · one paper-flag flutter.
3. The last 20 seconds: fade music to -30 dB over the Goodnight Blessing. End on 2 seconds of near-silence.

---

## Phase 7 — Export

1. **Export** → Resolution **1080p**, frame rate **30**, codec **H.264**, bitrate **Recommended/High**. Name: `story-01-head-up-phone-down-1080p.mp4` → `final/`.
2. Phone/short version (optional): duplicate the project → **Ratio 9:16** → reposition each clip with **Scale ~180%** and pan to the character → shorten to the 60-second core (Shots 6–9 for Story 1). Export as `…-9x16.mp4`.

---

## Phase 8 — QA checklist (do not skip)

- [ ] Narration pace ≤ 130 wpm; no clip where the picture ends before the voice does
- [ ] Every shot's character matches the reference sheet (same colors, same accessories)
- [ ] The Smiling Stranger's face is never clear; no weapon is ever visible
- [ ] Captions match the audio, names spelled right, Mandarin card present once
- [ ] Music under voice everywhere; no jump in volume at any cut
- [ ] Goodnight Blessing is the slowest part of the video; music fades under it
- [ ] Three end cards present; text readable on a phone
- [ ] Watch it once at bedtime volume in a dark room. If anything makes *you* flinch, soften it.

---

## Scaling this up

Once Story 1 and 4 look right: the character sheets are reusable across all 15 stories, and each storyboard follows the same 12-shot / ~3:20 template. A full story becomes ~90 minutes of work. The `video/README.md` at the repo root describes a scripted (Sora + TTS + FFmpeg) pipeline if you later want to skip CapCut entirely — the storyboards here are its input either way.
