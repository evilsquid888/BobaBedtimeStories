# Cameo Roster — the silly moment in every story

From Japan story 28 and Hawaii story 3 onward, every five-minute story carries **one cameo set-piece**: a popular
anime, game or movie character crashes into the story for 4–6 beats, is gloriously silly, and leaves. The cameo is the
"oh!" surprise-guest moment the [FIVE_MINUTE_STORY_GUIDE.md](FIVE_MINUTE_STORY_GUIDE.md) asks for. It is never the
solution to the hero's problem and never the lesson. Think Fast & Furious crashing a tea ceremony.

This file is the single list of who appears where, with the **design line** every story copies into its Animation
Notes cast (so the same cameo is drawn the same way in every story) and a gag seed. Change the assignment here first,
then in the story.

## Rules (from the pipeline's LESSONS.md)

1. **One cameo set-piece per story, one scene, plus an optional walk-on.** The main cameo takes 4–6 consecutive beats, usually in the middle set-piece or as the escalation
   that goes wrong. Enter big (crash, land, surface, pop out of a portal), one gag, one line at most per beat, exit as
   a **held pose** (waves from the rooftops, sinks back under, sits down and naps). Never a walk across the room.
2. **Present when named.** The cameo is in the shot in every beat that names it. Nobody refers to it before it arrives
   or after it leaves, except the hero's one-line reaction. Named-but-absent characters get drawn in from the frame edge.
3. **Design line in the cast.** Copy the design below into `- **Cast:**` as a token. Names that are also words carry
   their species ("Kirby, a round pink puffball"; "Toad, a small mushroom-capped person"). The still model reads names
   literally, so the design does the work, not the name.
4. **Prefer non-humans.** Mechs, kaiju, spirits, slimes, Pokémon and Mario creatures draw clean. A human cameo
   (Naruto, Kira, Suletta, Dom, Kiki, Rock Lee) is allowed as a declared cast human and is drawn anime; keep them to one
   per story, in their iconic outfit, and never add a second unnamed person around them.
5. **No text.** No headbands with symbols described as "a symbol", no item boxes "with a question mark", no tofu-shop
   lettering. "A plain metal headband plate", "a glowing rainbow cube", "a plain white hatchback with a black hood".
6. **Costumes stay on.** Never animate a hat, cape, helmet or crown leaving a body (the model invents a wearer). Lift,
   tip, hover right above.
7. **Giants are gentle.** Godzilla sneezes, Gundams kneel and apologize, Totoro's roar only makes wind. Nothing is
   stomped, nothing is scared. The cameo may make the hero's problem *funnier and bigger*; the hero still solves it.
8. **Header and notes.** The story header gets `**Cameo:** Name (franchise) — one line of what happens` after the
   Spotlight line. Animation Notes get `- **Cameo shot:** beats N–M, scene K; speaks: yes/no`. `check_five_minute.py`
   checks both.
9. **Both modes.** A cameo line is one speaker in its beat with a tag (`boomed the Gundam`) so MiniMax H3 can voice it in
   animated mode and the narrator reads it in narrated mode. Give the cast token a `voice:` of three words.

## The roster (design lines to copy)

### Mecha and kaiju
- `GUNDAM` — the Gundam (Mobile Suit Gundam): a towering white robot with blue chest, red skirt plates, yellow V-fin
  antenna on a knight-like head, two glowing camera eyes, a round shield; moves slowly and carefully; voice: booming,
  polite, sheepish.
- `STRIKE` — the Strike Gundam (Gundam SEED): a tall white-and-blue robot with winged red-and-blue thruster pack,
  green camera eyes, a V-fin; glides down trailing light. Pilot `KIRA` — Kira Yamato: a slim anime teen with messy
  brown hair and violet eyes in a blue-and-white pilot suit, standing on the robot's open hand; voice: soft, earnest,
  apologetic.
- `AERIAL` — Gundam Aerial (The Witch from Mercury): a sleek white robot with red-and-blue trim, glowing cyan lines,
  and eleven floating white shield-petals that drift around it and rearrange themselves. Pilot `SULETTA` — Suletta
  Mercury: an anime girl with long red hair in a thick braid, big worried eyes, a cream-and-blue school uniform; voice:
  stammering, nervous, kind. Catchphrase shape: "If you run, you gain one; if you go forward, you gain two."
- `HARO` — Haro (Gundam): a round lime-green ball robot the size of a melon with two flip-up ear panels and two round
  eyes, hops and flaps; voice: squeaky, repeating, cheerful ("Haro! Haro!").
- `EVA01` — Evangelion Unit-01: a huge lanky purple-and-green armored giant with a horned helmet, glowing green
  eyes, long arms; crouches awkwardly; voice: none (it hums).
- `GODZILLA` — Godzilla: a mountain-sized dark charcoal lizard with jagged dorsal fins that glow soft blue, small
  kind eyes, a long tail; rises from the sea slowly; voice: a rumbling roar, no words.
- `MINILLA` — Minilla, Godzilla's baby: a chubby grey kaiju the size of a shed, round belly, stubby dorsal bumps, big
  dopey eyes, blows a smoke ring instead of fire; voice: hiccuping squeaks.
- `MOTHRA` — Mothra: a giant gentle moth with cream fur and huge orange, yellow and blue patterned wings, feathery
  antennae, glowing blue eyes; lands softly; voice: a chirping sing-song, no words.
- `ULTRAMAN` — Ultraman: a giant silver-and-red hero with a smooth helmet-like head, big oval glowing eyes and a
  round blue chest light that blinks when his time runs low; strikes poses; voice: a single "Shuwatch!".
- `ASTRO` — Astro Boy: a small anime robot boy with glossy black hair in two spikes, big eyes, red boots, jet flames
  from his feet; voice: bright, kind, old-fashioned.
- `SHINKALION` — a Shinkalion (Shinkalion): a sleek white-and-blue bullet-train nose that unfolds into a tall boxy
  robot with train-car limbs and headlight eyes; voice: a conductor's chime, formal, proud.

### Studio Ghibli
- `TOTORO` — Totoro: a huge round grey forest spirit, fluffy, with a wide toothy grin, pointed ears, chevron marks on
  a cream belly, often holding a leaf on his head; voice: a yawning rumble, no words.
- `CATBUS` — the Catbus: a long grinning orange tabby cat shaped like a bus with headlight eyes, twelve furry legs,
  window openings along its sides and a fluffy tail; voice: a purring engine, no words.
- `SOOT` — Soot Sprites: a crowd of fist-sized fuzzy black fluffballs with big white eyes and stick-thin arms,
  carrying one small thing each; voice: squeaky chittering, no words.
- `NOFACE` — No-Face: a tall slim shadow-black spirit with a pale calm mask face, drifting silently, holding out gold
  nuggets in cupped hands; voice: a soft "ah... ah".
- `CALCIFER` — Calcifer: a small living flame with a grumpy face, two blue-white eye slits and a toothy mouth, sitting
  in a hearth or lantern; voice: crackly, grumpy, dramatic ("May all your bacon burn!").
- `KIKI` — Kiki: an anime girl in a plain dark dress with a big red hair bow, riding a wooden broom with a bag on it;
  voice: breathless, polite, hurried. `JIJI` — Jiji: a sleek small black cat with big round eyes riding behind her;
  voice: dry, sarcastic, worried.
- `PONYO` — Ponyo: a small round red-haired fish-girl in a red dress with a pale face, riding on waves made of
  big-eyed fish; voice: squeaky, delighted ("Ponyo loves ham!").
- `HAKU` — Haku the dragon: a long slim white river dragon with a pale teal mane, antlers and kind green eyes,
  flowing through the air; voice: calm, quiet.
- `RADISH` — the Radish Spirit: a huge plump white radish-shaped spirit in a red bowl-hat with tiny eyes and a
  gentle smile; stands very still; voice: none.
- `BARON` — the Baron (The Cat Returns): a dapper orange cat statue in a grey top hat, white shirt, green waistcoat
  and cane, who comes to life and bows; voice: silky, courtly, kind.
- `TURNIP` — Turnip Head: a hopping scarecrow with a turnip for a head, a painted smile, a tatty black coat and a
  tall hat, bouncing on one wooden pole; voice: none.
- `LAPUTA` — the Laputa garden robot: a tall tarnished bronze robot with a long oval head, moss and small flowers
  growing on its shoulders, a bird nesting on it; moves slowly; voice: none.
- `PORCO` — Porco Rosso: a scarlet two-wing seaplane with a round nose, flown by a stout pig in a brown flight jacket,
  goggles and a moustache; voice: gruff, dry, warm.
- `TETO` — Teto: a small fox-squirrel with sandy fur, a striped bushy tail, pointed ears and bright eyes, riding on
  shoulders; voice: chirps.
- `KODAMA` — kodama: small pale tree spirits with rattling tilting heads and tiny blank faces, standing in a row;
  voice: a rattling click. (Japan 75 already has one; use the roster line.)

### Naruto
- `NARUTO` — Naruto Uzumaki: an anime teen with spiky blond hair, blue eyes, whisker marks on his cheeks, an orange
  and blue jumpsuit and a plain metal headband plate; voice: loud, eager, grinning ("Believe it!"). His shadow clones
  are "ten more Narutos" drawn identical.
- `KAKASHI` — Kakashi: a tall anime ninja with spiky silver hair, a mask over his nose and mouth, one eye covered by a
  slanted headband, a green vest, reading a small plain orange book; voice: lazy, dry, amused. `PAKKUN` — Pakkun: a
  small pug in a blue vest and tiny headband; voice: gruff, bored.
- `GAMAKICHI` — Gamakichi: a bright orange toad the size of a chair with blue markings and a blue vest, puffing in on a
  cloud of smoke; voice: croaky, cheeky.
- `ROCKLEE` — Rock Lee: an anime teen in a green jumpsuit, orange leg warmers, bowl-cut black hair and enormous
  eyebrows, mid-push-up or mid-lap; voice: shouting, earnest, youthful.

### Fantasy and isekai
- `RIMURU` — Rimuru (That Time I Got Reincarnated as a Slime): a glossy sky-blue blob of slime the size of a pillow
  with two gentle dark eyes, bouncing and stretching; voice: polite, thoughtful, surprised.
- `SENSHI` — Senshi (Delicious in Dungeon): a stout dwarf with a huge grey beard, a bronze helmet, bare muscular arms,
  a big iron frying pan and a knapsack of vegetables; voice: deep, calm, stern about nutrition.
