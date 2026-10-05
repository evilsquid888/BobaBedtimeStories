#!/usr/bin/env python3
"""Check a five-minute animation story (FIVE_MINUTE_STORY_GUIDE.md) and fill in its Budget line.

    python3 check_five_minute.py japan/stories/025-*.md hawaii/stories/*.md
    python3 check_five_minute.py --fix japan/stories/025-*.md     # rewrite the Budget line in Animation Notes

Checks: header lines, beat count and words per beat, scene breaks vs the Scenes list, blessing length,
three image prompts, Animation Notes cast/scenes/budget, and the runtime estimate from the measured
narration rate (lifelessons/SPEC.md: 940 words = 7:00 at Kokoro jf_alpha,af_heart speed 0.92, gap 0.8 s).
Warns on words that cost re-renders in the pipeline (written text, humans, two speakers in one beat).
"""
import re
import sys

WPS = 2.57            # words per second of speech
GAP, TAIL = 0.8, 2.5  # seconds between beats, tail hold
MAX_SECS, MIN_SECS = 300, 255
BEAT_WORDS = 18
BEATS = (36, 48)
SCENES = (6, 12)
SCENE_BEATS = 8
BLESS_WORDS = 40

TAGS = (r"said|asked|whispered|cried|shouted|called|sang|giggled|gasped|announced|sighed|muttered|yelled|laughed|"
        r"squeaked|boomed|added|replied|grinned|wailed|huffed|hummed|puffed|crowed|chirped|rumbled|murmured|whooped|"
        r"breathed|offered|chuckled|declared|cheered|hollered|shrieked|whimpered|beamed|sniffled|agreed|begged|"
        r"wondered|repeated|decided|insisted|answered|explained|warned|admitted|managed|roared|bellowed|cooed|purred|"
        r"squealed|snorted|groaned|moaned|gulped|wheezed|hiccuped|burbled|fizzed|sizzled|trilled|piped|panted")
SPEAKER_AFTER = re.compile(r"\b(?:" + TAGS + r")\s+(?:the\s+)?([A-Z][\w'-]+)")
SPEAKER_BEFORE = re.compile(r"\b([A-Z][\w'-]+)\s+(?:" + TAGS + r")\b")
NOT_NAMES = {"The", "A", "An", "And", "But", "Then", "So", "Now", "Oh", "I", "It", "He", "She", "They", "We", "You",
             "Nobody", "Everyone", "Someone", "Something", "Nothing", "Everybody", "Wasshoi", "Who", "What"}
TEXT_WORDS = re.compile(r"\b(signs?|written|wrote|writes|writing|lettered|letters|label|labels|menu|screen|screens|"
                        r"phone|words on|spelled|spelling|a note|the note|notes)\b", re.I)
HUMAN_WORDS = re.compile(r"\b(people|person|crowds?|children|child|kids?|man|woman|men|women|boys?|girls?|hands?|"
                         r"fingers?|tourists?|visitors?|shopkeeper|vendor|vendors|grandma|grandpa|mother|father|"
                         r"lady|guy|guys|human|humans|folks)\b", re.I)


def words(t):
    t = re.sub(r"[*_>`]", " ", t)
    return re.findall(r"[\w'’-]+", t.lower().replace("’", "'"))


def section(md, head, stop=r"\n## "):
    m = re.search(head, md)
    if not m:
        return None
    rest = md[m.end():]
    e = re.search(stop, rest)
    return rest[:e.start()] if e else rest


