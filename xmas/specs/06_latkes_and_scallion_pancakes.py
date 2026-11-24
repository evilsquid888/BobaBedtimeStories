"""06 — Latkes and Scallion Pancakes (Sunday, December 6 · Hanukkah, third night)."""
from places import DOORWALL, LANE_NIGHT, bunk

ROSIE_CUP = "ROSIE, a small clear cup of pink milk tea with a dome lid and a striped straw,"
LINE = "a long line of little snow penguins holding paper plates"

STORY = {
    "num": "06",
    "slug": "latkes-and-scallion-pancakes",
    "title": "Latkes and Scallion Pancakes",
    "meta": [
        ("Day", "Sunday, December 6"),
        ("Holiday thread", "Hanukkah, the third night: foods fried in oil, and the morning after St. Nicholas Eve"),
        ("Guests", "Noa the jelly doughnut, Barnaby Beaksworth ❄️, SpicySquid, Kyle the black bear cub"),
        ("Cat’s role", "order runner on her snowboard, and proud wearer of a scallion pancake hat"),
        ("Mandarin", "蔥油餅 scallion pancakes · 一起 together · 好吃 delicious"),
        ("Setting", "The great hall of Frostpeak Lodge, two griddles side by side at the Squid Grill on Lantern "
                    "Lane, Lantern Lane at night, and the lodge bunk room"),
    ],
    "palette": "warm griddle gold and snowy white with saturated chili red and scallion green accents",
    "cast": ["ROSIE", "CAT", "TORI", "MOM", "NOA", "BARNABY", "SPICYSQUID", "KYLE"],
    "cast_note": "Humans in this story: none. Latkes are small golden potato pancakes; scallion pancakes are "
                 "flat, flaky and green-speckled; the scallion latke is golden with green flecks. The penguins "
                 "in the line are small background snow penguins. Herschel lights the third-night candles at "
                 "the lodge, seen only as a far glowing window.",
    "key_shot": 11,
    "places": {
        "hall": DOORWALL,
        "grill": {
            "name": "the Squid Grill stall on Lantern Lane",
            "scene": "the Squid Grill stall",
            "props": "two wide iron griddles side by side on a long wooden counter, a striped red awning hung "
                     "with strings of dried chilies, a big bowl of grated potato batter and a big bowl of "
                     "scallion dough, a jar of applesauce and a bottle of soy sauce, a tall stack of paper "
                     "plates, a rack of grilled corn skewers",
            "light": "Late golden sun and the orange glow of the grill coals warm the stall",
            "accents": "chili red and scallion green",
            "atmo": "Sizzling steam rises from the two griddles",
            "motion": "sizzling steam rises from the two griddles",
        },
        "lane": LANE_NIGHT,
        "bunk": bunk("a tiny frying pan and one little orange on the nightstand"),
    },
    "shots": [
        {"title": "Door six", "place": "hall",
         "angle": "Low angle looking up the Door Wall in",
         "who": "KYLE stands on tiptoe holding a little door open with one paw and sniffing a tiny black frying "
                f"pan that hangs inside, an orange tucked under his other arm; NOA bounces on the rug below with "
                f"her tiny arms up; {ROSIE_CUP} stands beside a boot brimming with little oranges and walnuts",
         "beats": [
             ("That morning, every boot by the door was full. Oranges, walnuts, and one very proud mitten.",
              "medium shot", "ROSIE bounces beside the brimming boot and her straw wiggles", "ROSIE",
              "delighted and wide awake", "pushes in", "a rattle of walnuts and a crackling fire"),
             ("Then Kyle opened door six. Inside hung a tiny frying pan. He sniffed it. Empty. Tragic.",
              "medium close-up", "KYLE sniffs the tiny frying pan and his ears droop", "KYLE",
              "hopeful, then heartbroken", "tilts up", "two loud sniffs and a tiny clink"),
             ("\"Frying day!\" cheered Noa. \"Tonight is the third night of Hanukkah. We fry things in oil!\"",
              "medium shot", "NOA bounces with both tiny arms up and a little sugar puffs off her", "NOA",
              "thrilled and proud", "tilts down", "a soft bounce and a poof"),
         ]},
        {"title": "My stall is your stall", "place": "grill",
         "angle": "Wide establishing view under the striped red awning of",
         "who": "SPICYSQUID sweeps two curly tentacles over the two clean griddles with a huge grin; MOM stands "
                "at one griddle rolling up her tiny sleeves beside the bowl of scallion dough; NOA stands on an "
                "upturned crate at the other griddle holding a spatula as tall as she is; KYLE sits on a stool "
                "tucking a napkin under his chin",
         "beats": [
             ("On Lantern Lane, SpicySquid cleared two griddles. \"My stall is your stall! Spice is nice!\"",
              "wide shot", "SPICYSQUID sweeps his tentacles wide over the two griddles", "SPICYSQUID",
              "generous and booming", "pushes in", "a hiss of hot iron and a crackle of coals"),
             ("Noa got one griddle. Mom got the other. Kyle got a napkin, and tucked it in.",
              "medium shot", "KYLE tucks the napkin under his chin and folds his paws on the counter", "KYLE",
              "prepared and patient", "pans right", "a napkin flap and a hiss of hot iron"),
         ]},
        {"title": "Latkes", "place": "grill",
         "angle": "Low angle across the sizzling griddle at",
         "who": "NOA stands on her upturned crate flipping small golden potato pancakes with her tall spatula, "
                "powdered sugar puffing off her with every flip, eyes shining",
         "beats": [
             ("Noa fried latkes: crispy potato pancakes, golden as coins. Sizzle, flip, sizzle.",
              "medium shot", "NOA flips a golden latke with her tall spatula", "NOA", "busy and expert",
              "pushes in", "a loud sizzle and a spatula scrape"),
             ("\"Long ago, a little oil lasted eight whole nights,\" she said. \"So we fry, and we remember.\"",
              "medium close-up", "NOA holds her spatula up like a torch and rocks on her toes", "NOA",
              "proud and glowing", "tilts up", "a steady sizzle"),
             ("\"My cousin Sésame is a Montreal bagel. He says boiling is better. He is wrong.\"",
              "close-up", "NOA shakes her spatula firmly and flips another latke", "NOA", "cheerful and certain",
              "holds still", "a sizzle and a spatula tap"),
         ]},
        {"title": "Scallion pancakes", "place": "grill",
         "angle": "Medium view over the second griddle at",
         "who": "MOM tosses a flat round green-speckled scallion pancake high above her griddle with a flick of "
                f"her spatula, eyes following it up, smiling; {ROSIE_CUP} stands on the counter beside her "
                "looking straight up with her straw tipped back",
         "beats": [
             ("The whole lane smelled of onions and potatoes and something good coming.",
              "medium close-up", "ROSIE sniffs the steam and her straw wiggles", "ROSIE", "hungry and happy",
              "pushes in", "a steady sizzle"),
             ("Mom fried **蔥油餅** (cōngyóubǐng) = scallion pancakes. Flaky, green-speckled, sizzling. Flip!",
              "medium shot", "MOM flicks her spatula and the scallion pancake sails up", "MOM",
              "calm and showy", "tilts up", "a sizzle and a whoosh of a flying pancake"),
         ]},
        {"title": "A hat I can eat", "place": "grill",
         "angle": "Close low view beside the long wooden counter of",
         "who": "CAT the little blue penguin stands in the snow with a round scallion pancake draped over her "
                "head like a floppy hat, eyes rolled up to look at it, beak open in a grin",
         "beats": [
             ("One flew up, up, and came down on Cat the penguin. \"A hat I can eat,\" said Cat.",
              "medium close-up", "CAT pats the pancake on her head with both flippers", "CAT",
              "surprised and delighted", "pushes in", "a soft warm flop"),
             ("She wore it all afternoon. It was warm. It was also lunch.",
              "close-up", "CAT nibbles the edge of her pancake hat and wiggles", "CAT", "cozy and cheeky",
              "holds still", "a tiny crispy nibble"),
         ]},
        {"title": "Cousins", "place": "grill",
         "angle": "Close view along the counter between the two griddles at",
         "who": f"{ROSIE_CUP} stands on the counter between a plate of golden latkes and a plate of scallion "
                "pancakes, holding a little picture list in front of her cup; TORI leans on the counter beside "
                "her with a squeeze bottle in each tiny arm, green straw tilted",
         "beats": [
             ("Rosie made a list. Latkes: round, crispy, fried in oil. Scallion pancakes: round, crispy, fried in oil.",
              "medium shot", "ROSIE looks from one plate to the other and marks her little picture list", "ROSIE",
              "busy and surprised", "pans right", "a tiny pencil scratch and a steady sizzle"),
             ("\"They're cousins,\" said Rosie. \"They should meet,\" said Tori.",
              "medium close-up", "TORI taps her two squeeze bottles together and ROSIE's straw bobs",
              ["TORI", "ROSIE"], "amused and pleased", "pushes in", "a plastic tap and a sizzle"),
         ]},
        {"title": "The line", "place": "grill",
         "angle": "Wide view from behind the counter looking down the snowy lane from",
         "who": "BARNABY skids up to the counter on his orange pizza snowboard holding an empty paper plate "
                f"high, tummy first, beaming; behind him {LINE} stretches away past the cocoa cart and around "
                "the fir trees",
         "beats": [
             ("The smell drifted down the lane. Whoosh! Barnaby Beaksworth slid up on his pizza board.",
              "wide shot", "BARNABY skids to the counter and lifts his paper plate higher", "BARNABY",
              "hungry and overjoyed", "pushes in", "a swoosh of a snowboard and a paper plate flap"),
             ("Behind him came a line of hungry penguins. Past the cocoa cart. Around the fir trees.",
              "wide shot", "BARNABY waves one flipper back along the long line of penguins", "BARNABY",
              "proud and generous", "pans left", "a shuffle of many little feet in snow"),
             ("The end of the line was so far away, it had different weather.",
              "wide shot", "BARNABY shades his eyes with one flipper and peers down the lane", "BARNABY",
              "impressed and unbothered", "tilts up", "a far-off shuffle and a hush of wind"),
         ]},
        {"title": "Order up!", "place": "grill",
         "angle": "Dynamic diagonal view along the busy counter of",
         "who": "CAT the little blue penguin zooms past the counter on her snowboard with a stack of full paper "
                "plates balanced on each flipper, still wearing her pancake hat; TORI holds up a jar of "
                "applesauce in one tiny arm and a bottle of soy sauce in the other, calling out; NOA and MOM "
                "flip pancakes side by side behind her",
         "beats": [
             ("Sizzle, flip, plate! Sizzle, flip, plate! Cat zoomed the orders out on her snowboard.",
              "wide shot", "CAT glides along the counter with plates balanced on both flippers", "CAT",
              "zippy and heroic", "tracks beside", "a snowboard swish and a rattle of plates"),
             ("\"Applesauce or soy sauce?\" called Tori. \"Yes!\" said every single penguin.",
              "medium shot", "TORI lifts the jar and the bottle high and shakes them both", "TORI",
              "busy and laughing", "pushes in", "a slosh of sauce and a sizzle"),
         ]},
        {"title": "Scrape", "place": "grill",
         "angle": "High angle looking down into two big bowls at",
         "who": "NOA leans over the potato bowl scraping the very bottom with a wooden spoon; MOM tips the "
                f"scallion bowl toward the light, nearly empty; {ROSIE_CUP} stands on the counter between the "
                "bowls counting on her little picture list, straw drooping a little",
         "beats": [
             ("Then Noa scraped her bowl. Scrape. Mom scraped hers. Scrape. Both nearly empty.",
              "medium shot", "NOA scrapes the bottom of her bowl while MOM tips hers to look inside",
              ["NOA", "MOM"], "puzzled and a little alarmed", "tilts down", "two hollow wooden scrapes"),
             ("Rosie counted the line. Twelve more penguins. And Barnaby, who counted as three.",
              "medium close-up", "ROSIE taps down her little picture list and her straw droops a little", "ROSIE",
              "busy and doubtful", "pushes in", "quick tiny pencil taps"),
         ]},
        {"title": "Mix them!", "place": "grill",
         "angle": "Low angle looking up from the counter at",
         "who": f"{ROSIE_CUP} stands on the counter with her straw shooting straight up and one tiny arm pointing "
                "at each bowl; TORI holds one big mixing bowl steady in front of her with both tiny arms, "
                "grinning",
         "beats": [
             ("Rosie looked at one bowl. Then the other. Her straw shot up. \"**一起** (yìqǐ) = together! Mix them!\"",
              "medium shot", "ROSIE points from one bowl to the other and her straw shoots up", "ROSIE",
              "inspired and bossy", "pushes in", "a tiny straw squeak and a sizzle"),
             ("Tori held the big bowl steady. \"Pour, little sip. You've got this.\" Potato. Scallion. Stir, stir, stir.",
              "medium close-up", "TORI holds the mixing bowl steady while ROSIE leans over it", ["TORI", "ROSIE"],
              "steady and gleeful", "tilts down", "a gloopy pour and a wooden spoon knocking a bowl"),
         ]},
        {"title": "The scallion latke", "place": "grill",
         "angle": "Close view at griddle height across the hot iron at",
         "who": "one big golden pancake flecked with green scallion sizzles on the griddle; NOA and MOM stand "
                "side by side behind it, each sliding a spatula under one edge, both leaning in with shining eyes",
         "beats": [
             ("Sizzle! Golden potato, green scallion, crispy all the way around. The scallion latke was born.",
              "close-up", "NOA and MOM lean in as the golden pancake sizzles and steams", ["NOA", "MOM"],
              "amazed and proud", "pushes in", "one big glorious sizzle"),
             ("Noa and Mom flipped it together. It took two spatulas and one very loud \"Hup!\"",
              "medium shot", "NOA and MOM lift their spatulas together and the pancake flips over",
              ["NOA", "MOM"], "teamed up and triumphant", "tilts up", "a spatula scrape and a big flop"),
         ]},
        {"title": "Responsibly", "place": "grill",
         "angle": "Cozy view at stool height beside the counter of",
         "who": "KYLE sits on his stool with his napkin tucked in, holding one golden green-flecked scallion "
                "latke in both paws, eyes squeezed shut in bliss, a single crumb on his tan muzzle",
         "beats": [
             ("Somebody had to test it. Kyle raised a paw. He had been ready since breakfast.",
              "medium shot", "KYLE lifts the scallion latke with both paws and takes a deep sniff", "KYLE",
              "solemn and ready", "pushes in", "one long happy sniff"),
             ("He ate one. Exactly one. \"I was just taste-testing,\" said Kyle. \"**好吃** (hǎochī) = delicious!\"",
              "medium close-up", "KYLE chews slowly and his whole face melts into a grin", "KYLE",
              "blissful and proud of himself", "holds still", "crispy munching and a creak of a stool"),
         ]},
        {"title": "Enough for one more", "place": "grill",
         "angle": "Wide view down the snowy lane beside",
         "who": f"BARNABY stands at the head of {LINE}, passing full paper plates back with both flippers like a "
                "juggler, his little snack satchel swinging; the penguins in the line sway from side to side "
                "with their beaks open, humming",
         "beats": [
             ("\"There's always enough for one more!\" sang Barnaby. He passed plates down the line like a juggler.",
              "wide shot", "BARNABY passes a full plate back over his shoulder with each flipper", "BARNABY",
              "jolly and quick", "tracks beside", "a patter of paper plates and happy squeaks"),
             ("The penguins hummed while they waited. Hungry humming. It was nearly a carol.",
              "wide shot", "BARNABY sways from side to side in time with the long line behind him", "BARNABY",
              "merry and musical", "pans left", "a shuffle of little feet swaying in snow"),
             ("Every penguin got one. The very last penguin got two, for waiting in the different weather.",
              "medium shot", "BARNABY holds up two full plates and nods down the lane", "BARNABY",
              "fair and satisfied", "pushes in", "a patter of paper plates"),
         ]},
        {"title": "Spice is nice", "place": "grill",
         "angle": "Low angle across the glowing coals at",
         "who": "SPICYSQUID sprinkles red chili flakes over a scallion latke on a paper plate with one curly "
                "tentacle while his other tentacles turn skewers of corn on the grill, grinning wide",
         "beats": [
             ("SpicySquid sprinkled chili on his. \"Spice is nice!\" Now it was three recipes on one plate.",
              "medium shot", "SPICYSQUID shakes chili flakes over the latke with a flourish", "SPICYSQUID",
              "delighted and showy", "pushes in", "a shake of chili flakes and a crackle of coals"),
             ("He ate it standing up, turning corn with all his other arms.",
              "medium close-up", "SPICYSQUID takes a bite and keeps turning the corn skewers", "SPICYSQUID",
              "busy and content", "pans right", "a crunchy bite and a sizzle of corn"),
         ]},
        {"title": "Third night", "place": "lane", "time": "night",
         "angle": "Wide view up the snowy hill from",
         "who": "NOA stands on the cocoa cart pointing one tiny arm up the hill at a far lodge window glowing "
                f"gold; {ROSIE_CUP} stands beside her looking up, straw tall; CAT the little blue penguin leans "
                "on the cart with a last scrap of pancake hat on her head",
         "beats": [
             ("At nightfall the lodge window glowed. \"Third night,\" said Noa. \"Herschel's lighting three candles, "
              "and the helper.\"",
              "wide shot", "NOA points up at the far golden window and bounces on her toes", "NOA",
              "proud and glad", "tilts up", "a hush of snow and a far sizzle"),
         ]},
        {"title": "The gold lantern", "place": "lane", "time": "night",
         "angle": "Low angle looking up at the lantern string over",
         "who": "MOM holds NOA up high with both tiny arms; NOA hooks a round gold paper lantern onto the string "
                "beside five glowing lanterns, powdered sugar drifting down; SPICYSQUID looks up from his "
                "glowing grill with a skewer of corn in one tentacle",
         "beats": [
             ("Mom lifted Noa. Noa lifted the gold lantern. Up it went, the sixth on the string.",
              "medium shot", "MOM lifts NOA higher and NOA hooks the gold lantern onto the string", ["MOM", "NOA"],
              "careful and teamed up", "tilts up", "a tiny brass click and a paper rustle"),
             ("\"One more light,\" said Mom and Noa, at exactly the same time.",
              "medium close-up", "MOM and NOA look at each other and laugh as the gold lantern glows",
              ["MOM", "NOA"], "warm and surprised", "pushes in", "a soft paper flutter"),
             ("SpicySquid looked up. \"Somebody sure likes lanterns,\" he said, and flipped the corn. He suspected nothing.",
              "medium shot", "SPICYSQUID glances up at the lanterns and turns his corn skewer", "SPICYSQUID",
              "cheerful and unsuspecting", "pans right", "a sizzle of corn and a crackle of coals"),
         ]},
        {"title": "And new", "place": "lane", "time": "night",
         "angle": "Warm close view under the glowing gold paper lantern on",
         "who": f"{ROSIE_CUP} stands in the snow marking her little picture list, gold glow on her lid, straw "
                 "wiggling; KYLE sits beside her licking a very clean paper plate; TORI leans down between them "
                 "with one tiny arm around each",
         "beats": [
             ("Rosie added a line to her list. Scallion latkes: round, crispy, fried in oil. And new.",
              "medium close-up", "ROSIE marks her little picture list and her straw wiggles", "ROSIE",
              "proud and cozy", "pushes in", "a tiny pencil scratch"),
             ("Kyle licked his plate. \"Tomorrow,\" he said, \"I could taste-test responsibly again.\"",
              "medium shot", "KYLE licks his paper plate clean while TORI gives him a squeeze", ["KYLE", "TORI"],
              "hopeful and full", "pulls back", "a plate lick and a hush of snow"),
         ]},
        {"title": "Goodnight", "place": "bunk", "time": "night", "blessing": True,
         "angle": "Low angle across the nightstand toward the lower bunk in",
         "who": f"{ROSIE_CUP} tucked beneath a patchwork quilt with lid and straw visible, eyes comfortably "
                "closed; CAT the little blue penguin asleep on a soft pillow at the foot of the bunk with one "
                "crumb on her beak, yellow scarf visible",
         "beats": [
             ("Goodnight, little sip, with a brand-new recipe. Goodnight, Noa and Mom, side by side.",
              "medium shot", "ROSIE's eyes soften above her quilt", "ROSIE", "comfortable and drowsy",
              "holds still", "a soft quilt rustle"),
             ("Goodnight, Kyle, who tasted only one. May your table always have room for one more.",
              "medium close-up", "CAT settles deeper into her pillow with a slow sleepy breath", "CAT",
              "comfortable and drowsy", "holds still", "a soft quilt rustle"),
         ]},
    ],
    "blessing": [
        "Goodnight, little sip, with a brand-new recipe.",
        "Goodnight, Noa and Mom, side by side.",
        "Goodnight, Kyle, who tasted only one.",
        "May your table always have room for one more.",
    ],
}
