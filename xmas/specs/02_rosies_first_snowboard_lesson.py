"""02 — Rosie's First Snowboard Lesson (Wednesday, December 2)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "02",
    "slug": "rosies-first-snowboard-lesson",
    "title": "Rosie's First Snowboard Lesson",
    "meta": [
        ("Day", "Wednesday, December 2"),
        ("Holiday thread", "A snow day: the first lesson on the Bunny Bump"),
        ("Guests", "Willa Wobble ❄️ (Cat's tiny cousin), Finnegan Flipsworth ❄️, Kyle the black bear cub "
                   "(briefly a snowball)"),
        ("Cat’s role", "the teacher: bend, look where you want to go, arms out; shows off one hip-hop wiggle, "
                       "flops down on purpose to prove that snow is a pillow, and leads the wobbly line down"),
        ("Mandarin", "滑雪板 snowboard · 加油 you can do it · 再一次 one more time"),
        ("Setting", "The great hall of Frostpeak Lodge, the Bunny Bump beginner slope, Lantern Lane at night, "
                    "and the lodge bunk room"),
    ],
    "palette": "powder white and bright sky blue with saturated carrot orange and violet purple accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "WILLA", "FINNEGAN", "KYLE"],
    "cast_note": "Humans in this story: none. Rosie rides a tiny purple snowboard exactly her size; she stands "
                 "on it as a cup and sits down softly in powder snow when she falls. Kyle spends the middle of "
                 "the story packed in a big round snowball with his head, hat and paws poking out, until the "
                 "snowball pops in the cushions at the bottom.",
    "key_shot": 13,
    "places": {
        "hall": DOORWALL,
        "bump": {
            "name": "the Bunny Bump, the beginner slope of Frostpeak",
            "scene": "the Bunny Bump beginner slope",
            "props": "a gentle little hill of soft powder snow, a snow sculpture of a bunny with long ears at the "
                     "top, a row of carrot-orange flags, a slow wooden chairlift with red bench seats, a rack of "
                     "tiny snowboards, a stop wall of hay bales padded with striped cushions",
            "light": "Bright blue-sky winter sun sparkles on the powder",
            "accents": "carrot orange and violet purple",
            "atmo": "Glittering snow dust hangs in the cold air",
            "motion": "glittering snow dust drifts over the slope",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny purple snowboard and a little picture list covered in ticks on the nightstand"),
    },
    "shots": [
        {"title": "Door two", "place": "hall",
         "angle": "Low angle looking up the Door Wall in",
         "who": "CAT the little blue penguin hangs in mid-jump with one flipper on the brass knob of a little "
                f"door carved with a plain snowboard, beak set in effort; {ROSIE_CUP} stands on the rug below "
                "looking up, straw perked",
         "beats": [
             ("Good morning, Frostpeak Lodge! Door two was a little higher. Cat the penguin had to jump.",
              "medium shot", "CAT springs up and catches the brass knob with one flipper", "CAT",
              "determined and bouncy", "tilts up", "a little grunt of effort and a crackling fire"),
         ]},
        {"title": "A tiny purple snowboard", "place": "hall",
         "angle": "Close view at the open little door in",
         "who": f"a tiny purple snowboard leans inside the open little door; {ROSIE_CUP} stands in front of it "
                "holding a little picture list in front of her cup, straw wiggling; CAT the little blue penguin "
                "points both flippers at the board with a huge grin",
         "beats": [
             ("Click! Behind it stood a tiny purple **滑雪板** (huáxuě bǎn) = snowboard. Exactly cup-sized.",
              "close-up", "ROSIE leans toward the tiny purple snowboard with wide eyes", "ROSIE",
              "amazed and tempted", "pushes in", "a tiny hinge creak and a crackling fire"),
             ("\"Snowboard day!\" cheered Cat. Rosie's straw wiggled. Then it wobbled. So she made a list.",
              "medium shot", "CAT bounces on her pink feet and points both flippers at the board", "CAT",
              "thrilled and proud", "pulls back", "happy little foot taps on the rug"),
             ("One: learn to snowboard. Two: do not fall down. Not even once.",
              "medium close-up", "ROSIE holds her little picture list up in front of her cup and nods firmly",
              "ROSIE", "serious and a little nervous", "holds still", "a paper rustle"),
         ]},
        {"title": "The Bunny Bump", "place": "bump",
         "angle": "Wide establishing view from the very bottom of",
         "who": f"{ROSIE_CUP} stands at the foot of the little hill on a tiny purple snowboard, looking up with "
                "her straw tipped back; MOM kneels beside her fastening the board's little strap, a steaming "
                "cocoa flask tucked under one tiny arm",
         "beats": [
             ("The Bunny Bump was the smallest hill in Frostpeak. To Rosie, it looked like a mountain.",
              "wide shot", "ROSIE tips her lid back to look up the little hill", "ROSIE", "small and impressed",
              "tilts up", "a slow creak of the chairlift and a hush of wind"),
             ("Mom clipped Rosie onto the tiny board. \"I'll be right here,\" she said, \"with the cocoa.\"",
              "medium shot", "MOM pats the little strap snug and holds up her cocoa flask", "MOM",
              "calm and steady", "pushes in", "a tiny buckle click and a slosh of cocoa"),
         ]},
        {"title": "Bend, look, arms out", "place": "bump",
         "angle": "Medium view on the gentle top of",
         "who": "CAT the little blue penguin stands on her little snowboard with her knees bent and both "
                f"flippers stretched out like wings, looking far down the slope; {ROSIE_CUP} stands on her tiny "
                "purple snowboard beside her, copying with her tiny arms out and her straw bent forward",
         "beats": [
             ("\"Three things,\" said Cat. \"Bend your knees. Look where you want to go. Arms out like wings.\"",
              "medium shot", "CAT bends low on her board and stretches both flippers wide", "CAT",
              "clear and teacherly", "tracks beside", "a soft squeak of snow under a board"),
             ("\"I don't have knees,\" said Rosie. \"Bend your straw,\" said Cat. \"That's what I'd do.\"",
              "medium close-up", "ROSIE bends her straw forward and CAT gives a flipper thumbs-up", ["ROSIE", "CAT"],
              "earnest and amused", "pushes in", "a tiny straw squeak"),
             ("Cat went first. Swoosh, swish, a spin, a hip-hop wiggle. \"Easy,\" she said. \"Eventually.\"",
              "medium shot", "CAT swishes her board from side to side and wiggles her hips", "CAT",
              "showy and honest", "tracks beside", "a swish-swish of a board on snow"),
         ]},
        {"title": "How do I stop?!", "place": "bump",
         "angle": "Dynamic diagonal view down",
         "who": "FINNEGAN rockets down the slope on his red snowboard with his flippers windmilling and his spiky "
                "yellow crest blown flat, beak wide open, heading straight for the cushioned hay bales",
         "beats": [
             ("Then Finnegan Flipsworth shot past, crest flapping. \"WOOOHOOO—wait, how do I stop?!\"",
              "wide shot", "FINNEGAN zooms downhill with his flippers windmilling", "FINNEGAN",
              "thrilled, then alarmed", "pans right", "a fast swoosh of a snowboard and a rush of wind"),
         ]},
        {"title": "How not to stop", "place": "bump",
         "angle": "Close view at the cushioned hay bales at the bottom of",
         "who": "FINNEGAN is stuck headfirst in the striped cushions with only his feet and his red snowboard "
                "sticking out; CAT the little blue penguin stands beside him pointing one flipper like a teacher "
                "at a chalkboard",
         "beats": [
             ("FWUMP! He stopped. In the hay bales. Only his feet stuck out.",
              "medium shot", "FINNEGAN's feet wiggle in the air above the striped cushions", "FINNEGAN",
              "stuck and unbothered", "pushes in", "a soft cushiony thump and a rustle of hay"),
             ("\"That,\" said Cat, \"is how not to stop.\" \"You're welcome,\" said the feet.",
              "medium close-up", "CAT points at the cushions while FINNEGAN's feet give a little wave",
              ["CAT", "FINNEGAN"], "dry and cheerful", "holds still", "a rustle of hay"),
         ]},
        {"title": "A snowball with a hat", "place": "bump",
         "angle": "Low angle at the snowy bottom of",
         "who": "KYLE is packed inside a big round snowball with only his head in its red beanie, his tan muzzle "
                "and his four paws poking out, grinning with snow on his nose",
         "beats": [
             ("Kyle went next. He tipped. He tumbled. He rolled all the way down.",
              "wide shot", "KYLE rocks to a stop inside the big snowball and blinks", "KYLE",
              "dizzy and delighted", "pushes in", "a soft rumbling thud in the snow"),
             ("At the bottom he was a snowball with a hat. \"I was just taste-testing the snow.\"",
              "medium close-up", "KYLE licks the snow off his nose and wiggles his four paws", "KYLE",
              "cheerful and unbothered", "holds still", "a lip smack and a soft crunch of snow"),
         ]},
        {"title": "Plop number one", "place": "bump",
         "angle": "Side view at snow level on",
         "who": f"{ROSIE_CUP} stands on her tiny purple snowboard on the gentle slope with her tiny arms out and "
                "her straw bent forward in concentration; CAT the little blue penguin watches from beside a "
                "carrot-orange flag with both flippers clasped",
         "beats": [
             ("Rosie's turn. Bend. Look. Arms out. She slid one whole inch.",
              "medium shot", "ROSIE slides a tiny way forward on her board with her arms out", "ROSIE",
              "focused and hopeful", "tracks beside", "a tiny hiss of a board on snow"),
             ("Plop! Down she sat, in soft snow. Nothing hurt. \"That's one,\" said Cat.",
              "medium shot", "ROSIE tips gently back and sits down in the powder with a puff", "ROSIE",
              "surprised and unhurt", "holds still", "a soft powdery plop"),
         ]},
        {"title": "Two and three", "place": "bump",
         "angle": "High angle looking straight down on the powder of",
         "who": f"{ROSIE_CUP} sits in a soft dent of powder snow beside her tiny purple snowboard with her straw "
                "drooping and a cap of snow on her lid",
         "beats": [
             ("Try two. Wobble, plop. Try three. Wobble, wiggle, plop.",
              "medium shot", "ROSIE pushes herself up and sits right back down with a puff of snow", "ROSIE",
              "trying hard and tired", "pushes in", "two soft powdery plops"),
             ("Three Rosie-shaped dents in a row. Her straw drooped. \"Three plops,\" said Rosie. \"I counted.\"",
              "medium close-up", "ROSIE's straw droops and a little snow slides off her lid", "ROSIE",
              "rumpled and matter-of-fact", "pulls back", "a hush of wind over snow"),
         ]},
        {"title": "Willa counted", "place": "bump",
         "angle": "Low close view across the powder on",
         "who": "WILLA shuffles close on her tiny purple snowboard, fluffy purple earmuffs a little crooked, shy "
                f"eyes shining; {ROSIE_CUP} sits in the snow looking at her with a drooping straw",
         "beats": [
             ("A very tiny penguin in purple earmuffs shuffled over. It was Willa Wobble, Cat's cousin.",
              "medium shot", "WILLA shuffles one small step closer on her tiny board", "WILLA",
              "shy and kind", "tracks beside", "tiny shuffling scrapes on snow"),
             ("\"I fell forty times my first day,\" Willa whispered. \"I counted too. Cat fell fifty.\"",
              "medium close-up", "WILLA leans in close behind one tiny flipper", "WILLA",
              "shy and a little cheeky", "pushes in", "a hush of wind"),
             ("\"The smallest step is still a step,\" said Willa. \"Even a sitting-down one.\"",
              "close-up", "WILLA nods and ROSIE's straw lifts a little", ["WILLA", "ROSIE"],
              "gentle and sure", "holds still", "a hush of wind and a tiny happy squeak"),
         ]},
        {"title": "Snow is a pillow", "place": "bump",
         "angle": "High angle looking straight down onto the soft powder of",
         "who": "CAT the little blue penguin lies flat on her back in the snow with her flippers spread wide, "
                f"grinning up at the sky; {ROSIE_CUP} lies on her back beside her in a neat cup-shaped dent with "
                "her straw pointing at the sky, giggling; WILLA lies on her other side sweeping two tiny "
                "flippers through the powder",
         "beats": [
             ("\"Fifty-one,\" said Cat, and she flopped down on purpose. \"See? Snow is a pillow.\"",
              "medium shot", "CAT pats the powder with both flippers and kicks her pink feet", "CAT",
              "proud and silly", "tilts down", "a soft powdery flump"),
             ("So everybody flopped. Two snow angels, and one shaped exactly like a cup. A snow teacup.",
              "wide shot", "WILLA sweeps her flippers through the snow while ROSIE's straw wiggles at the sky",
              ["WILLA", "ROSIE"], "giggly and carefree", "pulls back", "soft swishes of flippers in powder"),
         ]},
        {"title": "Tori on the chairlift", "place": "bump",
         "angle": "Low angle from the slope looking up at the slow wooden chairlift above",
         "who": "TORI rides a red chairlift bench high overhead, leaning over the safety bar and waving both tiny "
                "arms, green straw bobbing, mouth open in a cheer",
         "beats": [
             ("\"**加油** (jiāyóu) = you can do it!\" called Tori, high up on the chairlift.",
              "wide shot", "TORI leans over the safety bar and waves both tiny arms", "TORI",
              "loud and proud", "tilts up", "a slow creak of the chairlift cable"),
             ("\"You've got this, little sip!\" She waved so hard the whole chair swung.",
              "medium shot", "TORI waves harder and the red bench swings gently back and forth", "TORI",
              "cheering with her whole heart", "pushes in", "a creak-creak of the swinging bench"),
         ]},
        {"title": "Try four", "place": "bump",
         "angle": "Dynamic side view tracking down",
         "who": f"{ROSIE_CUP} glides down the gentle slope standing on her tiny purple snowboard with her tiny "
                "arms out and her straw bent forward, eyes wide and shining, carrot-orange flags sliding past "
                "behind her",
         "beats": [
             ("Try four. Bend the straw. Look where you want to go. Arms out.",
              "medium shot", "ROSIE bends her straw forward and stretches her tiny arms wide", "ROSIE",
              "focused and steady", "tracks beside", "a soft hiss of a board on snow"),
             ("And Rosie slid. One second. Two seconds. The orange flags went by.",
              "wide shot", "ROSIE glides smoothly down the gentle slope on her tiny board", "ROSIE",
              "amazed and gliding", "tracks beside", "a long smooth hiss of a board on snow"),
             ("Three whole seconds! Then, plop. But this plop had a glide in front of it.",
              "medium shot", "ROSIE sits down softly in the powder and her straw shoots straight up", "ROSIE",
              "astonished and thrilled", "pushes in", "a soft powdery plop and a tiny straw squeak"),
         ]},
        {"title": "Three seconds!", "place": "bump",
         "angle": "Wide view across the snowy bottom of",
         "who": f"{ROSIE_CUP} sits in soft snow with her straw straight up and a huge smile; WILLA hops beside "
                "her with both tiny flippers up; FINNEGAN leans out of the hay bales with a striped cushion on "
                "his head, cheering; KYLE, still a round snowball with a hat, claps the two front paws that "
                "poke out",
         "beats": [
             ("\"Three seconds!\" squeaked Willa. Finnegan cheered from the hay bales. The snowball clapped.",
              "wide shot", "WILLA hops up and down while KYLE claps his paws and FINNEGAN waves a flipper",
              ["WILLA", "KYLE", "FINNEGAN"], "overjoyed and noisy", "pulls back",
              "happy flipper slaps and muffled paw claps"),
             ("\"**再一次** (zài yí cì) = one more time!\" said Rosie. And up she got.",
              "medium close-up", "ROSIE pushes herself up onto her board with a proud little bounce", "ROSIE",
              "eager and proud", "pushes in", "a crunch of snow and a tiny happy squeak"),
         ]},
        {"title": "The wobbly line", "place": "bump",
         "angle": "Sweeping downhill view of the gentle slope of",
         "who": "CAT the little blue penguin leads a wobbly line down the slope on her snowboard with her "
                f"flippers out; {ROSIE_CUP} glides behind her on her tiny purple snowboard with her straw bent "
                "forward; WILLA follows on her tiny board holding her earmuffs on; FINNEGAN brings up the rear "
                "sliding backwards with his flippers windmilling; KYLE, a big round snowball with a hat, looms "
                "at the top of the hill behind them",
         "beats": [
             ("So down they all went in one wobbly line. Cat, Rosie, Willa, and Finnegan, backwards.",
              "wide shot", "CAT leads the line downhill while FINNEGAN windmills his flippers at the back",
              ["CAT", "FINNEGAN"], "gleeful and wobbly", "tracks beside", "four boards hissing on snow"),
         ]},
        {"title": "Strike!", "place": "bump",
         "angle": "Close view into the striped cushions at the bottom of",
         "who": "a happy heap in the cushions: FINNEGAN at the bottom with only his yellow crest and beak "
                f"showing; CAT the little blue penguin and WILLA tangled on top of him; {ROSIE_CUP} sitting "
                "upright in the middle with a striped cushion on her lid; KYLE on the very top, a bear again, "
                "with lumps of burst snowball all around him",
         "beats": [
             ("Behind them rolled Kyle the snowball. Bonk, bonk, bonk, bonk. Everybody into the cushions!",
              "medium shot", "KYLE shakes the last lumps of snow off his fur on top of the heap", "KYLE",
              "dizzy and delighted", "pushes in", "four soft bonks and a cushiony whump"),
             ("\"Strike!\" yelled Finnegan, from the bottom of the pile. The snowball had popped. Kyle was a bear again.",
              "medium close-up", "FINNEGAN's crest pops up from the cushions and ROSIE's straw springs up",
              ["FINNEGAN", "ROSIE"], "squashed and overjoyed", "holds still", "a rustle of hay and a soft cushiony squeak"),
         ]},
        {"title": "Right here", "place": "bump",
         "angle": "Warm close view beside the rack of tiny snowboards at the foot of",
         "who": "MOM pours steaming cocoa from her flask into a row of tiny mugs, eyes warm and proud; "
                f"{ROSIE_CUP} stands beside her dusted with snow, straw wiggling high; CAT the little blue "
                "penguin leans on her snowboard with a proud teacher's grin",
         "beats": [
             ("Mom poured the cocoa. She had been right there for every single second. All three.",
              "medium shot", "MOM pours a little stream of steaming cocoa and smiles down", "MOM",
              "proud and calm", "pushes in", "a glug of cocoa and a curl of steam"),
             ("\"Best student I ever had,\" said Cat. \"Also the only one. Still counts.\"",
              "medium close-up", "CAT leans on her board and pats ROSIE's lid with one flipper", ["CAT", "ROSIE"],
              "proud and cheeky", "holds still", "a soft pat and a slurp of cocoa"),
         ]},
        {"title": "The purple lantern", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the lantern string over",
         "who": "WILLA stands on tiptoe on an upturned sled holding up a round purple paper lantern with both "
                f"tiny flippers, earmuffs crooked, eyes brave; {ROSIE_CUP} stands below with her straw tall; "
                "KYLE stands beside them, dripping, with one last cap of snow on his beanie",
         "beats": [
             ("At dusk the snow turned pink, then blue. Everybody slid down to Lantern Lane.",
              "medium shot", "KYLE shakes himself and a last lump of snow slides off his beanie", "KYLE",
              "damp and cheerful", "pans left", "a wet shake and a plop of snow"),
             ("Willa climbed the sled, one small step at a time, and hung up the purple lantern.",
              "medium shot", "WILLA stretches up on tiptoe and hooks the purple lantern onto the string", "WILLA",
              "careful and brave", "tilts up", "a tiny brass click and a paper rustle"),
             ("\"One more light,\" she whispered. It was the loudest thing she said all day.",
              "close-up", "WILLA looks up at the glowing purple lantern and her eyes shine", "WILLA",
              "quietly proud", "pushes in", "a soft paper flutter"),
         ]},
        {"title": "The list", "place": "lane", "time": "night",
         "angle": "Warm close view under the glowing lantern string on",
         "who": f"{ROSIE_CUP} stands in the snow holding her little picture list in front of her cup, purple "
                "glow on her lid, straw wiggling; TORI leans down beside her to look, green straw tilted",
         "beats": [
             ("Rosie checked her list. Plops: four. Glides: one. Snow teacups: one. Strikes: one.",
              "medium close-up", "ROSIE taps her little picture list three times and TORI leans in to see",
              ["ROSIE", "TORI"], "satisfied and proud", "pushes in", "three tiny pencil taps"),
             ("\"Tomorrow,\" said Rosie, \"four seconds.\" Her straw wiggled all the way home.",
              "medium shot", "ROSIE's straw wiggles and she gives one happy bounce", "ROSIE",
              "hopeful and glowing", "pulls back", "soft footsteps in snow"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep on a soft pillow at the foot of the bunk with one "
                "flipper resting on her little snowboard, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, with snow in your straw. Goodnight, Cat, the best teacher on the hill.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, purple lantern, number two. May your dreams glide for three whole seconds, and more.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, with snow in your straw.",
        "Goodnight, Cat, the best teacher on the hill.",
        "Goodnight, purple lantern, number two.",
        "May your dreams glide for three whole seconds, and more.",
    ],
}
