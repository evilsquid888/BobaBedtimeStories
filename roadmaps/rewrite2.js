export const meta = {
  name: 'rewrite-differentiated',
  description: 'Rewrite 33 stories with fresh distinct premises to remove thematic repetition',
  phases: [{ title: 'Rewrite stories' }],
}
const SPECS = [{"collection": "taiwan", "number": 69, "newTitle": "Story 69: Candied Tomato & the Is-It-Fruit-or-Candy Riddle", "newSlug": "candied-tomato-and-the-fruit-or-candy-riddle", "mainCharacter": "Mì Fānqié (Candied Tomato) — cherry tomatoes on a stick in a glossy crackly sugar shell dusted with sour plum powder, giggly and tangy-sweet", "guests": "None", "setting": "A buzzing Tainan night-market 'guess the snack' game stall", "theme": "Joy doesn't care what category you fit in", "spotlightTerm": "番茄", "spotlightRomanization": "fānqié", "spotlightMeaning": "tomato", "premise": "When a night-market game declares snacks must be either 'fruit' or 'candy,' poor Candied Tomato doesn't fit either box and feels left out — until she proves that the most delightful treats are the ones that are happily, deliciously both.", "arc": "Sweet Encore", "spotlightLabel": "Mandarin Spotlight", "path": "stories/69-candied-tomato-and-the-fruit-or-candy-riddle.md"}, {"collection": "taiwan", "number": 83, "newTitle": "Story 83: Brown Sugar & the Happy Little Mistake", "newSlug": "brown-sugar-and-the-happy-little-mistake", "mainCharacter": "Hēi Táng (Brown Sugar) — a warm dark-amber sugar cube with a cozy molasses glow, kindly and a little clumsy", "guests": "None", "setting": "A bubbling boba-syrup kitchen at dusk", "theme": "A little imperfection can make you richer, not ruined", "spotlightTerm": "黑糖", "spotlightRomanization": "hēitáng", "spotlightMeaning": "brown sugar", "premise": "Brown Sugar is mortified when he bubbles a moment too long and turns a deeper, darker, slightly-burnt shade — until everyone tastes the new caramel-deep flavor and discovers his 'mistake' is the most delicious syrup the tea shop has ever poured.", "arc": "Sweet Encore", "spotlightLabel": "Mandarin Spotlight", "path": "stories/83-brown-sugar-and-the-happy-little-mistake.md"}, {"collection": "taiwan", "number": 89, "newTitle": "Story 89: Sun Cake & the Trail of Golden Crumbs", "newSlug": "sun-cake-and-the-trail-of-golden-crumbs", "mainCharacter": "Tàiyáng Bǐng (Sun Cake) — a flaky golden Taichung pastry shaped like a little sun, sheds crumbs everywhere, sunny and shy", "guests": "None", "setting": "The winding lanes of old Taichung at golden hour", "theme": "The little bits you scatter can lead friends right to you", "spotlightTerm": "太陽餅", "spotlightRomanization": "tàiyáng bǐng", "spotlightMeaning": "sun cake", "premise": "Flaky Sun Cake is embarrassed that she leaves a trail of crumbs everywhere she goes — until a lost, lonely little friend follows that exact golden trail straight to her and a warm circle of new friends.", "arc": "Sweet Encore", "spotlightLabel": "Mandarin Spotlight", "path": "stories/89-sun-cake-and-the-trail-of-golden-crumbs.md"}, {"collection": "hawaii", "number": 49, "newTitle": "Story 49: Poi and the Volcano's Quiet Glow", "newSlug": "poi-and-the-volcanos-quiet-glow", "mainCharacter": "Poi — a smooth, soft, lavender-grey bowl of pounded taro, humble and calm with a gentle smile", "guests": "None", "setting": "A grassy slope on the Big Island at night, the volcano glowing softly far away", "theme": "Wonder is sweetest snuggled close to the ones you love", "spotlightTerm": "hōkū", "spotlightRomanization": "HOH-koo", "spotlightMeaning": "star", "premise": "Humble little Poi worries he's too plain to matter at the lively beach parties, until a quiet starlit night watching the volcano's faraway glow shows him that calm, cozy wonder shared with ohana is its own kind of magic.", "arc": "Volcano & Land", "spotlightLabel": "Hawaiian Spotlight", "path": "hawaii/stories/49-poi-and-the-volcanos-quiet-glow.md"}, {"collection": "costa-rica", "number": 25, "newTitle": "Story 25: Rana and the Rainforest Choir", "newSlug": "rana-and-the-rainforest-choir", "mainCharacter": "Rana — a tiny bright red-eyed tree frog with blue-striped legs, shy but with a surprising croak", "guests": "Don Café", "setting": "The Monteverde rainforest at nightfall, full of dripping leaves", "theme": "Every small voice helps complete the song", "spotlightTerm": "canción", "spotlightRomanization": "kahn-SYOHN", "spotlightMeaning": "song", "premise": "Shy little Rana thinks her croak is too small and silly to matter, until a rainy-night rainforest concert teaches her that every tiny voice — crickets, raindrops, and one little frog — is exactly what makes the whole jungle's song complete.", "arc": "Arc 2 — Rainforest Friends", "spotlightLabel": "Spanish Spotlight", "path": "costa-rica/stories/25-rana-and-the-rainforest-choir.md"}, {"collection": "costa-rica", "number": 10, "newTitle": "Story 10: Tato the Patacón and the Brave First Dip", "newSlug": "tato-the-patacon-and-the-brave-first-dip", "mainCharacter": "Tato the Patacón — a twice-fried green plantain round, crispy-golden and chunky, cautious and proud of staying crunchy", "guests": "None", "setting": "A sunny Pacific-coast soda (little eatery) by the beach", "theme": "Trying something new can be the best crunch of all", "spotlightTerm": "valiente", "spotlightRomanization": "bah-lee-EN-teh", "spotlightMeaning": "brave", "premise": "Crunchy Tato refuses to be dipped in anything new for fear of going soggy, until a gentle black-bean dip and his cheering friends help him take one brave dunk — and discover that being brave opens up a whole world of delicious.", "arc": "Arc 1 — Pura Vida Town (Home & Family)", "spotlightLabel": "Spanish Spotlight", "path": "costa-rica/stories/10-tato-the-patacon-and-the-brave-first-dip.md"}, {"collection": "costa-rica", "number": 41, "newTitle": "Story 41: Cajeta and the Grandmother's Recipe", "newSlug": "cajeta-and-the-grandmothers-recipe", "mainCharacter": "Cajeta the Coconut Fudge — soft golden coconut-milk fudge balls dusted with toasted coconut, warm and a little forgetful", "guests": "None", "setting": "A cozy village kitchen during a family gathering", "theme": "The sweetest recipes are kept in our hearts, not on paper", "spotlightTerm": "abuela", "spotlightRomanization": "ah-BWEH-lah", "spotlightMeaning": "grandmother", "premise": "When the only written copy of Abuela's beloved coconut-fudge recipe goes missing before the family party, Cajeta panics — then learns the recipe was never really on paper at all; it lives in her hands, her nose, and everyone's happy memories.", "arc": "Arc 5 — Festivals & Family", "spotlightLabel": "Spanish Spotlight", "path": "costa-rica/stories/41-cajeta-and-the-grandmothers-recipe.md"}, {"collection": "japan", "number": 45, "newTitle": "Story 45: Tama Tamago and the Conveyor-Belt Parade", "newSlug": "tama-tamago-and-the-conveyor-belt-parade", "mainCharacter": "Tama Tamago — a sweet, golden, pillowy egg (tamago) nigiri with a little seaweed belt, gentle and easily overlooked", "guests": "Niko Nigiri", "setting": "A spinning conveyor-belt sushi restaurant", "theme": "Simple and kind never goes out of style", "spotlightTerm": "優しい", "spotlightRomanization": "yasashii", "spotlightMeaning": "kind / gentle", "premise": "Plain little Tama Tamago feels invisible riding the sushi conveyor belt beside the flashy, fancy plates — until a tired, overwhelmed customer reaches past all the dazzle for the one simple, gentle, comforting bite, and Tama learns soft kindness is its own kind of special.", "arc": "Arc 6 — Foodie Street Eats", "spotlightLabel": "Japanese Spotlight", "path": "japan/stories/045-tama-tamago-and-the-conveyor-belt-parade.md"}, {"collection": "japan", "number": 31, "newTitle": "Story 31: Anko and the Sharing Bench", "newSlug": "anko-and-the-sharing-bench", "mainCharacter": "Anko — a round, soft, sweet red-bean bun with a shiny top and a generous heart", "guests": "None", "setting": "A sunny park bench by a koi pond", "theme": "A snack shared is a snack doubled", "spotlightTerm": "分ける", "spotlightRomanization": "wakeru", "spotlightMeaning": "to share", "premise": "Anko the red-bean bun saves the comfiest park bench all for himself and his snack, then slowly discovers that every friend he scoots over to make room for makes the bench cozier and the afternoon sweeter.", "arc": "Arc 5 — Four Seasons: Hanami and Hanabi", "spotlightLabel": "Japanese Spotlight", "path": "japan/stories/031-anko-and-the-sharing-bench.md"}, {"collection": "japan", "number": 19, "newTitle": "Story 19: Sora Soft-Cream and the Lake That Held Mount Fuji", "newSlug": "sora-soft-cream-and-the-lake-that-held-mount-fuji", "mainCharacter": "Sora the Soft-Cream — a tall, swirly, pale-vanilla soft-serve cone with a gentle wobble, dreamy and thoughtful", "guests": "None", "setting": "The calm shore of Lake Kawaguchi with Mount Fuji reflected in the water", "theme": "Sometimes the best view is the one reflected back", "spotlightTerm": "鏡", "spotlightRomanization": "kagami", "spotlightMeaning": "mirror / reflection", "premise": "Sora is sad she's too short and swirly to climb tall Mount Fuji like the big kids — until the glass-calm lake shows the whole mountain upside-down at her feet, and she learns there's more than one beautiful way to see something grand.", "arc": "Arc 3 — Onsen and Mountains", "spotlightLabel": "Japanese Spotlight", "path": "japan/stories/019-sora-soft-cream-and-the-lake-that-held-mount-fuji.md"}];
phase('Rewrite stories')

