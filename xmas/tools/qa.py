#!/usr/bin/env python3
"""Series QA for 24 Days of Xmas: what build.py and check_storyboard.py do not check.

    python xmas/tools/qa.py                 # every spec
    python xmas/tools/qa.py --terms         # also list every Mandarin/French term for proofreading
    python xmas/tools/qa.py --repeats       # also list lines and jokes repeated across stories

FAIL = breaks a series rule. warn = a pipeline hazard or an editorial flag to look at by eye.
"""
import collections
import glob
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build import TOKEN, load, still_prompt, words  # noqa: E402

FAMILY = ("ROSIE", "CAT", "TORI", "MOM")
NAMES = {"ROSIE": "Rosie", "CAT": "Cat", "TORI": "Tori", "MOM": "Mom"}
# Simplified forms of characters these stories are likely to use; the series is traditional (Taiwan).
SIMPLIFIED = set("节帮灯谢欢乐圣诞饼汤圆团爷门车冻说这个们吗为对时东热红笼蜡烛鱼饺寿长妈礼铃钟树邮给写画飞风筝极鲨鱿来葱姜纸"
                 "赛赢输转独鲸间请听声关没开温脚岁亲爱难过兴会还样边发现点儿后见让总轻紧张担惊讶")
HUMANS = re.compile(r"\b(people|person|persons|child|children|kids?|man|woman|men|women|crowds?|shopkeepers?|"
                    r"villagers?|hands?|fingers?|boys?|girls?|skaters?|shoppers?|passengers?|tourists?|vendors?|"
                    r"bakers?|carvers?|conductors?|drivers?|families|strangers?|grown-ups?|humans?|riders?|singers?)\b",
                    re.I)
LETTERING = re.compile(r"\b(signs?|labels?|lettering|letters|words?|written|writing|numbers?|numerals?|menus?|"
                       r"readable|text|captions?|initials|names?)\b", re.I)
LIPSYNC = re.compile(r"\b(says?|sings?|shouts?|whispers?|talks?|speaks?|calls out|tells?|explains?|announces?|"
                     r"asks|answers|recites?|reads aloud|counts aloud)\b", re.I)
WALKS = re.compile(r"\b(walks?|runs?|strides?|marches|exits?|enters?|strolls?|dashes|races off|chases)\b",
                   re.I)
ROLLS = re.compile(r"\b(rolls?|rolling|spins?|spinning|twirls?|tumbles?|somersaults?|cartwheels?)\b", re.I)
ROUND = ("BOBA", "MOCHI", "NOA", "SESAME", "TANGYUAN", "COUIC", "ROSIE", "TORI", "MOM", "LINA", "HONGDOU",
         "YEHYEH", "PINTO", "GALLO")
VOCAL = re.compile(r"\b(gasps?|sighs?|giggl\w*|laugh\w*|chuckl\w*|cheer\w*|murmur\w*|sniffl\w*|humming|"
                   r"sing\w*|shout\w*|whisper\w*|yell\w*|squeal\w*|voices?|chatter\w*|gulps?|whoops?|carol\w*)\b",
                   re.I)
CJK = re.compile(r"\*\*([一-鿿]+)\*\* \(([^)]+)\) = ([^.,!?\"”]+)")
LATIN_TERM = re.compile(r"\*\*([A-Za-zÀ-ÿ' -]+)\*\* \(([^)]+)\) = ([^.,!?\"”]+)")
RITUAL = ("smell the rose", "blow out the candle", "one more light", "one step at a time", "you've got this",
          "that's okay", "took a rose breath", "cat the penguin", "in two three four", "out two three four")


