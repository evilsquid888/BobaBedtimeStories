#!/usr/bin/env python3
"""Build a 24 Days of Xmas story (.md with its LTX-2.5 storyboard) from a compact spec.

    python xmas/tools/build.py xmas/specs/00_*.py        # one story
    python xmas/tools/build.py xmas/specs/*.py           # all of them

A spec is a Python file defining STORY (see xmas/specs/00_thanksgiving.py and
xmas/README.md "Writing a new day"). The narration lives in one place, the
beats, so "The Story" and the storyboard can never drift apart. The builder
applies the Life Lessons pipeline rules (lifelessons/SPEC.md, LTX_GUIDE.md)
and refuses to write a file that breaks them. Afterwards run the shared checker:

    python lifelessons/check_storyboard.py xmas/stories/*.md
"""
import glob
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cast import CAST  # noqa: E402

OUT = HERE.parent / "stories"
WPS, GAP, TAIL = 2.57, 0.8, 2.5
END = "no music, no voices, no speech"
NIGHT = re.compile(r"\b(night|nighttime|moon|moonlit|moonlight|bedtime|stars?|starry|evening|dusk|asleep|"
                   r"sleeps?|sleeping|night-light)\b", re.I)
NEG = re.compile(r"\b(no|without|not|never)\b", re.I)
TOKEN = re.compile(r"\b[A-Z]{3,}\b")
CAMERAS = ("pushes in", "pulls back", "pans left", "pans right", "tilts up", "tilts down", "tracks beside",
           "holds still")
PIPELINE = ("Qwen-Image-2.1 stills at 1792×1024, one reference view per character (Sample Images → Character "
            "views), day/night \"pop\" still look · camera_pins.py --motion --hold-end · LTX-2.5 two-stage --hires "
            "(native 1920×1088), --end --end-strength 0.35 · Kokoro jf_alpha,af_heart, speed 0.92, gap 0.8 · "
            "assemble_mp4.py --tail-hold 2.5")
NEGATIVE = ("blurry, jpeg artifacts, distorted hands, extra fingers, watermark, text overlay, photorealistic, "
            "flicker, character morphing, identity drift")
TAILSTYLE = "rounded storybook forms, gentle rim light, expressive faces, clear silhouettes"
VIEW = "single full-body front view on a clean cream background, clear silhouette, consistent storybook proportions"


def words(t):
    t = re.sub(r"[*_>`]", " ", t)
    return re.findall(r"[\w']+", t.lower().replace("’", "'"))


