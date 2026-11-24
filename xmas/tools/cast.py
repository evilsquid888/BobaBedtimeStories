"""Shared cast for the 24 Days of Xmas series.

One entry per drawn character: TOKEN -> (name, ID phrase, reference design).
The ID phrase is used word for word in every beat prompt; the design is the
reference-view prompt. Change a design here and rebuild every story with
`python xmas/tools/build.py xmas/specs/*.py`.

Still prompts name characters by TOKEN only, so designs may use words (such as
"star") that would flip a day still to the night look if written in a still.
"""

CAST = {
    # --- The family -------------------------------------------------------
    "ROSIE": ("Rosie", "the little pink rose-milk-tea cup with the striped straw",
              "Rosie, a small cute cup of pale-pink rose milk tea with a clear dome lid, creamy pink swirls, "
              "three tiny dark tapioca pearls at the bottom, a pink rose petal clip on her lid, big warm brown eyes, "
              "rosy cheeks, tiny arms and legs, and a pink-striped straw"),
    "CAT": ("Cat", "the little blue penguin with the yellow scarf",
            "Cat, a small round little blue penguin with glossy slate-blue feathers, a soft white tummy, "
            "a tiny orange beak, little pink feet, bright playful eyes, and a tiny knitted yellow scarf"),
    "TORI": ("Tori", "the tall golden lychee-tea cup with the green straw",
             "Tori, a taller cup of golden-amber rose lychee oolong tea with white lychee jelly cubes, "
             "a dark-red rose petal on her lid, a tall green straw, and a tiny phone clipped to her cup sleeve, "
             "big kind eyes, tiny arms and legs"),
    "MOM": ("Mom", "the tall rose-milk-tea mom cup with the pink lid",
            "Mom, a larger elegant cup of rose milk tea with a soft pink lid and a deep-pink rose on top, "
            "kind warm eyes, rosy cheeks, tiny arms and legs"),
    "YEHYEH": ("Yeh Yeh", "the round clay teapot grandpa with the bushy white eyebrows",
               "Yeh Yeh, a small round reddish-brown clay teapot of aged oolong tea with a short curved spout, "
               "a looped handle, a wisp of white steam curling from his lid like a tuft of white hair, "
               "bushy white eyebrows, round wire spectacles, kind crinkly eyes, tiny arms and legs, "
               "and a little bamboo walking stick"),
    # --- Friends ----------------------------------------------------------
    "LINA": ("Lina", "the little white snowflake crisp with the red bow",
             "Lina, a small square snowflake crisp cookie bar, soft white and powdery like fresh snow, "
             "studded with ruby-red cranberries and green pistachio bits, big bright curious eyes, rosy cheeks, "
             "tiny arms and legs, and a tiny red ribbon bow on one corner"),
    "GABBY": ("Gabby", "the little black shark with the sparkle-speckled back",
              "Gabby, a small chubby friendly black shark pup with tiny white star-shaped spots sprinkled across "
              "her back, a pale grey tummy, big shiny dark eyes, a wide gentle smile with tiny rounded teeth, "
              "short rounded fins, a curved tail, and a tiny red-and-white striped knit scarf, "
              "floating in the air as if swimming"),
    "KYLE": ("Kyle", "the black bear cub with the white V and the red beanie",
             "Kyle, a small round Formosan black bear cub with fluffy black fur, a creamy white V-shaped mark "
             "on his chest, round ears, a tan muzzle, bright cheerful eyes, and a red knit beanie with a white pom-pom"),
    "SPICYSQUID": ("SpicySquid", "the red grilled squid with the curly tentacles",
                   "SpicySquid, a cheerful grilled squid on a bamboo skewer, glossy red-orange with a sweet chili "
                   "glaze and a sprinkle of sesame seeds and chili flakes, big friendly eyes, a wide grin, "
                   "curly tentacles, and a tiny white chef's headband"),
    "NOA": ("Noa", "the round sugar-dusted jelly doughnut with the blue scarf",
            "Noa, a small round golden sufganiyah jelly doughnut dusted with powdered sugar, a shiny ruby-red "
            "jelly dot on top, big warm eyes, rosy cheeks, tiny arms and legs, and a little blue knit scarf"),
    # --- Montreal and Quebec City (the Market Train day trips) ---------------
    "SESAME": ("Sésame", "the sesame-covered bagel in the red tuque",
               "Sésame, a small golden-brown Montreal bagel with a big round hole, a shiny honey glaze, a thick coat "
               "of sesame seeds, bright friendly eyes, rosy cheeks, tiny arms and legs, and a tiny red knit tuque "
               "with a white pom-pom"),
    "COUIC": ("Couic", "the tiny white cheese curd with the striped scarf",
              "Couic, a very tiny lumpy white cheese curd with a glossy fresh surface, huge round eyes, a tiny shy "
              "smile, tiny arms and legs, and a tiny blue-and-white striped scarf"),
    "MARGOT": ("Margot", "the golden maple taffy swirl on the wooden stick",
               "Margot, a golden-amber swirl of maple taffy rolled around a wooden stick like a lollipop, glossy and "
               "stretchy, warm honey-colored eyes, a sweet easy smile, tiny stretchy arms, and a few snow crystals "
               "sparkling on her swirl"),
    "HARFANG": ("Harfang", "the big snowy owl with the red woven sash",
                "Harfang, a big fluffy snowy owl with white feathers flecked with grey, round golden eyes, a calm "
                "wise face, feathered feet, and a red woven arrow-pattern sash tied around his middle"),
    # --- Frostpeak Valley (Penguinsnowboard) --------------------------------
    "PIPER": ("Piper Paddlefoot", "the tall emperor penguin with the glittery blue snowboard",
              "Piper Paddlefoot, a tall young emperor penguin with a black back, a white tummy, golden-yellow "
              "ear patches, bright brave eyes, and a glittery blue snowboard with silver snowflakes"),
    "BARNABY": ("Barnaby Beaksworth", "the round chinstrap penguin with the orange pizza snowboard",
                "Barnaby Beaksworth, a round chinstrap penguin with a white face, a thin black line under his chin "
                "like a strap, a big happy tummy, a little snack satchel, and an orange snowboard painted like "
                "a slice of pizza"),
    "WILLA": ("Willa Wobble", "the tiny penguin with the purple earmuffs",
              "Willa Wobble, a very tiny little blue penguin with soft blue-grey feathers, a white tummy, "
              "shy bright eyes, fluffy purple earmuffs, and a tiny purple snowboard"),
    "FINNEGAN": ("Finnegan Flipsworth", "the rockhopper penguin with the spiky yellow crest",
                 "Finnegan Flipsworth, a rockhopper penguin with spiky yellow crest feathers sticking out above "
                 "each eye, a black back, a white tummy, wide excited eyes, and a red snowboard covered in fish "
                 "and lightning stickers"),
    "COLDWATER": ("Cleo Coldwater", "the macaroni penguin with the swoopy orange plumes",
                  "Cleo Coldwater, a macaroni penguin with long swoopy orange-gold plumes above her eyes, a black "
                  "back, a white tummy, dreamy artist eyes, a little paintbrush tucked behind one plume, and a teal "
                  "snowboard with gold racing lines"),
    "BJORN": ("Bjorn Bigpaws", "the big polar bear with the forest-green skis",
              "Bjorn Bigpaws, a big noble snow-white polar bear with a gentle face, a forest-green scarf, "
              "and forest-green skis with paw-print edges"),
    "NORA": ("Nora Snowmane", "the gentle polar bear with the blue shawl",
             "Nora Snowmane, a calm gentle snow-white polar bear with soft kind eyes, a pale-blue knitted shawl, "
             "a steaming cocoa mug in one paw, and white skis with pale-blue patterns"),
    "TEDDY": ("Teddy Powderpuff", "the polar bear cub with the red pom-pom hat",
              "Teddy Powderpuff, a small fluffy white polar bear cub with a mischievous grin, a red pom-pom hat, "
              "and tiny yellow skis"),
    "TILDA": ("Tilda Powderpuff", "the polar bear cub with the teal pom-pom hat",
              "Tilda Powderpuff, a small fluffy white polar bear cub with a mischievous grin, a teal pom-pom hat, "
              "and tiny yellow skis"),
    "MAGNUS": ("Magnus Meltsworth", "the grumpy old polar bear with the wooden skis",
               "Magnus Meltsworth, a big old polar bear with a grey muzzle, bushy frowning eyebrows over soft eyes, "
               "a patched brown scarf, and ancient wooden skis"),
    "AURORA": ("Aurora Frostholm", "the polar bear with the shimmering rainbow skis",
               "Aurora Frostholm, a lively young polar bear with sparkling eyes, a pink-and-green striped scarf, "
               "and shimmering rainbow-sheen skis"),
    "HERSCHEL": ("Herschel the Walrus", "the big walrus with the bushy whiskers and the cocoa ladle",
                 "Herschel the Walrus, a big kindly brown walrus with long ivory tusks, a bushy whiskery moustache, "
                 "twinkly eyes, a cream cocoa apron, and a wooden cocoa ladle"),
    "NIBBLES": ("Nibbles", "the little grey seal pup with the red bobble hat",
                "Nibbles, a small round grey seal pup with big dark eyes, long whiskers, clapping flippers, "
                "and a red bobble hat"),
    "SPLASH": ("Splash", "the little spotted seal pup with the green bobble hat",
               "Splash, a small round silver-spotted seal pup with big dark eyes, long whiskers, clapping flippers, "
               "and a green bobble hat"),
    "PRISM": ("Captain Prism", "the narwhal with the rainbow-shimmer tusk and the captain's hat",
              "Captain Prism, a plump blue-grey narwhal with a long spiral tusk that shimmers in rainbow colors, "
              "proud twinkly eyes, and a tiny navy captain's hat"),
    "WHISTLEWICK": ("Whistlewick", "the quick white arctic fox with the brass whistle",
                    "Whistlewick, a slim quick snow-white arctic fox with a big fluffy tail, sharp clever eyes, "
                    "a small brass whistle on a cord, and a little red mail satchel"),
    # --- Taiwan crew (guests) ----------------------------------------------
    "BOBA": ("Boba", "the glossy tapioca pearl with the big grin",
             "Boba, a round glossy dark-brown tapioca pearl with a big bouncy grin, bright eyes and tiny arms and legs"),
    "BING": ("Bīng", "the tall shaved ice in the sunglasses",
             "Bīng, a tall glittering mountain of shaved ice with rainbow syrup stripes, tiny sunglasses, "
             "a cherry on top, tiny arms and legs"),
    "TANGYUAN": ("Tāng Yuán", "the soft round white rice ball with the pink cheeks",
                 "Tāng Yuán, a small soft round white glutinous rice ball with pink cheeks, sleepy happy eyes, "
                 "a tiny red paper lantern, tiny arms and legs"),
    "HONGDOU": ("Hóng Dòu", "the plump red bean grandmother with the tiny ladle",
                "Hóng Dòu, a plump round dark-red adzuki bean grandmother with a soft wrinkled smile, a tiny grey "
                "hair bun, little round spectacles, a tiny wooden ladle, tiny arms and legs"),
    "MOCHI": ("Mochi", "the stretchy white mochi with the rosy cheeks",
              "Mochi, a soft round white mochi with rosy cheeks, a huge happy smile, and stretchy tiny arms and legs"),
    # --- Costa Rica crew (guests) -------------------------------------------
    "TICO": ("Tico the Toucan", "the toucan with the rainbow beak",
             "Tico the Toucan, a glossy black keel-billed toucan with a bright yellow chest and a huge rainbow "
             "beak, round excited eyes"),
    "GALLO": ("Gallo", "the cheerful white rice grain with the red bandana",
              "Gallo, a small cheerful white rice grain with a wide smile, a tiny red bandana, tiny arms and legs"),
    "PINTO": ("Pinto", "the glossy black bean with the straw hat",
              "Pinto, a small glossy black bean with a calm friendly smile, a tiny straw hat, tiny arms and legs"),
}
