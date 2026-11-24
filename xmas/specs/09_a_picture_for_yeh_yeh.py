"""09 — A Picture for Yeh Yeh (Wednesday, December 9 · Market Train to Montreal)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "09",
    "slug": "a-picture-for-yeh-yeh",
    "title": "A Picture for Yeh Yeh",
    "meta": [
        ("Day", "Wednesday, December 9 · door nine · the first Market Train day trip"),
        ("Holiday thread", "Holiday post from the big Christmas market in downtown Montreal"),
        ("Guests", "Sésame the Montreal bagel ⚜️ (new; Noa's cousin and a born tour guide), Whistlewick ❄️ "
                   "(the train's mail fox), Lina the snowflake crisp"),
        ("Cat’s role", "explains the Market Train, tries on a mitten, and reaches under the stalls as far as "
                       "a flipper goes"),
        ("French", "Bonjour-hi, the Montreal hello · merci, thank you"),
        ("Mandarin", "爺爺 grandpa · 想你 I miss you"),
        ("Setting", "The Door Wall, the mail car of the Market Train, the big Christmas market in downtown "
                    "Montreal, Lantern Lane at night, and the bunk room"),
    ],
    "palette": "snowy white and warm honey gold with saturated mailbox red and fir green accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "SESAME", "WHISTLEWICK", "LINA"],
    "cast_note": "Humans in this story: none. Tickets, picture cards, the mailbox and the stalls show plain "
                 "little pictures only. Sésame faces the camera in every still, even tipped up on his edge "
                 "like a wheel.",
    "key_shot": 14,
    "places": {
        "door": DOORWALL,
        "train": {
            "name": "the mail car of the Market Train",
            "scene": "the Market Train mail car",
            "props": "a wall of little wooden pigeonholes stuffed with envelopes, sacks of parcels tied with "
                     "string, red plush benches, a brass luggage rack, a swinging brass lamp, round windows "
                     "with snowy pines rushing past",
            "light": "Snowy daylight streams through the round windows",
            "accents": "plush red and brass gold",
            "atmo": "Envelopes tremble in their pigeonholes with the rattle of the rails",
            "motion": "the envelopes tremble with the rattle of the rails",
        },
        "market": {
            "name": "the big Christmas market in downtown Montreal",
            "scene": "the Montreal Christmas market",
            "props": "rows of little wooden chalet stalls with snowy peaked roofs, a giant decorated fir tree, "
                     "a wood-fired bagel oven stall with a glowing brick oven mouth, a bright red mailbox on "
                     "a post, strings of unlit round bulbs overhead, a skating rink beyond the stalls",
            "light": "Crisp bright winter daylight sparkles on the snowy square",
            "accents": "mailbox red and honey gold",
            "atmo": "Woodsmoke curls up from the bagel oven",
            "motion": "woodsmoke curls up from the bagel oven",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny golden train ticket and a stub of pink crayon on the nightstand"),
    },
    "shots": [
        {"title": "Door nine", "place": "door",
         "angle": "Close low angle at knob height on one open little door in",
         "who": f"{ROSIE_CUP} stands on a wooden footstool holding a tiny golden train ticket in front of her "
                "cup, the ticket plain and shiny with one small picture of a train on it, eyes wide; CAT the "
                "little blue penguin bounces beside the footstool with both flippers up, thrilled",
         "beats": [
             ("Door nine was Rosie's turn. Inside sat something flat and shiny: a tiny golden train ticket.",
              "close-up", "ROSIE lifts the tiny golden ticket and it glints in the firelight", "ROSIE",
              "surprised and curious", "pushes in", "a tiny door creak and a crackling fire"),
             ("\"The Market Train!\" said Cat the penguin. \"It runs to the city for the day. Home by dark.\"",
              "medium shot", "CAT bounces with both flippers up beside ROSIE", ["CAT", "ROSIE"],
              "thrilled and in the know", "pulls back", "happy penguin foot taps"),
         ]},
        {"title": "Some of today", "place": "door",
         "angle": "Medium close two-shot beside the crackling stone fireplace in",
         "who": f"{ROSIE_CUP} stands with her straw drooping, looking at the tiny golden ticket she holds in "
                "front of her cup; MOM bends close beside her with kind warm eyes and one tiny arm resting "
                "on the ticket",
         "beats": [
             ("A train. Yeh Yeh loved trains. Rosie's straw drooped. She missed her **爺爺** (yéye) = grandpa.",
              "medium close-up", "ROSIE looks down at the ticket and her straw droops", "ROSIE",
              "wistful", "pushes in", "a soft crackling fire"),
             ("\"Then let's send him some of today,\" said Mom. Rosie's straw came halfway back up.",
              "medium shot", "MOM taps the ticket gently and ROSIE's straw lifts halfway", ["MOM", "ROSIE"],
              "tender and hopeful", "holds still", "a soft crackling fire"),
         ]},
        {"title": "The mail fox", "place": "train",
         "angle": "Wide view down the swaying aisle of",
         "who": "WHISTLEWICK sorts envelopes into the little wooden pigeonholes with a blur of quick paws, brass "
                f"whistle swinging on its cord, sharp and busy; {ROSIE_CUP} sits on the edge of a red plush "
                "bench watching him with round eyes",
         "beats": [
             ("The Market Train puffed south through snowy pines. In the mail car rode Whistlewick, the "
              "arctic fox.",
              "wide shot", "WHISTLEWICK flicks an envelope into a pigeonhole and his tail swishes",
              "WHISTLEWICK", "sharp and busy", "tracks beside", "a steady clickety-clack of rails"),
             ("He sorted letters at top speed. Zip, zip, zip. He never talked. He whistled.",
              "medium shot", "WHISTLEWICK slots three envelopes in a row while ROSIE's eyes follow each one",
              ["WHISTLEWICK", "ROSIE"], "brisk and impressive", "pans right",
              "three quick paper zips and a short bright whistle"),
         ]},
        {"title": "Montreal!", "place": "market",
         "angle": "Wide establishing view with deep perspective down the snowy rows of",
         "who": f"{ROSIE_CUP} stands tiny at the entrance of the market with her straw straight up; CAT the "
                "little blue penguin points ahead with one flipper; TORI gazes up at the giant fir with her "
                "green straw tipped back; MOM follows with a calm smile",
         "beats": [
             ("Montreal! Rows of little wooden houses, a fir tree tall as a hill, and the smell of baking.",
              "wide shot", "ROSIE turns slowly to take it all in and her straw stands straight up", "ROSIE",
              "dazzled", "tilts up", "soft crunching snow and a faraway bell"),
             ("Bells rang. Skates swished. Everything sparkled.",
              "medium shot", "TORI tips her green straw back to look all the way up the giant fir", "TORI",
              "wide-eyed", "tilts up", "bells and a swish of skates far off"),
         ]},
        {"title": "Bonjour-hi!", "place": "market",
         "angle": "Low angle looking up at the glowing bagel oven stall in",
         "who": "SESAME bounces out of the bagel oven stall facing the camera with both tiny arms flung wide "
                f"and his red tuque bobbing, bright and welcoming; {ROSIE_CUP} looks up at him with a surprised "
                "smile, her little picture list held in front of her cup",
         "beats": [
             ("Out bounced a small bagel in a red hat. \"**Bonjour-hi** (bohn-ZHOOR hi) = hello, the Montreal "
              "way!\"",
              "medium shot", "SESAME bounces forward and flings both tiny arms wide", "SESAME",
              "bright and welcoming", "pushes in", "a springy bounce and an oven crackle"),
             ("\"I'm Sésame. Wood-fired, honey-boiled, smaller and sweeter than other bagels. On purpose.\"",
              "medium close-up", "SESAME pats his seedy side proudly and tips his tuque", "SESAME",
              "proud and merry", "holds still", "a tiny pat and an oven crackle"),
             ("\"You must be Rosie. My cousin Noa said to look for a cup with a list.\"",
              "medium shot", "SESAME points at the list and ROSIE lifts it a little higher", ["SESAME", "ROSIE"],
              "friendly and tickled", "pulls back", "a paper rustle"),
         ]},
        {"title": "The tour", "place": "market",
         "angle": "Medium view along a stall hung with woolly mittens in",
         "who": "CAT the little blue penguin stands inside one enormous red mitten that covers her up to her "
                "chin, very pleased; SESAME points one tiny arm along the row like a tour guide, facing the "
                "camera; LINA hops along the snowy stall roof above them with a puff of white powdered sugar "
                "bursting off her corners",
         "beats": [
             ("Sésame showed them everything. The giant tree. The skating rink. Forty kinds of mittens.",
              "medium shot", "SESAME sweeps one tiny arm along the row of mittens", "SESAME",
              "quick and proud", "tracks beside", "soft crunching snow and a faraway bell"),
             ("Cat tried one mitten. It fit all of her. \"Perfect,\" said Cat. \"A sleeping bag.\"",
              "medium close-up", "CAT wriggles deeper into the big red mitten until only her beak shows",
              "CAT", "snug and smug", "pushes in", "a woolly rustle"),
             ("Lina hopped along the rooftops. Poof! \"A little extra snow. You're welcome, Montreal.\"",
              "medium shot", "LINA hops along the stall roof and a white puff of sugar drifts down", "LINA",
              "generous and pleased with herself", "tilts up", "a soft poof"),
         ]},
        {"title": "The red mailbox", "place": "market",
         "angle": "Low angle looking up at the bright red mailbox in",
         "who": "SESAME stands beside the bright red mailbox patting its post with one tiny arm, facing the "
                "camera, proud, the plain red front of the mailbox showing one small picture of an envelope; "
                f"{ROSIE_CUP} gazes up at the mailbox with her straw shooting straight up and her eyes shining",
         "beats": [
             ("Last came a bright red mailbox. \"Cards go in,\" said Sésame. \"They come out anywhere in the "
              "world.\"",
              "medium shot", "SESAME pats the mailbox post and nods up at the slot", "SESAME",
              "matter-of-fact and proud", "tilts up", "a hollow metal pat"),
             ("\"The mail fox empties it at noon. Sharp.\" Rosie's straw shot up. Yeh Yeh!",
              "medium close-up", "ROSIE's straw shoots straight up and she gives a little hop", "ROSIE",
              "an idea arriving", "pushes in", "one happy hop in snow"),
         ]},
        {"title": "A picture card", "place": "market",
         "angle": "High angle looking down on a snowy barrel top in",
         "who": f"{ROSIE_CUP} stands on a barrel top holding a stub of pink crayon in front of her cup, a "
                "picture card at her feet showing plain crayon doodles of little houses, a tall fir tree, a "
                "round bagel in a hat and one small heart, her straw wiggling with concentration",
         "beats": [
             ("Rosie drew Yeh Yeh a picture card. The market. The giant tree. A bagel in a hat.",
              "medium shot", "ROSIE leans over the card with her crayon and her straw wiggles", "ROSIE",
              "busy and tender", "pushes in", "soft crayon scratches"),
             ("At the bottom she drew a heart. That meant **想你** (xiǎng nǐ) = I miss you.",
              "close-up", "ROSIE presses the crayon down for one last careful stroke and leans back", "ROSIE",
              "full of feeling", "holds still", "one slow crayon stroke"),
         ]},
        {"title": "The potato swan", "place": "market",
         "angle": "Close view across the snowy barrel top in",
         "who": "TORI holds up a picture card showing a lumpy round crayon doodle with a long neck, proud and "
                "a little unsure; CAT the little blue penguin squints at it with her head tilted and one "
                "flipper on her chin",
         "beats": [
             ("Tori drew one too. \"It's a swan,\" she said. \"It's a potato,\" said Cat.",
              "medium close-up", "TORI holds her card up while CAT tilts her head the other way",
              ["TORI", "CAT"], "proud and doubtful", "pushes in", "a paper flap"),
             ("\"It's a potato swan,\" said Tori. \"Yeh Yeh will know.\"",
              "medium close-up", "TORI hugs the card to her cup and lifts her chin", "TORI",
              "dignified and fond", "holds still", "a paper rustle"),
         ]},
        {"title": "Whoosh", "place": "market",
         "angle": "Dynamic low angle along the snowy ground toward the red mailbox in",
         "who": f"{ROSIE_CUP} hops forward with both tiny arms stretched out and her eyes wide, a picture card "
                "tumbling away from her on a gust of wind toward the shadowy gap under a wooden chalet stall",
         "beats": [
             ("Bong! The noon bells began. Rosie hopped for the mailbox. Whoosh! The wind snatched her card.",
              "medium shot", "ROSIE hops forward and the card lifts out of her tiny arms", "ROSIE",
              "hurrying, then startled", "tracks beside", "a deep bell and a gust of wind"),
             ("It skittered over the snow and slid under the little wooden houses. Gone.",
              "wide shot", "ROSIE stops short with her arms out as the card slides out of sight", "ROSIE",
              "dismayed", "pans right", "a papery skitter and a deep bell"),
         ]},
        {"title": "Not this", "place": "market",
         "angle": "Ground-level view looking out from the shadowy gap under a chalet stall in",
         "who": f"{ROSIE_CUP} peers into the low gap with her straw tilted, snow up to her tiny feet; CAT the "
                "little blue penguin lies on her tummy beside her stretching one short flipper as far in as it "
                "will go, cheek squashed on the snow",
         "beats": [
             ("Rosie peeked under. Dark and low. Cat reached in. \"My flipper is perfect for many things. Not "
              "this.\"",
              "medium shot", "CAT stretches her flipper into the gap and pats around in the snow", "CAT",
              "determined and squashed", "pushes in", "soft patting on snow and a deep bell"),
             ("Bong, bong went the bells. \"Help!\" called Rosie. \"My card for Yeh Yeh went under!\"",
              "medium close-up", "ROSIE stands up tall and her straw points straight up", "ROSIE",
              "urgent and loud for a small cup", "tilts up", "two deep bells and one hop in snow"),
         ]},
        {"title": "One sharp whistle", "place": "market",
         "angle": "Medium view down the row of chalet stalls in",
         "who": "WHISTLEWICK crouches low at the gap under the stall with his brass whistle in his mouth and "
                f"his fluffy tail high, ready to spring; {ROSIE_CUP} stands in the snow behind him with her "
                "straw straight up, watching",
         "beats": [
             ("One sharp whistle. TWEEET! A white blur shot under the stalls. That was Whistlewick.",
              "medium shot", "WHISTLEWICK springs low into the gap and his fluffy tail whisks after him",
              "WHISTLEWICK", "fast and sure", "pans left", "one sharp bright whistle and a whisk of snow"),
             ("Out the far side popped the card, sliding away down the icy lane.",
              "wide shot", "ROSIE swings round to look down the row and her straw swings with her", "ROSIE",
              "hopeful, then alarmed", "pans right", "a papery slide on ice and a deep bell"),
         ]},
        {"title": "I'm a bagel", "place": "market",
         "angle": "Low angle along the icy lane between the stalls in",
         "who": "SESAME stands tipped up on his round edge like a wheel, facing the camera with a fearless grin "
                "and his red tuque pulled down tight; a picture card slides away across the ice behind him; "
                "a long loop of gold tinsel trails from the giant decorated fir nearby",
         "beats": [
             ("\"Stand back,\" said Sésame. \"I'm a bagel.\" He tipped onto his side and rolled like a wheel.",
              "medium shot", "SESAME tugs his tuque down tight and rocks once on his edge", "SESAME",
              "fearless and thrilled", "pushes in", "a soft rumble on packed snow"),
             ("He rolled past the mittens and twice around the giant tree, picking up tinsel.",
              "wide shot", "SESAME bounces fast along the lane, face forward, with gold tinsel fluttering after him",
              "SESAME", "gleeful", "tracks beside", "a rolling rumble and a tinsel rustle"),
         ]},
        {"title": "Across the rink", "place": "market",
         "angle": "Wide dynamic view across the skating rink at the edge of",
         "who": "SESAME glides across the empty ice, scored with fresh blade lines, tipped up on his round edge, "
                "facing the camera, wrapped in a loop of gold tinsel, grinning; LINA rides on top of him with her tiny arms out and a trail of "
                "white powdered sugar streaming behind her; WHISTLEWICK races alongside with his brass whistle "
                "in his mouth and his tail flying",
         "beats": [
             ("He rolled across the skating rink, calling \"Bonjour-hi!\" Lina hopped on for the ride. Poof!",
              "wide shot", "SESAME glides over the ice while LINA rides on top with her arms out",
              ["SESAME", "LINA"], "giddy", "tracks beside", "a smooth rumble on ice and a soft poof"),
             ("Whistlewick ran beside him, whistling the turns. Left! Right! Mind the snowman!",
              "medium shot", "WHISTLEWICK races alongside with his whistle in his mouth and his tail flying",
              "WHISTLEWICK", "keen and bossy", "pans right", "three short bright whistles"),
         ]},
        {"title": "What the hole is for", "place": "market",
         "angle": "Close view beneath the giant decorated fir in",
         "who": "SESAME sits in the snow facing the camera with a picture card caught neatly in the round hole "
                "in his middle like a letter in a slot, tuque crooked, draped in gold tinsel, dizzy and "
                f"delighted; {ROSIE_CUP} hops toward him with her straw high",
         "beats": [
             ("Bump! The card flew up, flipped twice, and landed neatly in his hole.",
              "medium shot", "SESAME sways dizzily with the card held snug in his middle", "SESAME",
              "dizzy and delighted", "pushes in", "a soft thump in snow and a paper flutter"),
             ("\"That,\" said Sésame, \"is what the hole is for.\"",
              "medium close-up", "SESAME straightens his tuque and beams as ROSIE hops closer",
              ["SESAME", "ROSIE"], "smug and kind", "holds still", "a happy hop in snow"),
         ]},
        {"title": "Clunk", "place": "market",
         "angle": "Close low angle at the slot of the bright red mailbox in",
         "who": f"{ROSIE_CUP} stands on a snowy crate pushing a picture card into the slot of the red mailbox "
                "with both tiny arms; WHISTLEWICK waits below with his little red mail satchel held open, one "
                "eye closed in a wink",
         "beats": [
             ("On the last bong, Rosie posted her card. Clunk. Whistlewick tucked it into his satchel.",
              "close-up", "ROSIE pushes the card through the slot and it drops inside", "ROSIE",
              "relieved and proud", "pushes in", "a deep last bell and a hollow clunk"),
             ("\"**Merci** (mehr-SEE) = thank you!\" said Rosie. The fox winked. That was plenty.",
              "medium shot", "WHISTLEWICK pats his satchel shut and winks up at ROSIE", ["WHISTLEWICK", "ROSIE"],
              "brisk and kind", "pans left", "a satchel buckle click"),
         ]},
        {"title": "Now he'll know", "place": "market",
         "angle": "Warm close view beside the bright red mailbox in",
         "who": f"TORI leans close to ROSIE with a soft smile, green straw tilted toward her; {ROSIE_CUP} looks "
                "up at the mailbox with her straw gently raised; MOM holds out a paper cone of roasted "
                "chestnuts with steam curling up; SESAME holds up a folded pink paper lantern in both tiny "
                "arms, facing the camera, beaming",
         "beats": [
             ("Tori posted her potato swan. \"I miss him too, little sip,\" she said. \"Now he'll know.\"",
              "medium close-up", "TORI leans in against ROSIE and they both look up at the mailbox",
              ["TORI", "ROSIE"], "tender and close", "pushes in", "a hollow clunk and soft wind"),
             ("Mom bought roasted chestnuts. They ate them under the giant tree, warm to their "
              "straws.",
              "medium shot", "MOM holds out the paper cone and steam curls up from the chestnuts", "MOM",
              "cozy and content", "pans right", "a paper crinkle and a faraway bell"),
             ("Sésame handed them a pink paper lantern. \"For your lane,\" he said. \"Come back soon!\"",
              "medium shot", "SESAME holds the folded pink lantern up high with both tiny arms", "SESAME",
              "generous and bright", "pulls back", "a crinkle of paper"),
         ]},
        {"title": "Lantern nine", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the long lantern string in",
         "who": "CAT the little blue penguin stands on a snowy barrel hooking a pink paper lantern onto the "
                f"string, careful and proud; {ROSIE_CUP} stands below looking up with her straw tall; LINA hops "
                "beside her in the lantern light; MOM stands behind them with a calm smile",
         "beats": [
             ("The train had them home by dark. On Lantern Lane, Cat hung the pink lantern from Montreal.",
              "wide shot", "CAT hooks the pink lantern onto the string while LINA hops below", ["CAT", "LINA"],
              "careful and proud", "tilts up", "a tiny hook click and soft crunching snow"),
             ("\"One more light,\" said Rosie. Far away, a card was riding toward a round old teapot.",
              "medium close-up", "ROSIE gazes up at the pink glow and MOM nods softly behind her",
              ["ROSIE", "MOM"], "content and hopeful", "pulls back", "soft wind and a faraway train whistle"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Warm close view across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep curled inside one big red mitten at the foot of "
                "the bunk, yellow scarf visible",
         "beats": [
             ("Goodnight, little card, on your way tonight. Goodnight, Sésame, round as a wheel.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Yeh Yeh, far away and loved. Sleep well. Good things are in the mail.",
              "medium close-up", "CAT settles deeper into her mitten with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little card, on your way tonight.",
        "Goodnight, Sésame, round as a wheel.",
        "Goodnight, Yeh Yeh, far away and loved.",
        "Sleep well. Good things are in the mail.",
    ],
}
