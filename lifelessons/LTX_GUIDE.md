# 🎬 LTX 2.5 Guide — Life Lessons Videos

How to turn each story's **Video Storyboard** into a clean ~5-minute bedtime video with LTX 2.5 (or 2.3).

## Why 2.5 looks better but errors more
2.5 moves more. Each extra bit of motion is another chance for the model to morph a hand, drift a face, or flicker a texture. The decoder helps, but fast or complex motion still breaks anatomy and identity. **Calm, simple motion is the fix.** That suits bedtime stories anyway.

> **2.5 = better creative engine. 2.3 = better workhorse.** If a beat keeps breaking in 2.5, re-run that one beat in 2.3.

## How the storyboards are built for this
Each story has **10 shots of about 30 seconds** each. Every shot is split into **3–4 beats of about 8 seconds**, and each beat is one LTX generation with **one action**.

Each beat prompt follows the **6-part screenplay structure**, written in plain language:

| Part | What to write | Example |
|---|---|---|
| **Shot** | framing | Medium close-up. |
| **Scene** | where / light (short) | Cozy kitchen table, warm afternoon light. |
| **Action** | the ONE thing that changes | Rosie's striped straw droops, then slowly perks back up. |
| **Character** | the ID phrase + expression change | the little pink rose-milk-tea cup with the striped straw — worried eyes soften into a small smile |
| **Camera** | one concrete verb | The camera slowly pushes in. |
| **Audio** | ambient only (narration is added in editing) | Soft kitchen hum, a gentle ding. No speech. |

### Rules
1. **Image-to-video: don't re-describe the image.** The start frame already shows everything. The beat prompt says only **what changes**: who moves first, what expression shifts, how the camera reframes, what sound begins. Restating the whole frame is an official anti-pattern.
2. **One action per beat.** Most errors come from overloading a shot. If a shot needs two things to happen, split it into two beats.
3. **Concrete camera verbs only:** *pushes in, pulls back, tracks beside, pans left/right, tilts up/down, holds still.* Never write "dynamic cinematic camera" or "cool angles."
4. **Gentle motion.** Small hops, slow waves, soft wobbles. No spinning, running crowds, or fast camera moves.
5. **No lip sync.** Narration is added as voice-over, so the audio part is ambient sound only, and characters show feelings through visible acting cues (straw wiggle, eyes, small gestures), not talking mouths. That keeps the visuals simple.

## Lock character identity across shots
- **Same start frame:** generate the story's **Character portrait** sample image first and use it as the reference/start frame source for every shot.
- **Same ID phrase in every beat:** use these word for word.
  - Rosie → **"the little pink rose-milk-tea cup with the striped straw"**
  - Tori → **"the tall golden lychee-tea cup with the green straw"**
  - Each coach has an ID phrase listed at the top of that story's storyboard.
- Keep lighting logic and props identical between beats of the same shot.
- **Multishot inside one generation** when you can: chain a shot's beats in one run rather than stitching separate clips. If you must stitch, use the last frame of beat 1 as the start frame of beat 2.

## Negative prompt (paste in the separate negative field)
Keep it short, 5–15 tokens, covering the five buckets:
```
blurry, jpeg artifacts, distorted hands, extra fingers, watermark, text overlay, photorealistic, flicker, character morphing, identity drift
```
Buckets: quality · anatomy · brand pollution · style drift · motion.
Note: **distilled checkpoints run at CFG 1, so negatives may do nothing** unless you use NAG or the full (non-distilled) model.

⚠️ Shot 1 of each story has a title card. Generate the title text in editing, not in LTX, because the negative prompt blocks text overlays and LTX garbles letters anyway.

## Technical settings
| Setting | Value |
|---|---|
| Resolution | divisible by 32. Use **1280×704** (16:9) or **704×1280** (vertical). Stay at or under ~720×1280 for the best quality per compute. |
| Frame count | must be **1 + a multiple of 8**. At 24 fps: **121** (~5 s), **193** (~8 s, the default beat), **241** (~10 s). |
| Final quality | generate at 720p-class, then upscale with **2.5's latent spatial upscaler**. |
| A clip keeps artifacting | re-run it at **~960×544** with the **2.5 decompression IC-LoRA**. |

### Guide strength (keyframe-guided workflows)
| Strength | Use for |
|---|---|
| 1.0 | rigid lock (title card, the recap "steps" shot) |
| 0.85 | strong end-frame (a beat must land on a specific pose, e.g., the hug) |
| **0.70–0.80** | **balanced motion, the default for these stories** |
| 0.55–0.65 | fast action (rare here: a bounce, a hop) |

## Workflow per story
1. Generate the 3 **Sample Images**. Pick the best **Character portrait** as the identity reference.
2. For each shot, generate the still from its **Image prompt**.
3. Animate each **beat** from that still (1280×704, 193 frames, guide 0.75, negative prompt above).
4. Upscale with the latent upscaler.
5. Lay the clips under the **Narration** voice-over (soft, slow voice plus gentle music). Hold the "Rosie's Steps" shot longer, and consider putting the steps on screen as text.