def check(path, fix=False):
    md = open(path, encoding="utf-8").read()
    errs, warns = [], []
    name = path.split("/")[-1]

    # ---- header
    if not re.match(r"# Story \d+: \S", md):
        errs.append("first line must be '# Story N: Title'")
    for h in ("Main Character", "Guest Characters", "Setting", "Theme"):
        if not re.search(rf"^\*\*{h}:\*\* \S", md, re.M):
            errs.append(f"missing **{h}:** line")
    spot = re.search(r"^\*\*(Japanese|Hawaiian|Mandarin|Spanish) Spotlight:\*\* \*\*([^*]+)\*\*", md, re.M)
    if not spot:
        errs.append("missing **<Language> Spotlight:** **term** line")

    # ---- body = between the first '---' after the header and '## Goodnight Blessing'
    parts = md.split("\n---\n")
    if len(parts) < 3:
        errs.append("body must sit between a '---' after the header and a '---' before the blessing")
        body_blocks = []
        body_text = ""
    else:
        end = md.find("## Goodnight Blessing")
        start = md.find("\n---\n") + 5
        body_text = md[start:end]
        # drop the closing '---' before the blessing
        body_text = re.sub(r"\n---\s*$", "", body_text.rstrip())
        body_blocks = [b.strip() for b in re.split(r"\n---\n", body_text)]
    beats = []
    scene_sizes = []
    for si, block in enumerate(body_blocks, 1):
        paras = [p.strip() for p in re.split(r"\n\s*\n", block) if p.strip()]
        scene_sizes.append(len(paras))
        if len(paras) > SCENE_BEATS:
            errs.append(f"scene {si} has {len(paras)} beats (<= {SCENE_BEATS}; add a '---' scene break)")
        for p in paras:
            beats.append(p)
            if "\n" in p:
                errs.append(f"beat has a line break inside it: '{p[:50]}...' (one paragraph = one beat)")
    for i, b in enumerate(beats, 1):
        n = len(words(b))
        if n > BEAT_WORDS:
            errs.append(f"beat {i}: {n} words (<= {BEAT_WORDS}): '{b[:60]}...'")
        if TEXT_WORDS.search(b):
            warns.append(f"beat {i}: written-text word '{TEXT_WORDS.search(b).group(0)}' (nothing to read on screen)")
        if HUMAN_WORDS.search(b):
            warns.append(f"beat {i}: human word '{HUMAN_WORDS.search(b).group(0)}' (humans get drawn)")
        speakers = {m for m in SPEAKER_AFTER.findall(b) + SPEAKER_BEFORE.findall(b) if m not in NOT_NAMES}
        if len(speakers) > 1:
            warns.append(f"beat {i}: two speakers in one beat ({', '.join(sorted(speakers))})")
    if spot:
        term = spot.group(2).strip()
        if not re.search(r"\*\*" + re.escape(term) + r"\*\*", body_text, re.I):
            errs.append(f"spotlight term **{term}** never appears bold in the story body")
    if not BEATS[0] <= len(beats) <= BEATS[1]:
        errs.append(f"{len(beats)} beats ({BEATS[0]}-{BEATS[1]})")
    if not SCENES[0] <= len(body_blocks) <= SCENES[1]:
        errs.append(f"{len(body_blocks)} scenes ({SCENES[0]}-{SCENES[1]} blocks separated by '---')")

    # ---- blessing, prompts
    bless = section(md, r"## Goodnight Blessing\n")
    if bless is None:
        errs.append("missing '## Goodnight Blessing'")
        bw = []
    else:
        bw = words(bless)
        if len(bw) > BLESS_WORDS:
            errs.append(f"blessing is {len(bw)} words (<= {BLESS_WORDS})")
    prompts = section(md, r"## AI Image Prompts\n")
    if prompts is None:
        errs.append("missing '## AI Image Prompts'")
    else:
        n = len(re.findall(r"^\d+\. ", prompts, re.M))
        if n != 3:
            errs.append(f"{n} image prompts (3)")

    # ---- animation notes
    notes = section(md, r"## Animation Notes\n", stop=r"\n## |\Z")
    if notes is None:
        errs.append("missing '## Animation Notes'")
    else:
        cast = re.findall(r"^- \*\*Cast:\*\*|^  - `?[A-Z]{3,}`? ", notes, re.M)
        if not re.search(r"^- \*\*Cast:\*\*", notes, re.M):
            errs.append("Animation Notes: missing '- **Cast:**'")
        toks = re.findall(r"^  - `([A-Z]{3,}[A-Z0-9]*)`", notes, re.M)
        if not toks:
            errs.append("Animation Notes: Cast needs lines like '  - `DAI` — Dai Daruma, design..., voice...'")
        if not re.search(r"^- \*\*Scenes:\*\*", notes, re.M):
            errs.append("Animation Notes: missing '- **Scenes:**'")
        scenes = re.findall(r"^  \d+\. ", notes, re.M)
        if len(scenes) != len(body_blocks):
            errs.append(f"Animation Notes lists {len(scenes)} scenes but the body has {len(body_blocks)} '---' blocks")
        if not re.search(r"^- \*\*Budget:\*\*", notes, re.M):
            errs.append("Animation Notes: missing '- **Budget:**' line")

    # ---- runtime
    narrated = sum(len(words(b)) for b in beats) + len(bw)
    secs = narrated / WPS + GAP * len(beats) + TAIL
    if secs > MAX_SECS:
        errs.append(f"estimated runtime {secs:.0f} s (<= {MAX_SECS}): cut words or beats")
    elif secs < MIN_SECS:
        warns.append(f"estimated runtime {secs:.0f} s is short (aim >= {MIN_SECS})")
    est = f"{int(secs // 60)}:{int(secs % 60):02d}"
    budget = f"- **Budget:** {narrated} narrated words · {len(beats)} beats · {len(body_blocks)} scenes · est. {est}"
    if fix and notes is not None:
        new = re.sub(r"^- \*\*Budget:\*\*.*$", budget, md, count=1, flags=re.M)
        if new != md:
            open(path, "w", encoding="utf-8").write(new)
            md = new
    elif notes is not None and budget not in md:
        warns.append("Budget line is stale (run with --fix)")

    print(f"{name}: {narrated} words, {len(beats)} beats, {len(body_blocks)} scenes "
          f"(max {max(scene_sizes) if scene_sizes else 0}/scene), est {est}")
    for w in warns:
        print("   warn:", w)
    for e in errs:
        print("   FAIL:", e)
    return not errs


if __name__ == "__main__":
    args = sys.argv[1:]
    fix = "--fix" in args
    paths = [a for a in args if a != "--fix"]
    ok = [check(p, fix) for p in paths]
    print(f"\n{sum(ok)}/{len(ok)} pass")
    sys.exit(0 if all(ok) else 1)
