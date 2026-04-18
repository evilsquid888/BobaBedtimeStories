# Bedtime Story Video Pipeline Plan

This plan turns the illustrated HTML stories into fully automated bedtime-story videos.

## Goal

Create a repeatable pipeline that converts one illustrated story folder into a YouTube-ready bedtime video.

Default target:

- Input: `illustrated/NN-story-title/index.html`
- Output: `video-output/NN-story-title/final/story-NN-title-1080p.mp4`
- Format: 16:9 landscape, 1920x1080 final render
- Duration: 4-5 minutes
- Style: calm narrated bedtime story with gentle motion, captions, fades, and cozy pacing
- Budget target: under `$15` per story unless explicitly overridden

## Recommended Low-Cost Architecture

Use the existing illustrated stories as the canonical storyboard. Each HTML story already has an intro plus 10 pages, with 11 images total. The video pipeline should reuse that structure instead of generating video from scratch.

Default automated stack:

- Sora API for one generated video clip per story scene
- OpenAI TTS for consistent bedtime narration
- Local FFmpeg rendering through `imageio-ffmpeg` or another bundled binary
- Generated captions from the narration script and scene timing
- A dry-run cost estimator before any paid generation

This keeps the process scriptable and repeatable while avoiding manual video editing.

## Pipeline Steps

1. Parse the illustrated HTML story.
   - Extract title, lead, Mandarin spotlight, 10 page headings, page text, image paths, image alt text, and Goodnight Blessing.
   - Produce a `manifest.json` with 11 scenes: intro plus pages 1-10.

2. Generate narration.
   - Build a calm bedtime narration script from the page text.
   - Use OpenAI TTS by default.
   - Save audio and timing metadata under `video-output/NN-story-title/audio/`.

3. Generate video clips.
   - Create one clip per scene using Sora.
   - Use image-to-video references when allowed and safe.
   - Fall back to prompt-only generation for images containing human faces or likely children, because video APIs may reject those image references.
   - Keep clip prompts gentle: slow motion, soft camera drift, cozy light, no readable text, no logos, no scary motion.

4. Assemble the final video.
   - Normalize clips to 1920x1080.
   - Add narration, captions, and soft transitions.
   - Optionally add quiet background ambience or music if licensing is clear.
   - Save final MP4 under `video-output/NN-story-title/final/`.

5. Save run artifacts.
   - `manifest.json`
   - `cost-report.json`
   - `captions.srt`
   - `run-log.json`
   - final MP4

## Cost Guard

Before calling paid APIs, the pipeline should estimate:

- Total generated video seconds
- TTS character count
- Expected provider cost
- Whether the run exceeds the default `$15` story budget

If the estimate exceeds budget, stop before generation unless the operator passes an explicit override such as `--allow-over-budget`.

## Seedance 2.0 Notes

Seedance 2.0 is worth tracking as a future provider, especially for premium clips.

Potential strengths:

- Strong multimodal video generation
- Supports image-to-video and reference-based video workflows
- Good fit for hero scenes, trailers, or higher-budget story versions

Current recommendation:

- Do not use Seedance 2.0 as the first default backend.
- Use Sora first for automation and budget control.
- Add Seedance later through a provider adapter so individual scenes can choose `sora`, `seedance`, or another backend.

Reason:

- Current Seedance 2.0 per-second pricing through hosted APIs makes full 4-5 minute videos likely much more expensive than the `$15` target.
- It may still be excellent for selected hero clips such as the intro, climax, or closing scene.

## Future Implementation Checklist

- `video/story-video.schema.json`
- `video/scripts/build_manifest.py`
- `video/scripts/generate_narration.py`
- `video/scripts/generate_clips.py`
- `video/scripts/render_video.py`
- `video/scripts/estimate_cost.py`
- Provider adapter interface for Sora first, Seedance later
- Dry-run mode that writes prompts and estimates without API calls
- Smoke test mode that generates one short clip and one short TTS sample

## Acceptance Criteria

A finished pipeline should:

- Generate a complete 4-5 minute video from an illustrated story folder
- Require no manual video editing
- Produce a valid 1920x1080 MP4
- Include narration and captions
- Preserve the existing story order and cozy bedtime tone
- Stop before paid API calls if the estimated cost exceeds the configured budget

