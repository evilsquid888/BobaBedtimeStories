# Five-Minute Animation Story Guide

How a Japan or Hawaii story is written so the local video pipeline
(`bedtime-video-pipeline`, branch `prototype/rigged-animation`: Codex/Qwen stills → **LTX-2.5** for scenery,
expressions and action, **MiniMax H3** for talking shots, voice C narration) can turn it into a **five-minute**
animated bedtime video without abridging it first. Every rule here comes from a measured result in that repo's
LESSONS.md or from `lifelessons/SPEC.md`.

Check every story with `python3 check_five_minute.py --fix <story.md>`. It must pass (0 FAIL); fix as many
warns as you sensibly can. The exemplar is `japan/stories/025-dai-daruma-and-the-wishing-eye.md`.

## The budget (measured, not guessed)

The video runs as long as the narration. 940 words = 7:00 at the production voice (Kokoro `jf_alpha,af_heart`
0.92 / its Chatterbox clone), i.e. ~2.57 words a second, plus 0.8 s of silence per beat and a 2.5 s tail.

| | |
|---|---|
| **Beats** (paragraphs in the body) | **36–48**, each **≤ 18 words** (one clip of ~6–7 s) |
| **Scenes** (blocks separated by `---`) | **6–12**, at most 8 beats each |
| **Narrated words** (body + blessing) | about **600–680**; the checker computes the runtime |
| **Goodnight Blessing** | 3–4 soft lines, **≤ 40 words** |
| **Runtime** | words ÷ 2.57 + 0.8 × beats + 2.5 s → **4:15–5:00** |

Cut words, not events. A five-minute story has *more* happening than the old 2,000-word one, told in fewer words.

## File format

```
# Story 25: Dai Daruma and the Wishing Eye

**Main Character:** Dai Daruma
**Guest Characters:** Fuwa, a shy little steamed bun
**Setting:** A shrine stall selling lucky daruma dolls, at dusk
**Theme:** A wish is a promise you make to yourself
**Japanese Spotlight:** **negai** (neh-gah-ee) — wish

---

One beat per paragraph. One sentence, sometimes two. ≤ 18 words.

"One speaker per beat," said Dai, "and the tag says who."

---

A `---` line starts a new scene: a new place, or a new time of day in the same place.

---

## Goodnight Blessing
Three or four soft sleepy lines, ≤ 40 words, ending in Goodnight.

## AI Image Prompts
1. Key scene — ...
2. Character portrait — ...
3. Closing scene — ...

## Animation Notes
- **Cast:**
  - `DAI` — Dai Daruma: a round crimson dome-shaped daruma bun, big determined eyebrows, one painted eye, the other cheek blank; voice: peppy coach, big and bouncy.
  - `FUWA` — Fuwa: a small pale steamed bun with rosy cheeks and a fluffy curl on top; voice: tiny, breathy, nervous.
- **Scenes:**
  1. Shrine steps and daruma stall at dusk, paper lanterns, rows of red daruma dolls.
  2. ...
- **Budget:** (written by `check_five_minute.py --fix`)
```

Keep the **file name, title, main character, setting, theme and spotlight term** of the existing story (the README
index links to them). The headers use the same labels as the existing stories (`**Hawaiian Spotlight:**` in
Hawaii). Headers are not narrated.

## What a beat is

A beat is **one picture with one movement in it**. The pipeline makes one clip per beat from one still, so write
each paragraph as something you could draw and then animate for six seconds:

- **One action** that shows a feeling: a bounce, a wobble, a gasp with both arms up, a slow sad droop, a sneeze of
  incense smoke, a cape swoosh, a splash. Physical comedy tied to the ingredient (a mochi stretches, a daruma tips
  and rights himself, a ramune bottle fizzes over, a soft-serve leans in the heat).
- **One speaker at most.** A talking beat is one character's line, with a tag (`said Dai`). H3 renders the speaker's
  voice and mouth for that beat; a second speaker in the same beat has to be faked. Split exchanges into beats.
  Narrator asides and the narrator's "said X" tag are fine.
