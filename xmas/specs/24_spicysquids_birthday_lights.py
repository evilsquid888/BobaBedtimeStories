"""24 — SpicySquid's Birthday Lights (Thursday, December 24 · Christmas Eve). The finale."""
from places import DOORWALL, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

LIT_PROPS = ("a long string of twenty-four glowing paper lanterns in twenty-four colors overhead, a long feast "
             "table with a chili-red cloth, the Squid Grill stall with rising steam, a cocoa cart, snowy wooden "
             "stalls with striped awnings, snow-dusted fir trees")

STORY = {
    "num": "24",
    "slug": "spicysquids-birthday-lights",
    "title": "SpicySquid's Birthday Lights",
    "meta": [
        ("Day", "Thursday, December 24 · door twenty-four, the last and biggest"),
        ("Holiday thread", "Christmas Eve, and SpicySquid's birthday: the whole lane lit at last"),
        ("Guests", "SpicySquid (the birthday squid), Yeh Yeh, Herschel the Walrus ❄️, Piper Paddlefoot ❄️, "
                   "Lina, Gabby, Kyle; and off the Market Train, Sésame, Couic, Margot and Harfang"),
        ("Cat’s role", "keeper of the surprise (she checked: he never looked up), noodle patrol, and proud host "
                       "of her home valley"),
        ("Mandarin", "生日快樂 happy birthday · 謝謝 thank you"),
        ("Setting", "The Door Wall in the lodge great hall, then Lantern Lane at dusk and at night with all "
                    "twenty-four lanterns glowing, and the bunk room"),
    ],
    "palette": "deep winter blue and warm lantern gold with saturated chili red and grill orange accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "SPICYSQUID", "YEHYEH", "HERSCHEL", "PIPER", "LINA", "GABBY", "KYLE",
             "SESAME", "COUIC", "MARGOT", "HARFANG"],
    "cast_note": "Humans in this story: none. Grown-ups light the lanterns with long lighting sticks; a grown-up "
                 "lights the birthday candle. Nobody eats a character: the feast is latkes, scallion pancakes, "
                 "plain rice-ball tangyuan, pie and one long noodle. The twenty-four lanterns are the month in a "
                 "row: red first, chili red last.",
    "key_shot": 7,
    "places": {
        "doorwall": DOORWALL,
        "lane_dusk": {
            "name": "Lantern Lane at the Frostpeak winter night market, just before the lanterns are lit",
            "scene": "Lantern Lane at dusk",
            "props": "a long string of twenty-four paper lanterns hanging dim overhead, the Squid Grill stall "
                     "glowing orange with rising steam, a cocoa cart, snowy wooden stalls with striped awnings, "
                     "snow-dusted fir trees, footprints in the snow",
            "light": "The orange glow of the grill stall lights the blue snowy lane at dusk",
            "accents": "grill orange and deep winter blue",
            "atmo": "Steam and tiny sparks drift up from the grill",
            "motion": "steam and tiny sparks drift up from the grill",
        },
        "lane_lit": {
            "name": "Lantern Lane at the Frostpeak winter night market with every lantern glowing",
            "scene": "Lantern Lane, every lantern glowing",
            "props": LIT_PROPS,
            "light": "Twenty-four glowing paper lanterns light the snowy lane at night",
            "accents": "chili red and lantern gold",
            "atmo": "Soft snow drifts through the lantern light",
            "motion": "soft snow drifts through the lantern light",
        },
        "bunk": bunk("one small birthday candle and a little picture list with every line ticked on the nightstand"),
    },
    "shots": [
        {"title": "The last door", "place": "doorwall",
         "angle": "Low angle looking up at the biggest carved door in the middle of the Door Wall in",
         "who": f"{ROSIE_CUP} stands on a wooden step stool before the biggest little door, open wide, with one "
                "small red birthday candle standing inside it, holding a little picture list in front of her "
                "cup, the list showing three plain doodles of a lantern, a waving arm and a heart, straw high; "
                "HERSCHEL leans down beside her with twinkly eyes and his wooden cocoa ladle over one shoulder",
         "beats": [
             ("Door twenty-four was the biggest. Rosie had opened the first door. Now she opened the last.",
              "medium shot", "ROSIE leans toward the big open door and her straw rises", "ROSIE",
              "proud and a little solemn", "tilts up", "a deep door creak and a crackling fire"),
             ("Inside stood one birthday candle. \"Tonight,\" rumbled Herschel the Walrus, \"one squid gets a lane "
              "full of light.\"",
              "medium close-up", "HERSCHEL leans down and taps the side of his nose with one flipper", "HERSCHEL",
              "jolly and conspiring", "pushes in", "a tap of a wooden ladle and a crackling fire"),
             ("Rosie's list had three lines left. Hang the last lantern. Give the signal. Say thank you.",
              "close-up", "ROSIE holds her little picture list up in front of her cup", "ROSIE",
              "ready and careful", "holds still", "a paper rustle"),
         ]},
        {"title": "Grilling for everybody", "place": "lane_dusk", "time": "night",
         "angle": "Wide establishing view with deep perspective down",
         "who": "SPICYSQUID works at his glowing grill with a pair of tongs in one curly tentacle and corn sticks "
                "in three others, grinning wide, his white headband askew; KYLE stands at the grill counter with "
                "a tall stack of empty corn sticks beside him and one paw raised to order again, cheeks full",
         "beats": [
             ("At dusk the whole valley came to Lantern Lane. SpicySquid was grilling for everybody, as always.",
              "wide shot", "SPICYSQUID flips corn on the grill with a flourish of his tongs", "SPICYSQUID",
              "busy and big-hearted", "pushes in", "a loud sizzle and a clack of tongs"),
             ("\"Spice is nice!\" he boomed. He had not sat down since the first of December.",
              "medium shot", "SPICYSQUID passes a corn stick over the counter and grabs the next one", "SPICYSQUID",
              "cheerful and tireless", "tracks beside", "a sizzle and a rattle of corn sticks"),
             ("Kyle's job was to keep him busy. Kyle ordered corn. Then more corn. Kyle loved his job.",
              "medium close-up", "KYLE raises one paw to order again while SPICYSQUID turns back to the grill",
              ["KYLE", "SPICYSQUID"], "devoted and hungry", "pushes in", "a happy munch and a sizzle"),
         ]},
        {"title": "Lantern twenty-four", "place": "lane_dusk", "time": "night",
         "angle": "Low angle looking up at the last empty hook on the lantern string above",
         "who": "PIPER flies through the air in a high leap off her glittery blue snowboard, hooking a chili-red "
                "paper lantern onto the last brass hook with both flippers; GABBY swims low over the snow "
                "carrying a wide tray hidden under a plaid blanket on her back; LINA rides on top of the "
                "blanket with a puff of white powdered sugar bursting from her corners",
         "beats": [
             ("Behind his back, Piper leaped. \"Slide into it!\" Up went lantern twenty-four, chili red.",
              "wide shot", "PIPER sails up and hooks the chili-red lantern onto the last hook", "PIPER",
              "daring and gleeful", "tilts up", "a soft swoosh and a click of a brass hook"),
             ("Gabby swam the dishes in under a blanket. Lina sugared it. \"Poof! Snow.\"",
              "medium shot", "GABBY glides low with the covered tray while LINA puffs sugar over the blanket",
              ["GABBY", "LINA"], "sneaky and pleased", "tracks beside", "a soft poof and a hush of fins"),
         ]},
        {"title": "The signal", "place": "lane_dusk", "time": "night",
         "angle": "Very low angle from the snowy ground looking up at a tiny cup on top of the cocoa cart in",
         "who": f"{ROSIE_CUP} stands alone on the roof of the cocoa cart, very small under the long row of dim "
                "lanterns, her straw wobbling, looking out over the lane",
         "beats": [
             ("Now the signal. Rosie climbed onto the cocoa cart. The whole valley looked up.",
              "wide shot", "ROSIE steps to the edge of the cart roof and looks out", "ROSIE",
              "brave and exposed", "tilts up", "a hush falling over the lane"),
             ("So many faces. Her straw wobbled.",
              "medium close-up", "ROSIE's straw wobbles side to side", "ROSIE",
              "shy and wobbly", "holds still", "a far sizzle and a held breath"),
         ]},
        {"title": "Big voice", "place": "lane_dusk", "time": "night",
         "angle": "Close view from the cocoa cart roof down to a tall green straw beside",
         "who": f"TORI stands on tiptoe on a snowy crate beside the cocoa cart, looking up with a proud steady "
                f"smile and one tiny arm raised in a fist; {ROSIE_CUP} stands on the cart roof above her, straw "
                "rising, chest full",
         "beats": [
             ("\"You've got this, little sip,\" whispered Tori. \"Big voice.\"",
              "medium close-up", "TORI lifts one tiny arm in a little fist and nods up at ROSIE", ["TORI", "ROSIE"],
              "proud and sure", "pushes in", "a soft creak of the crate"),
             ("Rosie filled her whole cup with air. \"ONE MORE LIGHT!\"",
              "medium shot", "ROSIE stretches up tall and her straw shoots straight up", "ROSIE",
              "bold and ringing", "tilts up", "a ringing echo down the lane"),
         ]},
        {"title": "Up went the lighting sticks", "place": "lane_dusk", "time": "night",
         "angle": "Wide side view along the row of dim lanterns above",
         "who": "MOM, HERSCHEL and YEHYEH stand in a row under the lantern string, each lifting a long thin "
                "lighting stick with a tiny flame toward a paper lantern, faces lit warm; YEHYEH's stick is only "
                "halfway up, and he is smiling",
         "beats": [
             ("\"ONE MORE LIGHT!\" roared the valley. Up went the long lighting sticks. Mom's. Herschel's. Yeh "
              "Yeh's, slowly.",
              "wide shot", "MOM and HERSCHEL raise their lighting sticks high while YEHYEH lifts his slowly",
              ["MOM", "HERSCHEL", "YEHYEH"], "joyful and careful", "pans right", "a thunder of stamping feet "
              "and tiny flickers"),
         ]},
        {"title": "All twenty-four", "place": "lane_lit", "time": "night",
         "angle": "Sweeping wide view with deep perspective down the whole length of",
         "who": "twenty-four paper lanterns glow in one long row, red at the near end, then purple, green, blue, "
                "orange and gold, a round white one, a sky-blue one a little crumpled, and a chili-red one last, "
                f"right above the grill; {ROSIE_CUP} stands tiny on the cocoa cart roof looking up at them with "
                "her straw high",
         "beats": [
             ("All twenty-four lanterns glowed at once. Red for the first door. Green for the wonky tree.",
              "wide shot", "ROSIE looks up as warm light spreads down the row of lanterns", "ROSIE",
              "awed and overjoyed", "pans right", "a soft rush like a held breath let go"),
             ("Round white for the longest night. Sky blue, a little crumpled. And one chili red, brand new.",
              "wide shot", "the row of lanterns sways gently and the chili-red one glows brightest", [],
              "glowing and full", "tilts up", "paper lanterns rustling and far stamping feet"),
         ]},
        {"title": "Nothing to say", "place": "lane_lit", "time": "night",
         "angle": "Close low angle past the grill counter looking up at",
         "who": "SPICYSQUID stands frozen at his grill with his head tipped all the way back, eyes huge and shiny "
                "with lantern light, mouth open, his tongs falling from one curly tentacle",
         "beats": [
             ("SpicySquid looked up. His tongs went clatter. For the first time ever, he had nothing to say.",
              "close-up", "SPICYSQUID tips his head back and his tongs drop from his tentacle", "SPICYSQUID",
              "stunned and speechless", "tilts up", "a clatter of tongs and a soft sizzle"),
             ("\"**生日快樂** (shēngrì kuàilè) = Happy birthday!\" shouted everybody. \"One lantern a day. Since the "
              "first.\"",
              "medium close-up", "SPICYSQUID blinks hard and his curly tentacles lift to his cheeks", "SPICYSQUID",
              "overwhelmed and melting", "pushes in", "a great thunder of stamping feet and clapping flippers"),
         ]},
        {"title": "He never looked up", "place": "lane_lit", "time": "night",
         "angle": "Medium view across the grill counter under the chili-red lantern in",
         "who": "SPICYSQUID throws his head back in a huge laugh with all his curly tentacles in the air, sesame "
                "seeds flying; CAT the little blue penguin stands on the grill counter with her flippers folded "
                "and a very smug grin",
         "beats": [
             ("\"Twenty-four lanterns? Over MY grill? And I never looked up?\" \"Not once,\" said Cat the penguin.",
              "medium shot", "CAT folds her flippers and shakes her head slowly at SPICYSQUID", ["CAT", "SPICYSQUID"],
              "smug and delighted", "pushes in", "a sizzle and a tiny penguin foot tap"),
             ("\"And I gave you all CORN for it!\" He laughed until his sesame seeds rattled.",
              "medium close-up", "SPICYSQUID throws his head back and shakes with laughter", "SPICYSQUID",
              "roaring with joy", "holds still", "a rattle like tiny maracas and a wheeze of steam"),
         ]},
        {"title": "Sit", "place": "lane_lit", "time": "night",
         "angle": "Low angle at chair height beside the long feast table in",
         "who": "HERSCHEL holds out a big wooden chair with a red cushion at the head of the feast table, one "
                "flipper pointing firmly at the seat; SPICYSQUID sits down on the cushion for the very first "
                "time, tentacles sticking straight out, eyes round with surprise",
         "beats": [
             ("Herschel pulled out a chair. \"Sit.\" \"I never sit,\" said SpicySquid. \"Tonight you do,\" said "
              "everybody.",
              "medium shot", "HERSCHEL points one flipper firmly at the chair beside SPICYSQUID",
              ["HERSCHEL", "SPICYSQUID"], "firm and fond", "pushes in", "a chair scrape on snow"),
             ("He sat. \"Ooh,\" said SpicySquid. \"So that's a chair. They're good.\"",
              "medium close-up", "SPICYSQUID sinks into the cushion and his tentacles slowly relax", "SPICYSQUID",
              "amazed and comfortable", "holds still", "a soft cushion puff and a creak of the chair"),
         ]},
        {"title": "A feast for the one who feeds everyone", "place": "lane_lit", "time": "night",
         "angle": "Wide view down the long feast table toward three proud cooks in",
         "who": "HERSCHEL carries a platter stacked with golden latkes; MOM carries a plate of crispy scallion "
                "pancakes with a proud smile; YEHYEH carries a steaming blue-and-white bowl of plain little white "
                "rice balls in ginger soup, walking slowly with his bamboo stick",
         "beats": [
             ("Out came the feast. Herschel's latkes. Yeh Yeh's tangyuan, round for together. Mom carried scallion "
              "pancakes.",
              "wide shot", "HERSCHEL, MOM and YEHYEH set their dishes on the long table one by one",
              ["HERSCHEL", "MOM", "YEHYEH"], "proud and generous", "pans right", "plates settling and a slow "
              "bamboo tap"),
         ]},
        {"title": "Two suspects", "place": "lane_lit", "time": "night",
         "angle": "Close view at tabletop height across a big pie with one slice missing in",
         "who": "KYLE stands at one side of the pie with crumbs on his tan muzzle and wide blameless eyes; GABBY "
                "floats at the other side with a crumb on her smile and her fins folded neatly, looking at the "
                "sky",
         "beats": [
             ("A pie with one slice missing. \"Taste-testing,\" said Kyle. \"I only bite pie,\" said Gabby. Two "
              "suspects.",
              "medium close-up", "KYLE licks a crumb off his muzzle while GABBY looks up and away", ["KYLE", "GABBY"],
              "caught and giggly", "pushes in", "a lip smack and a soft swish of fins"),
         ]},
        {"title": "The birthday noodle", "place": "lane_lit", "time": "night",
         "angle": "Wide side view down the whole length of the feast table in",
         "who": "one single very long golden noodle stretches down the lane like a ribbon toward a big bowl; "
                f"{ROSIE_CUP} holds the front end in front of her cup; LINA holds up the wobbly middle; "
                "GABBY floats along carrying her part gently in her smile; KYLE carries the tail end with both "
                "paws, licking his lips; CAT the little blue penguin glides underneath on her snowboard with "
                "both flippers up; SPICYSQUID sits at the head of the table with a big bowl, beaming",
         "beats": [
             ("Last came one very long long-life noodle, carried by everybody. Nobody broke it. Nobody bit it. Kyle.",
              "wide shot", "ROSIE takes one small careful hop forward with the front of the noodle while KYLE "
              "gazes at his end", ["ROSIE", "KYLE"], "careful and proud", "tracks beside",
              "soft shuffling steps in snow"),
             ("SpicySquid slurped it in one go. It took a while.",
              "medium shot", "SPICYSQUID slurps and slurps as the noodle slides up from the bowl", "SPICYSQUID",
              "blissful and determined", "pushes in", "one very long slurp and stamping feet"),
         ]},
        {"title": "Bonjour-hi!", "place": "lane_lit", "time": "night",
         "angle": "Medium group view at the far end of the feast table, a little red train puffing steam behind, in",
         "props": "a little red train puffing steam beyond the last stall, a long string of twenty-four glowing "
                  "paper lanterns in twenty-four colors overhead, a long feast table with a chili-red cloth, "
                  "snowy wooden stalls with striped awnings, snow-dusted fir trees",
         "who": "SESAME waves both tiny arms high with a huge grin, red tuque bobbing; COUIC stands on top of "
                "SESAME with a tiny mouth wide open in a squeak; MARGOT leans in beside them with a sweet easy "
                "smile, snow crystals sparkling; HARFANG stands behind them all with his wings half spread like "
                "a cloak, golden eyes calm",
         "beats": [
             ("Toot! The Market Train puffed in with friends from the city. Sésame, Margot, Harfang and tiny Couic.",
              "wide shot", "SESAME waves both arms while HARFANG spreads his wings behind MARGOT and COUIC",
              ["SESAME", "HARFANG", "MARGOT", "COUIC"], "merry and just in time", "pushes in",
              "a train whistle and a hiss of steam"),
             ("\"Bonjour-hi!\" called Sésame. Couic squeaked one high note. It was the start of the birthday song.",
              "medium close-up", "COUIC takes a tiny breath and squeaks on top of SESAME", ["COUIC", "SESAME"],
              "tiny and important", "tilts up", "one very small very high squeak"),
             ("\"Hoo-là-là,\" said Harfang, and danced. \"Stick with me!\" said Margot. She was stuck to his wing.",
              "medium shot", "HARFANG sways in a slow dance and lifts one wing with MARGOT stuck to its tip",
              ["HARFANG", "MARGOT"], "stately and stuck", "pans right", "a soft flap of wings and a sticky stretch"),
         ]},
        {"title": "But this is nicer", "place": "lane_lit", "time": "night",
         "angle": "Warm close view at candle height across the pie in",
         "who": "MOM holds a long thin lighting stick to one small red birthday candle standing in the pie; "
                "SPICYSQUID sits in his chair behind the candle with shiny eyes and his cheeks puffed to blow; "
                "LINA stands on the table beside the pie; KYLE sits at the table edge dusted white with sugar "
                "from ears to nose",
         "beats": [
             ("Everybody sang. Mom lit the little candle. SpicySquid blew. Off flew Lina's sugar snow, all over Kyle.",
              "medium shot", "SPICYSQUID blows out the candle and a white puff of sugar sweeps over KYLE",
              ["SPICYSQUID", "KYLE"], "surprised and giggling", "pulls back",
              "a big puff of breath and a soft poof"),
             ("SpicySquid looked down the glowing lane. \"Spice is nice,\" he said softly. \"But this is nicer.\"",
              "close-up", "SPICYSQUID looks along the lanterns and his grin goes soft", "SPICYSQUID",
              "quiet and full-hearted", "pushes in", "a soft paper rustle and a far crackle"),
         ]},
        {"title": "Thank you", "place": "lane_lit", "time": "night",
         "angle": "Tender two-shot at the head of the feast table under the chili-red lantern in",
         "who": f"{ROSIE_CUP} stands on the table edge holding her little picture list in front of her cup, the "
                "list showing plain doodles with one last empty box, looking up with shining eyes; SPICYSQUID "
                "leans down from his chair with one curly tentacle curled gently around her, eyes wet and smiling",
         "beats": [
             ("Rosie's list had one line left. She hopped up beside him.",
              "medium close-up", "ROSIE looks up at SPICYSQUID and her straw stands tall", ["ROSIE", "SPICYSQUID"],
              "brave and sincere", "pushes in", "a paper rustle and soft snow"),
             ("\"**謝謝** (xièxie) = thank you. On my first night, your grill was the one warm light.\"",
              "close-up", "ROSIE tips her straw toward the glowing grill stall", "ROSIE",
              "tender and sure", "holds still", "a soft sizzle far off"),
             ("SpicySquid hugged her with one curly tentacle. \"Then come back every winter. I'll keep it lit.\"",
              "medium close-up", "SPICYSQUID curls one tentacle gently around ROSIE and blinks hard",
              ["SPICYSQUID", "ROSIE"], "gruff and deeply touched", "pulls back", "a soft squeeze and falling snow"),
         ]},
        {"title": "Made by me", "place": "lane_lit", "time": "night",
         "angle": "Close view at cup height between two sisters at",
         "who": "TORI holds a small smooth pine straw-rest painted with blue waves in both tiny arms, an open "
                f"paper parcel and a ribbon at her feet, her eyes shiny; {ROSIE_CUP} stands close beside her "
                "with her straw wiggling, their cups touching",
         "beats": [
             ("Then Rosie gave Tori a small parcel. A pine straw-rest, painted with blue waves. \"Made by me.\"",
              "close-up", "TORI lifts the little painted straw-rest out of the paper and stares at it", "TORI",
              "surprised and moved", "pushes in", "a crinkle of paper and a slipping ribbon"),
             ("Tori could not say a word. She just leaned her cup against Rosie's. Clink.",
              "medium close-up", "TORI leans her cup gently against ROSIE and both straws tip together",
              ["TORI", "ROSIE"], "speechless and close", "holds still", "one soft clink of cups"),
         ]},
        {"title": "Snow on Christmas Eve", "place": "lane_lit", "time": "night",
         "angle": "High wide view from above the lantern string looking down the whole glowing length of",
         "who": "CAT the little blue penguin stands in the middle of the lane with her flippers on her hips and "
                f"her chest out, gazing down the row of lights; {ROSIE_CUP} stands beside her holding her little "
                "picture list in front of her cup, every doodle ticked by a little heart, straw high; KYLE stands a little way off holding one grilled corn stick up toward the stars like an "
                "offering, ears pricked; big soft snowflakes fall around them",
         "beats": [
             ("Snow fell on Christmas Eve. \"That's my home,\" said Cat. \"Told you it was good.\"",
              "wide shot", "CAT sweeps one flipper down the glowing lane and puffs out her chest", "CAT",
              "proud and happy", "pulls back", "soft snow falling and a far clink of cutlery"),
             ("Far away, up past the stars, sleigh bells jingled. Kyle left out a corn. Just in case.",
              "medium shot", "KYLE pricks his ears, then sets one corn stick down carefully in the snow", "KYLE",
              "hopeful and generous", "tilts up", "faint sleigh bells far overhead"),
             ("Twenty-four doors. Twenty-four lights. One very full squid. Rosie ticked the last line.",
              "medium close-up", "ROSIE holds her finished list in front of her cup and her straw wiggles high",
              "ROSIE", "content and complete", "tilts up", "a tiny pencil tick and soft snow"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably closed; "
                "CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, yellow scarf "
                "visible",
         "beats": [
             ("Goodnight, little sip, your list all done. Goodnight, SpicySquid, sitting down at last.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Frostpeak, twenty-four lights bright. May you always find one warm light, and be one, too.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, your list all done.",
        "Goodnight, SpicySquid, sitting down at last.",
        "Goodnight, Frostpeak, twenty-four lights bright.",
        "May you always find one warm light, and be one, too.",
    ],
}
