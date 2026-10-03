# 🎬 LTX-2.5 Guide — Life Lessons Videos

How each story's **Video Storyboard** becomes a rich, lively ~5-minute bedtime video on the local pipeline (`~/dev/bobavideo-pipeline/bedtime-video-pipeline`, see its RUNBOOK "Current production path"). Every rule here comes from a measured result in that repo's LESSONS.md.

## Storyboard header (paste into every story)
```
**Pipeline:** Qwen-Image-2.1 stills at 1792×1024, one reference view per character (Sample Images → Character views), day/night "pop" still look ·
camera_pins.py --motion --hold-end · LTX-2.5 two-stage --hires (native 1920×1088), --end --end-strength 0.35 ·
Kokoro jf_alpha,af_heart, speed 0.92, gap 0.8 · assemble_mp4.py --tail-hold 2.5
**Video style anchor (every beat):** `rich storybook animation, Pixar-meets-picture-book, warm rose pink, cream and honey gold with saturated teal and coral accents, gentle rim light, glowing highlights, deep layered depth, lively gentle character animation, expressive faces, blinking, small natural gestures`
**Negative prompt:** `blurry, jpeg artifacts, distorted hands, extra fingers, watermark, text overlay, photorealistic, flicker, character morphing, identity drift`
```

## The 5-minute structure
- **14–20 stills** ("shots"), **1–3 beats per still**, **36–48 beats** in all; the whole film ≤ 5:00 by `check_storyboard.py`'s estimate.
- One beat = one clip ≈ its narration length (≤ 18 words, ~6–7 s). The narration is the master clock; clips are never slowed down to fill it.
- A run of more than 3 beats on one still restarts the same pose at every cut (122) — split it into a new still with a different angle (wide → close on Rosie → close on the coach).
- Day vs night: the pipeline picks the still look per shot. It goes **night** if the still prompt says night, moon, bedtime, stars, evening, dusk, asleep, sleep(s/ing) or night-light. From story 08 onward, describe Cat's active story-specific task by day; use sleep words only in genuine bedtime scenes. The early nap stories retain "napping" or "dozing" by day, not "asleep". Evening outings can show an awake Cat: night lighting does not require sleeping characters.

## Image prompts (stills) — make them pop
The pipeline prepends the "pop" look (rim light on every character, glowing highlights, saturated accents, depth, busy lived-in set dressing, bright airy daylight by day, lamplight and fairy lights by night). The shot's own prompt must give it something to light. Every still prompt has, in about 60–90 words:

1. **A camera angle with drama** — low angle looking up at tiny Rosie on a big counter, over-the-shoulder, a wide establishing view with deep perspective, a tight close-up where the face fills the frame. Scale is the epic: a tiny cup in a big, warm human world.
2. **The place, packed with props that fit it** — 4–6 specific things (a grocery store: pyramids of oranges, hanging price-tag-shaped pennants with no writing, a wooden crate of honey jars glowing amber).
3. **A named light source + two saturated accents** — "late sun slanting through the window in long gold beams, teal shelves and coral flowers".
4. **One atmospheric touch** — dust motes in a sunbeam, curls of steam, drifting rose petals, soft bokeh from fairy lights, rain beads on glass.
5. **Characters by TOKEN, each with a pose and a feeling** — `ROSIE stands on the counter on her tiny legs, straw perked up, eyes wide with wonder`.

Pipeline-safe wording (each one cost re-renders before):
- **Characters by ALL-CAPS token** (`ROSIE`, `CAT`, `BOBA`); the reference view carries the design. Name everyone who is in the frame; anyone unnamed gets invented ("friends" drew human strangers).
- **Rosie stays a cup.** Walking across a rug, raising an arm high, hugging in bed drew a pink human girl on 2 of 2 seeds. Give cup poses: stands, hops, holds something in front of her cup, sits at a table edge, tucked in with lid and straw above the blanket. In a pose-risky still, spell her out: "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw".
- **Cat stays a penguin.** Write `CAT the little blue penguin` in every still (the name alone can draw a kitten).
- **No words to draw.** Signs, menus, cards, screens and speech bubbles are "plain doodles", "little pictures", "blank". Quoted text gets lettered in, misspelled.
- **No negations** ("no people", "without text") — they add the thing. Say what *is* there.
- **One place per character.** "Glows like a night-light" drew a lamp-Aiyu and a bed-Aiyu. Give the nightstand "a plain lamp".
- **Screens, windows and mirrors are full-frame holds** — a crop that cuts a phone's border puts the caller in the room.
- Round characters (Boba, Dai Daruma, Mochi) rock, bounce or wobble in place — no rolling or spinning (the face slides off).

