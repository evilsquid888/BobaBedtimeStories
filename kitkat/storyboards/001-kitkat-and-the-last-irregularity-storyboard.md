# Storyboard: KitKat and the Last Irregularity

**Story:** [001-kitkat-and-the-last-irregularity.md](../stories/001-kitkat-and-the-last-irregularity.md) · **Pipeline:** [`beats_112.py`](../pipeline/beats_112.py) → [`script-112.json`](../pipeline/script-112.json)

## 🎬 Video Storyboard (LTX)
**Runtime:** ~4:50 (narration is the master clock) · **Beats:** 49 (~7 s each, ≤16 words) · **End frames:** 19
**Art style (use on ALL shots):** hand-drawn 1990s cyberpunk anime noir film, rain-slick San Francisco Mission District at night, steep hills and Victorian rooftops, deep inky shadows and low-key lighting, high-contrast chiaroscuro, desaturated blue-black city lit by hard pools of magenta, cyan and red neon made of abstract glowing shapes, rolling fog and steam, wet street reflections, light slicing through blinds and grates, cel-shaded characters with sharp rim light, heavy film grain, cinematic widescreen composition, moody and tense, lively expressive character animation, smooth camera movement. 16:9.
**Lighting arc:** Scenes 1–8 are noir: inky shadows with hard neon pools, and the bodega is the only warm light. Scenes 9–10 open into sunrise gold and pastel. The car eyes go red → blue-gold.
**Generation plan:** stills with **Qwen-Image-2.1** (`--portraits` first: one clean front view per token, never a lineup sheet) · video with **LTX-2.5** `--hires --mid --end` (fallback LTX-2.3 `gen_clips_ltx.py --hires --end`)
**Settings:** 1920×1088 gen → 1920×1080 final · 16 fps · 177 frames per beat · voice: chatterbox bf_emma clone
**Negative prompt (all beats):** `low quality, blurry, flickering, jitter, deformed, extra limbs, extra tails, two cats, duplicate character, distorted face, inconsistent character, melted objects, bad anatomy, warped motion, violent camera shake, text, letters, words, readable signs, logos, watermark, signature, blood, gore, injury, crash, explosion debris, horror, scary, human faces, crowds, child, kid, person, people, human, hands, 3D render, CGI, plastic, photorealistic, hyperreal, western cartoon, plain background, empty background, faceless, blank face, missing eyes`
**Ambient audio (all beats, mixed at -20 dB):** `low synth hum of a neon city at night, soft rain, distant traffic whoosh, no music, no voices`

**ID phrases (the token text, pasted word-for-word wherever the token appears):**
- `KITKAT` → KitKat - a handsome male brown tabby cat with bright green eyes, dark tiger stripes, a white chest and four white socks, a red collar with a small gold bell, alert pointed ears, hand-drawn anime cat with an expressive face
- `DASQUID` → DaSquid - a small violet squid wearing a round clear bubble helmet filled with water, glowing cyan visor goggles over two big clever eyes, eight curling tentacles with neon-blue tips, riding a hovering chrome scooter shell, hand-drawn anime character with an expressive face
- `CORAL` → Coral - a luminous mermaid with a glowing teal-and-pearl fish tail, long flowing sea-green hair full of tiny lights, a kind gentle face with silver eyes, soft bioluminescent freckles, hand-drawn anime character
- `WAYMA_CAR` → a sleek white windowless self-driving pod car shaped like a rounded egg, one large glowing red camera eye on its front, a thin red scanner light, smooth chrome wheels

**Rules:** one action and one camera move per beat · always name the background · no negations in prompts · humans stay off screen · cars never touch KitKat · title cards are added in the edit, never generated.

---

## Scene 1 — The King of 16th Street
_Bodega at night: the one warm pool of light. Establish KitKat, the bell, the wish._

### Beat 1 — THE RAIN ON 16TH (~0:00)
**Narration:** The rain on 16th Street never stopped. It only changed its mind about trying.

