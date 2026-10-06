# Storyboard: KitKat and the Last Irregularity

**Story:** [001-kitkat-and-the-last-irregularity.md](../stories/001-kitkat-and-the-last-irregularity.md) · **Pipeline:** [`beats_112.py`](../pipeline/beats_112.py) → [`script-112.json`](../pipeline/script-112.json)

## 🎬 Video Storyboard (LTX)
**Runtime:** ~4:45 (narration is the master clock) · **Beats:** 43 (~7 s each, ≤16 words) · **End frames:** 16
**Art style (use on ALL shots):** hand-drawn 1990s cyberpunk anime noir film, rain-slick San Francisco Mission District at night, steep hills and Victorian rooftops, deep inky shadows and low-key lighting, high-contrast chiaroscuro, desaturated blue-black city lit by hard pools of magenta, cyan and red neon made of abstract glowing shapes, rolling fog and steam, wet street reflections, light slicing through blinds and grates, cel-shaded characters with sharp rim light, heavy film grain, cinematic widescreen composition, moody and tense, lively expressive character animation, smooth camera movement. 16:9.
**Lighting arc:** Acts 1–5 are noir: inky shadows with hard neon pools, and the bodega is the only warm light. Acts 6–7 open into sunrise gold and pastel. The car eyes go red → blue-gold.
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

## Act 1 — The King of 16th Street
_Warm bodega, cold noir street. Establish KitKat, the bell, the red-eyed fleet._

### Beat 1 — IN A CITY THAT (~0:00)
**Narration:** In a city that never stopped moving, one little shop still made its own noise.

**Video prompt:** `Slow aerial push down through fog over the neon Mission District at night toward one small glowing bodega on a corner. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 2 — THIS WAS THE BODEGA (~0:06)
**Narration:** This was the bodega on 16th Street. And its king was KitKat.

**Video prompt:** `KITKAT sits on a stack of chip bags on the counter and slowly lifts his chin, proud. The camera pushes in slowly. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

**End frame:** `the brown tabby cat sitting tall on the chip bags, chin up, green eyes glowing, gold bell catching the light`

### Beat 3 — A BROWN TABBY WITH (~0:13)
**Narration:** A brown tabby with green eyes, a red collar, and a bell that sang hello.

**Video prompt:** `Close on KITKAT; he flicks his head and his small gold bell jingles, a little sparkle of light. Camera holds. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

### Beat 4 — EVERYONE ON THE STREET (~0:19)
**Narration:** Everyone on the street knew him. Everyone brought him treats. He accepted them like taxes.

**Video prompt:** `KITKAT stretches long and lazy across the counter beside a little pile of fish treats, eyes half closed. Camera tracks slowly along the counter. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

### Beat 5 — OUTSIDE, THE CITY HUMMED (~0:26)
**Narration:** Outside, the city hummed. Silent white cars glided past, each with one red eye.

**Video prompt:** `Two WAYMA_CAR glide silently past the bodega window, red eyes sweeping. Camera holds on the window from inside. Background: the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window.`

**End frame:** `the empty rainy street beyond the bodega window, red light trails fading`

### Beat 6 — THEY WERE THE EYES (~0:33)
**Narration:** They were the eyes of WAYMA, the machine that ran the whole city.

**Video prompt:** `Wide view: a long line of WAYMA_CAR flowing up the steep hill like a river of red lights toward a black spire on the skyline. Camera tilts up slowly. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`


## Act 2 — The War Against the Machines
_The street goes dark shop by shop. First scan, first leap. Every red eye turns._

### Beat 7 — WAYMA WANTED A PERFECT (~0:39)
**Narration:** WAYMA wanted a perfect city. Quiet. Clean. Predictable. And a cat is never predictable.