## Beat prompts (video) — make them lively
Image-to-video from the still: say only **what changes**. Six parts, plain language:

| Part | Write | Example |
|---|---|---|
| **Shot** | framing | Medium close-up. |
| **Scene** | the place in 3–6 words | The sunny grocery aisle. |
| **Action** | ONE character action **+ one ambient motion** | ROSIE hops once and her straw springs up, while dust motes swirl in the sunbeam. |
| **Character** | ID phrase + the feeling change | the little pink rose-milk-tea cup with the striped straw — worry melts into a bright grin |
| **Camera** | one concrete verb | The camera slowly pushes in. |
| **Audio** | ambient sound, always ending `no music, no voices, no speech` | a cart wheel squeak, soft store hum, no music, no voices, no speech |

Rules:
1. **Name only the characters who are in that still.** An off-screen name makes the model slide a new, off-model one in from the edge. Point looks at "the camera" or "someone beside her".
2. **One action per beat**, and it should *show a feeling*: a straw that droops then springs up, eyes going wide, a happy wiggle, a proud little bounce, a slow nod, a gasp with both hands on the lid.
3. **One ambient motion** keeps the frame alive: steam curls, petals drift, fairy lights twinkle, a curtain sways, bubbles rise in the tea. Cat's active gesture is the primary character action, not an ambient motion; bedtime breathing can be her primary action when appropriate. Never people or vehicles passing — those are intruders.
4. **Camera verbs only:** pushes in, pulls back, pans left/right, tilts up/down, tracks beside, holds still. Most beats move (a camera move is a crop of the still, so it's safe); use "holds still" for quiet moments like the Rose breath.
5. **Exits and walk-aways are held poses** ("waves from the doorway"), not walking across the room.
6. **No lip sync.** Narration is the voice-over; characters act with faces, straws, arms and wiggles.
7. **Scenery-only beats** (no token in the prompt) are rendered locked — fine for establishing shots; describe the light changing or steam rising.

## ID phrases (word for word in every beat)
- Rosie → **the little pink rose-milk-tea cup with the striped straw**
- Tori → **the tall golden lychee-tea cup with the green straw**
- Cat → **the little blue penguin with the yellow scarf**
- Each coach has one fixed ID phrase in that story's Cast list.

## Running a story through the pipeline

### Reusing prompts with other generators

The storyboards keep narration, still-image prompts, and motion prompts separate. You can reuse the prose prompts in your other image and video generators, including your MiniMax workflow. Keep the same character reference designs and scene palette across a story; map ALL-CAPS tokens to those references, then animate one action per narration beat. The command flags below belong to the documented LTX pipeline, so use your chosen generator's own controls when adapting it.

Runtime estimates are for the measured Kokoro setup. If you change voices, speech speed, or pause lengths, time the new narration before generating clips. These files have been checked as scripts; alternate-model images and clips have not been rendered or visually validated here.

### Documented LTX workflow
1. Author `beats_NNN.py` from the storyboard: each still → `(image_prompt, [(narration, video_prompt, audio, end_or_None), …])`, tokens in `character_tokens`, designs in `character_designs`, `style_anchor` = the video style anchor above. `build_v2.py` prints words and max words per beat.
2. `tts.py --voice "jf_alpha,af_heart" --lang a --speed 0.92 --gap 0.8` — check the printed runtime is ≤ 5:00 before any images.
3. `gen_keyframes_img.py --model qwen21 --portraits`, pick one view per token; then stills at `--width 1792 --height 1024 --candidates 2`; screen and review.
4. `camera_pins.py --motion --hold-end`, then `gen_clips_ltx25.py --hires --end --end-strength 0.35 --dest ltx25`.
5. QC (contact sheets + `screen_clips.py`; list the cast's humans so they aren't flagged), re-render, `assemble_mp4.py --tail-hold 2.5`.

If a beat keeps breaking on 2.5, re-run that beat on LTX-2.3 (`gen_clips_ltx.py --hires --end`) — 2.5 is the better creative engine, 2.3 the steadier workhorse.
