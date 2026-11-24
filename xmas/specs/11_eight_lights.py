"""11 — Eight Lights (Friday, December 11 · Hanukkah, eighth night)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

HANUKKIAH = ("a brass hanukkiah with nine candle holders on the wide stone sill, eight in a row and one helper "
             "holder set a little higher in the middle")
WINDOW = {
    "name": "the great window of Frostpeak Lodge at night",
    "scene": "the great window at night",
    "accents": "candle gold and deep winter blue",
}
WINDOW_BEFORE = dict(
    WINDOW,
    props=f"a tall arched window of many panes, {HANUKKIAH}, nine unlit candles standing in the holders, "
          "a cushioned window seat, a plate of golden latkes, a wicker armchair, the wide snowy valley far below "
          "with tiny dark cabins",
    light="One hanging brass lamp glows softly beside the deep blue glass",
    atmo="Snow drifts past the dark panes",
    motion="snow drifts past the dark panes",
)
WINDOW_LIT = dict(
    WINDOW,
    props=f"a tall arched window of many panes, {HANUKKIAH}, nine small candle flames reflected in the glass, "
          "a cushioned window seat, a plate of golden latkes, a wicker armchair, the wide snowy valley far below "
          "with tiny dark cabins",
    light="Nine small candle flames glow gold against the deep blue glass",
    atmo="The candle flames sway and snow drifts past the panes",
    motion="the nine candle flames sway gently",
)
WINDOW_ANSWER = dict(
    WINDOW_LIT,
    props=f"a tall arched window of many panes, {HANUKKIAH}, nine small candle flames reflected in the glass, "
          "a cushioned window seat, an empty latke plate, a wicker armchair, the wide snowy valley far below "
          "dotted with tiny glowing cabin windows",
)

STORY = {
    "num": "11",
    "slug": "eight-lights",
    "title": "Eight Lights",
    "meta": [
        ("Day", "Friday, December 11 · door eleven"),
        ("Holiday thread", "Hanukkah, the eighth and last night: all eight candles and the helper, hosted by "
                           "Herschel and Noa"),
        ("Guests", "Herschel the Walrus ❄️ (lights the candles and tells the story in three lines), Noa the "
                   "jelly doughnut, Magnus Meltsworth ❄️ (the dark never bothered him)"),
        ("Cat’s role", "window lookout by day, and by night the guide who knows whose light is whose"),
        ("Mandarin", "八 eight · 光明節 Hanukkah · 蠟燭 candle"),
        ("Setting", "The Door Wall, the great window of the lodge at night looking over the whole valley, "
                    "Lantern Lane at night, and the bunk room"),
    ],
    "palette": "deep winter blue and soft cream with saturated candle gold and brass accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "HERSCHEL", "NOA", "MAGNUS"],
    "cast_note": "Humans in this story: none. The hanukkiah has nine holders: eight in a row and the helper "
                 "candle (the shamash) set a little higher. On this eighth night all nine burn. Only Herschel "
                 "touches the candles.",
    "key_shot": 12,
    "places": {
        "door": DOORWALL,
        "before": WINDOW_BEFORE,
        "lit": WINDOW_LIT,
        "answer": WINDOW_ANSWER,
        "lane": LANE_NIGHT,
        "bunk": bunk("a row of eight tiny brass dots and one spare blue candle on the nightstand"),
    },
    "shots": [
        {"title": "Door eleven", "place": "door",
         "angle": "Medium view at knob height along the tall Door Wall in",
         "who": "MOM opens one little carved door with a gentle tiny arm, smiling softly, eight tiny brass dots "
                f"gleaming in a row inside it; {ROSIE_CUP} stands on a wooden footstool beside her counting the "
                "dots with her straw, eyes bright",
         "beats": [
             ("Door eleven was Mom's turn. She opened it gently, the way she opens everything.",
              "medium shot", "MOM eases the little door open with one tiny arm", "MOM", "gentle and unhurried",
              "pushes in", "a tiny door creak and a crackling fire"),
             ("Inside shone eight tiny brass dots in a row. Rosie counted them twice. Still **八** (bā) = eight.",
              "close-up", "ROSIE taps her straw toward each brass dot in turn", "ROSIE", "careful and curious",
              "pans right", "eight tiny taps"),
         ]},
        {"title": "The eighth night", "place": "door",
         "angle": "Low angle from the woven rug up at the open little door in",
         "who": "NOA bounces high on the rug with both tiny arms up and powdered sugar flying off her, "
                f"overjoyed; {ROSIE_CUP} looks down at her from the wooden footstool with a wiggling straw",
         "beats": [
             ("Noa the jelly doughnut bounced. \"Eight dots! Tonight is the eighth night of **光明節** "
              "(Guāngmíng jié) = Hanukkah!\"",
              "medium shot", "NOA bounces on the rug and powdered sugar puffs off her", "NOA",
              "overjoyed", "tilts up", "soft bounces and a puff of sugar"),
             ("\"The last night. All eight candles, plus the helper. We light them as the sun goes down.\"",
              "medium close-up", "NOA holds up her tiny arms to count while ROSIE's straw wiggles",
              ["NOA", "ROSIE"], "proud and excited", "pushes in", "a crackling fire"),
         ]},
        {"title": "Still daytime", "place": "door",
         "angle": "Wide view across the long woven rug toward a tall snowy window in",
         "who": "CAT the little blue penguin stands on tiptoe at the tall window with one flipper shading her "
                f"eyes like a lookout, very serious; {ROSIE_CUP} stands on the rug holding a little picture list "
                "in front of her cup, the list showing plain doodles of a sun, a sun and one candle",
         "beats": [
             ("Rosie made a list. One: wait for sundown. Two: keep waiting. Sundown took all day.",
              "medium shot", "ROSIE looks at her list, then at the bright window, and her straw taps",
              "ROSIE", "patient, barely", "pans left", "a slow ticking of the fire and a straw tap"),
             ("Cat the penguin checked the window forty times. \"Still daytime,\" she reported. \"I'll check "
              "again.\"",
              "medium close-up", "CAT peers out under her flipper, turns and gives a solemn nod", "CAT",
              "serious and official", "pushes in", "quick penguin foot taps on the rug"),
         ]},
        {"title": "The great window", "place": "before", "time": "night",
         "angle": "Wide establishing view from the top of the stairs toward",
         "who": f"{ROSIE_CUP} stands on the cushioned window seat looking tiny against the huge dark glass, "
                "straw up; TORI stands beside her; MOM carries a plate of golden latkes with a calm smile; "
                "CAT the little blue penguin hops up onto the seat",
         "beats": [
             ("At last the sun slid behind the peaks. Everyone climbed to the great window, high above the valley.",
              "wide shot", "ROSIE hops close to the huge dark glass and her straw lifts", "ROSIE",
              "small and full of wonder", "pushes in", "soft footsteps on stairs and a hush"),
         ]},
        {"title": "Nine holders", "place": "before", "time": "night",
         "angle": "Close view along the wide stone sill of",
         "who": "HERSCHEL sets a candle into the last holder of the brass hanukkiah with one careful flipper, "
                "whiskers bristling with concentration; NOA stands on the sill beside it pointing one tiny arm "
                "at the higher middle holder, proud",
         "beats": [
             ("Herschel the walrus set nine candles in their holders. Eight in a row, and one a little higher.",
              "medium shot", "HERSCHEL presses the last candle gently into its holder", "HERSCHEL",
              "careful and fond", "tracks beside", "a soft tap of wax on brass"),
             ("\"The high one is the helper,\" said Noa. \"It lights the others. And Herschel lights the helper.\"",
              "medium close-up", "NOA points at the higher middle candle and HERSCHEL nods",
              ["NOA", "HERSCHEL"], "proud and clear", "pushes in", "a soft tap of wax on brass"),
         ]},
        {"title": "The dark never bothered me", "place": "before", "time": "night",
         "angle": "Medium view into the lamplit corner beside",
         "who": "MAGNUS sits in the wicker armchair with a plate of golden latkes on his knee and his arms "
                "folded, bushy eyebrows frowning; CAT the little blue penguin stands beside the chair counting "
                "on her flippers with a sideways look",
         "beats": [
             ("In the corner sat Magnus Meltsworth, a grumpy old polar bear, with a plate of latkes.",
              "medium shot", "MAGNUS folds his arms and his wicker chair creaks", "MAGNUS",
              "grumpy and comfortable", "pushes in", "a long wicker creak"),
             ("\"Lights, lights,\" grumbled Magnus. \"The dark never bothered me. The dark is nice and quiet.\"",
              "medium close-up", "MAGNUS lowers his bushy eyebrows and pops a latke into his mouth", "MAGNUS",
              "gruff", "holds still", "a wicker creak and a crunchy bite"),
             ("\"That's eleven latkes,\" whispered Cat. \"I'm not judging. I'm counting.\"",
              "medium close-up", "CAT counts on her flippers and glances up at MAGNUS", ["CAT", "MAGNUS"],
              "cheeky and precise", "pans left", "a tiny flipper tap and a crunchy bite"),
         ]},
        {"title": "So big, so small", "place": "before", "time": "night",
         "angle": "Over-the-shoulder view past the unlit candles and out through",
         "who": f"{ROSIE_CUP} stands on the window seat gazing out at the wide dark valley with her straw "
                "drooping a little, her reflection faint in the glass",
         "beats": [
             ("Rosie looked out. The valley was so big and so dark. The candles were so small.",
              "wide shot", "ROSIE looks from the candles to the dark valley and back", "ROSIE",
              "small and wondering", "pushes in", "soft wind on glass"),
             ("\"Will anybody even see them?\" asked Rosie. Her straw drooped a little.",
              "medium close-up", "ROSIE's straw dips toward the glass", "ROSIE", "doubtful",
              "holds still", "soft wind on glass"),
         ]},
        {"title": "Best seat in the lodge", "place": "before", "time": "night",
         "angle": "Warm close view on the cushioned window seat of",
         "who": f"TORI leans close against ROSIE with a soft steady smile, a patchwork blanket draped around "
                f"them both; {ROSIE_CUP} stands snug on the cushion with her straw lifting; MOM holds out a "
                "plate of golden latkes beside them with a warm smile",
         "beats": [
             ("\"Best seat in the lodge, little sip,\" said Tori, and shared her blanket.",
              "medium close-up", "TORI tugs the blanket snug around ROSIE and leans in", ["TORI", "ROSIE"],
              "warm and cozy", "pushes in", "a soft blanket rustle"),
             ("Mom handed the latkes along. They were hot and crispy and smelled like a holiday.",
              "medium shot", "MOM holds the plate of latkes closer and steam curls up", "MOM",
              "calm and generous", "pans right", "a soft plate scrape and a crispy crackle"),
         ]},
        {"title": "Three lines", "place": "before", "time": "night",
         "angle": "Low angle from the window seat looking up at the big whiskery face beside",
         "who": "HERSCHEL leans on the stone sill beside the nine unlit candles with twinkling eyes and one "
                f"flipper raised like a storyteller; {ROSIE_CUP} looks up at him from the cushion with her "
                "straw half raised",
         "beats": [
             ("Herschel's whiskers twitched. \"Here is the story,\" he said. \"It only takes three lines.\"",
              "medium shot", "HERSCHEL raises one flipper and his whiskers twitch", "HERSCHEL",
              "twinkly and warm", "pushes in", "a deep soft rumble"),
             ("\"Long ago, there was a little oil for the lamp. Only enough for one night.\"",
              "medium close-up", "HERSCHEL holds up one flipper tip to show how little", "HERSCHEL",
              "hushed and gentle", "holds still", "soft wind on glass"),
             ("\"It lasted eight.\" He smiled. \"And we have been lighting candles for it ever since.\"",
              "medium close-up", "ROSIE's straw rises as HERSCHEL spreads both flippers wide",
              ["ROSIE", "HERSCHEL"], "wonder growing", "pulls back", "a soft happy rumble"),
         ]},
        {"title": "The helper first", "place": "lit", "time": "night",
         "angle": "Close view at flame height along the stone sill of",
         "who": "HERSCHEL holds the lit helper candle in one steady flipper and touches its flame to the next "
                "candle in the row, eyes soft and bright; NOA watches from the sill with her tiny arms clasped "
                "and candlelight shining on her sugar",
         "beats": [
             ("Then Herschel lit the helper. The helper lit the first candle. And the next. And the next.",
              "close-up", "HERSCHEL tips the helper candle and a new little flame catches", "HERSCHEL",
              "steady and reverent", "tracks beside", "a tiny flare of a wick"),
             ("Each **蠟燭** (làzhú) = candle, one by one, caught the flame. Eight flames, and the helper made nine.",
              "medium shot", "NOA clasps her tiny arms tighter as the row of flames grows beside HERSCHEL",
              ["NOA", "HERSCHEL"], "glowing with pride", "pans right", "soft wick flares one after another"),
         ]},
        {"title": "Nine little lights", "place": "lit", "time": "night",
         "angle": "Medium view from outside the glass looking in through",
         "who": f"{ROSIE_CUP} stands on the window seat with nine tiny flames reflected on her dome lid, eyes "
                "shining; NOA stands beside her with flames reflected in her big eyes; MOM stands behind them "
                "with the latke plate set down, one tiny arm pointing gently out at the valley",
         "beats": [
             ("Nobody talked. Nine little lights shone on the glass, and on Rosie's lid, and in Noa's eyes.",
              "medium close-up", "ROSIE gazes at the flames and their reflections flicker on her lid", "ROSIE",
              "hushed and happy", "pushes in", "soft candle flickers"),
             ("Mom leaned close. \"Look, Rosie,\" she said softly. \"Somebody is answering.\"",
              "medium shot", "MOM points one tiny arm gently out through the glass", "MOM", "quiet and glad",
              "pans right", "soft candle flickers"),
         ]},
        {"title": "The valley answers", "place": "answer", "time": "night",
         "angle": "Wide view over the row of candle flames and out through",
         "who": f"{ROSIE_CUP} stands silhouetted on the window seat with her straw rising, the valley below "
                "filling with tiny golden window lights; CAT the little blue penguin presses close to the glass "
                "pointing a flipper from light to light",
         "beats": [
             ("Far below, one window blinked on. Then another. Then three more, all at once.",
              "wide shot", "ROSIE's straw rises as tiny lights appear across the valley", "ROSIE",
              "astonished", "pushes in", "soft wind and a tiny squeak of a straw"),
             ("\"That's Piper's,\" said Cat. \"That's Willa's, the tiny one. That one's Barnaby's. I can smell "
              "it from here.\"",
              "medium close-up", "CAT taps the glass toward one light after another", "CAT",
              "proud and at home", "pans left", "three soft taps on glass"),
             ("Rosie counted. Ten. Twenty. More. Every window in the valley was answering the lodge.",
              "wide shot", "ROSIE counts with her straw bobbing while CAT leans on the glass", ["ROSIE", "CAT"],
              "delighted", "pulls back", "soft wind and candle flickers"),
         ]},
        {"title": "Every window but one", "place": "answer", "time": "night",
         "angle": "Medium view toward the doorway from the cushioned seat of",
         "who": "MAGNUS stands in the doorway with his patched brown scarf thrown over one shoulder and his "
                f"wooden skis under one arm, looking back with a scowl that is almost a smile; {ROSIE_CUP} "
                "watches him from the window seat with round eyes",
         "beats": [
             ("Every window but one. High on the hill sat one dark cabin. \"Whose is that?\" asked Rosie.",
              "medium shot", "ROSIE turns from the glass with her straw tilted like a question", "ROSIE",
              "curious", "pans left", "soft wind on glass"),
             ("\"Mine,\" said Magnus. Everybody looked at him. He looked at the ceiling.",
              "medium close-up", "MAGNUS shifts his skis under his arm and looks up at the ceiling", "MAGNUS",
              "caught and grumbly", "holds still", "a long creak of floorboards"),
             ("\"Fine,\" he grumbled, and stomped out. \"But this is my one noble act for the week.\"",
              "medium shot", "MAGNUS tosses his scarf over his shoulder and scowls back from the doorway",
              "MAGNUS", "gruff and secretly pleased", "pushes in", "a scarf flap and one heavy step"),
         ]},
        {"title": "The last window", "place": "answer", "time": "night",
         "angle": "Close view from behind two small watchers and out through",
         "who": f"{ROSIE_CUP} stands with her lid almost touching the glass, staring up at the far hill; CAT the "
                "little blue penguin presses her beak to the pane beside her; one last tiny golden light glows "
                "high on the dark hill above all the others",
         "beats": [
             ("They waited. Rosie did not even blink.",
              "close-up", "ROSIE holds perfectly still with her straw pointing at the far hill", "ROSIE",
              "hopeful and holding her breath", "holds still", "soft wind and a held breath"),
             ("Then, way up high, the last window in the valley blinked on.",
              "wide shot", "ROSIE's straw shoots straight up as the highest light twinkles", "ROSIE",
              "thrilled", "tilts up", "a squeak of a straw and soft candle flickers"),
             ("\"He ran,\" said Cat. \"I have never seen Magnus run.\"",
              "medium close-up", "CAT turns from the glass with her beak wide open", "CAT",
              "amazed and tickled", "pushes in", "a tap of a beak on glass"),
         ]},
        {"title": "The whole valley", "place": "answer", "time": "night",
         "angle": "Warm low angle beside the nine candle flames in",
         "who": "HERSCHEL sways beside the glowing hanukkiah with his eyes closed and his whiskers lifted, "
                "humming; NOA bounces on the stone sill with powdered sugar flying off in a little cloud; "
                f"{ROSIE_CUP} stands on the sill with her straw standing straight up, the valley twinkling with "
                "tiny golden lights behind them",
         "beats": [
             ("Now the whole valley twinkled back at the lodge. Noa bounced so hard that sugar snowed on "
              "everyone.",
              "medium shot", "NOA bounces on the sill and a cloud of powdered sugar drifts down", "NOA",
              "overjoyed", "pulls back", "soft bounces and a puff of sugar"),
             ("Herschel hummed an old candle song, deep as a tuba. Everybody swayed. Even the flames.",
              "medium close-up", "HERSCHEL sways slowly from side to side with his whiskers lifted", "HERSCHEL",
              "content and glowing", "holds still", "a deep slow rumble"),
             ("\"Lanterns!\" said Rosie suddenly. Her straw stood straight up. \"We still have one to hang!\"",
              "medium shot", "ROSIE bounces on the sill with her straw straight up", "ROSIE",
              "bright and eager", "pushes in", "a happy hop on stone"),
         ]},
        {"title": "Lantern eleven", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the long lantern string in",
         "who": "MAGNUS reaches up easily and hooks a deep-blue paper lantern dotted with eight "
                "gold dots onto the string, snow on his bushy eyebrows, puffing little clouds of breath; NOA "
                f"bounces in the snow beside him with both tiny arms up; {ROSIE_CUP} stands beside her looking "
                "up with her straw tall",
         "beats": [
             ("Down on Lantern Lane, lantern eleven was deep blue, with eight gold dots.",
              "wide shot", "NOA bounces under the deep-blue lantern with both tiny arms up", "NOA",
              "joyful", "tilts up", "soft crunching snow"),
             ("Magnus was there already, puffing, with snow on his eyebrows. He was the tallest. He hung it.",
              "medium shot", "MAGNUS hooks the lantern onto the string and puffs a cloud of breath", "MAGNUS",
              "out of breath and pretending otherwise", "pushes in", "a tiny hook click and a big puff"),
             ("\"One more light,\" said Rosie and Noa together. Magnus said nothing. But his eyebrows almost "
              "smiled.",
              "medium close-up", "ROSIE and NOA bounce together while MAGNUS lifts one bushy eyebrow",
              ["ROSIE", "NOA", "MAGNUS"], "glad all round", "pulls back",
              "soft bouncing crunches and a faraway sizzle from the grill"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Warm close view across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, "
                "facing the frosted round window, yellow scarf visible",
         "beats": [
             ("Goodnight, eight candles, and the helper too. Goodnight, valley, window by window.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Magnus, noble for one more week. Sleep well, with one small light still glowing.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, eight candles, and the helper too.",
        "Goodnight, valley, window by window.",
        "Goodnight, Magnus, noble for one more week.",
        "Sleep well, with one small light still glowing.",
    ],
}