const STYLE = `You write ONE cozy bedtime story for a 9-YEAR-OLD GIRL (ages 9-12) in the "Boba Bedtime Stories" style.
TONE: warm, playful, silly, cozy — Roald Dahl meets a vibrant food market. A laugh line in every major scene; a warm narrator who occasionally winks at the reader.
AGE SAFETY: nothing genuinely scary, sad, violent, or dark. Gentle cute spookiness only. Any "becoming a treat" moment must be JOYFUL and proud, never frightening.
LENGTH: 1800-2000 words of story. Fun within the first ~150 words.
VOCAB: weave in 3-5 local-language terms naturally; on FIRST use format as **native term** (romanization) = English. The header spotlight term is the key word.
This is a REWRITE to make the story DISTINCT from others — fully commit to the NEW premise, character, and lesson below. Give the main character a vivid physical description tied to its real food.`

const RET = { type:'object', additionalProperties:false, required:['path','title','wordCount','ok'],
  properties:{ path:{type:'string'}, title:{type:'string'}, wordCount:{type:'integer'}, ok:{type:'boolean'} } }

function prompt(s){
  const num = s.number
  const title = s.newTitle.replace(/^Story \d+:\s*/,'')
  return `${STYLE}

WRITE THIS STORY (a rewrite — ignore any previous version):
- Number: ${num}
- Title: ${title}
- Main Character: ${s.mainCharacter}
- Guest Characters: ${s.guests || 'None'}
- Setting: ${s.setting}
- Theme (must come through clearly and is DISTINCT from other stories): ${s.theme}
- ${s.spotlightLabel} term: ${s.spotlightTerm} (${s.spotlightRomanization}) = ${s.spotlightMeaning}
- Premise: ${s.premise}
- Arc: ${s.arc}
- EXACT file path to Write: ${s.path}

Use the Write tool to create the file at that exact path with this structure:

# Story ${num}: ${title}

**Main Character:** ${s.mainCharacter}
**Guest Characters:** ${s.guests || 'None'}
**Setting:** ${s.setting}
**Theme:** ${s.theme}
**${s.spotlightLabel}:** ${s.spotlightTerm} (${s.spotlightRomanization}) = ${s.spotlightMeaning}

---

<opening hook ~150 words>

<main narrative ~1500 words>

<warm ending>

---

## Goodnight Blessing
<soft sleepy closing ending with "Goodnight.">

## AI Image Prompts
1. <key scene>
2. <character portrait>
3. <closing scene>

Then return {path, title, wordCount, ok}.`
}

const results = await parallel(SPECS.map(s => () =>
  agent(prompt(s), { label:`rewrite:${s.collection}-${s.number}`, phase:'Rewrite stories', schema:RET })
    .then(r=>r).catch(()=>null)
))
const ok=results.filter(Boolean)
const failed=SPECS.filter((s,i)=>!results[i]).map(s=>`${s.collection}-${s.number}`)
log(`Rewrote ${ok.length}/${SPECS.length}; failed=[${failed.join(',')}]`)
return { wrote: ok.length, total: SPECS.length, failed }
