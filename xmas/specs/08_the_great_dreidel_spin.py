"""08 — The Great Dreidel Spin (Tuesday, December 8 · Hanukkah, fifth night)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "08",
    "slug": "the-great-dreidel-spin",
    "title": "The Great Dreidel Spin",
    "meta": [
        ("Day", "Tuesday, December 8 · door eight"),
        ("Holiday thread", "Hanukkah, the fifth night: the dreidel game, hosted by Noa"),
        ("Guests", "Noa the jelly doughnut (teaches the game), Finnegan Flipsworth ❄️ (spins himself), "
                   "Nibbles and Splash ❄️ (clap at everything)"),
        ("Cat’s role", "guide to the frozen pond, kung fu spinner, and the one who knows where Finnegan stops"),
        ("Mandarin", "陀螺 spinning top · 光明節 Hanukkah · 分享 share"),
        ("Setting", "The Door Wall, Looking-Glass Pond with a low table on the ice, Lantern Lane at night, "
                    "and the bunk room"),
    ],
    "palette": "glassy ice blue and snowy white with saturated gold foil and deep blue accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "NOA", "FINNEGAN", "NIBBLES", "SPLASH"],
    "cast_note": "Humans in this story: none. The dreidel is a small wooden four-sided spinning top; each side "
                 "shows one plain carved shape (an empty ring, a half circle, a full circle, one dot) and "
                 "nothing else. The coins are chocolate in gold foil.",
    "key_shot": 10,
    "places": {
        "door": DOORWALL,
        "pond": {
            "name": "the frozen Looking-Glass Pond below Frostpeak Lodge",
            "scene": "the frozen pond",
            "props": "a low wooden table standing on the ice under a deep-blue cloth, a little wooden spinning "
                     "top with a plain shape carved on each side, a clay pot heaped with gold-foil chocolate "
                     "coins, plump cushions on a woven mat, a round fishing hole in the ice, snowbanks and bare "
                     "silver birches along the shore",
            "light": "Bright winter sun gleams on the glassy ice",
            "accents": "gold foil and deep blue",
            "atmo": "Ice crystals glitter in the air above the pond",
            "motion": "ice crystals glitter in the air above the pond",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny wooden spinning top and one gold-foil chocolate coin on the nightstand"),
    },
    "shots": [
        {"title": "Door eight", "place": "door",
         "angle": "Wide view along the tall Door Wall in",
         "who": "NOA bounces on a wooden footstool reaching for the brass knob of one little closed door, "
                f"powdered sugar drifting off her like snow, thrilled; {ROSIE_CUP} stands on the long woven rug "
                "below with her straw wiggling",
         "beats": [
             ("Door eight was Noa's turn. Noa the jelly doughnut bounced, and powdered sugar "
              "snowed down.",
              "wide shot", "NOA bounces on the footstool and powdered sugar drifts down around her", "NOA",
              "thrilled and bouncy", "pushes in", "a crackling fire and soft little bounces"),
             ("Behind it sat a tiny wooden **陀螺** (tuóluó) = spinning top, with a shape carved on each side.",
              "medium shot", "ROSIE hops closer on the rug and her straw wiggles", "ROSIE", "curious and eager",
              "tilts up", "a tiny creak of a little door"),
         ]},
        {"title": "A dreidel!", "place": "door",
         "angle": "Close view into one open little door in",
         "who": "NOA lifts a tiny wooden spinning top out of the little open door with both tiny arms, eyes "
                f"huge with delight; {ROSIE_CUP} leans in beside her holding a blank little picture list in "
                "front of her cup",
         "beats": [
             ("\"A dreidel!\" said Noa. \"Tonight is the fifth night of **光明節** (Guāngmíng jié) = Hanukkah.\"",
              "close-up", "NOA lifts the tiny wooden top high and beams", "NOA", "proud and glowing",
              "pushes in", "a soft wooden clack"),
             ("\"Herschel lights five candles after dark. Until then, we spin!\" Rosie's straw wiggled.",
              "medium close-up", "ROSIE holds her blank list up in front of her cup and nods at NOA",
              ["ROSIE", "NOA"], "keen and organized", "pulls back", "a paper rustle and a crackling fire"),
         ]},
        {"title": "A table on the ice", "place": "pond",
         "angle": "Wide establishing view from the snowy bank across",
         "who": "CAT the little blue penguin belly-slides out onto the ice ahead of everyone with her flippers "
                f"spread, gleeful; {ROSIE_CUP} stands at the edge of the ice with her straw up and her eyes "
                "wide; MOM carries a cocoa flask and a folded blanket with a calm smile",
         "beats": [
             ("Cat the penguin led them down to the frozen pond. A low table stood on the ice.",
              "wide shot", "CAT glides across the ice on her tummy toward the low table", "CAT",
              "gleeful and at home", "tracks beside", "a long smooth swish on ice"),
             ("On it sat one wooden dreidel and a pot of chocolate coins in gold foil.",
              "medium shot", "ROSIE leans toward the glittering pot and her eyes go wide", "ROSIE",
              "dazzled", "pushes in", "a faint jingle of foil coins"),
             ("Mom brought cocoa and a blanket. \"I'll be the cheering section,\" she said.",
              "medium close-up", "MOM settles the blanket over one arm and lifts the cocoa flask in a little "
              "toast", "MOM", "calm and amused", "holds still", "a soft slosh of cocoa"),
         ]},
        {"title": "The audience arrives", "place": "pond",
         "angle": "Low angle at ice level beside the round fishing hole in",
         "who": "NIBBLES and SPLASH pop up side by side through the round fishing hole with water beading on "
                "their whiskers, clapping their flippers, overjoyed",
         "beats": [
             ("Up through a hole in the ice popped two seal pups, Nibbles and Splash.",
              "medium shot", "NIBBLES and SPLASH bob up higher in the fishing hole and blink",
              ["NIBBLES", "SPLASH"], "bright and curious", "pushes in", "a watery plop and a splash"),
             ("They clapped. Nothing had happened yet. They clapped anyway.",
              "medium close-up", "NIBBLES and SPLASH clap their wet flippers as fast as they can",
              ["NIBBLES", "SPLASH"], "overjoyed for no reason", "holds still", "fast wet flipper claps"),
         ]},
        {"title": "Four sides, four shapes", "place": "pond",
         "angle": "Close view at table height across the pot of gold coins in",
         "who": "NOA holds up the little wooden spinning top to show one carved side, an empty ring, proud and "
                f"patient; {ROSIE_CUP} holds her little picture list in front of her cup, the list showing four "
                "plain doodles of an empty ring, a half circle, a full circle and one dot, eyes fixed on the top",
         "beats": [
             ("\"Everybody gets ten coins,\" said Noa. \"Everybody puts one in the pot. Then you spin.\"",
              "medium shot", "NOA taps the rim of the clay pot and holds up the wooden top", "NOA",
              "proud and patient", "pushes in", "a soft tap on clay and a jingle of foil"),
             ("\"Empty ring: take nothing. Half circle: take half. One dot: put one in.\"",
              "close-up", "NOA turns the wooden top slowly to show each carved side", "NOA", "clear and careful",
              "holds still", "a tiny wooden click at each turn"),
             ("\"And the full circle?\" asked Rosie. Noa's eyes went huge. \"Full circle: take it all!\"",
              "medium close-up", "ROSIE points her straw at the top while NOA throws both tiny arms wide",
              ["ROSIE", "NOA"], "curious, then thrilled", "pulls back", "a jingle of foil coins"),
         ]},
        {"title": "An excellent spinner", "place": "pond",
         "angle": "Medium view across the low table in",
         "who": "FINNEGAN stands on the ice beside the table with his flippers flung wide and his chest puffed "
                "out, crest feathers quivering, wildly confident; CAT the little blue penguin watches with one "
                "flipper over her eyes",
         "beats": [
             ("\"Stand back,\" said Finnegan Flipsworth, the rockhopper penguin. \"I am an excellent spinner.\"",
              "medium shot", "FINNEGAN puffs out his chest and flings his flippers wide", "FINNEGAN",
              "wildly confident", "pushes in", "a flap of flippers and a scrape on ice"),
             ("He spun. Not the dreidel. Himself. Round and round, away across the pond.",
              "medium shot", "FINNEGAN twirls slowly on one foot and begins to slide away while CAT peeks "
              "through her flipper", ["FINNEGAN", "CAT"], "confident, then surprised", "pans right",
              "a rising whirr of feet on ice"),
         ]},
        {"title": "How do I stop?", "place": "pond",
         "angle": "High wide angle over the whole glassy sweep of",
         "who": "FINNEGAN twirls far out across the ice like a spinning top with his flippers out and his beak "
                "wide open, a spiral scratch trailing behind him on the ice; NIBBLES and SPLASH clap at the "
                "fishing hole; CAT the little blue penguin points a calm flipper at a big soft snowbank on the "
                "far shore",
         "beats": [
             ("\"WOOOHOOO—wait, how do I stop?!\" The seals clapped like mad.",
              "wide shot", "FINNEGAN twirls across the ice while NIBBLES and SPLASH clap",
              ["FINNEGAN", "NIBBLES", "SPLASH"], "thrilled and alarmed", "tracks beside",
              "a long whirring slide and fast flipper claps"),
             ("\"He stops at the snowbank,\" said Cat. \"He always stops at the snowbank.\" Poomf.",
              "medium shot", "CAT points one calm flipper as FINNEGAN lands in the soft snowbank with his feet "
              "waggling", ["CAT", "FINNEGAN"], "calm and knowing", "pans left", "a soft snowy poomf"),
         ]},
        {"title": "Round and round the table", "place": "pond",
         "angle": "Close view over the pot of gold coins in",
         "who": "TORI scoops a pile of gold coins toward herself with both tiny arms, grinning; CAT the little "
                "blue penguin stands in a gentle kung fu pose with one flipper stretched over the little "
                "spinning top; FINNEGAN, dusted head to toe in snow, drops one gold coin into the clay pot with "
                "a brave smile",
         "beats": [
             ("Tori spun first. Half circle! She scooped up half the pot.",
              "medium shot", "TORI scoops gold coins toward herself and her green straw bobs", "TORI",
              "pleased and playful", "pushes in", "a jingle of foil coins"),
             ("Cat spun with a kung fu flick. One dot. \"I meant that,\" said Cat, and paid.",
              "medium close-up", "CAT flicks the top with one flipper, then slides a coin into the pot", "CAT",
              "dignified and cheeky", "pans right", "a wooden whirr and one coin clink"),
             ("Finnegan came back covered in snow and got the dot. Then the dot. Then the dot again.",
              "medium close-up", "FINNEGAN drops a coin into the pot and snow slides off his crest", "FINNEGAN",
              "brave and baffled", "holds still", "three coin clinks and a soft plop of snow"),
         ]},
        {"title": "Rosie's turn", "place": "pond",
         "angle": "Low angle across the tabletop toward the heaped clay pot in",
         "who": f"{ROSIE_CUP} stands at the table edge holding the little wooden spinning top by its stem in "
                "front of her cup, straw wiggling, eyes huge; TORI leans in beside her with an encouraging "
                "smile, green straw tall",
         "beats": [
             ("Then it was Rosie's turn. The pot was piled high. Her list said: pinch, twist, let go.",
              "medium shot", "ROSIE lifts the little wooden top and her straw wiggles", "ROSIE",
              "nervous and excited", "pushes in", "a faint jingle of foil and a held breath"),
             ("\"You've got this, little sip,\" said Tori. Pinch. Twist. Let go!",
              "medium close-up", "TORI nods beside ROSIE as ROSIE twists the top and lets it go",
              ["TORI", "ROSIE"], "steady and encouraging", "holds still", "a quick wooden whirr"),
         ]},
        {"title": "Full circle!", "place": "pond",
         "angle": "Extreme close-up at tabletop height on",
         "who": "the little wooden spinning top lies tipped on its side with a full carved circle facing up, "
                f"gold coins spilling from the clay pot around it; {ROSIE_CUP} peers over it with her eyes wide "
                "and her straw shooting straight up; SPLASH tips backward at the fishing hole behind her with "
                "both flippers in the air while NIBBLES claps",
         "beats": [
             ("The dreidel whirled. It wobbled. It tipped over. Full circle! Rosie took the whole pot.",
              "extreme close-up", "ROSIE gasps and her straw shoots straight up", "ROSIE",
              "amazed and overjoyed", "pulls back", "a wooden clatter and a cascade of foil coins"),
             ("Gold coins everywhere! The seals clapped so hard that Splash fell back down the hole.",
              "medium shot", "SPLASH topples backward into the fishing hole while NIBBLES keeps clapping",
              ["SPLASH", "NIBBLES"], "delighted and wobbly", "pans right", "fast flipper claps and a plop"),
         ]},
        {"title": "A mountain of gold", "place": "pond",
         "angle": "Medium view down the length of the low table in",
         "who": f"{ROSIE_CUP} stands behind a tall mountain of gold coins that reaches up to her lid, eyes wide; "
                "NOA holds the empty clay pot in both tiny arms and looks around the table, expectant",
         "beats": [
             ("The dreidel loved Rosie that day. Full circle. Half. Full circle again. Her pile became a "
              "mountain.",
              "medium shot", "ROSIE peeks over the top of her mountain of coins and a few slide down", "ROSIE",
              "giddy and amazed", "tilts up", "a slithering jingle of foil coins"),
             ("\"Everybody put one in,\" said Noa. Nobody moved.",
              "medium close-up", "NOA holds out the empty clay pot and waits", "NOA", "cheerful, then puzzled",
              "holds still", "a hollow little tap on clay"),
         ]},
        {"title": "One empty wrapper", "place": "pond",
         "angle": "Close view along the bare side of the low table in",
         "who": "TORI shows two empty tiny arms with a small shrug; CAT the little blue penguin pats the bare "
                "tablecloth in front of her; FINNEGAN holds up one crumpled empty gold wrapper with a hopeful "
                "face",
         "beats": [
             ("Tori had no coins. Cat had no coins. Even Noa had none.",
              "medium shot", "TORI shrugs her empty arms while CAT pats the bare cloth", ["TORI", "CAT"],
              "good-natured and stuck", "pans right", "a soft pat on cloth"),
             ("Finnegan held up one empty wrapper. \"I have this,\" he said.",
              "medium close-up", "FINNEGAN holds the crumpled wrapper up high and smiles", "FINNEGAN",
              "hopeful", "pushes in", "a tiny foil crinkle"),
         ]},
        {"title": "No fun at all", "place": "pond",
         "angle": "Medium view past a tall mountain of gold coins in",
         "who": f"{ROSIE_CUP} leans out from behind a tall mountain of gold coins with one eye peeking and her "
                "straw tilted, puzzled; the low table stretches away quiet and bare beyond her",
         "beats": [
             ("Rosie peeked around her mountain. Nobody was spinning. Nobody was jingling.",
              "medium shot", "ROSIE leans out from behind her coins and looks along the bare table", "ROSIE",
              "puzzled", "pans right", "a hush and one coin sliding down"),
             ("\"Well, that's no fun,\" said Rosie. \"New rule! **分享** (fēnxiǎng) = share.\"",
              "medium close-up", "ROSIE hops out from behind the mountain and her straw springs up", "ROSIE",
              "brisk and bright", "pushes in", "a happy hop and a jingle of foil"),
         ]},
        {"title": "One for you", "place": "pond",
         "angle": "Close view at coin height along the tabletop in",
         "who": f"{ROSIE_CUP} pushes a neat stack of gold coins across the deep-blue cloth with both tiny arms, "
                "straw rising; TORI and CAT the little blue penguin each have a neat stack of coins in front of "
                "them and matching surprised smiles; FINNEGAN drops a gold coin into the clay pot at once, "
                "beaming",
         "beats": [
             ("She dealt out coins like a tiny banker. One for you. One for you.",
              "medium shot", "ROSIE pushes a stack of coins across the cloth and her straw lifts", "ROSIE",
              "businesslike and generous", "tracks beside", "a slide and jingle of foil coins"),
             ("Ten for Tori. Ten for Cat. Ten for Noa. Ten for Finnegan, who put one in immediately.",
              "medium close-up", "FINNEGAN drops a coin into the pot while TORI and CAT gather their stacks",
              ["FINNEGAN", "TORI", "CAT"], "surprised and delighted", "pans right",
              "one eager coin clink and happy jingling"),
         ]},
        {"title": "Two for the seals", "place": "pond",
         "angle": "Medium view from the low table toward the round fishing hole in",
         "who": "NIBBLES and SPLASH each hold one shiny gold coin between their flippers with huge astonished "
                "eyes; MOM pours steaming cocoa from her flask into a row of little cups on the table edge, "
                "smiling",
         "beats": [
             ("\"Two for the seals,\" said Rosie. \"For clapping.\" The seals were too surprised to clap.",
              "medium close-up", "NIBBLES and SPLASH stare at their gold coins with their flippers frozen",
              ["NIBBLES", "SPLASH"], "astonished and honored", "pushes in", "two tiny foil crinkles"),
             ("Mom poured cocoa all round. The whole pond smelled like chocolate.",
              "medium shot", "MOM pours cocoa into the little cups and steam curls up", "MOM",
              "cozy and content", "pans left", "a warm glug of cocoa"),
         ]},
        {"title": "The great spin", "place": "pond",
         "angle": "Dynamic low angle along the ice from the low table across",
         "who": "the little wooden spinning top skims away across the glassy ice in a blur; CAT the little blue "
                "penguin stands at the table in a huge kung fu pose with one flipper flung out and her beak "
                f"open; {ROSIE_CUP} sits on a round cushion gliding over the ice after the top with her straw streaming "
                "back; TORI slides beside her with her tiny arms out; FINNEGAN twirls far off with his flippers "
                "wide",
         "beats": [
             ("Then Cat tried her biggest kung fu flick. The dreidel shot off the table and across the ice.",
              "medium shot", "CAT holds her kung fu pose and her beak drops open", "CAT",
              "mighty, then alarmed", "pans right", "a sharp wooden whirr skating away"),
             ("\"After it!\" Everybody slipped and slid and chased. The dreidel hummed along the whole pond.",
              "wide shot", "ROSIE glides along on her cushion while TORI slides beside her", ["ROSIE", "TORI"],
              "giddy", "tracks beside", "sliding swishes and a buzzing whirr"),
             ("It passed Finnegan, who was spinning again. \"Still can't stop!\" he called happily.",
              "medium shot", "FINNEGAN twirls slowly with his flippers wide and his crest flying", "FINNEGAN",
              "cheerfully helpless", "pans left", "a flap of flippers and feet whirring on ice"),
         ]},
        {"title": "Everybody's spin", "place": "pond",
         "angle": "Close low angle at ice level beside the round fishing hole in",
         "who": "the little wooden spinning top lies on the ice beside the fishing hole with a full carved "
                "circle facing up; NIBBLES and SPLASH lean out of the hole with their noses almost touching "
                f"it; {ROSIE_CUP} sits on her round cushion beside them, out of breath, straw high; NOA bounces "
                "up behind her with both tiny arms wide",
         "beats": [
             ("At last it wobbled to a stop, right beside the fishing hole. Up popped the seals to look.",
              "close-up", "NIBBLES and SPLASH lean out and sniff the fallen top", ["NIBBLES", "SPLASH"],
              "nosy and thrilled", "pushes in", "a last wooden clatter and a watery plop"),
             ("Full circle! \"Whose spin was it?\" asked Noa. \"Everybody's,\" said Rosie. So everybody took "
              "all.",
              "medium shot", "NOA throws both tiny arms wide and ROSIE bounces on her cushion",
              ["NOA", "ROSIE"], "triumphant and silly", "pulls back",
              "fast wet flipper claps and a jingle of foil"),
         ]},
        {"title": "Lantern eight", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the long lantern string in",
         "who": "TORI stands on tiptoe on an upturned crate hooking a silver paper lantern onto the string, "
                f"careful and proud; NOA bounces in the snow below with both tiny arms up; {ROSIE_CUP} stands "
                "beside her looking up with her straw tall; CAT the little blue penguin steadies the crate with "
                "both flippers; the lodge windows glow warm far up the hill behind them",
         "beats": [
             ("They played until dusk. Then lantern eight went up on Lantern Lane, silver as a brand-new coin.",
              "wide shot", "TORI hooks the silver lantern onto the string while CAT steadies the crate",
              ["TORI", "CAT"], "careful and proud", "tilts up", "a tiny hook click and soft crunching snow"),
             ("\"One more light!\" said Noa. It was Noa's favorite thing to say.",
              "medium close-up", "NOA bounces in the snow with both tiny arms up", "NOA", "joyful",
              "pushes in", "soft bouncing crunches in snow"),
             ("Up in the lodge window, Herschel's five candles and the helper were glowing too.",
              "medium shot", "ROSIE turns to look up the hill and her straw sways gently", "ROSIE",
              "peaceful and glad", "pulls back", "soft wind and a faraway sizzle from the grill"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Warm close view across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, "
                "one flipper still out in a tiny kung fu pose, yellow scarf visible",
         "beats": [
             ("Goodnight, little top, at rest on your side. Goodnight, seal pups, all clapped out.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, five candles, and the helper too. May every game you play keep going.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little top, at rest on your side.",
        "Goodnight, seal pups, all clapped out.",
        "Goodnight, five candles, and the helper too.",
        "May every game you play keep going.",
    ],
}
