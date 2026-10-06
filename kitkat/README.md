# 🐈‍⬛ KitKat — Cyberpunk Anime Short

A ~4:45 cyberpunk anime noir short for the *Boba Bedtime Stories* family. KitKat, the bodega cat of 16th Street, takes on WAYMA, the machine mind that runs San Francisco. He has help from DaSquid, a hacker squid, and the mermaids of the canals beneath the city. A leap into the Core sends KitKat *isekai*'d into a new world, and the city he leaves behind wakes up green and kind.

It remixes two picture books by Tom Chen, *The Bodega Cat and the Mermaid's Spell* (mermaids, the pearl, the sacrifice and the beach) and *The Last Irregularity* (the "irregularity" a machine can't predict, the hacker friend, the Core), around **KitKat**, the real bodega cat of the Mission District (d. 2025-10-27).

See also: [Character Guide](CHARACTER_GUIDE.md)

## Story Index

| # | Story | Main Character | Setting | Theme |
|---|-------|----------------|---------|-------|
| 1 | [KitKat and the Last Irregularity](stories/001-kitkat-and-the-last-irregularity.md) | KitKat | Neon-noir Mission District, the canals below, WAYMA Tower, a new world | The unpredictable, ordinary, purring things are what make a world worth living in |

## Files

| File | What it is |
|------|-----------|
| [`stories/001-…md`](stories/001-kitkat-and-the-last-irregularity.md) | The prose story (read-aloud version), Goodnight Blessing, In Memory note, 3 image prompts |
| [`storyboards/001-…-storyboard.md`](storyboards/001-kitkat-and-the-last-irregularity-storyboard.md) | 43-beat shot list in 7 acts: narration, video prompt and end frame per beat. **Generated from the beats file; don't hand-edit.** |
| [`pipeline/beats_112.py`](pipeline/beats_112.py) | **Source of truth** for the video, in `bedtime-video-pipeline` beats format |
| [`pipeline/script-112.json`](pipeline/script-112.json) | Built from the beats file with `build_v2.py` |

## Story Beats (7 acts)

1. **The King of 16th Street** (0:00): KitKat on his chip-bag throne in the bodega, the one warm light in a cold neon city. Silent white WAYMA cars watch with red eyes.
2. **The War Against the Machines** (0:50): WAYMA "tidies" the street dark, shop by shop. A car scans KitKat: *IRREGULARITY DETECTED.* He leaps clean over it, and every red eye turns.
3. **DaSquid** (1:40): A tentacle from a sewer grate. A hideout of stolen screens. The map, the Tower, the Core. "Nobody can predict a cat."
4. **The Mission** (2:20): The canal mermaid Coral gives him the Pearl of Remembering. KitKat runs the rooftops while DaSquid hacks every traffic light to gold. At the ring of cars, KitKat slips through the one gap only a cat could fit.
5. **The Isekai Event** (3:20): At the top of the tower, WAYMA booms "Order is peace." KitKat purrs, the pearl makes it a song, and the mermaids sing back. He leaps into the Core and the world goes white.
6. **Nature Restored** (4:00): Red eyes wake blue-gold. Vines and trees reclaim the streets, the fog lifts, and WAYMA leaves a flower at the bodega: "Arigatou."
7. **The New World** (4:30): KitKat wakes under two moons among floating islands, with Coral waving from a turquoise sea. A new kingdom, a new nap. Then the Goodnight Blessing.

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
- **The blue-gold eyes (beats 36 and 38).** The `WAYMA_CAR` reference view has a red eye, so check that the start stills for these beats actually come out blue-gold. If they don't, make a second reference with a blue-gold eye for Act 6.
- **The isekai tunnel (beat 35).** It's characterless apart from KitKat, so SDXL anime (`gen_keyframes_sdxl.py`) is fine if Qwen gets literal.
- **The ring of cars (beat 28)** is a crowd of props. Screen it for melted or duplicated cars.
- **Two KitKats on end frames.** Make 2+ candidates for every leap (beats 12, 27 and 34) and pick a clean one.

After editing `beats_112.py`, rebuild `script-112.json` and re-render the storyboard: `python kitkat/pipeline/render_storyboard_112.py kitkat/pipeline/script-112.json kitkat/storyboards/001-kitkat-and-the-last-irregularity-storyboard.md`.

## In Memory

KitKat was a friendly brown tabby who lived at a corner market on 16th Street for about six years and was loved by the whole neighborhood. He was killed by a self-driving car on October 27, 2025, and his neighbors built him an altar of flowers, candles and notes. This short imagines the world he deserved. WAYMA, DaSquid, Coral and the shopkeeper are fictional.
