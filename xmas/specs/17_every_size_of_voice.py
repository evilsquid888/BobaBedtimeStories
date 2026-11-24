"""17 — Every Size of Voice. Market Train to Montreal: carol practice at the Old Port, and two very small voices."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
BELL = "a tiny brass bell"

STORY = {
    "num": "17",
    "slug": "every-size-of-voice",
    "title": "Every Size of Voice",
    "meta": [
        ("Day", "Thursday, December 17 · door seventeen · Market Train to Montreal"),
        ("Holiday thread", "Carol practice for the market sing-along at the Old Port of Montreal: "
                           "\"Vive le vent\", which is Jingle Bells in French"),
        ("Guests", "Cleo Coldwater ❄️ (conducting), Finnegan Flipsworth ❄️ (too loud), Sésame the Montreal "
                   "bagel ⚜️, Couic the cheese curd ⚜️ (new; one squeak is his whole voice), Kyle the black "
                   "bear cub (the rumble)"),
        ("Cat’s role", "the beat: knows where carol practice is, and beatboxes under the whole song "
                       "(every carol needs a drop)"),
        ("Mandarin", "鈴鐺 bell · 唱歌 sing"),
        ("French", "Bonjour-hi the Montreal hello · Vive le vent long live the wind · couic squeak"),
        ("Setting", "The Door Wall, then by Market Train to the little bandstand at the Old Port of Montreal, "
                    "beside the skating rink and the giant Ferris wheel; Lantern Lane and the bunk room at night"),
    ],
    "palette": "frosty blue and old-stone grey with saturated brass yellow and tuque red accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "COLDWATER", "FINNEGAN", "SESAME", "COUIC", "KYLE"],
    "cast_note": "Humans in this story: none. Couic is very tiny, about the size of Rosie's bell. Cleo "
                 "conducts with her paintbrush. Tickets, stalls and awnings show plain little pictures only.",
    "key_shot": 16,
    "places": {
        "hall": DOORWALL,
        "port": {
            "name": "the little bandstand at the Old Port of Montreal",
            "scene": "the Old Port bandstand",
            "props": "a small eight-sided wooden bandstand with a big brass bell hanging under its snowy roof, "
                     "a skating rink scored with fresh blade lines, a row of empty wooden benches, a giant Ferris wheel, a little "
                     "poutine stand with rising steam, strings of round glass bulbs between the lamp posts, "
                     "the grey stone buildings and silver domes of the old city behind",
            "light": "Low golden winter sun glows on the ice and the old stone",
            "accents": "brass yellow and tuque red",
            "atmo": "Puffs of frosty breath hang in the cold air",
            "motion": "puffs of frosty breath hang in the cold air",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny golden train ticket and a tiny brass bell on the nightstand"),
    },
    "shots": [
        {"title": "Door seventeen", "place": "hall",
         "angle": "Low angle looking up the tall wall of little carved doors in",
         "who": f"{ROSIE_CUP} stands by a little open door holding a tiny golden train ticket with {BELL} tied "
                "to it in front of her cup, straw wiggling; TORI leans down to look with a knowing smile; "
                "CAT the little blue penguin throws both flippers in the air",
         "beats": [
             ("Rosie opened door seventeen. Inside lay a tiny golden train ticket with a bell tied on.",
              "close-up", "ROSIE lifts the golden ticket in front of her cup and the tiny bell swings", "ROSIE",
              "curious and pleased", "pushes in", "a soft wooden click and one tiny ting"),
             ("Rosie shook the **鈴鐺** (língdāng) = bell. Ting! \"A ticket means the Market Train,\" said Tori.",
              "medium shot", "ROSIE shakes the tiny bell while TORI taps the golden ticket", ["ROSIE", "TORI"],
              "delighted and in the know", "tilts up", "a bright tiny ting and a fire crackle"),
             ("\"Montreal!\" said Cat the penguin. \"Today we **唱歌** (chànggē) = sing. Bring your loudest beak.\"",
              "medium close-up", "CAT throws both flippers up and bounces on her toes", "CAT",
              "thrilled and bossy", "pans right", "a bouncing penguin patter"),
         ]},
        {"title": "The Old Port", "place": "port",
         "angle": "Wide establishing view with deep perspective across the skating rink toward",
         "who": "CAT the little blue penguin stands out in front on the snow pointing one flipper at the "
                f"bandstand; MOM stands behind with a calm smile and a flask of cocoa; TORI stands beside {ROSIE_CUP} "
                "who stands looking up at the giant Ferris wheel with her straw tipped right back",
         "beats": [
             ("The Market Train ran south all morning. By lunchtime they were at the Old Port of Montreal.",
              "wide shot", "CAT plants her feet and points one flipper at the little bandstand", "CAT",
              "eager and leading", "pans right", "a far train whistle and a soft crunch of snow"),
         ]},
        {"title": "Bonjour-hi", "place": "port",
         "angle": "Low angle at snow level in front of the poutine stand at",
         "who": f"SESAME bounces high in the air with both tiny arms wide, his red tuque flying; {ROSIE_CUP} "
                "looks up at him with her straw perked and the golden ticket in front of her cup",
         "beats": [
             ("\"**Bonjour-hi** (bohn-ZHOOR hi) = Hello, the Montreal way!\" It was Sésame the bagel, bouncing.",
              "medium shot", "SESAME bounces up with his tiny arms wide and lands in a puff of snow", "SESAME",
              "warm and springy", "tilts up", "a springy boing and a puff of snow"),
             ("\"Tonight the whole market sings **Vive le vent** (veev luh VAHN) = long live the wind!\"",
              "medium close-up", "SESAME sweeps one tiny arm toward the bandstand and ROSIE turns to look",
              ["SESAME", "ROSIE"], "proud and excited", "pans left", "a soft crunch of snow"),
             ("\"You know it,\" said Sésame. \"It's Jingle Bells in a tuque.\"",
              "close-up", "SESAME tugs his red tuque down and winks", "SESAME", "quick and funny",
              "holds still", "a tiny woolly tug"),
         ]},
        {"title": "One, two, three", "place": "port",
         "angle": "Medium view up the wooden steps of",
         "who": "COLDWATER stands on the top step of the bandstand with her paintbrush raised like a baton and "
                "her orange plumes swooping; KYLE stands on the step below with his chest puffed out; SESAME "
                "bounces beside him; FINNEGAN stands at the end of the row with his beak wide open and his "
                "yellow crest sticking straight up",
         "beats": [
             ("On the bandstand stood Cleo Coldwater, conducting with a paintbrush. \"Every song tells a story! "
              "One, two, three—\"",
              "medium shot", "COLDWATER sweeps her paintbrush up and brings it down on the beat", "COLDWATER",
              "dreamy and commanding", "tilts up", "a paintbrush tap on a wooden rail"),
             ("Kyle the bear cub growled. Sésame bounced. Finnegan sang \"WOOOHOOO—wait, how do I stop?!\"",
              "medium shot", "FINNEGAN throws his beak wide open while KYLE and SESAME lean away from him",
              ["FINNEGAN", "KYLE", "SESAME"], "enormous and out of control", "pans right",
              "a rattle of wooden boards and a springy boing"),
         ]},
        {"title": "Needs gravy", "place": "port",
         "angle": "Low angle from the foot of the steps looking up at the snowy roof of",
         "who": "FINNEGAN stands with his beak still wide open and his eyes round with alarm; KYLE sits beside "
                "him buried up to his red beanie in a heap of snow that has slid off the roof, a dab of snow "
                "on his tongue",
         "beats": [
             ("He could not stop. Snow slid off the bandstand roof onto Kyle. Flump.",
              "medium shot", "FINNEGAN blinks in alarm as a heap of snow settles around KYLE",
              ["FINNEGAN", "KYLE"], "startled and sorry", "tilts down", "a long slither and one soft flump"),
             ("\"I was just taste-testing,\" said Kyle, from inside the snow. \"Needs gravy.\"",
              "medium close-up", "KYLE pokes his muzzle out of the snow and licks a dab off his nose", "KYLE",
              "unbothered and hungry", "pushes in", "a muffled lip smack"),
         ]},
        {"title": "A very small la", "place": "port",
         "angle": "High angle looking down at the bottom step of",
         "who": f"{ROSIE_CUP} stands alone on the bottom step holding {BELL} and a little picture list in front "
                "of her cup, straw drooping, looking very small beside the big wooden steps",
         "beats": [
             ("Rosie sang too. \"La.\" It was a very small la. Nobody heard it. Not even Rosie.",
              "medium shot", "ROSIE opens her mouth in a tiny round shape and then closes it", "ROSIE",
              "hopeful, then unsure", "pushes in", "a far rattle of wooden boards"),
             ("Her straw drooped. She crossed sing off her list. She wrote: hold the bell.",
              "close-up", "ROSIE marks her picture list and hugs the tiny bell closer as her straw droops", "ROSIE",
              "decided and a bit glum", "tilts down", "a pencil scratch and a faint ting"),
         ]},
        {"title": "Behind the poutine stand", "place": "port",
         "angle": "Ground-level view along the snow behind the steaming poutine stand at",
         "who": f"COUIC peeks out from behind a wooden crate, half hidden, hugging {BELL} that is nearly as big "
                f"as he is, huge round eyes wide; {ROSIE_CUP} stands a little way off looking at him in surprise "
                "with her straw tilted",
         "beats": [
             ("Ting! The tiny bell slipped and rolled away, right behind the poutine stand.",
              "medium shot", "ROSIE hops after the bell and stops short with her straw tilted", "ROSIE",
              "flustered, then surprised", "tracks beside", "a tiny rolling tinkle"),
             ("Somebody was already there. Somebody very small, in a striped scarf.",
              "close-up", "COUIC peeks out from behind the crate and hugs the bell tighter", "COUIC",
              "shy and startled", "pushes in", "a faint ting and a hiss of steam"),
             ("\"**Couic** (KWEEK) = squeak!\" said the somebody. He was a cheese curd. Fresh curds squeak.",
              "close-up", "COUIC lets out one squeak and claps both tiny arms over his mouth", "COUIC",
              "embarrassed and sweet", "holds still", "one tiny bright squeak"),
         ]},
        {"title": "Two small voices", "place": "port",
         "angle": "Close two-shot at snow level behind the poutine stand at",
         "who": f"COUIC stands hidden behind {BELL} with only his huge round eyes and the ends of his striped "
                f"scarf showing; {ROSIE_CUP} sits on the edge of the wooden crate beside him, straw low; TORI "
                "peeks around the corner of the stand above them, her tall green straw showing first",
         "beats": [
             ("\"Is that your whole voice?\" asked Rosie. Couic nodded and hid behind the bell.",
              "medium close-up", "COUIC nods and ducks down behind the tiny bell", "COUIC", "bashful",
              "pushes in", "a faint ting"),
             ("\"Mine is small too,\" said Rosie. \"So I'm only holding the bell.\" \"Couic,\" said Couic sadly.",
              "medium close-up", "ROSIE's straw dips toward COUIC and he peeks out with one eye",
              ["ROSIE", "COUIC"], "kindred and glum", "holds still", "one tiny sad squeak"),
             ("Tori's tall straw peeked round the stand. \"Cleo wants every voice. Even the hiding ones.\"",
              "medium shot", "TORI leans around the corner of the stand and beckons with one tiny arm", "TORI",
              "kind and coaxing", "tilts up", "a soft crunch of snow"),
         ]},
        {"title": "Every size", "place": "port",
         "angle": "Low angle looking up from the bandstand floor at",
         "who": "COLDWATER points her paintbrush like a baton with her plumes swooping; KYLE stands tall with "
                "one paw on his white chest mark, rumbling; FINNEGAN stands rigid beside him with his beak "
                "clamped shut and his whole body quivering",
         "beats": [
             ("Cleo tapped her paintbrush. \"I don't need one big voice. I need every size.\"",
              "medium shot", "COLDWATER taps her paintbrush on the rail and looks along the row", "COLDWATER",
              "firm and inspired", "pushes in", "two paintbrush taps on wood"),
             ("\"Kyle, you're the rumble.\" Kyle rumbled. The benches shook.",
              "medium close-up", "KYLE puffs out his chest and rumbles with his eyes shut", "KYLE",
              "proud and thunderous", "tilts down", "a deep rattle of wooden boards"),
             ("\"Finnegan, the trumpet. One toot. At the very end.\" Finnegan trembled with waiting.",
              "medium close-up", "FINNEGAN clamps his beak shut and quivers from crest to feet", "FINNEGAN",
              "bursting and obedient", "holds still", "a tiny quivering rattle"),
         ]},
        {"title": "Every carol needs a drop", "place": "port",
         "angle": "Wide side view along the rail of",
         "who": "SESAME bounces on the rail with his tuque flying; MOM and TORI stand side by side swaying with "
                "their eyes closed and their straws swaying together; CAT the little blue penguin crouches in "
                "front with one flipper cupped at her beak, beatboxing, the other flipper chopping the air",
         "beats": [
             ("\"Sésame, the bounce.\" Boing, boing. \"Mom and Tori, the warm middle.\" They hummed like kettles.",
              "medium shot", "SESAME bounces on the rail while MOM and TORI sway side by side",
              ["SESAME", "MOM", "TORI"], "bouncy and mellow", "pans left", "two springy boings and a soft hum of wind"),
             ("Cat was already doing the beat. Boom, tss, boom-boom, tss. \"Every carol needs a drop.\"",
              "medium close-up", "CAT cups one flipper at her beak and chops the beat with the other", "CAT",
              "cool and locked in", "pushes in", "a soft thump and hiss of a beat on wood"),
         ]},
        {"title": "Two holes in the song", "place": "port",
         "angle": "Medium view along the row on the steps of",
         "who": "COLDWATER leans out from the top step measuring a small empty space on the step between KYLE "
                "and SESAME with her two flippers held a cup-width apart, one eyebrow raised; KYLE and SESAME "
                "both look down at the empty space between them",
         "beats": [
             ("They tried again. Rumble, bounce, hum, boom, tss. It sounded like a real song!",
              "wide shot", "KYLE sways and SESAME bounces in time on either side of the empty space",
              ["KYLE", "SESAME"], "pleased and in step", "tracks beside", "a steady thump on wooden boards"),
             ("But twice the tune hopped up to a tiny high note. And twice, nobody was there.",
              "medium shot", "COLDWATER freezes with her paintbrush in the air and looks down at the gap",
              "COLDWATER", "puzzled and listening", "tilts down", "a sudden hush and a creak of a board"),
             ("\"This song has two holes in it,\" said Cleo. \"One cup-sized. One curd-sized.\"",
              "medium close-up", "COLDWATER measures the empty space with her flippers, then pinches them close",
              "COLDWATER", "thoughtful and certain", "pushes in", "a soft tap of a paintbrush"),
         ]},
        {"title": "Excuse the rumble", "place": "port",
         "angle": "Close view up at a round bear cub on the steps of",
         "who": "KYLE stretches up on his tiptoes with his muzzle pointed at the sky and one paw over his "
                "mouth, eyes wide with surprise at himself; COLDWATER winces beside him with her plumes "
                "blown back",
         "beats": [
             ("Kyle tried the high note. It came out as a burp. \"Excuse the rumble.\"",
              "medium close-up", "KYLE stretches up, hiccups and claps one paw over his mouth while COLDWATER "
              "winces", ["KYLE", "COLDWATER"], "ambitious, then sheepish", "tilts up", "one small round burp"),
         ]},
        {"title": "Exactly your size", "place": "port",
         "angle": "Warm close two-shot at the foot of the steps of",
         "who": f"TORI bends down close with a sure warm smile, green straw bobbing; {ROSIE_CUP} looks up at her "
                f"holding {BELL} in front of her cup, straw halfway up; COUIC peeks out from behind the cup "
                "with one huge eye",
         "beats": [
             ("Tori bent close to Rosie. \"That hole is exactly your size. You've got this, little sip.\"",
              "medium close-up", "TORI bends down and nods at the empty space as ROSIE's straw lifts",
              ["TORI", "ROSIE"], "sure and encouraging", "pushes in", "a soft crunch of snow"),
         ]},
        {"title": "From the top", "place": "port",
         "angle": "Close view from the bandstand floor up at",
         "who": "FINNEGAN holds his beak shut with both flippers, his cheeks blown up round and his yellow "
                "crest standing straight on end, eyes bulging; CAT the little blue penguin crouches beside him "
                "with one flipper cupped at her beak and the other raised to count in; COUIC climbs the wooden "
                "rail behind them with his striped scarf trailing",
         "beats": [
             ("\"From the top!\" said Cleo. Finnegan held his toot in with both flippers. His cheeks ballooned.",
              "medium shot", "FINNEGAN clamps both flippers over his beak and his cheeks swell rounder",
              "FINNEGAN", "bursting and heroic", "pushes in", "a tight squeaky wheeze"),
             ("Cat counted them in. Boom, tss. Rosie hopped into the cup-sized space. Couic climbed the rail.",
              "medium shot", "CAT chops the count with one flipper while COUIC hauls himself up the rail",
              ["CAT", "COUIC"], "cool and determined", "tilts up", "a soft thump and hiss of a beat on wood"),
         ]},
        {"title": "La!", "place": "port",
         "angle": "Low angle from the snow looking up the steps of",
         "who": f"{ROSIE_CUP} stands in the space on the step between KYLE and SESAME with her eyes closed and "
                "her mouth a tiny round shape, straw straight up, the tiny bell in front of her cup; KYLE "
                "rumbles on one side and SESAME bounces on the other; COLDWATER conducts above them with a "
                "wide delighted smile",
         "beats": [
             ("Rumble, bounce, hum, boom. The tune hopped up. \"La!\" sang Rosie, clear as a spoon on a teacup.",
              "medium shot", "ROSIE lifts her straw high with her eyes closed and her mouth a tiny round shape", "ROSIE",
              "brave and ringing", "tilts up", "one clear glassy ting"),
             ("One hole filled! On went the song, right to the very last note. Everybody stopped.",
              "wide shot", "COLDWATER sweeps her paintbrush wide and then holds it perfectly still", "COLDWATER",
              "thrilled, then waiting", "pulls back", "a steady thump on boards, then silence"),
         ]},
        {"title": "The last note", "place": "port",
         "angle": "Tight close-up on the wooden rail under the big brass bell of",
         "who": f"COUIC stands all alone on the wooden rail, very tiny, with his eyes squeezed shut, his tiny "
                f"arms stiff at his sides and his mouth wide open; {ROSIE_CUP} stands just below the rail "
                f"ringing {BELL} in front of her cup and nodding up at him",
         "beats": [
             ("Rosie rang her tiny bell and nodded at Couic. \"Your turn. It's exactly your size.\"",
              "medium close-up", "ROSIE rings the tiny bell and nods up at COUIC on the rail", ["ROSIE", "COUIC"],
              "encouraging and sure", "tilts up", "one bright tiny ting"),
             ("\"Couic!\" It was tiny. It was perfect. It sat right on top of the song.",
              "close-up", "COUIC squeezes his eyes shut and lets out one squeak with his whole body", "COUIC",
              "terrified, then proud", "pushes in", "one tiny perfect squeak"),
         ]},
        {"title": "Bravo, Couic", "place": "port",
         "angle": "Wide joyful view across the rink toward the strings of glowing bulbs over",
         "who": "FINNEGAN leaps in the air with his beak open for one proud toot; SESAME bounces with COUIC "
                "riding on top of his red tuque, the tiny curd blushing bright pink with both tiny arms up; "
                "KYLE claps his paws over his head; CAT the little blue penguin spins on one foot; every round "
                "bulb on the strings glows gold",
         "beats": [
             ("Toot! went Finnegan. Just one. Every bulb at the Old Port lit up, and everybody cheered.",
              "wide shot", "FINNEGAN leaps with one toot and KYLE claps his paws over his head",
              ["FINNEGAN", "KYLE"], "triumphant and amazed at himself", "pulls back",
              "one short bright toot and a wave of clapping paws"),
             ("\"Bravo, Couic!\" Couic turned pink. For a cheese curd, that takes some doing.",
              "close-up", "COUIC blushes pink on top of the tuque as SESAME bounces him gently",
              ["COUIC", "SESAME"], "overwhelmed and glowing", "pushes in", "a springy boing and clapping paws"),
         ]},
        {"title": "Lantern seventeen", "place": "lane", "time": "night",
         "angle": "Upward view along the string of lanterns over",
         "who": "CAT the little blue penguin stands on a snowy crate hooking a bell-shaped brass-yellow paper "
                f"lantern onto the long string; {ROSIE_CUP} stands below with her eyes closed and her straw "
                f"straight up, her mouth a tiny round shape, {BELL} in front of her cup; TORI sways beside her; MOM stands at the "
                "far end of the lane with her tiny arms clasped, listening",
         "beats": [
             ("By dark the Market Train had them home. Cat hung the bell-shaped lantern on Lantern Lane.",
              "wide shot", "CAT hooks the bell-shaped lantern onto the string and it swings gently", "CAT",
              "careful and pleased", "tilts up", "a far train whistle and a creak of string"),
             ("\"One more light!\" sang Rosie. Far down the lane, Mom smiled. She had heard every note.",
              "medium shot", "ROSIE lifts her straw straight up with her eyes closed while MOM clasps her tiny arms far behind",
              ["ROSIE", "MOM"], "clear and proud", "pulls back", "one clear glassy ting and a soft crunch of snow"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep curled on a soft pillow at the foot of the bed, "
                "yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, with your just-right voice. Goodnight, Couic, one squeak, one cheer.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Finnegan, one toot at a time. May your dreams hum Jingle Bells in a tuque.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, with your just-right voice.",
        "Goodnight, Couic, one squeak, one cheer.",
        "Goodnight, Finnegan, one toot at a time.",
        "May your dreams hum Jingle Bells in a tuque.",
    ],
}
