"""22 — Gabby and the Sky Full of Stars (Tuesday, December 22)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

RIDGE_PROPS = ("a round wooden lookout deck with a log rail, a brass spyglass on a tripod, a heap of plaid "
               "blankets, a sled stacked with a cocoa flask and tin mugs, a lone wind-bent pine, a little wooden "
               "easel")

STORY = {
    "num": "22",
    "slug": "gabby-and-the-sky-full-of-stars",
    "title": "Gabby and the Sky Full of Stars",
    "meta": [
        ("Day", "Tuesday, December 22 · door twenty-two"),
        ("Holiday thread", "The northern lights over Aurora Ridge"),
        ("Guests", "Gabby the black star shark (leads), Aurora Frostholm ❄️, Cleo Coldwater ❄️, "
                   "Lina the snowflake crisp"),
        ("Cat’s role", "night guide up the ridge (she knows every bump) and keeper of the facts about who is "
                       "named after what"),
        ("Mandarin", "星星 star · 極光 northern lights"),
        ("Setting", "The Door Wall in the lodge great hall, then the Aurora Ridge lookout at night, "
                    "Lantern Lane at night, and the bunk room"),
    ],
    "palette": "deep indigo and midnight blue with saturated aurora green and rose pink accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "AURORA", "COLDWATER", "GABBY", "LINA"],
    "cast_note": "Humans in this story: none. Gabby swims through the air a little above the ground. The pattern "
                 "of white spots on her back is the same in every shot: three in a row, a little scoop, and a "
                 "wonky W, matching the brightest stars overhead.",
    "key_shot": 13,
    "places": {
        "doorwall": DOORWALL,
        "ridge": {
            "name": "the high ridge lookout above Frostpeak Valley at night",
            "scene": "the high ridge lookout",
            "props": RIDGE_PROPS,
            "light": "A sky crowded with bright stars lights the snowy ridge",
            "accents": "starlight silver and deep indigo",
            "atmo": "Breath puffs glitter in the cold and the snow glows faintly blue",
            "motion": "tiny stars twinkle above the ridge",
        },
        "ridge_lights": {
            "name": "the high ridge lookout above Frostpeak Valley at night under the northern lights",
            "scene": "the high ridge lookout",
            "props": RIDGE_PROPS,
            "light": "Ribbons of green and pink northern lights ripple across a sky full of stars",
            "accents": "aurora green and rose pink",
            "atmo": "Soft green light washes over the snow and breath puffs glitter",
            "motion": "ribbons of green and pink light ripple across the sky",
        },
        "lane_night": LANE_NIGHT,
        "bunk": bunk("a tiny silver star and a small painting of white dots on dark blue paper on the nightstand"),
    },
    "shots": [
        {"title": "Door twenty-two", "place": "doorwall",
         "angle": "Close view at knob height along the rows of little carved doors in",
         "who": "GABBY floats in front of one open little door with her nose just touching its brass knob, a tiny "
                "silver five-pointed shape resting inside the door, her eyes wide; MOM leans in beside her with a "
                "soft smile",
         "beats": [
             ("Door twenty-two belonged to Gabby the black star shark. She bumped the knob with her nose. Click.",
              "close-up", "GABBY bumps the little brass knob with her nose and the door swings open", "GABBY",
              "careful and curious", "pushes in", "a soft bump and a tiny door creak"),
             ("Behind it sat a tiny silver star. \"**星星** (xīngxing) = star,\" said Mom.",
              "medium close-up", "MOM points one tiny arm at the tiny silver shape in the door", "MOM",
              "warm and pleased", "holds still", "a crackling fire"),
         ]},
        {"title": "Why are you called that?", "place": "doorwall",
         "angle": "Low angle from the long woven rug looking up at",
         "who": "LINA hops on the rug with a puff of white powdered sugar bursting off her corners, pointing one "
                "tiny arm up; GABBY floats above her, twisted around to peer over her own shoulder at her back, puzzled",
         "beats": [
             ("\"A star for the star shark!\" said Lina. Poof! \"Gabby, why are you called that?\"",
              "medium shot", "LINA hops and a white puff of sugar bursts around her", "LINA",
              "bright and nosy", "tilts up", "a soft poof and a crackling fire"),
             ("Gabby peered over her shoulder. \"No idea. I can't see my own back. I'm told there are dots.\"",
              "medium close-up", "GABBY twists to look over her own shoulder and turns in a slow circle", "GABBY",
              "puzzled and unbothered", "pushes in", "a soft swish of fins"),
         ]},
        {"title": "It wasn't me", "place": "doorwall",
         "angle": "Medium view beside the crackling stone fireplace in",
         "who": f"GABBY floats with a small dry smile; {ROSIE_CUP} and TORI stand side by side "
                "on the rug, both turned to look at LINA; LINA stands very straight with both tiny arms up and a "
                "trail of white sugar behind her",
         "beats": [
             ("\"Kyle says it looks like somebody sneezed sugar on me.\"",
              "medium close-up", "GABBY gives a small dry smile and shrugs one fin", "GABBY",
              "dry and deadpan", "holds still", "a crackling fire"),
             ("Everybody looked at Lina. \"It wasn't me,\" said Lina. \"This time.\"",
              "medium shot", "ROSIE and TORI turn to look at LINA, and LINA throws both tiny arms up",
              ["ROSIE", "TORI", "LINA"], "suspicious and giggly", "pans right", "a tiny poof and a clink of cups"),
         ]},
        {"title": "Last one up buys cocoa!", "place": "doorwall",
         "angle": "Dynamic diagonal view from the antler coat rack toward the open front door of",
         "who": "AURORA skids in through the open front door on her shimmering rainbow-sheen skis with snow flying "
                "off her striped scarf, one paw pointing straight up; CAT the little blue penguin leans against "
                "the copper cocoa urn with one flipper beside her beak and a sideways grin",
         "beats": [
             ("BANG went the door. In skied Aurora Frostholm. \"The sky lights are coming tonight! Up on my ridge!\"",
              "wide shot", "AURORA skids to a stop on the rug and points one paw straight up", "AURORA",
              "breathless and thrilled", "pushes in", "a door bang and a scrape of skis"),
             ("\"Last one up buys cocoa!\" she called.",
              "medium shot", "AURORA spins on her skis and waves toward the door", "AURORA",
              "competitive and gleeful", "pans left", "a clatter of skis"),
             ("\"It's called Aurora Ridge,\" whispered Cat the penguin. \"She thinks it's named after her.\"",
              "medium close-up", "CAT leans in behind one flipper and tips her head toward the door with a grin", "CAT",
              "cheeky and fond", "holds still", "a soft crackling fire"),
         ]},
        {"title": "Up, up, up", "place": "ridge", "time": "night",
         "angle": "Wide view up the last snowy steps toward",
         "who": "CAT the little blue penguin marches at the front with a little brass lamp held high in one "
                "flipper, chest out; MOM comes last up the steps pulling a small sled stacked with a cocoa flask "
                "and tin mugs, smiling to herself",
         "beats": [
             ("That night Cat led the way, because Cat knew every bump. Up, up, up to the lookout.",
              "wide shot", "CAT lifts her little lamp higher and takes one proud step up", "CAT",
              "sure-footed and proud", "tilts up", "crunching steps in snow"),
             ("Last one up was Mom. On purpose. She had carried the cocoa anyway.",
              "medium shot", "MOM pulls the cocoa sled up the last step and pats the flask", "MOM",
              "calm and amused", "pulls back", "a sled runner scrape and a clink of tin mugs"),
             ("Mom poured. Everybody waited. Waiting is easier with cocoa.",
              "medium close-up", "MOM pours steaming cocoa from the flask into a tin mug", "MOM",
              "cozy and patient", "pushes in", "a slow pour and a clink of tin"),
         ]},
        {"title": "Only sky", "place": "ridge", "time": "night",
         "angle": "Very low angle from the snowy deck looking straight up past a tiny cup at the huge sky over",
         "who": f"{ROSIE_CUP} stands alone by the log rail, very small under the enormous sky, holding a little picture "
                "list of dots in front of her cup and looking up, her straw drooping",
         "beats": [
             ("Above them there was only sky. More stars than Rosie had ever seen. Too many to list.",
              "wide shot", "ROSIE tips back to look up at the enormous sky", "ROSIE",
              "awed and overwhelmed", "tilts up", "a hush of wind over snow"),
             ("Rosie tried anyway. One. Two. Three. At four hundred and six, her straw drooped.",
              "medium close-up", "ROSIE looks from her list up to the sky and her straw droops slowly", "ROSIE",
              "dizzy and outnumbered", "holds still", "a tiny pencil scratch and a hush of wind"),
         ]},
        {"title": "The little pink one", "place": "ridge", "time": "night",
         "angle": "Warm close two-shot from behind two straws, looking up at one small pink star above",
         "who": f"TORI sits on a plaid blanket close beside her little sister, pointing her tall green straw up at "
                f"one small pink star; {ROSIE_CUP} sits on the blanket edge beside her, looking where she points, "
                "straw slowly lifting",
         "beats": [
             ("\"Skip to the best one,\" said Tori, sitting close. \"See that little pink one?\"",
              "medium close-up", "TORI tips her green straw up toward one small pink star beside ROSIE",
              ["TORI", "ROSIE"], "cozy and sure", "tilts up", "a soft blanket rustle"),
             ("\"You've got this, little sip.\" Rosie looked. The little pink star winked.",
              "close-up", "ROSIE looks up and her straw rises as the pink star twinkles", "ROSIE",
              "charmed and glad", "pushes in", "a hush of wind"),
         ]},
        {"title": "Every sky tells a story", "place": "ridge", "time": "night",
         "angle": "Over-the-shoulder view past swoopy orange plumes at a little easel on",
         "who": "COLDWATER dabs white dots onto a sheet of dark blue paper on the easel with her little paintbrush, "
                "dreamy and intent, a dab of white paint on her beak; the painted dots show three in a row, a "
                "little scoop and a wonky zigzag, the same as the brightest stars above her",
         "beats": [
             ("Cleo Coldwater set up her easel. \"Every slope tells a story,\" she said. \"So does every sky.\"",
              "medium shot", "COLDWATER lifts her paintbrush and looks from the sky to her paper", "COLDWATER",
              "dreamy and intent", "pushes in", "a tiny clink of a paint jar"),
             ("Dab, dab, dab. White dots on dark paper. Three in a row. A little scoop. A wonky W.",
              "close-up", "COLDWATER dabs one white dot after another onto the dark paper", "COLDWATER",
              "careful and absorbed", "pans right", "soft dabs of a brush on paper"),
         ]},
        {"title": "Hold very still", "place": "ridge", "time": "night",
         "angle": "Medium view along the log rail of",
         "who": "COLDWATER stares at GABBY with her paintbrush frozen in the air and her eyes huge; GABBY floats by "
                "the rail with a puzzled look; CAT the little blue penguin "
                "peeks out from behind the brass spyglass with one flipper over her beak",
         "beats": [
             ("Then Cleo looked at Gabby's back. At her painting. At the sky.",
              "medium shot", "COLDWATER looks from GABBY to her paintbrush to the sky and back", ["COLDWATER", "GABBY"],
              "startled and thinking", "pans left", "a hush of wind"),
             ("\"Gabby. Hold very still.\" \"Oh no,\" whispered Cat. \"She's going to paint her.\"",
              "medium close-up", "CAT ducks behind the spyglass and peeks out with one eye", "CAT",
              "alarmed and giggly", "pushes in", "a tiny squeak of the spyglass"),
         ]},
        {"title": "One for one", "place": "ridge", "time": "night",
         "angle": "High angle looking down over a small painting and a spotted back on",
         "who": "COLDWATER holds her painting of white dots on dark blue paper right beside GABBY's back, where "
                f"tiny white star-shaped spots make the very same pattern; {ROSIE_CUP} stands on the log rail "
                "holding a little picture list in front of her cup, the list showing plain doodles of dots, "
                "straw wiggling",
         "beats": [
             ("Cleo only held her painting beside Gabby's back. Three in a row. A little scoop. A wonky W.",
              "close-up", "COLDWATER holds the painting next to GABBY and the two patterns line up",
              ["COLDWATER", "GABBY"], "amazed and certain", "pushes in", "a paper rustle"),
             ("The sky matched the spots on Gabby's back, one for one. Rosie checked them off. Twice.",
              "medium close-up", "ROSIE looks up at the sky and down at her list, and her straw wiggles", "ROSIE",
              "busy and thrilled", "tilts up", "a tiny pencil scratch"),
         ]},
        {"title": "A map of the sky", "place": "ridge", "time": "night",
         "angle": "Close view at fin height past the edge of a small painting on",
         "who": "GABBY floats very still in front of the painting that COLDWATER holds up for her, looking at it "
                "with big shiny eyes full of starlight and her mouth a small round O",
         "beats": [
             ("\"What is it? I can't see my own back!\" said Gabby. So Cleo turned the painting around.",
              "medium shot", "COLDWATER turns the painting to face GABBY", ["COLDWATER", "GABBY"],
              "itching with curiosity", "pans right", "a paper rustle"),
             ("Gabby looked for a long time. \"That's on my back? I've been carrying the sky around?\"",
              "close-up", "GABBY gazes at the painting and her eyes grow rounder and rounder", "GABBY",
              "astonished and thrilled", "pushes in", "a hush of wind and a paper flutter"),
         ]},
        {"title": "The northern lights", "place": "ridge_lights", "time": "night",
         "angle": "Sweeping wide view from behind the log rail up into the glowing sky over",
         "who": "MOM stands at the rail with a tin mug in her tiny arms and her face lit green, breathless; AURORA "
                "stands in the middle of the deck taking a deep bow with one paw on her chest; CAT the little "
                "blue penguin stands beside her with both flippers on her hips, shaking her head and smiling",
         "beats": [
             ("And just then the sky lit up. Green ribbons. Pink ribbons. Rippling like a scarf.",
              "wide shot", "MOM lifts her face to the sky as green light washes over the deck", "MOM",
              "breathless and amazed", "tilts up", "a soft shimmer of wind and a creak of the rail"),
             ("\"**極光** (jíguāng) = the northern lights,\" breathed Mom. \"Also called the aurora,\" said Aurora. "
              "\"After me.\"",
              "medium shot", "AURORA puts one paw on her chest and lifts her chin proudly", "AURORA",
              "proud and beaming", "pushes in", "a soft shimmer of wind"),
             ("\"Other way round,\" said Cat. But Aurora was already taking a bow.",
              "medium close-up", "CAT shakes her head while AURORA sweeps into a deep bow", ["CAT", "AURORA"],
              "fond and amused", "holds still", "a creak of skis on snow"),
         ]},
        {"title": "Fins wide", "place": "ridge_lights", "time": "night",
         "angle": "Low angle looking up from the snowy deck at a small shark swimming through the glowing air over",
         "who": "GABBY swims in a slow loop high above the deck with both fins stretched wide and her widest gentle "
                "smile, every tiny white star-shaped spot on her back glowing green and pink under the lights",
         "beats": [
             ("Gabby the star shark did a slow, happy loop overhead, right through the green and the pink.",
              "wide shot", "GABBY stretches both fins wide and glides in a slow curve overhead", "GABBY",
              "free and joyful", "tracks beside", "a soft whoosh of air"),
             ("Under the green light, every spot on her back glowed. A little swimming piece of sky.",
              "medium close-up", "GABBY banks gently and the spots on her back shimmer", "GABBY",
              "proud and shining", "tilts up", "a soft shimmer of wind"),
         ]},
        {"title": "I'm fireworks", "place": "ridge_lights", "time": "night",
         "angle": "Close upward view from the snowy deck at the log rail of",
         "who": "LINA stands on the log rail in the middle of a hop with a big puff of powdered sugar bursting "
                "around her, the sugar glowing green on one side and pink on the other, arms flung up; AURORA "
                "stands below with her head tipped back and her mouth open, perfectly silent, skis crossed",
         "beats": [
             ("Lina hopped. Poof! Her sugar snow turned green, then pink. \"I'm fireworks,\" said Lina.",
              "medium shot", "LINA hops on the rail and a glowing puff of sugar bursts around her", "LINA",
              "dazzled by herself", "tilts up", "a soft poof and a shimmer of wind"),
             ("The lights made no sound at all. Even Aurora went quiet. For nearly a whole minute.",
              "medium close-up", "AURORA gazes up with her mouth open and slowly sits down in the snow", "AURORA",
              "hushed and spellbound", "holds still", "deep quiet and one soft creak of skis"),
         ]},
        {"title": "Snow angels", "place": "ridge_lights", "time": "night",
         "angle": "High angle looking straight down at the snowy deck of",
         "who": f"{ROSIE_CUP} lies on her back in the snow in a small cup-shaped snow angel, straw pointing up; "
                "TORI lies beside her in a taller snow angel; CAT the little blue penguin lies flat with her "
                "flippers sweeping the snow; GABBY lies in a shark-shaped dent in the snow with her tail "
                "swishing, all of them washed in green light under the stars",
         "beats": [
             ("Everybody flopped back in the snow to watch. Seven snow angels and one snow shark.",
              "wide shot", "CAT sweeps her flippers through the snow while GABBY swishes her tail",
              ["CAT", "GABBY"], "blissful and silly", "pulls back", "soft swishes in snow"),
         ]},
        {"title": "A star to keep", "place": "ridge_lights", "time": "night",
         "angle": "Close view from behind a plaid blanket, two cups side by side, looking up from",
         "who": f"{ROSIE_CUP} sits on the blanket pointing her striped straw at one small pink star; TORI sits "
                "right beside her pointing her green straw at a bright gold star next to it, their cups touching",
         "beats": [
             ("Then everybody picked a star to keep. Rosie picked the small pink one.",
              "medium close-up", "ROSIE points her striped straw up at the small pink star", "ROSIE",
              "sure and happy", "tilts up", "a soft blanket rustle"),
             ("Tori picked the gold one right beside it. \"To keep an eye on you.\"",
              "medium close-up", "TORI points her green straw at the gold star and leans her cup against ROSIE",
              ["TORI", "ROSIE"], "teasing and tender", "pushes in", "a soft clink of cups"),
         ]},
        {"title": "I brought my own", "place": "ridge_lights", "time": "night",
         "angle": "Medium view across the deck toward the wind-bent pine on",
         "who": "LINA stands on the log rail with both tiny arms spread to the whole sky; CAT the little blue "
                "penguin points one flipper at a streak of light shooting across the sky, beak open; GABBY floats "
                "between them with her fins wide, smiling with every tooth",
         "beats": [
             ("Lina picked all the tiny ones. \"Sugar,\" she said. Cat picked one. It shot away. \"Typical.\"",
              "medium shot", "CAT points at a streak of light and then drops her flipper while LINA spreads her arms",
              ["CAT", "LINA"], "greedy and unbothered", "pans right", "a tiny whoosh far away"),
             ("\"Which one is yours, Gabby?\" Gabby smiled with every tooth. \"I brought my own.\"",
              "medium close-up", "GABBY smiles her widest smile and tips her back toward the sky", "GABBY",
              "dry and delighted", "pushes in", "a soft swish of fins"),
         ]},
        {"title": "Midnight black", "place": "lane_night", "time": "night",
         "angle": "Upward view at the long lantern string above",
         "who": "MOM reaches up to a midnight-black paper lantern pricked with tiny holes that shine like little "
                "stars, steadying it on its hook; LINA stands on a snowy crate holding tiny round-tipped scissors, "
                "very pleased with herself; GABBY floats beside the lantern with her fins wide, its little lights "
                f"dotting her face; {ROSIE_CUP} stands on the crate beside LINA with one tiny arm pointing up, "
                "counting",
         "beats": [
             ("On the way home they hung the day's lantern. Midnight black, with tiny holes snipped by Lina.",
              "medium shot", "LINA holds up her tiny scissors and a white puff of sugar pops off her corners", "LINA",
              "pleased with herself", "tilts up", "a soft poof and a paper rustle"),
             ("Mom lit it. Out shone a sky of stars. Three in a row. A scoop. A wonky W.",
              "close-up", "MOM lets go of the lantern gently and tiny dots of light spill over the snow", "MOM",
              "calm and careful", "pushes in", "a tiny flicker and a soft paper rustle"),
             ("\"One more light,\" said Gabby. \"Forty-one, with the holes,\" said Rosie. She had counted.",
              "medium close-up", "GABBY floats closer to the lantern while ROSIE points at one tiny hole after another",
              ["GABBY", "ROSIE"], "proud and precise", "pulls back", "a soft swish of fins and a far sizzle"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably closed; "
                "CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, yellow scarf "
                "visible",
         "beats": [
             ("Goodnight, little sip, and your small pink star. Goodnight, Gabby, with the sky on your back.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, northern lights, rippling far. May your dreams be full of stars, and one of them yours.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, and your small pink star.",
        "Goodnight, Gabby, with the sky on your back.",
        "Goodnight, northern lights, rippling far.",
        "May your dreams be full of stars, and one of them yours.",
    ],
}
