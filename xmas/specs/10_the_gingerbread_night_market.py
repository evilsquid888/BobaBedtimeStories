"""10 — The Gingerbread Night Market (Thursday, December 10)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "10",
    "slug": "the-gingerbread-night-market",
    "title": "The Gingerbread Night Market",
    "meta": [
        ("Day", "Thursday, December 10 · door ten"),
        ("Holiday thread", "Gingerbread: building Lantern Lane out of cookies and icing"),
        ("Guests", "Barnaby Beaksworth ❄️ (the baker), Teddy and Tilda Powderpuff ❄️ (gumdrops and icing, "
                   "mostly icing), Kyle the black bear cub, Lina the snowflake crisp (the weather)"),
        ("Cat’s role", "building inspector with a spoon, and the top half of tonight's lantern ladder"),
        ("Mandarin", "薑餅 gingerbread · 夜市 night market · 對不起 sorry"),
        ("Setting", "The Door Wall, the long floury table of the lodge bakery, Lantern Lane at night, "
                    "and the bunk room"),
    ],
    "palette": "gingerbread brown and warm cream with saturated peppermint red and gumdrop green accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "BARNABY", "TEDDY", "TILDA", "KYLE", "LINA"],
    "cast_note": "Humans in this story: none. The gingerbread lane is a tabletop model: little cookie stalls "
                 "glued with white icing, plain and unlettered. The gingerbread is ordinary cookie, with no "
                 "faces.",
    "key_shot": 17,
    "places": {
        "door": DOORWALL,
        "bakery": {
            "name": "the warm bakery of Frostpeak Lodge",
            "scene": "the warm lodge bakery",
            "props": "a long floury wooden table, a brick bread oven with a glowing mouth, trays of gingerbread "
                     "walls and roofs, piping bags of white icing, jars of gumdrops and peppermints, copper "
                     "cookie cutters hanging on hooks",
            "light": "Warm oven glow and snowy window light fill the bakery",
            "accents": "peppermint red and gumdrop green",
            "atmo": "Flour dust drifts in the warm oven glow",
            "motion": "flour dust drifts in the warm oven glow",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("one green gumdrop and a tiny wooden roof tile with a small bite mark on the nightstand"),
    },
    "shots": [
        {"title": "Door ten", "place": "door",
         "angle": "Low angle from the woven rug up the tall Door Wall in",
         "who": "KYLE stands on tiptoe on a small wooden step with his nose pressed to one little closed door, "
                f"eyes shut in bliss; {ROSIE_CUP} stands beside him on the rug with her straw perked; CAT the "
                "little blue penguin holds the wooden step steady with both flippers",
         "beats": [
             ("Door ten was Kyle's turn. Kyle the black bear cub stood on tiptoe and sniffed the little door.",
              "medium shot", "KYLE sniffs the little door with long happy sniffs", "KYLE", "hopeful and hungry",
              "tilts up", "long snuffly bear sniffs and a crackling fire"),
             ("Inside sat a tiny brown roof tile. It smelled like **薑餅** (jiāngbǐng) = gingerbread. Kyle bit it.",
              "medium close-up", "KYLE opens the little door, lifts out a tiny brown tile and nibbles one corner",
              "KYLE", "eager, then puzzled", "pushes in", "a tiny door creak and a woody crunch"),
         ]},
        {"title": "It's a clue", "place": "door",
         "angle": "Close view at knob height beside one open little door in",
         "who": "KYLE holds a tiny brown wooden roof tile with one small bite mark in it, tongue out, "
                f"disappointed; {ROSIE_CUP} looks at the tile with bright thinking eyes and a wiggling straw; "
                "CAT the little blue penguin points one flipper toward the hall doorway with a grin",
         "beats": [
             ("\"It's wood,\" said Kyle. \"I was just taste-testing.\" \"It's a clue,\" said Rosie. Her straw "
              "wiggled.",
              "medium close-up", "KYLE holds the bitten tile out while ROSIE's straw wiggles",
              ["KYLE", "ROSIE"], "sheepish and excited", "pushes in", "a tiny tongue smack"),
             ("\"Gingerbread day!\" said Cat the penguin. \"To the bakery. Follow the smell. Kyle already is.\"",
              "medium shot", "CAT points toward the doorway as KYLE lifts his nose and leans that way",
              ["CAT", "KYLE"], "brisk and teasing", "pans right", "eager sniffing and penguin foot taps"),
         ]},
        {"title": "Warm as a mitten", "place": "bakery",
         "angle": "Wide establishing view with deep perspective down the long floury table in",
         "who": "BARNABY slides a tray of gingerbread walls out of the brick oven on a wooden paddle, tummy "
                f"dusted with flour, jolly; {ROSIE_CUP} stands on the floury table holding a little picture list "
                "in front of her cup, the list showing plain doodles of little stalls and a string of lanterns, "
                "straw wiggling",
         "beats": [
             ("The lodge bakery was warm as a mitten. It smelled of ginger and cinnamon and butter.",
              "wide shot", "ROSIE turns slowly to look down the long table and her straw lifts", "ROSIE",
              "cozy and impressed", "pushes in", "a soft oven crackle"),
             ("Barnaby Beaksworth, the chinstrap penguin, was baking. Walls, roofs, tiny doors, all gingerbread.",
              "medium shot", "BARNABY slides the tray onto the table and fans it with one flipper", "BARNABY",
              "jolly and proud", "tracks beside", "a tray scrape and an oven crackle"),
             ("\"Today,\" said Rosie, \"we build Lantern Lane. The whole **夜市** (yèshì) = night market. I made "
              "a list.\"",
              "medium close-up", "ROSIE lifts her little picture list high in front of her cup", "ROSIE",
              "organized and thrilled", "tilts down", "a paper rustle"),
         ]},
        {"title": "Glue you can eat", "place": "bakery",
         "angle": "Medium view across bowls of white icing in",
         "who": "MOM stirs a big bowl of white icing with a wooden spoon, calm and smiling; TORI pipes a tiny "
                "icing lantern onto a gingerbread wall with her tongue-tip out; CAT the little blue penguin taps "
                "a standing gingerbread wall with the back of a spoon, one eye squinted like an inspector",
         "beats": [
             ("Mom stirred the icing. \"Icing is glue you can eat,\" she said. \"But it needs time to dry.\"",
              "medium shot", "MOM lifts her spoon and a thick ribbon of icing folds back into the bowl", "MOM",
              "calm and knowing", "pushes in", "a soft thick stirring sound"),
             ("Tori piped tiny icing lanterns, slow and steady. Cat tapped each wall with a spoon. \"Solid. "
              "Mostly.\"",
              "medium close-up", "TORI pipes one careful dot while CAT taps the wall and nods gravely",
              ["TORI", "CAT"], "careful and official", "pans right", "two spoon taps on cookie"),
         ]},
        {"title": "I am the weather", "place": "bakery",
         "angle": "Low angle at tabletop height along a row of little gingerbread roofs in",
         "who": "LINA hops from one little gingerbread roof to the next with a puff of white powdered sugar "
                "bursting off her corners at every landing, sugar snow settling on each roof, bright and proud",
         "beats": [
             ("Lina hopped from roof to roof. Poof! Poof! Poof! Sugar snow on every one.",
              "medium shot", "LINA hops to the next little roof and a white puff of sugar settles on it", "LINA",
              "busy and gleeful", "tracks beside", "three soft poofs"),
             ("\"I am the weather,\" said Lina. Nobody argued with the weather.",
              "medium close-up", "LINA lands, lifts her chin and dusts her tiny arms together", "LINA",
              "grand and pleased with herself", "holds still", "a soft poof and a tiny pat-pat"),
         ]},
        {"title": "Mostly icing", "place": "bakery",
         "angle": "Close view over a heap of gumdrops in",
         "who": "TEDDY and TILDA stand side by side at the table edge holding piping bags, each with a big blob "
                "of white icing on the tip of the nose, grinning the same mischievous grin",
         "beats": [
             ("Teddy and Tilda, the polar bear cubs, were in charge of gumdrops. And icing. Mostly icing.",
              "medium shot", "TEDDY and TILDA squeeze their piping bags and giggle", ["TEDDY", "TILDA"],
              "mischievous and merry", "pushes in", "two squelchy icing squeezes"),
             ("They had iced each other's noses. \"We didn't mean to—\" \"—but it was worth it.\"",
              "medium close-up", "TEDDY and TILDA go cross-eyed looking at their own iced noses",
              ["TEDDY", "TILDA"], "guilty and delighted", "holds still", "two squelchy icing drips"),
         ]},
        {"title": "Enough fish for one more", "place": "bakery",
         "angle": "Medium close view along the little gingerbread lane in",
         "who": "BARNABY sets a tiny gingerbread fish stall at the end of a row of four with one careful "
                f"flipper, beaming; {ROSIE_CUP} stands beside him adding to the picture list held in front of "
                "her cup, patient and amused",
         "beats": [
             ("Barnaby added a little fish stall. Then another. \"There's always enough fish for one more!\"",
              "medium shot", "BARNABY sets down a tiny fish stall and pats its roof", "BARNABY",
              "generous and delighted", "pans right", "a soft cookie tap"),
             ("Lantern Lane now had four fish stalls. Rosie added them to the list.",
              "medium close-up", "ROSIE looks along the row of fish stalls and her straw gives a small shrug",
              "ROSIE", "patient and amused", "tilts down", "a tiny pencil scratch"),
         ]},
        {"title": "The little lane", "place": "bakery",
         "angle": "Low hero angle along the finished little gingerbread lane in",
         "who": "a little gingerbread market lane stands finished down the middle of the table, tiny stalls with "
                "striped icing awnings, a tiny grill stall, a tiny cocoa cart, a string of tiny icing lanterns "
                f"overhead and sugar snow on every roof; {ROSIE_CUP} stands at the far end gazing down the lane "
                "with her straw wiggling high",
         "beats": [
             ("At last it stood finished. Stalls, awnings, a tiny Squid Grill, a string of icing lanterns.",
              "wide shot", "ROSIE gazes down the little lane and her straw wiggles high", "ROSIE",
              "awed and proud", "tracks beside", "a soft oven crackle"),
             ("Rosie's straw wiggled so hard it hummed.",
              "medium close-up", "ROSIE gives one proud little bounce at the end of the lane", "ROSIE",
              "glowing", "pushes in", "one happy hop on wood"),
         ]},
        {"title": "One wall too many", "place": "bakery",
         "angle": "Close view from behind a tiny gingerbread cocoa cart in",
         "who": "KYLE crouches at the table edge with his nose almost touching a gingerbread wall, a small bite "
                "missing from the corner of the tiny cocoa cart, crumbs on his tan muzzle, eyes dreamy",
         "beats": [
             ("Kyle was hungry. He taste-tested one crumb. Then one shutter. Then the corner of the cocoa cart.",
              "close-up", "KYLE nibbles a tiny corner and licks a crumb off his muzzle", "KYLE",
              "dreamy and peckish", "pushes in", "tiny nibbling crunches"),
             ("Then one wall. It was the wall that was holding up everything else.",
              "medium close-up", "KYLE slides one gingerbread wall out with two careful claws", "KYLE",
              "innocent and doomed", "holds still", "a long slow cookie creak"),
         ]},
        {"title": "Crumble", "place": "bakery",
         "angle": "High angle looking down the whole floury table in",
         "who": "the little gingerbread lane tips over like a row of dominoes in a rising cloud of white sugar "
                "snow; KYLE sits back with a piece of gingerbread wall in his paws and his mouth in a round O; "
                "LINA hops backward out of the cloud with round eyes",
         "beats": [
             ("Creeeak. The Squid Grill leaned. The cocoa cart tipped. Crumble, crumble, crumble, down went "
              "the lane.",
              "wide shot", "KYLE freezes with the wall in his paws as the little stalls topple one by one",
              "KYLE", "horrified", "pans right", "a creak and a long soft cookie clatter"),
             ("Sugar snow puffed up in a cloud. When it settled, Lantern Lane was a heap.",
              "medium shot", "LINA gives one tiny sneeze and a last puff of sugar pops up", "LINA",
              "stunned", "pulls back", "a soft settling hiss and a tiny sneeze"),
         ]},
        {"title": "A tiny voice", "place": "bakery",
         "angle": "Close low angle across a heap of broken gingerbread in",
         "who": "KYLE stands with his round ears drooping and his paws pressed together, crumbs on his muzzle, "
                "eyes shiny and sorry, one green gumdrop rolling away past his feet",
         "beats": [
             ("Nobody said a word. Kyle's ears drooped. One last gumdrop rolled off the table. Plink.",
              "medium shot", "KYLE's ears droop slowly as a gumdrop rolls past his feet", "KYLE",
              "caught and small", "holds still", "a hush and one tiny plink"),
             ("\"I wasn't taste-testing,\" said Kyle in a tiny voice. \"I was eating. **對不起** (duìbuqǐ) = "
              "sorry.\"",
              "medium close-up", "KYLE presses his paws together and peeks up", "KYLE", "honest and sorry",
              "pushes in", "a tiny shuffle of paws"),
         ]},
        {"title": "Do it again!", "place": "bakery",
         "angle": "Medium close view over the heap of broken gingerbread in",
         "who": "TEDDY and TILDA bounce on their toes with their paws in the air and their iced noses shining, "
                f"thrilled; {ROSIE_CUP} stands beside the heap with her straw half drooped and a smile just "
                "starting",
         "beats": [
             ("\"That was the best crash ever,\" said Teddy. \"Do it again!\" said Tilda.",
              "medium shot", "TEDDY and TILDA bounce with their paws in the air", ["TEDDY", "TILDA"],
              "thrilled", "pushes in", "bouncing paws on floorboards"),
             ("Rosie's straw drooped, then wiggled. \"Then we have to build it again,\" she said.",
              "medium close-up", "ROSIE's straw droops, then springs back up with a wiggle", "ROSIE",
              "dismay turning to a grin", "holds still", "a tiny straw squeak"),
         ]},
        {"title": "One more lane", "place": "bakery",
         "angle": "Medium view along the floury table in",
         "who": "BARNABY rolls out a fresh sheet of gingerbread dough with a rolling pin, flour flying, jolly; "
                "KYLE holds two gingerbread walls upright between his big steady paws, perfectly still, cheeks "
                "puffed with effort; MOM pipes a thick line of white icing along the join",
         "beats": [
             ("Barnaby was already rolling dough. \"There's always enough gingerbread for one more lane!\"",
              "medium shot", "BARNABY rolls the dough flat and a puff of flour flies up", "BARNABY",
              "jolly and unbothered", "pans right", "a rolling pin rumble"),
             ("This time Kyle held every wall while the icing dried.",
              "medium shot", "KYLE holds the walls steady while MOM pipes icing along the join", ["KYLE", "MOM"],
              "careful and determined", "tracks beside", "a soft icing squeeze"),
             ("He held so still that he forgot to be hungry. Almost.",
              "close-up", "KYLE holds perfectly still and only his nose twitches", "KYLE",
              "heroically still", "holds still", "one tiny sniff"),
         ]},
        {"title": "Bakery law", "place": "bakery",
         "angle": "Close view over a plate of broken gingerbread in",
         "who": "BARNABY slides a plate heaped with broken gingerbread toward KYLE with a wink; KYLE gazes at it "
                "with shining eyes and one hopeful paw raised; CAT the little blue penguin hugs a tiny "
                "gingerbread cocoa cart to her tummy with crumbs on her beak",
         "beats": [
             ("Barnaby slid him the broken bits. \"Broken bits are for tasting. That's bakery law.\"",
              "medium shot", "BARNABY nudges the plate closer and winks at KYLE", ["BARNABY", "KYLE"],
              "kindly and jolly", "pans left", "a plate sliding on a floury table"),
             ("So the first lane became the snack. Cat had the cocoa cart.",
              "medium close-up", "CAT takes a happy nibble of the tiny cocoa cart", "CAT",
              "blissful", "pushes in", "a small crunchy nibble"),
         ]},
        {"title": "That's you", "place": "bakery",
         "angle": "Tight view at the tiny window of a little gingerbread stall in",
         "who": "TORI pipes a tiny pink icing cup into the window of a little gingerbread stall with one steady "
                f"tiny arm, tongue-tip out; {ROSIE_CUP} watches right beside her with her straw wiggling; tiny "
                "candy-cane lampposts and windows of clear red candy line the little lane",
         "beats": [
             ("The new lane had candy-cane lampposts and windows of melted red candy.",
              "medium shot", "ROSIE looks along the row of red candy windows and her straw wiggles", "ROSIE",
              "impressed", "tracks beside", "a soft oven crackle"),
             ("In one window Tori piped a tiny pink cup. \"That's you, little sip,\" said Tori.",
              "close-up", "TORI pipes the last dot of the tiny pink cup and tilts her straw toward ROSIE",
              ["TORI", "ROSIE"], "fond and careful", "pushes in", "a tiny icing squeeze"),
         ]},
        {"title": "Ten gumdrops", "place": "bakery",
         "angle": "Close view under a string of white icing in",
         "who": "a smaller sturdier little gingerbread lane stands with thick icing at every corner and a row "
                "of gumdrops stuck along a string of icing above it; KYLE holds one green gumdrop between two "
                "careful paws, gazing at it; TEDDY and TILDA lean in behind with their iced noses",
         "beats": [
             ("Last came the gumdrops, one for every lantern so far. Ten gumdrops on a string of icing.",
              "medium shot", "TEDDY and TILDA lean in to count the row of gumdrops with their noses",
              ["TEDDY", "TILDA"], "busy and careful", "pans right", "tiny sticky taps"),
             ("Kyle held the tenth one. He looked at it for a long time. Then he stuck it on.",
              "close-up", "KYLE gazes at the green gumdrop, then presses it gently onto the icing string",
              "KYLE", "tempted, then noble", "pushes in", "a long sniff and one sticky tap"),
         ]},
        {"title": "Stall by stall", "place": "bakery",
         "angle": "Low hero angle along the little gingerbread lane beside the glowing oven mouth in",
         "who": "the smaller sturdier little gingerbread lane sits beside the glowing oven mouth with warm light "
                "shining through every red candy window and a row of ten gumdrops strung above it; BARNABY "
                f"nudges its board closer to the glow with one flipper; {ROSIE_CUP} stands at the end of the "
                "lane with the glow on her lid and her straw high; KYLE rests his chin on the table beside her, "
                "gazing",
         "beats": [
             ("Barnaby slid the little lane beside the oven. The glow shone through every candy window.",
              "medium shot", "BARNABY nudges the board toward the oven and the candy windows begin to glow",
              "BARNABY", "proud and gentle", "tracks beside", "a soft scrape and an oven crackle"),
             ("The gingerbread night market lit up, stall by stall.",
              "wide shot", "ROSIE's straw rises as KYLE's eyes go wide in the warm glow", ["ROSIE", "KYLE"],
              "hushed and happy", "pulls back", "a soft oven crackle"),
         ]},
        {"title": "Lantern ten", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the long lantern string in",
         "who": "CAT the little blue penguin stands on the shoulders of KYLE hooking a brown paper lantern "
                "striped with white lines onto the string; KYLE stands steady as a post in the snow with his "
                f"nose lifted toward the lantern; {ROSIE_CUP} stands beside them looking up with her straw tall",
         "beats": [
             ("At dusk Kyle carried lantern ten down to Lantern Lane. It was brown, with white icing lines.",
              "wide shot", "KYLE stands steady in the snow and lifts his nose toward the brown lantern", "KYLE",
              "proud and careful", "tilts up", "soft crunching snow"),
             ("He sniffed it. \"Paper,\" he said, and passed it up to Cat without one single bite.",
              "medium shot", "CAT hooks the brown lantern onto the string from the shoulders of KYLE",
              ["CAT", "KYLE"], "steady and pleased", "pushes in", "one sniff and a tiny hook click"),
             ("\"One more light,\" said Rosie. Ten lanterns on the real lane. Ten gumdrops on the little one.",
              "medium close-up", "ROSIE gazes up at the glowing lantern and her straw sways gently", "ROSIE",
              "content and proud", "pulls back", "soft wind and a faraway sizzle from the grill"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Warm close view across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, "
                "a wooden spoon tucked under one flipper, yellow scarf visible",
         "beats": [
             ("Goodnight, little lane of gingerbread. Goodnight, Kyle, who helped it stand.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, ten gumdrops in a row. Sleep sweet, in a lodge that smells of ginger.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little lane of gingerbread.",
        "Goodnight, Kyle, who helped it stand.",
        "Goodnight, ten gumdrops in a row.",
        "Sleep sweet, in a lodge that smells of ginger.",
    ],
}