def qa(path, corpus):
    s = load(path)
    day = int(s["num"])
    fails, warns = [], []
    shots, places = s["shots"], s["places"]
    stills = [still_prompt(sh, places) for sh in shots]
    story_beats = [b for sh in shots if not sh.get("blessing") for b in sh["beats"]]
    text = " ".join(b[0] for b in story_beats)
    low = " ".join(words(text))

    # --- structure -----------------------------------------------------------
    pnames = [places[sh["place"]]["name"] for sh in shots]
    if day >= 1:
        first_hall = next((i for i, n in enumerate(pnames) if "great hall" in n), None)
        if first_hall is None:
            fails.append("never visits the Door Wall")
        elif first_hall > (6 if day == 1 else 1):
            warns.append(f"the Door Wall first appears in shot {first_hall + 1}")
        if "one more light" not in low:
            fails.append('nobody says "One more light."')
        lane_night = [i for i, sh in enumerate(shots) if "Lantern Lane" in pnames[i] and sh.get("time") == "night"]
        if not lane_night and day != 15:
            fails.append("no night shot on Lantern Lane (the lantern hanging)")
        if "bunk room" not in pnames[-1]:
            fails.append("last shot is not the bunk room")
        if "lantern" not in low:
            fails.append("the story never mentions a lantern")
    if not shots[-1].get("blessing") or shots[-1].get("time") != "night":
        fails.append("last shot must be the night blessing")
    seen_night = False
    for i, sh in enumerate(shots, 1):
        night = sh.get("time") == "night"
        if seen_night and not night:
            warns.append(f"shot {i} is day after an earlier night shot (time runs backwards?)")
            break
        seen_night = seen_night or night

    # --- the family ----------------------------------------------------------
    for t in FAMILY:
        n = sum(t in TOKEN.findall(sp) for sp in stills[:-1])
        acts = sum(t in (b[3] if isinstance(b[3], (list, tuple)) else [b[3]]) for b in story_beats)
        if NAMES[t] not in text:
            fails.append(f"{NAMES[t]} is never named in the narration")
        if n < 2 or acts < 1:
            warns.append(f"{NAMES[t]} is thin: {n} stills before the blessing, the subject of {acts} beats")
    m = re.search(r"\bCat\b", text)
    if m and not text[m.start():].startswith("Cat the penguin"):
        warns.append('the first "Cat" in the narration is not "Cat the penguin"')
    if not re.search(r"(said|called|cheered|whispered|laughed|giggled) Tori|Tori (said|called|cheered|whispered|"
                     r"laughed|giggled|squeezed|hugged)", text):
        warns.append("Tori has no clear line or hug")
    if not re.search(r"(said|called|whispered|laughed) Mom|Mom (said|called|whispered|laughed|smiled|lifted|"
                     r"stirred|flipped|poured|tucked|wrapped|held|carried|handed|nodded|helped)", text):
        warns.append("Mom has no clear line or action")
    if not any(k == "Cat’s role" for k, _ in s["meta"]):
        warns.append("meta has no Cat’s role line")

    # --- fun and warm, not a lesson -------------------------------------------
    for rx, label in ((r"that's okay", '"That\'s okay." (the named-feeling formula)'),
                      (r"rose breath|smell the rose|blow out the candle out", "the Rose breath"),
                      (r"one sip at a time", '"One step at a time, one sip at a time."'),
                      (r"\b(learned|lesson|step (one|two|three|four))\b", "teaching language"),
                      (r"\bfelt (worried|nervous|sad|scared|shy|cross|frustrated|homesick|lonely)\b",
                       "a named-feeling line")):
        if re.search(rx, low):
            warns.append(f"life-lesson style: {label}")

    # --- continuity ----------------------------------------------------------
    if re.search(r"\bsecrets?\b", low):
        warns.append('uses the word "secret" (the lantern plan is a surprise)')
    if 1 <= day < 20 and "YEHYEH" in s["cast"]:
        fails.append("Yeh Yeh is drawn before he arrives on day 20")
    if "GABBY" in s["cast"]:
        for i, (sh, sp) in enumerate(zip(shots, stills), 1):
            if sh.get("time") != "night" and re.search(r"\b(stars?|starry)\b", sp, re.I):
                fails.append(f"shot {i}: 'star' in a day still with Gabby")
    if len(s["cast"]) > 9 and day != 24:
        warns.append(f"{len(s['cast'])} drawn characters (aim for 9 or fewer)")
    if day in (9, 12, 17, 18) and "ticket" not in low:
        fails.append("a Market Train day whose story never mentions the ticket")

    # --- language ------------------------------------------------------------
    cjk = CJK.findall(text)
    if not 1 <= len(cjk) <= 4:
        warns.append(f"{len(cjk)} Mandarin terms (2-4; 1-2 on a Market Train day)")
    for zh, py, en in cjk:
        bad = [c for c in zh if c in SIMPLIFIED]
        if bad:
            fails.append(f"simplified characters in {zh}: {''.join(bad)}")
    bare = re.findall(r"[一-鿿]+", re.sub(r"\*\*[一-鿿]+\*\* \([^)]+\) = ", "", text))
    if bare:
        warns.append(f"Chinese without pinyin and meaning: {' '.join(bare)}")

    # --- prompt hazards ------------------------------------------------------
    for i, (sh, sp) in enumerate(zip(shots, stills), 1):
        body = sp.split(". The lived-in setting")[0]
        toks = TOKEN.findall(sp)
        if len(set(toks)) > 6:
            warns.append(f"shot {i}: {len(set(toks))} characters in one still")
        for t, c in collections.Counter(toks).items():
            if c > 2:
                warns.append(f"shot {i}: {t} is named {c} times in the still (one place per character)")
        for rx, label in ((HUMANS, "may draw humans"), (LETTERING, "may draw lettering")):
            hit = sorted({h.lower() for h in rx.findall(sp)})
            if hit:
                warns.append(f"shot {i}: still {label}: {', '.join(hit)}")
        if re.search(r"ROSIE[^;.]*\b(walks?|runs?|climbs?|skates?|dances?|kneels?|crawls?|leaps?|rides?|skis)\b", body):
            warns.append(f"shot {i}: pose-risky Rosie in the still (she is a cup)")
        if "ROSIE" in toks and "small clear cup" not in sp and re.search(
                r"ROSIE[^;.]*\b(snowboard|sled|toboggan|skat|slid|glid|carr|hug)", body):
            warns.append(f"shot {i}: Rosie in an action pose without being spelled out as a cup")
        for b in sh["beats"]:
            nar, framing, action, who, feel, cam, audio = b
            tag = f"shot {i} «{nar[:34]}…»"
            if LIPSYNC.search(action):
                warns.append(f"{tag}: action asks for speech ({LIPSYNC.search(action)[0]}); no lip sync")
            if WALKS.search(action):
                warns.append(f"{tag}: action is a walk or exit ({WALKS.search(action)[0]}); use a held pose")
            if ROLLS.search(action) and any(t in action for t in ROUND):
                warns.append(f"{tag}: a round character rolls or spins ({ROLLS.search(action)[0]})")
            if HUMANS.search(action):
                warns.append(f"{tag}: action may draw humans ({HUMANS.search(action)[0]})")
            if VOCAL.search(audio):
                warns.append(f"{tag}: audio has a voice sound ({VOCAL.search(audio)[0]}) before 'no voices'")
            if len(action.split()) > 26:
                warns.append(f"{tag}: action is {len(action.split())} words; one action per beat")
    for i in range(1, len(shots)):
        a, b = shots[i - 1]["angle"].split()[:2], shots[i]["angle"].split()[:2]
        if a == b:
            warns.append(f"shots {i} and {i + 1} open with the same camera angle ({' '.join(a)})")
    for k, p in places.items():
        if HUMANS.search(p["motion"]) or re.search(r"\b(cars?|trains?|sleds?|buses)\b", p["motion"]):
            warns.append(f"place '{k}': ambient motion has passers-by or vehicles")
    if not 1 <= s["key_shot"] <= len(shots):
        fails.append("key_shot is out of range")

    corpus[s["num"]] = {"title": s["title"], "text": text, "cast": s["cast"], "terms": cjk,
                        "latin": LATIN_TERM.findall(text),
                        "places": [p["name"] for p in places.values()]}
    print(f"{s['num']} {s['title']}: {len(fails)} FAIL, {len(warns)} warn · cast {len(s['cast'])}: "
          f"{' '.join(s['cast'])}")
    for f in fails:
        print("   FAIL:", f)
    for w in warns:
        print("   warn:", w)
    return not fails