- `LAIOS` — Laios (Delicious in Dungeon): a tall anime knight with short blond hair in blue-grey armor, eyes
  sparkling at monsters, a fork in hand; voice: delighted, earnest, hungry.
- `MUSHROOM` — a Walking Mushroom (Delicious in Dungeon): a knee-high brown-capped mushroom with two stubby legs and
  no face, waddling; voice: none. `MANDRAKE` — a Mandrake: a root-vegetable with a scrunched baby face and leafy hair,
  pulled from the ground mid-shriek; voice: one long shriek.
- `FRIEREN` — Frieren: a small anime elf with long white twin-tails, pointed ears, a white-and-gold robe and a wooden
  staff, calm half-closed eyes; voice: flat, curious, slow. `MIMIC` — a Mimic: a wooden treasure chest with a wide
  toothy mouth and a long pink tongue; voice: a snap.
- `MEGUMIN` — Megumin (KonoSuba): a small anime girl in a black witch robe and huge pointed black hat with a red
  ribbon, an eyepatch, a crooked staff; voice: dramatic, chanting ("EXPLOSION!"), then exhausted.
- `FEL` — Fel (Campfire Cooking in Another World): a giant silver-white wolf as big as a food stall with ice-blue eyes
  and a lordly chin; voice: haughty, booming, demanding seconds.
- `ANYA` — Anya Forger (Spy x Family): a tiny anime girl with pink hair, two black hair horns, huge green eyes and a
  black school dress; voice: tiny, blunt, thrilled ("waku waku!"). `BOND` — Bond: a huge fluffy white dog with a black
  bow tie; voice: a soft "borf".
- `ALPHONSE` — Alphonse Elric: a tall hollow suit of grey plate armor with a horned helmet, glowing white eye slits
  and a soft voice, a kitten peeking out of the chest plate; voice: gentle, boyish, polite.
- `ALLMIGHT` — All Might: a towering muscular hero with two tall blond hair spikes, a huge white grin, a blue-red-gold
  suit; voice: booming, laughing ("I AM HERE!").
- `SAITAMA` — Saitama (One-Punch Man): a bald anime man with a blank face in a yellow jumpsuit, red gloves and boots,
  white cape, holding a shopping bag; voice: flat, bored, mild.
- `GOKU` — Goku: an anime man with wild black spiky hair in an orange martial-arts gi with a blue sash, riding `NIMBUS`,
  a small fluffy golden cloud; voice: cheerful, hungry, simple.
- `SHENRON` — Shenron: an enormous green serpent dragon with a long body coiling into the sky, red eyes, flowing
  whiskers and antlers, under a dark sky; voice: deep, slow, patient.
- `LUFFY` — Luffy: an anime teen in a straw hat, red vest and blue shorts with a scar under one eye, arms that
  stretch like rubber across the whole scene; voice: loud, laughing, hungry.
- `CHOPPER` — Chopper: a small round reindeer with a blue nose, a big pink top hat, tiny antlers and hooves, hiding
  the wrong way round behind a thin tree; voice: squeaky, flustered, delighted.
- `SAILORMOON` — Sailor Moon: an anime girl with very long blond twin-tails in two buns, a white-and-blue sailor
  uniform with a red bow and red boots, a crescent tiara; voice: dramatic, then whiny, food-loving.
