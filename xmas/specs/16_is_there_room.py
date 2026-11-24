"""16 — Is There Room? (Las Posadas begins). Three very cold friends from Costa Rica, and Rosie becomes the last door."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
RIDERS = "GALLO and PINTO sit side by side on his long rainbow beak shaking tiny maracas"

STORY = {
    "num": "16",
    "slug": "is-there-room",
    "title": "Is There Room?",
    "meta": [
        ("Day", "Wednesday, December 16 · door sixteen"),
        ("Holiday thread", "Las Posadas begins: friends go door to door asking for room, and the last door "
                           "says yes"),
        ("Guests", "Tico the Toucan, Gallo and Pinto 🇨🇷 (just off the mail-boat, and freezing), "
                   "Herschel the Walrus ❄️"),
        ("Cat’s role", "posada planner: picks Cabin Row, zooms ahead to play a door (full of penguin), and gives "
                       "up her spot for the windowsill"),
        ("Mandarin", "歡迎 welcome · 有位子 there's room"),
        ("Spanish", "posada shelter · pura vida life is good"),
        ("Setting", "The Door Wall, then Cabin Row at dusk, door after glowing door; Lantern Lane and a very "
                    "full bunk room at night"),
    ],
    "palette": "deep winter blue and warm cream with saturated turquoise and marigold orange accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "TICO", "GALLO", "PINTO", "HERSCHEL"],
    "cast_note": "Humans in this story: none. Gallo and Pinto are very small and ride side by side on Tico's "
                 "beak, shaking tiny maracas from the suitcase. Rosie carries a small brass lamp with a steady glow (a little electric lamp, never a flame).",
    "key_shot": 11,
    "places": {
        "hall": DOORWALL,
        "row": {
            "name": "Cabin Row in Frostpeak Valley at dusk",
            "scene": "Cabin Row at dusk",
            "props": "a curving row of little log cabins with round glowing windows, cabin doors painted red, "
                     "blue and green, a brass lamp post, snow-heaped roofs with smoking chimneys, a path of "
                     "stamped snow, a stack of firewood under a striped tarp",
            "light": "Golden light spills from the cabin doorways into the blue dusk",
            "accents": "turquoise and marigold orange",
            "atmo": "Chimney smoke curls up through the first falling snowflakes",
            "motion": "chimney smoke curls up through the falling snowflakes",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny wooden door with a smaller door in it and a tiny straw hat on the nightstand"),
    },
    "shots": [
        {"title": "Door sixteen", "place": "hall",
         "angle": "Low angle looking up the tall wall of little carved doors in",
         "who": f"{ROSIE_CUP} stands at a little open door, and behind it sits a tiny wooden door with an even "
                "smaller door set into it, her straw tilted in wonder; CAT the little blue penguin leans in "
                "beside her with one flipper on her chin",
         "beats": [
             ("Door sixteen was Rosie's. Behind it was a tiny door. In that door was an even tinier door.",
              "close-up", "ROSIE opens the little door and peers at the tiny door inside", "ROSIE",
              "curious and tickled", "pushes in", "two tiny wooden clicks and a fire crackle"),
             ("\"It's doors all the way down,\" said Cat the penguin. \"I respect that.\"",
              "medium close-up", "CAT strokes her chin with one flipper and nods slowly", "CAT",
              "impressed and cheeky", "holds still", "a tiny penguin foot tap"),
         ]},
        {"title": "Three snowy lumps", "place": "hall",
         "angle": "Wide view down the long woven rug toward the open front door of",
         "who": "TICO stands in the open front doorway caked in snow with an icicle hanging from the tip of his "
                "huge rainbow beak and his wings wrapped around himself; GALLO and PINTO huddle together on top "
                "of a small striped suitcase, dusted white and shivering, a coconut and tiny sunglasses "
                "spilling out of it",
         "beats": [
             ("BANG! The big front door blew open. In tumbled three snowy lumps and one small suitcase.",
              "wide shot", "TICO stumbles in through the doorway and snow slides off his wings", "TICO",
              "frozen and bewildered", "pushes in", "a door bang and a gust of wind"),
             ("It was Tico the toucan, with Gallo the rice grain and Pinto the black bean.",
              "medium shot", "GALLO and PINTO shake the snow off together on top of the suitcase",
              ["GALLO", "PINTO"], "shivery and brave", "tilts down", "two tiny shivers and pattering snow"),
             ("They had come from Costa Rica on the mail-boat. Their suitcase held sunglasses and one coconut.",
              "close-up", "PINTO pats the coconut in the open suitcase and shrugs", "PINTO",
              "calm and a little sheepish", "pans right", "a hollow coconut knock"),
         ]},
        {"title": "Only when it's frozen", "place": "hall",
         "angle": "Medium view beside the copper cocoa urn in",
         "who": "HERSCHEL ladles steaming cocoa from the urn into three small mugs with twinkling eyes and a "
                "bushy smile; TICO stands by the fire with his rainbow beak chattering and the icicle still on "
                "its tip; MOM tucks one big knitted blanket around GALLO and PINTO on the hearth rug",
         "beats": [
             ("Tico's rainbow beak chattered. Clack-clack-clack. \"Is s-snow always this c-cold?\"",
              "medium close-up", "TICO's beak chatters fast and the icicle on its tip wobbles", "TICO",
              "freezing and amazed", "pushes in", "a quick clacking of a beak"),
             ("\"Only when it's frozen,\" said Herschel the walrus, and he ladled out three cocoas.",
              "medium shot", "HERSCHEL pours a ladle of cocoa into a small mug and his whiskers twitch",
              "HERSCHEL", "twinkly and kind", "tilts down", "a slow pour and a fire crackle"),
             ("\"**歡迎** (huānyíng) = Welcome!\" said Mom. She tucked one big blanket around all three.",
              "medium shot", "MOM wraps the knitted blanket snugly around GALLO and PINTO", ["MOM", "GALLO", "PINTO"],
              "warm and welcoming", "pans left", "a soft blanket rustle"),
         ]},
        {"title": "Las Posadas", "place": "hall",
         "angle": "Close view at mug height along the hearth of",
         "who": "GALLO stands on the rim of a cocoa mug with both tiny arms flung wide and his red bandana "
                "bright; PINTO sits beside him holding a thimble of cocoa with a calm smile; TICO leans in "
                f"wrapped in a blanket with his beak high; {ROSIE_CUP} listens with her little picture list "
                "ready in front of her cup",
         "beats": [
             ("Gallo thawed first. \"Rise and pinto! Tonight Las Posadas begins! At home we go door to door.\"",
              "medium close-up", "GALLO flings both tiny arms wide and bounces on the mug rim", "GALLO",
              "sunny and bursting", "pushes in", "a tiny tap on a mug rim"),
             ("\"We knock and ask: is there room?\" said Pinto. \"Door after door says no.\"",
              "medium close-up", "PINTO knocks twice on the side of the mug with one tiny arm", "PINTO",
              "calm and steady", "holds still", "two small knocks on a mug"),
             ("\"Beak the news!\" cried Tico. \"The last door says yes! That is the **posada** (poh-SAH-dah) = shelter.\"",
              "medium shot", "TICO throws his beak up high while ROSIE lifts her picture list", ["TICO", "ROSIE"],
              "loud and joyful", "tilts up", "a happy beak clack and a paper rustle"),
         ]},
        {"title": "Cabin Row", "place": "row", "time": "night",
         "angle": "Wide establishing view with deep perspective down the curving path of",
         "who": "CAT the little blue penguin glides ahead on her snowboard pointing one flipper down the row of "
                f"glowing doors; {ROSIE_CUP} stands on the stamped snow holding a small glowing brass lamp in "
                f"front of her cup, straw perked up; TICO steps along beside her wrapped in a blanket while {RIDERS}",
         "beats": [
             ("At dusk, Cat led them to Cabin Row. Little cabins. Glowing doors. Snow on every roof.",
              "wide shot", "CAT glides forward and sweeps one flipper along the row of glowing doors", "CAT",
              "proud and in charge", "pans right", "a snowboard hiss and a far crackle of chimneys"),
             ("Rosie carried a little lamp. Gallo and Pinto rode on Tico's beak, shaking tiny maracas. Chicka-chicka!",
              "medium shot", "TICO lifts his beak proudly and GALLO and PINTO shake their maracas on it",
              ["TICO", "GALLO", "PINTO"], "cozy and excited", "tracks beside", "a dry rattle of tiny maracas and crunching snow"),
             ("Rosie made a list. Knock. Ask. Giggle. Next door.",
              "medium close-up", "ROSIE holds her lamp steady and nods once at each step of her plan", "ROSIE",
              "serious and ready", "pushes in", "a soft crunch of snow"),
         ]},
        {"title": "Full of hats", "place": "row", "time": "night",
         "angle": "Low angle from the snowy doorstep looking up into the bright red doorway on",
         "who": "TORI stands in the open red cabin doorway with three knit hats stacked on her lid and her tiny "
                f"arms spread wide across the door, holding back a giggle; {ROSIE_CUP} stands on the doorstep "
                "holding her small glowing lamp in front of her cup, straw perked up; PINTO looks down "
                "from the tip of the long rainbow beak of TICO",
         "beats": [
             ("Knock, knock. \"Is there room?\" Tori opened the red door. \"Sorry! This cabin is full of hats.\"",
              "medium shot", "TORI spreads her tiny arms across the doorway and her stack of hats wobbles",
              "TORI", "playful and trying to look stern", "tilts up", "two knocks and a creak of a door"),
             ("She was wearing all of them. \"Beak the news!\" called Tico. \"Door one says no!\"",
              "medium close-up", "TICO throws his beak up high and PINTO holds on to his straw hat",
              ["TICO", "PINTO"], "loud and delighted", "pans right", "a happy beak clack and a rattle of maracas"),
         ]},
        {"title": "Full of penguin", "place": "row", "time": "night",
         "angle": "Medium view straight into the open blue doorway on",
         "who": "CAT the little blue penguin lies sprawled sideways across the whole blue cabin doorway with "
                f"her flippers behind her head and a huge grin; TICO peers in over her while {RIDERS}, both "
                "leaning forward to look",
         "beats": [
             ("Cat had zoomed ahead to the blue door. \"No room! This cabin is full of penguin.\"",
              "medium shot", "CAT stretches out across the doorway and crosses her feet", "CAT",
              "smug and delighted", "pushes in", "a door creak and a lazy flipper flap"),
             ("It was one penguin, lying sideways.",
              "wide shot", "TICO tilts his head at the doorway and GALLO and PINTO tilt theirs the same way",
              ["TICO", "GALLO", "PINTO"], "puzzled and amused", "pulls back", "a soft crunch of snow"),
         ]},
        {"title": "Most of the room", "place": "row", "time": "night",
         "angle": "Low angle from the path looking up at the green doorway on",
         "who": "HERSCHEL fills the entire green cabin doorway from side to side, tusks, whiskers and cocoa "
                f"apron, with an apologetic twinkle; {ROSIE_CUP} stands below him holding her small glowing lamp "
                "in front of her cup, straw up, giggling",
         "beats": [
             ("Knock, knock. The green door opened. It was all walrus, from side to side.",
              "wide shot", "HERSCHEL squeezes forward until he fills the whole green doorway", "HERSCHEL",
              "solemn and twinkling", "tilts up", "two knocks and a groan of a door frame"),
             ("\"No room, I'm afraid,\" said Herschel. \"I am most of the room.\"",
              "medium shot", "HERSCHEL spreads his flippers sadly and his whiskers twitch", "HERSCHEL",
              "apologetic and amused", "holds still", "a deep creak of a door frame"),
             ("Rosie giggled so hard her lamp wobbled. Chicka-chicka went the maracas. One door to go!",
              "medium close-up", "ROSIE giggles and her straw springs back up", "ROSIE", "giggly and eager",
              "pushes in", "a wobbling lamp rattle and a soft crunch of snow"),
         ]},
        {"title": "The last door", "place": "row", "time": "night",
         "angle": "Wide view at the far end of",
         "who": "MOM stands beside one huge rounded snowdrift with only a stone chimney and the tip of a roof "
                "poking out of the top, holding a snow shovel and a flask of cocoa, her face gentle and sorry; "
                f"TICO stops short in front of the drift with his beak hanging open while {RIDERS}, staring up",
         "beats": [
             ("The last door was their own guest cabin. Mom was waiting there to say yes.",
              "wide shot", "MOM lifts the cocoa flask in a small wave and lowers it again", "MOM",
              "welcoming, then sorry", "pushes in", "a soft crunch of snow and a slosh in a flask"),
             ("But there was no door. There was a snowdrift with a chimney on top.",
              "medium shot", "TICO looks slowly up the huge snowdrift to the chimney and his beak drops open",
              "TICO", "stunned", "tilts up", "a soft slump of sliding snow"),
             ("\"The roof slid,\" said Mom. \"It's snow right up to the ceiling.\"",
              "medium close-up", "MOM pats the drift with her shovel and shakes her head", "MOM",
              "practical and sorry", "pans left", "a muffled shovel pat on snow"),
         ]},
        {"title": "Not a game", "place": "row", "time": "night",
         "angle": "Close view at beak height in the falling snow on",
         "who": "TICO hugs his blanket tight with his rainbow beak chattering and his eyes worried; GALLO and "
                f"PINTO press close together under his chin; {ROSIE_CUP} looks up at the three of them with "
                "her straw drooping, her small glowing lamp in front of her cup",
         "beats": [
             ("Tico's beak began to chatter again. Clack-clack-clack. Even the maracas went quiet.",
              "medium close-up", "TICO's beak chatters as GALLO and PINTO press closer under his chin",
              ["TICO", "GALLO", "PINTO"], "cold and worried", "pushes in", "a quick clacking of a beak"),
         ]},
        {"title": "Rosie is the last door", "place": "row", "time": "night",
         "angle": "Heroic low angle looking up at a small cup on a snowy step in",
         "who": f"{ROSIE_CUP} stands tall on a snowy step holding her small glowing brass lamp in front of her "
                f"cup, straw straight up, eyes bright and sure; TICO bends down toward her while {RIDERS}, all "
                "three with widening hopeful eyes, gold lamplight on their faces",
         "beats": [
             ("\"The last door says yes,\" said Rosie. \"So I'll be the last door.\"",
              "medium shot", "ROSIE hops up onto the snowy step and holds her lamp out in front of her cup",
              "ROSIE", "brave and certain", "tilts up", "one soft hop in snow"),
             ("Nobody had asked. Rosie said it anyway. \"**有位子** (yǒu wèizi) = There's room! Room with us.\"",
              "medium close-up", "TICO's beak stops chattering and GALLO and PINTO throw up their tiny arms",
              ["TICO", "GALLO", "PINTO"], "relief bursting into joy", "pushes in", "a happy beak clack and a rattle of maracas"),
             ("Tico was speechless. For a toucan, that is very big news.",
              "close-up", "TICO opens his beak, closes it again and blinks his round eyes", "TICO",
              "moved beyond words", "holds still", "one soft click of a beak"),
         ]},
        {"title": "A big squish", "place": "row", "time": "night",
         "angle": "Warm close two-shot under the brass lamp post on",
         "who": f"TORI bends down close with her three stacked hats sliding sideways and a proud grin; "
                f"{ROSIE_CUP} looks up at her holding the small glowing lamp in front of her cup, straw wiggling",
         "beats": [
             ("\"Our bunk room is small, little sip,\" said Tori. \"Then we'll squish,\" said Rosie.",
              "medium close-up", "TORI bends down and ROSIE's straw wiggles back at her", ["TORI", "ROSIE"],
              "doubtful, then charmed", "pushes in", "a soft crunch of snow"),
             ("Tori grinned. \"You've got this. I'll find more pillows.\"",
              "medium close-up", "TORI grins and her stack of hats slides over one eye", "TORI",
              "proud and game", "holds still", "a soft woolly flop"),
         ]},
        {"title": "Lantern sixteen", "place": "lane", "time": "night",
         "angle": "Low angle looking up along the string of lanterns over",
         "who": "TICO stretches up on his toes and hooks a turquoise paper lantern onto the long string with "
                f"the tip of his rainbow beak; {ROSIE_CUP} stands below holding her small glowing lamp in front "
                "of her cup, straw high; TORI steadies a snowy crate for him with her stack of hats sliding",
         "beats": [
             ("On the way home they hung lantern sixteen on Lantern Lane. Turquoise, like the sea back home.",
              "wide shot", "TICO stretches up and slips the turquoise lantern onto its hook with his beak",
              "TICO", "careful and proud", "tilts up", "a tiny click of a hook and a creak of string"),
             ("\"One more light,\" said Rosie. The snow came down turquoise all around it.",
              "medium shot", "ROSIE lifts her lamp toward the lantern and her straw wiggles", "ROSIE",
              "glad and glowing", "pushes in", "a soft crunch of snow and a far sizzle of a grill"),
         ]},
        {"title": "Coconut cocoa", "place": "lane", "time": "night",
         "angle": "Medium view beside the steaming cocoa cart on",
         "who": "HERSCHEL holds a coconut neatly cracked in two halves on the tip of one long tusk, whiskers "
                "twinkling, his cocoa ladle in the other flipper; GALLO and PINTO dance side by side on the "
                "roof of the cocoa cart shaking tiny maracas; CAT the little blue penguin holds up a mug with "
                "both flippers",
         "beats": [
             ("Herschel cracked the coconut on one tusk. Tock! \"Coconut cocoa,\" he said. \"A first for Frostpeak.\"",
              "medium shot", "HERSCHEL taps the coconut on his tusk and it falls neatly into two halves",
              "HERSCHEL", "proud and twinkly", "pushes in", "one hollow tock and a slow pour"),
             ("\"**Pura vida** (POO-rah VEE-dah) = Life is good!\" sang Gallo and Pinto. Cat asked for seconds.",
              "medium close-up", "GALLO and PINTO shake their maracas while CAT lifts her mug higher",
              ["GALLO", "PINTO", "CAT"], "warm at last and merry", "pans right", "a dry rattle of tiny maracas"),
         ]},
        {"title": "Seven friends and a beak", "place": "bunk", "time": "night",
         "angle": "High angle from the top bunk looking down over the crowded room in",
         "who": "TICO lies in the lower bunk under a patchwork quilt with his long rainbow beak sticking far "
                "out past the edge and resting on its own small pillow, eyes half closed; GALLO and PINTO lie "
                "side by side sharing one big pillow, tucked in like two peas; TORI plumps an armful of extra "
                "pillows; MOM spreads one more quilt",
         "beats": [
             ("One bunk room. Seven friends. Eight, counting Tico's beak, which needed its own pillow.",
              "wide shot", "TICO wriggles under the quilt and his long beak settles onto its own pillow", "TICO",
              "snug and thawed", "pulls back", "a soft quilt rustle and a creak of a bunk"),
             ("Gallo and Pinto shared a pillow. \"Better together,\" yawned Pinto.",
              "medium close-up", "PINTO yawns and GALLO snuggles closer on their shared pillow",
              ["PINTO", "GALLO"], "drowsy and content", "pushes in", "one tiny yawn"),
             ("Mom counted lids, beaks and beans. \"All in,\" she said, and spread one more quilt.",
              "medium shot", "MOM spreads one more quilt over the bunk and smooths it down", "MOM",
              "calm and satisfied", "tilts down", "a soft quilt flap"),
         ]},
        {"title": "The windowsill", "place": "bunk", "time": "night",
         "angle": "Medium view across the lower bunk toward the frosted round window in",
         "who": "CAT the little blue penguin sits on the sill of the frosted round window with a small cushion, "
                f"one flipper raised as if explaining, chin up; {ROSIE_CUP} sits tucked at the edge of the "
                "crowded bunk with her straw wiggling, looking around at the full room with shining eyes",
         "beats": [
             ("Cat took the windowsill. \"Penguins like a draft.\" Nobody believed her. Everybody thanked her.",
              "medium shot", "CAT plumps her small cushion on the windowsill and lifts her chin", "CAT",
              "noble and a bit chilly", "pans right", "a cushion pat and a soft tick of snow on glass"),
             ("It was a squish. It was the best squish Rosie had ever been in.",
              "medium close-up", "ROSIE looks slowly around the full room and her straw wiggles", "ROSIE",
              "squashed and very happy", "pushes in", "a soft quilt rustle and sleepy breathing"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the crowded lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; TICO asleep beside her with his long rainbow beak sticking out of the quilt; GALLO and "
                "PINTO asleep side by side on one pillow; CAT the little blue penguin asleep curled on a "
                "cushion on the windowsill, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, the door that said yes. Goodnight, Tico, beak out in the cool.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, rice and bean, side by side. May there always be room for you, and one pillow more.",
              "medium close-up", "CAT settles deeper into her cushion with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, the door that said yes.",
        "Goodnight, Tico, beak out in the cool.",
        "Goodnight, rice and bean, side by side.",
        "May there always be room for you, and one pillow more.",
    ],
}