def sentences(text):
    return [re.sub(r"\s+", " ", x).strip() for x in re.split(r"(?<=[.!?])[\"”]?\s+", text) if len(words(x)) >= 4]


def series(corpus, show_terms, show_repeats):
    print("\n== Series ==")
    shared = ("great hall", "Lantern Lane", "bunk room")
    owners = collections.defaultdict(list)
    for num, c in corpus.items():
        for p in set(c["places"]):
            if not any(x in p for x in shared):
                owners[p].append(num)
    for p, nums in owners.items():
        if len(nums) > 1:
            print(f"   warn: place reused in {', '.join(nums)}: {p}")
    grams = collections.defaultdict(set)
    for num, c in corpus.items():
        w = words(c["text"])
        for i in range(len(w) - 5):
            g = " ".join(w[i:i + 6])
            if not any(r in g or g in r for r in RITUAL):
                grams[g].add(num)
    pair = collections.Counter()
    for g, nums in grams.items():
        for a in nums:
            for b in nums:
                if a < b:
                    pair[(a, b)] += 1
    for (a, b), n in pair.most_common(8):
        if n >= 6:
            print(f"   warn: stories {a} and {b} share {n} six-word runs")
    if show_repeats:
        print("\n-- Lines that appear in 3 or more stories --")
        sent = collections.defaultdict(set)
        for num, c in corpus.items():
            for x in sentences(c["text"]):
                sent[" ".join(words(x))].add(num)
        for x, nums in sorted(sent.items(), key=lambda kv: -len(kv[1])):
            if len(nums) >= 3:
                print(f"   {len(nums):2d}× {x}  [{' '.join(sorted(nums))}]")
        print("\n-- Running gags (stories that use each) --")
        for label, rx in (("taste-test", r"taste testing|taste test"), ("only bite", r"only bite"),
                          ("poof", r"\bpoof\b"), ("little sip", r"little sip"),
                          ("màn man lái", r"màn man lái"),
                          ("bonjour-hi", r"bonjour hi"), ("noble act", r"noble act"),
                          ("descended with style", r"descended with style"),
                          ("how do I stop", r"how do i stop"), ("enough fish", r"enough fish"),
                          ("smallest step", r"smallest step"), ("cocoa first", r"cocoa first")):
            nums = [n for n, c in corpus.items() if re.search(rx, " ".join(words(c["text"])))]
            print(f"   {len(nums):2d}× {label}: {' '.join(nums)}")
    if show_terms:
        print("\n-- Terms to proofread --")
        for num, c in corpus.items():
            for zh, py, en in c["terms"]:
                print(f"   {num}  {zh}  ({py})  = {en.strip()}")
            for fr, pr, en in c["latin"]:
                print(f"   {num}  {fr}  ({pr})  = {en.strip()}")
    use = collections.Counter(t for c in corpus.values() for t in c["cast"])
    print("\n-- Appearances --")
    print("   " + ", ".join(f"{t} {n}" for t, n in use.most_common()))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    paths = sorted(p for a in (args or [str(HERE.parent / "specs" / "*.py")]) for p in glob.glob(a))
    corpus = {}
    ok = [qa(p, corpus) for p in paths]
    series(corpus, "--terms" in sys.argv, "--repeats" in sys.argv)
    sys.exit(0 if all(ok) else 1)
