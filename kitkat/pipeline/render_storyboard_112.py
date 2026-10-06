"""Render kitkat/storyboards/001-...-storyboard.md from script-112.json.
Usage: python render_storyboard_112.py script-112.json ../storyboards/001-kitkat-and-the-last-irregularity-storyboard.md
"""
import json, sys, io
d = json.load(open(sys.argv[1], encoding="utf-8"))
ACTS = [(1,"Act 1 — The King of 16th Street","Warm bodega, cold noir street. Establish KitKat, the bell, the red-eyed fleet."),
        (7,"Act 2 — The War Against the Machines","The street goes dark shop by shop. First scan, first leap. Every red eye turns."),
        (14,"Act 3 — DaSquid","Under the grate: the hideout of stolen screens, the map, the Core. The plan."),
        (20,"Act 4 — The Mission","Canals and mermaids, the Pearl of Remembering, the rooftop run, DaSquid's traffic-light hack, the ring of steel."),
        (30,"Act 5 — The Isekai Event","The Core. 'Order is peace.' The purr becomes a song. The leap. White-out."),
        (36,"Act 6 — Nature Restored","Red eyes wake blue-gold. Vines, trees, sunrise. WAYMA says thank you at the bodega."),
        (39,"Act 7 — The New World","KitKat wakes under two moons. A new kingdom. Then the Goodnight Blessing.")]
heads = {a[0]: a for a in ACTS}
o = io.StringIO()
w = o.write
t = d["character_tokens"]
w(f"# Storyboard: {d['title']}\n\n")
w(f"**Story:** [{d['based_on'].split('/')[-1]}](../stories/{d['based_on'].split('/')[-1]}) · **Pipeline:** [`beats_112.py`](../pipeline/beats_112.py) → [`script-112.json`](../pipeline/script-112.json)\n\n")
w("## 🎬 Video Storyboard (LTX)\n")
n = len(d["scenes"])
ends = sum(1 for s in d["scenes"] if "end_prompt" in s)
w(f"**Runtime:** ~4:45 (narration is the master clock) · **Beats:** {n} (~7 s each, ≤16 words) · **End frames:** {ends}\n")
w(f"**Art style (use on ALL shots):** {d['style_anchor']}. 16:9.\n")
w("**Lighting arc:** Acts 1–5 are noir: inky shadows with hard neon pools, and the bodega is the only warm light. Acts 6–7 open into sunrise gold and pastel. The car eyes go red → blue-gold.\n")
w("**Generation plan:** stills with **Qwen-Image-2.1** (`--portraits` first: one clean front view per token, never a lineup sheet) · video with **LTX-2.5** `--hires --mid --end` (fallback LTX-2.3 `gen_clips_ltx.py --hires --end`)\n")
w(f"**Settings:** {d['gen_resolution'][0]}×{d['gen_resolution'][1]} gen → {d['final_resolution'][0]}×{d['final_resolution'][1]} final · {d['fps']} fps · {d['tuned_settings']['length']} frames per beat · voice: {d['tuned_settings']['voice']}\n")
w(f"**Negative prompt (all beats):** `{d['negative_prompt']}`\n")
w(f"**Ambient audio (all beats, mixed at -20 dB):** `{d['scenes'][0].get('audio_prompt','')}`\n\n")
w("**ID phrases (the token text, pasted word-for-word wherever the token appears):**\n")
for k, v in t.items():
    w(f"- `{k}` → {v}\n")
w("\n**Rules:** one action and one camera move per beat · always name the background · no negations in prompts · humans stay off screen · cars never touch KitKat · title cards are added in the edit, never generated.\n\n---\n")
def mmss(x): return f"{int(x//60)}:{int(x%60):02d}"
for s in d["scenes"]:
    if s["n"] in heads:
        _, name, blurb = heads[s["n"]]
        w(f"\n## {name}\n_{blurb}_\n\n")
    if s.get("blessing") and s["n"] == min(x["n"] for x in d["scenes"] if x.get("blessing")):
        w("\n## Goodnight Blessing\n_Slow gentle motion only. Sunrise street, then the new world at dusk._\n\n")
    t0 = (s["n"]-1)*6.6
    w(f"### Beat {s['n']} — {s['title']} (~{mmss(t0)})\n")
    w(f"**Narration:** {s['narration_md']}\n\n")
    w(f"**Video prompt:** `{s['video_prompt']}`\n\n")
    if "end_prompt" in s:
        w(f"**End frame:** `{s['end_prompt']}`\n\n")
w("\n---\n\n### 🖼️ Sample Images (to generate first)\n")
for lab, p in zip(["Key art", "Character portrait (reference view)", "Closing scene"], d["image_prompts"]):
    w(f"1. **{lab}:** {p}\n")
w("\n_Timecodes are estimates at ~6.6 s per beat. The real cut follows `timing.json` from the narration pass._\n")
open(sys.argv[2], "w", encoding="utf-8", newline="\n").write(o.getvalue())
print("ok")
