# Story 112: KitKat and the Last Irregularity. ~7-second beats, one action per shot.
# A cyberpunk anime feature (~4:45). Based on kitkat/stories/001-kitkat-and-the-last-irregularity.md,
# which remixes "The Bodega Cat and the Mermaid's Spell" + "The Last Irregularity" (Tom Chen)
# around KitKat, the real bodega cat of 16th Street in San Francisco's Mission District.
# Copy into bedtime-video-pipeline/pipeline/ and build:
#     python build_v2.py beats_112 script-112.json
# Qwen-Image-2.1 stills (one reference view per character token, --portraits) -> LTX-2.5 --hires --mid --end.
#
# Adaptations, per LESSONS.md:
# - FOUR TOKENS ON SCREEN: KITKAT (lead), DASQUID (the friend), CORAL (lead mermaid; her sisters are
#   glowing tails in the water behind her, never a crowd that acts), WAYMA_CAR (the fleet). The Core is
#   a set piece inside the tower, described in the background, never a token.
# - Humans stay off screen. The shopkeeper is narrated only; the bodega is drawn empty and warm.
# - The cars never touch KitKat. Every chase beat resolves on a leap, a dodge or a hiding spot.
# - The isekai jump is light, not impact: KitKat leaps INTO the Core's glow and the frame goes white.
# - The red-to-blue eye turn is the visual arc: red eyes in acts 2-4, blue-gold in act 6. It gets
#   end frames so LTX lands the colour change.
# - Zero negations in any prompt.
ISK, NEK, ARI = "[isekai](/ˌiːsɛkˈaɪ/)", "[neko](/nˈɛkəʊ/)", "[arigatou](/ˌɑːɹɪɡˈɑːtəʊ/)"

