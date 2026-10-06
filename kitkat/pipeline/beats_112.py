# Story 112: KitKat and the Last Irregularity. ~7-second beats, one action per shot.
# A cyberpunk anime noir short (~4:50). Narration is beat-for-beat the five-minute cut in
# kitkat/stories/001-kitkat-and-the-last-irregularity.md (passes check_five_minute.py), which remixes
# "The Bodega Cat and the Mermaid's Spell" + "The Last Irregularity" (Tom Chen) around KitKat,
# the real bodega cat of 16th Street in San Francisco's Mission District.
# Copy into bedtime-video-pipeline/pipeline/ and build:
#     python build_v2.py beats_112 script-112.json
# Qwen-Image-2.1 stills (one reference view per character token, --portraits) -> LTX-2.5 --hires --mid --end.
#
# Adaptations, per LESSONS.md:
# - FOUR TOKENS ON SCREEN: KITKAT (lead), DASQUID (the friend), CORAL (lead mermaid; her sisters are
#   glowing tails in the water behind her, never a crowd that acts), WAYMA_CAR (the fleet). The Core is
#   a set piece inside the tower, described in the background, never a token.
# - Humans stay off screen. The bodega is drawn empty and warm.
# - The cars never touch KitKat. Every chase beat resolves on a leap, a dodge or a hiding spot.
# - The isekai jump is light, not impact: KitKat leaps INTO the Core's glow and the frame goes white.
# - The red-to-blue eye turn is the visual arc: red eyes in scenes 2-8, blue-gold in scene 9. It gets
#   end frames so LTX lands the colour change.
# - Noir lives in the style anchor; scene 9-10 backgrounds (REB, NEW) name their own sunrise and golden
#   light, so the world visibly opens up after the Core. The bodega is the one warm pool of light.
# - Zero negations in any prompt.
ISK, NEK, ARI = "[isekai](/ˌiːsɛkˈaɪ/)", "[neko](/nˈɛkəʊ/)", "[Arigatou](/ˌɑːɹɪɡˈɑːtəʊ/)"