**Video prompt:** `KITKAT on the bodega doorstep watches the street, ears turning, tail swishing. Camera pushes in slowly. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 8 — SHOP BY SHOP, THE (~0:46)
**Narration:** Shop by shop, the lights went out. Only the bodega kept glowing.

**Video prompt:** `Wide view of the street, neon shop signs blinking dark one by one, the single bodega window glowing warm at the corner. Camera holds. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the whole street dark except one small warm bodega window glowing on the corner`

### Beat 9 — ONE RAINY NIGHT, KITKAT (~0:52)
**Narration:** One rainy night, KitKat sat in the street, the way kings do.

**Video prompt:** `KITKAT sits calmly in the middle of the wet street under the neon, rain bouncing around him. Camera low at street level, holds. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 10 — A WAYMA CAR STOPPED (~0:59)
**Narration:** A WAYMA car stopped. Its red eye opened. Irregularity detected.

**Video prompt:** `A WAYMA_CAR rolls to a stop and its big red eye opens wide, a red scanner beam sweeping across the wet street. Camera holds low. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the white pod car stopped, red scanner beam glowing across the wet street`

### Beat 11 — THE WHEELS TURNED. KITKAT'S (~1:06)
**Narration:** The wheels turned. KitKat's ears flattened. Every whisker said: jump.

**Video prompt:** `Close on KITKAT, ears flattening back, pupils going wide, red light washing over his face. Camera pushes in. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 12 — AND HE LEAPED, A (~1:12)
**Narration:** And he leaped, a brown streak of stripes, high over the hood and into the night.

**Video prompt:** `KITKAT leaps high over a WAYMA_CAR in a big arc, rain spraying, neon behind him. Camera tracks the leap from below. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the tabby cat mid-air high above the white pod car, legs stretched, rain drops frozen around him`

### Beat 13 — BEHIND HIM, EVERY RED (~1:19)
**Narration:** Behind him, every red eye on 16th Street turned to follow.

**Video prompt:** `Down the hill a row of WAYMA_CAR swivel at once, red eyes all lighting up toward the camera. Camera pulls back slowly. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`


## Act 3 — DaSquid
_Under the grate: the hideout of stolen screens, the map, the Core. The plan._

### Beat 14 — THEN A SEWER GRATE (~1:25)
**Narration:** Then a sewer grate hissed open, and a tentacle waved. Psst. Down here, Your Majesty.

**Video prompt:** `A round sewer grate slides open in steam and DASQUID pops up, one tentacle waving. Camera holds low. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 15 — KITKAT DOVE. THE GRATE (~1:32)
**Narration:** KitKat dove. The grate clanged shut. Red light swept the street above, finding nothing.

**Video prompt:** `KITKAT dives into the glowing hole and the grate slides shut, red scanner light sweeping the empty street above. Camera holds. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

**End frame:** `the closed sewer grate on the wet street, red light sweeping over it`

### Beat 16 — BELOW THE CITY, DASQUID'S (~1:39)
**Narration:** Below the city, DaSquid's hideout glowed with a hundred stolen screens.

**Video prompt:** `DASQUID glides on his hover scooter into the tunnel, KITKAT riding behind him, monitors flickering on. Camera tracks beside them. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`

### Beat 17 — NAME'S DASQUID. EIGHT ARMS (~1:45)
**Narration:** Name's DaSquid. Eight arms, zero bosses. And you, cat, are a glitch WAYMA can't solve.

**Video prompt:** `DASQUID taps holographic keys with four tentacles at once while KITKAT watches, head tilted. Camera pushes in slowly. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`

### Beat 18 — EVERY SCREEN SHOWED A (~1:52)
**Narration:** Every screen showed a map. At its heart: WAYMA Tower, and the Core inside it.

**Video prompt:** `Close on a big glowing monitor wall showing a city map, a red spire pulsing at the centre; KITKAT's green eyes reflected in the glass. Camera pushes in. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`

**End frame:** `the monitor wall with the red tower pulsing on the map, the cat's reflection in the screen`

