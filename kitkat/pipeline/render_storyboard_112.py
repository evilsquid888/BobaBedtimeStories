"""Render kitkat/storyboards/001-...-storyboard.md from script-112.json.
Usage: python render_storyboard_112.py script-112.json ../storyboards/001-kitkat-and-the-last-irregularity-storyboard.md
"""
import json, sys, io
d = json.load(open(sys.argv[1], encoding="utf-8"))
ACTS = [(1,"Scene 1 — The King of 16th Street","Bodega at night: the one warm pool of light. Establish KitKat, the bell, the wish."),
        (6,"Scene 2 — The War on the Street","The red-eyed fleet. WAYMA's perfect city. Shop by shop the neon goes dark."),
        (9,"Scene 3 — Irregularity Detected","The scan, the leap, the tentacle in the sewer grate."),
        (14,"Scene 4 — DaSquid","The flooded subway hideout. Eight arms, zero bosses. The Tower and the Core."),
        (19,"Scene 5 — The Mermaid's Pearl","The singing canals. Coral and the Pearl of Remembering."),
        (24,"Scene 6 — The Rooftop Run","The run, the fall into the gutter, DaSquid's traffic-light hack, the soar."),
        (29,"Scene 7 — The Ring of Steel","The cars ring the tower. A vent the size of a cereal box."),
        (31,"Scene 8 — The Isekai Event","The Core. 'Order is peace.' The purr becomes a song. The leap. White-out."),
        (38,"Scene 9 — Nature Restored","Sunrise. Red eyes wake blue-gold. Vines and trees. A flower at the bodega."),
        (43,"Scene 10 — The New World","Two moons, floating islands, a sneeze, Coral waving. A new kingdom.")]
heads = {a[0]: a for a in ACTS}
o = io.StringIO()
w = o.write
t = d["character_tokens"]
w(f"# Storyboard: {d['title']}\n\n")
w(f"**Story:** [{d['based_on'].split('/')[-1]}](../stories/{d['based_on'].split('/')[-1]}) · **Pipeline:** [`beats_112.py`](../pipeline/beats_112.py) → [`script-112.json`](../pipeline/script-112.json)\n\n")
w("## 🎬 Video Storyboard (LTX)\n")
n = len(d["scenes"])
ends = sum(1 for s in d["scenes"] if "end_prompt" in s)
w(f"**Runtime:** ~4:50 (narration is the master clock) · **Beats:** {n} (~7 s each, ≤16 words) · **End frames:** {ends}\n")
w(f"**Art style (use on ALL shots):** {d['style_anchor']}. 16:9.\n")
w("**Lighting arc:** Scenes 1–8 are noir: inky shadows with hard neon pools, and the bodega is the only warm light. Scenes 9–10 open into sunrise gold and pastel. The car eyes go red → blue-gold.\n")
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
    t0 = (s["n"]-1)*6.3
    w(f"### Beat {s['n']} — {s['title']} (~{mmss(t0)})\n")
    w(f"**Narration:** {s['narration_md']}\n\n")
    w(f"**Video prompt:** `{s['video_prompt']}`\n\n")
    if "end_prompt" in s:
        w(f"**End frame:** `{s['end_prompt']}`\n\n")
w("\n---\n\n### 🖼️ Sample Images (to generate first)\n")
for lab, p in zip(["Key art", "Character portrait (reference view)", "Closing scene"], d["image_prompts"]):
    w(f"1. **{lab}:** {p}\n")
w("\n_Timecodes are estimates at ~6.3 s per beat. The real cut follows `timing.json` from the narration pass._\n")
open(sys.argv[2], "w", encoding="utf-8", newline="\n").write(o.getvalue())
print("ok")
