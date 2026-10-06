# 🐈‍⬛ KitKat — Cyberpunk Anime Short

A ~4:50 cyberpunk anime noir short for the *Boba Bedtime Stories* family. KitKat, the bodega cat of 16th Street, takes on WAYMA, the machine mind that runs San Francisco. He has help from DaSquid, a hacker squid, and the mermaids of the canals beneath the city. A leap into the Core sends KitKat *isekai*'d into a new world, and the city he leaves behind wakes up green and kind.

It remixes two picture books by Tom Chen, *The Bodega Cat and the Mermaid's Spell* (mermaids, the pearl, the sacrifice and the beach) and *The Last Irregularity* (the "irregularity" a machine can't predict, the hacker friend, the Core), around **KitKat**, the real bodega cat of the Mission District (d. 2025-10-27).

See also: [Character Guide](CHARACTER_GUIDE.md)

## Story Index

| # | Story | Main Character | Setting | Theme |
|---|-------|----------------|---------|-------|
| 1 | [KitKat and the Last Irregularity](stories/001-kitkat-and-the-last-irregularity.md) | KitKat | Neon-noir Mission District, the canals below, WAYMA Tower, a new world | The unpredictable, ordinary, purring things are what make a world worth living in |

## Files

| File | What it is |
|------|-----------|
| [`stories/001-…md`](stories/001-kitkat-and-the-last-irregularity.md) | The five-minute narration in the repo's [FIVE_MINUTE_STORY_GUIDE](../FIVE_MINUTE_STORY_GUIDE.md) format (one beat per paragraph, `---` per scene), with the Goodnight Blessing, image prompts, Animation Notes and an In Memory note. **Passes `check_five_minute.py`** (0 fail, 0 warn) |
| [`storyboards/001-…-storyboard.md`](storyboards/001-kitkat-and-the-last-irregularity-storyboard.md) | 49-beat shot list in 10 scenes: narration, video prompt and end frame per beat. **Generated from the beats file; don't hand-edit.** |
| [`pipeline/beats_112.py`](pipeline/beats_112.py) | **Source of truth** for the video, in `bedtime-video-pipeline` beats format. The narration matches the story beat for beat |
| [`pipeline/script-112.json`](pipeline/script-112.json) | Built from the beats file with `build_v2.py`: 49 beats, 641 words, max 16 words per beat, 19 end frames |

## Story Beats (10 scenes · 46 beats + 3 blessing)

1. **The King of 16th Street** (0:00): KitKat on his chip-bag throne in the bodega, the one warm light in a cold neon city. His one wish: keep his loud, messy street exactly that way.
2. **The War on the Street** (0:32): The red-eyed WAYMA fleet. WAYMA wants a perfect, predictable city, so the neon goes dark shop by shop.
3. **Irregularity Detected** (0:50): A car scans KitKat. He leaps clean over its hood, and a violet tentacle waves him into a sewer grate.
4. **DaSquid** (1:22): The flooded subway hideout. "Eight arms, zero bosses." The Tower and the Core. "Nobody can predict a cat."
5. **The Mermaid's Pearl** (1:53): Coral rises from the singing canals and gives him the Pearl of Remembering.
6. **The Rooftop Run** (2:25): KitKat runs the rooftops, falls splat into a gutter, and soars on as DaSquid flips every traffic light to gold.
7. **The Ring of Steel** (2:56): The cars ring the tower. KitKat pours himself through a vent the size of a cereal box.
8. **The Isekai Event** (3:09): At the top, WAYMA booms "Order is peace." KitKat purrs, the pearl makes it a song, and the mermaids sing back. He leaps into the Core, and everything goes white.
9. **Nature Restored** (3:53): At sunrise the red eyes wake blue-gold, vines and trees reclaim the street, and WAYMA leaves a flower at the bodega: "Arigatou."
10. **The New World** (4:25): KitKat wakes among floating islands under two moons. He sneezes at a petal, Coral waves from the sea, and a new kingdom needs a king (and a nap). Then the Goodnight Blessing.

## Look

**Hand-drawn 1990s cyberpunk anime noir.** The city is inky shadows, low-key lighting and high-contrast chiaroscuro, with hard pools of magenta, cyan and red neon, rain, fog and steam, and heavy film grain. The bodega is the only warm light. After the Core the palette opens up into sunrise gold, then the pastel sky of the new world. The car eyes carry the arc: red to blue-gold.

## Make the Video (bedtime-video-pipeline)

The pipeline follows `RUNBOOK.md` → "Current production path": Qwen-Image-2.1 stills → LTX-2.5.

```bash
# from the pipeline repo
cp ../BobaBedtimeStories/kitkat/pipeline/beats_112.py pipeline/
cd pipeline && python build_v2.py beats_112 script-112.json && cd ..
S=pipeline/script-112.json; O=~/dev/videos/out/112-kitkat-and-the-last-irregularity

# 1. narration first (audio is the master clock); tts warns outside 180–300 s
~/dev/videos/venv-tts/bin/python pipeline/tts_chatterbox.py --script $S --out $O \
    --ref ~/dev/videos/out/voice-ref/bf_emma.wav --cfg 0.65 --gap 0.8
# 2. one clean view per token: KITKAT, DASQUID, CORAL, WAYMA_CAR -> keyframes/ref/<token>.png
$PY pipeline/gen_keyframes_img.py --script $S --out $O --model qwen21 --portraits
# 3. keyframes, 4. end frames (+ hold-pose pin on static beats), 5. animate + assemble
$PY pipeline/gen_keyframes_img.py --script $S --out $O --model qwen21
$PY pipeline/gen_keyframes_img.py --script $S --out $O --model qwen21 --end --candidates 2
$PY pipeline/gen_clips_ltx25.py --script $S --out $O --hires --mid --end --dest ltx25
$PY pipeline/assemble_mp4.py --out $O --dir ltx25 --tag ltx25 --narration $O/narration.wav
```

**Watch for:**
- **The blue-gold eyes (beats 38, 40 and 41).** The `WAYMA_CAR` reference view has a red eye, so check that the start stills for these beats actually come out blue-gold. If they don't, make a second reference with a blue-gold eye for scene 9.
- **The isekai tunnel (beat 37).** It's characterless apart from KitKat, so SDXL anime (`gen_keyframes_sdxl.py`) is fine if Qwen gets literal.
- **The ring of cars (beat 29)** is a crowd of props. Screen it for melted or duplicated cars.
- **Two KitKats on end frames.** Make 2+ candidates for every leap (beats 11, 28 and 36) and pick a clean one.

After editing the story, run `python check_five_minute.py --fix kitkat/stories/001-kitkat-and-the-last-irregularity.md`, then make the same change in `beats_112.py`, rebuild `script-112.json` and re-render the storyboard: `python kitkat/pipeline/render_storyboard_112.py kitkat/pipeline/script-112.json kitkat/storyboards/001-kitkat-and-the-last-irregularity-storyboard.md`.

## In Memory

KitKat was a friendly brown tabby who lived at a corner market on 16th Street for about six years and was loved by the whole neighborhood. He was killed by a self-driving car on October 27, 2025, and his neighbors built him an altar of flowers, candles and notes. This short imagines the world he deserved. WAYMA, DaSquid and Coral are fictional.
