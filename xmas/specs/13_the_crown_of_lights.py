"""13 — The Crown of Lights (St. Lucia Day). A big-sister story on the dark lodge stairs."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
CROWN = "a leafy green crown of five little glowing lamp-candles"

# The Door Wall, exactly as every other day, but before sunrise: same props, darker windows.
HALL_DARK = dict(
    DOORWALL,
    scene="the lodge great hall before sunrise",
    light="Low firelight glows in the hall before sunrise, the tall windows still dark with night",
    atmo="Firelight flickers and snow drifts past the dark windows",
)

STORY = {
    "num": "13",
    "slug": "the-crown-of-lights",
    "title": "The Crown of Lights",
    "meta": [
        ("Day", "Sunday, December 13 · door thirteen"),
        ("Holiday thread", "St. Lucia Day: the eldest girl wears a crown of lights and carries buns to the "
                           "household before sunrise"),
        ("Guests", "Nora Snowmane ❄️, Willa Wobble ❄️, Lina the snowflake crisp"),
        ("Cat’s role", "stair scout: slides down the banister ahead of the walk and reports back (one mop, friendly)"),
        ("Mandarin", "妹妹 little sister · 早安 good morning"),
        ("Setting", "Frostpeak Lodge before sunrise: the Door Wall by low firelight, the long dark staircase, "
                    "the breakfast hall at sunrise; Lantern Lane and the bunk room at night"),
    ],
    "palette": "deep midnight blue and warm cream with saturated saffron gold and berry red accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "NORA", "WILLA", "LINA"],
    "cast_note": "Humans in this story: none. Tori's crown holds five little lamp-candles (tiny electric lamps "
                 "shaped like candles, a steady warm glow, never a flame). The buns are golden saffron buns "
                 "curled like snails.",
    "key_shot": 6,
    "places": {
        "hall": HALL_DARK,
        "stairs": {
            "name": "the long grand staircase of Frostpeak Lodge before sunrise",
            "scene": "the long dark lodge staircase",
            "props": "a wide wooden staircase with a banister carved into little pine trees, a striped stair "
                     "runner, a tall grandfather clock on the landing, framed paintings of snowboards up the wall, "
                     "a shelf of small brass lamps, a friendly old mop leaning in a corner",
            "light": "The gold glow of little lamps pools on the dark steps in the last of the night",
            "accents": "saffron gold and deep indigo blue",
            "atmo": "Dust motes drift through the lamp glow",
            "motion": "dust motes drift through the lamp glow",
        },
        "breakfast": {
            "name": "the breakfast hall of Frostpeak Lodge at sunrise",
            "scene": "the sunrise breakfast hall",
            "props": "a long plank table with a red checked cloth, a row of blue cocoa mugs, a big round window "
                     "facing the mountains, pots of cloudberry jam, wooden benches with sheepskins, a rack of toast",
            "light": "Pink and gold sunrise pours through the big round window",
            "accents": "sunrise pink and saffron gold",
            "atmo": "Curls of cocoa steam rise from the mugs",
            "motion": "curls of cocoa steam rise from the mugs",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a leafy green crown of five little lamps and one saved golden bun on a plate on the nightstand"),
    },
    "shots": [
        {"title": "Door thirteen", "place": "hall", "time": "night",
         "angle": "Low angle looking up the tall wall of little carved doors in",
         "who": "TORI reaches one tiny arm up to a little door carved with a plain crown and turns its brass knob, "
                f"green straw tall; {ROSIE_CUP} stands beside her holding a little picture list in front of her "
                "cup, eyes wide and a little drowsy; CAT the little blue penguin yawns hugely by the fireplace "
                "with one flipper over her beak",
         "beats": [
             ("It was still dark when Rosie tiptoed into the great hall. Even the fire was yawning.",
              "wide shot", "ROSIE takes one tiny tiptoe hop and blinks at the low fire", "ROSIE",
              "drowsy and curious", "pushes in", "a low fire crackle and one tiny footstep"),
             ("Door thirteen was Tori's turn. Rosie's list said so. Tori turned the tiny brass knob.",
              "medium shot", "TORI turns the little brass knob while ROSIE lifts her picture list to check it",
              ["TORI", "ROSIE"], "careful and excited", "tilts up", "a tiny squeak of a brass knob"),
             ("Behind it sat a tiny golden crown, no bigger than a button.",
              "close-up", "TORI swings the little door open and a tiny golden crown glints inside", "TORI",
              "surprised and pleased", "pushes in", "a soft wooden click and a low fire crackle"),
         ]},
        {"title": "St. Lucia Day", "place": "hall", "time": "night",
         "angle": "Medium view across the long woven rug toward the fireside armchair in",
         "who": "NORA sits in a big armchair by the fire with a steaming cocoa mug in one paw and a leafy green "
                "crown of five little lamp-candles resting in her lap, eyes soft; TORI looks up at her with bright "
                f"curious eyes; {ROSIE_CUP} leans in close with her straw perked up",
         "beats": [
             ("\"Today is St. Lucia Day,\" said Nora the polar bear, softly, over her cocoa mug.",
              "medium shot", "NORA lowers her cocoa mug and smiles through the steam", "NORA",
              "calm and warm", "pushes in", "a soft sip and a low fire crackle"),
             ("\"The eldest girl wears a crown of lights. She carries buns to everyone before sunrise.\"",
              "medium close-up", "NORA lifts the leafy crown from her lap and holds it up in both paws", "NORA",
              "gentle and proud", "tilts up", "a rustle of leaves"),
             ("\"On the darkest mornings, somebody brings the light,\" said Nora. \"Today, somebody is Tori.\"",
              "medium shot", "TORI points one tiny arm at herself and her green straw bobs", "TORI",
              "amazed and honored", "pans left", "a tiny creak of a floorboard and a low fire crackle"),
         ]},
        {"title": "A cake that can walk", "place": "hall", "time": "night",
         "angle": "Low angle from the hearth rug looking up at",
         "who": f"NORA lowers {CROWN} onto the lid of TORI, who stands as tall as she can with shining eyes; "
                "CAT the little blue penguin tilts her head with a cheeky grin, gold lamp glow on her beak",
         "beats": [
             ("Nora set a leafy crown on Tori's lid. Five little lamp-candles. Click. They glowed.",
              "medium shot", "NORA settles the crown on the lid of TORI and the five little lamps glow gold",
              ["NORA", "TORI"], "careful and delighted", "pushes in", "one soft click and a rustle of leaves"),
             ("Tori stood very tall. Then a bit taller. \"How do I look?\"",
              "medium close-up", "TORI stretches up on her tiny legs and the crown glows above her straw", "TORI",
              "proud and a little shy", "tilts up", "a tiny creak of a floorboard"),
             ("\"Like a birthday cake that can walk,\" said Cat the penguin. \"So, perfect.\"",
              "medium close-up", "CAT grins and gives one slow approving nod", "CAT", "cheeky and fond",
              "holds still", "a tiny penguin foot tap"),
         ]},
        {"title": "Rosie's job", "place": "hall", "time": "night",
         "angle": "Close view at tray height beside the copper cocoa urn in",
         "who": "MOM holds out a wooden tray of golden buns, each one curled like a snail, smiling warmly; "
                f"{ROSIE_CUP} holds both tiny arms out in front of her cup to take the tray, straw wiggling; "
                "LINA stands on the rim of the tray puffing white sugar over the buns",
         "beats": [
             ("Mom carried in a tray of golden buns, curled like snails. The hall smelled of saffron and butter.",
              "medium shot", "MOM lowers the tray of curled buns and steam rises from them", "MOM",
              "warm and proud", "pushes in", "a soft tray clink and a low fire crackle"),
             ("\"Rosie carries the tray,\" said Mom. Rosie's straw wiggled. A job! She put it on her list.",
              "medium close-up", "ROSIE takes the tray in front of her cup and her straw wiggles", "ROSIE",
              "thrilled and serious", "tilts down", "a wooden tray scrape"),
             ("Lina hopped along the edge. Poof! Poof! Poof! \"Every bun gets a sugar-snow hat.\"",
              "close-up", "LINA hops along the tray rim and white sugar puffs over each bun", "LINA",
              "busy and pleased with herself", "pans right", "three soft poofs"),
         ]},
        {"title": "Thirty-nine steps", "place": "stairs", "time": "night",
         "angle": "High angle from the very top step looking steeply down",
         "who": f"{ROSIE_CUP} stands on the top step holding the tray of curled golden buns in front of her cup, "
                "straw drooping, eyes wide; the long stairs fall away below her into soft blue shadow",
         "beats": [
             ("Then came the stairs. The long, long stairs. Thirty-nine steps of dark.",
              "wide shot", "ROSIE peers over the edge of the top step, holding the tray very still", "ROSIE",
              "small and unsure", "tilts down", "a slow tick of a grandfather clock"),
             ("Rosie's straw drooped. One tray. Twelve round buns. Every one of them wanted to roll.",
              "medium close-up", "ROSIE's straw droops as the buns shift a little on the tray", "ROSIE",
              "daunted and wide-eyed", "holds still", "a slow tick of a clock and a tiny wobble on wood"),
         ]},
        {"title": "Walk in my light", "place": "stairs", "time": "night",
         "angle": "Low angle from three steps down looking up at",
         "who": f"TORI wears {CROWN} and bends toward her sister from one step below, a warm circle of gold "
                f"light on the step between them; {ROSIE_CUP} holds the tray of curled golden buns in front of "
                "her cup and looks down into the circle of light with hopeful eyes",
         "beats": [
             ("Tori stepped down one stair. Her crown made a little circle of gold on the step.",
              "medium shot", "TORI bends closer and the circle of gold light slides across the step", "TORI",
              "kind and steady", "tilts down", "one soft step on the stair runner"),
             ("\"Walk in my light, little sip,\" said Tori. \"I go first. You stay in the circle.\"",
              "medium close-up", "TORI nods toward the gold circle and ROSIE's straw lifts a little",
              ["TORI", "ROSIE"], "reassuring and hopeful", "pushes in", "a slow tick of a clock"),
         ]},
        {"title": "The morning song", "place": "stairs", "time": "night",
         "angle": "Medium view past the carved banister post on",
         "who": "NORA walks down the stairs with her cocoa mug raised like a lantern, humming with her eyes "
                "closed and her blue shawl swaying; LINA stands on top of the banister post puffing white sugar "
                "that drifts down through the gold lamp glow like tiny stars",
         "beats": [
             ("Nora began to hum the old morning song. It rumbled like a cello under a quilt.",
              "medium shot", "NORA hums with her eyes closed and sways her cocoa mug in time", "NORA",
              "deep and dreamy", "tracks beside", "a low warm hum of wind in the stairwell"),
             ("Lina kept the beat. Poof. Poof. Poof. Sugar snow drifted down the stairs like tiny stars.",
              "medium close-up", "LINA hops on the banister post and puffs of sugar float down", "LINA",
              "bright and busy", "tilts down", "three soft poofs"),
         ]},
        {"title": "Step. Step. Step.", "place": "stairs", "time": "night",
         "angle": "Wide side view along the carved banister and the striped stair runner of",
         "who": f"TORI wears {CROWN} and walks one stair ahead, glancing back kindly; {ROSIE_CUP} stands inside "
                "the circle of gold light holding the tray of buns in front of her cup with a careful brave face; "
                "CAT the little blue penguin slides down the carved banister on her tummy with both flippers out",
         "beats": [
             ("Step. Step. Step. Rosie stayed inside the gold circle. The buns stayed on the tray.",
              "wide shot", "ROSIE takes one small careful hop down inside the circle of gold light", "ROSIE",
              "careful and brave", "tracks beside", "soft steps on the stair runner"),
             ("Cat slid down the banister to scout ahead. \"All clear! One mop. It's friendly.\"",
              "medium shot", "CAT slides down the banister on her tummy and waves one flipper back", "CAT",
              "zippy and helpful", "pans right", "a long wooden swish"),
         ]},
        {"title": "Quite big steps", "place": "stairs", "time": "night",
         "angle": "Low angle from the stair runner looking up past a tiny penguin on",
         "who": "WILLA stands on the edge of a stair far too big for her, holding a paper star on a stick, purple "
                "earmuffs fluffy, eyes shy and bright in the gold lamp glow; NORA walks behind her with her cocoa "
                "mug, smiling down",
         "beats": [
             ("Behind them came tiny Willa with a paper star on a stick, one stair at a time.",
              "medium shot", "WILLA hops down one big stair and her paper star bobs on its stick", "WILLA",
              "shy and determined", "tracks beside", "one tiny plop on the stair runner"),
             ("\"The smallest step is still a step,\" whispered Willa. \"These are quite big steps, though.\"",
              "medium close-up", "WILLA looks down over the edge of the next stair and gulps", "WILLA",
              "brave and wobbly", "tilts down", "a tiny scuff of feet and a slow tick of a clock"),
         ]},
        {"title": "Lopsided", "place": "stairs", "time": "night",
         "angle": "Medium view across the middle landing beside the grandfather clock on",
         "who": f"TORI stands on the middle landing with {CROWN} tipped down over one eye, both tiny arms "
                f"stretched up and far too short to reach it, mouth a surprised circle; {ROSIE_CUP} stands one "
                "step above her holding the tray of buns in front of her cup, eyes wide",
         "beats": [
             ("Halfway down, Tori looked back to check on Rosie. Her crown slid over one eye.",
              "medium shot", "TORI turns her head and the glowing crown slips down over one eye", "TORI",
              "startled and blinking", "pushes in", "a rustle of leaves and a tiny rattle of lamps"),
             ("Tori's tiny arms could not reach her own lid. \"I've gone lopsided,\" she said.",
              "medium close-up", "TORI stretches both tiny arms up and the tipped crown wobbles", "TORI",
              "stuck and trying to stay calm", "tilts up", "a wobbling rustle of leaves"),
         ]},
        {"title": "One bun thought about it", "place": "stairs", "time": "night",
         "angle": "Tight close view over the tray of buns on",
         "who": f"{ROSIE_CUP} leans forward from the step above and nudges {CROWN} straight with the tip of her "
                "striped straw, the tray of buns held level in front of her cup, tongue out in concentration; "
                "TORI holds very still below her with one eye peeking out and a growing smile",
         "beats": [
             ("Rosie was one step above. She leaned in and nudged the crown straight with her straw.",
              "close-up", "ROSIE leans in and pushes the crown level with the tip of her straw", "ROSIE",
              "focused and gentle", "pushes in", "a soft rustle of leaves"),
             ("Not one bun spilled. One bun thought about it. It stayed.",
              "close-up", "ROSIE steadies the tray as one curled bun rocks at the edge and settles", "ROSIE",
              "tense, then relieved", "tilts down", "a tiny wobble on wood, then stillness"),
         ]},
        {"title": "Eyes closed", "place": "stairs", "time": "night",
         "angle": "Wide view from the landing looking back up the shadowy flight of",
         "who": f"TORI beams with {CROWN} sitting straight on her lid; {ROSIE_CUP} looks slowly around the dim "
                "stairs with calm curious eyes, the tray of buns in front of her cup; the grandfather clock and "
                "the friendly old mop stand in soft blue shadow behind them",
         "beats": [
             ("\"You fixed my light,\" said Tori. \"Thank you, **妹妹** (mèimei) = little sister.\"",
              "medium shot", "TORI beams and dips her glowing crown toward ROSIE in a little bow",
              ["TORI", "ROSIE"], "grateful and proud", "pushes in", "a slow tick of a clock"),
             ("Rosie looked around. The dark was only the stairs with their eyes closed.",
              "wide shot", "ROSIE turns slowly to look up the shadowy stairs and her straw rises", "ROSIE",
              "calm and surprised at herself", "pulls back", "a slow tick of a clock and a soft breath"),
         ]},
        {"title": "A light of her own", "place": "stairs", "time": "night",
         "angle": "Close view at tray height on the last landing of",
         "who": f"TORI wears {CROWN} and sets one small glowing brass lamp on the tray of buns; {ROSIE_CUP} holds "
                "the tray in front of her cup, her face lit gold from below, straw rising; WILLA stands close "
                "behind in the new circle of light holding her paper star on a stick",
         "beats": [
             ("On the last landing, Tori clicked on a small brass lamp and set it on Rosie's tray.",
              "close-up", "TORI sets the small brass lamp on the tray and its glow spreads", "TORI",
              "tender and sure", "pushes in", "one soft click"),
             ("\"Your own light,\" said Tori. \"You've got this, little sip.\"",
              "medium close-up", "ROSIE looks down at the lamp and her straw springs up tall", "ROSIE",
              "glowing with pride", "tilts up", "a soft happy breath"),
             ("Now Rosie walked in her own gold circle. And tiny Willa walked in Rosie's.",
              "medium shot", "WILLA hops into the gold circle behind ROSIE and lifts her paper star",
              ["WILLA", "ROSIE"], "safe and cheerful", "pulls back", "two soft steps on the stair runner"),
         ]},
        {"title": "Good morning", "place": "breakfast",
         "angle": "Wide view down the long plank table in",
         "who": f"{ROSIE_CUP} stands on the table holding out a curled golden bun in front of her cup, a small "
                f"brass lamp beside her, proud eyes; TORI wears {CROWN} and sways with her straw held high and a wide open smile; "
                "MOM sits on the bench with shiny happy eyes and her tiny arms clasped; CAT the little blue "
                "penguin holds a bun in both flippers",
         "beats": [
             ("At the bottom, the breakfast hall was waiting. So was everybody's tummy.",
              "wide shot", "CAT pats her tummy and reaches both flippers toward the buns", "CAT",
              "hungry and cheerful", "pushes in", "a clink of mugs and a creak of benches"),
             ("\"**早安** (zǎo ān) = Good morning!\" sang Tori. Rosie handed out buns, one by one.",
              "medium shot", "TORI sways with her straw held high while ROSIE holds out a curled bun", ["TORI", "ROSIE"],
              "bright and proud", "tracks beside", "a clink of mugs and a soft bench creak"),
             ("Mom's eyes were shiny. \"My two lights,\" she said. Cat saved a bun for the mop.",
              "medium close-up", "MOM presses her tiny arms to her lid while CAT tucks a bun under one flipper",
              ["MOM", "CAT"], "moved and tickled", "pans right", "a soft clink of mugs"),
         ]},
        {"title": "The sun comes to breakfast", "place": "breakfast",
         "angle": "Long view along the red checked cloth toward the big round window in",
         "who": "NORA sits at the head of the table lifting her cocoa mug in one paw and a curled bun in the "
                "other with a soft smile; WILLA perches on an upturned mug nibbling a bun as big as her head; "
                "LINA stands on the windowsill looking out at the pink sunrise with one tiny arm raised",
         "beats": [
             ("\"Sit,\" said Nora. \"Cocoa first. Then buns. Then feelings.\" Rosie's feeling was proud.",
              "medium shot", "NORA raises her cocoa mug and takes a slow happy sip", "NORA",
              "content and kind", "pushes in", "a slow sip and a clink of mugs"),
             ("Then the big window turned pink, then gold. The sun had come to breakfast too.",
              "wide shot", "WILLA stops nibbling and stares as gold light spreads across the table", "WILLA",
              "awed and cozy", "tilts up", "a soft hush and a tiny crumb patter"),
             ("Lina studied the sunrise. \"Pretty,\" she said. \"Needs sugar.\" Poof!",
              "medium close-up", "LINA tilts her head at the window and puffs a white cloud of sugar at it", "LINA",
              "thoughtful and cheeky", "pans left", "one soft poof"),
         ]},
        {"title": "Lantern thirteen", "place": "lane", "time": "night",
         "angle": "Upward view along the string of lanterns over",
         "who": "TORI stands on a snowy crate hooking a cream paper lantern painted with a gold crown onto the "
                f"long string, green straw tall; {ROSIE_CUP} stands below her holding a small glowing brass lamp "
                "up in front of her cup so its light falls on the hook, straw high; MOM steadies the crate with "
                "a calm smile; CAT the little blue penguin points one flipper up at the lantern",
         "beats": [
             ("That night they hung lantern thirteen on Lantern Lane. Cream paper, with a gold crown.",
              "wide shot", "CAT points up as the cream lantern sways on the string", "CAT",
              "eager and proud", "tilts up", "a soft crunch of snow and a creak of string"),
             ("Tori hooked it up high. Rosie held her little lamp underneath, so Tori could see.",
              "medium shot", "TORI slips the lantern onto its hook while ROSIE holds her lamp steady below",
              ["TORI", "ROSIE"], "careful and teamed up", "pushes in", "a tiny click of a hook"),
             ("\"One more light,\" said Rosie. \"Two,\" said Tori, \"counting yours.\"",
              "medium close-up", "ROSIE looks at the lamp in front of her cup and her straw wiggles", "ROSIE",
              "proud and warm", "pulls back", "a soft crunch of snow and a far sizzle of a grill"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; TORI tucked in the next bunk with her green straw resting on the pillow; CAT the little "
                "blue penguin asleep curled on a soft pillow at the foot of the bed, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, with a lamp of your own. Goodnight, Tori, tall under your crown.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Cat. Goodnight, friendly mop. May morning find you with warm buns and a light to walk in.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, with a lamp of your own.",
        "Goodnight, Tori, tall under your crown.",
        "Goodnight, Cat. Goodnight, friendly mop.",
        "May morning find you with warm buns and a light to walk in.",
    ],
}
