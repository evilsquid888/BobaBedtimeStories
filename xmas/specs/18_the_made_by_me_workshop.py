"""18 — The Made-by-Me Workshop. Market Train to Quebec City: no coins, one walnut, and a wood-carving chalet."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
REST = "a little pine straw-rest, a small smooth block of pale wood with a dip in its top,"

STORY = {
    "num": "18",
    "slug": "the-made-by-me-workshop",
    "title": "The Made-by-Me Workshop",
    "meta": [
        ("Day", "Friday, December 18 · door eighteen · Market Train to Quebec City"),
        ("Holiday thread", "Making presents at the Christmas market in Old Quebec City"),
        ("Guests", "Magnus Meltsworth ❄️ (came for the wood), Harfang the snowy owl ⚜️ (guide), "
                   "Margot the maple taffy ⚜️ (holds the wrapping paper)"),
        ("Cat’s role", "lookout: blocks the chalet door with a hip-hop routine so the surprise stays a surprise"),
        ("Mandarin", "禮物 present · 慢慢來 take it slow"),
        ("French", "marché de Noël Christmas market · merci thank you"),
        ("Setting", "The Door Wall, then by Market Train to the Christmas market in Old Quebec City and the "
                    "wood-carving chalet; Lantern Lane and the bunk room at night"),
    ],
    "palette": "warm pine and cream with saturated pine green and paint-pot blue accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "MAGNUS", "HARFANG", "MARGOT"],
    "cast_note": "Humans in this story: none. The present is a little pine straw-rest for Tori's tall straw, "
                 "painted with blue waves; it is wrapped today and given on the 24th (a surprise). Tickets, "
                 "stalls and awnings show plain little pictures only.",
    "key_shot": 11,
    "places": {
        "hall": DOORWALL,
        "market": {
            "name": "the Christmas market in Old Quebec City",
            "scene": "the Old Quebec Christmas market",
            "props": "rows of little wooden chalets hung with fir garlands, a stall of glass birds, a stall of "
                     "painted music boxes, a tall fir tree in the square, strings of glass bulbs, the snowy "
                     "stone walls and steep copper roofs of the old town",
            "light": "Bright winter sun sparkles on the snowy stone square",
            "accents": "holly red and copper green",
            "atmo": "Soft snowflakes drift between the chalets",
            "motion": "soft snowflakes drift between the chalets",
        },
        "chalet": {
            "name": "the wood-carving chalet at the Christmas market in Old Quebec City",
            "scene": "the wood-carving chalet",
            "props": "a little wooden chalet with a plank door and a frosted round window, a scarred carving "
                     "bench with a vise, curls of pine shavings all over the floor, half-carved wooden animals "
                     "on a shelf, jam jars of paint and brushes, loops of ribbon hanging from the rafters",
            "light": "Golden afternoon sun slants in through the frosted round window",
            "accents": "pine green and paint-pot blue",
            "atmo": "Sawdust sparkles drift in the sunbeams",
            "motion": "sawdust sparkles drift in the sunbeams",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny carved wooden cup with a straw and a tiny spool of red ribbon on the nightstand"),
    },
    "shots": [
        {"title": "Door eighteen", "place": "hall",
         "angle": "Low angle looking up the tall wall of little carved doors in",
         "who": f"{ROSIE_CUP} stands by a little open door holding a tiny spool of red ribbon and a tiny golden "
                "train ticket in front of her cup, a little picture list tucked under one tiny arm, straw "
                "tilted; CAT the little blue penguin hops beside her with both flippers up",
         "beats": [
             ("Rosie opened door eighteen. Out rolled a spool of red ribbon and a golden train ticket.",
              "close-up", "ROSIE catches the tiny spool of ribbon in front of her cup and blinks at the ticket",
              "ROSIE", "surprised and pleased", "pushes in", "a soft wooden click and a tiny rolling rattle"),
             ("\"Ribbon is for a **禮物** (lǐwù) = present,\" said Rosie. She checked her list. Tori: blank.",
              "medium shot", "ROSIE pulls out her picture list and her straw tilts at an empty space on it",
              "ROSIE", "thoughtful and a little stuck", "tilts down", "a paper rustle and a fire crackle"),
             ("\"Quebec City!\" said Cat the penguin. \"The Christmas market! Bring your coins.\"",
              "medium close-up", "CAT hops with both flippers up and points at the golden ticket", "CAT",
              "thrilled and sure", "pans right", "a bouncing penguin patter"),
         ]},
        {"title": "One walnut", "place": "hall",
         "angle": "Close view at rug height beside the crackling fireplace in",
         "who": f"{ROSIE_CUP} stands over a tiny upturned coin purse with one button, a tuft of fluff and one "
                "walnut on the rug in front of her, straw sagging; MOM bends down close beside her with one "
                "tiny arm at the side of her lid, whispering with a wink",
         "beats": [
             ("Rosie tipped out her coin purse. One button. Some fluff. A walnut.",
              "close-up", "ROSIE shakes the tiny purse and a walnut drops out onto the rug", "ROSIE",
              "hopeful, then flat", "tilts down", "a tiny rattle and one hollow knock"),
             ("\"I'll keep Tori busy,\" whispered Mom. \"A surprise needs a lookout.\"",
              "medium close-up", "MOM bends close and winks while ROSIE's straw lifts a little", ["MOM", "ROSIE"],
              "conspiring and warm", "pushes in", "a soft rustle of cloth and a fire crackle"),
         ]},
        {"title": "The Christmas market", "place": "market",
         "angle": "Wide establishing view with deep perspective up the snowy hill into",
         "who": "CAT the little blue penguin slides ahead on her tummy between the chalets with her scarf "
                f"flying; {ROSIE_CUP} stands in the middle of the square turning to look at everything, straw "
                "tipped right back; TORI and MOM stand arm in arm far ahead under the tall fir tree",
         "beats": [
             ("The Market Train ran south to Quebec City, all stone walls and steep snowy roofs.",
              "wide shot", "CAT slides forward on her tummy and spins to a stop in the square", "CAT",
              "gleeful and quick", "tilts up", "a far train whistle and a long slide on snow"),
             ("Up the hill was the **marché de Noël** (mar-SHAY duh no-EL) = Christmas market.",
              "wide shot", "TORI and MOM stand arm in arm looking up at the tall fir tree as its glass bulbs sway",
              ["TORI", "MOM"], "happy and unhurried", "pans right", "soft crunching steps and a tinkle of glass"),
             ("It smelled of gingerbread and pine. Every little chalet twinkled.",
              "medium shot", "ROSIE turns slowly on the spot and her straw swings round after her", "ROSIE",
              "dazzled", "pushes in", "a tinkle of glass and a far music box"),
         ]},
        {"title": "Nobody wanted a walnut", "place": "market",
         "angle": "Low angle from the snow looking up at the high counter of a stall in",
         "who": f"{ROSIE_CUP} stands far below a counter of shining glass birds and painted music boxes holding "
                "one walnut up in front of her cup, straw drooping; HARFANG perches on the roof of the stall "
                "right above her, looking down with round golden eyes",
         "beats": [
             ("And everything cost coins. Glass birds, five. Music boxes, ten. Nobody wanted a walnut.",
              "medium shot", "ROSIE holds her walnut up toward the counter and slowly lowers it again", "ROSIE",
              "hopeful, then sunk", "tilts up", "a tinkle of glass and a soft flump of snow"),
             ("Rosie's straw drooped. Then a calm voice above her said, \"Hoo-là-là.\"",
              "medium close-up", "HARFANG leans down from the stall roof and blinks once, very slowly", "HARFANG",
              "calm and kindly", "tilts up", "a soft ruffle of feathers"),
         ]},
        {"title": "Harfang", "place": "market",
         "angle": "Medium view along the snowy lane between the chalets of",
         "who": "HARFANG stands tall in the snow in his red woven sash with his head turned all the way around "
                f"to look backward over his own tail, one wing pointing down the lane; {ROSIE_CUP} looks up at "
                "him with wide eyes, the walnut in front of her cup",
         "beats": [
             ("It was Harfang the snowy owl, in his red sash. His head turned all the way around.",
              "medium shot", "HARFANG turns his head slowly all the way round and back to the front", "HARFANG",
              "dignified and thorough", "pushes in", "a slow soft creak of feathers"),
             ("\"No coins, small one? Follow me. I know a chalet where you do not buy. You make.\"",
              "medium shot", "HARFANG sweeps one wing down the lane and ROSIE's straw springs up",
              ["HARFANG", "ROSIE"], "grand and hopeful", "pans left", "a whoosh of a wing and a crunch of snow"),
         ]},
        {"title": "The wood-carving chalet", "place": "chalet",
         "angle": "Wide view from the plank doorway into",
         "who": "MAGNUS sits hunched on a stool at the carving bench with a small knife and a curl of pine in "
                "his big paws, bushy eyebrows frowning, his ancient wooden skis leaning in the corner; "
                f"{ROSIE_CUP} stands in the doorway with her straw up; HARFANG fills the doorway behind her",
         "beats": [
             ("The wood-carving chalet smelled of pine and paint. Curls of wood lay everywhere, like snow.",
              "wide shot", "ROSIE takes one hop inside and a curl of wood skitters away from her feet", "ROSIE",
              "curious and delighted", "pushes in", "a soft crunch of shavings"),
             ("At the bench sat a big grumpy shape, whittling. \"Magnus!\" said Rosie.",
              "medium shot", "MAGNUS looks up from his whittling and his eyebrows shoot up", "MAGNUS",
              "caught and gruff", "tilts up", "a knife scrape on wood, then a pause"),
             ("\"I came for the wood,\" grumbled Magnus. \"Not the tinsel. The wood.\"",
              "medium close-up", "MAGNUS waves his curl of pine at the window and goes back to whittling",
              "MAGNUS", "grumpy and at home", "holds still", "a slow knife scrape on wood"),
         ]},
        {"title": "One noble act", "place": "chalet",
         "angle": "Low angle from the shavings on the floor looking up at",
         "who": f"{ROSIE_CUP} stands on an upturned crate holding one walnut out in front of her cup, eyes big "
                "and hopeful; MAGNUS looks down at the walnut with a long-suffering frown and soft eyes; CAT "
                "the little blue penguin leans on the bench leg with one flipper raised, grinning",
         "beats": [
             ("\"I need a present for Tori,\" said Rosie. \"I have a walnut.\"",
              "medium shot", "ROSIE holds the walnut out a little farther and her straw quivers", "ROSIE",
              "earnest and hopeful", "pushes in", "a soft crunch of shavings"),
             ("Magnus sighed down to his toes. \"Fine. But this is my one noble act for the week.\"",
              "medium close-up", "MAGNUS heaves a huge sigh that blows shavings off the bench", "MAGNUS",
              "worn down and quietly pleased", "tilts up", "one long gust and a flutter of shavings"),
             ("\"You were a tent pole on Tuesday,\" said Cat. \"That was furniture,\" said Magnus.",
              "medium shot", "CAT raises one flipper and MAGNUS glares down at her over his muzzle",
              ["CAT", "MAGNUS"], "cheeky and unmoved", "pans left", "a tiny foot tap on shavings"),
         ]},
        {"title": "A straw-rest. Obviously.", "place": "chalet",
         "angle": "Close view across the scarred carving bench in",
         "who": "MAGNUS sets a small pale block of pine with a dip in its top on the bench with one big claw; "
                f"{ROSIE_CUP} stands on the bench beside it with her striped straw bent over to look, a little "
                "picture list in front of her cup",
         "beats": [
             ("\"What does your sister need?\" \"Somewhere to lean her straw at night. It's very tall.\"",
              "medium close-up", "ROSIE tips her own straw far to one side to show how it flops", "ROSIE",
              "serious and practical", "pushes in", "a pencil scratch on paper"),
             ("\"A straw-rest,\" said Magnus. \"Obviously.\" He gave her a pine block with a dip in it.",
              "close-up", "MAGNUS slides the little pine block across the bench with one claw", "MAGNUS",
              "matter-of-fact", "tilts down", "a soft scrape of wood on wood"),
         ]},
        {"title": "Shff, shff, shff", "place": "chalet",
         "angle": "Tight low angle at bench height in",
         "who": f"{ROSIE_CUP} hugs a scrap of sandpaper against the little pine block and rubs with all her "
                "might, her whole cup blurred with jiggling and foam rising under her dome lid, tongue out; "
                "MAGNUS holds the block steady with one claw, watching closely",
         "beats": [
             ("Magnus showed her how to sand. Shff, shff, shff. Rosie's whole cup jiggled. Her tea went foamy.",
              "medium close-up", "ROSIE rubs the sandpaper back and forth and her whole cup jiggles", "ROSIE",
              "fierce and foamy", "pushes in", "a quick steady rasp of sandpaper"),
             ("\"**慢慢來** (màn man lái) = Take it slow,\" she hummed, like Yeh Yeh. The pine turned smooth as butter.",
              "close-up", "ROSIE slows to long careful strokes while MAGNUS gives one small nod",
              ["ROSIE", "MAGNUS"], "patient and proud", "holds still", "a slow soft rasp of sandpaper"),
         ]},
        {"title": "Glug", "place": "chalet",
         "angle": "High angle looking straight down on the paint jars of",
         "who": f"{ROSIE_CUP} stands frozen on the bench with a tiny brush of green paint in front of her cup "
                "and her straw drooping, beside a tipped jam jar of bright blue paint that has spilled in a "
                "curly-edged pool right across the little pine block",
         "beats": [
             ("Now for paint. Green, like Tori's straw. But Rosie's elbow bumped the pot of blue.",
              "medium shot", "ROSIE turns with her tiny green brush and the jar of blue rocks behind her",
              "ROSIE", "busy, then startled", "pushes in", "a glassy wobble"),
             ("Glug. Blue paint ran right across the little straw-rest. Rosie's straw drooped.",
              "close-up", "ROSIE's straw droops as the blue pool spreads over the pine block", "ROSIE",
              "dismayed", "tilts down", "one slow glug"),
         ]},
        {"title": "Like a wave", "place": "chalet",
         "angle": "Extreme close-up at the level of the pine block on the bench in",
         "who": f"{ROSIE_CUP} leans in with her lid tilted and the tiniest brush in front of her cup, painting "
                "curls along the edge of the blue so that blue waves roll around the little pine straw-rest, "
                "a dab of blue on her lid, straw wiggling; MAGNUS watches over her with one eyebrow raised",
         "beats": [
             ("Then she tilted her lid. The spill had a curly edge. Like a wave!",
              "close-up", "ROSIE tilts her lid to one side and her straw slowly rises", "ROSIE",
              "puzzled, then sparked", "pushes in", "a tiny thoughtful hum of breath"),
             ("Rosie took the tiniest brush. One curl. Two curls. Soon blue waves rolled all round.",
              "extreme close-up", "ROSIE paints one small curl after another along the blue edge", "ROSIE",
              "absorbed and happy", "tracks beside", "tiny wet brush strokes"),
             ("\"Hm,\" said Magnus. From Magnus, that was a standing ovation.",
              "medium close-up", "MAGNUS raises one eyebrow and gives the smallest nod", "MAGNUS",
              "impressed and hiding it", "holds still", "one low rumbly hum"),
         ]},
        {"title": "I'm dancing", "place": "chalet",
         "angle": "Wide view from the snowy market lane outside the plank door of",
         "who": "CAT the little blue penguin stands planted on the doorstep with her back against the closed "
                "plank door and both flippers spread wide, grinning too hard; TORI walks up with a paper bag of "
                "gingerbread, her green straw tilted in suspicion; MOM hurries up behind her with an apologetic "
                "face",
         "beats": [
             ("Then, outside: \"Rosie? Are you in there?\" Tori! Mom hurried behind. \"Sorry! She's quick!\"",
              "wide shot", "TORI leans toward the plank door while MOM hurries up behind her", ["TORI", "MOM"],
              "curious and flustered", "pushes in", "quick crunching steps in snow"),
             ("Cat zoomed out and blocked the door. \"You can't come in. I'm... dancing.\"",
              "medium shot", "CAT spreads her flippers across the door and grins as wide as she can", "CAT",
              "panicked and inventive", "holds still", "a door thump and a nervous foot tap"),
         ]},
        {"title": "Do it again", "place": "chalet",
         "angle": "Dynamic low angle from the snow on the doorstep of",
         "who": "CAT the little blue penguin leans far back on one foot in a hip-hop pose with one flipper "
                "pointing at the sky and her yellow scarf whipping round; TORI watches with her paper bag "
                "forgotten and her mouth open; HARFANG perches on the snowy roof above with his head twisted "
                "all the way round, eyes huge",
         "beats": [
             ("And she danced. Slide, spin, flipper-pop, moonwalk. Harfang's head went right round. Twice.",
              "wide shot", "CAT slides backward across the doorstep and pops one flipper up while HARFANG "
              "follows her with his whole head", ["CAT", "HARFANG"], "dazzling and dizzying", "tracks beside",
              "squeaky slides on snow and a soft creak of feathers"),
             ("\"That was weird,\" said Tori. \"Do it again.\" So Cat did. With a backspin.",
              "medium shot", "TORI bobs her straw in time as CAT drops into a new pose", ["TORI", "CAT"],
              "entertained and proud of it", "pans right", "a quick shuffle of feet and a paper bag rustle"),
         ]},
        {"title": "Stick with me", "place": "chalet",
         "angle": "Close busy view across the carving bench in",
         "who": "MARGOT leans over a sheet of brown wrapping paper holding it flat with both stretchy arms, "
                f"smiling sweetly, strands of taffy stuck to the paper and the bench; {ROSIE_CUP} ties a red "
                "ribbon around a small lumpy parcel in front of her cup, a dab of blue on her lid; MAGNUS holds "
                "up one elbow with a sheet of brown paper stuck to it",
         "beats": [
             ("Rosie wrapped fast. Margot the maple taffy hopped in to hold the paper. \"Stick with me!\"",
              "medium shot", "MARGOT presses the wrapping paper flat with both stretchy arms", "MARGOT",
              "easygoing and helpful", "pushes in", "a crackle of paper"),
             ("It stuck. It stuck to Margot, to the bench, and to Magnus's elbow.",
              "medium close-up", "MAGNUS lifts his elbow and a sheet of paper stretches up with it on taffy strings",
              "MAGNUS", "stuck and resigned", "tilts up", "a long sticky stretch and a crackle of paper"),
             ("Rosie tied on the red ribbon from the door. \"**Merci** (mehr-SEE) = thank you, everybody!\"",
              "close-up", "ROSIE pulls the red ribbon into a bow and her straw wiggles", "ROSIE",
              "proud and grateful", "holds still", "a soft ribbon swish"),
         ]},
        {"title": "I found it", "place": "chalet",
         "angle": "Tight close-up along the top of the carving bench in",
         "who": "MAGNUS pushes a tiny carved wooden cup with a tiny wooden straw across the bench with one "
                "claw while looking up at the rafters, fresh pine shavings all over his paws; "
                f"{ROSIE_CUP} stares at the tiny wooden cup with her eyes huge and her straw straight up",
         "beats": [
             ("Magnus slid something tiny across the bench. A wooden cup with a straw. \"I found it.\"",
              "close-up", "MAGNUS nudges the tiny wooden cup forward with one claw and looks away", "MAGNUS",
              "gruff and bashful", "pushes in", "a tiny scrape of wood"),
             ("There were fresh shavings all over his paws. \"On the floor. Just lying there.\"",
              "medium close-up", "ROSIE looks from the tiny cup to the shavings on the paws of MAGNUS and beams",
              ["ROSIE", "MAGNUS"], "touched and tickled", "tilts up", "a soft crunch of shavings"),
         ]},
        {"title": "That lump", "place": "market",
         "angle": "Medium view beside the tall fir tree in",
         "who": "MOM stands very straight with a square lump bulging under her scarf and a perfectly innocent "
                f"face; TORI points her green straw at the lump with one eyebrow up; {ROSIE_CUP} stands between "
                "them looking at the sky with her straw wiggling",
         "beats": [
             ("Mom hid the present under her scarf. \"What's that lump?\" asked Tori. \"A walnut,\" said Mom.",
              "medium shot", "TORI points at the lump while MOM pats her scarf flat and smiles", ["TORI", "MOM"],
              "suspicious and serene", "pushes in", "a soft pat on wool and a tinkle of glass"),
         ]},
        {"title": "Lantern eighteen", "place": "lane", "time": "night",
         "angle": "Upward view along the string of lanterns over",
         "who": "TORI stands on a snowy crate hooking a pine-green paper lantern tied with a red ribbon onto "
                f"the long string, looking back over her shoulder with a puzzled smile; {ROSIE_CUP} stands below "
                "with her straw wiggling; MOM and CAT the little blue penguin stand side by side beaming up at "
                "her, a square lump still under the scarf of MOM",
         "beats": [
             ("The Market Train had them home by dark, with a pine-green lantern tied in ribbon.",
              "wide shot", "TORI lifts the pine-green lantern toward the string and its ribbon flutters", "TORI",
              "careful and cheerful", "tilts up", "a far train whistle and a creak of string"),
             ("Tori hung it on Lantern Lane. \"One more light. Why is everyone smiling at me?\"",
              "medium shot", "TORI hooks the lantern on and looks back down at MOM and CAT, who beam up at her",
              ["TORI", "MOM", "CAT"], "puzzled and amused", "pushes in", "a tiny click of a hook"),
             ("\"It's a surprise,\" said Rosie. Her straw wiggled all the way to the bunk room.",
              "medium close-up", "ROSIE's straw wiggles fast and she gives one happy bounce", "ROSIE",
              "bursting and delighted", "pulls back", "a soft crunch of snow and a far sizzle of a grill"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, a dab of blue paint "
                "on her lid, eyes comfortably closed; CAT the little blue penguin asleep curled on a soft "
                "pillow at the foot of the bed, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, with paint on your lid. Goodnight, Magnus, who carved nothing at all.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Cat, still dancing in your dreams. May all your surprises keep until Christmas.",
              "medium close-up", "CAT settles deeper into her pillow and one foot gives a tiny sleepy tap", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, with paint on your lid.",
        "Goodnight, Magnus, who carved nothing at all.",
        "Goodnight, Cat, still dancing in your dreams.",
        "May all your surprises keep until Christmas.",
    ],
}