- **Scenery beats** (no character) are fine for openings, reveals and the blessing: a lantern lane, a wave, a sky.
- Round characters **rock, bounce, wobble, hop, tip, lean**. Avoid "rolled" and "spun" for a character (the face
  slides off in the animator); a thing can roll.
- **Exits are held poses** ("waved from the gate"), not walks across the room.

## What costs re-renders (avoid in the body)

- **Text to read.** Signs, labels, menus, screens, letters, written wishes: the model letters them in, misspelled.
  Write "a plain wooden plaque", "a little drawing of a fox", "a paper with a doodled star". Never quote what a sign
  says. A written wish becomes a picture-wish; a recipe becomes a remembered song.
- **Humans.** "People", "children", "a hand", "the shopkeeper" get drawn as humans. The stall-keeper is a food
  character or a lantern; a crowd is "a lane full of lanterns and treat-folk"; a "hand" is a paw, an arm, a flipper.
  Use `kids`, `grandma`, `people` only when the story truly needs a person (rare).
- **Off-screen names.** Naming a character who is not in the shot slides an off-model copy in from the edge.
  Keep the cast to the main character + at most three guests, all present in the scene where they're named.
- **Negations in action.** "He did not fall" draws a fall. Say what happens.
- **A story reveal in the setting.** If the sea glows at beat 20, the first 19 beats describe a dark sea.
- **Sleep words by day.** "asleep / sleeping / bedtime / stars / moon / evening / dusk" switch the still to the
  night look. Use them only when it is night. Day naps are "dozing".

## Add more action and more interesting things

The old 2,000-word versions were mostly talk. Each five-minute cut needs, in order:

1. **Fun by beat 3.** A gag, a pratfall, a spectacle, a dare.
2. **A want** stated by beat 6 (the character wants something concrete and visible).
3. **A set-piece in the middle**: a chase, a climb, a race, a rescue, a thing that tips over and has to be caught,
   a contest, a storm, a lost item hunted through three places, a parade that goes wrong. It has **escalation**:
   try, fail funnier, try bigger, fail bigger, then the turn.
4. **Two "oh!" moments** the viewer can see: a reveal (the fog lifts and the whole valley is lanterns), a reversal
   (the shy one saves the bold one), a surprise guest, a trick that tricks the trickster.
5. **The turn** comes from the theme, shown by an action, then said in one line by one character.
6. **A cozy landing** of 3–5 beats that slows down: lights dim, friends lean together, a yawn, the last gag.
7. **A laugh line in every scene.** Silly, never mean.

Keep the heart of the original: its lesson, its best joke, its guest. Everything else can change.

## Voice and language

- Warm narrator, Roald-Dahl-meets-a-night-market. Playful, silly, cozy. Never preachy; the lesson is one line.
- **Spotlight term** appears bold with pronunciation and meaning on first use, and again plainly later:
  `**negai** (neh-gah-ee) — wish`. One or two more local terms are welcome, same format, once each.
- Dialogue short and in character (see the arc's `CHARACTER_GUIDE.md`: catchphrase, voice, pronouns). Pronouns are
  canonical. Dai Daruma's second eye stays blank until Japan story 98.
- The blessing is read by the narrator over a scenery shot. Soft, sleepy, 3–4 lines, ends with "Goodnight."

## Animation Notes

- **Cast:** every character who appears, as an ALL-CAPS token: `TOKEN` — Name: design in one line (shape, colors,
  the two details that identify them), then `voice:` three words for the H3 talking shots. Use the design from the
  arc's character guide.
- **Scenes:** one numbered line per `---` block, in order: place, light, the props worth drawing. Night scenes say
  night. A reveal (glow, snow, lights coming on) belongs only to the scenes after it happens.
- **Budget:** leave the line in place; `check_five_minute.py --fix` fills it.