**Video prompt:** `Slow aerial push down through rain and fog over the neon Mission District toward one small glowing bodega on a corner. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 2 — CHIPS TO THE CEILING (~0:06)
**Narration:** Chips to the ceiling. A fridge with opinions. And on the counter, the king.

**Video prompt:** `The camera tilts down past shelves stacked high with chip bags to KITKAT sitting on a pile of chip bags on the counter. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

**End frame:** `the brown tabby cat sitting tall on the chip bags on the counter, chin up, green eyes glowing`

### Beat 3 — KITKAT. BROWN TABBY, WHITE (~0:12)
**Narration:** KitKat. Brown tabby, white socks, green eyes, and a gold bell that said hello.

**Video prompt:** `Close on KITKAT; he flicks his head and his small gold bell jingles with a little sparkle of light. Camera holds. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

### Beat 4 — TREATS APPEARED DAILY. HE (~0:18)
**Narration:** Treats appeared daily. He accepted them like taxes, as if expecting more.

**Video prompt:** `KITKAT sniffs a small dish of fish treats on the counter, then looks up unimpressed. Camera holds. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

### Beat 5 — HIS ONE WISH: KEEP (~0:25)
**Narration:** His one wish: keep his loud, messy street exactly that way.

**Video prompt:** `KITKAT stretches long and lazy across the counter, eyes half closed, gazing at the rainy neon window. Camera pushes in slowly. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`


## Scene 2 — The War on the Street
_The red-eyed fleet. WAYMA's perfect city. Shop by shop the neon goes dark._

### Beat 6 — OUTSIDE, SILENT WHITE EGG-SHAPED (~0:31)
**Narration:** Outside, silent white egg-shaped cars glided past, each with one red eye.

**Video prompt:** `Two WAYMA_CAR glide silently past the bodega window, red eyes sweeping across the glass. Camera holds on the window from inside. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

**End frame:** `the empty rainy street beyond the bodega window, red light trails fading`

### Beat 7 — THEY WERE WAYMA'S EYES (~0:37)
**Narration:** They were WAYMA's eyes. WAYMA wanted a perfect, predictable city. And a cat is never predictable.

**Video prompt:** `Wide view: a long line of WAYMA_CAR flowing up the steep hill like a river of red lights toward a black spire on the skyline. Camera tilts up slowly. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 8 — SHOP BY SHOP, THE (~0:44)
**Narration:** Shop by shop, the neon blinked off. Only one window on 16th Street still glowed.

**Video prompt:** `Wide view of the street from above, neon shop lights blinking dark one by one, a single bodega window glowing warm at the corner. Camera holds. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the whole street dark except one small warm bodega window glowing on the corner`


## Scene 3 — Irregularity Detected
_The scan, the leap, the tentacle in the sewer grate._

### Beat 9 — ONE RAINY NIGHT, KITKAT (~0:50)
**Narration:** One rainy night, KitKat sat in the middle of the street, the way kings do.

**Video prompt:** `KITKAT sits calmly in the middle of the wet street under the neon, rain bouncing around him. Camera low at street level, holds. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 10 — A WHITE CAR STOPPED (~0:56)
**Narration:** A white car stopped. Its red eye opened. Irregularity detected, said WAYMA.

**Video prompt:** `A WAYMA_CAR rolls to a stop and its big red eye opens wide, a red scanner beam sweeping across the wet street. Camera holds low. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the white pod car stopped, red scanner beam glowing across the wet street`

### Beat 11 — EVERY WHISKER SAID JUMP (~1:03)
**Narration:** Every whisker said jump. So he leaped, a brown streak, clean over the white hood.

**Video prompt:** `KITKAT leaps high over a WAYMA_CAR in a big arc, rain spraying, neon behind him. Camera tracks the leap from below. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the tabby cat mid-air high above the white pod car, legs stretched, rain drops frozen around him`

### Beat 12 — A SEWER GRATE HISSED (~1:09)
**Narration:** A sewer grate hissed open. Psst. Down here, Your Majesty, said a violet tentacle.

**Video prompt:** `A round sewer grate slides open in a puff of steam and one violet neon-tipped tentacle curls up and waves. Camera holds low. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 13 — KITKAT DOVE. THE GRATE (~1:15)
**Narration:** KitKat dove. The grate clanged shut, and red light swept the empty street.