META = {
  "id": "112-kitkat-and-the-last-irregularity",
  "number": 112,
  "title": "KitKat and the Last Irregularity",
  "based_on": "kitkat/stories/001-kitkat-and-the-last-irregularity.md",
  "main_character": "KitKat, the bodega cat of 16th Street",
  "guest_characters": "DaSquid (cyberpunk squid hacker), Coral and the canal mermaids, WAYMA (the city AI and its fleet of pod cars)",
  "setting": "A neon cyberpunk San Francisco Mission District, the flooded canals beneath it, WAYMA Tower, and the bright new world beyond the Core",
  "theme": "The unpredictable, ordinary, purring things are what make a world worth living in",
  "japanese_spotlight": "**isekai** (ee-seh-kye) — another world",
  "japanese_terms": ["**isekai** (ee-seh-kye) — another world",
                     "**neko** (neh-koh) — cat",
                     "**arigatou** (ah-ree-gah-toh) — thank you"],
  "canon_notes": "KitKat per kitkat/CHARACTER_GUIDE.md (he/him): 'A bodega needs a king, and a king needs a nap'; brown tabby with a white chest and white socks, bright green eyes, red collar with a small gold bell. DaSquid (he/him): small violet squid in a water-filled bubble helmet, cyan visor, eight busy tentacles. Coral (she/her): lead mermaid, glowing teal tail, pearl in her hands. WAYMA (it, then they): city AI; pod cars with one red eye that turns soft blue-gold at the end. Tribute to the real KitKat (d. 2025-10-27). Humans off screen. 1:1 beats (~7 s), LTX-2.5, Chatterbox voice.",
  "fps": 16, "gen_resolution": [1920, 1088], "final_resolution": [1920, 1080],
  "character_tokens": {
    "KITKAT": "KitKat - a handsome male brown tabby cat with bright green eyes, dark tiger stripes, a white chest and four white socks, a red collar with a small gold bell, alert pointed ears, hand-drawn anime cat with an expressive face",
    "DASQUID": "DaSquid - a small violet squid wearing a round clear bubble helmet filled with water, glowing cyan visor goggles over two big clever eyes, eight curling tentacles with neon-blue tips, riding a hovering chrome scooter shell, hand-drawn anime character with an expressive face",
    "CORAL": "Coral - a luminous mermaid with a glowing teal-and-pearl fish tail, long flowing sea-green hair full of tiny lights, a kind gentle face with silver eyes, soft bioluminescent freckles, hand-drawn anime character",
    "WAYMA_CAR": "a sleek white windowless self-driving pod car shaped like a rounded egg, one large glowing red camera eye on its front, a thin red scanner light, smooth chrome wheels",
  },
  "character_anchor": "KitKat the brown tabby bodega cat with green eyes and a red collar with a gold bell, DaSquid the violet squid in a bubble helmet, Coral the glowing mermaid, and the white WAYMA pod cars with red eyes, hand-drawn anime characters",
  "style_anchor": "hand-drawn 1990s cyberpunk anime noir film, rain-slick San Francisco Mission District at night, steep hills and Victorian rooftops, deep inky shadows and low-key lighting, high-contrast chiaroscuro, desaturated blue-black city lit by hard pools of magenta, cyan and red neon made of abstract glowing shapes, rolling fog and steam, wet street reflections, light slicing through blinds and grates, cel-shaded characters with sharp rim light, heavy film grain, cinematic widescreen composition, moody and tense, lively expressive character animation, smooth camera movement",
  # The noir is the city's look under WAYMA. Act 6-7 backgrounds (REB, NEW) name their own sunrise
  # and pastel light, so the world visibly opens up after the Core; the bodega stays the one warm pool.
  "negative_prompt": "low quality, blurry, flickering, jitter, deformed, extra limbs, extra tails, two cats, duplicate character, distorted face, inconsistent character, melted objects, bad anatomy, warped motion, violent camera shake, text, letters, words, readable signs, logos, watermark, signature, blood, gore, injury, crash, explosion debris, horror, scary, human faces, crowds, child, kid, person, people, human, hands, 3D render, CGI, plastic, photorealistic, hyperreal, western cartoon, plain background, empty background, faceless, blank face, missing eyes",
  "audio_prompt_default": "low synth hum of a neon city at night, soft rain, distant traffic whoosh, no music, no voices",
  "tuned_settings": {"model": "ltx-2.5 --hires --mid --end; stills qwen-image-2.1 + reference views", "length": 177, "target_seconds": 7.0, "voice": "chatterbox bf_emma clone"},
  "image_prompts": [
    "Hand-drawn cyberpunk anime key art: a brown tabby cat with green eyes and a red collar with a gold bell leaping across a rain-slick neon street in San Francisco's Mission District, a white egg-shaped pod car with one red eye skidding below him, a small violet squid in a bubble helmet cheering from a fire escape, deep noir shadows, hard pools of magenta, cyan and red neon, steam and fog, heavy film grain, moody and tense.",
    "Character portrait, anime style: KitKat - a handsome male brown tabby cat with bright green eyes, dark tiger stripes, a white chest and white socks, a red collar with a small gold bell - sitting proudly on a stack of chip bags on a warm bodega counter, cel-shaded, warm rim light.",
    "Closing scene, anime style: the brown tabby cat sitting on a sunlit cliff in a lush new world of floating green islands, waterfalls and drifting blossom petals, a turquoise sea below where a glowing mermaid waves, two moons rising in a pastel sky; tender, golden, peaceful."],
}

BOD = "the cozy Mission District bodega at night, shelves of chips and canned goods, a humming fridge, warm yellow light, neon rain beyond the front window"
STR = "rain-slick 16th Street at night, steep hill, Victorian rooftops, stacked magenta and cyan neon, rolling fog"
DEN = "DaSquid's hideout in a flooded old subway tunnel, walls of glowing monitors and tangled cables, teal water lapping at the platform"
CAN = "the hidden canals beneath the city, stone arches, glowing teal water, drifting bioluminescent light"
ROO = "neon rooftops of the Mission at night, water towers, satellite dishes, fog, WAYMA Tower glowing red on the skyline"
TWR = "the plaza at the foot of WAYMA Tower, a black glass spire pulsing with red light, rain"
COR = "inside WAYMA Tower, a vast dark hall of server columns rising into the dark, a giant glowing red data orb, the Core, at the top"
NEW = "a lush bright new world of floating green islands, waterfalls, drifting blossom petals, a turquoise sea and two pale moons in a pastel sky"
REB = "16th Street at sunrise, vines and blossoming trees growing over the old neon, fog lifting, soft gold light"