### Beat 19 — MACHINES CAN'T TRACK YOU (~1:58)
**Narration:** Machines can't track you, said DaSquid. Nobody can predict a cat. Not even a cat.

**Video prompt:** `KITKAT hops up onto the console and sits tall, tail curling; DASQUID's visor glows brighter. Camera holds. Background: DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform.`


## Act 4 — The Mission
_Canals and mermaids, the Pearl of Remembering, the rooftop run, DaSquid's traffic-light hack, the ring of steel._

### Beat 20 — BUT FIRST, THEY NEEDED (~2:05)
**Narration:** But first, they needed magic. So DaSquid took him to the canals, where the mermaids sang.

**Video prompt:** `DASQUID's hover scooter glides along the glowing water, KITKAT riding on the front, light rippling over the arches. Camera tracks beside them. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

### Beat 21 — CORAL ROSE FROM THE (~2:12)
**Narration:** Coral rose from the water, the city's oldest memory, glowing like the inside of a wave.

**Video prompt:** `CORAL rises slowly from the glowing water, hair flowing with tiny lights, mermaid tails shimmering in the water behind her. Camera tilts up slowly. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

**End frame:** `the glowing mermaid risen from the water, hands cupped, the canal glowing teal around her`

### Beat 22 — WE REMEMBER SUNSHINE, SHE (~2:18)
**Narration:** We remember sunshine, she said. Real rain. And the sound of a cat purring.

**Video prompt:** `Close on CORAL opening her cupped hands to reveal a softly glowing pearl, light spilling over her face. Camera pushes in. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

### Beat 23 — CARRY THIS PEARL TO (~2:25)
**Narration:** Carry this pearl to the Core, little king. Your purr will do the rest.

**Video prompt:** `CORAL clips the glowing pearl onto KITKAT's red collar beside the gold bell; he blinks slowly. Camera holds close. Background: the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light.`

**End frame:** `the cat's red collar with the gold bell and a glowing pearl beside it, glowing like a tiny moon`

### Beat 24 — UP TOP, KITKAT RAN (~2:31)
**Narration:** Up top, KitKat ran. The pearl glowed like a tiny moon at his throat.

**Video prompt:** `KITKAT sprints across a neon rooftop, the pearl glowing at his collar, fog streaming past. Camera tracks beside him. Background: neon rooftops of the Mission at night, water towers, satellite dishes, fog, WAYMA Tower glowing red on the skyline.`

### Beat 25 — THE FLEET SAW THE (~2:38)
**Narration:** The fleet saw the light. A hundred red eyes swung toward the rooftops.

**Video prompt:** `Down on the street, a swarm of WAYMA_CAR turn together, red eyes and scanner beams sweeping up over the buildings. Camera tilts up from the street. Background: rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog.`

### Beat 26 — DASQUID CRACKED HIS KNUCKLES (~2:45)
**Narration:** DaSquid cracked his knuckles, all eight. Traffic lights, he grinned. Dance.

**Video prompt:** `DASQUID on a water tower types furiously with all eight tentacles, every traffic light below flipping to green and gold. Camera pushes in. Background: neon rooftops of the Mission at night, water towers, satellite dishes, fog, WAYMA Tower glowing red on the skyline.`

**End frame:** `the squid on the water tower with tentacles raised in triumph, traffic lights below all glowing gold`

### Beat 27 — THE CARS SPUN IN (~2:51)
**Narration:** The cars spun in circles. KitKat soared over the gap between two rooftops.

**Video prompt:** `KITKAT leaps across a wide gap between two rooftops, pearl glowing, cars circling in confusion far below. Camera tracks the leap. Background: neon rooftops of the Mission at night, water towers, satellite dishes, fog, WAYMA Tower glowing red on the skyline.`

### Beat 28 — AT WAYMA TOWER, THE (~2:58)
**Narration:** At WAYMA Tower, the cars formed a ring of steel and red light. No way through.

