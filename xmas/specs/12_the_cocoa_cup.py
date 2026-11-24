"""12 — The Cocoa Cup (Saturday, December 12 · Market Train to Quebec City)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"

STORY = {
    "num": "12",
    "slug": "the-cocoa-cup",
    "title": "The Cocoa Cup",
    "meta": [
        ("Day", "Saturday, December 12 · door twelve · Market Train day trip to Quebec City"),
        ("Holiday thread", "The big toboggan race on the old wooden slide in Old Quebec"),
        ("Guests", "Aurora Frostholm ❄️ (last one down buys cocoa), Harfang the snowy owl ⚜️ (new; the race "
                   "starter), Margot the maple taffy ⚜️ (new; her stand is at the bottom), Gabby the black "
                   "star shark, Kyle the black bear cub"),
        ("Cat’s role", "opens the door, shares Rosie's toboggan, and discovers that penguin tummies have no "
                       "brakes"),
        ("French", "tuque, a knit winter hat · c'est le fun, this is fun"),
        ("Mandarin", "加油 go, go, go · 一起 together"),
        ("Setting", "The Door Wall, the old wooden toboggan slide on Dufferin Terrace in Old Quebec City, "
                    "Lantern Lane at night, and the bunk room"),
    ],
    "palette": "snowy white and icy blue with saturated maple amber and copper green accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "AURORA", "HARFANG", "MARGOT", "GABBY", "KYLE"],
    "cast_note": "Humans in this story: none. Gabby swims through the powder snow as if it were water. The "
                 "maple taffy pops Margot rolls are plain golden taffy on sticks, with no faces. Tickets and "
                 "stalls show plain pictures only.",
    "key_shot": 14,
    "places": {
        "door": DOORWALL,
        "slide": {
            "name": "the old wooden toboggan slide on Dufferin Terrace in Old Quebec City",
            "scene": "the Dufferin Terrace toboggan slide",
            "props": "three icy lanes running down a long wooden ramp, empty wooden toboggans with curled "
                     "fronts waiting in a row, the great copper-roofed castle hotel towering behind, the frozen St. Lawrence "
                     "River far below, a maple taffy stand with a trough of clean snow, green iron lampposts "
                     "along the snowy boardwalk",
            "light": "Bright cold sunshine flashes on the icy lanes",
            "accents": "maple amber and copper green",
            "atmo": "Sparkling ice dust hangs in the air above the ramp",
            "motion": "sparkling ice dust hangs in the air above the ramp",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny tin trophy cup and a red knitted tuque on the nightstand"),
    },
    "shots": [
        {"title": "Door twelve", "place": "door",
         "angle": "Low angle from the woven rug up at one open little door in",
         "who": "CAT the little blue penguin stands on tiptoe on a wooden footstool holding up a tiny golden "
                "train ticket with a tiny tin trophy cup tied to it by a red thread, beak wide open with joy; "
                f"{ROSIE_CUP} stands on the rug below with her straw wiggling",
         "beats": [
             ("Cat the penguin opened door twelve. Out slid a golden train ticket with a tin cup tied on.",
              "medium shot", "CAT lifts the golden ticket high and the tiny tin cup swings on its thread", "CAT",
              "astonished and thrilled", "pushes in", "a tiny door creak and a tinny little clink"),
             ("\"The Cocoa Cup!\" squeaked Cat. \"The great toboggan race! In Quebec City! Today!\"",
              "medium close-up", "CAT bounces on the footstool while ROSIE's straw wiggles below",
              ["CAT", "ROSIE"], "beside herself", "pulls back", "squeaky penguin bounces"),
         ]},
        {"title": "Packing", "place": "door",
         "angle": "Medium view beside the antler coat rack in",
         "who": "KYLE stuffs a paper bag of snacks into a little knapsack with a serious face; GABBY floats "
                f"beside him looping her striped scarf with one fin, calm; {ROSIE_CUP} holds a little picture "
                "list in front of her cup, the list showing three plain doodles that are all the same pair of "
                "gripping mittens, very earnest",
         "beats": [
             ("Kyle the bear cub packed snacks. Gabby the black star shark packed a scarf. Rosie "
              "packed a list.",
              "medium shot", "KYLE pushes the snack bag into his knapsack while GABBY loops her scarf",
              ["KYLE", "GABBY"], "busy and eager", "pans right", "a paper bag crinkle and a crackling fire"),
             ("The list said: One, hold on. Two, hold on. Three, hold on.",
              "medium close-up", "ROSIE holds her little picture list up high in front of her cup", "ROSIE",
              "earnest", "pushes in", "a paper rustle"),
         ]},
        {"title": "A city with a castle on top", "place": "slide",
         "angle": "Wide establishing view from the snowy boardwalk up the whole length of",
         "who": f"{ROSIE_CUP} stands tiny on the snowy boardwalk gazing up the long ramp with her straw straight "
                "up; CAT the little blue penguin bounces beside her pointing a flipper at the top; MOM stands "
                "behind them with a calm smile, the great castle hotel towering over everything",
         "beats": [
             ("The Market Train followed the frozen river to a city with a castle on top.",
              "wide shot", "CAT bounces and points up at the castle roofs", "CAT", "proud and excited",
              "tilts up", "soft crunching snow and a faraway train whistle"),
             ("Below the castle ran the old toboggan slide. Three icy lanes, straight down.",
              "wide shot", "ROSIE looks all the way up the ramp and her straw tips back", "ROSIE",
              "awed and a bit wobbly", "tilts up", "a distant rumble of wood on ice"),
         ]},
        {"title": "Hoo-là-là", "place": "slide",
         "angle": "Low angle from toboggan height up at a wooden post at the top of",
         "who": "HARFANG stands on a wooden post with his red woven sash bright against his white feathers, "
                "calm and dignified, holding out a small heap of knitted tuques in one wing; "
                f"{ROSIE_CUP} stands below wearing a red tuque pulled down over her dome lid with her straw "
                "poking through the top; KYLE wears two tuques stacked on his head, pleased; TORI leans far "
                "back to look up at the owl",
         "beats": [
             ("At the top stood Harfang, a big snowy owl in a red sash. \"Hoo-là-là. Racers.\"",
              "medium shot", "HARFANG looks slowly down at the racers and ruffles his feathers", "HARFANG",
              "calm and dignified", "tilts up", "a soft feathery ruffle and wind"),
             ("He handed everyone a **tuque** (TOOK) = knit winter hat. Rosie's covered her lid. Kyle wore "
              "two.",
              "medium close-up", "ROSIE tugs her tuque straight while KYLE pats his two hats",
              ["ROSIE", "KYLE"], "snug and pleased", "pans right", "woolly rustles"),
             ("Then he turned his head all the way around to count them. Twice.",
              "medium shot", "HARFANG slowly turns his head far to one side as TORI leans back to watch",
              ["HARFANG", "TORI"], "solemn and thorough", "holds still", "a slow feathery creak"),
         ]},
        {"title": "Last one down", "place": "slide",
         "angle": "Medium view along the top of the three icy lanes of",
         "who": "AURORA bounces at the back of a long wooden toboggan with her pink-and-green scarf flying, "
                "sparkling with mischief; KYLE sits at the front gripping the curled wooden nose with both "
                "paws; TORI sits in the middle with her green straw tall",
         "beats": [
             ("Aurora Frostholm, the polar bear, bounced on her toes. \"Last one down buys cocoa!\"",
              "medium shot", "AURORA bounces behind the toboggan and punches one paw in the air", "AURORA",
              "sparkling with mischief", "pushes in", "bouncing paws on packed snow"),
             ("Lane one: Aurora, Kyle and Tori on one long toboggan. Kyle was the engine.",
              "medium shot", "KYLE grips the curled nose and leans forward while TORI holds on behind him",
              ["KYLE", "TORI"], "ready and serious", "pans left", "a creak of old wood"),
         ]},
        {"title": "Lanes two and three", "place": "slide",
         "angle": "Close view from the curled nose of a toboggan at the top of",
         "who": f"{ROSIE_CUP} sits at the front of a long wooden toboggan holding the rope tight in front of her "
                "cup, red tuque over her lid, eyes huge; CAT the little blue penguin sits behind her with her "
                "flippers up, ready; GABBY floats low over the snowy lane beside them with her striped scarf "
                "fluttering and one fin raised in a small wave, relaxed",
         "beats": [
             ("Lane two: Rosie and Cat. \"You've got this, little sip!\" called Tori. Rosie held on. See list.",
              "medium close-up", "ROSIE grips the rope tighter in front of her cup while CAT wiggles into place",
              ["ROSIE", "CAT"], "nervous and thrilled", "pushes in", "a rope creak and a held breath"),
             ("Lane three: Gabby. No toboggan. \"I'll swim,\" she said. \"Don't worry. I only bite pie.\"",
              "medium shot", "GABBY gives a small wave of one fin and dips her nose toward the snow", "GABBY",
              "relaxed and dry", "pans right", "a soft swish in powder snow"),
         ]},
        {"title": "One slow blink", "place": "slide",
         "angle": "Tight close-up on two round golden eyes at the top of",
         "who": "HARFANG holds one white wing raised high, his round golden eyes half closed in one slow solemn "
                "blink",
         "beats": [
             ("Harfang lifted one wing. Everybody held their breath. Harfang blinked. One slow blink.",
              "close-up", "HARFANG closes his golden eyes slowly and opens them again", "HARFANG",
              "solemn", "holds still", "wind and one tiny creak of ice"),
             ("\"That was the start,\" said Harfang. \"You may go.\"",
              "medium close-up", "HARFANG lowers his wing and tilts his head", "HARFANG",
              "mildly surprised at everyone", "pulls back", "a soft feathery ruffle"),
         ]},
        {"title": "Whoosh", "place": "slide",
         "angle": "Dynamic low angle racing down the icy lanes of",
         "who": f"{ROSIE_CUP} sits at the front of a speeding toboggan, lid and straw visible, with her tuque streaming back like a flag "
                "and her straw bent by the wind, eyes shining; CAT the little blue penguin whoops behind her "
                "with both flippers up; AURORA, KYLE and TORI streak past in the next lane, AURORA with one "
                "paw in the air and KYLE with his mouth wide open",
         "beats": [
             ("WHOOSH! Down they flew. The castle blurred. The river blurred. Rosie's tuque flapped like a "
              "flag.",
              "wide shot", "ROSIE leans into the wind as CAT throws both flippers up behind her",
              ["ROSIE", "CAT"], "thrilled", "tracks beside", "a roaring rumble of wood on ice"),
             ("\"**C'est le fun** (say luh FUN) = this is fun!\" yelled Aurora. \"Is there cocoa?\" yelled Kyle.",
              "medium shot", "AURORA whoops with one paw in the air while KYLE's ears flap in the wind",
              ["AURORA", "KYLE"], "wild and hungry", "pans left", "a rumble of wood on ice and wind"),
         ]},
        {"title": "Winning by a mile", "place": "slide",
         "angle": "High angle looking down the third lane of",
         "who": "GABBY swims through the powder snow far ahead with her back fin cutting a neat furrow and her "
                "striped scarf streaming behind her, smiling; MOM stands tiny at the bottom of the ramp beside "
                "a finish ribbon waving both tiny arms",
         "beats": [
             ("Nobody was faster than Gabby. She swam through the snow, winning by a mile.",
              "wide shot", "GABBY swims down the lane and powder snow curls off her fin", "GABBY",
              "easy and joyful", "tracks beside", "a long smooth swish through powder"),
             ("\"**加油** (jiāyóu) = go, go, go!\" called Mom from the bottom, waving both arms.",
              "medium shot", "MOM waves both tiny arms beside the finish ribbon", "MOM",
              "proud and excited", "pushes in", "a faraway cowbell on the wind"),
         ]},
        {"title": "The halfway bump", "place": "slide",
         "angle": "Side view at the big snowy halfway bump of",
         "who": "a long wooden toboggan tips up on its side at the top of the bump; "
                f"{ROSIE_CUP} sails off it in a soft low arc toward a deep fluffy snowbank with her tuque "
                "flying and her eyes round; CAT the little blue penguin slides off the other side on her tummy "
                "with her flippers out",
         "beats": [
             ("Then came the halfway bump. Lane two went up. Lane two came down. Lane two went sideways.",
              "medium shot", "ROSIE lifts off the tipping toboggan with her eyes round", "ROSIE",
              "surprised", "pans right", "a wooden thump and a scrape"),
             ("Poomf! Rosie landed in a snowbank. Only her straw stuck out, like a striped flagpole.",
              "medium shot", "ROSIE drops softly into the fluffy snowbank and a puff of powder rises", "ROSIE",
              "astonished and unhurt", "pushes in", "a soft deep poomf"),
         ]},
        {"title": "No brakes", "place": "slide",
         "angle": "Wide view down the empty middle lane of",
         "who": f"{ROSIE_CUP} sits buried up to her lid in a deep fluffy snowbank with only her straw and the "
                "tip of her red tuque showing, beside an upturned wooden toboggan; CAT the little blue penguin "
                "slides away down the icy lane on her tummy looking back over her shoulder with a helpless "
                "grin",
         "beats": [
             ("Cat kept going on her tummy. \"Penguin tummies have no brakes!\" she called. \"Back soon! "
              "Probably!\"",
              "wide shot", "CAT slides away down the lane on her tummy and waves one flipper back", "CAT",
              "helpless and cheerful", "tracks beside", "a long tummy swish on ice"),
             ("Rosie's straw looked left. It looked right. The hill was very big.",
              "medium close-up", "ROSIE's straw swivels left, then right, above the snow", "ROSIE",
              "stuck and thoughtful", "holds still", "wind and a tiny squeak of snow"),
         ]},
        {"title": "A whisker from the finish", "place": "slide",
         "angle": "Low angle from the finish ribbon back up the long ramp of",
         "who": "GABBY hovers a whisker from the finish ribbon looking back over her fin up the hill, her smile "
                "turning thoughtful; MOM stands beside the ribbon looking up the hill too with one tiny arm "
                "shading her eyes",
         "beats": [
             ("Far ahead, Gabby looked back. One small straw in the snow. She stopped, a whisker from the "
              "finish.",
              "medium shot", "GABBY stops just short of the ribbon and looks back up the hill", "GABBY",
              "thoughtful", "tilts up", "a soft swish stopping short"),
             ("Then she turned around and swam straight back up the hill.",
              "wide shot", "GABBY turns her nose uphill while MOM watches with a soft smile", ["GABBY", "MOM"],
              "certain", "tilts up", "a steady swish through powder"),
         ]},
        {"title": "Going down?", "place": "slide",
         "angle": "Close view at the snowbank beside the halfway bump of",
         "who": f"GABBY lifts ROSIE gently out of the snow on the tip of her round nose; {ROSIE_CUP} sits on the "
                "nose of GABBY with a little cap of snow on top of her straw and her tuque crooked, beaming",
         "beats": [
             ("She scooped Rosie out with her nose, softer than a kiss. \"Going down?\" asked Gabby.",
              "close-up", "GABBY lifts ROSIE gently up out of the snowbank on her nose", ["GABBY", "ROSIE"],
              "gentle and funny", "pushes in", "a soft crunch of snow"),
             ("\"**一起** (yìqǐ) = together,\" said Rosie. Her straw popped up, with snow on top.",
              "medium close-up", "ROSIE's straw springs up with its little cap of snow", "ROSIE",
              "delighted", "holds still", "a tiny straw squeak"),
         ]},
        {"title": "Like a parade", "place": "slide",
         "angle": "Wide front view up the middle lane toward a slow toboggan on",
         "who": f"{ROSIE_CUP} sits at the front of the long wooden toboggan waving one tiny arm like a queen in "
                "a parade, snow on her straw; GABBY sits upright on the toboggan behind her with her striped "
                "scarf neat and one fin raised in a royal wave, smiling wide; CAT the little blue penguin "
                "waits at the finish ribbon with her flippers on her hips; AURORA, KYLE and TORI cheer beside "
                "the ribbon with their arms in the air",
         "beats": [
             ("So a cup and a shark rode the toboggan down. Slowly. Waving, like a parade.",
              "wide shot", "ROSIE waves one tiny arm while GABBY gives a slow royal wave of her fin",
              ["ROSIE", "GABBY"], "grand and giggly", "pulls back", "a slow creaky rumble of wood on ice"),
             ("They crossed the line last. Very last. Everybody cheered as if they had won.",
              "medium shot", "AURORA, KYLE and TORI jump and cheer beside the ribbon",
              ["AURORA", "KYLE", "TORI"], "overjoyed", "pans right", "stamping paws and a ribbon flutter"),
             ("Cat was waiting at the bottom. \"I said back soon. You came to me. Same thing.\"",
              "medium close-up", "CAT plants her flippers on her hips and grins", "CAT", "cheeky",
              "pushes in", "a penguin foot tap in snow"),
         ]},
        {"title": "With great ceremony", "place": "slide",
         "angle": "Close view across the counter of the little taffy and cocoa stand at the foot of",
         "who": f"{ROSIE_CUP} stands on the counter counting out gold-foil chocolate coins one by one with a "
                "picture list in front of her cup, very solemn; GABBY floats beside her balancing a tray of "
                "steaming cocoa mugs on her back; AURORA holds out a tin trophy cup brimming with cocoa toward "
                "GABBY, grinning; KYLE hugs a mug heaped with marshmallows in both paws",
         "beats": [
             ("\"Last ones down buy cocoa!\" sang Aurora. \"With pleasure,\" said Gabby. Rosie had a list "
              "for it.",
              "medium shot", "GABBY balances the cocoa tray on her back while ROSIE checks her list",
              ["GABBY", "ROSIE"], "proud and official", "pans right", "a clink of mugs"),
             ("Nine cocoas. Extra marshmallows for Kyle. Rosie paid in chocolate coins, with great ceremony.",
              "close-up", "ROSIE counts out a gold coin onto the counter while KYLE hugs his mug",
              ["ROSIE", "KYLE"], "solemn and delighted", "pushes in", "foil coin clinks one by one"),
             ("Aurora had won the tin trophy cup. She filled it with cocoa and gave it to Gabby.",
              "medium close-up", "AURORA holds the brimming tin cup out to GABBY with both paws",
              ["AURORA", "GABBY"], "warm and grinning", "holds still", "a warm glug and a tinny clink"),
         ]},
        {"title": "Stick with me!", "place": "slide",
         "angle": "Side view along the trough of clean snow at the taffy stand beside",
         "who": "MARGOT hops on her wooden stick along the edge of the snow trough pouring a ribbon of amber "
                "maple syrup from a little copper pot onto the clean snow, easygoing and cheerful; KYLE leans "
                "over the trough with his tongue out and a dab of snow on his nose; TORI holds up a rolled "
                "golden taffy pop on a stick, delighted",
         "beats": [
             ("Beside the cocoa hopped Margot, a swirl of maple taffy on a stick. \"Stick with me!\"",
              "medium shot", "MARGOT hops along the trough on her stick and waves a stretchy arm", "MARGOT",
              "easygoing and cheerful", "tracks beside", "a springy wooden tap-tap"),
             ("She poured hot maple syrup on clean snow and rolled it up. Taffy for everyone.",
              "close-up", "MARGOT pours a ribbon of syrup onto the snow as TORI lifts her taffy pop",
              ["MARGOT", "TORI"], "generous and proud", "pans right", "a slow syrupy trickle"),
             ("Kyle taste-tested the snow. \"Needs syrup.\" Margot poured. \"Now it's perfect,\" "
              "said Kyle.",
              "medium close-up", "KYLE licks the snow thoughtfully and MARGOT tips her copper pot over it",
              ["KYLE", "MARGOT"], "thoughtful, then blissful", "pushes in", "a lick and a syrupy trickle"),
         ]},
        {"title": "Lantern twelve", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the long lantern string in",
         "who": f"GABBY floats up beside the lantern string with ROSIE riding on her back; {ROSIE_CUP} sits on "
                "the back of GABBY holding a yellow paper lantern up to the string in front of her cup, red "
                "tuque over her lid; TORI and CAT the little blue penguin look up from the snow below, CAT "
                "with a tiny tin trophy cup on her head like a hat",
         "beats": [
             ("Margot sent them home with a yellow lantern. By dark it was on Lantern Lane.",
              "wide shot", "TORI and CAT look up from the snow as the yellow lantern rises", ["TORI", "CAT"],
              "happy and tired", "tilts up", "soft crunching snow"),
             ("Gabby swam Rosie up to the string. Together they hooked it on. It was a little sticky.",
              "medium shot", "GABBY floats steady while ROSIE lifts the yellow lantern to the string",
              ["GABBY", "ROSIE"], "careful and close", "pushes in", "a tiny hook click and soft wind"),
             ("\"One more light,\" said Rosie. Twelve lanterns. Halfway to SpicySquid's surprise.",
              "medium close-up", "ROSIE gazes at the yellow glow from the back of GABBY and her straw sways",
              ["ROSIE", "GABBY"], "content", "pulls back", "soft wind and a faraway sizzle from the grill"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Warm close view across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep flat on her tummy on a soft pillow at the foot of "
                "the bunk, flippers out as if still sliding, yellow scarf visible",
         "beats": [
             ("Goodnight, old slide, three lanes of ice. Goodnight, Gabby, who came back up the hill.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, castle, river, maple and snow. Sleep well, little sip. Last place was the warmest.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, old slide, three lanes of ice.",
        "Goodnight, Gabby, who came back up the hill.",
        "Goodnight, castle, river, maple and snow.",
        "Sleep well, little sip. Last place was the warmest.",
    ],
}