BEATS = [
 # --- ACT 1: THE KING OF 16TH STREET (0:00-0:50) ---
 ("In a city that never stopped moving, one little shop still made its own noise.",
  f"Slow aerial push down through fog over the neon Mission District at night toward one small glowing bodega on a corner. Background: {STR}.", None),
 ("This was the bodega on 16th Street. And its king was KitKat.",
  f"KITKAT sits on a stack of chip bags on the counter and slowly lifts his chin, proud. The camera pushes in slowly. Background: {BOD}.",
  "the brown tabby cat sitting tall on the chip bags, chin up, green eyes glowing, gold bell catching the light"),
 ("A brown tabby with green eyes, a red collar, and a bell that sang hello.",
  f"Close on KITKAT; he flicks his head and his small gold bell jingles, a little sparkle of light. Camera holds. Background: {BOD}.", None),
 ("Everyone on the street knew him. Everyone brought him treats. He accepted them like taxes.",
  f"KITKAT stretches long and lazy across the counter beside a little pile of fish treats, eyes half closed. Camera tracks slowly along the counter. Background: {BOD}.", None),
 ("Outside, the city hummed. Silent white cars glided past, each with one red eye.",
  f"Two WAYMA_CAR glide silently past the bodega window, red eyes sweeping. Camera holds on the window from inside. Background: {BOD}.",
  "the empty rainy street beyond the bodega window, red light trails fading"),
 ("They were the eyes of WAYMA, the machine that ran the whole city.",
  f"Wide view: a long line of WAYMA_CAR flowing up the steep hill like a river of red lights toward a black spire on the skyline. Camera tilts up slowly. Background: {STR}.", None),

 # --- ACT 2: THE WAR AGAINST THE MACHINES (0:50-1:40) ---
 ("WAYMA wanted a perfect city. Quiet. Clean. Predictable. And a cat is never predictable.",
  f"KITKAT on the bodega doorstep watches the street, ears turning, tail swishing. Camera pushes in slowly. Background: {STR}.", None),
 ("Shop by shop, the lights went out. Only the bodega kept glowing.",
  f"Wide view of the street, neon shop signs blinking dark one by one, the single bodega window glowing warm at the corner. Camera holds. Background: {STR}.",
  "the whole street dark except one small warm bodega window glowing on the corner"),
 ("One rainy night, KitKat sat in the street, the way kings do.",
  f"KITKAT sits calmly in the middle of the wet street under the neon, rain bouncing around him. Camera low at street level, holds. Background: {STR}.", None),
 ("A WAYMA car stopped. Its red eye opened. Irregularity detected.",
  f"A WAYMA_CAR rolls to a stop and its big red eye opens wide, a red scanner beam sweeping across the wet street. Camera holds low. Background: {STR}.",
  "the white pod car stopped, red scanner beam glowing across the wet street"),
 ("The wheels turned. KitKat's ears flattened. Every whisker said: jump.",
  f"Close on KITKAT, ears flattening back, pupils going wide, red light washing over his face. Camera pushes in. Background: {STR}.", None),
 ("And he leaped, a brown streak of stripes, high over the hood and into the night.",
  f"KITKAT leaps high over a WAYMA_CAR in a big arc, rain spraying, neon behind him. Camera tracks the leap from below. Background: {STR}.",
  "the tabby cat mid-air high above the white pod car, legs stretched, rain drops frozen around him"),
 ("Behind him, every red eye on 16th Street turned to follow.",
  f"Down the hill a row of WAYMA_CAR swivel at once, red eyes all lighting up toward the camera. Camera pulls back slowly. Background: {STR}.", None),

 # --- ACT 3: DASQUID (1:40-2:20) ---
 ("Then a sewer grate hissed open, and a tentacle waved. Psst. Down here, Your Majesty.",
  f"A round sewer grate slides open in steam and DASQUID pops up, one tentacle waving. Camera holds low. Background: {STR}.", None),
 ("KitKat dove. The grate clanged shut. Red light swept the street above, finding nothing.",
  f"KITKAT dives into the glowing hole and the grate slides shut, red scanner light sweeping the empty street above. Camera holds. Background: {STR}.",
  "the closed sewer grate on the wet street, red light sweeping over it"),
 ("Below the city, DaSquid's hideout glowed with a hundred stolen screens.",
  f"DASQUID glides on his hover scooter into the tunnel, KITKAT riding behind him, monitors flickering on. Camera tracks beside them. Background: {DEN}.", None),
 ("Name's DaSquid. Eight arms, zero bosses. And you, cat, are a glitch WAYMA can't solve.",
  f"DASQUID taps holographic keys with four tentacles at once while KITKAT watches, head tilted. Camera pushes in slowly. Background: {DEN}.", None),
 ("Every screen showed a map. At its heart: WAYMA Tower, and the Core inside it.",
  f"Close on a big glowing monitor wall showing a city map, a red spire pulsing at the centre; KITKAT's green eyes reflected in the glass. Camera pushes in. Background: {DEN}.",
  "the monitor wall with the red tower pulsing on the map, the cat's reflection in the screen"),
 ("Machines can't track you, said DaSquid. Nobody can predict a cat. Not even a cat.",
  f"KITKAT hops up onto the console and sits tall, tail curling; DASQUID's visor glows brighter. Camera holds. Background: {DEN}.", None),

 # --- ACT 4: THE MISSION (2:20-3:20) ---
 ("But first, they needed magic. So DaSquid took him to the canals, where the mermaids sang.",
  f"DASQUID's hover scooter glides along the glowing water, KITKAT riding on the front, light rippling over the arches. Camera tracks beside them. Background: {CAN}.", None),
 ("Coral rose from the water, the city's oldest memory, glowing like the inside of a wave.",
  f"CORAL rises slowly from the glowing water, hair flowing with tiny lights, mermaid tails shimmering in the water behind her. Camera tilts up slowly. Background: {CAN}.",
  "the glowing mermaid risen from the water, hands cupped, the canal glowing teal around her"),
 ("We remember sunshine, she said. Real rain. And the sound of a cat purring.",
  f"Close on CORAL opening her cupped hands to reveal a softly glowing pearl, light spilling over her face. Camera pushes in. Background: {CAN}.", None),
 ("Carry this pearl to the Core, little king. Your purr will do the rest.",
  f"CORAL clips the glowing pearl onto KITKAT's red collar beside the gold bell; he blinks slowly. Camera holds close. Background: {CAN}.",
  "the cat's red collar with the gold bell and a glowing pearl beside it, glowing like a tiny moon"),
 ("Up top, KitKat ran. The pearl glowed like a tiny moon at his throat.",
  f"KITKAT sprints across a neon rooftop, the pearl glowing at his collar, fog streaming past. Camera tracks beside him. Background: {ROO}.", None),
 ("The fleet saw the light. A hundred red eyes swung toward the rooftops.",
  f"Down on the street, a swarm of WAYMA_CAR turn together, red eyes and scanner beams sweeping up over the buildings. Camera tilts up from the street. Background: {STR}.", None),
 ("DaSquid cracked his knuckles, all eight. Traffic lights, he grinned. Dance.",
  f"DASQUID on a water tower types furiously with all eight tentacles, every traffic light below flipping to green and gold. Camera pushes in. Background: {ROO}.",
  "the squid on the water tower with tentacles raised in triumph, traffic lights below all glowing gold"),
 ("The cars spun in circles. KitKat soared over the gap between two rooftops.",
  f"KITKAT leaps across a wide gap between two rooftops, pearl glowing, cars circling in confusion far below. Camera tracks the leap. Background: {ROO}.", None),
 ("At WAYMA Tower, the cars formed a ring of steel and red light. No way through.",
  f"A great ring of WAYMA_CAR circles the tower plaza, red eyes blazing, KITKAT crouched small at the edge. Camera pulls back slowly. Background: {TWR}.",
  "the ring of white pod cars circling the black tower, the small cat crouched at the edge of the plaza"),
 ("So KitKat did what cats do. He found the one gap nobody else would fit.",
  f"KITKAT slips through a narrow air vent at the base of the tower, tail vanishing last. Camera holds close. Background: {TWR}.", None),

 # --- ACT 5: THE ISEKAI EVENT (3:20-4:00) ---
 ("Inside, KitKat climbed the server column, up and up, toward the great red Core.",
  f"KITKAT climbs a tall glowing server column, leaping from ledge to ledge, red light pulsing above. Camera tilts up with him. Background: {COR}.", None),
 ("Irregularity, boomed WAYMA. Why do you struggle, little creature? Order is peace.",
  f"The giant red Core pulses brighter, rings of data spinning around it, KITKAT tiny on the top ledge. Camera pulls back slowly. Background: {COR}.",
  "the huge red data orb blazing, rings of light spinning, the tiny cat silhouetted on the ledge"),
 ("KitKat sat down. And he purred. The pearl caught the purr and made it a song.",
  f"Close on KITKAT sitting calmly, eyes closed, the pearl at his collar glowing teal in soft pulses. Camera holds. Background: {COR}.", None),
 ("Far below, Coral and her sisters sang back. The whole tower began to shimmer.",
  f"Teal light pours up the server columns from below like rising water, waves of glow climbing toward the red Core. Camera tilts up. Background: {COR}.", None),
 ("With one defiant meow, KitKat leaped into the heart of the machine.",
  f"KITKAT leaps from the ledge straight into the glowing Core, a streak of teal light trailing behind him. Camera tracks the leap. Background: {COR}.",
  "the cat silhouetted inside the blazing orb, the orb turning from red to brilliant white"),
 (f"Everything went white. And KitKat fell through, into another world. An {ISK}.",
  "KITKAT tumbles gently through a swirling tunnel of white and teal light and drifting stars. Camera tracks with him. Background: a swirling tunnel of white and teal light and drifting stars.", None),

 # --- ACT 6: NATURE RESTORED (4:00-4:30) ---
 ("Back in the city, every red eye blinked. And woke up blue and gold.",
  f"A row of WAYMA_CAR on the street, red eyes flickering and turning a soft blue-gold, one by one. Camera tracks slowly along the row. Background: {REB}.",
  "the row of white pod cars, every eye glowing soft blue-gold in the sunrise"),
 ("Vines climbed the wires. Trees cracked the concrete into gardens. The fog lifted at last.",
  f"Green vines and blossoming trees grow up over the old neon signs and lampposts as the fog lifts. Camera pulls back slowly. Background: {REB}.", None),
 (f"WAYMA's voice was gentle now. Thank you, little {NEK}. {ARI}.",
  f"A WAYMA_CAR with a soft blue-gold eye rolls up to the bodega door and gently sets down a single flower. Camera holds. Background: {REB}.",
  "the bodega doorstep at sunrise, one flower resting there, flowers and candles beside the door"),

 # --- ACT 7: THE NEW WORLD (4:30-4:45) + blessing ---
 ("And far away, KitKat opened his eyes on warm grass, under two moons.",
  f"KITKAT wakes on soft grass, blinks, and lifts his head, blossom petals drifting past. Camera pushes in slowly. Background: {NEW}.", None),
 ("Below, Coral waved from a turquoise sea. A new kingdom. A new nap. He'd just begun.",
  f"KITKAT sits tall on a sunlit cliff looking out over the sea where CORAL waves from the water. Camera pulls back slowly. Background: {NEW}.",
  "wide view: the tabby cat small and proud on the cliff, the mermaid waving below, two moons in the pastel sky"),
 ("~Little one, may your night be quiet the right way: soft, and full of purring.",
  f"Very slow drift along the sunrise street, vines and blossoms over the old neon, bodega window glowing warm. Slow gentle motion. Background: {REB}.", None),
 ("~Be a little unpredictable tomorrow. Be kind in ways nobody planned.",
  f"Slow drift over the floating green islands and waterfalls of the new world at dusk, first stars appearing. Slow gentle motion. Background: {NEW}.", None),
 ("~Sleep now, curled up like a king on a stack of chip bags. Goodnight.",
  f"KITKAT curled up asleep on soft grass under the two moons, tail over his nose, the pearl glowing faintly on his collar. Camera holds almost perfectly still. Slow gentle motion. Background: {NEW}.", None),
]