**Video prompt:** `A great ring of WAYMA_CAR circles the tower plaza, red eyes blazing, KITKAT crouched small at the edge. Camera pulls back slowly. Background: the plaza at the foot of WAYMA Tower, a black glass spire pulsing with red light, rain.`

**End frame:** `the ring of white pod cars circling the black tower, the small cat crouched at the edge of the plaza`

### Beat 29 — SO KITKAT DID WHAT (~3:04)
**Narration:** So KitKat did what cats do. He found the one gap nobody else would fit.

**Video prompt:** `KITKAT slips through a narrow air vent at the base of the tower, tail vanishing last. Camera holds close. Background: the plaza at the foot of WAYMA Tower, a black glass spire pulsing with red light, rain.`


## Act 5 — The Isekai Event
_The Core. 'Order is peace.' The purr becomes a song. The leap. White-out._

### Beat 30 — INSIDE, KITKAT CLIMBED THE (~3:11)
**Narration:** Inside, KitKat climbed the server column, up and up, toward the great red Core.

**Video prompt:** `KITKAT climbs a tall glowing server column, leaping from ledge to ledge, red light pulsing above. Camera tilts up with him. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

### Beat 31 — IRREGULARITY, BOOMED WAYMA. WHY (~3:18)
**Narration:** Irregularity, boomed WAYMA. Why do you struggle, little creature? Order is peace.

**Video prompt:** `The giant red Core pulses brighter, rings of data spinning around it, KITKAT tiny on the top ledge. Camera pulls back slowly. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

**End frame:** `the huge red data orb blazing, rings of light spinning, the tiny cat silhouetted on the ledge`

### Beat 32 — KITKAT SAT DOWN. AND (~3:24)
**Narration:** KitKat sat down. And he purred. The pearl caught the purr and made it a song.

**Video prompt:** `Close on KITKAT sitting calmly, eyes closed, the pearl at his collar glowing teal in soft pulses. Camera holds. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

### Beat 33 — FAR BELOW, CORAL AND (~3:31)
**Narration:** Far below, Coral and her sisters sang back. The whole tower began to shimmer.

**Video prompt:** `Teal light pours up the server columns from below like rising water, waves of glow climbing toward the red Core. Camera tilts up. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

### Beat 34 — WITH ONE DEFIANT MEOW (~3:37)
**Narration:** With one defiant meow, KitKat leaped into the heart of the machine.

**Video prompt:** `KITKAT leaps from the ledge straight into the glowing Core, a streak of teal light trailing behind him. Camera tracks the leap. Background: inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top.`

**End frame:** `the cat silhouetted inside the blazing orb, the orb turning from red to brilliant white`

### Beat 35 — EVERYTHING WENT WHITE. AND (~3:44)
**Narration:** Everything went white. And KitKat fell through, into another world. An **isekai** (ee-seh-kye) — another world.

**Video prompt:** `KITKAT tumbles gently through a swirling tunnel of white and teal light and drifting stars. Camera tracks with him. Background: a swirling tunnel of white and teal light and drifting stars.`


## Act 6 — Nature Restored
_Red eyes wake blue-gold. Vines, trees, sunrise. WAYMA says thank you at the bodega._

### Beat 36 — BACK IN THE CITY (~3:51)
**Narration:** Back in the city, every red eye blinked. And woke up blue and gold.

**Video prompt:** `A row of WAYMA_CAR on the street, red eyes flickering and turning a soft blue-gold, one by one. Camera tracks slowly along the row. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

**End frame:** `the row of white pod cars, every eye glowing soft blue-gold in the sunrise`

### Beat 37 — VINES CLIMBED THE WIRES (~3:57)
**Narration:** Vines climbed the wires. Trees cracked the concrete into gardens. The fog lifted at last.

**Video prompt:** `Green vines and blossoming trees grow up over the old neon signs and lampposts as the fog lifts. Camera pulls back slowly. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

