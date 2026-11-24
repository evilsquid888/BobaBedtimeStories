"""04 — The Helper Candle (Friday, December 4 · Hanukkah, first night)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

# First night: the helper candle (the shamash) in the tall middle cup and one candle at the right end.
UNLIT = "two slim unlit candles, one in the tall middle cup and one at the right end"
LIT = "the tall helper candle burning in the middle cup and one candle burning at the right end"

NOOK = {
    "name": "the window nook of Herschel's cocoa kitchen",
    "scene": "the cocoa kitchen window nook",
    "props": "a deep window seat with blue-and-white cushions, a brass candle holder with nine little cups in a "
             "row on the wide windowsill, rows of copper cocoa pots on hooks, jars of cinnamon sticks and "
             "marshmallows, a little wooden box of slim white candles, a plate of golden potato latkes",
    "light": "Late golden sun glows through the frosted window panes",
    "accents": "candle gold and deep blue",
    "atmo": "Cocoa steam curls past the window",
    "motion": "cocoa steam curls past the window",
}
NOOK_NIGHT = dict(NOOK, name="Herschel's cocoa kitchen window nook after dark", light="Soft candle glow and one copper lamp light the nook at nightfall, the window "
                              "deep blue with night")

STORY = {
    "num": "04",
    "slug": "the-helper-candle",
    "title": "The Helper Candle",
    "meta": [
        ("Day", "Friday, December 4"),
        ("Holiday thread", "Hanukkah, the first night: Herschel and Noa host, and the family are welcome guests"),
        ("Guests", "Herschel the Walrus ❄️, Noa the jelly doughnut (new), Gabby the black star shark"),
        ("Cat’s role", "the helper penguin: polishes the brass, stands like a candle, counts cocoa pots while "
                       "waiting for dark, checks the window from outside, and dances like a candle too"),
        ("Mandarin", "蠟燭 candle · 光明節 Hanukkah · 光 light"),
        ("Setting", "The great hall of Frostpeak Lodge, the window nook of Herschel's cocoa kitchen (afternoon, "
                    "then nightfall), Lantern Lane at night, and the lodge bunk room"),
    ],
    "palette": "deep winter blue and warm cream with saturated candle gold and copper accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "HERSCHEL", "NOA", "GABBY"],
    "cast_note": "Humans in this story: none. Hanukkah details to keep exact in every picture: the candle holder "
                 "has nine cups; on this first night it holds two candles only, the helper candle (the shamash) "
                 "in the tall middle cup and one candle at the right end; Herschel, a grown-up, does all the "
                 "lighting. Gabby swims through the air a little above the floor.",
    "key_shot": 10,
    "places": {
        "hall": DOORWALL,
        "nook": NOOK,
        "nook_night": NOOK_NIGHT,
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny unlit white candle and a chocolate coin in gold foil on the nightstand"),
    },
    "shots": [
        {"title": "Door four", "place": "hall",
         "angle": "Close view at brass-knob height of a little door in",
         "who": "TORI holds a little door open with one tiny arm, a tiny white candle standing on a blue velvet "
                f"shelf inside, green straw tilted with interest; {ROSIE_CUP} stands on tiptoe beside her, straw "
                "wiggling; HERSCHEL leans down behind them with his whiskers lifted in a smile",
         "beats": [
             ("Door four was Tori's turn. Click! Inside stood one tiny **蠟燭** (làzhú) = candle.",
              "close-up", "TORI swings the little door wide and ROSIE stretches up to see", ["TORI", "ROSIE"],
              "curious and pleased", "pushes in", "a tiny hinge creak and a crackling fire"),
             ("\"Ah,\" rumbled Herschel. \"Tonight is the first night of **光明節** (Guāngmíng jié) = Hanukkah.\"",
              "medium shot", "HERSCHEL leans closer and his whiskers lift in a wide smile", "HERSCHEL",
              "glad and glowing", "tilts up", "a low happy rumble and a crackling fire"),
             ("\"Come to my cocoa kitchen before sundown. Everyone is welcome. Especially the penguin.\"",
              "medium close-up", "HERSCHEL spreads both flippers wide in welcome", "HERSCHEL",
              "warm and twinkly", "holds still", "a crackling fire"),
         ]},
        {"title": "Noa", "place": "nook",
         "angle": "Low angle across the blue-and-white cushions of",
         "who": "NOA stands on the window seat hugging CAT the little blue penguin with both tiny arms, a soft "
                "cloud of powdered sugar puffing off her; CAT the little blue penguin blinks in the hug with a "
                "dusting of white sugar on her beak",
         "beats": [
             ("In the kitchen window nook stood a small round jelly doughnut in a blue scarf.",
              "medium shot", "NOA bounces on the cushion and a little sugar puffs off her", "NOA",
              "bubbly and welcoming", "pushes in", "a soft bounce on a cushion"),
             ("\"I'm Noa! Welcome, welcome!\" She hugged Cat the penguin. Poof. Powdered sugar.",
              "medium close-up", "NOA squeezes CAT in a hug and a white puff of sugar bursts around them",
              ["NOA", "CAT"], "joyful and surprised", "holds still", "a soft squeeze and a poof"),
             ("\"Sorry,\" said Noa. \"I shed.\" Cat sneezed a tiny white cloud.",
              "close-up", "CAT sneezes a tiny puff of sugar off her beak and grins", "CAT",
              "tickled and cheerful", "pushes in", "one tiny penguin sneeze"),
         ]},
        {"title": "Nine little cups", "place": "nook",
         "angle": "Close view along the wide windowsill of",
         "who": f"NOA points one tiny arm at the brass candle holder, which holds {UNLIT}; {ROSIE_CUP} stands "
                 "on the windowsill beside it with a little picture list held in front of her cup, counting",
         "beats": [
             ("On the windowsill stood a brass candle holder with nine little cups. Rosie counted twice.",
              "medium shot", "ROSIE hops one step along the sill, counting the little brass cups", "ROSIE",
              "careful and curious", "tracks beside", "tiny taps on a wooden sill"),
             ("\"Eight cups for eight nights,\" said Noa. \"The tall one is for the shamash, the helper candle.\"",
              "medium close-up", "NOA points up at the tall candle in the middle cup", "NOA",
              "proud and clear", "tilts up", "a soft bubbling of cocoa"),
             ("\"The helper lights the others. One tonight. Two tomorrow. Every night, one more light!\"",
              "medium close-up", "NOA holds up one tiny arm, then two, and bounces", "NOA",
              "excited and generous", "pushes in", "a soft bounce and a bubbling of cocoa"),
         ]},
        {"title": "More winters than whiskers", "place": "nook",
         "angle": "Medium view past the copper cocoa pots in",
         "who": "HERSCHEL holds the empty brass candle holder up to the window light in both flippers, looking at "
                "it fondly; CAT the little blue penguin polishes one of its brass cups with the end of her yellow "
                "scarf, her round reflection shining in the brass",
         "beats": [
             ("\"It was my grandmother's,\" said Herschel. \"It has seen more winters than I have whiskers.\"",
              "medium shot", "HERSCHEL turns the brass holder slowly in the window light", "HERSCHEL",
              "fond and proud", "pushes in", "a soft brass chime and a bubbling of cocoa"),
             ("\"Grown-ups light the candles. Kids polish,\" he said. So Cat polished until she could see her beak.",
              "medium close-up", "CAT rubs a brass cup with her scarf and peers at her reflection", "CAT",
              "busy and pleased", "holds still", "a squeaky rub of cloth on brass"),
         ]},
        {"title": "The helper penguin", "place": "nook",
         "angle": "Low view along the window seat of",
         "who": "NOA stands on a cushion with her tiny arms thrown wide, mid-explanation; CAT the little blue "
                "penguin stands very tall and straight beside her with her flippers pressed to her sides like a "
                "candle, beak pointed up, eyes solemn",
         "beats": [
             ("\"Eight nights of candles and latkes and songs,\" said Noa. \"It's the festival of lights!\"",
              "medium shot", "NOA throws her tiny arms wide and rocks on her toes", "NOA", "proud and sparkling",
              "pushes in", "a soft bounce on a cushion"),
             ("\"I'm a helper too,\" said Cat. She stood very straight, like a candle. A candle with a beak.",
              "medium close-up", "CAT stretches up even taller and holds perfectly still", "CAT",
              "solemn and silly", "tilts up", "a tiny stretch squeak"),
         ]},
        {"title": "Thirty-six lights", "place": "nook",
         "angle": "Close view at windowsill height in",
         "who": f"{ROSIE_CUP} stands beside the tall unlit helper candle in the brass holder, her little picture "
                "list covered in tiny tally marks held in front of her cup, looking up at the candle with her "
                "straw tilted in a question",
         "beats": [
             ("Rosie did the sum. One and two and three, up to eight. Thirty-six lights to give!",
              "medium close-up", "ROSIE taps down her little picture list and her eyes go wide", "ROSIE",
              "busy, then startled", "pushes in", "quick tiny pencil taps"),
             ("\"Won't the helper run out?\" asked Rosie. Herschel's whiskers twitched. \"Wait for sundown,\" he said. \"And watch.\"",
              "close-up", "ROSIE looks up at the tall candle and tilts her straw in a question", "ROSIE",
              "curious and puzzled", "tilts up", "a soft bubbling of cocoa"),
         ]},
        {"title": "Waiting for sundown", "place": "nook",
         "angle": "Wide view from the kitchen floor up toward the tall frosted window of",
         "who": "GABBY floats in a little above the floor with a pie dish balanced on her back and a soft closed "
                "smile; MOM sets a plate of golden latkes on the window seat; CAT the little blue penguin points "
                "one flipper along the row of copper pots, counting",
         "beats": [
             ("Gabby swam in with a pie. Mom carried in the latkes: crispy potato pancakes, fried in oil.",
              "wide shot", "GABBY glides forward with the pie while MOM sets down the plate of latkes",
              ["GABBY", "MOM"], "calm and festive", "pans right", "a soft whoosh of air and a plate clink"),
             ("Then everybody waited for sundown. Waiting is hard. Cat counted the cocoa pots. Four times.",
              "medium shot", "CAT points her flipper at one copper pot after another", "CAT",
              "fidgety and patient-ish", "tracks beside", "tiny flipper taps on copper"),
         ]},
        {"title": "A grown-up job", "place": "nook_night", "time": "night",
         "angle": "Hushed wide view toward the tall window in",
         "who": f"HERSCHEL stands at the windowsill holding one small lit match beside the brass candle holder, "
                f"which holds {UNLIT}, the glow on his whiskers; NOA bounces on her toes on the sill beside him; "
                f"{ROSIE_CUP} watches from the window seat with wide eyes",
         "beats": [
             ("At last the sun dipped behind the peaks. \"Now,\" said Herschel. \"Lighting is a grown-up job.\"",
              "wide shot", "HERSCHEL lifts the small match and its glow spreads over his whiskers", "HERSCHEL",
              "solemn and happy", "pushes in", "the scratch and flare of one match"),
             ("He lit the helper candle first. Only the helper.",
              "medium close-up", "HERSCHEL touches the match to the tall middle candle and a flame catches",
              "HERSCHEL", "careful and steady", "holds still", "a tiny flutter of a new flame"),
         ]},
        {"title": "The blessing", "place": "nook_night", "time": "night",
         "angle": "Close view at flame height across the windowsill of",
         "who": "HERSCHEL holds the lit helper candle up in one flipper with his eyes half closed, singing softly, "
                "the one small flame glowing on his tusks; NOA stands beside the brass holder with her tiny arms "
                "clasped and her eyes shining",
         "beats": [
             ("He held it up and sang a blessing, low and rumbly, like a very kind tugboat.",
              "medium close-up", "HERSCHEL sways gently with the candle held high while NOA sways along",
              ["HERSCHEL", "NOA"], "peaceful and glad", "holds still", "a tiny flutter of flame"),
         ]},
        {"title": "One flame becomes two", "place": "nook_night", "time": "night",
         "angle": "Extreme close-up at flame height on the windowsill of",
         "who": f"the brass candle holder with {LIT}, two small steady flames reflected in the dark window "
                f"glass; {ROSIE_CUP} stands close beside them with golden glow on her dome lid, eyes huge",
         "beats": [
             ("Then the helper dipped down and touched the first candle. One flame became two.",
              "extreme close-up", "ROSIE leans in as the two small flames grow tall and steady", "ROSIE",
              "breathless and amazed", "pushes in", "a tiny flutter of two flames"),
             ("Rosie looked hard at the helper. Still tall. Still bright. Nothing was missing.",
              "close-up", "ROSIE looks from one flame to the other and her straw begins to rise", "ROSIE",
              "searching, then relieved", "pans left", "a tiny flutter of flames"),
             ("\"A light that is shared is never spent,\" said Herschel.",
              "close-up", "ROSIE's straw rises tall and the two flames shine in her eyes", "ROSIE",
              "glad and glowing", "holds still", "a tiny flutter of flames"),
         ]},
        {"title": "Two flames and a squeeze", "place": "nook_night", "time": "night",
         "angle": "Warm close view on the candlelit window seat of",
         "who": "MOM wraps her tiny arms around ROSIE and TORI together, golden candle glow on all three lids, "
                "eyes closed in a smile",
         "beats": [
             ("Mom squeezed Rosie and Tori close. The window glowed. The whole kitchen smelled of cocoa and latkes.",
              "medium close-up", "MOM squeezes ROSIE and TORI close and rocks them gently", ["MOM", "ROSIE", "TORI"],
              "cozy and sure", "pushes in", "a soft squeeze and a tiny flutter of flames"),
         ]},
        {"title": "In the window", "place": "nook_night", "time": "night",
         "angle": "Full-frame view from inside toward the dark window glass of",
         "who": "NOA stands on the sill beside the two small candle flames, pointing out through the glass; "
                "CAT the little blue penguin stands outside in the snow with her beak squashed flat against the "
                "pane and her breath fogging it",
         "beats": [
             ("\"We put them in the window,\" said Noa, \"so anyone out in the dark can share the light.\"",
              "medium shot", "NOA points one tiny arm out through the dark glass", "NOA", "proud and gentle",
              "holds still", "a tiny flutter of flames"),
             ("Cat ran outside to check. She squashed her beak on the glass. \"It works!\" she yelled.",
              "medium close-up", "CAT presses her beak flatter on the glass and waves one flipper", "CAT",
              "delighted and squashed", "holds still", "a squeak of a beak on cold glass"),
         ]},
        {"title": "Gabby's smile", "place": "nook_night", "time": "night",
         "angle": "Medium view along the candlelit windowsill of",
         "who": "GABBY floats beside the window with her widest smile, every tiny tooth gleaming gold in the "
                "candlelight; NOA peeks out from behind a copper cocoa pot with only her eyes and her red jelly "
                "dot showing",
         "beats": [
             ("Gabby smiled at the candles. Every tooth gleamed gold. Noa squeaked and hid behind a cocoa pot.",
              "medium shot", "GABBY beams at the flames while NOA ducks lower behind the copper pot",
              ["GABBY", "NOA"], "happy and startled", "pans right", "a tiny squeak and a clink of copper"),
             ("\"Don't worry,\" said Gabby. \"I only bite pie.\" Noa peeked out. \"I'm a doughnut.\"",
              "medium close-up", "NOA peeks a little higher over the copper pot", "NOA", "wary and curious",
              "pushes in", "a soft clink of copper"),
             ("\"Exactly,\" said Gabby. \"Totally different shelf.\" Noa giggled until sugar puffed out.",
              "medium close-up", "GABBY winks and her tail gives one slow happy swish", "GABBY",
              "gentle and funny", "holds still", "a soft poof and a clink of copper"),
         ]},
        {"title": "Now they matched", "place": "nook_night", "time": "night",
         "angle": "Close two-shot on the blue-and-white cushions of",
         "who": "NOA sits on the window seat holding out a chocolate coin in gold foil; GABBY floats close beside "
                "her with a dab of white powdered sugar on her nose and a soft happy smile",
         "beats": [
             ("The sugar landed on Gabby's nose. Now they matched. Noa gave her a chocolate coin.",
              "medium close-up", "NOA holds the gold coin out and GABBY dips her sugary nose in thanks",
              ["NOA", "GABBY"], "shy and friendly", "pushes in", "a crinkle of gold foil"),
         ]},
        {"title": "The walrus dance", "place": "nook_night", "time": "night",
         "angle": "Low wide angle from the kitchen floor up at",
         "who": "HERSCHEL dances with both flippers in the air and his apron flying, singing with his eyes shut; "
                "NOA rides on his shoulder with her tiny arms up, powdered sugar drifting down from her like "
                "snow; the copper cocoa pots swing on their hooks behind them",
         "beats": [
             ("Then Herschel sang and danced. The cocoa pots rattled. Noa shed so much sugar it snowed indoors.",
              "wide shot", "HERSCHEL stomps and sways with his flippers up while NOA bounces on his shoulder",
              ["HERSCHEL", "NOA"], "joyful and booming", "tilts up", "rattling copper pots and thumping floorboards"),
         ]},
        {"title": "Round and round", "place": "nook_night", "time": "night",
         "angle": "High angle looking down on the candlelit floor of",
         "who": f"MOM and TORI dance in a ring with their tiny arms linked; {ROSIE_CUP} hops in the ring between "
                "them with her straw wiggling; GABBY swims a happy loop just above their lids; CAT the little "
                "blue penguin dances in the middle standing very straight like a candle, with one flipper "
                "flickering on top of her head",
         "beats": [
             ("Everybody joined in, round and round. Mom spun Tori. Tori spun Rosie. Gabby looped overhead.",
              "wide shot", "MOM and TORI swing around in the ring while ROSIE hops and GABBY loops above",
              ["MOM", "TORI", "ROSIE", "GABBY"], "dizzy and delighted", "pans right",
              "shuffling steps and happy squeaks"),
             ("Cat danced like a candle. Very straight, with a little flicker at the top.",
              "medium close-up", "CAT stands stiff and tall and wiggles one flipper above her head like a flame",
              "CAT", "solemn and silly", "pushes in", "a tiny flipper flutter and thumping floorboards"),
         ]},
        {"title": "From one lantern to another", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the lantern string over",
         "who": "HERSCHEL holds a long thin taper with a tiny flame up between a glowing green paper lantern on "
                f"the string and a round blue paper lantern; {ROSIE_CUP} stands on an upturned crate below "
                "holding the blue lantern up in front of her cup, very still; TORI steadies the crate with both "
                "tiny arms",
         "beats": [
             ("On Lantern Lane, Rosie held up the blue lantern. \"Hold still,\" said Tori. \"You've got this, little sip.\"",
              "medium shot", "ROSIE holds the blue lantern perfectly still while TORI steadies the crate",
              ["ROSIE", "TORI"], "careful and brave", "tilts up", "a creak of a crate and a hush of snow"),
             ("Herschel lit a taper from the green lantern, then lit the blue. The green stayed just as bright.",
              "medium close-up", "HERSCHEL dips the taper into the blue lantern and it begins to glow", "HERSCHEL",
              "gentle and precise", "pushes in", "a tiny flutter of a new flame"),
         ]},
        {"title": "One more light", "place": "lane", "time": "night",
         "angle": "Close view under four glowing paper lanterns, red, purple, green and blue, on",
         "who": "NOA bounces on top of an upturned crate with both tiny arms in the air and a puff of powdered "
                f"sugar around her; {ROSIE_CUP} stands beside her holding a little picture list in front of her "
                "cup, blue glow on her lid; CAT the little blue penguin stands beside her, very straight, with one "
                "flipper on top of her head",
         "beats": [
             ("\"One more light!\" cheered Noa. It was her favorite thing to say. Today she said it twice.",
              "medium shot", "NOA bounces with both tiny arms up and sugar puffs around her", "NOA",
              "thrilled and proud", "tilts up", "a soft bounce and a poof"),
             ("Rosie counted every **光** (guāng) = light. Candles: two. Lanterns: four. Sugar sneezes: lots.",
              "medium close-up", "ROSIE marks her little picture list three times", "ROSIE",
              "busy and happy", "pushes in", "three tiny pencil scratches"),
             ("\"And one candle with a beak,\" said Cat. Rosie wrote that down too.",
              "close-up", "CAT stands up very straight and ROSIE makes one more mark on her list", ["CAT", "ROSIE"],
              "proud and amused", "holds still", "one tiny pencil scratch"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep on a soft pillow at the foot of the bunk with a "
                "dusting of white sugar on her head, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, with candlelight in your eyes. Goodnight, Noa, with sugar on your pillow.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, helper candle, who gave and still glowed. May tomorrow night bring one more light.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, with candlelight in your eyes.",
        "Goodnight, Noa, with sugar on your pillow.",
        "Goodnight, helper candle, who gave and still glowed.",
        "May tomorrow night bring one more light.",
    ],
}