def load(path):
    spec = importlib.util.spec_from_file_location("spec", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.STORY


def still_prompt(shot, places):
    p = places[shot["place"]]
    props = shot.get("props", p["props"])
    return (f"{shot['angle']} {p['name']}: {shot['who']}. The lived-in setting includes {props}. "
            f"{p['light']}, with saturated {p['accents']} accents. {p['atmo']} in layered depth; {TAILSTYLE}.")


def build(path):
    s = load(path)
    cast = dict(CAST)
    cast.update(s.get("extra_cast", {}))
    places, errs = s["places"], []

    def err(msg):
        errs.append(msg)

    story_paras, lines, n = [], [], 0
    for i, sh in enumerate(s["shots"], 1):
        p = places[sh["place"]]
        night = sh.get("time", "day") == "night"
        sp = still_prompt(sh, places)
        toks = set(TOKEN.findall(sp))
        for t in toks - set(s["cast"]):
            err(f"shot {i}: still names {t}, who is not in this story's cast list")
        if bool(NIGHT.search(sp)) != night:
            err(f"shot {i}: marked {'night' if night else 'day'} but the still "
                f"{'lacks' if night else 'has'} a night word ({(NIGHT.search(sp) or [''])[0]})")
        if "CAT" in toks and "CAT the little blue penguin" not in sp:
            err(f'shot {i}: still must say "CAT the little blue penguin"')
        if NEG.search(sp):
            err(f"shot {i}: negation in still ({NEG.search(sp)[0]})")
        if '"' in sp or "`" in sp:
            err(f"shot {i}: quote or backtick in still")
        if not 1 <= len(sh["beats"]) <= 3:
            err(f"shot {i}: {len(sh['beats'])} beats (1-3 per still)")
        lines.append(f"### Shot {i} — {sh['title']} · {'night' if night else 'day'}")
        lines.append(f"**Still:** `{sp}`")
        for b in sh["beats"]:
            n += 1
            nar, framing, action, who, feel, cam, audio = b
            if not sh.get("blessing"):
                story_paras.append(nar)
            if len(words(nar)) > 18:
                err(f"shot {i} beat {n}: {len(words(nar))} words of narration (<= 18): {nar}")
            who = [who] if isinstance(who, str) else list(who)
            for t in set(TOKEN.findall(action)) | set(who):
                if t not in toks:
                    err(f"shot {i} beat {n}: names {t}, who is not in the still")
            for t in who:
                if t not in action:
                    err(f"shot {i} beat {n}: Character lists {t} but the action does not name them")
            if not any(c in cam for c in CAMERAS):
                err(f"shot {i} beat {n}: camera '{cam}' is not one of the pipeline verbs")
            if "`" in nar + action + feel + audio:
                err(f"shot {i} beat {n}: backtick in beat")
            ids = [cast[t][1] for t in who]
            if len(ids) > 1:  # "the little blue penguin and the pink axolotl", as in Life Lessons 54
                ids = [re.sub(r" (with|in) the .*", "", x) for x in ids]
            character = (" and ".join(ids) + " — " + feel) if ids else feel
            # place["motion"] is the ambient motion as a bare clause: "dry leaves swirl over the doormat"
            join = "as" if " while " in action else "while"
            ambient = f", {join} {p['motion']}" if action else p["motion"][0].upper() + p["motion"][1:]
            cam_s = cam if cam.startswith("holds") else f"slowly {cam}"
            lines.append(f"{n}. **Narration:** {nar}")
            lines.append(f"   `Shot: {framing}. Scene: {p.get('scene', p['name'])}. Action: {action}{ambient}. "
                         f"Character: {character}. Camera: {cam_s}. Audio: {audio}, {END}.`")
        lines.append("")

    blessing = [b[0] for sh in s["shots"] if sh.get("blessing") for b in sh["beats"]]
    bless_lines = s["blessing"]
    if words(" ".join(blessing)) != words(" ".join(bless_lines)):
        err("the blessing shot's beats do not read back STORY['blessing']")
    sw, bw = words(" ".join(story_paras)), words(" ".join(bless_lines))
    if not 500 <= len(sw) <= 580:
        err(f"story is {len(sw)} words (500-580)")
    if len(bw) > 40:
        err(f"blessing is {len(bw)} words (<= 40)")
    if "Cat the penguin" not in " ".join(story_paras):
        err('story never says "Cat the penguin"')
    if not 14 <= len(s["shots"]) <= 20:
        err(f"{len(s['shots'])} stills (14-20)")
    if not 36 <= n <= 48:
        err(f"{n} beats (36-48)")
    for must in s.get("must_appear", ("ROSIE", "CAT", "TORI", "MOM")):
        if not any(must in TOKEN.findall(still_prompt(sh, places)) for sh in s["shots"]):
            err(f"{must} is never drawn (the family is in every video)")
    used = set()
    for sh in s["shots"]:
        used |= set(TOKEN.findall(still_prompt(sh, places)))
    for t in s["cast"]:
        if t not in cast:
            err(f"cast token {t} has no design (add it to tools/cast.py or the spec's extra_cast)")
        elif t not in used:
            err(f"cast token {t} is listed but never drawn")
    secs = (len(sw) + len(bw)) / WPS + GAP * n + TAIL
    if secs > 300:
        err(f"estimated runtime {secs:.0f} s (<= 300)")

    name = f"{s['num']}-{s['slug']}.md"
    print(f"{name}: story {len(sw)} + blessing {len(bw)} words, {len(s['shots'])} stills, {n} beats, "
          f"est {int(secs // 60)}:{int(secs % 60):02d}")
    if errs:
        for e in errs:
            print("   FAIL:", e)
        return False

    key = s["shots"][s["key_shot"] - 1]
    md = [f"# {s['num']} — {s['title']}", ""]
    md += [f"**{k}:** {v}" for k, v in s["meta"] if k != "Today's little gift"]
    md += ["", "---", "", "## The Story", ""]
    for para in story_paras:
        md += [para, ""]
    md += ["---", "", "## 🌙 Goodnight Blessing", ""]
    md += bless_lines
    md += ["", "---", "", "## 🎬 Video Storyboard (LTX-2.5)", "",
           f"**Runtime:** ~{int(secs // 60)}:{int(secs % 60):02d} (est.) · **Narrated words:** {len(sw) + len(bw)} · "
           f"**Stills:** {len(s['shots'])} · **Beats:** {n}",
           f"**Pipeline:** {PIPELINE}",
           f"**Video style anchor (every beat):** `rich storybook animation, Pixar-meets-picture-book, {s['palette']}, "
           "gentle rim light, glowing highlights, deep layered depth, lively gentle character animation, "
           "expressive faces, blinking, small natural gestures`",
           f"**Negative prompt:** `{NEGATIVE}`",
           f"**Cast** (TOKEN → ID phrase · design for the reference view). {s['cast_note']}"]
    md += [f"- `{t}` → {cast[t][0]}, {cast[t][1]} · `{cast[t][2]}`" for t in s["cast"]]
    md += [""] + lines
    md += ["### 🖼️ Sample Images (to generate first)", "",
           f"1. **Key scene** — `{still_prompt(key, places)}`",
           "2. **Character views** — generate each of these as a separate image:"]
    md += [f"   - `{cast[t][2]}; {VIEW}`" for t in s["cast"]]
    md += [f"3. **Closing scene** — `{still_prompt(s['shots'][-1], places)}`", ""]
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text("\n".join(md), encoding="utf-8", newline="\n")
    return True


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    paths = [p for a in sys.argv[1:] for p in sorted(glob.glob(a))]
    if not paths:
        sys.exit("usage: python xmas/tools/build.py xmas/specs/NN_*.py")
    sys.exit(0 if all([build(p) for p in paths]) else 1)