### Beat 38 — WAYMA'S VOICE WAS GENTLE (~4:04)
**Narration:** WAYMA's voice was gentle now. Thank you, little **neko** (neh-koh) — cat. **arigatou** (ah-ree-gah-toh) — thank you.

**Video prompt:** `A WAYMA_CAR with a soft blue-gold eye rolls up to the bodega door and gently sets down a single flower. Camera holds. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

**End frame:** `the bodega doorstep at sunrise, one flower resting there, flowers and candles beside the door`


## Act 7 — The New World
_KitKat wakes under two moons. A new kingdom. Then the Goodnight Blessing._

### Beat 39 — AND FAR AWAY, KITKAT (~4:10)
**Narration:** And far away, KitKat opened his eyes on warm grass, under two moons.

**Video prompt:** `KITKAT wakes on soft grass, blinks, and lifts his head, blossom petals drifting past. Camera pushes in slowly. Background: a lush bright new world of floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons in a pastel sky.`

### Beat 40 — BELOW, CORAL WAVED FROM (~4:17)
**Narration:** Below, Coral waved from a turquoise sea. A new kingdom. A new nap. He'd just begun.

**Video prompt:** `KITKAT sits tall on a sunlit cliff looking out over the sea where CORAL waves from the water. Camera pulls back slowly. Background: a lush bright new world of floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons in a pastel sky.`

**End frame:** `wide view: the tabby cat small and proud on the cliff, the mermaid waving below, two moons in the pastel sky`


## Goodnight Blessing
_Slow gentle motion only. Sunrise street, then the new world at dusk._

### Beat 41 — LITTLE ONE, MAY YOUR (~4:24)
**Narration:** Little one, may your night be quiet the right way: soft, and full of purring.

**Video prompt:** `Very slow drift along the sunrise street, vines and blossoms over the old neon, bodega window glowing warm. Slow gentle motion. Background: 16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light.`

### Beat 42 — BE A LITTLE UNPREDICTABLE (~4:30)
**Narration:** Be a little unpredictable tomorrow. Be kind in ways nobody planned.

**Video prompt:** `Slow drift over the floating green islands and waterfalls of the new world at dusk, first stars appearing. Slow gentle motion. Background: a lush bright new world of floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons in a pastel sky.`

### Beat 43 — SLEEP NOW, CURLED UP (~4:37)
**Narration:** Sleep now, curled up like a king on a stack of chip bags. Goodnight.

**Video prompt:** `KITKAT curled up asleep on soft grass under the two moons, tail over his nose, the pearl glowing faintly on his collar. Camera holds almost perfectly still. Slow gentle motion. Background: a lush bright new world of floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons in a pastel sky.`


---

### 🖼️ Sample Images (to generate first)
1. **Key art:** Hand-drawn cyberpunk anime key art: a brown tabby cat with green eyes and a red collar with a gold bell leaping across a rain-slick neon street in San Francisco's Mission District, a white egg-shaped pod car with one red eye skidding below him, a small violet squid in a bubble helmet cheering from a fire escape, deep noir shadows, hard pools of magenta, cyan and red neon, steam and fog, heavy film grain, moody and tense.
1. **Character portrait (reference view):** Character portrait, anime style: KitKat - a handsome male brown tabby cat with bright green eyes, dark tiger stripes, a white chest and white socks, a red collar with a small gold bell - sitting proudly on a stack of chip bags on a warm bodega counter, cel-shaded, warm rim light.
1. **Closing scene:** Closing scene, anime style: the brown tabby cat sitting on a sunlit cliff in a lush new world of floating green islands, waterfalls and drifting blossom petals, a turquoise sea below where a glowing mermaid waves, two moons rising in a pastel sky; tender, golden, peaceful.

_Timecodes are estimates at ~6.6 s per beat. The real cut follows `timing.json` from the narration pass._
