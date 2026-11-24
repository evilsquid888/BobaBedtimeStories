"""21 — The Longest Night (Monday, December 21 · Dōngzhì 冬至, the winter solstice)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "21",
    "slug": "the-longest-night",
    "title": "The Longest Night",
    "meta": [
        ("Day", "Monday, December 21 · door twenty-one"),
        ("Holiday thread", "Dōngzhì 冬至, the winter solstice: rolling tangyuan with Yeh Yeh on the longest night "
                           "of the year"),
        ("Guests", "Yeh Yeh the clay teapot, Herschel the Walrus ❄️, Nora Snowmane ❄️, Barnaby Beaksworth ❄️, "
                   "Kyle the black bear cub"),
        ("Cat’s role", "dough chopper (gentle kitchen kung fu: twenty neat pieces, one stuck to her beak)"),
        ("Mandarin", "冬至 winter solstice · 湯圓 round rice balls · 團圓 being together"),
        ("Setting", "The Door Wall in the lodge great hall, then the hearth kitchen of Frostpeak Lodge on the "
                    "longest night, Lantern Lane at night, and the bunk room"),
    ],
    "palette": "deep midnight blue and warm firelight amber with saturated ginger gold and porcelain blue accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "YEHYEH", "HERSCHEL", "NORA", "BARNABY", "KYLE"],
    "cast_note": "Humans in this story: none. The tangyuan are ordinary little white rice-dough balls with no "
                 "faces; a grown-up tends the fire and the pot, and a grown-up lights the lantern.",
    "key_shot": 6,
    "places": {
        "doorwall": DOORWALL,
        "kitchen": {
            "name": "the hearth kitchen of Frostpeak Lodge on the longest night of the year",
            "scene": "the firelit hearth kitchen",
            "props": "a wide stone hearth with a black iron pot of sweet ginger soup hanging over the fire, a long "
                     "floury wooden table, a big bowl of soft white rice dough, bamboo trays of plain little white "
                     "dough balls, a row of blue-and-white bowls, a small dark window edged with frost ferns",
            "light": "Hearth fire and a row of brass oil lamps glow amber against the dark window",
            "accents": "ginger gold and porcelain blue",
            "atmo": "Steam curls from the pot and rice flour hangs in the firelight",
            "motion": "steam curls up from the pot of ginger soup",
        },
        "lane_night": LANE_NIGHT,
        "bunk": bunk("a tiny blue bowl and a floury little wooden spoon on the nightstand"),
    },
    "shots": [
        {"title": "Door twenty-one", "place": "doorwall",
         "angle": "Low angle looking up past a wooden step stool at the rows of little carved doors in",
         "who": "YEHYEH stands on the step stool with one tiny arm on a brass knob, turning it very slowly, eyes "
                f"twinkling behind his spectacles; {ROSIE_CUP} leans in from below with her straw stretched up; "
                "TORI leans in beside her on tiptoe",
         "beats": [
             ("Door twenty-one was Yeh Yeh's turn. He turned the tiny knob. Slowly. Everybody leaned in.",
              "medium shot", "YEHYEH turns the little brass knob very slowly while ROSIE and TORI lean closer",
              ["YEHYEH", "ROSIE", "TORI"], "unhurried and teasing", "pushes in", "a slow brass squeak and a crackling fire"),
             ("Behind it sat a tiny blue bowl with three round white dots inside.",
              "close-up", "ROSIE stretches up to see and her straw wiggles", "ROSIE",
              "curious and eager", "tilts up", "a tiny door creak"),
         ]},
        {"title": "The winter solstice", "place": "doorwall",
         "angle": "Warm close view at teapot height beside the crackling fireplace in",
         "who": "YEHYEH holds a tiny blue bowl with three round white dots in it up to the firelight, a curl of "
                "steam rising from his lid, smiling a slow knowing smile",
         "beats": [
             ("\"Ah,\" said Yeh Yeh. \"Today is **冬至** (Dōngzhì) = the winter solstice.\"",
              "close-up", "YEHYEH lifts the tiny bowl to the firelight and nods", "YEHYEH",
              "pleased and knowing", "pushes in", "a soft kettle hiss and a crackling fire"),
             ("\"The shortest day and the longest night of the year. So tonight, we roll.\"",
              "medium close-up", "YEHYEH tucks the tiny bowl under one arm and taps his stick once", "YEHYEH",
              "warm and decided", "holds still", "one tap of bamboo on wood"),
         ]},
        {"title": "Dark by four", "place": "kitchen", "time": "night",
         "angle": "Wide establishing view from the doorway across the long floury table in",
         "who": f"{ROSIE_CUP} stands on the deep windowsill looking out at the dark glass with a little picture list held in front of her cup, her straw drooping; "
                "HERSCHEL stirs the iron pot at the hearth with his wooden ladle, whiskers dusted white; NORA "
                "sits by the fire in her blue shawl with a steaming cocoa mug, breathing in its steam",
         "beats": [
             ("By four o'clock the hearth kitchen windows were already dark. The longest night had begun.",
              "wide shot", "HERSCHEL stirs the big iron pot slowly and firelight ripples over the table", "HERSCHEL",
              "calm and cozy", "pushes in", "a crackling fire and a slow wooden stir"),
             ("Inside, the kitchen smelled of ginger and brown sugar. Snow piled up soft on the windowsill.",
              "medium shot", "NORA lifts her cocoa mug and breathes in the steam with her eyes closed", "NORA",
              "snug and content", "pans right", "a soft crackling fire and a bubbling pot"),
             ("\"Dark already?\" said Rosie. Her straw drooped. \"I had sunset on my list. For five o'clock.\"",
              "medium close-up", "ROSIE's straw droops as she looks at the dark window", "ROSIE",
              "surprised and put out", "tilts down", "a soft crackling fire and wind at the glass"),
         ]},
        {"title": "Good news, with soup", "place": "kitchen", "time": "night",
         "angle": "Medium view from the windowsill down to the fireside in",
         "who": "YEHYEH leans on his bamboo walking stick below the windowsill, looking up with crinkled eyes; NORA "
                f"pats the bench beside her with one big white paw, cocoa mug in the other; {ROSIE_CUP} sits on "
                "the edge of the windowsill with her straw half lifted",
         "beats": [
             ("\"There is good news hidden in the longest night,\" said Yeh Yeh. \"It comes with the soup.\"",
              "medium close-up", "YEHYEH looks up at ROSIE and a puff of steam pops from his lid", ["YEHYEH", "ROSIE"],
              "twinkly and mysterious", "pushes in", "a soft kettle puff"),
             ("\"Sit,\" said Nora the polar bear. \"Rolling first. Then soup. Then good news. Then more soup.\"",
              "medium shot", "NORA pats the bench beside her with one big paw", "NORA",
              "firm and kind", "pans left", "a soft pat on wood and a crackling fire"),
         ]},
        {"title": "Round", "place": "kitchen", "time": "night",
         "angle": "Close view at tabletop height across the floury wooden table in",
         "who": "YEHYEH shapes a small white dough ball between his tiny clay arms, spectacles dusted with flour, "
                f"face calm and happy; {ROSIE_CUP} stands on the table edge watching every move with her straw "
                "perked up; a neat row of perfectly round little white dough balls sits on a bamboo tray",
         "beats": [
             ("Yeh Yeh pinched off some soft white dough. Roll, roll, roll. A perfect little moon.",
              "close-up", "YEHYEH shapes the dough between his tiny arms and sets a round white ball on the tray",
              "YEHYEH", "calm and practiced", "pushes in", "a soft pat of dough"),
             ("\"**湯圓** (tāngyuán) = round rice balls,\" he said. \"Round for **團圓** (tuányuán) = being "
              "together.\"",
              "medium close-up", "YEHYEH holds up one round white ball and ROSIE leans in to look",
              ["YEHYEH", "ROSIE"], "warm and proud", "holds still", "a crackling fire"),
         ]},
        {"title": "Hi-ya!", "place": "kitchen", "time": "night",
         "angle": "Dynamic low angle along a long rope of white dough on the table in",
         "who": "CAT the little blue penguin stands on the table in a gentle kung fu pose with one flipper raised "
                "over a long rope of white dough, a small piece of dough stuck to her beak, fierce and happy; KYLE "
                "sits at the table edge with flour on his nose and both paws behind his back, cheeks full",
         "beats": [
             ("Cat the penguin chopped the dough rope. Hi-ya! Hi-ya! Twenty pieces. One stuck to her beak.",
              "medium shot", "CAT chops her flipper down on the dough rope and little pieces hop apart", "CAT",
              "fierce and delighted", "tracks beside", "quick soft chops on a floury table"),
             ("Flour flew up in a cloud. When it settled, everybody looked like a polar bear. Nora approved.",
              "medium shot", "CAT and KYLE blink at each other, dusted white with flour from head to toe",
              ["CAT", "KYLE"], "startled and giggly", "pulls back", "a soft whump of flour"),
             ("Kyle rolled one. Then it was gone. \"I was just taste-testing,\" he said. \"It needs soup.\"",
              "medium close-up", "KYLE swallows, licks flour off his nose and shrugs", "KYLE",
              "caught and cheerful", "pushes in", "a lip smack and a pat of floury paws"),
         ]},
        {"title": "One more pinch", "place": "kitchen", "time": "night",
         "angle": "Low angle looking up from the tabletop at a huge white dough ball in",
         "who": "BARNABY hugs a white dough ball as big as a snowball against his round tummy with both flippers, "
                "beaming with pride, a blue-and-white bowl far too small sitting in front of him",
         "beats": [
             ("Barnaby Beaksworth rolled his as big as a snowball. \"There's always enough for one more pinch!\"",
              "medium shot", "BARNABY pats one more pinch of dough onto his giant dough ball", "BARNABY",
              "generous and gleeful", "tilts up", "a soft heavy pat of dough"),
             ("One more. One more. It did not fit the spoon. It did not fit the bowl.",
              "close-up", "BARNABY tries to set the giant ball on the little bowl and it sits on top like a hat",
              "BARNABY", "puzzled and proud", "pushes in", "a soft thump and a wobbling bowl"),
         ]},
        {"title": "A latke", "place": "kitchen", "time": "night",
         "angle": "Close view past long ivory tusks at two big floury flippers in",
         "who": "HERSCHEL holds up one perfectly flat white dough disc on his big flipper, whiskers white with "
                "flour, chest puffed out with pride",
         "beats": [
             ("Herschel the Walrus pressed one between his flippers. It came out flat. \"A latke,\" he said "
              "proudly.",
              "medium close-up", "HERSCHEL opens his flippers and holds up the flat dough disc", "HERSCHEL",
              "proud and amused", "pushes in", "a soft clap of floury flippers"),
         ]},
        {"title": "Eggs", "place": "kitchen", "time": "night",
         "angle": "High angle looking down at a little bamboo tray on the floury table in",
         "who": f"{ROSIE_CUP} stands beside a little tray of six small egg-shaped white dough balls, flour on her "
                "lid, her straw tipped sideways in a puzzled way; YEHYEH peers over his spectacles at the tray "
                "with a fond chuckle",
         "beats": [
             ("Rosie rolled hers. They would not go round. They came out as eggs.",
              "close-up", "ROSIE sets one more egg-shaped dough ball on the tray and tips her straw sideways",
              "ROSIE", "puzzled and trying", "tilts down", "a soft pat of dough"),
             ("Yeh Yeh peered over his spectacles. \"My first hundred were eggs too. Then I got a pear.\"",
              "medium close-up", "YEHYEH peers at the tray and chuckles, and ROSIE's straw springs up",
              ["YEHYEH", "ROSIE"], "fond and reassuring", "pushes in", "a puff of steam"),
         ]},
        {"title": "The lucky ones", "place": "kitchen", "time": "night",
         "angle": "Warm close two-shot across two bamboo trays in",
         "who": "TORI scoops two small egg-shaped dough balls from one tray onto her own tray of perfectly round "
                f"ones, green straw bobbing, smiling sideways; {ROSIE_CUP} looks up at her big sister with shining "
                "eyes",
         "beats": [
             ("Tori's were perfectly round, of course. She scooped two of Rosie's eggs onto her own tray.",
              "medium close-up", "TORI scoops two egg-shaped dough balls onto her own tray", "TORI",
              "sly and kind", "pans right", "a soft scrape on bamboo"),
             ("\"I want the egg ones,\" said Tori. \"They're lucky. You've got this, little sip.\"",
              "medium close-up", "TORI leans her cup gently against ROSIE and ROSIE's straw wiggles",
              ["TORI", "ROSIE"], "warm and proud", "pushes in", "a soft clink of cups"),
         ]},
        {"title": "When they float", "place": "kitchen", "time": "night",
         "angle": "Over-the-shoulder view past the rim of the black iron pot in",
         "who": "MOM stands on the hearth bench tipping a bamboo tray of little white dough balls into the "
                "steaming ginger soup with a long wooden spoon in her other tiny arm, calm and smiling; white "
                "dough balls bob in the golden soup, round ones, egg-shaped ones and one flat one; BARNABY stands on "
                "the bench beside her hugging his giant white dough ball; KYLE waits below with an empty bowl held "
                "up high",
         "beats": [
             ("Mom slid them all into the bubbling ginger soup. \"When they float, they are done.\"",
              "medium shot", "MOM tips the tray and the little dough balls slide into the soup", "MOM",
              "calm and careful", "tilts down", "soft plops and a bubbling pot"),
             ("Up they bobbed, one by one. Round ones. Egg ones. One latke.",
              "close-up", "MOM stirs slowly as white dough balls rise to the top of the golden soup", "MOM",
              "pleased and amused", "pushes in", "a bubbling pot and a slow wooden stir"),
             ("Then Barnaby's snowball went in. SPLOOSH! Ginger rain. Kyle held out his bowl and caught some.",
              "medium shot", "BARNABY drops his giant dough ball into the pot and KYLE holds his bowl up under the splash",
              ["BARNABY", "KYLE"], "gleeful and soggy", "pulls back", "one enormous sploosh and pattering drops"),
         ]},
        {"title": "One year older", "place": "kitchen", "time": "night",
         "angle": "Close view at bowl height along the bench by the fire in",
         "who": "YEHYEH holds a steaming blue-and-white bowl of little white rice balls in golden soup and lifts "
                "one on a porcelain spoon; KYLE sits beside him with an empty bowl in his paws and soup on his "
                "muzzle, looking at the big pot with a serious thinking face",
         "beats": [
             ("Everybody got a warm bowl. \"Eat your tangyuan,\" said Yeh Yeh, \"and you are one year older.\"",
              "medium shot", "YEHYEH lifts one little rice ball on his spoon and nods", "YEHYEH",
              "merry and wise", "pushes in", "a soft clink of a spoon on a bowl"),
             ("Kyle stopped chewing. \"How many bowls until I'm a grown-up?\"",
              "medium close-up", "KYLE holds up his empty bowl and tilts his head", "KYLE",
              "earnest and hopeful", "holds still", "a spoon clink on an empty bowl"),
             ("\"One bowl, one year,\" said Yeh Yeh. Kyle eyed the pot. Then he decided to stay a cub.",
              "medium shot", "KYLE looks at the big pot, then hugs his bowl and leans against YEHYEH",
              ["KYLE", "YEHYEH"], "content and cozy", "pans left", "a soft bubbling pot and a creak of the bench"),
         ]},
        {"title": "The good news", "place": "kitchen", "time": "night",
         "angle": "Medium view toward the small dark window with its frost ferns in",
         "who": "YEHYEH points his bamboo walking stick at the dark window, firelight on his spectacles; "
                f"{ROSIE_CUP} sits on the bench edge beside him holding an empty little bowl in front of her cup, "
                "looking where he points with her straw slowly rising",
         "beats": [
             ("\"Now the good news,\" said Yeh Yeh. He pointed his stick at the dark window.",
              "medium shot", "YEHYEH lifts his bamboo stick and points it at the window", "YEHYEH",
              "gentle and sure", "pans right", "a crackling fire"),
             ("\"Tonight the dark is as long as it can ever get. It cannot grow one minute more.\"",
              "medium close-up", "YEHYEH lowers his stick and turns to ROSIE with crinkled eyes", ["YEHYEH", "ROSIE"],
              "kind and certain", "pushes in", "a crackling fire and wind at the glass"),
             ("\"Tomorrow the sun stays a little longer. The next day, longer still. All the way to summer.\"",
              "close-up", "ROSIE looks at the window and her straw rises", "ROSIE",
              "wide-eyed and wondering", "holds still", "a soft crackling fire"),
         ]},
        {"title": "The light comes back", "place": "kitchen", "time": "night",
         "angle": "Warm wide view of everyone squeezed along the fireside bench in",
         "who": f"{ROSIE_CUP} sits in the middle of the bench with her straw tall; HERSCHEL sits at one end counting "
                "on his flippers with a twinkle; MOM sits close beside ROSIE with one tiny arm around her; NORA "
                "sits at the other end with her shawl spread wide",
         "beats": [
             ("Rosie's straw shot up. \"Then sunset goes back on my list. One minute later, every day!\"",
              "medium close-up", "ROSIE turns from the window and her straw stands tall", "ROSIE",
              "delighted and busy", "pushes in", "a soft crackling fire"),
             ("\"That is why everybody lights something in December,\" said Herschel. \"Candles. Crowns. Lanterns.\"",
              "medium shot", "HERSCHEL counts three on his big flippers and beams", "HERSCHEL",
              "jolly and wise", "pans right", "a crackling fire and a clap of flippers"),
             ("\"And why we sit close and eat something round,\" said Mom. \"Everybody together.\"",
              "medium close-up", "MOM squeezes ROSIE gently and NORA spreads her shawl wider", ["MOM", "ROSIE", "NORA"],
              "snug and content", "pulls back", "a soft squeeze and a crackling fire"),
         ]},
        {"title": "Round and white", "place": "lane_night", "time": "night",
         "angle": "Low angle looking up at the long lantern string above",
         "who": "YEHYEH holds a long thin lighting taper up to a perfectly round white paper lantern, spectacles "
                "glowing; BARNABY stretches up on his tiptoes with both flippers to hook the lantern on the "
                f"string; {ROSIE_CUP} stands on a snowy crate below, peering at the lantern with one eye squinted",
         "beats": [
             ("Out they went into the longest night, with the day's lantern. Round and white, like a tangyuan.",
              "medium shot", "BARNABY stretches up and hooks the round white lantern on the string", "BARNABY",
              "careful and proud", "tilts up", "a soft paper rustle and crunching snow"),
             ("Yeh Yeh lit it. Barnaby hung it. It was not egg-shaped. Rosie checked.",
              "medium close-up", "YEHYEH lifts his taper and the lantern glows while ROSIE squints up at its shape",
              ["YEHYEH", "ROSIE"], "careful and amused", "pushes in", "a tiny flicker and a soft paper rustle"),
             ("\"One more light,\" said Rosie. \"And tomorrow, one more minute of sun.\"",
              "medium shot", "ROSIE gives one small proud bounce on her crate", "ROSIE",
              "glad and brave", "pulls back", "a soft hush of falling snow"),
         ]},
        {"title": "Nobody minded the dark", "place": "lane_night", "time": "night",
         "angle": "Wide view down the glowing snowy lane under the stars in",
         "who": "NORA stands in the snow with her pale-blue shawl wrapped around TORI and CAT the little blue "
                "penguin, who snuggle against her, all three looking up at the row of lanterns with soft smiles",
         "beats": [
             ("Nora wrapped her shawl around one cup and one penguin. Nobody minded the dark.",
              "wide shot", "NORA tucks her shawl around TORI and CAT and they lean in close", ["NORA", "TORI", "CAT"],
              "snug and peaceful", "pulls back", "soft snow falling and a far sizzle"),
             ("Twenty-one lanterns glowed down the lane. The longest night was also the brightest yet.",
              "wide shot", "the long row of paper lanterns sways gently and glows a little warmer", [],
              "hushed and glowing", "tilts up", "soft snow falling and paper lanterns rustling"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably closed; "
                "CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, yellow scarf "
                "visible",
         "beats": [
             ("Goodnight, little sip, one bowl older. Goodnight, Yeh Yeh, round as the moon.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, longest night, you have had your turn. Tomorrow comes a little brighter, just for you.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, one bowl older.",
        "Goodnight, Yeh Yeh, round as the moon.",
        "Goodnight, longest night, you have had your turn.",
        "Tomorrow comes a little brighter, just for you.",
    ],
}
