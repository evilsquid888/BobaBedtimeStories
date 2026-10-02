#!/usr/bin/env python3
"""Check a Life Lessons story against the 5-minute spec (SPEC.md, LTX_GUIDE.md).

    python3 lifelessons/check_storyboard.py lifelessons/stories/*.md

Checks: story/blessing word budgets, beats read back the story + blessing word for word,
beat and still counts, words per beat, beats per still, audio endings, Cat present,
pipeline-unsafe words in stills and beats. Estimates runtime from the measured Kokoro rate
(122: 940 words = 7:00 at speed 0.92, gap 0.8).
"""
import re
import sys

WPS = 2.57          # Kokoro jf_alpha,af_heart @ 0.92: words per second of speech (122)
GAP, TAIL = 0.8, 2.5
END = "no music, no voices, no speech"
NIGHT = re.compile(r"\b(night|nighttime|moon|moonlit|moonlight|bedtime|stars?|starry|evening|dusk|asleep|sleeps?|sleeping|night-light)\b", re.I)


def words(t):
    t = re.sub(r"[*_>`]", " ", t)
    return re.findall(r"[\w']+", t.lower().replace("’", "'"))


def section(md, head, stop=r"\n## |\n---"):
    m = re.search(head, md)
    if not m:
        return ""
    rest = md[m.end():]
    e = re.search(stop, rest)
    return rest[:e.start()] if e else rest


def check(path):
    md = open(path, encoding="utf-8").read()
    errs, warns = [], []
    story = section(md, r"## The Story\n")
    bless = section(md, r"## 🌙 Goodnight Blessing\n")
    sw, bw = words(story), words(bless)
    if not 500 <= len(sw) <= 580:
        errs.append(f"story is {len(sw)} words (500-580)")
    if len(bw) > 40:
        errs.append(f"blessing is {len(bw)} words (<= 40)")
    if "Cat the penguin" not in story:
        errs.append('story never says "Cat the penguin"')

    board = md[md.find("## 🎬 Video Storyboard"):]
    shots = re.split(r"\n### Shot \d+", board)[1:]
    if shots:
        shots[-1] = shots[-1].split("### 🖼️")[0]
    beats, cat_shots = [], 0
    for i, sh in enumerate(shots, 1):
        still = re.search(r"\*\*Still:\*\* `([^`]+)`", sh)
        if not still:
            errs.append(f"shot {i}: no **Still:** prompt")
            continue
        sp = still.group(1)
        head = sh.split("\n", 1)[0]
        is_night = "· night" in head
        if bool(NIGHT.search(sp)) != is_night:
            errs.append(f"shot {i}: marked {'night' if is_night else 'day'} but the still "
                        f"{'lacks' if is_night else 'has'} a night word ({(NIGHT.search(sp) or [''])[0]})")
        if "CAT" in sp:
            cat_shots += 1
            if "CAT the little blue penguin" not in sp:
                errs.append(f'shot {i}: still must say "CAT the little blue penguin"')
        if re.search(r"\b(no|without|not|never)\b", sp, re.I):
            warns.append(f"shot {i}: negation in still")
        if '"' in sp:
            errs.append(f"shot {i}: quoted text in still (gets lettered in)")
        bs = re.findall(r"\n\d+\. \*\*Narration:\*\* (.+?)\n\s+`(Shot:[^`]+)`", sh)
        if not 1 <= len(bs) <= 3:
            errs.append(f"shot {i}: {len(bs)} beats (1-3 per still)")
        toks = set(re.findall(r"\b[A-Z]{3,}\b", sp))
        for n, (nar, vp) in enumerate(bs, 1):
            beats.append(nar)
            if len(words(nar)) > 18:
                errs.append(f"shot {i} beat {n}: {len(words(nar))} words of narration (<= 18)")
            if not vp.rstrip(". ").endswith(END):
                errs.append(f"shot {i} beat {n}: audio must end '{END}'")
            for part in ("Shot:", "Scene:", "Action:", "Character:", "Camera:", "Audio:"):
                if part not in vp:
                    errs.append(f"shot {i} beat {n}: missing {part}")
            for t in set(re.findall(r"\b[A-Z]{3,}\b", vp)) - toks:
                errs.append(f"shot {i} beat {n}: names {t}, who is not in the still")
    if not 14 <= len(shots) <= 20:
        errs.append(f"{len(shots)} stills (14-20)")
    if not 36 <= len(beats) <= 48:
        errs.append(f"{len(beats)} beats (36-48)")
    if cat_shots < 2:
        errs.append(f"CAT is in {cat_shots} stills (>= 2)")

    told = words(" ".join(beats))
    want = sw + bw
    if told != want:
        k = next((j for j, (a, b) in enumerate(zip(told, want)) if a != b), min(len(told), len(want)))
        errs.append(f"beats don't read back story+blessing: diverge at word {k}: "
                    f"beats '{' '.join(told[k:k + 8])}' vs story '{' '.join(want[k:k + 8])}'")
    secs = len(want) / WPS + GAP * len(beats) + TAIL
    if secs > 300:
        errs.append(f"estimated runtime {secs:.0f} s (<= 300)")
    print(f"{path.split('/')[-1]}: story {len(sw)} + blessing {len(bw)} words, {len(shots)} stills, "
          f"{len(beats)} beats, Cat in {cat_shots} stills, est {int(secs // 60)}:{int(secs % 60):02d}")
    for w in warns:
        print("   warn:", w)
    for e in errs:
        print("   FAIL:", e)
    return not errs


if __name__ == "__main__":
    ok = [check(p) for p in sys.argv[1:]]
    sys.exit(0 if all(ok) else 1)