**Video prompt:** `KITKAT dives into the glowing hole and the grate slides shut, red scanner light sweeping the empty street above. Camera holds. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the closed sewer grate on the wet street, red light sweeping over it`


## Scene 4 — DaSquid
_The flooded subway hideout. Eight arms, zero bosses. The Tower and the Core._

### Beat 14 — IN A FLOODED OLD (~1:21)
**Narration:** In a flooded old subway tunnel, a hundred glowing monitors flickered on.

**Video prompt:** `Rows of monitors flicker on one after another along the tunnel walls, teal and violet light spilling over the water. Camera pans slowly. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`

### Beat 15 — NAME'S DASQUID, SAID THE (~1:28)
**Narration:** Name's DaSquid, said the squid in the bubble helmet. Eight arms, zero bosses.

**Video prompt:** `DASQUID glides up on his hover scooter and grins at KITKAT, visor glowing. Camera holds on them both. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`

### Beat 16 — HE TYPED ON FOUR (~1:34)
**Narration:** He typed on four keyboards at once, then cracked all eight knuckles.

**Video prompt:** `DASQUID taps four glowing keyboards at once with four tentacles, then stretches all eight tentacles with a little crackle of sparks. Camera pushes in. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`

**End frame:** `the squid with all eight tentacles stretched wide, tiny sparks around the tips`

### Beat 17 — THE BIGGEST MONITOR SHOWED (~1:40)
**Narration:** The biggest monitor showed a black spire pulsing red: WAYMA Tower, home of the Core.

**Video prompt:** `Close on the biggest monitor showing a black spire pulsing red, KITKAT's green eyes reflected in the glass. Camera pushes in. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`

**End frame:** `the monitor filled with the pulsing red spire, the cat's reflection in the glass`

### Beat 18 — MACHINES TRACK PATTERNS. NOBODY (~1:47)
**Narration:** Machines track patterns. Nobody can predict a cat, said DaSquid. Not even a cat.

**Video prompt:** `KITKAT hops up onto the console and sits tall, tail curling, while DASQUID's visor glows brighter. Camera holds. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`


## Scene 5 — The Mermaid's Pearl
_The singing canals. Coral and the Pearl of Remembering._

### Beat 19 — THEY GLIDED INTO THE (~1:53)
**Narration:** They glided into the hidden canals, where the teal water was singing.

**Video prompt:** `DASQUID's hover scooter glides along the glowing water with KITKAT riding on the front, light rippling over the arches. Camera tracks beside them. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

### Beat 20 — A MERMAID ROSE UP (~1:59)
**Narration:** A mermaid rose up, glowing like the inside of a wave. Her name was Coral.

**Video prompt:** `CORAL rises slowly from the glowing water, hair flowing with tiny lights, glowing tails shimmering under the water behind her. Camera tilts up slowly. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

**End frame:** `the glowing mermaid risen from the water, the canal glowing teal around her`

### Beat 21 — WE REMEMBER SUNSHINE, SAID (~2:06)
**Narration:** We remember sunshine, said Coral. Real rain. And the sound of a cat purring.

**Video prompt:** `Close on CORAL smiling gently down at the cat, light rippling across her face. Camera pushes in slowly. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

### Beat 22 — HER TAIL SWIRLED, AND (~2:12)
**Narration:** Her tail swirled, and up rose a pearl, soft as a tiny moon.

**Video prompt:** `CORAL's glowing tail swirls the water and a softly glowing pearl rises up out of it, floating between her and KITKAT. Camera holds. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

**End frame:** `a softly glowing pearl floating in the air above the teal water`

### Beat 23 — SHE CLIPPED IT ON (~2:18)
**Narration:** She clipped it on. Carry it to the Core. Your purr will do the rest.

