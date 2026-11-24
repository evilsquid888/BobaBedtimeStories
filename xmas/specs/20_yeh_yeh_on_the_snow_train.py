"""20 — Yeh Yeh on the Snow Train (Sunday, December 20)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

PLATFORM = ("a little red snow train puffing white steam at a wooden station platform, a brass station bell, "
            "a stack of leather suitcases, a wooden trail post carved with a plain picture of a lodge, frosted fir "
            "trees, a wooden sled with a red rope")

STORY = {
    "num": "20",
    "slug": "yeh-yeh-on-the-snow-train",
    "title": "Yeh Yeh on the Snow Train",
    "meta": [
        ("Day", "Sunday, December 20 · door twenty"),
        ("Holiday thread", "Grandpa arrives: Yeh Yeh comes to Frostpeak on the snow train"),
        ("Guests", "Yeh Yeh the clay teapot (arrives today), Piper Paddlefoot ❄️, Willa Wobble ❄️"),
        ("Cat’s role", "station guide and cloud collector (catches Yeh Yeh's frozen steam puffs in her scarf)"),
        ("Mandarin", "爺爺 grandpa · 慢慢來 take it slow · 你看 look"),
        ("Setting", "The Door Wall in the lodge great hall, then the snowy path from Frostpeak Station up to the "
                    "lodge, Lantern Lane at night, and the bunk room"),
    ],
    "palette": "snowy cream and warm teapot brown with saturated icy turquoise and golden amber accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "YEHYEH", "PIPER", "WILLA"],
    "cast_note": "Humans in this story: none. Yeh Yeh walks slowly with his bamboo stick; in the cold his steam "
                 "freezes into tiny white clouds. The fox tracks are only tracks: no fox is drawn.",
    "key_shot": 12,
    "places": {
        "doorwall": DOORWALL,
        "path": {
            "name": "the snowy path from Frostpeak Station up to the lodge",
            "scene": "the snowy station path",
            "props": "a winding snowy path between frosted fir trees, a wooden trail post carved with a plain "
                     "picture of a lodge, a line of tiny fox tracks in the snow, a frozen waterfall of blue icicles "
                     "on a rock wall, a mossy log half buried in snow, a little red snow train far behind",
            "light": "Low golden winter sun slants through the firs in long beams",
            "accents": "teapot brown and icy turquoise",
            "atmo": "Puffs of breath hang in the cold air and snow sparkles on the branches",
            "motion": "sparkles of snow sift down from the fir branches",
        },
        "lane_night": LANE_NIGHT,
        "bunk": bunk("a tiny brown teapot and a little jar holding one small white cloud on the nightstand"),
    },
    "shots": [
        {"title": "Door twenty", "place": "doorwall",
         "angle": "Close view at knob height along the rows of little carved doors in",
         "who": f"{ROSIE_CUP} stands on a wooden step stool before one open little door with a tiny brown clay "
                "teapot the size of a button inside it, straw shooting straight up; MOM stands beside her holding "
                "a picture postcard with a plain doodle of a train, smiling",
         "beats": [
             ("Door twenty! Behind it sat a tiny brown teapot, no bigger than a button.",
              "close-up", "ROSIE leans toward the tiny teapot in the open little door", "ROSIE",
              "curious and hopeful", "pushes in", "a tiny door creak and a crackling fire"),
             ("Rosie's straw shot straight up. A teapot! That could only mean one thing.",
              "medium close-up", "ROSIE gasps and her straw shoots straight up", "ROSIE",
              "thrilled and breathless", "tilts up", "a crackling fire and a tiny hop on wood"),
             ("\"Yeh Yeh got your postcard,\" said Mom, smiling. \"His train comes at three.\"",
              "medium shot", "MOM holds up the postcard and nods", "MOM",
              "warm and glad", "holds still", "a paper rustle and a crackling fire"),
         ]},
        {"title": "Four things before dark", "place": "doorwall",
         "angle": "Low angle from the long woven rug looking up past the antler coat rack in",
         "who": f"{ROSIE_CUP} holds a little picture list in front of her cup, the list showing four plain doodles "
                "of a little door, a snowy bump, a mug and a lantern, eyes busy; CAT the little blue penguin "
                "winds her yellow scarf around her neck with a confident grin",
         "beats": [
             ("Rosie made a list. Door Wall. Bunny Bump. Cocoa. Lantern. \"All before dark!\"",
              "medium close-up", "ROSIE taps each doodle on her list with one tiny arm", "ROSIE",
              "busy and excited", "pushes in", "a paper rustle and quick little taps"),
             ("\"Easy,\" said Cat the penguin. \"The station path takes five minutes. Two, on your belly.\"",
              "medium shot", "CAT flicks her scarf over her shoulder and pats her tummy", "CAT",
              "breezy and sure", "pans right", "a soft scarf flap and a crackling fire"),
         ]},
        {"title": "The snow train", "place": "path",
         "angle": "Wide establishing view from the platform end of",
         "props": PLATFORM,
         "who": "YEHYEH stands in the open train door leaning on his little bamboo walking stick, a curl of steam "
                f"rising from his lid, eyes crinkled; {ROSIE_CUP} waits on the snowy platform with her straw "
                "perked up; TORI waits beside her on tiptoe, green straw bobbing",
         "beats": [
             ("Chuff, chuff, hiss. The little red snow train rolled in. One door opened. Very slowly.",
              "wide shot", "ROSIE bounces once on the platform as steam drifts along the train", "ROSIE",
              "eager and wiggly", "pushes in", "a long hiss of steam and a brass bell"),
             ("Out stepped a round old teapot with a bamboo stick. Tap. Tap. Tap.",
              "medium shot", "YEHYEH taps his bamboo stick on the platform and steps down slowly", "YEHYEH",
              "unhurried and twinkly", "tilts down", "a slow tap of bamboo on wood"),
         ]},
        {"title": "Grandpa!", "place": "path",
         "angle": "Warm close view at teapot height on the platform end of",
         "props": PLATFORM,
         "who": "YEHYEH stands in the middle with his lid tipped and his spectacles crooked, chuckling, a picture "
                f"postcard tucked under one tiny arm; {ROSIE_CUP} presses against one side of him, straw wiggling; "
                "TORI presses against his other side with a huge smile",
         "beats": [
             ("\"**爺爺** (yéye) = Grandpa!\" Rosie and Tori squeezed him so tight his lid rattled.",
              "medium close-up", "ROSIE and TORI lean in close against YEHYEH and his lid rattles",
              ["ROSIE", "TORI", "YEHYEH"], "overjoyed and squished", "pushes in", "a clay lid rattle and happy squeaks"),
             ("\"Your postcard came all the way from Montreal,\" chuckled Yeh Yeh. \"So I came all the way here.\"",
              "close-up", "YEHYEH pats the postcard under his arm and chuckles", "YEHYEH",
              "fond and amused", "holds still", "a soft kettle hiss"),
         ]},
        {"title": "Slide into it!", "place": "path",
         "angle": "Dynamic diagonal view along the snowy edge of the platform on",
         "props": PLATFORM,
         "who": "PIPER skids sideways on her glittery blue snowboard in a spray of snow, towing a wooden sled by "
                "its red rope, one flipper pointing up the hill; YEHYEH looks at the sled over the top of his "
                "spectacles with one bushy eyebrow raised",
         "beats": [
             ("WHOOSH! Piper Paddlefoot skidded up, towing a sled. \"Slide into it! Lodge in one minute flat!\"",
              "wide shot", "PIPER skids to a stop in a spray of snow and pats the sled", "PIPER",
              "speedy and proud", "pans right", "a long swoosh and a spray of snow"),
             ("Yeh Yeh eyed the sled. \"One minute? Then what would I do with the afternoon?\"",
              "medium close-up", "YEHYEH peers at the sled over his spectacles and raises one eyebrow", "YEHYEH",
              "amused and unhurried", "pushes in", "a soft kettle hiss"),
             ("\"**慢慢來** (màn man lái) = take it slow. Slow tea is the best tea. I will walk.\"",
              "medium shot", "YEHYEH plants his bamboo stick in the snow and a puff of steam pops from his lid",
              "YEHYEH", "calm and decided", "holds still", "one firm tap of bamboo in snow"),
         ]},
        {"title": "Tap. Tap. Tap.", "place": "path",
         "angle": "High angle looking down through the fir branches at",
         "who": "YEHYEH walks slowly up the middle of the path leaning on his bamboo stick; PIPER swoops around him "
                "in a wide circle on her snowboard, leaving a ring of tracks; CAT the little blue penguin hops "
                "from foot to foot beside him with her flippers twitching",
         "beats": [
             ("So they walked. Tap. Tap. Tap. Piper circled the whole family on her board. Four times.",
              "wide shot", "PIPER swoops in a wide circle around YEHYEH on her snowboard", ["PIPER", "YEHYEH"],
              "restless and zippy", "tracks beside", "a looping swoosh and a slow bamboo tap"),
             ("Cat hopped from foot to foot. \"Yeh Yeh, the snow will melt before we get there!\"",
              "medium shot", "CAT hops from one pink foot to the other and waves both flippers", "CAT",
              "fidgety and impatient", "pushes in", "quick little hops in snow"),
             ("\"In spring,\" said Yeh Yeh. \"We will arrive long before then. Probably.\"",
              "medium close-up", "YEHYEH chuckles and takes one more slow step beside CAT", ["YEHYEH", "CAT"],
              "twinkly and teasing", "holds still", "a slow bamboo tap and a puff of steam"),
         ]},
        {"title": "Not last", "place": "path",
         "angle": "Low angle at snow level along the trail of footprints on",
         "who": "WILLA takes one tiny careful step beside a small round footprint, purple earmuffs fluffy, looking "
                "up with a shy glad smile; YEHYEH bends a little toward her, leaning on his bamboo stick, nodding",
         "beats": [
             ("Only tiny Willa Wobble was happy. For once she was not last. She was tied.",
              "medium shot", "WILLA takes one tiny step and looks up beside YEHYEH", ["WILLA", "YEHYEH"],
              "shy and delighted", "tracks beside", "a tiny crunch of snow and a slow bamboo tap"),
             ("\"The smallest step is still a step,\" she whispered. Yeh Yeh nodded. \"A wise penguin.\"",
              "medium close-up", "YEHYEH nods slowly down at WILLA and she stands a little taller",
              ["YEHYEH", "WILLA"], "kind and proud", "pushes in", "a soft kettle hiss"),
         ]},
        {"title": "Four things, and the sun going down", "place": "path",
         "angle": "Close view over a little picture list toward the long shadows on",
         "who": f"{ROSIE_CUP} holds her little picture list of four plain doodles in front of her cup and looks up "
                "at the low sun between the firs, her straw drooping",
         "beats": [
             ("Rosie looked at her list. Four things! The sun was already sliding down the firs.",
              "medium close-up", "ROSIE looks from her list up to the low sun", "ROSIE",
              "anxious and counting", "tilts up", "wind in the firs and a far bamboo tap"),
             ("Her straw drooped. At teapot speed, they would never fit it all in.",
              "close-up", "ROSIE's straw droops slowly over her list", "ROSIE",
              "fretful and counting", "holds still", "wind in the firs"),
         ]},
        {"title": "Mom packed snacks", "place": "path",
         "angle": "Medium view beside the carved trail post on",
         "who": "MOM holds open a little cloth bag of golden pineapple cakes with a calm smile; TORI bends down "
                f"beside ROSIE and tucks a folded list under her own cup sleeve; {ROSIE_CUP} looks up at her big "
                "sister with her straw half lifted",
         "beats": [
             ("Mom was not worried. She had walked with Yeh Yeh before. She had packed snacks.",
              "medium shot", "MOM opens her little cloth bag and holds out a pineapple cake", "MOM",
              "calm and prepared", "pans left", "a cloth rustle and a crinkle of wrappers"),
             ("Tori tucked the list away. \"It can wait. Yeh Yeh is here now. You've got this, little sip.\"",
              "medium close-up", "TORI tucks the folded list under her sleeve and leans close to ROSIE",
              ["TORI", "ROSIE"], "gentle and sure", "pushes in", "a paper fold and wind in the firs"),
         ]},
        {"title": "Tap. Hop. Tap. Hop.", "place": "path",
         "angle": "Low side view at snow level, two small figures side by side, on",
         "who": f"{ROSIE_CUP} stands in the snow beside YEHYEH in the middle of one small hop, straw up, eyes on "
                "his stick; YEHYEH leans on his bamboo walking stick beside her with a pleased sideways glance, "
                "steam curling from his lid",
         "beats": [
             ("Then Rosie matched his steps. Tap. Hop. Tap. Hop.",
              "medium shot", "ROSIE takes one small hop in time with the tap of the stick beside YEHYEH",
              ["ROSIE", "YEHYEH"], "steady and content", "tracks beside", "a bamboo tap and a soft hop, in rhythm"),
         ]},
        {"title": "Fox tracks", "place": "path",
         "angle": "Close view at snow level along a wiggly line of tiny paw prints on",
         "who": "YEHYEH points the tip of his bamboo stick at a line of tiny paw prints in the snow, eyes twinkling "
                f"behind his spectacles; {ROSIE_CUP} leans over the tracks with round eyes; CAT the little blue "
                "penguin crouches low with her beak almost touching the snow",
         "beats": [
             ("\"**你看** (nǐ kàn) = look,\" said Yeh Yeh. He pointed his stick at the snow.",
              "medium shot", "YEHYEH lowers the tip of his stick toward the snow", "YEHYEH",
              "quiet and pleased", "tilts down", "a soft bamboo tap in snow"),
             ("Fox tracks! Tiny ones, in a wiggly line, with a tail swish.",
              "close-up", "ROSIE leans over the tiny tracks and her straw perks up", "ROSIE",
              "amazed and hushed", "pans right", "a hush of wind over snow"),
             ("They led under a mossy log. \"Somebody is home,\" whispered Cat. Everybody tiptoed.",
              "medium close-up", "CAT lifts one flipper to her beak and rises onto her tiptoes", "CAT",
              "hushed and gleeful", "pushes in", "tiny tiptoe crunches in snow"),
         ]},
        {"title": "The waterfall that stopped", "place": "path",
         "angle": "Low angle looking up at a tall frozen waterfall of blue icicles beside",
         "who": "PIPER stands frozen mid-skid on her snowboard with her beak hanging open, staring up; WILLA stands "
                "beside her, tiny and calm, one little flipper pointing up at the ice; YEHYEH gazes up with his "
                "spectacles full of blue light",
         "beats": [
             ("Around the bend hung a frozen waterfall, blue as a marble, stopped mid-splash.",
              "wide shot", "YEHYEH tips his head back and blue light slides over his spectacles", "YEHYEH",
              "full of wonder", "tilts up", "a faint tinkle of icicles"),
             ("Piper skidded to a stop. \"I zoom past here every day! Has that always been there?\"",
              "medium shot", "PIPER stares up at the ice with her beak hanging open", "PIPER",
              "astonished and sheepish", "pushes in", "a short skid in snow and a tinkle of icicles"),
             ("\"Every day,\" said Willa softly. \"I see it. I'm slow.\"",
              "medium close-up", "WILLA points one tiny flipper up at the ice and smiles", "WILLA",
              "quietly proud", "holds still", "a faint tinkle of icicles"),
         ]},
        {"title": "Icicle music", "place": "path",
         "angle": "Close low angle along a row of long blue icicles at the foot of the frozen waterfall beside",
         "who": "YEHYEH taps one long icicle with the tip of his bamboo walking stick, head tilted to listen, "
                "eyes merry; CAT the little blue penguin stands on a snowy rock with both flippers raised over a "
                "row of icicles like a drummer; PIPER stands behind them in the middle of a wiggly dance, "
                "flippers out",
         "beats": [
             ("Yeh Yeh tapped one icicle with his stick. Ting! The whole waterfall rang like a bell.",
              "close-up", "YEHYEH taps an icicle with his stick and tilts his head to listen", "YEHYEH",
              "curious and delighted", "pushes in", "one clear icy chime ringing on"),
             ("Cat played it like a xylophone. Ting, tang, tong! Piper danced on the spot.",
              "medium shot", "CAT taps icicles with both flippers while PIPER wiggles in a dance", ["CAT", "PIPER"],
              "gleeful and musical", "pans right", "bright icy chimes up and down"),
         ]},
        {"title": "Cloud collector", "place": "path",
         "angle": "Close view at lid height beside a curl of white steam on",
         "who": "YEHYEH puffs a round wisp of steam from his lid that hangs in the cold air as a tiny white cloud, "
                "eyes merry; CAT the little blue penguin holds her yellow scarf open like a basket with three "
                "tiny white clouds already in it, tongue out in concentration",
         "beats": [
             ("They even saw their own breath. Puff. Yeh Yeh's steam froze into a tiny white cloud.",
              "close-up", "YEHYEH puffs and a tiny white cloud pops from his lid and hangs in the air", "YEHYEH",
              "merry and surprised", "tilts up", "a soft kettle puff"),
             ("Puff. Another. Cat caught them in her scarf. \"This one looks like a dumpling.\"",
              "medium close-up", "CAT scoops a tiny cloud into her open scarf and peers at it", "CAT",
              "focused and tickled", "pans right", "a soft kettle puff and a scarf flap"),
         ]},
        {"title": "Slow is hard", "place": "path",
         "angle": "Medium view from behind a snowy fir branch on",
         "who": "PIPER walks on her own two feet with her glittery blue snowboard tucked under one flipper, wobbling "
                "a little, eyes wide and looking all around; WILLA walks beside her with an encouraging smile",
         "beats": [
             ("Piper tucked her board under one flipper and walked. \"Slow is hard,\" she puffed.",
              "medium shot", "PIPER takes one wobbly step with her board under her flipper beside WILLA",
              ["PIPER", "WILLA"], "wobbly and trying", "tracks beside", "careful crunching steps in snow"),
             ("\"But I've counted eleven new things. Twelve! That tree has a face.\"",
              "medium close-up", "PIPER points one flipper at a knobbly fir trunk and gasps", "PIPER",
              "amazed and delighted", "pans left", "a creak of a fir branch and wind in the firs"),
         ]},
        {"title": "One whole hour", "place": "path",
         "angle": "Wide view up the last bend toward a snowy lodge roof with smoking chimneys at the top of",
         "props": "a big log lodge with smoking chimneys and glowing windows, a wide snowy porch, a winding path "
                  "between frosted fir trees, a wooden trail post carved with a plain picture of a lodge, one long "
                  "line of small footprints and round stick marks",
         "who": f"{ROSIE_CUP} stands at the top of the path in late golden sun with her straw high; YEHYEH stands "
                "beside her leaning on his bamboo stick, steam curling gold from his lid; CAT the little blue "
                "penguin stands behind them with her scarf bundled full of tiny white clouds",
         "beats": [
             ("They reached the lodge in one whole hour. Nobody minded. Not even Cat. Much.",
              "wide shot", "CAT hugs her bundled scarf and gives a small shrug", "CAT",
              "content and a little surprised", "pulls back", "slow steps in snow and a far door creak"),
             ("\"Door Wall, Bunny Bump, cocoa,\" said Rosie. \"Tomorrow. Màn man lái.\" Yeh Yeh's lid rattled.",
              "medium close-up", "ROSIE looks up at YEHYEH and his lid rattles as he chuckles", ["ROSIE", "YEHYEH"],
              "easy and proud", "pushes in", "a clay lid rattle and a soft puff of steam"),
         ]},
        {"title": "Teapot brown", "place": "lane_night", "time": "night",
         "angle": "Low angle looking up at the long lantern string above",
         "who": "YEHYEH holds a long thin lighting taper up to a round teapot-brown paper lantern with a little "
                f"curly spout, taking his time, spectacles glowing; {ROSIE_CUP} stands on a snowy crate beside him "
                "with her straw high; MOM steadies the lantern on its hook with one tiny arm; TORI looks up "
                "beside her with a soft smile",
         "beats": [
             ("That night they hung the day's lantern, teapot brown, with a little curly spout.",
              "medium shot", "MOM settles the brown lantern on its hook while TORI looks up", ["MOM", "TORI"],
              "careful and glad", "tilts up", "a soft paper rustle and a far sizzle"),
             ("Yeh Yeh lit it. He took his time. Nobody hurried him. It glowed like warm tea.",
              "close-up", "YEHYEH lifts his long taper slowly and the lantern begins to glow", "YEHYEH",
              "patient and precise", "pushes in", "a tiny flicker and a soft paper rustle"),
             ("\"One more light,\" said Rosie. Then she whispered the plan: a surprise for SpicySquid's birthday.",
              "medium close-up", "ROSIE leans close to YEHYEH and her straw wiggles", ["ROSIE", "YEHYEH"],
              "excited and hushed", "holds still", "a soft hush of falling snow"),
         ]},
        {"title": "A lid on it", "place": "lane_night", "time": "night",
         "angle": "Warm close view under the glowing lanterns in",
         "who": "YEHYEH taps the lid on his own head with one tiny arm and winks, steam curling up into the "
                "lantern light; CAT the little blue penguin clutches her scarf full of tiny white clouds and "
                "laughs with her beak wide open",
         "beats": [
             ("\"I can keep a surprise,\" said Yeh Yeh. \"I am a teapot. I keep a lid on it.\"",
              "medium close-up", "YEHYEH taps his own lid and winks while CAT laughs", ["YEHYEH", "CAT"],
              "sly and delighted", "pushes in", "a tiny clay tap and a happy squeak"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably closed; "
                "CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, yellow scarf "
                "visible",
         "beats": [
             ("Goodnight, little sip, tucked in at last. Goodnight, Yeh Yeh, tap, tap, tap.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Cat, with a cloud in your scarf. May your dreams ring like icicles: ting, tang, tong.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, tucked in at last.",
        "Goodnight, Yeh Yeh, tap, tap, tap.",
        "Goodnight, Cat, with a cloud in your scarf.",
        "May your dreams ring like icicles: ting, tang, tong.",
    ],
}