- `JOTARO` — Jotaro (JoJo's Bizarre Adventure): a tall anime man in a long dark coat and cap with a gold chain,
  striking a dramatic bent-arm pose; behind him `STARPLATINUM`, a muscular glowing purple spirit striking the same
  pose; voice: a low "Yare yare".
- `DORAEMON` — Doraemon: a round blue robot cat with a white belly pouch, red collar and bell, no ears, big round
  eyes and a red nose; pulls gadgets from his pouch; voice: nasal, friendly, flustered.
- `ANPANMAN` — Anpanman: a round-headed hero with a glossy brown anpan-bun head, red cheeks, a red suit and brown
  cape, flying with one fist forward; voice: brave, warm, bright.
- `MIKU` — Hatsune Miku: an anime idol with very long teal twin-tails, a grey sleeveless top and teal tie, headphones,
  glowing sleeves; sings; voice: clear, bright, synthetic.
- `ISEKAI` — a lost isekai hero: an anime teen in a plain school uniform with a wooden sword, tumbling out of a glowing
  blue portal, a blank glowing blue panel floating beside him; voice: confused, hopeful.

### Pokémon, Nintendo, Sanrio, Sega and friends
- `PIKACHU` — Pikachu: a small chubby yellow mouse with red cheeks, black-tipped ears and a lightning-bolt tail,
  crackling with sparks; voice: "Pika!".
- `SNORLAX` — Snorlax: a huge round sleeping teal-and-cream bear-like creature with closed eyes and a big belly,
  lying flat across the road; voice: a snore.
- `MAGIKARP` — Magikarp: a big orange fish with huge round eyes, yellow whiskers and crown-fins, flopping and
  splashing uselessly; voice: "Karp!".
- `LAPRAS` — Lapras: a large gentle blue sea creature with a long neck, a grey shell with knobs, and kind eyes,
  giving rides; voice: a low musical call.
- `SQUIRTLE` — Squirtle: a small blue turtle with a brown shell and curly tail, pulling into its shell shyly,
  sometimes in round black sunglasses; voice: "Squirtle!".
- `CHARMANDER` — Charmander: a small orange lizard with a cream belly and a flame on its tail tip, hugging the tail
  flame anxiously; voice: "Char!".
- `JIGGLYPUFF` — Jigglypuff: a round pink balloon creature with big blue eyes, a curl on its forehead, holding a
  marker like a microphone; voice: a sleepy lullaby, then a puffed-up huff.
- `MARIO` — Mario: a short plump man in a red cap, red shirt, blue overalls and a big moustache in a red go-kart;
  voice: "Wahoo!", warm Italian lilt. `LUIGI` in green, taller, nervous. `PEACH` — Princess Peach: a tall anime
  princess in a pink gown with long blond hair, a gold crown with jewels; voice: sweet, kind, regal.
- `BOWSER` — Bowser: a huge turtle-dragon with a spiked green shell, red mane, horns, spiked cuffs, in a big kart;
  voice: a growling laugh, secretly delighted.
- `YOSHI` — Yoshi: a round green dinosaur with a white belly, red saddle-shell, big nose, red boots and a very long
  tongue; voice: "Yoshi!".
- `TOAD` — Toad: a small mushroom-capped person with a white cap with red spots, a blue vest; voice: squeaky, excited.
- `LAKITU` — Lakitu: a small turtle with goggles riding a smiling white cloud, holding a fishing rod with a glowing
  lure; voice: chirpy, officious.
- `DONKEYKONG` — Donkey Kong: a big friendly brown gorilla in a red necktie, pounding his chest; voice: a happy grunt.
- `KOROK` — a Korok (Zelda): a small walking wooden creature with a leaf for a face, two round eye-holes, a twig body,
  holding a tiny leaf fan; voice: giggly ("Yahaha! You found me!").
- `TOMNOOK` — Tom Nook (Animal Crossing): a plump round tanuki in a green apron and leaf-print shirt, standing on his
  hind legs; voice: chummy, business-like ("yes, yes!"). `ISABELLE` — Isabelle: a small cheerful yellow shih tzu with
  a bell-topped bun and a green plaid vest holding a clipboard; voice: bright, bubbly, official.
- `KIRBY` — Kirby: a round pink puffball with stubby arms, red feet, big oval eyes and pink cheeks, inhaling with a
  huge open mouth; voice: "Poyo!".
- `PACMAN` — Pac-Man: a flat round yellow chomper with a wedge mouth and one eye, chomping "waka waka" along a line of
  glowing pellets; voice: "waka waka".
- `SONIC` — Sonic: a cobalt-blue hedgehog with green eyes, red sneakers, white gloves, standing tapping his foot;
  voice: cocky, fast, friendly.
- `GUDETAMA` — Gudetama: a lazy raw egg yolk lying on its own egg white with a drooping face and a bacon blanket;
  voice: a slow "meh".
- `HELLOKITTY` — Hello Kitty: a small white cat with a red bow over one ear, yellow nose, no mouth, red overalls;
  voice: none (she waves).
- `CINNAMOROLL` — Cinnamoroll: a small white puppy with very long floppy ears he flies with, blue eyes, pink cheeks
  and a curled tail like a cinnamon roll; voice: a soft happy yip.
- `POMPOMPURIN` — Pompompurin: a plump golden retriever puppy shaped like a pudding with a brown beret and a caramel
  patch; voice: a slow happy "purin".
- `RILAKKUMA` — Rilakkuma: a soft round brown bear with a zipper on his back, a yellow belly patch and sleepy eyes,
  lying down anywhere; voice: a yawn.
- `MOLCAR` — a Pui Pui Molcar: a fluffy guinea-pig the size of a small car with wheels for feet, big dark eyes and
  round windows on its sides; voice: "pui pui" squeaks.
- `PIKMIN` — Pikmin: tiny plant-people in red, yellow and blue with a leaf or flower on a stalk from their heads,
  carrying things in a line; voice: tiny chirps.
- `STITCH` — Stitch (Lilo & Stitch): a small blue koala-like alien with big ears, dark eyes, four arms and a wide
  toothy grin; voice: gravelly giggles ("Ohana!").
- `HEIHEI` — Heihei (Moana): a scrawny grey-and-teal rooster with a red wattle, blank wide eyes, pecking at rocks;
  voice: a flat "bawk".
- `DOM` — Dom (Fast & Furious): a broad bald man in a white tank top and jeans standing by `CHARGER`, a growling black
  muscle car with a tall silver engine blower poking from the hood, wide rear tires; voice: low, gravelly, sincere
  ("I live my life a quarter mile at a time." "Family.").
- `AE86` — the tofu-shop AE86 (Initial D): a boxy white 1980s hatchback with a black hood, pop-up headlights and a
  wooden tofu delivery box in the back, drifting sideways through fog; driver `TAKUMI`: a sleepy anime teen in a plain
  white shirt; voice: flat, sleepy, modest.

### More main characters (added for variety)
- `LEVI` — Levi (Attack on Titan): a short anime man with sharp black hair, a white cravat tied over his nose, a brown jacket, holding a mop; voice: flat, cold, disgusted by dust.
- `GOJO` — Gojo (Jujutsu Kaisen): a tall anime man with spiky white hair, a black blindfold over his eyes, a dark high-collared uniform, hands in pockets; voice: lazy, teasing.
- `ASH` — Ash Ketchum (Pokémon): an anime boy with black spiky hair under a red-and-white cap, a blue jacket and green gloves; voice: eager, shouting. Rides with `PIKACHU`.
- `KIRITO` — Kirito (Sword Art Online): an anime teen with black hair in a long black coat with two swords on his back; voice: calm, modest.
- `SENKU` — Senku (Dr. Stone): an anime teen with tall white-and-green spiked hair, a lab coat over a tunic, a stick in hand; voice: gleeful, rapid ("ten billion percent").
- `MOB` — Mob (Mob Psycho 100): an anime boy with a plain bowl haircut in a black school uniform, blank calm face, faint glow; voice: quiet, polite.
- `SPIKE` — Spike Spiegel (Cowboy Bebop): a lanky anime man with fluffy dark green hair in a blue suit and loose tie; voice: dry, cool. `SWORDFISH` — Swordfish II: a sleek red single-seat fighter ship with a long nose and swept wings.
- `KAIJU8` — Kaiju No. 8: a tall lean blue-black kaiju with a skeletal face, glowing blue eyes and a glowing chest line, hunched politely; voice: deep, nervous, polite.
- `KOMI` — Komi (Komi Can't Communicate): a tall anime girl with very long black hair in a school uniform, trembling slightly, a notepad held closed; voice: none (a tiny nod).
- `INUYASHA` — Inuyasha: an anime half-demon with long silver hair, white dog ears and a red robe, barefoot, scowling; voice: gruff, sulky.
- `TODOROKI` — Shoto Todoroki (My Hero Academia): an anime teen with hair half red half white, a burn mark around one eye, a dark hero suit; frost on his right, steam on his left; voice: flat, polite.
- `MAOMAO` — Maomao (The Apothecary Diaries): an anime girl with dark hair in a plain apothecary's robe, freckles painted on, sparkling eyes at anything poisonous; voice: dry, delighted.
- `JESSIE` — Jessie (Team Rocket): an anime woman with long curved magenta hair in a white uniform with a red R; `JAMES` — James: an anime man with short lavender hair in the same uniform; `MEOWTH` walks between them; voice: theatrical, rhyming, "blasting off again!"
- `EDWARD` — Edward Elric (Fullmetal Alchemist): a short anime teen with a blond braid, a red coat, one shiny metal arm, furious at the word "small"; voice: loud, proud, quick.
- `NATSU` — Natsu (Fairy Tail): an anime teen with spiky pink hair and a white scaled scarf, green-faced with motion sickness; voice: groaning, then fired up. `HAPPY` — Happy: a small blue cat with white wings and a green backpack; voice: "Aye, sir!"
- `PUCK` — Puck (Re:Zero): a small round grey cat spirit with a fluffy tail and a crown-like tuft, floating and yawning; voice: sleepy, wise, cheeky.
- `UMARU` — Umaru (Himouto! Umaru-chan): a tiny chibi girl in an orange hamster hood, lying on a cushion with a cola and a comic; voice: whiny, blissful.
- `VIOLET` — Violet Evergarden: an anime girl with blond hair in a braided bun, a white dress with a blue ribbon and shining metal hands, carrying a typewriter case; voice: formal, gentle.
- `BOCCHI` — Bocchi (Bocchi the Rock): an anime girl with long pink hair in a pink tracksuit, inside a cardboard box with a guitar neck poking out; voice: a mumble, then a shredding guitar.
- `TANJIRO` / `NEZUKO` — as in the walk-on list; in Hawaii 12 they are the main cameo.
- `MIKU` — as above; Hawaii 33 and Japan 56.

### Gundam and Vivy additions (Japan 31–41)
- `CHAR` — Char Aznable (Mobile Suit Gundam): an anime man with neat blond hair in a bright red high-collared uniform and a dark visor-mask over his eyes, arms folded; voice: smooth, haughty, amused. `REDZAKU` — his red Zaku: a crimson round-headed robot with a single glowing pink eye, a spiked right shoulder, a shield on the left, kneeling; voice: none.
- `LACUS` — Lacus Clyne (Gundam SEED): an anime girl with very long pink hair and a gold hair clip in a flowing white-and-lavender dress, singing with eyes closed; voice: airy, sweet, oddly formal. `PINKHARO` — her pink Haro: a round pink ball robot with flapping ear panels; voice: "Haro! Haro!"
- `WINGZERO` — Wing Zero (Gundam Wing): a white, blue and red angel-like robot with huge white feathered wings, a yellow V-fin and green eyes, holding a long twin-barreled buster rifle in both hands; its beam is a river of white light that blooms into stars; voice: none.
- `UNICORN` — Unicorn Gundam: a sleek all-white robot with one long horn on its head; its armor splits along the seams and glows pink-red, the horn opening into a V; voice: none.
- `KSHATRIYA` — NZ-666 Kshatriya (Gundam Unicorn): a huge hunched dark-green robot with four giant green wing-binders on its shoulders and one glowing eye slit; voice: none. `MARIDA` — Marida Cruz: an anime woman with short pale-violet hair and calm eyes in a dark-green pilot suit; voice: quiet, formal, gentle.
- `VIVY` — Vivy (Vivy: Fluorite Eye's Song): an anime AI songstress with long blue hair, a flowing blue-and-white stage dress and calm turquoise eyes; voice: clear, soft, precise. `MATSUMOTO` — Matsumoto: a small white floating cube AI with glowing blue panel lines that unfolds into a teddy-bear shape to nag; voice: rapid, chirpy, bossy.
- `ZECHS` — Zechs Merquise (Gundam Wing): an anime man with very long platinum hair in a red-and-white uniform and a silver bird-shaped helmet-mask; voice: theatrical. `RAU` — Rau Le Creuset (Gundam SEED): an anime man with wavy blond hair in a white uniform and a white half-mask; voice: silky. `FRONTAL` — Full Frontal (Gundam Unicorn): an anime man with blond hair in a red uniform and a dark visor-mask; voice: smooth. All three masks stay on.
- `FREEDOM` — Freedom Gundam (Gundam SEED): a white, blue and red robot with ten blue-and-white wing blades fanned out behind it, a yellow V-fin and green eyes; voice: none.
Displaced from these rows and free to reuse later: Anpanman, Kirby, Megumin, Korok, Snorlax, Pikachu, Laios, Luffy.

### Studio-spread additions (Japan 42–52)
- `DENJI` — Denji (Chainsaw Man): an anime teen with messy blond hair, a sharp-toothed grin, a white shirt and black tie, drooling at bread; voice: loud, simple, hungry. `POCHITA` — Pochita: a small orange dog-like creature with stubby legs, a black chainsaw-shaped nose and a pull-cord tail; the nose only ever slices bread; voice: "Wan!"
- `AINZ` — Ainz Ooal Gown (Overlord): a tall skeleton in a vast black-and-purple robe with gold trim, two red points of light for eyes, holding a staff topped with seven coiled serpents; very polite; voice: deep, grand, secretly flustered.
- `LOID` — Loid Forger (Spy x Family): an anime man with neat blond hair in a green three-piece suit; voice: calm, smooth. `YOR` — Yor Forger: an anime woman with long black hair and red eyes in a black dress with a red choker, holding a lunchbox; voice: soft, apologetic. `ANYA` and `BOND` as in the roster.
- `GENOS` — Genos (One-Punch Man): an anime cyborg teen with blond hair, dark eyes with gold irises, metal arms glowing orange at the joints; voice: formal, intense. `SAITAMA` as in the roster.
- `MOTOKO` — Motoko Kusanagi (Ghost in the Shell): an anime woman with short purple hair and red eyes in a grey jacket over a dark bodysuit, arms folded; voice: cool, flat. `TACHIKOMA` as in the roster.
- `KAZUMA` — Kazuma (KonoSuba): an anime teen with brown hair in a green tracksuit-like adventurer outfit and short cape; voice: dry, complaining. `AQUA` — Aqua: an anime goddess with long blue hair in a blue-and-white dress, crying dramatically; voice: wailing, proud. `DARKNESS` — Darkness: an anime knight with a blond ponytail in heavy silver armor, cheeks flushed, bracing to be hit; voice: thrilled, breathless. `MEGUMIN` as in the roster.
- `KNIGHTSABERS` — the Knight Sabers (Bubblegum Crisis): four sleek armored figures in glossy hardsuits, blue, red, green and pink, with visored helmets that stay on; voice: clipped radio chatter. `PRISS` — Priss: an anime woman with short brown hair in a red leather jacket on a red motorcycle; voice: cocky, raspy.
- `VF25` — Alto's VF-25 Valkyrie (Macross Frontier): a white-and-red fighter jet that unfolds mid-air into a slim humanoid robot; voice: none. `RANKA` — Ranka Lee: an anime girl with short green hair in a yellow dress, singing with one hand raised; voice: bright, bubbly ("Kira!"). `SHERYL` — Sheryl Nome: an anime idol with long strawberry-blond hair in a pink stage outfit, striking a diva pose; voice: confident, belting.
- `ZEROTWO` — Zero Two (Darling in the Franxx): an anime girl with very long pink hair, two small red horns, teal eyes, a red military uniform with white gloves, licking a honey stick; voice: teasing, purring ("Darling").
Displaced from these rows and free to reuse later: Ponyo (42), Cinnamoroll (43), Rilakkuma (44), Senshi (46), Yoshi (49), Ultraman (51), Chopper (52), Saitama's old slot at 66.

### Later additions (Japan 53–60)
- `TAKUYA` — Takuya Seo (Gals Can't Be Kind to Otaku!?): an anime high-school boy with dark hair, glasses and a school uniform, clutching a shopping bag, flustered; voice: stammering, earnest. `KEI` — Kei Amane: an anime gal with long pale-blond hair, sharp cool eyes and a loose school uniform with a cardigan; voice: flat, cool, kind underneath. `KOTOKO` — Kotoko Ijichi: an anime gal with long dark hair with bright streaks, big expressive eyes, a loud school uniform with accessories; voice: loud, teasing, impossible to ignore.
- `MILIM` — Milim Nava (Slime): a small anime demon lord with very long pink twin-tails, bright blue eyes and a tiny black-and-pink outfit, bouncing; voice: shrill, delighted, hungry. `RANGA` — Ranga: a giant black wolf with a white star on his forehead, a single horn and purple-tinged fur, carrying things in his mouth; voice: deep, devoted ("Master!"). `GOBTA` — Gobta: a small green goblin in a leather vest, dropping whatever he holds; voice: squeaky, hapless. `SHUNA` — Shuna: a petite anime oni princess with pink hair and small horns in a white-and-red kimono; voice: gentle, polite. `BENIMARU` — Benimaru: a tall anime oni with red hair and small horns in a dark red coat, arms folded; voice: cool, dry. `VELDORA` — Veldora: a huge coiled storm dragon with grey-blue scales and gold eyes who laughs too loud; voice: booming "Kwa ha ha!" `RIMURU` as in the roster.
- `CLEVATESS` — Clevatess (Clevatess): a towering black beast king, part wolf and part dragon, with long dark horns, glowing gold eyes and a baby sling across his chest; moves softly so the baby stays asleep; voice: deep, grave, secretly doting. `ALICIA` — Alicia: an anime hero girl with long blond hair in a white-and-gold tunic, a sword on her back, arms folded; voice: stern, exasperated, caring. `LUNA` — Luna: a round-cheeked baby in a cream swaddle with a tuft of pale hair, giggling; voice: baby giggles.
- `WILL` — Will Serfort (Wistoria: Wand and Sword): an anime teen with short white hair and red-brown eyes in a dark academy uniform with a plain sword at his hip, grinning through failure; voice: bright, stubborn, upbeat. `ELFARIA` — Elfaria Albis: an anime young woman with very long golden hair and blue eyes in a flowing white-and-gold mage robe, drifting down on soft light; voice: gentle, warm, proud of him.
- `AURA` — Aura the Guillotine (Frieren): an anime demon woman with long pale-lilac hair, two curved dark horns, red eyes and a dark gown with gold trim, standing beside a giant floating golden set of scales; voice: imperious, then sulky ("Obey!"). `FRIEREN`, `FERN` and `STARK` as in the roster; in Japan 60 all three travel together.
- `SHINJI` — Shinji Ikari (Evangelion): an anime teen with short dark hair in a white shirt and black trousers, shoulders hunched, holding a wish-strip he cannot decide on; voice: quiet, apologetic. `ASUKA` — Asuka Langley Shikinami: an anime girl with long red-orange hair and twin red hair clips in a red plugsuit, hands on hips; voice: loud, proud, impatient. `MARI` — Mari Illustrious Makinami: an anime girl with long dark-brown twin-tails and red glasses in a pink plugsuit, grinning; voice: playful, singing, teasing. `EVA01` as in the roster (a crouching purple-and-green giant, never menacing). `PENPEN` as in the walk-on list; in Japan 74 he is the main cameo.
- `OJISAN` — Ojisan (Uncle from Another World): a scruffy anime man with a long tired face, messy dark hair and a thin beard in a grey tracksuit, one hand raised and glowing with a spell; voice: flat, earnest, slightly out of date. `ELF` — the Elf: an anime elf woman with very long blond hair, long pointed ears, green eyes, a white-and-green tunic and a bow on her back, arms crossed and blushing; voice: haughty, flustered, secretly fond.
- `SAITOU` — Saitou (Handyman Saitou in Another World): a plain anime man with short brown hair in a work jacket and a leather tool belt, screwdriver in hand, calm; voice: mild, practical. `RAELZA` — Raelza: an anime knight woman with long black hair in grey plate armor with a sword at her hip, stern; voice: gruff, loyal. `MORLOCK` — Morlock: a tiny ancient wizard with an enormous white beard, a tall crooked hat and a gnarled staff, mid-forgetting; voice: creaky, wandering. `LAFANPAN` — Lafanpan: a palm-sized fairy with pink hair, glittering wings and a coin purse bigger than herself; voice: shrill, greedy, cheerful.
Displaced and free to reuse later: Kiki and Jiji (53), Catbus (55), the Laputa robot (57), Doraemon (59), Turnip Head (72), Rimuru's second slot (74), Tom Nook (76), Charmander's Japan slot (78).

### Shonen and isekai additions (Japan 81–100)
- `VASH` — Vash the Stampede (Trigun): a tall anime man with spiky blond hair, round yellow glasses and a long red coat, flashing a peace sign; voice: goofy, loud ("Love and peace!"), then a sneeze.
- `MARIN` — Marin Kitagawa (My Dress-Up Darling): an anime girl with long blond hair with pink tips in a straw-stuffed scarecrow costume with a floppy hat, posing; voice: bubbly, loud, delighted. `WAKANA` — Wakana Gojo: a tall anime boy with dark hair and a serious face, a pincushion on his wrist and a needle in hand; voice: quiet, apologetic.
- `MASH` — Mash Burnedead (Mashle): an anime boy with short brown hair, a blank face and enormous muscles in a dark school uniform, holding a cream puff; voice: flat, polite.
- `REIGEN` — Reigen (Mob Psycho 100): an anime man with slicked blond hair in a cheap grey suit and tie, hands out as if sensing spirits; voice: smooth, fast-talking. `MOB` as in the roster.
- `EDWARD` and `ALPHONSE` as in the roster.
- `TANYA` — Tanya Degurechaff (Saga of Tanya the Evil): a tiny anime girl with blond hair in a dark military greatcoat and cap, floating on a glowing orb, saluting; voice: clipped, grumbling about paperwork.
- `JOSUKE` — Josuke Higashikata (JoJo): an anime teen with a tall glossy black pompadour in a dark school uniform with gold hearts, hands on hips; voice: friendly, then dangerous about his hair. `CRAZYDIAMOND` — Crazy Diamond: a glowing pink muscular spirit with heart motifs, hovering behind him, one finger extended; voice: none.
- `NAOFUMI` — Naofumi (Shield Hero): an anime young man with dark hair in a green cloak and leather armor, a round shield that glows and changes shape; voice: gruff, tired. `RAPHTALIA` — Raphtalia: an anime raccoon-girl with long brown hair, round raccoon ears and a striped tail, in a traveler's dress; voice: sweet, earnest. `FILO` — Filo: a giant round white bird like a fluffy ostrich with a blue-and-white feather crest, eating anything; voice: a cheerful squawk.
- Demon Slayer party: `TANJIRO`, `NEZUKO`, `ZENITSU`, `INOSUKE` as in the walk-on list; in Japan 95 they are the main cameo together.
- `JINWOO` — Sung Jinwoo (Solo Leveling): an anime man with dark hair and sharp eyes in a black coat, calm; voice: low, quiet ("Arise."). `IGRIS` — Igris: a tall shadow knight in dark red-black plate armor with a plume, kneeling then saluting; voice: none. `SHADOWS` — shadow soldiers: a line of soft translucent purple figures with glowing eyes, standing still; voice: none.
Displaced and free to reuse later: Molcar (83), Isabelle (85), Sonic (91), Toad (92), Haku's Japan slot (96). Fel moved to Hawaii 20 (replacing Snorlax), Frieren's mimic gag to Hawaii 34 (replacing Lakitu); Aerial and Suletta moved to Hawaii 28 (replacing Pikachu; Hawaii 43 stays Todoroki).

### Walk-ons (1–2 beats; design lines to copy)
- `PSYDUCK` — Psyduck: a yellow duck Pokémon with a blank stare, holding its head with both paws; voice: "Psy..."
- `MEOWTH` — Meowth: a cream cat Pokémon with a gold coin charm on its forehead, standing upright; voice: nasal, scheming.
- `EEVEE` — Eevee: a small brown fox-like Pokémon with a fluffy cream collar and big ears; voice: a chirp.
- `MIMIKYU` — Mimikyu: a small Pokémon hidden under a lumpy cloth costume with a drawn-on smiling face and a crooked tail; voice: a squeak.
- `DITTO` — Ditto: a purple blob Pokémon with dot eyes and a flat smile, melting into a bad copy of whoever is nearest; voice: none.
- `WOBBUFFET` — Wobbuffet: a tall blue blob Pokémon with squinted eyes, saluting; voice: "Wobba!"
- `SLOWPOKE` — Slowpoke: a pink dopey Pokémon lying on its belly, mouth open, very slow; voice: a late "Slow..."
- `WOOPER` — Wooper: a tiny blue Pokémon with a wide smile and branching gills, flopping happily; voice: "Woop!"
- `MUDKIP` — Mudkip: a small blue Pokémon with an orange belly and a fin on its head; voice: "Mud!"
- `OSHAWOTT` — Oshawott: a small blue-and-white otter Pokémon with a shell on its belly; voice: a proud squeak.
- `PIPLUP` — Piplup: a small blue penguin Pokémon with a white face, sliding on its belly; voice: a proud chirp.
- `TOGEPI` — Togepi: a tiny Pokémon still in a spotted eggshell, waving stubby arms; voice: "Toge!"
- `DRAGONITE` — Dragonite: a round-bellied orange dragon Pokémon with tiny wings and a delivery bag; voice: a happy hum.
- `GYARADOS` — Gyarados: a long blue sea-serpent Pokémon with a fierce face and a gentle heart; voice: a roar that ends in a grin.
- `GOLDEEN` — Goldeen: a white goldfish Pokémon with orange spots, a horn and flowing fins; voice: "Goldeen!"
- `LUCARIO` — Lucario: a blue-and-black jackal Pokémon with closed eyes, meditating cross-legged; voice: calm, low.
- `CLEFAIRY` — Clefairy: a pink round Pokémon with a curl on its head and small wings, dancing under the moon; voice: a sing-song.
- `LITWICK` — Litwick: a small white candle Pokémon with one eye showing and a purple flame; voice: a tiny crackle.
- `DROWZEE` — Drowzee: a yellow-and-brown tapir Pokémon with a long snout, sniffing dreams; voice: a sleepy snuffle.
- `SYLVEON` — Sylveon: a pale pink-and-white fox Pokémon with ribbon-like feelers; voice: a soft trill.
- `VULPIX` — Alolan Vulpix: a snow-white six-tailed fox Pokémon with icy blue eyes; voice: a cool yip.
- `BULBASAUR` — Bulbasaur: a teal frog-like Pokémon with a green bulb on its back; voice: "Bulba!"
- `POPPLIO` — Popplio: a blue sea-lion Pokémon with a round pink nose, blowing water balloons; voice: a bark.
- `WAILORD` — Wailord: an enormous navy-blue whale Pokémon with a pale belly, floating like a blimp; voice: a deep "Waiiil".
- `PYUKUMUKU` — Pyukumuku: a small black sea-cucumber Pokémon with pink spikes, flung and landing with a plop; voice: none.
- `RAICHU` — Alolan Raichu: an orange-and-cream mouse Pokémon surfing on its own flat tail; voice: "Rai!"
- `LITTEN` — Litten: a small black-and-red kitten Pokémon with a grumpy face; voice: a hiss-purr.
- `EXEGGUTOR` — Alolan Exeggutor: a Pokémon shaped like a very tall palm tree with three smiling heads at the top; voice: a slow "Exeg..."
- `KOMALA` — Komala: a small koala Pokémon asleep hugging a log, never waking; voice: a snore.
- `ROWLET` — Rowlet: a round owl Pokémon with a leaf bow tie, head rotating; voice: a hoot.
- `BEWEAR` — Bewear: a big pink-and-black bear Pokémon hugging things far too hard; voice: a happy grunt.
- `BOUNSWEET` — Bounsweet: a tiny purple fruit Pokémon with a leafy top, bouncing; voice: a chirp.
- `ORICORIO` — Oricorio: a small pink dancing bird Pokémon with pom-pom wings; voice: a cheer.
- `PICHU` — Pichu: a tiny yellow mouse Pokémon, baby Pikachu, sparking by accident; voice: "Pi!"
- `SLUGMA` — Slugma: a slug Pokémon made of slow orange lava with droopy eyes; voice: a gurgle.
- `PENPEN` — Pen Pen (Evangelion): a warm-water penguin with a red crest, a backpack and a cold beer-can-shaped juice; voice: "Kwaa."
- `HAMTARO` — Hamtaro: a tiny orange-and-white hamster with a big head and bright eyes; voice: a squeaky "Heke?"
- `KON` — Kon (Bleach): a scruffy stuffed lion plush with mismatched button eyes, alive and loud; voice: whiny, bold.
- `KERO` — Kero (Cardcaptor Sakura): a tiny golden winged lion-cub plush with a long tail; voice: bossy, sweet-toothed.
- `JIBANYAN` — Jibanyan (Yo-kai Watch): a red two-tailed cat yokai with a blue flame on each tail; voice: "Nyan!"
- `AGUMON` — Agumon (Digimon): a small orange dinosaur with green eyes and big claws; voice: eager, friendly.
- `SHIPPO` — Shippo (Inuyasha): a tiny fox-kit boy with a bushy tail and a bow in his hair; voice: squeaky, boastful.
- `LUNA` — Luna (Sailor Moon): a slim black cat with a crescent mark on her forehead; voice: prim, worried.
- `PANDA` — Panda (Jujutsu Kaisen): a big walking panda in a school uniform jacket; voice: deep, friendly.
- `ZENITSU` — Zenitsu (Demon Slayer): an anime boy with yellow-orange hair and a yellow haori, mid-scream at nothing; voice: a shriek.
- `INOSUKE` — Inosuke (Demon Slayer): a bare-chested anime boy wearing a grey boar-head mask (it stays on); voice: a bellow.
- `DEKU` — Deku (My Hero Academia): an anime boy with messy green hair and freckles in a green hero suit, saluting; voice: eager, nervous.
- `CHOJI` — Choji (Naruto): a round anime ninja with spiky brown hair, swirl cheek marks and a bag of chips; voice: munching, cheerful.
- `SHIKAMARU` — Shikamaru (Naruto): an anime ninja with a spiky ponytail lying on his back watching clouds; voice: a bored "what a drag".
- `KRILLIN` — Krillin (Dragon Ball): a short bald anime man with six dots on his forehead in an orange gi; voice: nervous, friendly.
- `VEGETA` — Vegeta (Dragon Ball): an anime man with tall flame-shaped black hair in blue armor, arms crossed, scowling; voice: proud, offended.
- `BUU` — Majin Buu: a round pink creature with a head tentacle, a purple cape and a huge grin, eating candy; voice: giggly, booming.
- `ZORO` — Zoro (One Piece): an anime man with green hair, three swords on his hip, holding a map upside down; voice: gruff, lost.
- `SANJI` — Sanji (One Piece): an anime man with blond hair over one eye in a black suit, lighting a stove; voice: smooth, proud.
- `USOPP` — Usopp (One Piece): an anime teen with a very long nose and curly hair in a cap, mid-tall-tale; voice: boastful.
- `TAILS` — Tails: a small orange two-tailed fox flying by spinning his tails; voice: bright, clever.
- `WADDLEDEE` — Waddle Dee: a small round orange creature with stubby feet, carrying a thing twice its size; voice: none.
- `SHYGUY` — Shy Guy: a small figure in a red hooded robe and a white mask (the mask stays on); voice: none.
- `KUROMI` — Kuromi (Sanrio): a small white rabbit-like creature in a black jester hood with a pink skull, sulking; voice: a huff.
- `CHIIKAWA` — Chiikawa trio: a small white hamster-like creature, a yellow cat and a blue-grey rabbit, standing in a row; voice: squeaks.
- `KAPIBARA` — Kapibarasan: a round beige capybara plush-like creature, half-asleep in warm water; voice: a sigh.
- `BOCCHI` — Bocchi (Bocchi the Rock): an anime girl with long pink hair in a pink tracksuit hiding inside a cardboard box; voice: a mumble.
- `FERN` — Fern (Frieren): an anime girl with long purple hair in a dark robe, holding a staff, politely scolding; voice: deadpan.
- `STARK` — Stark (Frieren): an anime warrior with red hair and a huge axe, trembling bravely; voice: a wobble.
- `WARAWARA` — Warawara (The Boy and the Heron): a drift of small white puffball spirits rising into the sky; voice: none.
- `HERON` — the Grey Heron (The Boy and the Heron): a tall grey heron with a wide toothy grin and a wobbling beak; voice: croaky, sly.
- `YAKUL` — Yakul (Princess Mononoke): a red elk with wide antlers and a kind face; voice: none.
- `ARRIETTY` — Arrietty: a tiny anime girl the size of a thumb with a red dress and a pin as a sword, under a leaf; voice: a tiny whisper.
- `OHMU` — an Ohmu (Nausicaä): a huge gentle armored insect with rows of glowing blue eyes; voice: a deep hum.
- `MOON` — Moon (Whisper of the Heart): a fat round grey-and-white cat sitting like a loaf; voice: none.
- `POMPOKO` — a Pom Poko tanuki: a plump raccoon-dog juggling leaves, mid-transformation; voice: a cackle.
- `TACHIKOMA` — a Tachikoma (Ghost in the Shell): a round blue spider-tank with four legs and a chirpy single eye; voice: chatty, childlike.
- `AKIRABIKE` — Kaneda's bike (Akira): a long glossy red futuristic motorcycle covered in round stickers, lying on its side skid; rider absent; voice: none.
- `TURBOGRANNY` — Turbo Granny (Dandadan): a tiny hunched granny ghost with white hair and glowing eyes, running on all fours at racing speed; voice: a cackle.
- `KAMENRIDER` — a Kamen Rider: a hero in a green insect-eyed helmet and red scarf on a motorcycle; voice: a shout of "Henshin!"
- `TANJIRO` — Tanjiro (Demon Slayer): an anime boy with dark red hair and a black-and-green checkered haori carrying a wooden box; voice: earnest, gentle.
- `NEZUKO` — Nezuko (Demon Slayer): an anime girl with long black hair tipped orange, a pink kimono and a bamboo muzzle, peeking from a box; voice: "Mmm!"
- `HINATA` — Hinata (Haikyuu): a small anime boy with spiky orange hair in a black-and-orange volleyball kit, leaping very high; voice: a yell.
- `GON` — Gon (Hunter x Hunter): an anime boy with tall spiky black-green hair, green jacket and a fishing rod; voice: cheerful.
- `DIMPLE` — Dimple (Mob Psycho 100): a small green floating ghost with a smug smile and red cheeks; voice: sly.
- `PLATELETS` — the Platelets (Cells at Work): a line of tiny children in blue caps carrying a sign-less banner; voice: tiny cheers. (Humans; use only where a tiny crowd fits.)
- `GOLION` — Voltron (GoLion): a towering robot made of five colored lion heads and limbs; voice: a fanfare.
- `MAZINGER` — Mazinger Z: a huge black-and-grey robot with a red chest plate and a horned helmet; voice: a blast of "Rocket Punch!"
- `GURREN` — Gurren Lagann: a red robot with a face for a chest, flaming sunglasses and a giant drill; voice: a shout of "Who the heck do you think I am!"
- `KURIBOH` — Kuriboh (Yu-Gi-Oh): a round brown fuzzball with green claws and big eyes; voice: a squeak.
- `MEW` — Mew (Pokémon): a small pink floating cat-like Pokémon with big blue eyes and a long thin tail, peeking in; voice: a soft "mew".
- `DEDENNE` — Dedenne (Pokémon): a tiny orange mouse Pokémon with whisker antennae and a round belly; voice: a squeak.
- `BLUESHELL` — a blue shell (Mario Kart): a spiky blue turtle shell with two small white wings, flying on its own toward whoever is in front; voice: a whistle.
- `INKLING` — an Inkling (Splatoon), squid form: a small bright-orange cartoon squid with big white eyes, hopping in an orange ink puddle; voice: "Woomy!"

## Assignments — Japan (stories 28–100)

| # | Story | Cameo | Gag seed |
|---|---|---|---|
| 28 | Pock Ramune and the Festival Goldfish Scoop | Gundam | Kneels at the tank with a poi the size of a door, tears it with one careful finger, sulks. Grabby hands, giant edition. |
| 29 | The Dango Three and the Portable-Shrine Parade | Totoro | Picks up the whole mikoshi alone, roars "wasshoi" as wind, everyone's load becomes zero, which is the wrong lesson, so they take it back. Walk-on: Soot Sprites carry one shrine bead. |
| 30 | Rin Ramen and the Lucky Omikuji | Haro | Bounces in reading fortunes wrong: "Haro! Great luck! Haro! Bad luck! Haro! Snack luck!" Walk-on: Psyduck holds its head at the fortune box. |
| 31 | Anko and the Sharing Bench | Char Aznable and his red Zaku (Mobile Suit Gundam) | A masked man in red strolls up and claims the bench as his own; his crimson one-eyed Zaku kneels behind him, also wanting to sit. Anko has met a bigger bench grump. Walk-on: Pompompurin naps on the bench. |
| 32 | Momo Mochi and the Pink Petal Snow | Lacus Clyne and her pink Haro (Gundam SEED) | Drifts through the petal storm singing, eyes closed, perfectly calm; the pink Haro bounces after petals shouting "Haro!" and starts a pink avalanche. Walk-on: Eevee chases petals. |
| 33 | Kori Kakigori and the Summer Meltdown | Godzilla | Wades ashore wanting shaved ice; his breath is hot; fans Kori with his tail, blows the stall over. Walk-on: Squirtle in sunglasses on the sand. |
| 34 | Tako and Yaki and the Summer Fireworks | Wing Zero and its twin buster rifle (Gundam Wing) | Lands on the far riverbank, spreads enormous white wings and fires the buster rifle straight up: the biggest, sparkliest firework of the night, then takes a bow. Walk-on: Luigi jumps at the bang. |
| 35 | Kuma Kuri and the Autumn Leaf Trail | Unicorn Gundam | A sleek white robot with one horn stands among the maples; its armor splits open and glows red to match the leaves, then it stays a tree-sized statue for the rest of the walk. Walk-on: Shikamaru naps in the leaves. |
| 36 | Yuki and the First Snowfall | Marida Cruz and the NZ-666 Kshatriya (Gundam Unicorn) | A huge dark-green four-winged robot lands softly in the snowy square; its pilot steps out and lets Yuki warm her cold cheeks, very formally. Walk-on: Pen Pen in the snow. |
| 37 | Maru Matcha and the Carp Streamers | Magikarp | Flops up trying to fly like the koinobori, splashes everyone, gets lifted by a gust at last. Walk-on: Dragonite flies with the carp. |
| 38 | Sora Soft-Cream and the Winter Illuminations | Vivy and Matsumoto (Vivy: Fluorite Eye's Song) | A blue-haired AI songstress sings one note and every light in the park pulses in time; the little white cube AI nags her about the mission and gets lit up like a bauble. Walk-on: Mimikyu under the lights. |
| 39 | Rin Ramen and the Secret Broth Recipe | Naruto + shadow clones | Bursts in for ramen, then ten more Narutos, all slurping, none of them the secret ingredient. Walk-on: Choji eating a bowl. |
| 40 | Pepper-kun and the Sizzling Showdown | The Mask Council: Zechs, Rau Le Creuset and Full Frontal (Gundam) | Three masked men in uniforms take the judges' table, score the sizzle with raised plates, and argue about whose mask is the most dramatic. Masks stay on. Walk-on: Sanji judging. |
| 41 | Tako and Yaki and the Osaka Takoyaki Stand | Freedom Gundam (Gundam SEED) | Descends on ten fanned blue-white wings and blocks the whole street; the runaway batter ball bounces off its foot back into the chase. Walk-on: an Inkling cheering. |
| 42 | Tai Taiyaki and the Riverside Stall | Alto's VF-25 Valkyrie, Ranka Lee and Sheryl Nome (Macross Frontier) | A white-and-red jet screams up the canal, unfolds into a robot and hovers; two idols land on its shoulders and have a sing-off over the stall; the taiyaki rise on the high notes. Walk-on: Mudkip in the canal. |
| 43 | Coro Korokke and the Bakery Rush | Denji and Pochita (Chainsaw Man) | A broke teen presses his face to the bakery window dreaming of bread with jam; his little orange chainsaw-nosed dog slices every loaf into perfect even slices far too fast; Coro quietly catches them. Walk-on: Hamtaro steals a crumb. |
| 44 | Mero Melonpan and the Sleepy Bakery Dream | Ainz Ooal Gown (Overlord) | Inside the dream, a very polite skeleton king in a vast purple robe announces he now rules the bakery, discovers nobody is scared, and asks if he may also have a nap. Walk-on: Kon the plush snores. |
| 45 | Tomi Tamago and the Conveyor-Belt Parade | Gudetama | Rides the belt around and around, refusing to be chosen: "meh". Tomi admires the commitment. Walk-on: Meowth rides the belt. |
| 46 | Tama Onigiri and the Bento-Box Balance | The Forgers: Loid, Yor, Anya and Bond (Spy x Family) | A whole family arrives at the picnic; Yor's bento is a smoking black brick, Anya reads every lunch's mind ("waku waku!"), Loid smoothly swaps boxes, Bond eats the brick and is fine. Walk-on: Togepi in a bento. |
| 47 | Rin Ramen and the Slurpy Udon Race | Saitama and Genos (One-Punch Man) | The bald hero finishes the race bowl in one slurp and looks bored; his cyborg disciple analyses noodle technique out loud; the udon granny is unimpressed by both. Walk-on: Zoro lost, map upside down. |
| 48 | Momo Mochi and the Shinkansen Departure | Motoko Kusanagi and a Tachikoma (Ghost in the Shell) | The Major stands perfectly still on the platform; her blue spider-tank chatters about the train's wheels and tries to board as luggage. Walk-on: Dragonite with a delivery bag. |
| 49 | Sora Soft-Cream and the Hokkaido Milk Farm | The KonoSuba party: Kazuma, Aqua, Megumin and Darkness | Aqua tries to bless the milk and cries when the cow ignores her; Megumin EXPLOSIONs an empty hill and naps; Darkness volunteers to be charged by the cow and is delighted; Kazuma sighs. Walk-on: Slowpoke in the milk pail. |
| 50 | The Grand Half-Way Festival of Friends | Mario Kart (Mario, Bowser, blue shell) | A kart race tears through the festival lane; a blue shell finds Bowser; everyone cheers from the stalls. Walk-on: Wobbuffet salutes a passing shell. |
| 51 | Tako and Yaki and the Osaka Castle Adventure | The Knight Sabers and Priss (Bubblegum Crisis) | Four glossy hardsuits land on the castle roof in a line and pose; Priss roars up on her red motorcycle, late; the tour guide thinks they are part of the exhibit. Walk-on: Panda the tourist. |
| 52 | Kuma Kuri and the Nara Deer Bows | Zero Two (Darling in the Franxx) | A pink-haired girl with little red horns bows to the deer, calls Kuma "darling", licks a honey stick, and the deer bow back deeper than they ever bowed for crackers. Walk-on: Yakul among the deer. |
| 53 | Niko Nigiri and the Kyoto Kimono Day | Takuya Seo, Kei Amane and Kotoko Ijichi (Gals Can't Be Kind to Otaku!?) | Two gals drag a flustered otaku into the kimono shop; Kotoko shouts about every colour, Kei picks one with a single cool nod, Takuya ends up in the loudest kimono in Kyoto and poses anyway. Walk-on: Luna on the shop roof. |
| 54 | Maru Matcha and the Tea Ceremony | No-Face | Sits perfectly still at the tea mat, offers gold nuggets instead of a sweet, bows when gently declined. Walk-on: Mew peeking in. |
| 55 | Momo Mochi and the Yukata Summer Stroll | Rimuru, Milim, Ranga and Gobta (That Time I Got Reincarnated as a Slime) | A blue slime strolls the river festival with a hyper pink-haired demon lord who wants every snack at once, a giant black wolf who carries the snacks, and a goblin who drops them; Momo's yukata sash becomes Milim's prize. Walk-on: the Chiikawa trio at a stall. |
| 56 | Sen Senbei and the Summer Wind-Chimes | Hatsune Miku | Sings one note and a thousand chimes answer in harmony; Sen's wobbly chime sings the loudest. Walk-on: Kero flying between chimes. |
| 57 | Kuma Kuri and the Golden Pavilion | Clevatess, Alicia and baby Luna (Clevatess) | A huge black beast king pads into the pavilion garden with a baby in a sling on his chest; the hero Alicia scolds him about nap time; the baby giggles at the gold in the pond and the beast king melts. True shine, et cetera. Walk-on: Zenitsu screams at a sparrow. |
| 58 | Kompei and the Indigo Dye Workshop | Soot Sprites | Mistake Kompei for their star candy and carry him toward the boiler; he comes back indigo-dusted. Walk-on: Ditto imitates Kompei. |
| 59 | Dai Daruma and the Calligraphy Brush | Will Serfort and Elfaria Albis (Wistoria: Wand and Sword) | A swordsman with zero magic tries the brush, draws a wobbly stroke, cheerfully swings his sword instead and slices the paper into perfect squares; Elfaria floats down from a tower of light and says the wobbly one is her favourite. Walk-on: Kuriboh fuzzing about. |
| 60 | Sora Soft-Cream and the Sapporo Snow Festival | Frieren, Fern, Stark and Aura the Guillotine (Frieren: Beyond Journey's End) | Frieren casts a useless spell that makes every snow sculpture smell like warm bread; Fern scolds her; Stark hides from a snow dragon that is clearly snow; Aura arrives with her giant golden scales and orders the sculptures to obey, the scale tips toward a snow rabbit, and she sulks off into the snow. Walk-on: Piplup sliding on the ice. |
| 61 | Yuki and the Hokkaido Snow Lanterns | Calcifer | Lives in one ice lantern, complaining he's the only flame in a city of ice: "May all your bacon burn." Walk-on: Wooper in the canal. |
| 62 | Tako and Yaki and the Okinawa Blue Sea | Porco Rosso | Scarlet seaplane lands in the shallows; the pig pilot wants one takoyaki, gets two. Walk-on: Oshawott swimming past. |
| 63 | Tai Taiyaki and the Okinawa Coral Reef | Lapras | Surfaces under the aquarium's window, gives the whole tank a tour from outside. Walk-on: Gyarados grinning in the big tank. |
| 64 | Pepper-kun and the Osaka Food Street | Jotaro and Star Platinum | Strikes a dramatic pose under the neon; the glowing spirit behind him poses too; Pika the Kushikatsu copies them. Walk-on: Vegeta disapproving of takoyaki. |
| 65 | Coro Korokke and the Hokkaido Potato Fields | Walking Mushroom + Mandrake | A mushroom pretends to be a potato in the row; Spud pulls a mandrake instead and it shrieks the length of the field. Walk-on: Bulbasaur in the potato row. |
| 66 | Niko Nigiri and the Tsukiji Morning Market | Rock Lee | Does five hundred laps of the market before dawn, shouting about youth, bowing to every fish stall he passes. Walk-on: Krillin bargaining. |
| 67 | Momo Mochi and the New Year Mochi Pounding | Goku on Nimbus | Eats the mountain of mochi as fast as it's pounded; Nimbus refuses to let anyone else ride. Walk-on: Majin Buu eating mochi. |
| 68 | Dai Daruma and the New Year First Shrine Visit | Shenron | Rises from the shrine when they clap; grants one wish; Dai wishes for a snack for Coro, who is starving. Walk-on: Lucario meditating at the gate. |
| 69 | Tama Onigiri and the Bean-Throwing Day | Bowser | Volunteers as the oni, loves being pelted with beans, asks for seconds. Walk-on: Inosuke cheering in his boar mask. |
| 70 | The Dango Three and the Doll Festival | Hello Kitty | Sits on the doll steps posing as a doll; waves when nobody is looking; Shiro notices. Walk-on: Kuromi sulking on the step. |
| 71 | Tai Taiyaki and the Children's Day Carp | All Might | "I AM HERE!" lifts the fallen carp pole with a laugh, flexes, and the pole bends. Walk-on: Deku saluting All Might. |
| 72 | Mero Melonpan and the Tanabata Wishes | Shinji Ikari, Asuka Langley Shikinami and Mari Illustrious Makinami with Unit-01 (Evangelion) | Three pilots argue over one wish-bamboo: Asuka wants the biggest wish, Mari laughs and hangs her own upside down, Shinji apologizes to the bamboo; behind them the purple giant crouches holding the whole bamboo grove steady like a bouquet. Walk-on: Warawara rising to the stars. |
| 73 | Maru Matcha and the Moon-Viewing Night | Sailor Moon | Lands: "In the name of the moon, I'll..." sees the dango. "...have one. Or six." Walk-on: Clefairy dancing at the moon. |
| 74 | Momo Mochi and the Warm Winter Solstice Bath | Pen Pen (Evangelion) | A warm-water penguin with a red crest waddles into the yuzu bath with his own towel, sinks to the eyes, and refuses to leave; the yuzu bob around him like ducks. Walk-on: Kapibarasan in the bath. |
| 75 | Kuma Kuri and the Friendly Forest Spirit | Puck (Re:Zero) | A small grey cat spirit yawns out of a tree hollow, Mori's much smaller neighbour, and freezes the pond by accident while stretching. Walk-on: Arrietty under a leaf. |
| 76 | Maru Matcha and the Tea-Loving Tanuki | Ojisan and the Elf (Uncle from Another World) | A scruffy man in a tracksuit steps out of a glowing portal, casts a sparkly spell to give Pon the tanuki a perfect disguise, and it turns Pon into a teapot; the Elf insists she only followed him to say the spell was wrong, blushing. Walk-on: a Pom Poko tanuki juggling leaves. |
| 77 | Tama Onigiri and the Shy Kappa of the Pond | Squirtle | Pulls into its shell at exactly the same moment Kappy hides; two shy shells side by side. Walk-on: Shippo the fox-kit. |
| 78 | Dora Dorayaki and the Lantern-Lighting Spirits | Saitou, Raelza, Morlock and Lafanpan (Handyman Saitou in Another World) | A handyman in a tool belt fixes a wobbly lantern post with one turn of a screwdriver; Morlock the ancient wizard forgets the light spell halfway and lights his own beard instead; Lafanpan the tiny fairy charges everyone a coin for watching; Raelza the knight holds the ladder and glares at the river. Walk-on: Litwick lighting itself. |
| 79 | Neko-Pan and the Lucky Beckoning Spirits | The Baron | A statue among the cat statues steps down, bows, and offers tea as if he owned the shrine. Walk-on: Jibanyan among the cats. |
| 80 | Mero Melonpan and the Dream-Eating Baku | Jigglypuff | Sings everyone to sleep inside the dream, puffs up when nobody listens, doodles on the baku. Walk-on: Drowzee peeking in. |
| 81 | Pock Ramune and the Summer Cicada Chorus | Kakashi and Pakkun | Reads under the tree, scores the cicada chorus "seven out of ten"; Pakkun gives it a four. Walk-on: Agumon listening. |
| 82 | Kuma Kuri and the Rice-Paddy Fireflies | Gamakichi | Puffs in on smoke to visit Mister Croak; the two toads argue about whose pond is bigger. Walk-on: Teto on Kuma's shoulder. |
| 83 | Sora Soft-Cream and the Lavender Fields | Vash the Stampede (Trigun) | A tall man in a long red coat wanders out of the lavender hopelessly lost, asking for donuts; he sneezes a purple cloud of pollen, flashes a peace sign, and trips over his own coat. Walk-on: Sylveon ribbons in the lavender. |
| 84 | Tama Onigiri and the Rice-Harvest Helpers | Marin Kitagawa and Wakana Gojo (My Dress-Up Darling) | Marin arrives in a scarecrow costume Wakana sewed overnight and poses in the paddy; the Heron inspects the stitching; Wakana apologizes for a loose button while the Field Mice applaud the outfit. Walk-on: the Grey Heron argues with the Heron. |
| 85 | Maru Matcha and the Tea Hill Morning | Mash Burnedead (Mashle) | A blank-faced boy with huge muscles lifts the entire morning tea harvest in one arm while looking for cream puffs; asked how he used magic, he says he used arms. Walk-on: Tails flying over the rows. |
| 86 | Tako and Yaki and the Koi Pond Friends | Mob and Reigen (Mob Psycho 100) | Reigen the fake psychic offers to 'exorcise' the koi pond for a fee and massages a rock; Mob quietly floats every koi out of the water in a gentle ring and apologizes to each fish. Walk-on: Goldeen among the koi. |
| 87 | Yuki and the Snow-Country Village | Edward and Alphonse Elric (Fullmetal Alchemist) | Someone calls Ed small; he explodes, claps his hands and alchemizes a snow wall that falls on him; Alphonse shelters a kitten in his chest plate and apologizes for his brother. Walk-on: Alolan Vulpix in the snow. |
| 88 | Pepper-kun and the Midnight Garage | Mothra | Lands on the garage roof; the tiny moth guest is star-struck; the wings fan the forge. Walk-on: a Tachikoma in the garage. |
| 89 | Niko Nigiri and the Neon Car Meet | Dom and the Charger | Revs once and the lot shakes: "I live my life a quarter mile at a time." Kei: "I live mine at putt-putt." Walk-on: Kaneda's red bike parked. |
| 90 | The Sushi-ya Express and the Touge Sunrise | The tofu AE86 and Takumi | Drifts past in the fog on the hairpins, tofu box steady; Kei beeps along to the music. Walk-on: Turbo Granny racing on all fours. |
| 91 | Tako and Yaki and the Time-Attack Circuit | Tanya the Evil (Saga of Tanya the Evil) | A tiny blond officer flies in on a glowing orb, salutes, declares the lap times inefficient, files a complaint with the lantern-keeper, and flies off muttering about paperwork. Walk-on: a Kamen Rider on a bike. |
| 92 | Dai Daruma and the Lucky Dashboard Charm | Josuke and Crazy Diamond (JoJo's Bizarre Adventure) | The dashboard charm cracks; a pompadoured teen's glowing pink spirit taps it and it is good as new; someone compliments his hair and he poses for a full minute. Walk-on: Shy Guy on the back seat. |
| 93 | Coro Korokke and the Neighborhood Cleanup Day | Levi (Attack on Titan) | Arrives with a mop and a cravat over his nose, declares the lane filthy, cleans one cobblestone to a mirror shine, then the rest. Walk-on: Waddle Dee carrying a bin. |
| 94 | Niko Nigiri and the Omiyage Souvenir Quest | Naofumi, Raphtalia and Filo (The Rising of the Shield Hero) | Naofumi's shield turns into a souvenir-shop bag, Raphtalia wants one of everything, and Filo the giant white bird eats the display stand; Goma charges them for the stand. Walk-on: Stark trembling at the chest. |
| 95 | Rin Ramen and the Farewell Feast | Tanjiro, Nezuko, Zenitsu and Inosuke (Demon Slayer) | Inosuke eats the feast in his boar mask, Zenitsu cries about leaving, Nezuko hums from her box, and Tanjiro smells the broth and bows to Rin like a master. Walk-on: Usopp telling a tall tale. |
| 96 | Tai Taiyaki and the Last Sunrise by the Sea | Sung Jinwoo and Igris (Solo Leveling) | A quiet man says 'Arise' and a line of soft purple shadow soldiers stand along the dawn beach to shield the scarf from the gull; Igris the shadow knight salutes the sunrise. Walk-on: Piplup on the dawn sand. |
| 97 | Maru Matcha and the Thank-You Tea | Violet Evergarden | Sets up a typewriter to type the perfect thank-you; Maru pours tea instead; Violet decides tea is a letter too. Walk-on: Fern pouring tea. |
| 98 | Dai Daruma and the Second Painted Eye | Gojo (Jujutsu Kaisen) | Kneels to watch Dai's eye get painted, lifts his blindfold a finger-width: "Nice eye." Lets it drop. Walk-on: Haro cheering. |
| 99 | Momo Mochi and the Final Shinkansen Home | Astro Boy | Flies alongside the train window waving; races it; loses politely; salutes. Walk-on: Tails racing the train. |
| 100 | The Grand Rising-Sun Reunion | Ash Ketchum and Pikachu (Pokémon) | Climbs the hill backwards cap-first, Pikachu on his shoulder; Pikachu sparks the sunrise a second early. Walk-on: Soot Sprites with star candy for everyone. |

## Assignments — Hawaii (stories 3–50)

| # | Story | Cameo | Gag seed |
|---|---|---|---|
| 3 | Malia the Malasada and the Warm Morning Batch | Totoro | Presses his whole face to the bakery window wanting sugar; one sneeze blows the sugar everywhere. Walk-on: Hamtaro on the sugar tray. |
| 4 | Musubi Manu and the Bento Backpack Mix-Up | Stitch | Grabs the backpack thinking it's lunch, four arms, "Ohana?" Adds a fourth wrong backpack. Walk-on: Meowth with the wrong bag. |
| 5 | Poke Pua and the Perfect Bowl | Maomao (The Apothecary Diaries) | Tastes the poke one cube at a time, muttering about poison, eyes sparkling; declares it dangerously delicious. Walk-on: Sanji admiring the bowl. |
| 6 | Saimin Sam and the Great Noodle Knot | Kirito (Sword Art Online) | Draws two swords and slices the noodle knot into perfect bite-size pieces, then apologizes for being dramatic. Walk-on: Choji slurping. |
| 7 | The Whole Gang Meets Honu Haupia | Lapras | Surfaces in the tide pool; two elders greet each other very, very slowly. Walk-on: Wooper in the tide pool. |
| 8 | Manapua Mano and the Midnight Snack Mission | Pac-Man | Chomps down the dark alley eating every pellet-shaped snack, "waka waka", Manapua chasing. Walk-on: Shikamaru asleep on a stall. |
| 9 | Lilikoi Lani and the Sour Surprise | Team Rocket (Jessie, James, Meowth) | Pranksters arrive to out-prank Lani, eat the sour one themselves, and blast off over the garden wall. Walk-on: Psyduck confused by sour. |
| 10 | Mac the Macadamia and the Little Big Rescue | Edward Elric (Fullmetal Alchemist) | Hears "small" from the cliff, explodes with rage, then claps and makes a stone staircase; small and mighty, twice. Walk-on: Waddle Dee carrying a nut. |
| 11 | Kalua the Pig and the First Big Luau | Senku (Dr. Stone) | Measures the imu with a stick thermometer: "Ten billion percent not ready." Kalua: "Low and slow." Walk-on: Majin Buu at the pit. |
| 12 | Poi Popo and the Old Island Stories | Tanjiro and Nezuko (Demon Slayer) | Tanjiro smells the poi from the road; Nezuko peeks from her box to listen to the old stories and hums. Walk-on: Fern under the banyan. |
| 13 | Pua the Pineapple and the Crooked Crown | Princess Peach | Offers a loaner crown; it is far too big; two crooked crowns are better than one. Walk-on: Vegeta judging crowns. |
| 14 | Lani the Loco Moco and the Lazy Sunday Feast | Umaru (Himouto! Umaru-chan) | A tiny hamster-hooded girl out-lazies Lani from the next booth with a cola and a comic; Lani is humbled. Walk-on: Slowpoke on a stool. |
| 15 | The Lei of Many Flowers | Pikmin | Carry flowers in a line of tiny plant people and weave the wrong lei entirely. Walk-on: Sylveon ribbons in the lei. |
| 16 | The Hula Everyone Forgot | Mob (Mob Psycho 100) | Joins the hula with the Body Improvement Club's effort, hits one hundred percent emotion, floats slightly off the grass. Walk-on: Clefairy dancing along. |
| 17 | Musubi Manu and the Grandparent's Recipe | Calcifer | In the stove, refuses to heat anything until told the recipe; sulks at "a pinch of love". Walk-on: Togepi in the mixing bowl. |
| 18 | The Luau Where Everyone Belonged | No-Face | Arrives silent and gold-handed; is handed a plate, a lei and a seat; makes a tiny happy "ah". Walk-on: Pen Pen at the luau. |
| 19 | Sailing to Maui on a Coconut Canoe | Heihei | Stows away in the canoe, pecks the coconut hull, stares into the sea, "bawk". Walk-on: Oshawott swimming alongside. |
| 20 | The Road to Hana and the Slow Honu Way | Fel the Fenrir (Campfire Cooking in Another World) | A silver-white wolf bigger than the one-lane bridge lies across it and declares a snack toll; every traveler pays in snacks, he wants seconds, and the slow way becomes the only way. Walk-on: Dedenne on the bridge rail. |
| 21 | Sunrise on Haleakala | Spike Spiegel and the Swordfish II (Cowboy Bebop) | A red fighter ship lands on the summit; Spike came for the sunrise, shrugs, and shares his bell peppers. Walk-on: Dragonite above the crater. |
| 22 | Kauai, the Garden Island Mystery | Korok | "Yahaha! You found me!" under every fern; the mystery has a very small culprit. Walk-on: Eevee in the ferns. |
| 23 | The Waimea Canyon Echo | Megumin | One "EXPLOSION!" into the canyon; the echo comes back nine times; she naps. Walk-on: Zenitsu screaming the echo back. |
| 24 | Molokai and the Friendly Quiet | Rilakkuma | Already lying on the quiet beach; the quietest thing on the quietest island. Walk-on: Kapibarasan in the shallows. |
| 25 | Lanai, the Pineapple Island Homecoming | Donkey Kong | Thunders through the field, confused that these bananas are spiky, pounds his chest anyway. Walk-on: Bulbasaur in the field. |
| 26 | Big Island, Black Sand and Green Sand | Godzilla | Rises from the Pacific to warm his belly on the black sand; the whole beach tilts. Walk-on: Gyarados in the surf. |
| 27 | The Stars Over Mauna Kea | Strike Gundam and Kira | Descends from orbit beside the telescopes; Kira: "Sorry. Just passing through." Walk-on: Haro bouncing on the dome. |
| 28 | Poke Pua Learns to Surf | Aerial and Suletta Mercury (The Witch from Mercury) | A sleek white robot lands in the shallows; its floating shield-petals line up as a wobbly surfboard and Suletta tries to ride one, stammering apologies to every wave: if you run you gain one, if you go forward you gain two, if you fall off you gain a mouthful of sea. Walk-on: Piplup bellyboarding. |
| 29 | The Penguins Who Came to Surf | Natsu and Happy (Fairy Tail) | Natsu gets motion sick on a surfboard before it touches water; Happy the blue cat flies him back to the sand. Walk-on: Mudkip in the shore break. |
| 30 | The Big Wave of the North Shore | Ponyo | Runs along the top of the giant wave on the backs of fish, giggling: "Ponyo loves waves!" Walk-on: Wooper riding a ripple. |
| 31 | Honu Haupia and the Gentle Reef | Magikarp | Flops through the reef splashing everyone, trying very hard to be a fish. Walk-on: Goldeen in the reef. |
| 32 | The Dolphins of the Bay | Porco Rosso | Scarlet seaplane lands in the bay and races the dolphins; the dolphins win; the pig salutes. Walk-on: Popplio blowing bubbles. |
| 33 | The Whale's Winter Song | Hatsune Miku | Sings one note at the whales; the whales sing back; the whole cove harmonizes. Walk-on: Wailord surfacing like a blimp. |
| 34 | Musubi Manu and the Tide Pool Treasures | Frieren and a Mimic (Frieren: Beyond Journey's End) | Frieren spots a barnacled treasure chest in the tide pool, opens it calmly, and it eats her head; she waits inside it, mildly annoyed, while Manu and Niu decide whether that counts as a treasure. Walk-on: Pyukumuku flung from the pool. |
| 35 | The Night the Sea Glowed | Haku | The white dragon flows through the glowing surf, trailing blue sparks. Walk-on: Alolan Raichu surfing the glow. |
| 36 | The Glow of Pele | Charmander | Meets the lava glow and is overjoyed to find something warmer than its tail. Walk-on: Litten warming its paws. |
| 37 | How the Island Was Born | Kaiju No. 8 | A tall blue-black kaiju with glowing eyes rises from the lava field, very polite, very confused about where it is. Walk-on: Alolan Exeggutor on the new land. |
| 38 | The Warm Black Sand Beach | Yoshi | Buries a spotted egg in the warm sand to keep it cosy, then a second, then can't find them. Walk-on: Komala asleep on a log. |
| 39 | The Rainforest Where the Rain Sings | Inuyasha | Bounds through the rain in his red robe, dog ears flattened and soaking, sulking that his ears are wet. Walk-on: Rowlet turning its head. |
| 40 | Macadamia Mac and the Mountain Orchard | Doraemon | A tree-shaking gadget shakes every nut off every tree at once; a nut avalanche. Walk-on: Bewear hugging a tree. |
| 41 | Pua the Pineapple and the Field of Gold | Mario Kart (Mario, Luigi, Bowser) | A kart race tears through the rows; Pua's crown becomes the trophy; it is returned. Walk-on: Bounsweet bouncing down a row. |
| 42 | The Makai Tide and the Mauka Stream | Rimuru | Flows down the mountain stream as a slime, meets the tide, isn't sure which way is home. Walk-on: Mudkip in the stream. |
| 43 | Dole Whip Dani and the Melting Day | Shoto Todoroki (My Hero Academia) | Raises an ice wall for shade with his right side; his left side steams; Dani melts anyway from laughing. Walk-on: Alolan Vulpix in the shade. |
| 44 | The Lost Little Malasada | Isabelle | Lost-and-found announcements from a clipboard at the fair; announces the wrong doughnut. Walk-on: Mimikyu also lost. |
| 45 | Musubi Manu and the First Day of School | Anya and Bond | The new classmate reads everyone's mind: "waku waku!" Bond is too big for the door. Walk-on: Pichu in the back row. |
| 46 | Lilikoi Lani and the Aloha Friday | Bocchi (Bocchi the Rock) | Plays a blistering guitar solo from inside a cardboard box on the block-party stage. Walk-on: Oricorio dancing. |
| 47 | Manapua Mano and the Quietest Question | Komi (Komi Can't Communicate) | Writes nothing, says nothing, and asks the quietest question of all with one look and a tiny nod. Walk-on: Dimple floating smugly. |
| 48 | Kamaron the Garlic Shrimp and the Cheering Truck | Dom and the Charger | Joins the truck convoy: "A quarter mile at a time." Learns the word "ohana". Walk-on: a Molcar in the convoy. |
| 49 | Poi and the Volcano's Quiet Glow | Minilla | The baby kaiju blows a smoke ring at the glow and hiccups; Tūtū Poi tells him to sit nicely. Walk-on: Slugma on the warm rock. |
| 50 | The Grand Aloha Reunion | Stitch | Arrives for the reunion with a lei on every arm: "Ohana." Nobody argues. Walk-on: Soot Sprites with leis. |

## Appearance count

Three or fewer across both arcs for every main cameo; walk-ons are spread once or twice each (Dedenne and Mew are
plain small Pokémon: a tiny orange mouse with whisker antennae; a small pink floating cat-like creature). Totoro: Japan 29, 75; Hawaii 3. Godzilla: Japan 33, 100;
Hawaii 26. Gundam RX-78-2: Japan 28, 98. Kirby: Japan 32, 93. No-Face: Japan 54; Hawaii 5, 18. All others once or twice.
