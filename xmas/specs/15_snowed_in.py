"""15 — Snowed In. A blizzard cancels the sleigh ride, so it becomes the best indoor day ever: one enormous blanket fort."""
from places import DOORWALL, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
POLE = "sits bolt upright in the middle of the fort with the quilt roof draped over his head like a hood"

# The Door Wall as always, on a blizzard morning: the tall windows are packed white.
HALL_BLIZZARD = dict(DOORWALL, atmo="Firelight flickers and thick snow whirls white against the tall windows")

STORY = {
    "num": "15",
    "slug": "snowed-in",
    "title": "Snowed In",
    "meta": [
        ("Day", "Tuesday, December 15 · door fifteen"),
        ("Holiday thread", "A blizzard day indoors: cocoa, the biggest blanket fort in Frostpeak, and a shadow show"),
        ("Guests", "Nora Snowmane ❄️, Magnus Meltsworth ❄️, Kyle the black bear cub, Lina the snowflake crisp"),
        ("Cat’s role", "blizzard-day guide: knows the lodge library has the best fire, pins the fort corners "
                       "with gentle kung fu, and test-rides the drawbridge"),
        ("Mandarin", "毯子 blanket · 暴風雪 blizzard · 可可 cocoa"),
        ("Setting", "Frostpeak Lodge in a blizzard: the Door Wall, the fireside library, and a blanket fort "
                    "after dark; the bunk room at night"),
    ],
    "palette": "warm cream and firelit amber with saturated ember orange and quilt blue accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "NORA", "MAGNUS", "KYLE", "LINA"],
    "cast_note": "Humans in this story: none. Today's lantern (soft grey with a white swirl) is hung indoors, "
                 "inside the blanket fort; it is a paper lantern with a small lamp inside, and Magnus holds it.",
    "key_shot": 11,
    "places": {
        "hall": HALL_BLIZZARD,
        "library": {
            "name": "the fireside library of Frostpeak Lodge in a blizzard",
            "scene": "the fireside lodge library",
            "props": "tall shelves of old books with a rolling ladder, a wide stone fireplace, squashy armchairs, "
                     "an old globe, a window seat under a tall window packed white with snow, a big basket of "
                     "knitted blankets",
            "light": "A crackling fire glows gold while the tall window shows only whirling white",
            "accents": "ember orange and book-cloth green",
            "atmo": "Snow whirls thick against the window glass",
            "motion": "snow whirls thick against the window glass",
        },
        "fort": {
            "name": "the blanket fort in the lodge library at night",
            "scene": "inside the blanket fort",
            "props": "a roof of patchwork quilts held up with clothespins, walls of sofa cushions, a nest of "
                     "pillows, a soft grey paper lantern with a white swirl, a tray of cocoa mugs, a doorstep "
                     "made of old books",
            "light": "One soft grey paper lantern glows inside the fort at night",
            "accents": "ember orange and quilt blue",
            "atmo": "Lantern light sways on the blanket walls",
            "motion": "lantern light sways on the blanket walls",
        },
        "bunk": bunk("a tiny folded blanket and a cocoa mug with one marshmallow on the nightstand"),
    },
    "shots": [
        {"title": "Door fifteen", "place": "hall",
         "angle": "Low angle looking up the tall wall of little carved doors in",
         "who": f"{ROSIE_CUP} stands by a little open door carved with a plain folded blanket, holding a tiny "
                "folded blanket in front of her cup with a puzzled tilt of her straw, a little picture list "
                "tucked under one tiny arm; CAT the little blue penguin stands on a stool with her beak pressed "
                "to a tall window that is solid white",
         "beats": [
             ("Rosie opened door fifteen. Inside was a tiny folded **毯子** (tǎnzi) = blanket, small as a stamp.",
              "close-up", "ROSIE lifts the tiny folded blanket in front of her cup and tilts her straw", "ROSIE",
              "puzzled and curious", "pushes in", "a soft wooden click and a fire crackle"),
             ("\"A blanket?\" Rosie checked her list. Today said sleigh ride, underlined three times.",
              "medium shot", "ROSIE pulls out her picture list and looks from the blanket to the list", "ROSIE",
              "confused and still hopeful", "tilts down", "a paper rustle"),
             ("Cat the penguin looked out the window. \"Hm,\" she said. \"Somebody took the outside.\"",
              "medium close-up", "CAT presses her beak to the white window and taps the glass with one flipper",
              "CAT", "baffled and matter-of-fact", "pans right", "a tap on glass and a long moan of wind"),
         ]},
        {"title": "Blizzard", "place": "hall",
         "angle": "Wide view along the long woven rug toward the tall white windows of",
         "who": "MOM stands beside the tall window that shows only whirling white, turning back with a gentle "
                f"smile; {ROSIE_CUP} stands on the rug holding her little picture list in front of her cup, "
                "straw drooping all the way down to her lid",
         "beats": [
             ("The window was all white. Whoooo, went the wind. It was a **暴風雪** (bàofēngxuě) = blizzard.",
              "wide shot", "MOM looks out at the whirling white and slowly shakes her head", "MOM",
              "calm and watchful", "pushes in", "a long moan of wind and rattling panes"),
             ("\"The sleigh can't go out in this,\" said Mom. \"We're snowed in, little one.\"",
              "medium shot", "MOM turns from the window and bends toward the rug with a soft smile", "MOM",
              "gentle and cheerful", "tilts down", "a moan of wind and a fire crackle"),
             ("Rosie crossed out sleigh ride. Her pencil squeaked. Her straw drooped right down to her lid.",
              "medium close-up", "ROSIE scribbles on her list and her straw sinks down to her lid", "ROSIE",
              "deflated", "pushes in", "one long pencil squeak"),
         ]},
        {"title": "Cocoa first", "place": "library",
         "angle": "Wide establishing view through the open doorway into",
         "who": "CAT the little blue penguin holds the heavy door open with her back and sweeps one flipper "
                "toward the fire like a tour guide; NORA sits in the biggest armchair by the fireplace stirring "
                f"a big copper pot of cocoa with a calm smile; {ROSIE_CUP} stands in the doorway looking up at a "
                "mug topped with one enormous marshmallow, straw lifting",
         "beats": [
             ("\"Blizzard day?\" said Cat. \"Follow me. The library. Best fire. Squashiest chairs.\"",
              "wide shot", "CAT leans on the door and sweeps one flipper toward the fireplace", "CAT",
              "sure and welcoming", "pushes in", "a door creak and a crackling fire"),
             ("By the fire sat Nora the polar bear with a big copper pot. \"Sit. Cocoa first. Then feelings.\"",
              "medium shot", "NORA taps her wooden spoon on the pot and nods at an empty chair", "NORA",
              "calm and kind", "tilts down", "a spoon tap on copper and a soft bubbling"),
             ("The **可可** (kěkě) = cocoa came with a marshmallow as big as Rosie's lid. Her straw perked up.",
              "medium close-up", "ROSIE gazes up at the enormous marshmallow and her straw springs up", "ROSIE",
              "cheered and impressed", "tilts up", "a soft plop and a curl of steam hissing"),
         ]},
        {"title": "A hobby", "place": "library",
         "angle": "Low angle at hearth level beside a row of mugs in",
         "who": "KYLE sits by the hearth with a ring of marshmallow fluff on his tan muzzle and an empty "
                "marshmallow bowl in his lap, one paw raised with a serious look on his face; CAT the little "
                "blue penguin stands beside him with one flipper on her hip",
         "beats": [
             ("Kyle the bear cub had marshmallow on his nose. \"I was just taste-testing. All of them.\"",
              "medium shot", "KYLE licks the fluff on his muzzle and tips the empty bowl to show it", "KYLE",
              "caught and cheerful", "pushes in", "a lip smack and a hollow bowl tap"),
             ("\"My feeling is hungry,\" he added. \"For you, that's a hobby,\" said Cat.",
              "medium close-up", "KYLE raises one paw while CAT shakes her head with a grin", ["KYLE", "CAT"],
              "earnest and teasing", "pans left", "a tummy rumble and a tiny foot tap"),
         ]},
        {"title": "Lists have a back", "place": "library",
         "angle": "Close view over a tall green straw down at the window seat of",
         "who": "TORI holds the crossed-out picture list flipped to its clean blank side with a grin; "
                f"{ROSIE_CUP} stands on the window seat with the tiny folded blanket in front of her cup, "
                "looking from the blanket to the blank page, straw beginning to wiggle",
         "beats": [
             ("Tori turned Rosie's list over. \"Lists have a back, little sip.\"",
              "medium close-up", "TORI flips the list to its clean side and holds it out", "TORI",
              "bright and playful", "pushes in", "a paper flip"),
             ("Rosie looked at the tiny blanket from the door. Her straw wiggled. One: build a fort.",
              "close-up", "ROSIE looks at the tiny blanket and her straw wiggles fast", "ROSIE",
              "sparked and eager", "tilts up", "a pencil scratch on paper"),
             ("Two: make it the biggest fort in Frostpeak. She underlined that four times.",
              "close-up", "ROSIE draws on the clean page with big sweeping strokes and bounces once", "ROSIE",
              "gleeful and busy", "holds still", "four quick pencil strokes"),
         ]},
        {"title": "A sofa with feet", "place": "library",
         "angle": "Wide busy view across the rug between the armchairs of",
         "who": "KYLE staggers under a towering heap of sofa cushions so that only his paws and the pom-pom of "
                "his red beanie show; MOM carries a tall folded stack of patchwork quilts with a smile; CAT the "
                "little blue penguin chops a clothespin onto a blanket corner with one flipper in a gentle kung "
                "fu pose; LINA stands on top of a draped quilt puffing white sugar across it",
         "beats": [
             ("Kyle carried every cushion in the lodge at once. He was a sofa with feet.",
              "wide shot", "KYLE wobbles two steps under the towering heap of cushions", "KYLE",
              "strong and wobbly", "tracks beside", "soft thumps and a muffled grunt"),
             ("Mom brought quilts. Cat pinned the corners with gentle kung fu. Hi-ya. Hi-ya. Tuck.",
              "medium shot", "CAT chops a clothespin onto the blanket corner while MOM shakes out a quilt",
              ["CAT", "MOM"], "brisk and playful", "pans right", "two clothespin snaps and a quilt flap"),
             ("Lina sugared the roof. Poof! \"Now it's a snow fort. No two alike!\"",
              "medium close-up", "LINA hops on the quilt and a white puff of sugar settles over it", "LINA",
              "pleased with herself", "tilts up", "one soft poof"),
         ]},
        {"title": "The drawbridge", "place": "library",
         "angle": "Dynamic diagonal view along the tall bookshelves of",
         "who": "CAT the little blue penguin rides the rolling ladder along the bookshelves with one flipper "
                "pointing ahead and her yellow scarf streaming, beak wide with glee, the big basket of knitted "
                "blankets waiting at the end of the rail",
         "beats": [
             ("The rolling ladder became a drawbridge. Cat tested it. Wheeee! Whump.",
              "wide shot", "CAT whizzes along the shelves on the rolling ladder with one flipper out", "CAT",
              "fearless and gleeful", "pans right", "a long rattle of little wheels and one soft whump"),
             ("\"It works,\" said Cat, from inside the blanket basket.",
              "medium close-up", "CAT pops her head up out of the blanket basket with a sock on her beak", "CAT",
              "dizzy and satisfied", "pushes in", "a woolly rustle"),
         ]},
        {"title": "A sad pancake", "place": "library",
         "angle": "Low angle from the rug looking up at the drooping quilt roof in",
         "who": f"{ROSIE_CUP} stands under a patchwork quilt roof that sags in the middle almost down to her "
                "straw, looking up at it with a thoughtful frown; LINA slides slowly down the dip of the quilt "
                "with her tiny arms out",
         "beats": [
             ("But the roof sagged in the middle like a sad pancake. It needed a pole. A tall one.",
              "medium shot", "LINA slides down the sagging quilt as ROSIE looks up at the dip", ["LINA", "ROSIE"],
              "stumped and thinking", "tilts up", "a slow slither of cloth"),
         ]},
        {"title": "Nobody had asked yet", "place": "library",
         "angle": "Medium view across the old globe toward the far corner armchair in",
         "who": "MAGNUS sits deep in the corner armchair hidden behind a big open book with a plain picture of "
                "a snowy mountain on its cover, only his bushy frowning eyebrows and grey ears showing above "
                "it, his ancient wooden skis propped beside him",
         "beats": [
             ("In the corner sat Magnus, behind a book about how snow was better in the old days.",
              "medium shot", "MAGNUS turns one page slowly and his eyebrows twitch above the book", "MAGNUS",
              "gruff and hiding", "pushes in", "a slow page turn and a fire crackle"),
             ("Everybody turned to look at him. \"No,\" said Magnus. Nobody had asked yet.",
              "medium close-up", "MAGNUS sinks lower behind his book until only his eyebrows show", "MAGNUS",
              "cornered and grumpy", "holds still", "an armchair creak"),
         ]},
        {"title": "One noble act", "place": "library",
         "angle": "Low angle from the rug looking up past a small pink cup at",
         "who": f"{ROSIE_CUP} stands in front of the corner armchair holding the tiny folded blanket in front of "
                "her cup, straw up straight, eyes big and hopeful; MAGNUS lowers his big book to his lap and "
                "looks down at her over it with a long-suffering frown and soft eyes",
         "beats": [
             ("So Rosie asked. Nicely. With her straw up. Magnus sighed like an old accordion.",
              "medium shot", "ROSIE holds up the tiny blanket and MAGNUS lowers his book with a heavy sigh",
              ["ROSIE", "MAGNUS"], "hopeful and worn down", "tilts up", "one long wheezy creak of an armchair"),
             ("\"Fine,\" he grumbled. \"But this is my one noble act for the week.\"",
              "medium close-up", "MAGNUS closes his book with a thump and heaves himself up from the chair",
              "MAGNUS", "grumbling and quietly pleased", "tilts up", "a book thump and an armchair creak"),
         ]},
        {"title": "The pole had eyebrows", "place": "fort", "time": "night",
         "angle": "Wide cozy view from the book doorstep into",
         "who": f"MAGNUS {POLE}, bushy eyebrows frowning out from under it, one paw raised and holding up the "
                f"glowing grey paper lantern; {ROSIE_CUP} sits on a pillow below looking up at the lantern with "
                "her straw high; KYLE and LINA nestle in the pillows with cocoa mugs",
         "beats": [
             ("By dark, the fort had a fine tall pole in the middle. The pole had eyebrows.",
              "wide shot", "MAGNUS frowns out from under the quilt roof and his eyebrows twitch", "MAGNUS",
              "dignified and trapped", "pushes in", "a muffled moan of wind and a soft quilt rustle"),
             ("They hung lantern fifteen from his paw. Soft grey with a white swirl, like the blizzard.",
              "medium shot", "MAGNUS lifts the grey lantern higher on one paw and its glow fills the fort",
              "MAGNUS", "patient and stiff", "tilts up", "a soft paper rustle"),
             ("\"One more light,\" whispered Rosie. \"I'm holding it,\" said Magnus. \"That's two noble acts.\"",
              "medium close-up", "ROSIE gazes up at the lantern and her straw wiggles", "ROSIE",
              "hushed and happy", "pulls back", "a soft paper rustle and a muffled moan of wind"),
         ]},
        {"title": "That is my paw", "place": "fort", "time": "night",
         "angle": "Medium view toward the glowing blanket wall inside",
         "who": f"MAGNUS {POLE}, holding the grey lantern in one paw while the shadow of his other paw falls on "
                "the blanket wall in the shape of a rabbit with two long ears; LINA points up at the shadow "
                "with both tiny arms; KYLE gazes at it with his mouth open",
         "beats": [
             ("The lantern threw his other paw onto the blanket wall. \"A rabbit!\" gasped Lina.",
              "medium shot", "LINA points up as the rabbit shadow wiggles its ears on the blanket wall", "LINA",
              "thrilled and loud", "pans right", "a soft quilt rustle and a pillow thump"),
             ("\"That is my paw,\" said Magnus. \"Tell us about the rabbit,\" said Kyle.",
              "medium close-up", "MAGNUS glares at his own paw while KYLE scoots closer on the pillows",
              ["MAGNUS", "KYLE"], "stubborn and eager", "pushes in", "a pillow shuffle"),
             ("Magnus sighed. \"Once there was a rabbit. He wanted to be left alone to read.\"",
              "medium shot", "MAGNUS bends two claws and the shadow rabbit bows its long ears", "MAGNUS",
              "reluctant and rather good at it", "tilts up", "a long slow creak of a quilt"),
         ]},
        {"title": "And the rabbit stayed", "place": "fort", "time": "night",
         "angle": "Low angle from the pillow nest looking up at",
         "who": "KYLE sits squarely on one big white foot of MAGNUS, looking down at it in surprise with his "
                f"cocoa mug in both paws; MAGNUS {POLE}, looking down at the cub with one eyebrow up and the "
                "smallest hint of a smile, the grey lantern glowing in his raised paw",
         "beats": [
             ("\"Then what?\" \"Then a bear cub sat on his foot.\" Kyle looked down. He was on Magnus's foot.",
              "medium shot", "KYLE looks down slowly at the big white foot under him and freezes", "KYLE",
              "caught and giggly", "tilts down", "a soft quilt rustle and a mug clink"),
             ("\"And the rabbit stayed,\" grumbled Magnus. \"It was warm in there. Tell no one.\"",
              "medium close-up", "MAGNUS raises one eyebrow and the corner of his mouth lifts", "MAGNUS",
              "gruff and soft underneath", "pushes in", "a low rumble and a soft paper rustle"),
         ]},
        {"title": "The shadow show", "place": "fort", "time": "night",
         "angle": "Wide view of the whole glowing blanket wall inside",
         "who": "CAT the little blue penguin holds a kung fu pose on one foot in front of the grey lantern, her "
                "big shadow kicking across the blanket wall; KYLE stands beside her with both paws up, his "
                "round shadow next to hers; LINA stands close to the lantern casting one big square shadow; "
                f"{ROSIE_CUP} stands on a pillow, her shadow stretching up the wall with a very tall straw",
         "beats": [
             ("Then everybody wanted a turn. Cat's shadow did kung fu. Kyle's shadow was a bear. \"I practiced.\"",
              "wide shot", "CAT kicks one foot out and KYLE lifts both paws as their shadows move on the wall",
              ["CAT", "KYLE"], "showy and proud", "pans left", "a swish of a kick and a pillow thump"),
             ("Lina's shadow was a square. \"It's a snowflake,\" said Lina. \"Very close up.\"",
              "medium shot", "LINA spreads her tiny arms and her big square shadow does the same", "LINA",
              "serene and certain", "pushes in", "a tiny poof"),
             ("Rosie's shadow had the tallest straw in the world. It tickled the lantern.",
              "medium shot", "ROSIE wiggles her straw and its long shadow waves up the blanket wall", "ROSIE",
              "giggly and amazed", "tilts up", "a soft paper rustle"),
         ]},
        {"title": "Sleighs can wait", "place": "fort", "time": "night",
         "angle": "Close cozy view across the tray of cocoa mugs inside",
         "who": f"{ROSIE_CUP} sits in the pillow nest holding her new picture list in front of her cup, three "
                "little doodles of a fort, a mug and a rabbit each ticked with a heart; TORI leans beside her "
                "with a cocoa mug; CAT the little blue penguin lies on her back on a cushion with her feet in "
                "the air",
         "beats": [
             ("Outside, the wind went whoooo. Inside it smelled of cocoa, wool and warm bear.",
              "medium shot", "TORI takes a slow sip of cocoa and leans back into the pillows", "TORI",
              "snug and unbothered", "pushes in", "a muffled moan of wind and a slow sip"),
             ("Rosie ticked her new list. Fort. Cocoa. Rabbit. \"And the sleigh?\" said Tori.",
              "close-up", "ROSIE taps each little doodle on her list while TORI leans in to look",
              ["ROSIE", "TORI"], "proud and curious", "tilts down", "three soft pencil taps"),
             ("\"It can wait,\" said Cat. \"Sleighs are terrible at running away.\"",
              "medium close-up", "CAT waves one flipper lazily from her cushion with her feet in the air", "CAT",
              "relaxed and wise", "pans left", "a lazy flipper flap"),
         ]},
        {"title": "The best fort in Frostpeak", "place": "fort", "time": "night",
         "angle": "Upward view from the pillow nest in soft lantern glow inside",
         "who": f"MAGNUS {POLE}, eyes closed and asleep sitting up, his raised paw still holding the grey "
                f"lantern; MOM tucks one big knitted blanket over the cushions below him; {ROSIE_CUP} sits snug "
                "in the pillows with the blanket up to her lid, straw wiggling gently",
         "beats": [
             ("Mom tucked one last blanket round everybody. Then the tall pole began to snore, sitting up.",
              "medium shot", "MOM smooths the blanket down as MAGNUS nods with his eyes closed", ["MOM", "MAGNUS"],
              "tender and amused", "tilts up", "a blanket pat and one long rumbling snore"),
             ("Nobody moved. It was the best fort in Frostpeak. Rosie had underlined it.",
              "close-up", "ROSIE snuggles down in the blanket and her straw gives a slow happy wiggle", "ROSIE",
              "snug and content", "pulls back", "a muffled moan of wind and a soft snore"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep curled on a soft pillow at the foot of the bed, "
                "yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, with a brand-new list. Goodnight, Magnus, the grumpiest tent pole.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, blizzard, blow yourself sleepy. May your snowed-in days be the coziest days of all.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, with a brand-new list.",
        "Goodnight, Magnus, the grumpiest tent pole.",
        "Goodnight, blizzard, blow yourself sleepy.",
        "May your snowed-in days be the coziest days of all.",
    ],
}