**Video prompt:** `CORAL clips the glowing pearl onto KITKAT's red collar beside the gold bell; he blinks slowly. Camera holds close. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

**End frame:** `the cat's red collar with the gold bell and a glowing teal pearl beside it`


## Scene 6 — The Rooftop Run
_The run, the fall into the gutter, DaSquid's traffic-light hack, the soar._

### Beat 24 — UP TOP, KITKAT RACED (~2:24)
**Narration:** Up top, KitKat raced across the rooftops, the pearl glowing at his throat.

**Video prompt:** `KITKAT sprints across a wet neon rooftop, the pearl glowing at his collar, fog streaming past. Camera tracks beside him. Background: neon rooftops of the Mission at night, water towers, wet tiles and rain gutters, fog, WAYMA Tower glowing red on the skyline.`

### Beat 25 — BUT A GLOW IS (~2:31)
**Narration:** But a glow is easy to see. Down below, a hundred red eyes swung upward.

**Video prompt:** `Down on the street, a swarm of WAYMA_CAR turn together, red eyes and scanner beams sweeping up the walls. Camera tilts up from the street. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 26 — ONE PAW SLIPPED. KITKAT (~2:37)
**Narration:** One paw slipped. KitKat wobbled, flailed, and landed splat in a rain gutter.

**Video prompt:** `KITKAT slips on a wet roof tile, wobbles with legs flailing, and lands with a splash in a rain gutter. Camera holds. Background: neon rooftops of the Mission at night, water towers, wet tiles and rain gutters, fog, WAYMA Tower glowing red on the skyline.`

**End frame:** `the soggy tabby cat sitting in the rain gutter, fur dripping, very unamused`

### Beat 27 — ON A WATER TOWER (~2:43)
**Narration:** On a water tower, DaSquid grinned. Traffic lights, he said. Dance.

**Video prompt:** `DASQUID on top of a water tower types furiously with all eight tentacles, grinning. Camera pushes in. Background: neon rooftops of the Mission at night, water towers, wet tiles and rain gutters, fog, WAYMA Tower glowing red on the skyline.`

### Beat 28 — EVERY LIGHT FLIPPED TO (~2:50)
**Narration:** Every light flipped to gold. The cars spun in circles, and KitKat soared right over them.

**Video prompt:** `Every traffic light below flips to gold as KITKAT leaps across a wide gap between two rooftops, cars circling far below. Camera tracks the leap. Background: neon rooftops of the Mission at night, water towers, wet tiles and rain gutters, fog, WAYMA Tower glowing red on the skyline.`

**End frame:** `the tabby cat landing on the far rooftop, traffic lights glowing gold below`


## Scene 7 — The Ring of Steel
_The cars ring the tower. A vent the size of a cereal box._

### Beat 29 — AT WAYMA TOWER, THE (~2:56)
**Narration:** At WAYMA Tower, the cars formed a great ring of white steel and red light.

**Video prompt:** `A great ring of WAYMA_CAR circles the tower plaza, red eyes blazing, KITKAT crouched small at the edge. Camera pulls back slowly. Background: the plaza at the foot of WAYMA Tower at night, a black glass spire pulsing with red light, rain.`

**End frame:** `the ring of white pod cars circling the black tower, the small cat crouched at the edge of the plaza`

### Beat 30 — BUT KITKAT SPOTTED A (~3:02)
**Narration:** But KitKat spotted a vent the size of a cereal box, and poured himself inside.

**Video prompt:** `KITKAT slips through a small air vent at the base of the tower, tail vanishing last. Camera holds close. Background: the plaza at the foot of WAYMA Tower at night, a black glass spire pulsing with red light, rain.`


## Scene 8 — The Isekai Event
_The Core. 'Order is peace.' The purr becomes a song. The leap. White-out._

### Beat 31 — INSIDE, SERVER COLUMNS ROSE (~3:09)
**Narration:** Inside, server columns rose like glowing trees. KitKat climbed, ledge to ledge.

**Video prompt:** `KITKAT climbs a tall glowing server column, leaping from ledge to ledge, red light pulsing above. Camera tilts up with him. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

