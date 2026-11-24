"""07 — No Two Snowflakes (Monday, December 7)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "07",
    "slug": "no-two-snowflakes",
    "title": "No Two Snowflakes",
    "meta": [
        ("Day", "Monday, December 7 · door seven"),
        ("Holiday thread", "Paper snowflakes for the lodge windows"),
        ("Guests", "Cleo Coldwater ❄️ (the valley's painter), Lina the snowflake crisp (in charge), "
                   "Gabby the black star shark"),
        ("Cat’s role", "local guide (she knows what happens if you stand still near Cleo, and stands still "
                       "anyway) and maker of the lightest snowfall in Frostpeak"),
        ("Mandarin", "雪花 snowflake · 剪紙 paper cutting · 不一樣 different"),
        ("Setting", "The Door Wall, the craft loft at the top of Frostpeak Lodge, Lantern Lane at night, "
                    "and the bunk room"),
    ],
    "palette": "paper white and warm cream with saturated icy teal and ribbon red accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "LINA", "GABBY", "COLDWATER"],
    "cast_note": "Humans in this story: none. Gabby swims through the air a little above the table; the paper "
                 "snowflakes are plain cut paper with holes and points, and every one is a different shape.",
    "key_shot": 14,
    "places": {
        "door": DOORWALL,
        "loft": {
            "name": "the craft loft at the top of Frostpeak Lodge",
            "scene": "the sunny craft loft",
            "props": "tall frosted windows with deep wooden sills, a long worktable strewn with white paper "
                     "squares, jars of round-tipped scissors, a round paper basket, paper chains looped along "
                     "the rafters, a paint-splashed easel, a step stool",
            "light": "Pale winter sun glows through the tall frosted windows",
            "accents": "icy teal and ribbon red",
            "atmo": "Tiny paper snippets flutter down like confetti",
            "motion": "tiny paper snippets flutter down like confetti",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a lopsided paper snowflake and a tiny pair of round-tipped scissors on the nightstand"),
    },
    "shots": [
        {"title": "Door seven", "place": "door",
         "angle": "Low angle looking up the tall Door Wall in",
         "who": f"{ROSIE_CUP} stands on the long woven rug gazing up with her straw perked and her eyes bright; "
                "LINA bounces on a wooden footstool beside one little closed door, a puff of white powdered sugar "
                "bursting off her corners, beaming with pride",
         "beats": [
             ("Morning at Frostpeak Lodge! Six little doors stood open on the Door Wall.",
              "wide shot", "ROSIE hops once on the rug and her straw perks up", "ROSIE", "eager and bright",
              "tilts up", "a crackling fire and one soft hop on the rug"),
             ("Door seven was Lina's turn. Poof! Up she hopped in a puff of sugar.",
              "medium shot", "LINA bounces on the footstool and a white puff of sugar bursts around her", "LINA",
              "bubbly and important", "pushes in", "a soft poof and a tiny brass knob rattle"),
         ]},
        {"title": "A folded triangle", "place": "door",
         "angle": "Close view at knob height of one open little door in",
         "who": "LINA holds a small folded white paper triangle in both tiny arms with sparkling eyes; "
                f"{ROSIE_CUP} leans in beside her with round curious eyes",
         "beats": [
             ("Behind the door sat a folded paper triangle. Lina unfolded it. A **雪花** (xuěhuā) = snowflake!",
              "close-up", "LINA unfolds the paper triangle into a lacy paper snowflake", "LINA",
              "careful, then thrilled", "pushes in", "a crisp paper rustle"),
             ("\"Paper-snowflake day!\" said Lina. \"I'm in charge. I was born for this.\"",
              "medium close-up", "LINA holds the paper snowflake high and strikes a proud pose while ROSIE gives "
              "a little bounce", ["LINA", "ROSIE"], "delighted and bossy in a friendly way", "pulls back",
              "a paper flutter and a crackling fire"),
         ]},
        {"title": "The craft loft", "place": "loft",
         "angle": "Wide establishing view with deep perspective down the long worktable in",
         "who": "LINA stands on an upturned paper basket like a teacher with one tiny arm raised; MOM holds out "
                f"white paper squares with a calm smile; {ROSIE_CUP} stands on the worktable holding a little "
                "picture list in front of her cup, the list showing three plain doodles of a folded square, "
                "a pair of scissors and an open snowflake",
         "beats": [
             ("The craft loft sat at the top of the lodge. It smelled of pine, paint, and paper.",
              "wide shot", "LINA spreads both tiny arms wide to show off the loft", "LINA",
              "proud and welcoming", "pushes in", "a soft creak of floorboards and paper rustling"),
             ("Mom handed out paper and round-tipped scissors. \"This is **剪紙** (jiǎnzhǐ) = paper cutting.\"",
              "medium shot", "MOM holds out a white paper square with a gentle nod", "MOM", "calm and kind",
              "tracks beside", "a paper rustle and a soft clink of scissors in a jar"),
             ("Rosie made a list. One: fold. Two: snip. Three: open. \"Fold, fold, fold,\" sang Lina. \"Snip!\"",
              "medium close-up", "ROSIE lifts her little picture list high in front of her cup while LINA hops "
              "in time on her basket", ["ROSIE", "LINA"], "organized and excited", "tilts down",
              "a paper rustle and three little hops"),
         ]},
        {"title": "Don't stand still", "place": "loft",
         "angle": "Medium view beside the tall frosted windows in",
         "who": "COLDWATER paints a curl of frost-blue along a window frame with her little paintbrush, a dab of "
                "blue paint on the tip of her beak, dreamy and calm; CAT the little blue penguin points one "
                "flipper at her with a knowing grin",
         "beats": [
             ("By the window stood Cleo Coldwater, the valley's painter, with blue paint on her beak.",
              "medium shot", "COLDWATER sweeps her paintbrush along the window frame in one slow curl",
              "COLDWATER", "dreamy and absorbed", "pans right", "a soft brush swish on wood"),
             ("\"That's Cleo,\" whispered Cat the penguin. \"She paints everything. Don't stand still.\"",
              "medium close-up", "CAT points a flipper at COLDWATER and shuffles quickly from foot to foot",
              ["CAT", "COLDWATER"], "cheeky and wise", "pushes in", "quick little penguin foot taps"),
             ("\"Every slope tells a story,\" said Cleo. \"So does every snip. Snip bravely.\"",
              "medium close-up", "COLDWATER turns from the window and raises her paintbrush like a wand",
              "COLDWATER", "grand and gentle", "holds still", "a tiny drip of paint and a paper rustle"),
         ]},
        {"title": "Tori's perfect one", "place": "loft",
         "angle": "Close view across the paper-strewn worktable in",
         "who": "TORI holds up a perfect six-pointed paper snowflake with a careful proud smile, green straw "
                f"tall; {ROSIE_CUP} stands beside her gazing at it with round admiring eyes, her picture list "
                "held in front of her cup",
         "beats": [
             ("Tori snipped slowly, tongue out. She opened her paper. Six even points. A perfect snowflake.",
              "medium shot", "TORI opens her folded paper into a perfect snowflake and holds it up", "TORI",
              "careful and pleased", "pushes in", "slow scissor snips and a crisp paper rustle"),
             ("\"Ooooh,\" said everyone. Rosie added to her list. Four: make mine exactly like Tori's.",
              "medium close-up", "ROSIE stares at the perfect snowflake and hugs her list closer to her cup",
              "ROSIE", "admiring and determined", "tilts down", "a soft chorus of paper rustles"),
         ]},
        {"title": "Nibble, nibble, nibble", "place": "loft",
         "angle": "Low angle at tabletop height past a jar of scissors in",
         "who": "GABBY floats just above the worktable nibbling the edge of a folded paper triangle with tiny "
                "careful bites, eyes crossed in concentration; LINA watches from the table with round "
                "delighted eyes",
         "beats": [
             ("Gabby the black star shark used no scissors. Nibble, nibble, nibble went her tiny teeth.",
              "close-up", "GABBY nibbles along the folded paper edge with tiny quick bites", "GABBY",
              "focused and dainty", "pushes in", "tiny paper nibbling sounds"),
             ("Out came a zigzag snowflake. \"Don't worry,\" said Gabby. \"I only bite pie. And paper.\"",
              "medium shot", "GABBY shakes the paper open into a zigzag snowflake while LINA claps her tiny arms",
              ["GABBY", "LINA"], "modest and funny", "pulls back", "a paper flap and tiny claps"),
         ]},
        {"title": "A very light snowfall", "place": "loft",
         "angle": "Medium close view over a heap of paper snippets in",
         "who": "CAT the little blue penguin holds up a paper snowflake that is one big round hole with a thin "
                "paper rim, peeking through the hole with a cheerful grin, tiny scissors in her other flipper; "
                "LINA stands beside her with her tiny arms thrown up in delight",
         "beats": [
             ("Cat snipped fast. Snip-snip-snip-snip! She opened hers. It was mostly hole.",
              "medium shot", "CAT lifts the paper ring and pokes her whole head through the hole", "CAT",
              "surprised, then pleased", "pushes in", "four fast scissor snips and a paper rustle"),
             ("\"It's a very light snowfall,\" said Cat. \"Poof! I love it,\" said Lina.",
              "medium close-up", "CAT wears the paper ring like a collar and shrugs while LINA bounces",
              ["CAT", "LINA"], "unbothered and merry", "holds still", "a soft poof and a paper rustle"),
         ]},
        {"title": "She stood still", "place": "loft",
         "angle": "Low angle beside the paint-splashed easel in",
         "who": "CAT the little blue penguin stands frozen in a proud pose holding her paper ring up to the "
                "light, a fresh blue painted snowflake shining on her white tummy; COLDWATER leans in behind "
                "her with her little paintbrush raised and a dreamy satisfied smile",
         "beats": [
             ("Cat held it up to admire it. She stood very still. Swish, swish.",
              "medium shot", "COLDWATER dabs her paintbrush twice toward the tummy of CAT, who holds her pose",
              ["COLDWATER", "CAT"], "dreamy and stealthy", "pushes in", "two soft brush swishes"),
             ("Now Cat had a blue snowflake on her tummy. \"I did warn me,\" said Cat.",
              "medium close-up", "CAT looks down at her painted tummy and slowly shakes her head", "CAT",
              "resigned and amused", "tilts down", "a tiny drip of paint"),
         ]},
        {"title": "Exactly like Tori's", "place": "loft",
         "angle": "Over-the-shoulder view past a perfect paper snowflake lying on the worktable in",
         "who": f"{ROSIE_CUP} holds a folded paper triangle and tiny round-tipped scissors in front of her cup, "
                "peeking sideways at the perfect snowflake with her straw wiggling, tongue-tip out in "
                "concentration",
         "beats": [
             ("Rosie peeked at Tori's. Fold like Tori. Snip like Tori. Her straw wiggled. She opened it.",
              "medium close-up", "ROSIE snips one tiny careful snip and her straw wiggles", "ROSIE",
              "hopeful and intent", "pushes in", "one careful scissor snip"),
             ("Oh. One arm was long. One arm was short. The middle hole leaned sideways.",
              "close-up", "ROSIE opens the paper into a lopsided snowflake and her eyes go round", "ROSIE",
              "hope sliding into surprise", "holds still", "a slow paper rustle"),
         ]},
        {"title": "Looking casual", "place": "loft",
         "angle": "High angle looking down on one corner of the worktable in",
         "who": f"{ROSIE_CUP} stands squarely in front of the round paper basket with her straw drooping and her "
                "eyes looking innocently at the ceiling, one corner of a lopsided paper snowflake poking out "
                "from under the basket behind her",
         "beats": [
             ("It looked nothing like Tori's. Rosie's straw drooped. She slid it under the paper basket.",
              "medium shot", "ROSIE nudges the lopsided snowflake under the basket and her straw droops", "ROSIE",
              "sheepish", "tilts down", "a soft scrape of a basket on wood"),
             ("Then she stood in front of the basket, looking casual. Cups are not good at casual.",
              "medium close-up", "ROSIE rocks on her tiny feet and looks up at the ceiling", "ROSIE",
              "elaborately innocent", "holds still", "a tiny tuneless hum"),
         ]},
        {"title": "Where is yours?", "place": "loft",
         "angle": "Low angle along the worktable past a row of paper snowflakes in",
         "who": "LINA hops along the table edge counting paper snowflakes with one tiny arm, bright and curious; "
                f"{ROSIE_CUP} stands by the round paper basket holding the lopsided snowflake half hidden "
                "behind her cup, eyes down",
         "beats": [
             ("Lina hopped down the table, counting. \"Tori's. Gabby's. Cat's hole. Rosie, where is yours?\"",
              "medium shot", "LINA hops along the row of snowflakes and stops with her head tilted", "LINA",
              "busy, then curious", "tracks beside", "little hops on wood and a soft poof"),
             ("\"It came out wonky,\" whispered Rosie. Slowly, she pulled it out.",
              "medium close-up", "ROSIE slowly brings the lopsided snowflake out from behind her cup", "ROSIE",
              "shy and honest", "pushes in", "a slow paper slide"),
         ]},
        {"title": "That is the whole point", "place": "loft",
         "angle": "Close low angle across the worktable in",
         "who": "LINA stands with her tiny arms on her hips and her chin up, a puff of white powdered sugar "
                f"bursting off her corners, fierce and fond; {ROSIE_CUP} looks at her with wide surprised eyes, "
                "holding the lopsided paper snowflake in front of her cup",
         "beats": [
             ("Lina put her tiny arms on her hips. \"Rosie. Look at me. I am a snowflake crisp.\"",
              "medium close-up", "LINA plants her tiny arms on her hips and lifts her chin", "LINA",
              "fierce and fond", "pushes in", "one firm little stomp"),
             ("\"No two alike. That is the whole point.\" Poof! went her sugar, for emphasis.",
              "medium shot", "LINA stamps one foot and a white puff of sugar bursts up while ROSIE blinks",
              ["LINA", "ROSIE"], "certain and sparkling", "holds still", "a soft poof"),
         ]},
        {"title": "Up to the window", "place": "loft",
         "angle": "Low angle looking up the tall frosted window in",
         "who": "COLDWATER holds the lopsided paper snowflake flat against the bright glass with both flippers, "
                f"her plumes glowing in the sun, thoughtful and sure; {ROSIE_CUP} stands on the deep wooden sill "
                "beside her looking up, straw half raised",
         "beats": [
             ("Cleo lifted Rosie's snowflake in two careful flippers and held it to the window.",
              "medium shot", "COLDWATER raises the lopsided snowflake and presses it gently to the glass",
              "COLDWATER", "thoughtful and sure", "tilts up", "a soft tap of paper on glass"),
             ("The winter sun shone through. A big lacy shadow spilled across the floor: a stem, and petals.",
              "medium close-up", "ROSIE turns to look down behind her and her straw rises a little", "ROSIE",
              "curious and hopeful", "tilts down", "a hush and a tiny creak of the sill"),
         ]},
        {"title": "A snowflake that is also a rose", "place": "loft",
         "angle": "High angle looking down at the sunlit floorboards of",
         "who": "a big lacy shadow shaped like a rose on a long stem spills across the floorboards in a bright "
                f"patch of window sun; {ROSIE_CUP} stands at the edge of the shadow with shining eyes and her "
                "straw rising; GABBY floats beside her with a soft closed smile; COLDWATER stands by the window "
                "with one flipper on her heart",
         "beats": [
             ("\"A snowflake that is also a rose,\" said Cleo softly. \"Only a Rosie could cut that.\"",
              "wide shot", "COLDWATER presses one flipper to her heart as ROSIE hops to the edge of the shadow",
              ["COLDWATER", "ROSIE"], "moved and astonished", "pushes in", "one soft hop on floorboards"),
             ("\"I bit a hundred holes and got zigzags,\" said Gabby. \"You got a garden.\"",
              "medium close-up", "GABBY swishes her tail and tips her head toward ROSIE", ["GABBY", "ROSIE"],
              "dry and generous", "holds still", "a soft tail swish"),
         ]},
        {"title": "Want to trade?", "place": "loft",
         "angle": "Warm close two-shot beside the sunny window sill in",
         "who": f"TORI leans close to ROSIE holding out her own perfect paper snowflake with a soft hopeful "
                f"smile, green straw bobbing; {ROSIE_CUP} hugs her lopsided paper snowflake in front of her cup "
                "with her straw wiggling high",
         "beats": [
             ("\"Mine is neat,\" said Tori. \"Yours is **不一樣** (bù yíyàng) = different. Want to trade?\"",
              "medium close-up", "TORI holds out her perfect snowflake and tilts her straw toward ROSIE",
              ["TORI", "ROSIE"], "warm and a little envious", "pushes in", "a soft paper rustle"),
             ("\"Not for anything,\" said Rosie. Her straw wiggled all the way up.",
              "medium close-up", "ROSIE hugs her snowflake closer and her straw wiggles high", "ROSIE",
              "proud and glowing", "holds still", "a tiny happy squeak of a straw"),
         ]},
        {"title": "One of everybody's", "place": "loft",
         "angle": "Wide view of the whole tall frosted window in",
         "who": "MOM stands on the step stool pressing a paper snowflake to the glass with a strip of tape, "
                "smiling; CAT the little blue penguin passes paper snowflakes up to her from a pile; "
                f"{ROSIE_CUP} stands on the sill with her straw tall; the window is filling with paper snowflakes "
                "of every shape, one with zigzag edges, one that is mostly hole, one perfect and even, one with "
                "a tiny heart in the middle, and a lopsided rose-shaped one in the very center",
         "beats": [
             ("Mom fetched the tape. Up went Tori's. Up went Gabby's zigzags. Up went Cat's very light snowfall.",
              "medium shot", "MOM presses a snowflake to the glass while CAT passes the next one up",
              ["MOM", "CAT"], "busy and cheerful", "tilts up", "a squeak of tape and paper rustling"),
             ("Up went Mom's, with a tiny heart in the middle. Up went Lina's, which looked like Lina.",
              "medium close-up", "MOM smooths a snowflake with a tiny heart in its middle onto the glass", "MOM",
              "tender and pleased", "pans right", "a soft pat on glass"),
             ("And right in the center went Rosie's rose.",
              "wide shot", "ROSIE looks up at the rose-shaped snowflake in the center and her straw wiggles",
              "ROSIE", "full-hearted and proud", "pulls back", "a hush and a happy little hop"),
         ]},
        {"title": "Indoor blizzard", "place": "loft",
         "angle": "Wide low angle across the sunlit floorboards of",
         "who": "lacy snowflake shadows of every shape cover the whole floor in bright window sun; LINA leaps "
                "in the middle of them flinging a double armful of white paper snippets high into the air; "
                f"{ROSIE_CUP} stands under the falling snippets with her straw up; MOM carries in a tray of "
                "steaming cocoa mugs, laughing; GABBY swims a happy loop through the paper snow",
         "beats": [
             ("Then the sun came right out. Lacy shadows snowed across the whole floor.",
              "wide shot", "ROSIE turns in a slow circle among the shadows with her straw up", "ROSIE",
              "delighted", "pulls back", "a soft hush and a floorboard creak"),
             ("\"Indoor blizzard!\" cried Lina, and threw the snippets high. Mom brought cocoa. They drank it "
              "in the snow.",
              "medium shot", "LINA flings paper snippets into the air as MOM sets down the cocoa tray",
              ["LINA", "MOM"], "gleeful and cozy", "tilts up", "a papery flutter and a clink of mugs"),
         ]},
        {"title": "Lantern seven", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the long lantern string in",
         "who": "GABBY floats up beside the lantern string hanging a white paper lantern cut with "
                "snowflake-shaped holes, tiny snowflake-shaped spots of light scattered across the snow below; "
                f"{ROSIE_CUP} stands in the snow looking up with her straw tall; CAT the little blue penguin "
                "steadies the string with both flippers; LINA hops in the lantern light",
         "beats": [
             ("At dusk, lantern seven went down to Lantern Lane. It was white, cut like a snowflake.",
              "wide shot", "LINA hops in the snow under the white lantern and points up with one tiny arm", "LINA",
              "proud and excited", "tilts up", "soft crunching snow and a paper rustle"),
             ("Gabby swam it up to the string. Snowflakes of light danced on the snow.",
              "medium shot", "GABBY hooks the white lantern onto the string while CAT steadies it",
              ["GABBY", "CAT"], "careful and glad", "pushes in", "a tiny hook click and soft wind"),
             ("\"One more light,\" said Rosie. SpicySquid's birthday surprise was growing.",
              "medium close-up", "ROSIE gazes up at the glowing lantern and her straw sways gently", "ROSIE",
              "content and proud", "pulls back", "soft wind and a faraway sizzle from the grill"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Warm close view across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, "
                "a paper ring still around her neck, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, and your lopsided rose. Goodnight, Lina, with sugar on your toes.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Cat, with paint on your tummy. Sleep well, under snow where no two flakes match.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, and your lopsided rose.",
        "Goodnight, Lina, with sugar on your toes.",
        "Goodnight, Cat, with paint on your tummy.",
        "Sleep well, under snow where no two flakes match.",
    ],
}
