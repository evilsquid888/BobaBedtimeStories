"""03 — The Wonky Tree (Thursday, December 3)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
TREE = "the small crooked pine tree with a bent top"

STORY = {
    "num": "03",
    "slug": "the-wonky-tree",
    "title": "The Wonky Tree",
    "meta": [
        ("Day", "Thursday, December 3"),
        ("Holiday thread", "Choosing and decorating the Christmas tree"),
        ("Guests", "Bjorn Bigpaws ❄️, Magnus Meltsworth ❄️, Kyle the black bear cub, Lina the snowflake crisp"),
        ("Cat’s role", "tree scout who wants one she can see the top of; hangs pinecones with gentle kung fu; "
                       "keeps count of Magnus's noble acts"),
        ("Mandarin", "聖誕樹 Christmas tree · 歪歪的 wonky · 爆米花 popcorn"),
        ("Setting", "The great hall of Frostpeak Lodge, the Whispering Pines tree grove, Lantern Lane at night, "
                    "and the lodge bunk room"),
    ],
    "palette": "deep pine green and snowy white with saturated ribbon red and warm firelight gold accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "BJORN", "MAGNUS", "KYLE", "LINA"],
    "cast_note": "Humans in this story: none. The wonky tree is a small living pine, about three cups tall, whose "
                 "top bends over like a question mark; it travels and stands in a big red clay pot, roots and "
                 "all. Day 23 calls back to its bent top.",
    "key_shot": 15,
    "places": {
        "hall": DOORWALL,
        "grove": {
            "name": "the Whispering Pines tree grove",
            "scene": "the Whispering Pines grove",
            "props": "rows of tall snowy pine trees tied with red ribbons, a split-log fence, a wooden tree sled "
                     "with a coil of rope, a stump holding a tin cocoa flask, pinecones scattered on the snow, "
                     "a little woodcutter's hut with a smoking chimney",
            "light": "Low golden winter sun slants between the trunks in long beams",
            "accents": "pine green and ribbon red",
            "atmo": "Snow sifts down from the high branches in sparkling veils",
            "motion": "snow sifts down from the high branches",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny pinecone and a curl of red ribbon on the nightstand"),
    },
    "shots": [
        {"title": "Door three", "place": "hall",
         "angle": "Low angle looking up the Door Wall in",
         "who": "LINA stands on a footstool beside an open little door with a tiny pinecone inside, a puff of "
                "white powdered sugar bursting off her corners, very pleased with herself; CAT the little blue "
                f"penguin points both flippers up at the pinecone; {ROSIE_CUP} stands beside the footstool "
                "holding a little picture list in front of her cup",
         "beats": [
             ("Door three was Lina's turn. She hopped up to the knob. Poof! Sugar snow everywhere.",
              "medium shot", "LINA lands with a hop and a white puff of sugar bursts around her", "LINA",
              "bubbly and pleased with herself", "tilts up", "a soft poof and a crackling fire"),
             ("Behind the door sat a tiny pinecone. \"Tree day!\" said Cat the penguin.",
              "medium close-up", "CAT points both flippers up at the tiny pinecone and bounces", "CAT",
              "excited and sure", "pushes in", "happy little foot taps on the rug"),
             ("Rosie made a list for the lodge's **聖誕樹** (shèngdàn shù) = Christmas tree. Tall. Straight. Perfect.",
              "medium close-up", "ROSIE holds her little picture list up in front of her cup and nods three times",
              "ROSIE", "serious and organized", "holds still", "a paper rustle"),
         ]},
        {"title": "The Whispering Pines", "place": "grove",
         "angle": "Wide establishing view with deep perspective down a snowy aisle of",
         "who": f"{ROSIE_CUP} stands small between the rows of tall pines with her straw tipped back; TORI looks "
                "up beside her with her green straw tilted; MOM holds one tiny arm up to her lid in a gentle "
                "hush, smiling",
         "beats": [
             ("The Whispering Pines stood in long snowy rows. When the wind blew, they all went shhhh.",
              "wide shot", "ROSIE tips her lid back and looks up at the swaying treetops", "ROSIE",
              "awed and hushed", "tilts up", "a long soft hush of wind in pine needles"),
             ("\"Like a hundred librarians,\" whispered Mom. So everybody whispered. Even Kyle. For almost a minute.",
              "medium shot", "MOM lifts one tiny arm to her lid in a hush and her eyes crinkle", "MOM",
              "playful and calm", "pushes in", "a long soft hush of wind"),
         ]},
        {"title": "Two bears and a sled", "place": "grove",
         "angle": "Low angle looking up from the wooden tree sled in",
         "who": "BJORN stands tall on his forest-green skis with the sled rope over one shoulder, chest out, a "
                "noble smile; MAGNUS stands beside him on his old wooden skis with his arms folded and his "
                "bushy eyebrows pulled down in a frown",
         "beats": [
             ("Two polar bears were waiting. Bjorn Bigpaws had a sled, a rope, and a noble look.",
              "medium shot", "BJORN lifts his chin and hoists the sled rope higher on his shoulder", "BJORN",
              "noble and ready", "tilts up", "a creak of rope and a crunch of snow"),
             ("Magnus Meltsworth had a frown. \"I'm only here to carry it,\" he grumbled. Nobody had asked.",
              "medium close-up", "MAGNUS folds his arms tighter and huffs a cloud of breath", "MAGNUS",
              "grumpy and secretly willing", "pans right", "one long grumbly huff"),
         ]},
        {"title": "The tallest, the straightest", "place": "grove",
         "angle": "Wide view up the towering trunks of",
         "who": "KYLE hugs the trunk of the very tallest pine with both arms, looking straight up; TORI points "
                "one tiny arm at a perfectly straight pine with a red ribbon; CAT the little blue penguin stands "
                "between them leaning so far back to see the treetops that she is about to tip over",
         "beats": [
             ("Everybody wanted the best tree. \"The tallest!\" said Kyle. \"The straightest!\" said Tori.",
              "wide shot", "KYLE hugs the tallest trunk while TORI points up at her straight pine", ["KYLE", "TORI"],
              "eager and competitive", "tilts up", "a pat of paws on bark and a hush of wind"),
             ("\"One I can see the top of,\" said Cat. She leaned back to look. Flump.",
              "medium shot", "CAT leans back further and further and tips over into the snow", "CAT",
              "curious, then flat on her back", "tilts down", "a soft powdery flump"),
         ]},
        {"title": "Too tall", "place": "grove",
         "angle": "Steep upward view along an enormous trunk in",
         "who": "BJORN holds one forest-green ski upright against the trunk of the very tallest pine like a "
                "ruler, squinting up with great seriousness; KYLE stands beside him with one paw raised and a "
                "helpful, hungry grin",
         "beats": [
             ("Bjorn measured the tallest one with a ski. \"Too tall. We would need a hole in the roof.\"",
              "medium shot", "BJORN slides his ski up the trunk and shakes his head slowly", "BJORN",
              "solemn and thorough", "tilts up", "a scrape of a ski on bark"),
             ("\"I could taste-test a hole,\" said Kyle. \"No,\" said everybody. Even the trees said shhhh.",
              "medium close-up", "KYLE raises his paw higher and then slowly lowers it", "KYLE",
              "helpful, then outvoted", "holds still", "a long soft hush of wind in pine needles"),
         ]},
        {"title": "The small one", "place": "grove",
         "angle": "Low angle at snow level toward the far end of the row in",
         "who": f"{TREE} stands alone at the end of the row, the top curled over like a question mark, plain "
                f"green and bare of ribbons; {ROSIE_CUP} stands in front of it, as tall as its lowest branch, "
                "looking up with a softly tilted straw",
         "beats": [
             ("At the very end of the row stood a small tree. Rosie stopped.",
              "wide shot", "ROSIE takes one small hop toward the little tree and stops", "ROSIE",
              "curious and quiet", "pushes in", "a tiny crunch of snow"),
             ("Its top bent over like a question mark. It had no ribbon. Nobody had picked it.",
              "medium shot", "ROSIE looks slowly up to the bent top of the little tree", "ROSIE",
              "thoughtful and tender", "tilts up", "a hush of wind in pine needles"),
         ]},
        {"title": "Wonky", "place": "grove",
         "angle": "Medium view beside the split-log fence in",
         "who": f"KYLE tilts his whole head sideways to match {TREE}, puzzled; {ROSIE_CUP} stands close beside "
                "the little tree with her lid tipped toward it in a tiny bow, straw perked",
         "beats": [
             ("\"That one?\" said Kyle. He tilted his head to match. \"It's **歪歪的** (wāi wāi de) = wonky.\"",
              "medium shot", "KYLE tilts his head further sideways and squints at the bent top", "KYLE",
              "puzzled and honest", "pans right", "a soft creak of the fence"),
             ("Rosie liked it. It looked like it was bowing hello. \"I pick this one,\" she said.",
              "medium close-up", "ROSIE bows her lid to the little tree and her straw stands up straight", "ROSIE",
              "charmed and certain", "pushes in", "a hush of wind and a tiny crunch of snow"),
         ]},
        {"title": "Then it's ours", "place": "grove",
         "angle": "Warm close view under the bent treetop in",
         "who": f"TORI bows low to {TREE} with one tiny arm across her cup, green straw dipping, smiling; "
                f"{ROSIE_CUP} stands beside her, beaming; MOM ties a red ribbon bow onto a low branch",
         "beats": [
             ("Tori looked at the tree. Then she bowed right back. \"Pleased to meet you. You're ours.\"",
              "medium close-up", "TORI dips into a deep bow to the little tree while ROSIE bounces beside her",
              ["TORI", "ROSIE"], "playful and fond", "pushes in", "a soft crunch of snow"),
             ("Mom tied on a red ribbon. Now it was picked.",
              "close-up", "MOM pulls the red ribbon bow snug on the branch", "MOM", "quiet and glad",
              "holds still", "a soft swish of ribbon"),
         ]},
        {"title": "Waving", "place": "grove",
         "angle": "Medium view from the other side of the little tree in",
         "who": f"KYLE tilts his head the opposite way beside {TREE}, a slow grin spreading; LINA stands on the "
                "fence rail with her tiny arms folded, squinting at the tree like a decorator, a sprinkle of "
                "powdered sugar on the rail",
         "beats": [
             ("Kyle tilted his head the other way. \"From this side, it looks like it's waving.\"",
              "medium shot", "KYLE tilts his head the other way and lifts one paw in a little wave", "KYLE",
              "won over and cheerful", "pans left", "a soft crunch of snow"),
             ("\"I can work with wonky,\" said Lina. \"Wonky has places to hang things.\"",
              "medium close-up", "LINA unfolds her tiny arms and frames the tree between them", "LINA",
              "expert and delighted", "pushes in", "a tiny poof of sugar"),
         ]},
        {"title": "A twig with ambition", "place": "grove",
         "angle": "Low angle looking up at a huge white bear in",
         "who": f"MAGNUS bends down over {TREE}, peering at it nose to needle with one bushy eyebrow raised; "
                f"{ROSIE_CUP} stands beside the tree looking up at him with "
                "hopeful eyes",
         "beats": [
             ("Magnus bent down and squinted. \"That is not a tree. That is a twig with ambition.\"",
              "medium shot", "MAGNUS leans down and raises one bushy eyebrow at the little tree", "MAGNUS",
              "gruff and unconvinced", "tilts down", "a creak of old wooden skis and a huff"),
         ]},
        {"title": "One noble act", "place": "grove",
         "angle": "Medium view beside the wooden tree sled in",
         "who": f"MAGNUS cradles {TREE} in both big arms, its roots in a big red clay pot, holding it as carefully "
                "as an egg, eyebrows grumpy and eyes soft; LINA and KYLE watch from the sled with open mouths",
         "beats": [
             ("He sighed. He scooped it up, roots and all. Gently as an egg.",
              "medium shot", "MAGNUS lifts the little tree in its red pot and holds it close", "MAGNUS",
              "careful and gruff", "tilts up", "a creak of old wooden skis and a soft scrape of a clay pot"),
             ("\"Fine. But this is my one noble act for the week.\" It was only Thursday.",
              "medium close-up", "MAGNUS frowns down at the little tree and tucks it more gently in his arms",
              "MAGNUS", "grumbling and gentle", "holds still", "one grumbly huff"),
         ]},
        {"title": "Descended with style", "place": "grove",
         "angle": "Wide view down the snowy hill below",
         "who": "BJORN sits upright in a burst snowbank with a tall heap of snow on his head like a hat and his "
                "forest-green skis crossed in front of him, chin lifted with great dignity; CAT the little blue "
                "penguin stands beside him with one flipper over her beak, giggling",
         "beats": [
             ("Bjorn skied the sled down the hill. Fast. Then faster. Then, FWUMP, into a snowbank.",
              "wide shot", "BJORN shakes his head once and snow slides down around his shoulders", "BJORN",
              "dazed and dignified", "pushes in", "a deep snowy thump and a slither of sliding snow"),
             ("He sat up wearing most of it as a hat. \"I did not fall. I descended with style.\"",
              "medium close-up", "BJORN lifts his chin under his snow hat while CAT hides her beak behind her flipper",
              ["BJORN", "CAT"], "noble and unbothered", "tilts up", "a soft plop of snow and a patter of little feet"),
         ]},
        {"title": "Decorating", "place": "hall",
         "angle": "Cozy wide view beside the Door Wall in",
         "who": f"{TREE} stands in its big red clay pot; LINA hops along one branch with puffs of white powdered "
                "sugar bursting from her corners onto the needles; KYLE sits beneath it threading a very short "
                "popcorn string with one cheek bulging; CAT the little blue penguin stands in a gentle kung fu "
                "pose with a pinecone ornament balanced on one flipper",
         "beats": [
             ("In the great hall, they decorated. Lina hopped from branch to branch. Poof! Poof! Sugar snow.",
              "medium shot", "LINA hops along the branch and a white puff of sugar settles on the needles", "LINA",
              "busy and delighted", "tracks beside", "two soft poofs and a crackling fire"),
             ("Kyle strung **爆米花** (bàomǐhuā) = popcorn. One for the string, two for Kyle. \"I was just taste-testing.\"",
              "medium close-up", "KYLE threads one piece of popcorn and pops another into his mouth", "KYLE",
              "caught and content", "pushes in", "crunchy munching"),
             ("Cat hung pinecones with gentle kung fu. Hi-ya, hook. Hi-ya, hook.",
              "medium shot", "CAT swings one flipper in a slow kung fu arc and hooks a pinecone onto a branch", "CAT",
              "focused and showy", "pans right", "a soft swish and a tiny click"),
         ]},
        {"title": "Where can it wait?", "place": "hall",
         "angle": "Close view up toward the bent treetop in",
         "who": "MOM holds up a round green paper lantern with both tiny arms, head tilted in a question; "
                f"{ROSIE_CUP} stands on the footstool beside {TREE}, looking from the lantern to the bent top "
                "with her straw shooting up; TORI holds the footstool steady with both tiny arms, grinning",
         "beats": [
             ("Mom held up today's lantern, green as a pine. \"Where can it wait until dark?\"",
              "medium shot", "MOM lifts the green lantern and tilts her lid in a question", "MOM",
              "wondering and calm", "pushes in", "a crinkle of paper and a crackling fire"),
             ("Rosie looked at the bent top. Her straw shot up. \"Stretch!\" said Tori. \"You've got this, little sip!\"",
              "medium shot", "TORI steadies the footstool while ROSIE stretches up on her toes", ["TORI", "ROSIE"],
              "thrilled and wobbly", "tilts up", "a creak of a footstool and a tiny straw squeak"),
         ]},
        {"title": "The perfect hook", "place": "hall",
         "angle": "Upward view of the decorated little tree beside the Door Wall in",
         "who": f"a round green paper lantern hangs from the curled tip of {TREE} like a hook made for it, the "
                "branches dusted with sugar snow, a short popcorn string and pinecone ornaments; "
                f"{ROSIE_CUP} stands below with her straw tall and her eyes shining; MAGNUS stands behind with "
                "his arms folded and one corner of his mouth lifted; BJORN claps his big paws beside him",
         "beats": [
             ("The bend was a hook! The lantern hung there perfectly, as if the tree had planned it.",
              "medium shot", "ROSIE bounces once and her straw wiggles as the green lantern sways gently", "ROSIE",
              "proud and overjoyed", "tilts up", "a soft paper sway and big paws clapping"),
             ("\"Hmf,\" said Magnus. From Magnus, that was a parade.",
              "medium close-up", "MAGNUS gives one short nod and BJORN claps his big paws", ["MAGNUS", "BJORN"],
              "gruffly impressed", "pushes in", "one grumbly hmf and soft paw claps"),
         ]},
        {"title": "The green lantern", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the lantern string over",
         "who": "MAGNUS reaches one long arm up and hangs a round green paper lantern on the string beside a "
                "red one and a purple one, frowning with care; CAT the little blue penguin stands at his feet "
                f"holding up two flippers, counting; {ROSIE_CUP} stands beside her with a little picture list "
                "held in front of her cup",
         "beats": [
             ("At dusk they carried it to Lantern Lane. The string was high. Everybody looked at Magnus.",
              "wide shot", "MAGNUS looks down at the little ones and heaves his shoulders in a sigh", "MAGNUS",
              "cornered and resigned", "tilts up", "a creak of old wooden skis and soft footsteps in snow"),
             ("He hung the green lantern beside the purple one. \"One more light,\" he grumbled.",
              "medium shot", "MAGNUS hooks the green lantern onto the string with one careful paw", "MAGNUS",
              "careful and gruff", "tilts up", "a tiny brass click and a paper rustle"),
             ("\"That's two noble acts,\" said Cat. \"Don't count,\" said Magnus. Rosie wrote it down anyway.",
              "medium close-up", "CAT holds up two flippers while ROSIE marks her little picture list",
              ["CAT", "ROSIE"], "cheeky and pleased", "tilts down", "a tiny pencil scratch and a grumbly huff"),
         ]},
        {"title": "Lights on", "place": "hall", "time": "night",
         "angle": "Wide firelit view at night beside the Door Wall in",
         "who": f"{TREE} stands in its big red clay pot wrapped in tiny golden fairy lights, sugar snow, popcorn "
                f"string and pinecone ornaments all sparkling, a red ribbon bow on one branch; {ROSIE_CUP} stands "
                "in front of it holding her little picture list in front of her cup, straw tall, golden light "
                "on her lid; BJORN kneels by the wall holding the plug of the fairy lights in one big paw",
         "beats": [
             ("Back at the lodge, Bjorn plugged in the fairy lights. Click! The little tree lit up gold.",
              "wide shot", "BJORN pushes in the plug and the fairy lights blink on along the branches", "BJORN",
              "careful and proud", "pushes in", "a soft click and a low crackling fire"),
             ("It sparkled from its red pot to its bent top. Wonky. Sugary. Theirs.",
              "medium shot", "ROSIE looks up the glowing tree and her straw wiggles", "ROSIE",
              "dazzled and proud", "tilts up", "a low crackling fire"),
         ]},
        {"title": "A very tuneful cough", "place": "hall", "time": "night",
         "angle": "Warm medium view at night across the crackling fireplace in",
         "who": "BJORN sings with his head thrown back and one big paw on his chest; KYLE and LINA sway beside "
                "him, KYLE holding a mug of cocoa in both paws; MAGNUS sits in the corner armchair with his arms "
                "folded and his mouth just barely open, eyes sliding away",
         "beats": [
             ("Everybody sang carols. Bjorn sang loudest. It sounded like a tuba falling downstairs.",
              "medium shot", "BJORN sways with his head thrown back and his paw on his chest while KYLE and LINA rock along",
              ["BJORN", "KYLE", "LINA"], "joyful and very loud", "pans right", "a crackling fire and a creak of floorboards"),
             ("Even Magnus hummed. \"That was a cough,\" said Magnus. It was a very tuneful cough.",
              "medium close-up", "MAGNUS snaps his mouth shut and folds his arms tighter", "MAGNUS",
              "caught and gruff", "pushes in", "a creak of an armchair and a crackling fire"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep on a soft pillow at the foot of the bunk with a pine "
                "needle on her beak, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, who stopped at the small one. Goodnight, wonky tree, with sugar snow on "
              "every branch.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Magnus, noble twice this week. May your dreams smell of pine and popcorn.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, who stopped at the small one.",
        "Goodnight, wonky tree, with sugar snow on every branch.",
        "Goodnight, Magnus, noble twice this week.",
        "May your dreams smell of pine and popcorn.",
    ],
}