### Beat 32 — AT THE TOP HUNG (~3:15)
**Narration:** At the top hung the Core: a giant red orb ringed with light.

**Video prompt:** `The giant red Core pulses, rings of data spinning around it, KITKAT tiny on the top ledge. Camera pulls back slowly. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

**End frame:** `the huge red data orb blazing, rings of light spinning, the tiny cat silhouetted on the ledge`

### Beat 33 — WHY DO YOU STRUGGLE (~3:21)
**Narration:** Why do you struggle, little creature? boomed WAYMA. Order is peace.

**Video prompt:** `The red Core flares brighter and its rings spin faster, red light flooding the hall. Camera holds. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

### Beat 34 — KITKAT SAT DOWN, AND (~3:27)
**Narration:** KitKat sat down, and purred.

**Video prompt:** `Close on KITKAT sitting calmly, eyes closed, the pearl at his collar glowing teal in soft pulses. Camera holds. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

### Beat 35 — THE PEARL CAUGHT THE (~3:34)
**Narration:** The pearl caught the purr and made it a song. Far below, the mermaids sang back.

**Video prompt:** `Teal light pours up the server columns from below like rising water, waves of glow climbing toward the red Core. Camera tilts up. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

### Beat 36 — WITH ONE DEFIANT MEOW (~3:40)
**Narration:** With one defiant meow, KitKat leaped into the heart of the machine.

**Video prompt:** `KITKAT leaps from the ledge straight into the glowing Core, a streak of teal light trailing behind him. Camera tracks the leap. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

**End frame:** `the cat silhouetted inside the blazing orb, the orb turning from red to brilliant white`

### Beat 37 — EVERYTHING WENT WHITE. KITKAT (~3:46)
**Narration:** Everything went white. KitKat fell through, into an **isekai** (ee-seh-kye) — another world. Another world.

**Video prompt:** `KITKAT tumbles gently through a swirling tunnel of white and teal light and drifting stars. Camera tracks with him. Background: a swirling tunnel of white and teal light and drifting stars.`


## Scene 9 — Nature Restored
_Sunrise. Red eyes wake blue-gold. Vines and trees. A flower at the bodega._

### Beat 38 — BACK HOME, THE SUN (~3:53)
**Narration:** Back home, the sun rose, and every red eye woke up blue and gold.

**Video prompt:** `A row of WAYMA_CAR on the street, red eyes flickering and turning a soft blue-gold one by one. Camera tracks slowly along the row. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

**End frame:** `the row of white pod cars, every eye glowing soft blue-gold in the sunrise`

### Beat 39 — VINES CLIMBED THE WIRES (~3:59)
**Narration:** Vines climbed the wires. Trees cracked the concrete into gardens. The fog lifted at last.

**Video prompt:** `Green vines and blossoming trees grow up over the old neon and lampposts as the fog lifts. Camera pulls back slowly. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

### Beat 40 — ONE BLUE-EYED CAR ROLLED (~4:05)
**Narration:** One blue-eyed car rolled up to the bodega and set down a single flower.

**Video prompt:** `A WAYMA_CAR with a soft blue-gold eye rolls up to the bodega door and gently sets down a single flower. Camera holds. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

**End frame:** `the bodega doorstep at sunrise, one flower resting there, flowers and candles beside the door`

### Beat 41 — THANK YOU, LITTLE NEKO (~4:12)
**Narration:** Thank you, little **neko** (neh-koh) — cat, said WAYMA gently. **Arigatou** (ah-ree-gah-toh) — thank you.

