"""01 — The First Door (Tuesday, December 1)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

# Day one: the string over the lane starts out bare, then holds exactly one lantern.
LANE_REST = ("snowy wooden stalls with striped awnings, a glowing grill stall with rising steam, a cocoa cart, "
             "snow-dusted fir trees, footprints in the snow")
LANE_BARE = "a long bare lantern string overhead, " + LANE_REST
LANE_ONE = "a long string overhead with one glowing red paper lantern, " + LANE_REST

STORY = {
    "num": "01",
    "slug": "the-first-door",
    "title": "The First Door",
    "meta": [
        ("Day", "Tuesday, December 1"),
        ("Holiday thread", "Arriving at Frostpeak; the first door and the first lantern"),
        ("Guests", "Herschel the Walrus ❄️ (new), Piper Paddlefoot ❄️, SpicySquid (new), Kyle the black bear cub"),
        ("Cat’s role", "the one who is home: belly-slides off the train, hugs a lamppost, and is the top of the "
                       "ladder that hangs lantern one"),
        ("Mandarin", "雪 snow · 家 home · 燈籠 lantern"),
        ("Setting", "The snow train heading north past Montreal and Quebec City, Frostpeak Station platform, "
                    "the great hall of Frostpeak Lodge with its Door Wall, Lantern Lane at night, and the lodge "
                    "bunk room"),
    ],
    "palette": "snowy white and soft sky blue with saturated train red and warm lantern orange accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "HERSCHEL", "PIPER", "SPICYSQUID", "KYLE"],
    "cast_note": "Humans in this story: none. The lantern string over the lane is bare until the red lantern goes "
                 "up, then holds exactly one lantern.",
    "key_shot": 9,
    "places": {
        "train": {
            "name": "a cozy carriage of the little red snow train",
            "scene": "the cozy train carriage",
            "props": "a wide frosted train window, red velvet seats, a brass luggage rack of striped suitcases, "
                     "a little folding table with a cocoa flask, a tasseled window blind, a grand old castle "
                     "hotel with steep green copper roofs on a snowy cliff sliding past outside",
            "light": "Pale early sun glows through the frosted window",
            "accents": "velvet red and copper green",
            "atmo": "Snowflakes streak past the glass",
            "motion": "snowflakes streak past the window",
        },
        "station": {
            "name": "the snowy platform of Frostpeak Station",
            "scene": "the snowy station platform",
            "props": "a little red snow train puffing white steam, a wooden clock tower with a carved snowflake "
                     "face, a brass luggage cart of striped suitcases, a row of ice-blue lampposts, a rack of "
                     "wooden sleds, tall white peaks beyond the station roof",
            "light": "Bright morning sun bounces off the fresh snow",
            "accents": "train red and glacier blue",
            "atmo": "Puffs of white steam roll across the platform and tiny snow crystals glitter",
            "motion": "puffs of white steam roll across the platform",
        },
        "hall": DOORWALL,
        "lane": LANE_NIGHT,
        "bunk": bunk("a little picture list with two tiny ticks and a train ticket punched with a snowflake on "
                     "the nightstand"),
    },
    "shots": [
        {"title": "North", "place": "train",
         "angle": "Close view from the red velvet seat toward the wide frosted window of",
         "who": f"{ROSIE_CUP} stands on the red velvet seat with her dome lid pressed against the glass and her "
                "straw tipped up, eyes huge, watching the castle roofs go by",
         "beats": [
             ("The snow train puffed north, past the lights of Montreal and the castle roofs of Quebec City.",
              "medium close-up", "ROSIE presses her lid closer to the glass and her straw tips up", "ROSIE",
              "wide-eyed and wondering", "holds still", "a steady clickety-clack of train wheels"),
         ]},
        {"title": "The snow train", "place": "station",
         "angle": "Wide establishing view with deep perspective along",
         "who": f"{ROSIE_CUP} stands in the open doorway of the little red train holding a little picture list in "
                "front of her cup, eyes wide; MOM stands just behind her with one tiny arm resting on a striped "
                "suitcase, smiling calmly",
         "beats": [
             ("Chuff, chuff, hisssss. It stopped at Frostpeak Station. It was December the first.",
              "wide shot", "ROSIE peeks out of the train doorway and her straw tips forward", "ROSIE",
              "curious and careful", "pushes in", "a long hiss of train steam and a far station bell"),
             ("Rosie stood in the train door with her list. One: get off the train.",
              "medium shot", "ROSIE lifts her little picture list in front of her cup and studies it", "ROSIE",
              "serious and a little nervous", "tilts down", "a paper rustle and a soft hiss of steam"),
             ("\"That is a very good first thing,\" said Mom. And she waited.",
              "medium close-up", "MOM nods slowly and rests her tiny arm on the suitcase", "MOM",
              "calm and patient", "holds still", "a soft hiss of steam"),
         ]},
        {"title": "Big, white, new", "place": "station",
         "angle": "Over-the-shoulder view from behind a tiny pink lid, looking out across",
         "who": f"{ROSIE_CUP} stands very small at the edge of the train step with her straw drooping, the white "
                "peaks towering far above her",
         "beats": [
             ("Outside, everything was big. Everything was white. Everything was new.",
              "wide shot", "ROSIE looks slowly up and up at the towering peaks", "ROSIE", "awed and small",
              "tilts up", "a hush of wind over snow"),
             ("**雪** (xuě) = snow. On the roofs. On the peaks. On the station clock.",
              "wide shot", "ROSIE turns her lid from the snowy roof to the clock tower", "ROSIE",
              "wide-eyed and unsure", "pans right", "a hush of wind and one slow clock tick"),
             ("Rosie's straw drooped. That was a lot of snow for one small cup.",
              "medium close-up", "ROSIE's straw droops slowly as she peers over the edge of the step", "ROSIE",
              "small and doubtful", "holds still", "a hush of wind over snow"),
         ]},
        {"title": "Home!", "place": "station",
         "angle": "Dynamic low angle skimming the snowy boards of",
         "who": "CAT the little blue penguin slides on her tummy across the platform toward an ice-blue lamppost "
                "with her flippers swept back and a fan of snow spraying up behind her, beak open in a joyful "
                "shout, a small snowbank beside the lamppost; KYLE stands behind her under a tall wobbly stack "
                "of striped suitcases with his nose lifted high, sniffing the air",
         "beats": [
             ("WHEEE! Cat the penguin shot out of the train on her tummy and slid across the platform.",
              "wide shot", "CAT slides forward on her tummy and snow sprays up behind her", "CAT",
              "thrilled and free", "tracks beside", "a long icy swoosh and a spray of snow"),
             ("She popped up and hugged a lamppost. \"**家** (jiā) = home! Hello, lamppost. I missed you. You too, snowbank.\"",
              "medium shot", "CAT pops upright and wraps both flippers around the lamppost", "CAT",
              "overjoyed and silly", "pushes in", "a soft thump of little feet and a squeak of flippers on cold metal"),
             ("Kyle the black bear cub carried every suitcase. He sniffed. \"Somebody is grilling corn. I must meet them.\"",
              "medium shot", "KYLE wobbles under the suitcase stack and lifts his nose higher", "KYLE",
              "strong and suddenly hungry", "tilts up", "a creak of suitcase straps and two loud sniffs"),
         ]},
        {"title": "On three", "place": "station",
         "angle": "Warm close two-shot at the train step on",
         "who": f"TORI stands in the fresh powder snow below the train step holding one tiny arm up toward ROSIE, "
                f"green straw bobbing, grinning; {ROSIE_CUP} stands on the edge of the step above her with her "
                "little picture list held in front of her cup, straw quivering, ready to jump",
         "beats": [
             ("\"Jump on three,\" said Tori. \"You've got this, little sip. One. Two—\"",
              "medium close-up", "TORI stretches her tiny arm higher toward ROSIE and bobs her straw in a count",
              ["TORI", "ROSIE"], "sisterly and sure", "pushes in", "a soft hiss of steam"),
             ("Rosie jumped on two. Hop! Snow, right up to her stripes. One thing done. Tick.",
              "medium shot", "ROSIE hops off the step and lands in the powder beside TORI with a puff",
              ["ROSIE", "TORI"], "startled and delighted", "pulls back", "a soft powdery plop and a squeak of snow"),
         ]},
        {"title": "The seesaw sled", "place": "station",
         "angle": "Wide side view of a long wooden sled on",
         "who": "KYLE sits happily on the very back of the sled, which tips up like a seesaw; "
                f"{ROSIE_CUP} sits on the raised front edge high in the air with her straw straight up in "
                "surprise; CAT the little blue penguin clings beside her with both flippers up; MOM sits in the "
                "middle holding her lid on with one tiny arm, laughing; PIPER stands at the front on her "
                "glittery blue snowboard holding the tow rope, flippers thrown wide",
         "beats": [
             ("WHOOSH! Piper Paddlefoot skidded up, towing a long wooden sled. \"You came! Slide into it!\"",
              "wide shot", "PIPER throws both flippers wide and tugs the tow rope tight", "PIPER",
              "thrilled and windblown", "pans right", "a long swoosh and a rattle of sled runners"),
             ("Everybody piled on. Kyle sat at the back. The front went up like a seesaw.",
              "wide shot", "KYLE plops down and the front of the sled tips up with ROSIE and CAT on it",
              ["KYLE", "ROSIE", "CAT"], "surprised and giddy", "tilts up", "a wooden creak and a soft thump"),
             ("Kyle scooted to the middle. Off they flew, all the way to Frostpeak Lodge. \"Again!\" said Mom.",
              "wide shot", "KYLE scoots forward and the sled settles flat as MOM bounces with her lid held on",
              ["KYLE", "MOM"], "windblown and merry", "tracks beside", "a soft bump and sled runners hissing on snow"),
         ]},
        {"title": "Cocoa on his whiskers", "place": "hall",
         "angle": "Low angle looking up past the copper cocoa urn in",
         "who": "HERSCHEL stirs the copper cocoa urn with his wooden ladle, drops of cocoa on his bushy whiskers, "
                "eyes twinkling in welcome; MOM and TORI stand on the long rug holding steaming mugs topped with "
                "enormous marshmallows; KYLE stands beside them with an empty mug and a white marshmallow "
                "moustache",
         "beats": [
             ("Inside the lodge, a fire crackled. A big walrus stirred a copper pot of cocoa.",
              "medium shot", "HERSCHEL stirs the cocoa slowly with his wooden ladle", "HERSCHEL",
              "cozy and unhurried", "pushes in", "a crackling fire and a slow cocoa stir"),
             ("\"Welcome! I am Herschel,\" he boomed. There was cocoa on his whiskers. Quite a lot.",
              "medium close-up", "HERSCHEL spreads his flippers wide and a drop of cocoa falls from his whiskers",
              "HERSCHEL", "booming and kind", "tilts up", "a crackling fire and one fat drip"),
             ("Everybody got cocoa, with a marshmallow as big as Rosie's lid. Kyle's did not last.",
              "medium shot", "KYLE licks his marshmallow moustache and holds out his empty mug", "KYLE",
              "blissful and hopeful", "pans right", "a happy slurp and a crackling fire"),
         ]},
        {"title": "The Door Wall", "place": "hall",
         "angle": "Low wide angle looking up the whole height of the Door Wall in",
         "who": f"HERSCHEL points his wooden ladle up at the wall of little carved doors; {ROSIE_CUP} stands tiny "
                "on the rug below with her straw tipped back, looking up in wonder; KYLE stands on tiptoe "
                "sniffing a brass knob higher up with a guilty grin",
         "beats": [
             ("Herschel pointed his ladle at the Door Wall: twenty-four little doors. \"One rule. One door a day.\"",
              "wide shot", "HERSCHEL sweeps his ladle slowly up along the rows of little doors", "HERSCHEL",
              "proud and twinkly", "tilts up", "a crackling fire and a soft creak of old wood"),
             ("\"Some doors hide a golden train ticket. Market Train days! Christmas markets in the cities, "
              "home by nightfall.\"",
              "medium shot", "HERSCHEL leans down toward ROSIE with twinkling eyes and her straw gives a tiny wiggle",
              ["HERSCHEL", "ROSIE"], "twinkly and amazed", "pushes in", "a crackling fire"),
             ("Kyle was already sniffing door nine. \"I was just smell-testing,\" he said.",
              "medium close-up", "KYLE pulls his nose back from the brass knob and tucks his paws behind him",
              "KYLE", "caught and innocent", "pans right", "one loud sniff and a tiny rattle of a knob"),
         ]},
        {"title": "Door one", "place": "hall",
         "angle": "Close view at brass-knob height of the lowest little door in",
         "who": f"{ROSIE_CUP} stands in front of the lowest little door, which stands open, a tiny brass hook "
                "resting on a red velvet shelf inside; CAT the little blue penguin leans in beside her with "
                "round eyes; HERSCHEL bends down behind them, whiskers lifted in a smile",
         "beats": [
             ("Door one was the lowest, just Rosie's size. Her straw wiggled all the way up.",
              "medium close-up", "ROSIE bounces once in front of the little door and her straw wiggles", "ROSIE",
              "excited and proud", "pushes in", "a tiny creak of a tiny hinge"),
             ("Click! Inside sat one tiny brass hook. Nothing else.",
              "close-up", "CAT leans closer to the tiny hook and tilts her head", "CAT", "puzzled and curious",
              "pushes in", "a soft brass clink"),
             ("\"A hook for what?\" asked Rosie. Herschel's eyes twinkled. \"Come to the lane at dusk.\"",
              "medium shot", "HERSCHEL winks and taps his whiskers with one flipper", "HERSCHEL",
              "mysterious and merry", "tilts up", "a crackling fire and a low bubbling of the cocoa urn"),
         ]},
        {"title": "The red lantern", "place": "hall",
         "angle": "Medium view beside the crackling fireplace in",
         "who": "MOM kneels by her open travel bag holding up a round red paper lantern with a plain little door "
                f"painted on its side, smiling; {ROSIE_CUP} stands beside her holding the tiny brass hook in "
                "front of her cup, looking from the hook to the lantern",
         "beats": [
             ("Mom unfolded the paper lantern from Thanksgiving. Pop! Red, with a little door. "
              "\"**燈籠** (dēnglóng) = lantern,\" she said.",
              "medium shot", "MOM gives the red lantern a little shake and it puffs out round", "MOM",
              "warm and playful", "pushes in", "a crinkle of paper and a papery pop"),
             ("Rosie looked at the hook. She looked at the lantern. \"Oh,\" she said.",
              "close-up", "ROSIE looks down at the hook, then up at the lantern, and her straw springs up",
              "ROSIE", "puzzled, then delighted", "holds still", "a crackling fire and a tiny brass clink"),
         ]},
        {"title": "Lantern Lane", "place": "lane", "time": "night", "props": LANE_BARE,
         "angle": "Wide establishing view with deep perspective down",
         "who": f"{ROSIE_CUP} stands small in the middle of the snowy lane holding the red paper lantern in front "
                "of her cup, looking up at the bare string; TORI and MOM stand close on either side of her",
         "beats": [
             ("At dusk they walked to Lantern Lane. A long string hung over the stalls. Empty.",
              "wide shot", "ROSIE looks up along the bare string and hugs the lantern closer", "ROSIE",
              "small and watchful", "tilts up", "soft footsteps in snow and a far sizzle"),
             ("The lane was dark and blue. But one stall glowed orange. It smelled wonderful.",
              "wide shot", "ROSIE turns toward the glowing grill stall and her straw perks up", "ROSIE",
              "curious and drawn in", "pans right", "a warm sizzle and a crackle of coals"),
         ]},
        {"title": "The Squid Grill", "place": "lane", "time": "night", "props": LANE_BARE,
         "angle": "Low angle across the glowing grill counter on",
         "who": "SPICYSQUID stands behind the glowing grill tossing golden corn cobs high with his curly "
                "tentacles, orange sparks flying up around him, grinning wide; KYLE presses his paws on the "
                "counter edge and gazes up with huge shining eyes",
         "beats": [
             ("\"Welcome to the Squid Grill!\" called SpicySquid. \"Spice is nice! A little heat keeps the cold away!\"",
              "medium shot", "SPICYSQUID waves two curly tentacles over the glowing grill", "SPICYSQUID",
              "big-hearted and cheerful", "pushes in", "a loud sizzle and a crackle of coals"),
             ("He flipped six corn cobs at once. Sparks flew up like tiny fireworks.",
              "wide shot", "SPICYSQUID tosses the corn cobs up and orange sparks swirl above the grill",
              "SPICYSQUID", "showy and delighted", "tilts up", "a whoosh of flame and popping sparks"),
             ("Kyle's tummy growled. \"It's him,\" Kyle whispered. \"It's the corn.\"",
              "medium close-up", "KYLE presses both paws to his tummy and stares at the corn", "KYLE",
              "awestruck and hungry", "holds still", "a long tummy rumble and a soft sizzle"),
         ]},
        {"title": "The ladder", "place": "lane", "time": "night", "props": LANE_BARE,
         "angle": "Steep upward view of a wobbly tower of friends beside the grill stall on",
         "who": "KYLE stands firm in the snow with CAT the little blue penguin balanced on top of his red beanie, "
                f"reaching a tiny brass hook up to the string; {ROSIE_CUP} stands below holding the red paper "
                "lantern up in front of her cup; HERSCHEL stands beside them with both flippers ready, smiling",
         "beats": [
             ("Out came the hook. Kyle was the ladder. Cat was the top of the ladder.",
              "medium shot", "CAT stretches up on top of KYLE and hooks the tiny brass hook over the string",
              ["CAT", "KYLE"], "wobbly and determined", "tilts up", "a tiny brass click and a crunch of snow"),
             ("Click went the hook. Up went the red lantern, right beside the warmest stall.",
              "medium shot", "HERSCHEL lifts the red lantern from ROSIE and raises it toward the hook",
              ["HERSCHEL", "ROSIE"], "careful and glad", "tilts up", "a paper rustle and a warm sizzle"),
         ]},
        {"title": "One more light", "place": "lane", "time": "night", "props": LANE_ONE,
         "angle": "Close huddle at whisker height under the single glowing red paper lantern on",
         "who": f"HERSCHEL bends low with red lantern glow on his whiskers, one flipper cupped beside his mouth; "
                f"{ROSIE_CUP} leans in close with wide eyes; TORI leans in beside her, green straw tilted to "
                "listen; CAT the little blue penguin stands in the middle holding up one flipper, counting",
         "beats": [
             ("\"One more light,\" said Herschel. \"It's the only light,\" said Cat. \"One more than none,\" said Herschel.",
              "medium shot", "CAT holds up one flipper and HERSCHEL nods slowly", ["CAT", "HERSCHEL"],
              "cheeky and content", "tilts down", "a soft paper flutter and a warm sizzle"),
             ("Herschel bent low. \"One lantern every day. By the twenty-fourth, this whole lane will shine.\"",
              "medium close-up", "HERSCHEL leans down and cups one flipper beside his whiskers", "HERSCHEL",
              "hushed and twinkly", "pushes in", "a hush of falling snow"),
             ("\"It's a surprise for SpicySquid. That's his birthday. He never tells anyone.\"",
              "close-up", "ROSIE gasps softly and TORI nods with her straw bobbing", ["ROSIE", "TORI"],
              "thrilled and hushed", "holds still", "a tiny straw squeak and a far sizzle"),
         ]},
        {"title": "Corn", "place": "lane", "time": "night", "props": LANE_ONE,
         "angle": "Medium view over the glowing grill counter on",
         "who": "SPICYSQUID leans over the counter holding out a skewer of golden grilled corn with a curious "
                "grin; KYLE reaches up for it with both paws and a very innocent smile",
         "beats": [
             ("\"What's all the whispering?\" boomed SpicySquid. \"Corn,\" said Kyle. So he got corn. "
              "SpicySquid suspected nothing.",
              "medium shot", "SPICYSQUID holds the corn out and KYLE takes it with both paws",
              ["SPICYSQUID", "KYLE"], "curious and innocent", "pushes in", "a sizzle and a rustle of a corn husk"),
         ]},
        {"title": "Lantern one", "place": "lane", "time": "night", "props": LANE_ONE,
         "angle": "Wide upward view from the snow, past a tiny pink lid, along",
         "who": f"{ROSIE_CUP} stands in the falling snow holding her little picture list in front of her cup, "
                "looking up at the one red lantern glowing against the big dark peaks, her straw standing tall; "
                "CAT the little blue penguin leans cozily against her side",
         "beats": [
             ("Then the snow began to fall, soft and slow, past one small red light.",
              "wide shot", "ROSIE looks up at the red lantern and her straw rises tall", "ROSIE",
              "calm and glad", "tilts up", "a soft paper flutter and a hush of snow"),
             ("Rosie added it to her list. Lantern one. Tick. Twenty-three to go.",
              "medium close-up", "ROSIE lifts her little picture list while CAT leans in to look", ["ROSIE", "CAT"],
              "proud and cozy", "pushes in", "a tiny pencil scratch"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep on her tummy on a soft pillow at the foot of the "
                "bunk, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, in a brand-new bed. Goodnight, Cat, home at last.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, one red lantern, glowing in the snow. May tomorrow's little door hold something wonderful.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, in a brand-new bed.",
        "Goodnight, Cat, home at last.",
        "Goodnight, one red lantern, glowing in the snow.",
        "May tomorrow's little door hold something wonderful.",
    ],
}