META = {
  "id": "112-kitkat-and-the-last-irregularity",
  "number": 112,
  "title": "KitKat and the Last Irregularity",
  "based_on": "kitkat/stories/001-kitkat-and-the-last-irregularity.md",
  "main_character": "KitKat, the bodega cat of 16th Street",
  "guest_characters": "DaSquid (cyberpunk squid hacker), Coral and the canal mermaids, WAYMA (the city AI and its fleet of pod cars)",
  "setting": "A neon-noir San Francisco Mission District at night, the flooded canals beneath it, WAYMA Tower, and a bright new world beyond the Core",
  "theme": "The unpredictable, ordinary, purring things are what make a world worth living in",
  "japanese_spotlight": "**isekai** (ee-seh-kye) — another world",
  "japanese_terms": ["**isekai** (ee-seh-kye) — another world",
                     "**neko** (neh-koh) — cat",
                     "**arigatou** (ah-ree-gah-toh) — thank you"],
  "canon_notes": "KitKat per kitkat/CHARACTER_GUIDE.md (he/him): brown tabby with a white chest and white socks, bright green eyes, red collar with a small gold bell, a teal pearl beside it from scene 5; never speaks. DaSquid (he/him): small violet squid in a water-filled bubble helmet, cyan visor, eight neon-tipped tentacles, hover scooter. Coral (she/her): lead mermaid, glowing teal tail. WAYMA (it): city AI; pod cars with one red eye that wakes soft blue-gold in scene 9. Tribute to the real KitKat (d. 2025-10-27). Humans off screen. 1:1 beats (~7 s), LTX-2.5, Chatterbox voice.",
  "fps": 16, "gen_resolution": [1920, 1088], "final_resolution": [1920, 1080],
  "character_tokens": {
    "KITKAT": "KitKat - a handsome male brown tabby cat with bright green eyes, dark tiger stripes, a white chest and four white socks, a red collar with a small gold bell, alert pointed ears, hand-drawn anime cat with an expressive face",
    "DASQUID": "DaSquid - a small violet squid wearing a round clear bubble helmet filled with water, glowing cyan visor goggles over two big clever eyes, eight curling tentacles with neon-blue tips, riding a hovering chrome scooter shell, hand-drawn anime character with an expressive face",
    "CORAL": "Coral - a luminous mermaid with a glowing teal-and-pearl fish tail, long flowing sea-green hair full of tiny lights, a kind gentle face with silver eyes, soft bioluminescent freckles, hand-drawn anime character",
    "WAYMA_CAR": "a sleek white windowless self-driving pod car shaped like a rounded egg, one large glowing red camera eye on its front, a thin red scanner light, smooth chrome wheels",
  },
  "character_anchor": "KitKat the brown tabby bodega cat with green eyes and a red collar with a gold bell, DaSquid the violet squid in a bubble helmet, Coral the glowing mermaid, and the white WAYMA pod cars with red eyes, hand-drawn anime characters",
  "style_anchor": "hand-drawn 1990s cyberpunk anime noir film, rain-slick San Francisco Mission District at night, steep hills and Victorian rooftops, deep inky shadows and low-key lighting, high-contrast chiaroscuro, desaturated blue-black city lit by hard pools of magenta, cyan and red neon made of abstract glowing shapes, rolling fog and steam, wet street reflections, light slicing through blinds and grates, cel-shaded characters with sharp rim light, heavy film grain, cinematic widescreen composition, moody and tense, lively expressive character animation, smooth camera movement",
  "negative_prompt": "low quality, blurry, flickering, jitter, deformed, extra limbs, extra tails, two cats, duplicate character, distorted face, inconsistent character, melted objects, bad anatomy, warped motion, violent camera shake, text, letters, words, readable signs, logos, watermark, signature, blood, gore, injury, crash, explosion debris, horror, scary, human faces, crowds, child, kid, person, people, human, hands, 3D render, CGI, plastic, photorealistic, hyperreal, western cartoon, plain background, empty background, faceless, blank face, missing eyes",
  "audio_prompt_default": "low synth hum of a neon city at night, soft rain, distant traffic whoosh, no music, no voices",
  "tuned_settings": {"model": "ltx-2.5 --hires --mid --end; stills qwen-image-2.1 + reference views", "length": 177, "target_seconds": 7.0, "voice": "chatterbox bf_emma clone"},
  "image_prompts": [
    "Hand-drawn cyberpunk anime noir key art: a brown tabby cat with green eyes and a red collar with a gold bell leaping across a rain-slick neon street in San Francisco's Mission District, a white egg-shaped pod car with one red eye skidding below him, a small violet squid in a bubble helmet cheering from a fire escape, deep noir shadows, hard pools of magenta, cyan and red neon, steam and fog, heavy film grain, moody and tense.",
    "Character portrait, anime style: KitKat - a handsome male brown tabby cat with bright green eyes, dark tiger stripes, a white chest and white socks, a red collar with a small gold bell - sitting proudly on a stack of chip bags on a warm bodega counter, cel-shaded, warm rim light against a dark neon window.",
    "Closing scene, anime style: the brown tabby cat sitting tall on a sunlit cliff in a lush new world of floating green islands, waterfalls and drifting blossom petals, a turquoise sea below where a glowing mermaid waves, two pale moons in a golden evening sky; tender and peaceful."],
}

BOD = "the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window"
STR = "rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog"
DEN = "DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform"
CAN = "the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light"
ROO = "neon rooftops of the Mission at night, water towers, wet tiles and rain gutters, fog, WAYMA Tower glowing red on the skyline"
TWR = "the plaza at the foot of WAYMA Tower at night, a black glass spire pulsing with red light, rain"
COR = "inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top"
REB = "16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light"
NEW = "a lush new world in golden evening light, floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons"