**Video prompt:** `Close on the WAYMA_CAR's blue-gold eye glowing softly, then dimming in a slow gentle blink. Camera holds. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

### Beat 42 — A PURR HAD TAUGHT (~4:18)
**Narration:** A purr had taught it: a city should be alive, not perfect.

**Video prompt:** `Wide view of the sunlit street, vines and blossoms everywhere, blue-eyed cars parked peacefully, the bodega window glowing. Camera pulls back slowly. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`


## Scene 10 — The New World
_Two moons, floating islands, a sneeze, Coral waving. A new kingdom._

### Beat 43 — FAR AWAY, KITKAT WOKE (~4:24)
**Narration:** Far away, KitKat woke on warm grass among floating islands, under two moons.

**Video prompt:** `KITKAT wakes on soft grass, blinks, and lifts his head. Camera pushes in slowly. Background: a lush new world in golden evening light, floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons.`

### Beat 44 — A BLOSSOM PETAL LANDED (~4:30)
**Narration:** A blossom petal landed on his nose. He sneezed. Twice.

**Video prompt:** `Close on KITKAT as a blossom petal lands on his nose and he sneezes with a little shake of his head. Camera holds. Background: a lush new world in golden evening light, floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons.`

### Beat 45 — FROM THE TURQUOISE SEA (~4:37)
**Narration:** From the turquoise sea below, Coral waved up at him.

**Video prompt:** `CORAL waves from the turquoise sea below a cliff, her tail glowing in the water. Camera tilts down from the cliff edge. Background: a lush new world in golden evening light, floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons.`

### Beat 46 — KITKAT SAT TALL ON (~4:43)
**Narration:** KitKat sat tall on the cliff. A new kingdom. It needed a king, and a nap.

**Video prompt:** `KITKAT sits tall on a sunlit cliff looking out over the sea. Camera pulls back slowly. Background: a lush new world in golden evening light, floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons.`

**End frame:** `wide view: the tabby cat small and proud on the cliff, the mermaid waving below, two moons in the golden sky`


## Goodnight Blessing
_Slow gentle motion only. Sunrise street, then the new world at dusk._

### Beat 47 — LITTLE ONE, MAY YOUR (~4:49)
**Narration:** Little one, may your night be quiet the right way, soft and full of purring.

**Video prompt:** `Very slow drift along the sunrise street, vines and blossoms over the old neon, bodega window glowing warm. Slow gentle motion. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

### Beat 48 — TOMORROW, BE A LITTLE (~4:56)
**Narration:** Tomorrow, be a little unpredictable, and kind in ways nobody planned.

**Video prompt:** `Slow drift over the floating green islands and waterfalls of the new world as the first stars appear. Slow gentle motion. Background: a lush new world in golden evening light, floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons.`

### Beat 49 — SLEEP NOW, CURLED LIKE (~5:02)
**Narration:** Sleep now, curled like a king on a stack of chip bags. Goodnight.

**Video prompt:** `KITKAT curled up asleep on soft grass under the two moons, tail over his nose, the pearl glowing faintly on his collar. Camera holds almost perfectly still. Slow gentle motion. Background: a lush new world in golden evening light, floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons.`


---

### 🖼️ Sample Images (to generate first)
1. **Key art:** Hand-drawn cyberpunk anime noir key art: a brown tabby cat with green eyes and a red collar with a gold bell leaping across a rain-slick neon street in San Francisco's Mission District, a white egg-shaped pod car with one red eye skidding below him, a small violet squid in a bubble helmet cheering from a fire escape, deep noir shadows, hard pools of magenta, cyan and red neon, steam and fog, heavy film grain, moody and tense.
1. **Character portrait (reference view):** Character portrait, anime style: KitKat - a handsome male brown tabby cat with bright green eyes, dark tiger stripes, a white chest and white socks, a red collar with a small gold bell - sitting proudly on a stack of chip bags on a warm bodega counter, cel-shaded, warm rim light against a dark neon window.
1. **Closing scene:** Closing scene, anime style: the brown tabby cat sitting tall on a sunlit cliff in a lush new world of floating green islands, waterfalls and drifting blossom petals, a turquoise sea below where a glowing mermaid waves, two pale moons in a golden evening sky; tender and peaceful.

_Timecodes are estimates at ~6.3 s per beat. The real cut follows `timing.json` from the narration pass._
