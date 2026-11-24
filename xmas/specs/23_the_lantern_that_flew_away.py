"""23 — The Lantern That Flew Away (Wednesday, December 23)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

LANE_BELOW = ("snowy wooden stalls with striped awnings, a long string of paper lanterns with one empty brass "
              "hook, crooked chimney pots on snowy roofs above, striped windsocks streaming sideways, a brass fish "
              "weathervane spinning on a pole, footprints in the snow")
TREE = ("a small crooked pine tree with a bent top standing in a red pot at the end of the lane, hung with paper "
        "snowflakes, red ribbons and gingerbread shapes, snowy stall roofs with crooked chimney pots, striped "
        "windsocks, a long string of paper lanterns, footprints in the snow")

STORY = {
    "num": "23",
    "slug": "the-lantern-that-flew-away",
    "title": "The Lantern That Flew Away",
    "meta": [
        ("Day", "Wednesday, December 23 · door twenty-three"),
        ("Holiday thread", "The night before the big night: one day to go"),
        ("Guests", "Piper Paddlefoot ❄️, Willa Wobble ❄️, Whistlewick the arctic fox ❄️, Bjorn Bigpaws ❄️, "
                   "Kyle the black bear cub"),
        ("Cat’s role", "wind reader (she knows how the Windy Pass wind turns, and where it will set things down)"),
        ("Mandarin", "風 wind · 幫忙 help · 一起 together"),
        ("Setting", "The Door Wall in the lodge great hall, then the snowy rooftops of Lantern Lane below Windy "
                    "Pass, the wonky tree from Day 3 at the end of the lane, the lane at night, and the bunk room"),
    ],
    "palette": "snowy white and windy sky blue with saturated chimney red and lantern gold accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "PIPER", "WILLA", "WHISTLEWICK", "BJORN", "KYLE"],
    "cast_note": "Humans in this story: none. The lost lantern is sky blue. The wonky tree from Day 3 stands "
                 "decorated in a red pot at the end of Lantern Lane; its bent top is the hook. SpicySquid is "
                 "heard but never drawn in this story.",
    "key_shot": 14,
    "places": {
        "doorwall": DOORWALL,
        "roofs": {
            "name": "the snowy rooftops of Lantern Lane below Windy Pass",
            "scene": "the rooftops of Lantern Lane",
            "props": "snowy shingled stall roofs with crooked chimney pots, a rope-and-plank roof bridge, a brass "
                     "fish weathervane spinning on a pole, striped windsocks streaming sideways, a narrow snowy "
                     "ledge along a tall brick chimney, the long string of paper lanterns swinging below",
            "light": "Bright blowy winter daylight shines under fast white clouds",
            "accents": "sky blue and chimney red",
            "atmo": "Gusts whirl loose snow off the roof edges",
            "motion": "gusts whirl loose snow off the roof edges",
        },
        "lane_night": LANE_NIGHT,
        "bunk": bunk("a tiny paper kite and a short loop of red rope on the nightstand"),
    },
    "shots": [
        {"title": "Door twenty-three", "place": "doorwall",
         "angle": "Close view at knob height along the rows of little carved doors in",
         "who": "CAT the little blue penguin stands on a wooden step stool holding up a tiny paper kite with a "
                f"ribbon tail from one open little door, her beak lifted to sniff the air; {ROSIE_CUP} stands "
                "beside the stool holding a little picture list in front of her cup, the list showing a plain "
                "doodle of a lantern with a tick beside it, straw perked up",
         "beats": [
             ("Door twenty-three belonged to Cat the penguin. Inside sat a tiny paper kite with a ribbon tail.",
              "close-up", "CAT lifts the tiny paper kite out of the little door by its tail", "CAT",
              "curious and pleased", "pushes in", "a tiny door creak and a paper flutter"),
             ("Cat sniffed the air. \"Kite weather. The **風** (fēng) = wind is coming down from Windy "
              "Pass.\"",
              "medium close-up", "CAT lifts her beak and sniffs, and her yellow scarf twitches", "CAT",
              "alert and knowing", "tilts up", "a low whistle of wind in the chimney"),
             ("\"One day to go,\" said Rosie. Her list said: lantern twenty-three, hung up early. Tick.",
              "medium shot", "ROSIE holds her list up in front of her cup and her straw wiggles", "ROSIE",
              "organized and proud", "holds still", "a paper rustle and a crackling fire"),
         ]},
        {"title": "Whoosh", "place": "roofs",
         "angle": "Low angle from the snowy lane looking up past the awnings at",
         "props": LANE_BELOW,
         "who": f"{ROSIE_CUP} stands in the snow looking straight up with her straw blown sideways; high above "
                "her a sky-blue paper lantern sails over the awnings on the wind like a kite, its string trailing",
         "beats": [
             ("The lantern was sky blue. It already hung on its hook, waiting for dark.",
              "medium shot", "ROSIE looks up proudly as the wind tugs her straw sideways", "ROSIE",
              "proud, then uneasy", "tilts up", "paper lanterns rattling in a rising wind"),
             ("Then WHOOSH. A gust lifted it right off. Up it went, like a kite with nobody holding.",
              "wide shot", "ROSIE gasps as the sky-blue lantern sails up over the awnings", "ROSIE",
              "shocked and helpless", "tilts up", "a big gust and a flapping awning"),
             ("Over the awnings. Over the chimneys. Gone.",
              "wide shot", "the sky-blue lantern shrinks to a dot above the chimney pots", [],
              "windy and empty", "pans right", "a fading gust and a creaking weathervane"),
         ]},
        {"title": "Twenty-two lanterns", "place": "roofs",
         "angle": "Close view at snow level beside one empty brass hook swinging under",
         "props": LANE_BELOW,
         "who": f"{ROSIE_CUP} stands under an empty brass hook with her straw drooped flat and her little picture "
                "list hanging at her side, eyes wide",
         "beats": [
             ("Rosie's straw drooped flat. \"Twenty-four hooks. Twenty-two lanterns. The surprise is ruined!\"",
              "medium close-up", "ROSIE's straw droops flat as she stares at the empty hook", "ROSIE",
              "dismayed and panicky", "pushes in", "an empty hook squeaking in the wind"),
         ]},
        {"title": "Call them", "place": "roofs",
         "angle": "Medium view under a flapping striped awning below",
         "props": LANE_BELOW,
         "who": f"MOM bends down with both tiny arms cupped around her mouth like a megaphone, eyes twinkling; TORI stands on the other side of ROSIE "
                f"with her green straw bent by the wind and a steady smile; {ROSIE_CUP} stands between them "
                "looking up",
         "beats": [
             ("\"Then we call for **幫忙** (bāngmáng) = help,\" said Mom. \"Loudly.\"",
              "medium shot", "MOM bends down beside ROSIE and cups both tiny arms around her mouth", ["MOM", "ROSIE"],
              "calm and playful", "pushes in", "a flapping awning"),
             ("\"This valley loves a rescue,\" said Tori. \"You've got this, little sip.\"",
              "medium close-up", "TORI leans close to ROSIE and tips her straw toward the rooftops", ["TORI", "ROSIE"],
              "sure and encouraging", "tilts up", "a flapping awning and a gust"),
         ]},
        {"title": "Help, please!", "place": "roofs",
         "angle": "Wide view down the windy lane toward a gathering rescue team below",
         "props": LANE_BELOW,
         "who": f"{ROSIE_CUP} stands on an upturned crate with her straw straight up; WHISTLEWICK stands in front "
                "of her with ears pricked and the brass whistle in a grin; PIPER skids in on her glittery blue "
                "snowboard; WILLA peeks from behind PIPER; BJORN strides up on his forest-green skis; KYLE "
                "trots behind with a big pretzel in one paw and a coil of red rope over his shoulder",
         "beats": [
             ("\"Help, please!\" called Rosie. One sharp whistle answered. Fweeet! Whistlewick the arctic fox was "
              "already there.",
              "medium shot", "WHISTLEWICK blows one sharp note on the brass whistle and ROSIE's straw springs up",
              ["WHISTLEWICK", "ROSIE"], "quick and ready", "pushes in", "one sharp whistle"),
             ("Then Piper. Then tiny Willa. Then Bjorn the polar bear. Then Kyle the bear cub, mid-pretzel.",
              "wide shot", "PIPER, WILLA, BJORN and KYLE squeeze in close, and KYLE takes a bite of his pretzel",
              ["PIPER", "WILLA", "BJORN", "KYLE"], "eager and willing", "pans left", "a snowboard skid and a crunch"),
             ("Whistlewick sniffed the wind. Ears up. Nose out. One paw pointed over the rooftops.",
              "medium close-up", "WHISTLEWICK sniffs, then lifts one front paw to point up at the roofs",
              "WHISTLEWICK", "sharp and certain", "tilts up", "quick sniffs and a gust"),
         ]},
        {"title": "Bjorn was the ladder", "place": "roofs",
         "angle": "Low angle from the snowy lane up the side of a stall toward",
         "who": "BJORN stands braced against the stall wall with both big paws on the roof edge, patient and "
                "noble; PIPER climbs over his shoulder onto the roof; WILLA sits on top of his head holding one "
                "of his ears, wide-eyed",
         "beats": [
             ("Bjorn was the ladder. Up his back they climbed, onto the snowy roofs.",
              "medium shot", "PIPER steps from the shoulder of BJORN onto the roof while WILLA clings to his ear",
              ["PIPER", "BJORN", "WILLA"], "brave and wobbly", "tilts up", "scrabbling feet and a creak of shingles"),
         ]},
        {"title": "Descended with style", "place": "roofs",
         "angle": "High angle from the roof edge looking down at a deep snowbank beside",
         "who": "BJORN sits buried to his chin in a deep snowbank with his forest-green skis sticking straight up "
                "and a perfectly dignified face, a small heap of roof snow on his head",
         "beats": [
             ("Then Bjorn climbed up too. The roof thought about it. FWUMP. Bjorn was in a snowbank.",
              "wide shot", "BJORN blinks in the snowbank as loose snow slides off the roof onto his head", "BJORN",
              "surprised and dignified", "tilts down", "a long slide and a deep soft fwump"),
             ("\"I did not fall,\" said the snowbank. \"I descended with style.\"",
              "medium close-up", "BJORN lifts his chin out of the snow and straightens his scarf", "BJORN",
              "noble and unbothered", "holds still", "a soft sprinkle of snow"),
         ]},
        {"title": "This way!", "place": "roofs",
         "angle": "Dynamic view along the snowy roof ridge of",
         "who": "WHISTLEWICK races along the roof ridge with a big fluffy tail streaming like a flag, nose pointed "
                f"ahead; {ROSIE_CUP} stands on the rope-and-plank roof bridge behind, pointing one tiny arm at a "
                "small flash of sky blue bobbing above the next roof",
         "beats": [
             ("Whistlewick ran ahead along the roofs, tail like a flag. Fweeet! That meant: this way!",
              "wide shot", "WHISTLEWICK stretches out long and low on the roof ridge with tail streaming in the wind", "WHISTLEWICK",
              "swift and sure", "tracks beside", "quick paws on snow and one sharp whistle"),
             ("There! A flash of sky blue, bobbing over the next roof. Then the wind took it again.",
              "medium shot", "ROSIE points one tiny arm at the flash of blue and her straw leans in the wind",
              "ROSIE", "hopeful, then dismayed", "pans right", "a gust and a far paper flutter"),
         ]},
        {"title": "The anchor", "place": "roofs",
         "angle": "Wide side view across a gap between two snowy roofs on",
         "who": "PIPER flies through the air over the gap on her glittery blue snowboard with a red rope trailing "
                "from one flipper, flippers wide; KYLE sits firmly on the other end of the rope on the near roof "
                "with a pretzel in his paw, calm and solid",
         "beats": [
             ("There was a gap between the roofs. \"Slide into it!\" Piper leaped across with the rope.",
              "wide shot", "PIPER sails over the gap on her snowboard with the red rope streaming behind", "PIPER",
              "fearless and thrilled", "pans right", "a long swoosh and a snap of rope"),
             ("Kyle sat on the other end. \"I'm the anchor. Anchors don't move. Anchors may snack.\"",
              "medium close-up", "KYLE settles more firmly on the rope end and takes a bite of pretzel", "KYLE",
              "solid and content", "pushes in", "a rope creak and a crunch"),
         ]},
        {"title": "Cable car", "place": "roofs",
         "angle": "Low angle from the gap between two snowy roofs looking up at a red rope stretched across",
         "who": "CAT the little blue penguin slides along the red rope hanging by both flippers, scarf looped "
                f"below her like a hammock; {ROSIE_CUP} sits snug in the loop of the yellow scarf like a tiny "
                "cable car, straw blown back, eyes wide and thrilled",
         "beats": [
             ("One by one they crossed the rope. Rosie rode across in Cat's scarf, like a cable car.",
              "wide shot", "CAT slides along the rope with ROSIE swinging gently in the loop of her scarf",
              ["CAT", "ROSIE"], "thrilled and giggly", "tracks beside", "a rope hum and a rush of wind"),
         ]},
        {"title": "Round and round", "place": "roofs",
         "angle": "Dynamic low angle looking up the pole of the spinning brass fish weathervane on",
         "who": "a sky-blue paper lantern is caught on the tail of the brass fish weathervane, whirling around "
                "with it; CAT the little blue penguin hangs in the air in the middle of a jump just below it, "
                "both flippers stretched up, beak open",
         "beats": [
             ("The lantern snagged on the fish weathervane. Round and round it spun. Cat jumped. Missed. Off it flew.",
              "medium shot", "CAT jumps with both flippers stretched up at the whirling lantern", "CAT",
              "determined and dizzy", "tilts up", "a squeaking weathervane and a paper flutter"),
         ]},
        {"title": "Wind reader", "place": "roofs",
         "angle": "Low angle looking up past the spinning brass fish weathervane on",
         "who": "CAT the little blue penguin stands beside the weathervane pole holding one wet flipper up in the "
                "wind, scarf streaming, eyes narrowed like a sea captain",
         "beats": [
             ("Cat licked a flipper and held it up. \"The pass wind always curls back down the lane.\"",
              "medium shot", "CAT holds one flipper high in the wind and her scarf streams sideways", "CAT",
              "expert and serious", "tilts up", "a creaking weathervane and a steady gust"),
             ("\"It turns like a snowboarder. Follow the turn! Also, somebody is making pancakes.\"",
              "medium close-up", "CAT sweeps her flipper in a curve, then sniffs the air happily", "CAT",
              "confident and hungry", "pans left", "a gust and two quick sniffs"),
         ]},
        {"title": "Over the Squid Grill", "place": "roofs",
         "angle": "High angle from a steaming chimney pot down to the snowy lane below",
         "who": f"{ROSIE_CUP} stands on tiptoe on the rope-and-plank roof bridge beside a chimney pot with curls of "
                "grill steam rising from it, one tiny arm over her lid; CAT the little blue penguin crouches beside her with one flipper pinching the tip of the striped straw; far below on the lane MOM and TORI hold a "
                "plaid blanket stretched wide between them, looking up",
         "beats": [
             ("They tiptoed over the Squid Grill roof. Below, SpicySquid hummed and flipped corn. He never "
              "looked up.",
              "medium shot", "ROSIE rises onto tiptoe beside the steaming chimney pot and holds very still", "ROSIE",
              "careful and giggly", "tracks beside", "a muffled sizzle and a soft creak of planks"),
             ("The spicy steam tickled Rosie's straw. Ah. Ah. Cat pinched it shut. Phew.",
              "medium close-up", "CAT pinches the tip of the straw and ROSIE holds very still with round eyes",
              ["CAT", "ROSIE"], "tickled and breathless", "pushes in", "a muffled sizzle and a tiny squeak"),
             ("Down on the lane, Mom and Tori ran along underneath with a blanket. Just in case.",
              "wide shot", "MOM and TORI stretch the plaid blanket wide and look up", ["MOM", "TORI"],
              "watchful and ready", "tilts down", "a blanket flap and quick steps in snow"),
         ]},
        {"title": "The narrowest ledge", "place": "roofs",
         "angle": "Dramatic close view along a narrow snowy ledge beside a tall brick chimney on",
         "who": "WILLA stands on the narrow ledge with her back against the chimney bricks and one tiny foot "
                "sliding forward, purple earmuffs fluffy, eyes brave and round; PIPER stands at the start of the "
                "ledge holding the red rope tied around WILLA's middle, watching closely",
         "beats": [
             ("The last roof had a tall chimney. The only way around was a ledge thin as a ruler.",
              "wide shot", "PIPER measures the ledge with one big foot and shakes her head", "PIPER",
              "stumped and worried", "pans right", "a gust around the chimney"),
             ("Too thin for Piper. Too thin for a cup. Just right for the tiniest penguin in the valley.",
              "medium shot", "WILLA steps onto the ledge and presses her back to the bricks", "WILLA",
              "nervous and determined", "pushes in", "a tiny scrape of feet on snow"),
             ("\"The smallest step is still a step,\" whispered Willa. Step. Step. Step. She peeked around the "
              "chimney.",
              "close-up", "WILLA slides one tiny foot forward and leans to peek past the bricks", "WILLA",
              "brave and careful", "tracks beside", "tiny careful steps and a rope creak"),
         ]},
        {"title": "I see it!", "place": "roofs",
         "angle": "Close view past the corner of the tall brick chimney on",
         "who": "WILLA leans around the chimney corner with one tiny flipper pointing down and away, beak wide "
                "open in a joyful squeak, earmuffs blown back by the wind",
         "beats": [
             ("\"I see it!\" squeaked Willa. \"It's in a tree! A funny little bendy tree!\"",
              "close-up", "WILLA points one tiny flipper down and bounces on the ledge", "WILLA",
              "thrilled and proud", "pushes in", "a happy squeak and a gust"),
         ]},
        {"title": "The wonky tree", "place": "roofs",
         "angle": "Wide view from the last roof down to a small crooked decorated pine tree at the end of the lane "
                  "below",
         "props": TREE,
         "who": "a sky-blue paper lantern hangs caught on the bent top of the little crooked pine tree, a little "
                f"crumpled, swinging gently; {ROSIE_CUP} stands in the snow at the foot of the tree looking up "
                "with her straw high; CAT the little blue penguin stands beside her with both flippers thrown up",
         "beats": [
             ("It was the wonky tree in its red pot, set out on the lane for tomorrow's party.",
              "wide shot", "CAT throws both flippers up and hops in the snow", "CAT",
              "amazed and gleeful", "tilts down", "a soft jingle of ornaments in the wind"),
             ("Its bent top had caught the lantern by the string.",
              "medium shot", "the sky-blue lantern swings gently on the bent treetop", [],
              "snug and safe", "tilts up", "a paper flutter and a soft jingle of ornaments"),
             ("\"I told you,\" said Rosie. \"That bent top is the perfect hook.\"",
              "medium close-up", "ROSIE looks up at the treetop and gives one proud little bounce", "ROSIE",
              "proud and relieved", "pushes in", "a soft jingle of ornaments"),
         ]},
        {"title": "Thank you, tree", "place": "roofs",
         "angle": "Low angle looking up past red ribbons and paper snowflakes at the bent treetop below",
         "props": TREE,
         "who": f"BJORN stands beside the little crooked pine tree holding one big paw up flat like a tray; "
                f"{ROSIE_CUP} stands on his raised paw holding the sky-blue paper lantern in front of her cup, a "
                "little crumpled, straw wiggling; TORI stands below with her tiny arms up ready to help",
         "beats": [
             ("Bjorn lifted Rosie up on one big paw. She unhooked it gently. \"Thank you, tree.\"",
              "medium shot", "BJORN raises his flat paw slowly and ROSIE holds the lantern in front of her cup",
              ["BJORN", "ROSIE"], "careful and grateful", "tilts up", "a soft jingle of ornaments"),
             ("The lantern was a little crumpled. \"It's had an adventure,\" said Tori. \"So have we.\"",
              "medium close-up", "TORI reaches up and smooths one crumpled corner of the lantern", "TORI",
              "fond and amused", "pushes in", "a soft paper crinkle"),
             ("Rosie thanked everybody. By name. From a list. It was a long list. Nobody minded.",
              "medium shot", "ROSIE bobs a little bow on the paw of BJORN and her straw wiggles", ["ROSIE", "BJORN"],
              "thankful and glowing", "pulls back", "a paper rustle and a happy rumble"),
         ]},
        {"title": "Double knot", "place": "lane_night", "time": "night",
         "angle": "Upward view at the long lantern string above",
         "who": "MOM holds a long thin lighting taper up to a sky-blue paper lantern, a little crumpled, tied to "
                f"its hook with a big bow of red rope; {ROSIE_CUP} stands on a snowy crate beside her with her "
                "straw high; KYLE sits in the snow right underneath the lantern with his arms folded, very solid",
         "beats": [
             ("That night they hung it again. Double knot. Triple knot. Then Mom lit it.",
              "medium shot", "MOM lifts her taper and the crumpled blue lantern begins to glow", "MOM",
              "calm and careful", "tilts up", "a tiny flicker and a soft paper rustle"),
             ("\"One more light,\" said everybody, **一起** (yìqǐ) = together.",
              "medium close-up", "ROSIE gives one small proud bounce on her crate", "ROSIE",
              "glad and proud", "pushes in", "a soft hush of falling snow"),
             ("Kyle sat down right under it. \"Anchor,\" he explained. One hook left. One day to go.",
              "medium shot", "KYLE folds his arms and settles deeper into the snow under the lantern", "KYLE",
              "solid and devoted", "pulls back", "a soft crunch of snow and a far sizzle"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably closed; "
                "CAT the little blue penguin asleep curled on a soft pillow at the foot of the bunk, yellow scarf "
                "visible",
         "beats": [
             ("Goodnight, little sip, your lantern is home. Goodnight, wonky tree, good catch.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, wind, you rascal, rest. May everything you lose blow back to you.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, your lantern is home.",
        "Goodnight, wonky tree, good catch.",
        "Goodnight, wind, you rascal, rest.",
        "May everything you lose blow back to you.",
    ],
}