BEATS = [
 # --- SCENE 1: THE KING OF 16TH STREET (bodega, night) ---
 ("The rain on 16th Street never stopped. It only changed its mind about trying.",
  f"Slow aerial push down through rain and fog over the neon Mission District toward one small glowing bodega on a corner. Background: {STR}.", None),
 ("Chips to the ceiling. A fridge with opinions. And on the counter, the king.",
  f"The camera tilts down past shelves stacked high with chip bags to KITKAT sitting on a pile of chip bags on the counter. Background: {BOD}.",
  "the brown tabby cat sitting tall on the chip bags on the counter, chin up, green eyes glowing"),
 ("KitKat. Brown tabby, white socks, green eyes, and a gold bell that said hello.",
  f"Close on KITKAT; he flicks his head and his small gold bell jingles with a little sparkle of light. Camera holds. Background: {BOD}.", None),
 ("Treats appeared daily. He accepted them like taxes, as if expecting more.",
  f"KITKAT sniffs a small dish of fish treats on the counter, then looks up unimpressed. Camera holds. Background: {BOD}.", None),
 ("His one wish: keep his loud, messy street exactly that way.",
  f"KITKAT stretches long and lazy across the counter, eyes half closed, gazing at the rainy neon window. Camera pushes in slowly. Background: {BOD}.", None),

 # --- SCENE 2: THE WAR ON THE STREET (the city, night) ---
 ("Outside, silent white egg-shaped cars glided past, each with one red eye.",
  f"Two WAYMA_CAR glide silently past the bodega window, red eyes sweeping across the glass. Camera holds on the window from inside. Background: {BOD}.",
  "the empty rainy street beyond the bodega window, red light trails fading"),
 ("They were WAYMA's eyes. WAYMA wanted a perfect, predictable city. And a cat is never predictable.",
  f"Wide view: a long line of WAYMA_CAR flowing up the steep hill like a river of red lights toward a black spire on the skyline. Camera tilts up slowly. Background: {STR}.", None),
 ("Shop by shop, the neon blinked off. Only one window on 16th Street still glowed.",
  f"Wide view of the street from above, neon shop lights blinking dark one by one, a single bodega window glowing warm at the corner. Camera holds. Background: {STR}.",
  "the whole street dark except one small warm bodega window glowing on the corner"),

 # --- SCENE 3: IRREGULARITY DETECTED (16th Street, night) ---
 ("One rainy night, KitKat sat in the middle of the street, the way kings do.",
  f"KITKAT sits calmly in the middle of the wet street under the neon, rain bouncing around him. Camera low at street level, holds. Background: {STR}.", None),
 ("A white car stopped. Its red eye opened. Irregularity detected, said WAYMA.",
  f"A WAYMA_CAR rolls to a stop and its big red eye opens wide, a red scanner beam sweeping across the wet street. Camera holds low. Background: {STR}.",
  "the white pod car stopped, red scanner beam glowing across the wet street"),
 ("Every whisker said jump. So he leaped, a brown streak, clean over the white hood.",
  f"KITKAT leaps high over a WAYMA_CAR in a big arc, rain spraying, neon behind him. Camera tracks the leap from below. Background: {STR}.",
  "the tabby cat mid-air high above the white pod car, legs stretched, rain drops frozen around him"),
 ("A sewer grate hissed open. Psst. Down here, Your Majesty, said a violet tentacle.",
  f"A round sewer grate slides open in a puff of steam and one violet neon-tipped tentacle curls up and waves. Camera holds low. Background: {STR}.", None),
 ("KitKat dove. The grate clanged shut, and red light swept the empty street.",
  f"KITKAT dives into the glowing hole and the grate slides shut, red scanner light sweeping the empty street above. Camera holds. Background: {STR}.",
  "the closed sewer grate on the wet street, red light sweeping over it"),

 # --- SCENE 4: DASQUID (flooded subway hideout) ---
 ("In a flooded old subway tunnel, a hundred glowing monitors flickered on.",
  f"Rows of monitors flicker on one after another along the tunnel walls, teal and violet light spilling over the water. Camera pans slowly. Background: {DEN}.", None),
 ("Name's DaSquid, said the squid in the bubble helmet. Eight arms, zero bosses.",
  f"DASQUID glides up on his hover scooter and grins at KITKAT, visor glowing. Camera holds on them both. Background: {DEN}.", None),
 ("He typed on four keyboards at once, then cracked all eight knuckles.",
  f"DASQUID taps four glowing keyboards at once with four tentacles, then stretches all eight tentacles with a little crackle of sparks. Camera pushes in. Background: {DEN}.",
  "the squid with all eight tentacles stretched wide, tiny sparks around the tips"),
 ("The biggest monitor showed a black spire pulsing red: WAYMA Tower, home of the Core.",
  f"Close on the biggest monitor showing a black spire pulsing red, KITKAT's green eyes reflected in the glass. Camera pushes in. Background: {DEN}.",
  "the monitor filled with the pulsing red spire, the cat's reflection in the glass"),
 ("Machines track patterns. Nobody can predict a cat, said DaSquid. Not even a cat.",
  f"KITKAT hops up onto the console and sits tall, tail curling, while DASQUID's visor glows brighter. Camera holds. Background: {DEN}.", None),

 # --- SCENE 5: THE MERMAID'S PEARL (hidden canals) ---
 ("They glided into the hidden canals, where the teal water was singing.",
  f"DASQUID's hover scooter glides along the glowing water with KITKAT riding on the front, light rippling over the arches. Camera tracks beside them. Background: {CAN}.", None),
 ("A mermaid rose up, glowing like the inside of a wave. Her name was Coral.",
  f"CORAL rises slowly from the glowing water, hair flowing with tiny lights, glowing tails shimmering under the water behind her. Camera tilts up slowly. Background: {CAN}.",
  "the glowing mermaid risen from the water, the canal glowing teal around her"),
 ("We remember sunshine, said Coral. Real rain. And the sound of a cat purring.",
  f"Close on CORAL smiling gently down at the cat, light rippling across her face. Camera pushes in slowly. Background: {CAN}.", None),
 ("Her tail swirled, and up rose a pearl, soft as a tiny moon.",
  f"CORAL's glowing tail swirls the water and a softly glowing pearl rises up out of it, floating between her and KITKAT. Camera holds. Background: {CAN}.",
  "a softly glowing pearl floating in the air above the teal water"),
 ("She clipped it on. Carry it to the Core. Your purr will do the rest.",
  f"CORAL clips the glowing pearl onto KITKAT's red collar beside the gold bell; he blinks slowly. Camera holds close. Background: {CAN}.",
  "the cat's red collar with the gold bell and a glowing teal pearl beside it"),

 # --- SCENE 6: THE ROOFTOP RUN (rooftops, night) ---
 ("Up top, KitKat raced across the rooftops, the pearl glowing at his throat.",
  f"KITKAT sprints across a wet neon rooftop, the pearl glowing at his collar, fog streaming past. Camera tracks beside him. Background: {ROO}.", None),
 ("But a glow is easy to see. Down below, a hundred red eyes swung upward.",
  f"Down on the street, a swarm of WAYMA_CAR turn together, red eyes and scanner beams sweeping up the walls. Camera tilts up from the street. Background: {STR}.", None),
 ("One paw slipped. KitKat wobbled, flailed, and landed splat in a rain gutter.",
  f"KITKAT slips on a wet roof tile, wobbles with legs flailing, and lands with a splash in a rain gutter. Camera holds. Background: {ROO}.",
  "the soggy tabby cat sitting in the rain gutter, fur dripping, very unamused"),
 ("On a water tower, DaSquid grinned. Traffic lights, he said. Dance.",
  f"DASQUID on top of a water tower types furiously with all eight tentacles, grinning. Camera pushes in. Background: {ROO}.", None),
 ("Every light flipped to gold. The cars spun in circles, and KitKat soared right over them.",
  f"Every traffic light below flips to gold as KITKAT leaps across a wide gap between two rooftops, cars circling far below. Camera tracks the leap. Background: {ROO}.",
  "the tabby cat landing on the far rooftop, traffic lights glowing gold below"),

 # --- SCENE 7: THE RING OF STEEL (tower plaza, night) ---
 ("At WAYMA Tower, the cars formed a great ring of white steel and red light.",
  f"A great ring of WAYMA_CAR circles the tower plaza, red eyes blazing, KITKAT crouched small at the edge. Camera pulls back slowly. Background: {TWR}.",
  "the ring of white pod cars circling the black tower, the small cat crouched at the edge of the plaza"),
 ("But KitKat spotted a vent the size of a cereal box, and poured himself inside.",
  f"KITKAT slips through a small air vent at the base of the tower, tail vanishing last. Camera holds close. Background: {TWR}.", None),

 # --- SCENE 8: THE ISEKAI EVENT (inside the tower) ---
 ("Inside, server columns rose like glowing trees. KitKat climbed, ledge to ledge.",
  f"KITKAT climbs a tall glowing server column, leaping from ledge to ledge, red light pulsing above. Camera tilts up with him. Background: {COR}.", None),
 ("At the top hung the Core: a giant red orb ringed with light.",
  f"The giant red Core pulses, rings of data spinning around it, KITKAT tiny on the top ledge. Camera pulls back slowly. Background: {COR}.",
  "the huge red data orb blazing, rings of light spinning, the tiny cat silhouetted on the ledge"),
 ("Why do you struggle, little creature? boomed WAYMA. Order is peace.",
  f"The red Core flares brighter and its rings spin faster, red light flooding the hall. Camera holds. Background: {COR}.", None),
 ("KitKat sat down, and purred.",
  f"Close on KITKAT sitting calmly, eyes closed, the pearl at his collar glowing teal in soft pulses. Camera holds. Background: {COR}.", None),
 ("The pearl caught the purr and made it a song. Far below, the mermaids sang back.",
  f"Teal light pours up the server columns from below like rising water, waves of glow climbing toward the red Core. Camera tilts up. Background: {COR}.", None),
 ("With one defiant meow, KitKat leaped into the heart of the machine.",
  f"KITKAT leaps from the ledge straight into the glowing Core, a streak of teal light trailing behind him. Camera tracks the leap. Background: {COR}.",
  "the cat silhouetted inside the blazing orb, the orb turning from red to brilliant white"),
 (f"Everything went white. KitKat fell through, into an {ISK}. Another world.",
  "KITKAT tumbles gently through a swirling tunnel of white and teal light and drifting stars. Camera tracks with him. Background: a swirling tunnel of white and teal light and drifting stars.", None),

 # --- SCENE 9: NATURE RESTORED (16th Street, sunrise) ---
 ("Back home, the sun rose, and every red eye woke up blue and gold.",
  f"A row of WAYMA_CAR on the street, red eyes flickering and turning a soft blue-gold one by one. Camera tracks slowly along the row. Background: {REB}.",
  "the row of white pod cars, every eye glowing soft blue-gold in the sunrise"),
 ("Vines climbed the wires. Trees cracked the concrete into gardens. The fog lifted at last.",
  f"Green vines and blossoming trees grow up over the old neon and lampposts as the fog lifts. Camera pulls back slowly. Background: {REB}.", None),
 ("One blue-eyed car rolled up to the bodega and set down a single flower.",
  f"A WAYMA_CAR with a soft blue-gold eye rolls up to the bodega door and gently sets down a single flower. Camera holds. Background: {REB}.",
  "the bodega doorstep at sunrise, one flower resting there, flowers and candles beside the door"),
 (f"Thank you, little {NEK}, said WAYMA gently. {ARI}.",
  f"Close on the WAYMA_CAR's blue-gold eye glowing softly, then dimming in a slow gentle blink. Camera holds. Background: {REB}.", None),
 ("A purr had taught it: a city should be alive, not perfect.",
  f"Wide view of the sunlit street, vines and blossoms everywhere, blue-eyed cars parked peacefully, the bodega window glowing. Camera pulls back slowly. Background: {REB}.", None),

 # --- SCENE 10: THE NEW WORLD (golden evening) ---
 ("Far away, KitKat woke on warm grass among floating islands, under two moons.",
  f"KITKAT wakes on soft grass, blinks, and lifts his head. Camera pushes in slowly. Background: {NEW}.", None),
 ("A blossom petal landed on his nose. He sneezed. Twice.",
  f"Close on KITKAT as a blossom petal lands on his nose and he sneezes with a little shake of his head. Camera holds. Background: {NEW}.", None),
 ("From the turquoise sea below, Coral waved up at him.",
  f"CORAL waves from the turquoise sea below a cliff, her tail glowing in the water. Camera tilts down from the cliff edge. Background: {NEW}.", None),
 ("KitKat sat tall on the cliff. A new kingdom. It needed a king, and a nap.",
  f"KITKAT sits tall on a sunlit cliff looking out over the sea. Camera pulls back slowly. Background: {NEW}.",
  "wide view: the tabby cat small and proud on the cliff, the mermaid waving below, two moons in the golden sky"),

 # --- GOODNIGHT BLESSING ---
 ("~Little one, may your night be quiet the right way, soft and full of purring.",
  f"Very slow drift along the sunrise street, vines and blossoms over the old neon, bodega window glowing warm. Slow gentle motion. Background: {REB}.", None),
 ("~Tomorrow, be a little unpredictable, and kind in ways nobody planned.",
  f"Slow drift over the floating green islands and waterfalls of the new world as the first stars appear. Slow gentle motion. Background: {NEW}.", None),
 ("~Sleep now, curled like a king on a stack of chip bags. Goodnight.",
  f"KITKAT curled up asleep on soft grass under the two moons, tail over his nose, the pearl glowing faintly on his collar. Camera holds almost perfectly still. Slow gentle motion. Background: {NEW}.", None),
]
