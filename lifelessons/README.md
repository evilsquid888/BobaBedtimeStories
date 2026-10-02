# 🌹 Life Lessons — Rosie's Step-by-Step Stories

11 cozy bedtime stories that teach everyday social skills, one clear step at a time. **Rosie the Rose Milk Tea** is a sweet, slightly nervous little drink who gets brave once she knows the steps. Friends from the Taiwan, Japan, and Costa Rica collections coach her. Her big sister **Tori** is always there to cheer, her little sister **Bud** tags along (usually with a sock), and **Cat the penguin** — a sleepy little blue penguin from Frostpeak staying with Rosie's family — comes on every adventure and naps somewhere new each time.

Written as a gentle social-skills guide (in the style of social stories), and useful for kids who do best with clear, literal, repeatable steps.

See also: [Character Guide](CHARACTER_GUIDE.md) · [Writing Spec](SPEC.md) · [🎬 LTX 2.5 Video Guide](LTX_GUIDE.md)

## How every story works
- **Model → Practice → Do.** A coach shows the step, Rosie practices at home, then does it for real.
- **Rosie's Steps**: 4–6 numbered steps, word-for-word the same every time they appear.
- **Magic sentence**: the one exact thing to say (in **bold**).
- **A small surprise** happens, and Rosie handles it with a **Rose breath** (smell the rose: in for 4; blow out the candle: out for 4) and a backup sentence.
- **Practice Together**: role-play tips for grown-ups.
- **5 minutes, read aloud**: each story is 500–580 words plus a 4-line blessing, so the narrated video lands at about 4:20–4:50.
- **Video Storyboard**: 14–20 rich "pop" stills and 36–48 one-action LTX-2.5 beats in screenplay form, each beat carrying its own line of narration, plus sample-image prompts (key scene, one view per character, closing scene). `python3 check_storyboard.py stories/*.md` checks every story against the spec.

## Story Index

| # | Story | Life Skill | Magic Sentence | Coaches |
|---|-------|-----------|----------------|---------|
| 1 | [Rosie Makes a Friend on the Train](stories/01-rosie-makes-a-friend-on-the-train.md) | Starting a conversation | "Hi! I'm Rosie. What's your name?" | Boba 🇹🇼, Momo Mochi 🇯🇵 |
| 2 | [Rosie Asks for Help at the Grocery Store](stories/02-rosie-asks-for-help-at-the-grocery-store.md) | Asking a worker for help | "Excuse me, can you help me find the honey?" | Taro 🇹🇼, Gallo & Pinto 🇨🇷 |
| 3 | [Rosie Orders a Drink at Starbucks](stories/03-rosie-orders-a-drink-at-starbucks.md) | Ordering at a coffee shop | "Hi! Can I please have a small hot chocolate?" | Don Café 🇨🇷, Bīng 🇹🇼 |
| 4 | [Rosie Answers the Phone](stories/04-rosie-answers-the-phone.md) | Answering the phone | "Hello, this is Rosie. Who is calling, please?" | Aiyu 🇹🇼, Tico the Toucan 🇨🇷 |
| 5 | [Rosie Calls Her Big Sister Tori](stories/05-rosie-calls-her-big-sister-tori.md) | Making a phone call | "Hi Tori, it's Rosie! Do you have time to talk?" | Mochi 🇹🇼, Pock Ramune 🇯🇵 |
| 6 | [Rosie Asks to Play at the Park](stories/06-rosie-asks-to-play-at-the-park.md) | Joining play and handling "no" | "Hi! Can I play with you?" | Mango 🇹🇼, Dai Daruma 🇯🇵, Tato 🇨🇷 |
| 7 | [Rosie Asks the Librarian](stories/07-rosie-asks-the-librarian.md) | Library voice, waiting, asking | "Excuse me, where can I find books about sea turtles?" | Dora the Dorayaki 🇯🇵, Slowy the Sloth 🇨🇷 |
| 8 | [Rosie Buys Boba](stories/08-rosie-buys-boba.md) | Ordering boba (sugar and ice levels) | "Hi! Can I please have a pearl milk tea, half sugar, less ice?" | Boba 🇹🇼, Hóng Dòu 🇹🇼, Tama Onigiri 🇯🇵 |
| 9 | [Rosie Finds a Safe Helper](stories/09-rosie-finds-a-safe-helper.md) | What to do if separated from a grown-up | "I can't find my mom. Can you help me?" | Caǎo 🇹🇼, Estrella 🇨🇷, Flan 🇨🇷 |
| 10 | [Rosie Pays at the Checkout](stories/10-rosie-pays-at-the-checkout.md) | Paying and waiting for change | "Hi! Just this, please." | Feng 🇹🇼, Neko-Pan 🇯🇵, Lala 🇨🇷 |
| 11 | [Rosie Says Goodbye at the Party](stories/11-rosie-says-goodbye-at-the-party.md) | Leaving a party: gather, find the hosts, say thank you, leave together | "Thank you for having us. We had fun!" | Marcus 🧭 (teen Inclusive Navigator), Feng 🇹🇼, Mochi 🇹🇼 |

## Making the videos (LTX-2.5)
See **[LTX_GUIDE.md](LTX_GUIDE.md)** for the full guide; it follows the local pipeline in `bedtime-video-pipeline` (RUNBOOK "Current production path"). The short version:
1. Make one reference view per character (Sample Images → Character views).
2. Generate each shot's still from its **Still** prompt (Qwen-Image-2.1, 1792×1024, the pipeline adds the day/night "pop" look).
3. Animate each **beat** on LTX-2.5 two-stage `--hires`, motion-mode camera pins, soft end pin 0.35.
4. Narrate the beats' **Narration** lines with Kokoro `jf_alpha,af_heart` at 0.92, then assemble. About 5 minutes.
