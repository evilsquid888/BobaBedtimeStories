"""14 — Under the Ice. Gabby's day: a lost snack satchel, a narwhal with a lot to say, and a smile all the way."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
SCARF = "a red-and-white striped knit scarf"

STORY = {
    "num": "14",
    "slug": "under-the-ice",
    "title": "Under the Ice",
    "meta": [
        ("Day", "Monday, December 14 · door fourteen"),
        ("Holiday thread", "Ice-fishing day on Glacier Lake"),
        ("Guests", "Captain Prism ❄️, Barnaby Beaksworth ❄️, Nibbles and Splash ❄️, Gabby the black star shark "
                   "(leads)"),
        ("Cat’s role", "lake guide: leads the way across the ice, and is honest that a penguin cannot see in "
                       "the deep dark water"),
        ("Mandarin", "貝殼 shell · 加油 you can do it · 微笑 smile"),
        ("Setting", "The Door Wall, then the ice-fishing huts on frozen Glacier Lake and the blue world under "
                    "the ice; Lantern Lane and the bunk room at night"),
    ],
    "palette": "icy white and deep sapphire blue with saturated sea green and hut orange accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "GABBY", "BARNABY", "PRISM", "NIBBLES", "SPLASH"],
    "cast_note": "Humans in this story: none. Gabby swims through the air a little above the ice, and through "
                 "water like any shark. Barnaby's snack satchel is a small brown leather bag with a long strap, "
                 "full of fish-shaped crackers.",
    "key_shot": 13,
    "places": {
        "hall": DOORWALL,
        "lake": {
            "name": "the ice-fishing huts on frozen Glacier Lake",
            "scene": "the fishing huts on Glacier Lake",
            "props": "a row of tiny painted fishing huts on the ice, a round fishing hole of deep blue water, "
                     "short fishing rods propped on forked sticks, a tin bucket, a sled piled with blankets, "
                     "a flask of cocoa",
            "light": "Bright winter sun glitters across the frozen lake",
            "accents": "sea green and hut orange",
            "atmo": "Sparkles of frost drift over the ice",
            "motion": "sparkles of frost drift over the ice",
        },
        "under": {
            "name": "the blue world under the ice of Glacier Lake",
            "scene": "the blue world under the ice",
            "props": "a glowing ceiling of pale ice, round fishing holes shining like skylights, smooth round "
                     "boulders, swaying green water weeds, strings of silver bubbles, an old sunken rowboat",
            "light": "Tall sunbeams slant down through the fishing holes",
            "accents": "deep sapphire blue and sea green",
            "atmo": "Silver bubbles rise slowly toward the ice",
            "motion": "silver bubbles rise slowly toward the ice",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a sea-green paper lantern and a tiny spiral shell on the nightstand"),
    },
    "shots": [
        {"title": "Door fourteen", "place": "hall",
         "angle": "Low angle looking up the tall wall of little carved doors in",
         "who": "GABBY floats nose first at a little open door carved with a plain spiral shell, tail swishing; "
                f"{ROSIE_CUP} stands below holding a tiny spiral shell against her lid with her eyes closed to "
                "listen; CAT the little blue penguin leans in beside her and pats her own tummy",
         "beats": [
             ("Door fourteen was Gabby's turn. She had no hands, so she booped it open with her nose.",
              "medium shot", "GABBY nudges the little carved door wide with the tip of her nose", "GABBY",
              "gentle and pleased", "tilts up", "a soft wooden click and a fire crackle"),
             ("Inside lay a tiny spiral **貝殼** (bèiké) = shell. Rosie held it to her lid and listened.",
              "close-up", "ROSIE presses the tiny shell to her lid and her straw tilts", "ROSIE",
              "curious and hushed", "pushes in", "a faint whooshing hum and a fire crackle"),
             ("\"It sounds like the sea,\" said Rosie. \"It sounds like lunch,\" said Cat the penguin.",
              "medium close-up", "CAT pats her tummy and grins at the shell", "CAT", "hungry and cheeky",
              "holds still", "a tiny tummy rumble"),
         ]},
        {"title": "Glacier Lake", "place": "lake",
         "angle": "Wide establishing view with deep perspective across the shining ice to",
         "who": "CAT the little blue penguin glides ahead on her snowboard pointing one flipper at the row of "
                f"huts, scarf flying; MOM pulls a small sled by its rope with a calm smile; {ROSIE_CUP} sits on "
                "the edge of the sled with her straw perked up; TORI sits beside her holding a cocoa flask",
         "beats": [
             ("Cat led everyone out onto Glacier Lake. Little fishing huts sat on the ice like painted hats.",
              "wide shot", "CAT glides forward on her snowboard and sweeps one flipper toward the huts", "CAT",
              "proud and at home", "pans right", "a snowboard hiss on ice and a far creak of the lake"),
         ]},
        {"title": "Fish for one more", "place": "lake",
         "angle": "Low angle at ice level across the round fishing hole toward",
         "who": "BARNABY sits on an upturned bucket beside the hole with his open snack satchel on his big tummy, "
                "holding up a flipper full of little fish-shaped crackers, eyes half shut and happy; NIBBLES and "
                "SPLASH sit side by side clapping their flippers",
         "beats": [
             ("By the biggest hole sat Barnaby Beaksworth. He had caught nothing all morning except a nap.",
              "medium shot", "BARNABY blinks awake on his bucket and stretches both flippers", "BARNABY",
              "drowsy and jolly", "pushes in", "a bucket creak and a soft lap of water"),
             ("\"Snack time!\" He opened his satchel. \"There's always enough fish for one more!\"",
              "medium close-up", "BARNABY flips his satchel open and holds up a flipper full of crackers",
              "BARNABY", "generous and beaming", "tilts down", "a buckle snap and a rustle of crackers"),
             ("They were fish crackers. The seal pups, Nibbles and Splash, clapped anyway.",
              "medium shot", "NIBBLES and SPLASH clap their flippers and bounce side by side",
              ["NIBBLES", "SPLASH"], "thrilled by everything", "pans left", "quick wet flipper claps"),
         ]},
        {"title": "Plop", "place": "lake",
         "angle": "High angle looking straight down past the rim of the fishing hole at",
         "who": "BARNABY bows low with one flipper across his tummy, his snack satchel sliding off his shoulder "
                "toward the deep blue hole; NIBBLES and SPLASH clap with their mouths wide open in delight",
         "beats": [
             ("Barnaby took a bow. His satchel slid off his shoulder. Plop! Down the hole it went.",
              "medium shot", "BARNABY bows and the satchel slips off his shoulder into the blue water", "BARNABY",
              "proud, then horrified", "tilts down", "one deep plop and a ripple of water"),
             ("Nibbles and Splash clapped harder. They thought it was a magic trick.",
              "medium close-up", "NIBBLES and SPLASH clap faster and rock back and forth", ["NIBBLES", "SPLASH"],
              "amazed and delighted", "pushes in", "fast wet flipper claps"),
         ]},
        {"title": "Dark as a cocoa pot", "place": "lake",
         "angle": "Underside view from just above the dark water looking up at the faces ringed around the hole on",
         "who": "CAT the little blue penguin leans over the rim squinting down with one flipper shading her "
                f"eyes; BARNABY peers down beside her with both flippers on his cheeks; {ROSIE_CUP} stands at "
                "the edge with her straw tilted, looking down",
         "beats": [
             ("Everybody peered down the hole. \"I can swim,\" said Cat, \"but it's dark as a cocoa pot.\"",
              "medium close-up", "CAT squints down past her flipper and shakes her head", "CAT",
              "honest and practical", "pushes in", "a soft lap of water"),
         ]},
        {"title": "A shark can", "place": "lake",
         "angle": "Medium close view beside the sled of blankets on",
         "who": "GABBY floats a little above the ice at the back with her fins tucked in and a small closed "
                f"smile, eyes on the hole; {ROSIE_CUP} turns to look up at her with bright eyes",
         "beats": [
             ("\"A shark can,\" said a soft voice. It was Gabby the black star shark.",
              "medium shot", "GABBY drifts forward a little and ROSIE turns to look up at her",
              ["GABBY", "ROSIE"], "shy and hopeful", "pans left", "a soft whoosh of air"),
             ("\"I can smell one cracker in a whole lake,\" said Gabby. \"It's a gift. Mostly.\"",
              "medium close-up", "GABBY wiggles the tip of her nose and gives one small shrug of her fins",
              "GABBY", "dry and modest", "pushes in", "a tiny sniff and a far creak of the lake"),
         ]},
        {"title": "Hold my scarf", "place": "lake",
         "angle": "Close view at the icy rim of the fishing hole on",
         "who": f"GABBY dips her head low beside the water so that {SCARF} slides off her neck; {ROSIE_CUP} "
                "stands at the rim holding the end of the scarf in front of her cup with a serious face and a "
                "little picture list tucked under one tiny arm",
         "beats": [
             ("Gabby slipped off her scarf. \"Hold this by the hole, Rosie. Then I'll know which hole is ours.\"",
              "close-up", "GABBY ducks her head and the striped scarf slides into the tiny arms of ROSIE",
              ["GABBY", "ROSIE"], "trusting and careful", "pushes in", "a soft slither of wool"),
             ("Rosie made a list. One: hold the scarf. Two: wait. Three: keep waiting.",
              "medium close-up", "ROSIE hugs the scarf in front of her cup and nods three times", "ROSIE",
              "serious and determined", "holds still", "a soft lap of water"),
             ("Gabby slid into the water without a splash. \"**加油** (jiāyóu) = You can do it!\" called Rosie.",
              "medium shot", "GABBY tips forward and slips nose first into the blue water", "GABBY",
              "brave and smooth", "tilts down", "one quiet plip of water"),
         ]},
        {"title": "Counting", "place": "lake",
         "angle": "Medium view across the still blue water of the fishing hole toward",
         "who": f"{ROSIE_CUP} stands at the rim holding {SCARF} in front of her cup, eyes fixed on the water, "
                "straw tipped forward; TORI sits close beside her holding out a small steaming mug of cocoa, "
                "green straw bobbing; MOM waits behind them with a fluffy towel folded over her tiny arms",
         "beats": [
             ("The water went still. Rosie counted to ten. No Gabby. She counted to ten again.",
              "medium shot", "ROSIE stares at the still water and hugs the scarf tighter", "ROSIE",
              "watchful and fidgety", "pushes in", "a far creak of the lake and a soft lap of water"),
             ("\"You've got this, little sip,\" said Tori, counting along with a cocoa. \"Eleven. Twelve.\"",
              "medium close-up", "TORI holds out the steaming mug and nods along with the count", "TORI",
              "easy and warm", "pans right", "a soft slosh of cocoa"),
         ]},
        {"title": "Put me back", "place": "lake",
         "angle": "Low angle at ice level looking up a bent fishing rod on",
         "who": "BARNABY holds a short fishing rod high in both flippers with a hopeful face; CAT the little "
                "blue penguin dangles from the end of the line by her yellow scarf with her flippers folded and "
                "one eyebrow up, an old boot and a kettle lid in the snow below her; NIBBLES and SPLASH clap "
                "their flippers",
         "beats": [
             ("Barnaby tried fishing for his satchel. He caught a boot, a kettle lid, and Cat's scarf.",
              "medium shot", "BARNABY heaves his fishing rod up and stares at what is on the end of it",
              "BARNABY", "hopeful, then baffled", "tilts up", "a creak of a rod and a squeak of line"),
             ("Cat was still wearing it. \"Put me back,\" said Cat. The seal pups clapped.",
              "medium close-up", "CAT dangles by her scarf with her flippers folded while NIBBLES and SPLASH clap",
              ["CAT", "NIBBLES", "SPLASH"], "unimpressed and dignified", "holds still",
              "a slow creak of line and wet flipper claps"),
         ]},
        {"title": "The blue world", "place": "under",
         "angle": "Wide view looking up from the lake bed through tall shafts of light in",
         "who": "GABBY swims down through a tall sunbeam with her nose pointing forward and her fins spread "
                "wide, eyes round with wonder, small and dark against the glowing blue",
         "beats": [
             ("Under the ice, everything was blue. Sunbeams came down the fishing holes like tall straws.",
              "wide shot", "GABBY glides down through a sunbeam with a slow sweep of her tail", "GABBY",
              "awed and at home", "tilts down", "a deep watery hum and soft bubbles"),
         ]},
        {"title": "The pole with a hat", "place": "under",
         "angle": "Low angle beside the old sunken rowboat looking up at",
         "who": "PRISM floats grandly with his chin raised and his captain's hat tilted, the brown snack satchel "
                "hanging by its strap from his long spiral rainbow-shimmer tusk; GABBY pauses below him with "
                "her fins tucked in and her mouth pressed shut, eyes wide",
         "beats": [
             ("The satchel hung on a long, shimmering pole. The pole was wearing a captain's hat.",
              "medium shot", "GABBY stops short and stares up at the satchel swinging on the long tusk", "GABBY",
              "puzzled and polite", "tilts up", "a deep watery hum and a soft creak of leather"),
             ("\"Halt!\" boomed the pole. \"I am Captain Prism, Admiral of the Under-Ice, Keeper of the Deep—\"",
              "medium close-up", "PRISM puffs out his chest and sweeps his tusk in a grand slow arc", "PRISM",
              "grand and delighted with himself", "pushes in", "a rumbling burst of bubbles"),
             ("It went on for some time. Gabby waited politely. The same bubble went by twice.",
              "wide shot", "PRISM goes on nodding grandly while GABBY bobs in place and watches one bubble drift by",
              ["PRISM", "GABBY"], "endless and patient", "pans left", "a steady burble of bubbles"),
         ]},
        {"title": "Like a clam", "place": "under",
         "angle": "Close two-shot at eye level among the silver bubbles in",
         "who": "GABBY keeps her mouth nearly closed in a tiny tight smile, fins tucked against her sides, eyes "
                "shy; PRISM leans down toward her with one eyebrow raised and his captain's hat sliding forward",
         "beats": [
             ("\"Please may I have the satchel?\" mumbled Gabby, with her mouth nearly shut.",
              "medium close-up", "GABBY mumbles through a tiny tight smile and one bubble slips out", "GABBY",
              "shy and careful", "pushes in", "one small bubble pop"),
             ("\"Speak up, sailor! Why talk like a clam?\" asked the Captain.",
              "medium close-up", "PRISM leans closer and tilts his head so his hat slides forward", "PRISM",
              "puzzled and kindly", "pans right", "a rumbling burst of bubbles"),
             ("\"It's my teeth,\" whispered Gabby. \"There are a lot of them. They startle people.\"",
              "close-up", "GABBY looks down and tucks her fins in tighter", "GABBY", "bashful and small",
              "holds still", "a soft watery hush"),
         ]},
        {"title": "One very long tooth", "place": "under",
         "angle": "Dramatic low angle looking up the whole length of a rainbow tusk in",
         "who": "PRISM lifts his long spiral rainbow-shimmer tusk high like a flagpole in a tall sunbeam, the "
                "snack satchel swinging from it, chest puffed with pride; GABBY looks up along the tusk with "
                "round shining eyes",
         "beats": [
             ("\"Teeth?\" The Captain raised his tusk. \"This is a tooth. One very long tooth!\"",
              "medium shot", "PRISM raises his tusk high and rainbow light ripples along it", "PRISM",
              "proud and booming", "tilts up", "a grand whoosh of water"),
             ("\"I have never hidden it once. It would not fit in anything.\"",
              "medium close-up", "PRISM looks along his own tusk and gives a helpless happy shrug", "PRISM",
              "frank and funny", "pans right", "a rumbling burble of bubbles"),
             ("\"Those are no trouble, sailor. That is a treasure chest. Open it!\"",
              "medium close-up", "PRISM dips his tusk toward GABBY and her eyes grow rounder", ["PRISM", "GABBY"],
              "kind and stirring", "pushes in", "a soft watery hush"),
         ]},
        {"title": "All the way", "place": "under",
         "angle": "Tight close-up, the face filling the frame, in",
         "who": "GABBY smiles her widest smile with every tiny rounded tooth showing, rainbow glints dancing "
                "across her teeth, fins spread wide, the strap of the snack satchel hooked over one fin; PRISM "
                "salutes behind her with one flipper at the brim of his captain's hat",
         "beats": [
             ("So Gabby gave her biggest **微笑** (wéixiào) = smile. The tusk's rainbow danced on every tooth.",
              "close-up", "GABBY's tiny smile spreads wide and rainbow glints sparkle on her teeth", "GABBY",
              "shy, then shining", "pushes in", "a bright shimmer of bubbles"),
             ("\"Now that,\" said Captain Prism, \"lights up the whole lake.\" And he handed over the satchel.",
              "medium shot", "PRISM salutes while GABBY spreads her fins with the satchel hooked on one",
              ["PRISM", "GABBY"], "proud and glad", "pulls back", "a rumbling burble of bubbles"),
         ]},
        {"title": "The biggest smile on Glacier Lake", "place": "lake",
         "angle": "Low angle at ice level across the splashing fishing hole on",
         "who": "GABBY bursts up out of the round hole in a sparkle of drops with the dripping satchel hooked on "
                f"one fin and her widest smile, every tooth showing; {ROSIE_CUP} stands at the rim holding "
                f"{SCARF} in front of her cup, straw shooting straight up; NIBBLES and SPLASH clap so hard they "
                "tip over backward",
         "beats": [
             ("Up top, Rosie held the striped scarf by the hole. The water bulged beside it.",
              "medium shot", "ROSIE leans toward the water as it swells and her straw lifts", "ROSIE",
              "hopeful and breathless", "pushes in", "a rising gurgle of water"),
             ("Out popped the satchel. Then Gabby. Then the biggest smile on Glacier Lake.",
              "medium shot", "GABBY rises from the hole with the satchel on her fin and beams with every tooth",
              "GABBY", "triumphant and free", "tilts up", "a big splash and pattering drops"),
             ("\"Don't worry,\" she told the seal pups. \"I only bite pie.\" They clapped till they fell over.",
              "medium close-up", "NIBBLES and SPLASH clap wildly and topple over backward together",
              ["NIBBLES", "SPLASH"], "overjoyed and dizzy", "pans left", "wild wet flipper claps and two soft thumps"),
         ]},
        {"title": "Cracker soup", "place": "lake",
         "angle": "Medium view beside the sled of blankets and the tin bucket on",
         "who": "MOM wraps a fluffy towel around GABBY, who is still smiling wide; BARNABY tips his dripping "
                "satchel upside down over the tin bucket with soggy crackers plopping out, laughing; CAT the "
                "little blue penguin peers into the bucket and leans away with a wrinkled beak",
         "beats": [
             ("Mom wrapped Gabby in a warm towel. Barnaby tipped out his satchel. Soggy crackers.",
              "medium shot", "MOM tucks the towel snugly around GABBY and pats it down", ["MOM", "GABBY"],
              "caring and proud", "pushes in", "a soft towel rustle and wet plops"),
             ("\"Cracker soup!\" said Barnaby. \"Always enough for one more!\" \"I'll pass,\" said Cat.",
              "medium close-up", "BARNABY holds up the bucket while CAT leans away and waves one flipper",
              ["BARNABY", "CAT"], "jolly and unconvinced", "pans right", "a slosh in a tin bucket"),
         ]},
        {"title": "Lantern fourteen", "place": "lane", "time": "night",
         "angle": "Upward view along the string of lanterns over",
         "who": "GABBY floats up beside the long string hooking a sea-green paper lantern on with her nose, "
                f"smiling with every tooth in the warm glow; {ROSIE_CUP} stands below holding her little picture "
                "list in front of her cup, straw wiggling; TORI and MOM look up side by side; CAT the little "
                "blue penguin claps her flippers; BARNABY holds his snack satchel wide open with a steaming "
                "flask of cocoa under one flipper",
         "beats": [
             ("That night Gabby hung lantern fourteen on Lantern Lane with her nose. It was sea green.",
              "wide shot", "GABBY nudges the sea-green lantern onto its hook and it sways", "GABBY",
              "careful and proud", "tilts up", "a creak of string and a soft crunch of snow"),
             ("\"One more light,\" said Gabby. She smiled all the way. Everybody smiled right back.",
              "medium close-up", "GABBY beams with every tooth while CAT claps her flippers below",
              ["GABBY", "CAT"], "glowing and easy", "pushes in", "soft flipper claps and a far sizzle of a grill"),
             ("Barnaby passed round cocoa and dry crackers. There was enough for one more. There always is.",
              "medium shot", "BARNABY holds his open satchel out and ROSIE's straw wiggles", ["BARNABY", "ROSIE"],
              "generous and cozy", "pulls back", "a rustle of crackers and a slosh of cocoa"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                f"closed, {SCARF} folded beside her pillow; CAT the little blue penguin asleep curled on a soft "
                "pillow at the foot of the bed, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, who waited so well. Goodnight, Gabby, smile wide as the lake.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Captain, still talking somewhere below. May your dreams be blue and deep and full of "
              "friendly bubbles.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, who waited so well.",
        "Goodnight, Gabby, smile wide as the lake.",
        "Goodnight, Captain, still talking somewhere below.",
        "May your dreams be blue and deep and full of friendly bubbles.",
    ],
}
