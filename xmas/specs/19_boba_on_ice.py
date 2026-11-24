"""19 — Boba on Ice (Saturday, December 19)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "19",
    "slug": "boba-on-ice",
    "title": "Boba on Ice",
    "meta": [
        ("Day", "Saturday, December 19 · door nineteen"),
        ("Holiday thread", "The winter night market: friends from Taiwan open a stand on Lantern Lane"),
        ("Guests", "Boba the tapioca pearl 🇹🇼, Bīng the shaved ice 🇹🇼, Hóng Dòu the red bean grandmother 🇹🇼, "
                   "SpicySquid"),
        ("Cat’s role", "shortcut guide and stand-builder (and the first penguin ever to snowboard down a dessert)"),
        ("Mandarin", "珍珠 pearl · 歡迎 welcome · 紅豆湯 red bean soup"),
        ("Setting", "The Door Wall in the lodge great hall, then the brand-new Boba on Ice stand on Lantern Lane, "
                    "the lane at night, and the bunk room"),
    ],
    "palette": "milk-tea tan and snowy cream with saturated cherry red and mango yellow accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "BOBA", "BING", "HONGDOU", "SPICYSQUID"],
    "cast_note": "Humans in this story: none. Boba is marble-small and bounces; Bīng is a character, and the "
                 "shaved-ice mountain he builds is ordinary ice with mango syrup. The lanterns are a surprise for "
                 "SpicySquid.",
    "key_shot": 7,
    "places": {
        "doorwall": DOORWALL,
        "stand": {
            "name": "the new striped shaved-ice stand on Lantern Lane at the Frostpeak winter market",
            "scene": "the new shaved-ice stand on Lantern Lane",
            "props": "a little wooden stand with a tan-and-cream striped awning, a big ice shaver with a crank handle, a row of "
                     "rainbow syrup bottles, a steaming copper pot of red bean soup, stacks of paper bowls, a long "
                     "string of paper lanterns overhead, a grill stall with rising steam next door",
            "light": "Bright winter daylight sparkles on the snowy lane",
            "accents": "milk-tea tan and cherry red",
            "atmo": "Soft snowflakes drift between the stalls and steam curls from the soup pot",
            "motion": "soft snowflakes drift between the stalls",
        },
        "lane_night": LANE_NIGHT,
        "bunk": bunk("a tiny glossy pearl in a saucer and a crinkled picture list drying on the nightstand"),
    },
    "shots": [
        {"title": "Door nineteen", "place": "doorwall",
         "angle": "Close view at knob height along the rows of little carved doors in",
         "who": f"{ROSIE_CUP} stands on a wooden step stool before one open little door with a single tiny glossy "
                "dark pearl resting inside it, straw perked up and eyes wide; MOM leans in beside her with a warm "
                "knowing smile",
         "beats": [
             ("Door nineteen! Rosie turned the little brass knob. Behind it sat one tiny, glossy pearl.",
              "close-up", "ROSIE leans toward the open little door and her straw springs up", "ROSIE",
              "curious and delighted", "pushes in", "a tiny door creak and a crackling fire"),
             ("\"Is that one of mine?\" Rosie checked her cup. One, two, three. \"All here.\"",
              "medium close-up", "ROSIE peers down at the three pearls in her own cup and nods", "ROSIE",
              "puzzled, then relieved", "tilts down", "a soft crackling fire"),
             ("\"A **珍珠** (zhēnzhū) = pearl,\" said Mom. \"Somebody from home is coming.\"",
              "medium shot", "MOM smiles and taps the little door frame with one tiny arm", "MOM",
              "warm and knowing", "holds still", "a soft crackling fire and a tiny tap on wood"),
         ]},
        {"title": "A list, of course", "place": "doorwall",
         "angle": "Low angle from the long woven rug looking up past the fireplace in",
         "who": f"{ROSIE_CUP} holds a little picture list in front of her cup, the list showing plain doodles of a "
                "little door, a snowy bump and a paper lantern, eyes bright; CAT the little blue penguin tucks her "
                "little snowboard under one flipper and points at the front door with a grin",
         "beats": [
             ("On the first of December, Frostpeak had felt big and strange. Now Rosie knew every corner.",
              "medium shot", "ROSIE looks around the hall and gives one proud little bounce", "ROSIE",
              "proud and at home", "pulls back", "a crackling fire and a soft creak of floorboards"),
             ("So she made a list. \"Welcome tour. Four stops. Extra marshmallows at stop three.\"",
              "medium close-up", "ROSIE lifts her little picture list high in front of her cup", "ROSIE",
              "busy and pleased", "pushes in", "a paper rustle and a crackling fire"),
             ("Cat the penguin grabbed her snowboard. \"To Lantern Lane! I know a shortcut. It's all downhill.\"",
              "medium shot", "CAT hops onto her little snowboard and points one flipper at the front door", "CAT",
              "zippy and eager", "pans right", "a snowboard clack on the floorboards"),
         ]},
        {"title": "Let's bounce!", "place": "stand",
         "angle": "Wide establishing view with deep perspective down the snowy lane toward",
         "who": "BOBA bounces high in the air above a half-unpacked wooden cart with a huge grin; HONGDOU hugs a "
                "copper soup pot far bigger than she is, her spectacles steamed up, smiling",
         "props": "a half-built wooden stand with a tan-and-cream striped awning, a wooden cart of crates and syrup "
                  "bottles, a big ice shaver with a crank handle, a copper soup pot, a long string of paper lanterns overhead, "
                  "a grill stall with rising steam next door",
         "beats": [
             ("Down on Lantern Lane, a new stand was going up. Boing! Something small bounced right over it.",
              "wide shot", "BOBA bounces up above the striped awning and comes down grinning", "BOBA",
              "bouncy and thrilled", "pushes in", "a springy boing and a creak of crates"),
             ("It was Boba the tapioca pearl, all the way from Taiwan. \"Let's bounce!\"",
              "medium shot", "BOBA lands on a crate and bounces twice in place", "BOBA",
              "cheerful and ready", "tilts up", "two rubbery bounces on wood"),
             ("Behind him came Hóng Dòu, the red bean grandmother, hugging a soup pot bigger than she was.",
              "medium shot", "HONGDOU shuffles one step with the big copper pot and peeks around it", "HONGDOU",
              "gentle and determined", "tracks beside", "a slosh of soup and soft steps in snow"),
         ]},
        {"title": "Not one drip", "place": "stand",
         "angle": "Low angle looking up from the snowy ground beside",
         "who": "BING stands in the falling snow with both tiny arms flung wide and his sunglasses pushed up, "
                "amazed and overjoyed; CAT the little blue penguin stands beside him with her snowboard and an "
                "easy shrug",
         "beats": [
             ("And Bīng, the tall shaved ice, stood very still in the falling snow. He gasped.",
              "medium shot", "BING holds out one tiny arm and watches a snowflake land on it", "BING",
              "stunned and hopeful", "tilts up", "a tinkle of ice and wind in the firs"),
             ("\"I am not dripping. Not one drip! This is THE BEST place in the whole world!\"",
              "medium close-up", "BING flings both tiny arms wide and his cherry wobbles", "BING",
              "dramatic and overjoyed", "pushes in", "a happy shiver of ice crystals"),
             ("\"Nobody melts in Frostpeak,\" said Cat. \"It's the one thing we're really good at.\"",
              "medium close-up", "CAT shrugs both flippers and pats BING on his frosty side", ["CAT", "BING"],
              "cheerful and matter-of-fact", "holds still", "a soft pat on packed snow"),
         ]},
        {"title": "Welcome, with a list", "place": "stand",
         "angle": "Close view at counter height across the wooden counter of",
         "who": f"{ROSIE_CUP} stands on the counter holding her little picture list in front of her cup, the list "
                "showing plain doodles, straw wiggling; BOBA rocks on the counter beside her with bright eyes; "
                "TORI stands behind them with a proud smile, green straw bobbing",
         "beats": [
             ("Rosie hopped onto the counter. \"**歡迎** (huānyíng) = welcome! I'm Rosie. I have a tour.\"",
              "medium close-up", "ROSIE holds her list out in front of her cup and her straw wiggles", "ROSIE",
              "brave and bubbly", "pushes in", "a paper rustle and a soft bubbling pot"),
             ("\"Stop one: the lodge, up the hill. It has a wall of little doors. No peeking.\"",
              "medium shot", "ROSIE points one tiny arm up the hill while BOBA rocks to look", ["ROSIE", "BOBA"],
              "clear and proud", "pans left", "a soft bubbling pot"),
             ("\"Stop two: the Bunny Bump. I fell down there three times.\" \"Then what?\" asked Boba.",
              "medium close-up", "BOBA leans toward ROSIE with round eager eyes", ["BOBA", "ROSIE"],
              "curious and hooked", "holds still", "a soft bubbling pot and a tiny bounce"),
         ]},
        {"title": "Then I didn't", "place": "stand",
         "angle": "Warm close two-shot under the striped awning of",
         "who": f"{ROSIE_CUP} stands tall on the counter with her straw wiggling high; BOBA bounces beside her with "
                "a huge grin",
         "beats": [
             ("\"Then I didn't,\" said Rosie. Her straw wiggled. Boba bounced. That was how Boba clapped.",
              "medium close-up", "ROSIE's straw wiggles high while BOBA bounces up and down beside her",
              ["ROSIE", "BOBA"], "proud and tickled", "pushes in", "quick rubbery bounces on the counter"),
         ]},
        {"title": "More is more!", "place": "stand",
         "angle": "Dramatic low angle looking up at a towering heap of fluffy shaved ice beside",
         "who": "BING cranks the handle of the ice shaver with both tiny arms, sunglasses flashing, delighted with "
                "himself; a mountain of plain fluffy shaved ice striped with mango syrup rises higher than the "
                "awning; CAT the little blue penguin swooshes down its side on her snowboard with both flippers up",
         "beats": [
             ("Meanwhile, Bīng had found the ice shaver. Crank, crank, crank. \"More is more!\"",
              "medium shot", "BING cranks the ice shaver and fluffy ice sprays up in an arc", "BING",
              "gleeful and unstoppable", "tilts up", "a crunchy crank and a hiss of falling ice"),
             ("His mountain grew taller than the stall. Cat snowboarded down it. Twice.",
              "wide shot", "CAT swooshes down the side of the ice mountain with both flippers up", "CAT",
              "thrilled and windblown", "tracks beside", "a long snowboard swoosh"),
             ("\"Best run in the valley,\" said Cat. \"Also the only one that tastes like mango.\"",
              "medium close-up", "CAT licks a dab of yellow syrup off her beak and nods", "CAT",
              "pleased and cheeky", "holds still", "a tiny lip smack"),
         ]},
        {"title": "Flump", "place": "stand",
         "angle": "High angle looking straight down at the wooden counter of",
         "who": f"{ROSIE_CUP} stands beside a soft fallen heap of shaved ice that covers her little picture list, the "
                "doodles running into pale puddles, her straw drooping all the way down; BING peeks over the "
                "counter edge with his sunglasses crooked and a sorry face",
         "beats": [
             ("\"Stop three,\" Rosie began. FLUMP. The top of the mountain slid off, right onto her list.",
              "medium shot", "ROSIE blinks at the soft heap of ice on her list while BING winces", ["ROSIE", "BING"],
              "startled and sorry", "tilts down", "a soft heavy flump of snow"),
             ("The pictures ran. Stop three was a puddle. \"This is THE WORST!\" wailed Bīng. Rosie's straw drooped.",
              "medium close-up", "ROSIE lifts one soggy corner of her list while BING throws both tiny arms up",
              ["ROSIE", "BING"], "dismayed and dramatic", "pushes in", "a slow drip on wood and a rattle of ice crystals"),
         ]},
        {"title": "By heart", "place": "stand",
         "angle": "Over-the-shoulder view past a tall green straw toward the long snowy lane beyond",
         "who": f"TORI bends down close with kind eyes and a small smile; {ROSIE_CUP} looks up at her and then out "
                "along the lane, her straw slowly lifting",
         "beats": [
             ("\"You have lived here nineteen whole days,\" said Tori. \"You know where the marshmallows are.\"",
              "medium close-up", "TORI bends down beside ROSIE and tips her straw toward the lane", ["TORI", "ROSIE"],
              "teasing and sure", "pushes in", "a soft bubbling pot and wind in the firs"),
             ("\"You've got this, little sip.\" Rosie looked down the lane. She did know it.",
              "medium shot", "ROSIE turns to look along the lane and her straw rises tall", "ROSIE",
              "steadier and brave", "pans right", "wind in the firs and a far clink of mugs"),
         ]},
        {"title": "The tour, by heart", "place": "stand",
         "angle": "Wide side view along the snowy lane from the counter of",
         "who": f"{ROSIE_CUP} stands on the counter pointing one tiny arm down the lane, straw high; BOBA, BING and "
                "HONGDOU line up below her in a row, all looking where she points with bright curious faces",
         "beats": [
             ("\"Stop three! Herschel's cocoa cart. Ask for extra marshmallows. He always says yes.\"",
              "medium shot", "ROSIE points one tiny arm down the lane and BOBA bounces to see", ["ROSIE", "BOBA"],
              "bright and sure", "pans right", "a far clink of mugs"),
             ("\"Stop four is the warmest spot in the valley. The Squid Grill. You'll smell it first.\"",
              "medium close-up", "HONGDOU sniffs the air and smiles while ROSIE nods", ["HONGDOU", "ROSIE"],
              "hungry and happy", "pans left", "a sizzle from the grill next door"),
         ]},
        {"title": "Spice is nice!", "place": "stand",
         "angle": "Low angle from the snowy ground looking up at the counter of",
         "who": "SPICYSQUID leans over from the grill stall next door holding out grilled corn on sticks in his "
                "curly tentacles, grinning wide; HONGDOU ladles steaming red bean soup into a paper bowl with her "
                "tiny wooden ladle, her spectacles steamed up; MOM holds a corn stick in one tiny arm and a soup bowl in the "
                "other, smiling",
         "beats": [
             ("\"Spice is nice!\" boomed SpicySquid, everybody's favorite, handing out corn. \"A little heat keeps "
              "the cold away!\"",
              "medium shot", "SPICYSQUID holds out a fan of grilled corn sticks with a booming grin", "SPICYSQUID",
              "big-hearted and loud", "pushes in", "a sizzle of the grill and a crackle of corn"),
             ("Hóng Dòu ladled hot **紅豆湯** (hóngdòu tāng) = red bean soup. \"Everyone needs a little sweetness.\"",
              "close-up", "HONGDOU pours a ladle of steaming soup into a paper bowl", "HONGDOU",
              "warm and nurturing", "tilts down", "a soft pour and a bubbling pot"),
             ("Spicy corn in one hand, sweet soup in the other. \"The perfect lunch,\" said Mom.",
              "medium close-up", "MOM lifts the corn and then the soup bowl and sighs happily", "MOM",
              "content and amused", "holds still", "a crunch of corn and a bubbling pot"),
         ]},
        {"title": "Who keeps hanging these?", "place": "stand",
         "angle": "Upward view past curly tentacles at the long lantern string above",
         "who": "SPICYSQUID tips his head back and points one curly tentacle up at the row of paper lanterns, "
                f"puzzled and counting; {ROSIE_CUP} stands frozen on the counter with wide eyes; BOBA rocks beside "
                "her with one eye shut in a wink",
         "beats": [
             ("Then SpicySquid looked up. \"Funny. Sixteen, seventeen, eighteen lanterns. Who keeps hanging these?\"",
              "medium shot", "SPICYSQUID points a curly tentacle at one lantern after another", "SPICYSQUID",
              "puzzled and curious", "tilts up", "paper lanterns rustling in the breeze"),
             ("Uh-oh. The lanterns were a surprise for him! Rosie looked at Boba. Boba winked.",
              "medium close-up", "ROSIE glances sideways at BOBA and BOBA winks back", ["ROSIE", "BOBA"],
              "alarmed, then hopeful", "pushes in", "a sizzle from the grill and a creak of the counter"),
         ]},
        {"title": "A bouncing distraction", "place": "stand",
         "angle": "Dynamic diagonal view from the striped awning down to the cocoa cart beside",
         "who": "BOBA sails through the air in a high bounce above the awning with a huge grin; SPICYSQUID watches "
                "with his head tipped back and his mouth open in a laugh; BING stands beside his ice mountain "
                "with both tiny arms up like a goalpost",
         "beats": [
             ("Boing! Off the awning. Boing! Off the cocoa cart. Boing! Off the tip-top of Bīng's mountain.",
              "wide shot", "BOBA bounces from the awning high into the air above BING", ["BOBA", "BING"],
              "daring and gleeful", "pans right", "three springy boings and a rattle of mugs"),
             ("SpicySquid watched every bounce. \"Ha! Now that deserves corn!\" He forgot all about counting.",
              "medium shot", "SPICYSQUID throws back his head and laughs, waving a corn stick", "SPICYSQUID",
              "delighted and distracted", "pushes in", "a sizzle of the grill and a springy boing"),
         ]},
        {"title": "Open for business", "place": "stand",
         "angle": "Medium view framed by the striped awning of",
         "who": "BING holds up a paper bowl of fluffy mango shaved ice like a trophy; HONGDOU stirs her copper pot "
                f"with a soft smile; {ROSIE_CUP} stands on the counter holding a fresh little card with one plain "
                "doodle of a striped stand and a small heart beside it, straw wiggling",
         "beats": [
             ("By afternoon the stand was open. Bīng served mango snow. Hóng Dòu served soup. Boba served bounces.",
              "medium shot", "BING lifts a bowl of mango ice high while HONGDOU stirs her pot", ["BING", "HONGDOU"],
              "busy and proud", "pulls back", "a crunchy crank and a bubbling pot"),
             ("Rosie started a new tour list. Stop one: Boba on Ice. Extra mango at stop one.",
              "close-up", "ROSIE holds her fresh little card in front of her cup and her straw wiggles", "ROSIE",
              "proud and content", "pushes in", "a tiny pencil scratch"),
         ]},
        {"title": "The best part", "place": "lane_night", "time": "night",
         "angle": "Low angle looking up at the long lantern string above",
         "who": "MOM reaches up beside a softly glowing milk-tea tan paper lantern with dark round dots, one tiny "
                f"arm steadying it on its hook, smiling; {ROSIE_CUP} stands on a snowy crate below with her straw "
                "high; BOBA, BING and HONGDOU look up in a row, their faces lit warm",
         "beats": [
             ("That night Rosie showed her new friends the best part. A lantern, milk-tea tan with dark dots.",
              "medium shot", "ROSIE looks up at the dotted lantern and her straw rises", "ROSIE",
              "eager and proud", "tilts up", "soft footsteps in snow and a far sizzle"),
             ("Mom lit it and hung it high. It glowed like a warm cup of bubble tea.",
              "medium close-up", "MOM steadies the glowing lantern on its hook and lets go gently", "MOM",
              "calm and careful", "pushes in", "a soft paper rustle"),
             ("\"Now we say it,\" whispered Rosie. \"One more light,\" said Boba, Bīng and Hóng Dòu.",
              "medium shot", "BOBA, BING and HONGDOU all gaze up at the lantern and BOBA gives one small bounce",
              ["BOBA", "BING", "HONGDOU"], "hushed and glad", "pulls back", "a soft paper rustle and one tiny boing"),
         ]},
        {"title": "Nineteen", "place": "lane_night", "time": "night",
         "angle": "Wide view down the glowing lane toward the grill stall in",
         "who": "SPICYSQUID hums over his glowing grill with a corn stick in each curly tentacle, eyes on his work; "
                "CAT the little blue penguin stands in the snow nearby with one flipper over her beak, giggling; "
                "TORI stands beside her looking up at the lanterns with a soft smile",
         "beats": [
             ("Nineteen lanterns. At his grill, SpicySquid hummed and flipped corn. He did not look up once.",
              "wide shot", "SPICYSQUID flips two corn sticks and hums while CAT hides a giggle behind her flipper",
              ["SPICYSQUID", "CAT"], "busy and unsuspecting", "pans left", "a sizzle of the grill and a soft hum"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably closed; "
                "CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, yellow scarf "
                "visible",
         "beats": [
             ("Goodnight, little sip, who knows the way. Goodnight, new friends, warm in the snow.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Cat, the best run is done. May all your dreams taste like mango snow.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, who knows the way.",
        "Goodnight, new friends, warm in the snow.",
        "Goodnight, Cat, the best run is done.",
        "May all your dreams taste like mango snow.",
    ],
}
