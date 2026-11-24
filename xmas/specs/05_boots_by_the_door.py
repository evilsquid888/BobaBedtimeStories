"""05 — Boots by the Door (Saturday, December 5 · St. Nicholas Eve)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
COZY = "tiny pink knitted cup cozy"

BOOTROOM = {
    "name": "the boot room of Frostpeak Lodge",
    "scene": "the lodge boot room",
    "props": "a long row of snow boots under a wooden bench, pegs hung with mittens and scarves, a wicker basket "
             "of spare mittens, a rack of skis, a brass boot scraper shaped like a hedgehog, a half-open door "
             "onto a snowy porch",
    "light": "Pale afternoon sun falls through the half-open porch door",
    "accents": "tangerine orange and wool red",
    "atmo": "Little puffs of cold air curl in from the porch",
    "motion": "little puffs of cold air curl in from the porch",
}
BOOTROOM_NIGHT = dict(BOOTROOM, name="the lantern-lit boot room of Frostpeak Lodge", light="One small porch lantern glows over the row of boots at night")

STORY = {
    "num": "05",
    "slug": "boots-by-the-door",
    "title": "Boots by the Door",
    "meta": [
        ("Day", "Saturday, December 5"),
        ("Holiday thread", "St. Nicholas Eve: a boot left by the door tonight is found full in the morning"),
        ("Guests", "Teddy & Tilda Powderpuff ❄️, Nora Snowmane ❄️, Gabby the black star shark"),
        ("Cat’s role", "practical penguin: lends a snowboard boot that smells like fish, digs through the boot "
                       "pile for Gabby, and stuffs a sock into the mitten so it stands up"),
        ("Mandarin", "靴子 boot · 橘子 little orange · 驚喜 surprise"),
        ("Setting", "The great hall of Frostpeak Lodge, the lodge boot room and its snowy porch (afternoon, "
                    "then night), Lantern Lane at night, and the lodge bunk room"),
    ],
    "palette": "snowy cream and warm wood brown with saturated tangerine orange and wool red accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "TEDDY", "TILDA", "NORA", "GABBY"],
    "cast_note": "Humans in this story: none. Today Rosie and Tori each wear a tiny knitted cup cozy (Rosie's "
                 "pink, Tori's green) until they set them in the row of boots. Gabby swims through the air a "
                 "little above the floor; her boot is one big red mitten with a sock stuffed inside. Who left "
                 "the basket on the porch is never shown.",
    "key_shot": 12,
    "places": {
        "hall": DOORWALL,
        "boot": BOOTROOM,
        "boot_night": BOOTROOM_NIGHT,
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny brown boot and one spare red mitten on the nightstand"),
    },
    "shots": [
        {"title": "Door five", "place": "hall",
         "angle": "Low angle looking up the Door Wall in",
         "who": "GABBY floats high beside an open little door with her nose just touching it, a tiny brown boot "
                f"standing on a velvet shelf inside, looking at it with a small thoughtful smile; {ROSIE_CUP} "
                "stands on the rug below looking up, straw perked; NORA stands by the fireplace in her "
                "pale-blue shawl with a steaming cocoa mug",
         "beats": [
             ("Door five was up high. Gabby swam up and bumped it open with her nose.",
              "medium shot", "GABBY nudges the little door wider with her nose", "GABBY", "gentle and curious",
              "tilts up", "a tiny hinge creak and a crackling fire"),
             ("Inside stood one tiny **靴子** (xuēzi) = boot. Gabby looked at it for a long time.",
              "close-up", "GABBY tilts her head at the tiny boot and her tail slows", "GABBY",
              "thoughtful and quiet", "pushes in", "a crackling fire"),
             ("\"Tonight is Saint Nicholas Eve,\" said Nora the polar bear. \"Leave a boot by the door.\"",
              "medium shot", "NORA lifts her cocoa mug toward the little door and nods", "NORA",
              "calm and knowing", "pans right", "a crackling fire and a soft sip"),
         ]},
        {"title": "A long sip", "place": "hall",
         "angle": "Close view beside the crackling fireplace in",
         "who": "NORA sips from her steaming cocoa mug with a mysterious smile over the rim; TEDDY and TILDA "
                "lean in on either side of her with huge eyes and matching grins",
         "beats": [
             ("\"In the morning, look inside. That is all I am saying,\" said Nora.",
              "medium close-up", "NORA raises her mug and her eyes smile over the rim", "NORA",
              "mysterious and warm", "pushes in", "a crackling fire"),
             ("\"Who fills them?\" asked Teddy. \"With what?\" asked Tilda. Nora sipped her cocoa. It was a long sip.",
              "medium shot", "TEDDY and TILDA lean closer while NORA takes one very slow sip",
              ["TEDDY", "TILDA", "NORA"], "bursting with questions", "holds still", "one very long cocoa sip"),
         ]},
        {"title": "Forty-one boots", "place": "boot",
         "angle": "Wide low view down the long row of boots in",
         "who": f"{ROSIE_CUP} wearing a {COZY}, stands at the end of the row with a little picture list held in "
                "front of her cup, counting; CAT the little blue penguin drags a small snowboard boot into the "
                "row with both flippers, proud",
         "beats": [
             ("The boot room had more boots than Rosie could count. She counted anyway. Forty-one.",
              "wide shot", "ROSIE hops one step along the row, tapping her little picture list", "ROSIE",
              "busy and satisfied", "tracks beside", "tiny pencil taps and a drip of melting snow"),
             ("Cat the penguin added her snowboard boot. \"It smells like fish,\" said Cat. \"That's the good part.\"",
              "medium shot", "CAT shoves her boot into the row and pats it fondly", "CAT", "proud and cheeky",
              "pushes in", "a scrape of a boot and a happy pat"),
         ]},
        {"title": "The plan", "place": "boot",
         "angle": "Close view through the rack of skis in",
         "who": "TEDDY and TILDA crouch behind the skis with their pom-pom hats together, whispering behind "
                "their paws, eyes sparkling with mischief, two small boots set neatly in the row in front of them",
         "beats": [
             ("Teddy and Tilda set out two small boots. Then they hid behind the skis to whisper.",
              "medium shot", "TEDDY and TILDA duck lower behind the skis and bump their hats together",
              ["TEDDY", "TILDA"], "sneaky and thrilled", "pushes in", "a clatter of skis and a shh"),
             ("\"Tonight we stay awake—\" \"—and peek!\" \"We'll see who fills them—\" \"—with our own four eyes!\"",
              "close-up", "TEDDY and TILDA nod at each other faster and faster", ["TEDDY", "TILDA"],
              "plotting and gleeful", "holds still", "a clatter of skis and a rustle of wool"),
         ]},
        {"title": "Cups do not wear boots", "place": "boot",
         "angle": "High angle looking down at the row of boots in",
         "who": f"{ROSIE_CUP} stands at a gap in the row of boots setting down her {COZY} in the empty space, "
                "straw perked with a new idea",
         "beats": [
             ("Rosie looked down. Cups do not wear boots. She had nothing for the row.",
              "medium shot", "ROSIE looks down at her own tiny feet and then along the row", "ROSIE",
              "puzzled and thinking", "tilts down", "a drip of melting snow"),
             ("Then her straw popped up. She slipped off her tiny knitted cup cozy and set it down.",
              "medium close-up", "ROSIE sets her cozy snugly into the gap and pats it", "ROSIE",
              "clever and pleased", "pushes in", "a soft woolly pat"),
         ]},
        {"title": "A cozy and a slipper", "place": "boot",
         "angle": "Low view along the row of boots in",
         "who": "TORI sets a tiny green knitted cup cozy down beside a tiny pink one, green straw bobbing; MOM "
                "places one fuzzy slipper next to them with a small shrug and a smile",
         "beats": [
             ("\"Good thinking, little sip,\" said Tori. She put her own cozy right beside it.",
              "medium shot", "TORI sets her green cozy down next to the pink one", "TORI",
              "impressed and warm", "tracks beside", "a soft woolly pat"),
             ("Mom set out one fuzzy slipper. \"Saint Nicholas is not fussy,\" she said.",
              "medium close-up", "MOM places her slipper in the row and gives a little shrug", "MOM",
              "calm and amused", "holds still", "a soft fuzzy plop"),
         ]},
        {"title": "No feet", "place": "boot",
         "angle": "Wide view across the room toward the wicker basket in",
         "who": "GABBY floats beside the row of boots looking down at her own tail, her striped scarf drooping a "
                f"little; {ROSIE_CUP} stands by the row looking up at her, straw tilted; CAT the little blue "
                "penguin is half buried in a heap of odd boots with only her pink feet and tail sticking out",
         "beats": [
             ("Everybody had something in the row. Except Gabby. No feet. No boots. Not even a slipper.",
              "wide shot", "GABBY looks down at her own tail and gives it one small swish", "GABBY",
              "puzzled and a bit left out", "pushes in", "a hush of cold air"),
             ("\"Sharks don't really do boots,\" said Gabby. Her scarf drooped, just a little.",
              "medium shot", "GABBY's scarf droops as she drifts a little lower", "GABBY", "soft and wistful",
              "holds still", "a hush of cold air"),
             ("\"Then we'll find you one,\" said Rosie. Cat was already digging in the boot pile.",
              "medium shot", "ROSIE bounces on her toes while CAT's pink feet kick in the heap of boots",
              ["ROSIE", "CAT"], "determined and busy", "pans right", "a clatter of tumbling boots"),
         ]},
        {"title": "Clonk", "place": "boot",
         "angle": "Low angle along the floorboards of",
         "who": "GABBY lies flat on the floorboards with the tip of her tail stuck in one enormous heavy ski "
                "boot, fins spread, eyes wide in surprise; CAT the little blue penguin stands over her with both "
                "flippers on her cheeks",
         "beats": [
             ("First, a ski boot. Gabby put her tail in. Clonk. She sank straight to the floor.",
              "medium shot", "GABBY tugs at the heavy ski boot with her tail and stays flat on the floor", "GABBY",
              "surprised and stuck", "tilts down", "one heavy clonk on floorboards"),
         ]},
        {"title": "Hello?", "place": "boot",
         "angle": "Close view up at one tall yellow rubber boot in",
         "who": "GABBY has vanished tail-first into a tall yellow rubber boot with only her eyes, her nose and "
                f"two fin tips poking out of the top; {ROSIE_CUP} stands beside the boot looking up, straw "
                "wiggling with giggles",
         "beats": [
             ("Next, a rubber boot. It swallowed her up to the fins. \"Hello?\" said the boot.",
              "medium close-up", "GABBY peeks over the rim of the rubber boot and blinks", "GABBY",
              "muffled and amused", "tilts up", "a rubbery squeak and a tiny echo"),
         ]},
        {"title": "A boot for a fin", "place": "boot",
         "angle": "Medium view beside the wicker basket of spare mittens in",
         "who": f"{ROSIE_CUP} holds one big red knitted mitten up in front of her cup, straw popped up, eyes "
                "bright; CAT the "
                "little blue penguin pokes a rolled-up sock into the mitten with one flipper, tongue out in "
                "concentration",
         "beats": [
             ("Then Rosie spotted the spare basket. A big red mitten! \"A mitten is a boot for a hand.\"",
              "medium shot", "ROSIE lifts the big red mitten up high in front of her cup", "ROSIE",
              "bright and determined", "pushes in", "a rustle of wool in a basket"),
             ("\"And a fin is nearly a hand,\" said Cat. She stuffed in a sock so it stood up.",
              "medium close-up", "CAT pushes the sock down into the mitten and it stands up straight", "CAT",
              "practical and proud", "tilts down", "a soft stuffing squish"),
         ]},
        {"title": "I have a boot", "place": "boot",
         "angle": "Upward view from the floorboards in",
         "who": "GABBY floats in a happy curve with the big red mitten on the tip of her tail, smiling her "
                f"widest smile with every tiny tooth showing; {ROSIE_CUP} stands below her with her straw "
                "wiggling high",
         "beats": [
             ("Rosie held it up high. \"Gabby. This one is yours.\"",
              "medium shot", "ROSIE bounces on her toes and looks up at GABBY", ["ROSIE", "GABBY"],
              "shy and hopeful", "tilts up", "a tiny hop on floorboards"),
             ("Gabby tried it on her tail. It fit! Sort of. She smiled her widest smile, all teeth.",
              "medium close-up", "GABBY wags the mitten on her tail and her smile spreads wide", "GABBY",
              "surprised and overjoyed", "pushes in", "a soft woolly flap"),
             ("\"I have a boot,\" she told everyone. Then she told everyone again.",
              "medium shot", "GABBY swims a happy loop with the mitten held high on her tail", "GABBY",
              "proud and giddy", "pans left", "a soft whoosh of air"),
         ]},
        {"title": "The orange lantern", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the lantern string over",
         "who": "GABBY floats up at the string holding the loop of a round orange paper lantern gently in her "
                "smile, beside a red, a purple, a green and a blue lantern; CAT the little blue penguin looks up "
                f"from the snow with both flippers on her hips; {ROSIE_CUP} stands beside her with her straw tall",
         "beats": [
             ("At dusk the orange lantern went up, round as a **橘子** (júzi) = little orange.",
              "wide shot", "GABBY rises slowly toward the string with the orange lantern", "GABBY",
              "careful and proud", "tilts up", "a paper rustle and a hush of snow"),
             ("Gabby swam it up to the string herself. No ladder. \"Who needs boots?\" said Cat.",
              "medium shot", "CAT throws both flippers wide and looks up at the lantern", "CAT",
              "impressed and cheeky", "pushes in", "a tiny brass click"),
             ("\"One more light,\" said Gabby, softly, around the string.",
              "close-up", "GABBY lets go of the loop and the orange lantern glows on her smile", "GABBY",
              "quietly glad", "holds still", "a soft paper flutter"),
         ]},
        {"title": "Bed", "place": "boot_night", "time": "night",
         "angle": "Medium view from the porch door at night into",
         "who": "MOM stands by the row of boots pointing one tiny arm toward the stairs with a firm kind smile; "
                "TEDDY and TILDA stretch in two enormous pretend yawns behind her, each with one eye open; TORI "
                "waits on the bottom stair with a folded quilt over one tiny arm, green straw drooping sleepily",
         "beats": [
             ("\"Bed,\" said Mom. \"**驚喜** (jīngxǐ) = surprise! It comes faster when you sleep.\" Everybody went. Almost everybody.",
              "medium shot", "MOM points toward the stairs while TEDDY and TILDA stretch in huge pretend yawns",
              ["MOM", "TEDDY", "TILDA"], "firm and suspiciously sleepy", "pans right",
              "a creak of stairs and a soft slipper shuffle"),
         ]},
        {"title": "Four eyes", "place": "boot_night", "time": "night",
         "angle": "Close view through the rack of skis at night in",
         "who": "TEDDY and TILDA hide behind the skis under a big heap of striped scarves with only their "
                "noses, their wide open eyes and their pom-pom hats poking out",
         "beats": [
             ("Behind the skis sat a pile of scarves. The pile of scarves had four eyes. It giggled.",
              "medium close-up", "TEDDY and TILDA blink at the same time and the heap of scarves shakes",
              ["TEDDY", "TILDA"], "watchful and giggly", "pushes in", "a rustle of scarves and a hush of snow"),
             ("They waited. Nobody came. They waited some more. Only the snow came.",
              "medium shot", "TEDDY yawns for real and TILDA nudges him with her elbow", ["TEDDY", "TILDA"],
              "bored and drowsy", "holds still", "a soft rustle of scarves"),
         ]},
        {"title": "The basket", "place": "boot_night", "time": "night",
         "angle": "Low angle through the half-open porch door at night from",
         "who": "a big basket heaped with little oranges and walnuts sits on the snowy porch step under the "
                "porch lantern, big soft footprints leading away and filling with snow; TEDDY and TILDA peek "
                "around the door at it with round eyes",
         "beats": [
             ("Then Teddy looked at the porch. There sat a big basket of little oranges and walnuts.",
              "medium shot", "TEDDY points one paw at the basket and his mouth drops open", "TEDDY",
              "astonished and thrilled", "pushes in", "a creak of the porch door and a hush of snow"),
             ("Nobody was there. Only footprints, already filling with snow. \"We missed it—\" \"—by one yawn!\"",
              "medium close-up", "TILDA leans out to look at the snowy footprints and claps a paw to her hat",
              "TILDA", "amazed and dismayed", "tilts down", "a hush of falling snow"),
         ]},
        {"title": "Tiptoe", "place": "boot_night", "time": "night",
         "angle": "Low view along the row of boots at night in",
         "who": "TEDDY tiptoes along the row with his arms full of little oranges; TILDA tiptoes behind him "
                "dropping a walnut into a boot; a tiny pink knitted cup cozy, a tiny green one, a fuzzy slipper "
                "and a big red mitten stand in the row among the boots",
         "beats": [
             ("\"A basket can't fill boots by itself,\" whispered Tilda. \"Somebody should help,\" whispered Teddy.",
              "medium shot", "TEDDY and TILDA look at each other and nod very slowly", ["TEDDY", "TILDA"],
              "noble and delighted", "pushes in", "a rattle of walnuts and a hush of snow"),
             ("So they tiptoed down the row. An orange here. Two walnuts there. Shhh. Giggle. Shhh.",
              "medium shot", "TEDDY lowers an orange into a boot while TILDA drops in a walnut", ["TEDDY", "TILDA"],
              "careful and giggly", "tracks beside", "soft tiptoe steps and a walnut rattle"),
             ("Rosie's cozy fit exactly one walnut. Gabby's mitten got the biggest orange of all.",
              "close-up", "TILDA settles one walnut into the tiny pink cozy with both paws", "TILDA",
              "tender and proud", "pushes in", "one tiny walnut tap"),
         ]},
        {"title": "Worth it", "place": "boot_night", "time": "night",
         "angle": "Wide view from the row of full boots at night toward the inner doorway of",
         "who": "NORA stands in the doorway in her pale-blue shawl with her steaming cocoa mug, one eyebrow "
                "raised and a smile underneath; TEDDY and TILDA stand frozen in mid-tiptoe with empty paws and "
                "enormous guilty grins",
         "beats": [
             ("A big white shape filled the doorway. It was Nora, with her cocoa.",
              "wide shot", "NORA raises one eyebrow and takes a slow sip from her mug", "NORA",
              "calm and amused", "pushes in", "a floorboard creak and a slow sip"),
             ("\"We didn't mean to—\" said Teddy. \"—but it was worth it,\" said Tilda.",
              "medium shot", "TEDDY and TILDA hold up their empty paws and grin", ["TEDDY", "TILDA"],
              "caught and glowing", "pans left", "a shuffle of paws on floorboards"),
             ("Nora looked at the full boots. She looked at the cubs. \"Sit. Cocoa first. Then bed.\"",
              "medium close-up", "NORA holds out her cocoa mug and nods toward the bench", "NORA",
              "fond and proud", "holds still", "a soft slosh of cocoa"),
         ]},
        {"title": "Oranges", "place": "boot_night", "time": "night",
         "angle": "Warm close view at night along the wooden bench of",
         "who": "NORA sits on the bench with TEDDY and TILDA leaning against her on either side, each cub holding "
                "a little mug of cocoa with drooping eyelids; the row of boots in front of them brims with little "
                "oranges and walnuts, snow falling past the porch door",
         "beats": [
             ("Outside, the snow came down, soft and thick. Inside, the whole room smelled of oranges.",
              "medium shot", "TEDDY and TILDA lean heavier against NORA and their eyelids droop",
              ["TEDDY", "TILDA", "NORA"], "cozy and drowsy", "pulls back", "a hush of falling snow and a soft sip"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep on a soft pillow at the foot of the bunk with one "
                "sock on her flipper, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, your cozy by the door. Goodnight, Gabby, with a boot of your own.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, twins, quiet at last. May you wake to oranges and a little bit of wonder.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, your cozy by the door.",
        "Goodnight, Gabby, with a boot of your own.",
        "Goodnight, twins, quiet at last.",
        "May you wake to oranges and a little bit of wonder.",
    ],
}
