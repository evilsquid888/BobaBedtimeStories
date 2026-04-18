# Illustrated Story Workflow

Use this workflow to convert a markdown story from `stories/` into an illustrated HTML bedtime story matching the existing editions.

## Inputs

- Source story: `stories/NN-story-title.md`
- Existing examples: `illustrated/04-mochi-and-the-stretchy-escape/index.html`, `illustrated/05-grass-jelly-and-the-cool-shadow/index.html`, and `illustrated/06-pineapple-cake-and-the-golden-gift/index.html`
- Style references: `CHARACTER_GUIDE.md`, `STYLE_GUIDE.md`, and `STORY_SYNOPSIS.md`
- Template: `illustrated/TEMPLATE.html`

## Output Shape

Create:

```text
illustrated/NN-story-title/
├── index.html
└── assets/
    ├── story-NN-intro.png
    ├── story-NN-page-01.png
    ├── ...
    └── story-NN-page-10.png
```

Each illustrated story has:

- One intro section and ten numbered story pages
- One image per section, for 11 images total
- A sticky top page navigation matching stories 4, 5, and 6
- A short Mandarin spotlight on the intro page
- Mandarin terms on first use with Chinese, pinyin, and English
- A warm Goodnight Blessing on page 10
- A palette tuned to the main character and setting, while preserving the shared layout

## Story Adaptation Steps

1. Read the source markdown story and identify the main beats.
2. Condense the story into 10 picture-book page beats plus the intro.
3. Keep the opening funny within the first page.
4. Preserve the main character's voice from `CHARACTER_GUIDE.md`.
5. Keep each page to one or two short paragraphs.
6. Use the joyful dessert-destiny framing when a character is eaten or shared.
7. Avoid rewriting unrelated story canon.

## Image Generation Steps

Generate images in this order:

1. Intro image
2. Page 1 image
3. Page 2 image
4. Page 3 image
5. Page 4 image
6. Page 5 image
7. Page 6 image
8. Page 7 image
9. Page 8 image
10. Page 9 image
11. Page 10 closing image

Use consistent prompt scaffolding:

```text
Use case: illustration-story
Asset type: illustrated bedtime story page image, 3:2 landscape
Primary request: [specific story moment]
Scene/backdrop: [Taiwan location and details]
Subject: [main character details from CHARACTER_GUIDE.md]
Style/medium: warm whimsical children's storybook illustration
Composition/framing: wide 3:2
Lighting/mood: cozy, playful, bedtime-friendly
Color palette: [character and setting colors]
Constraints: no readable text, no logos, no watermark, child-friendly, consistent character design
```

Copy generated images into the story's `assets/` folder. Keep the originals in the generator output folder.

## HTML Steps

1. Copy `illustrated/TEMPLATE.html` to the new `index.html`.
2. Replace all `{{...}}` placeholders.
3. Set `src` values to `assets/story-NN-intro.png` and `assets/story-NN-page-##.png`.
4. Write descriptive alt text for every image.
5. Tune the CSS variables for the story palette.
6. Add the new illustrated edition link to the `README.md` list.

## Validation

Run this from the repo root, replacing the path:

```powershell
$story = 'illustrated\NN-story-title'
$html = Get-Content -Raw "$story\index.html"
$matches = [regex]::Matches($html, 'src="([^"]+)"')
foreach ($m in $matches) {
  $path = Join-Path $story $m.Groups[1].Value
  if (-not (Test-Path $path)) { Write-Output "MISSING $path" }
}
Write-Output "Checked $($matches.Count) image references"
```

Expected result: `Checked 11 image references` and no `MISSING` lines.

## Reusable Prompt

```text
Generate illustrated HTML Story NN using the BobaBedtimeStories illustrated workflow.

Read stories/NN-*.md plus the character and style guides. Create illustrated/NN-title/index.html matching stories 4, 5, and 6: intro plus 10 pages, 11 generated 3:2 images, Mandarin on first use, a page 10 Goodnight Blessing, and a tuned story palette. Save images as story-NN-intro.png and story-NN-page-01.png through story-NN-page-10.png in the new assets folder. Update README.md and verify all image references resolve.
```
