export const meta = {
  name: 'howto-planning',
  description: 'Plan ~30 how-to bedtime stories that teach making foods/crafts/activities',
  phases: [{ title: 'Plan how-to roadmap' }],
}
phase('Plan how-to roadmap')

const SCHEMA = {
  type:'object', additionalProperties:false, required:['collection','newCharacters','stories'],
  properties:{
    collection:{type:'string'},
    newCharacters:{type:'array', items:{type:'object', additionalProperties:false,
      required:['name','food','appearance','voice','catchphrase'],
      properties:{name:{type:'string'},food:{type:'string'},appearance:{type:'string'},voice:{type:'string'},catchphrase:{type:'string'}}}},
    stories:{type:'array', items:{type:'object', additionalProperties:false,
      required:['number','slug','title','mainCharacter','type','guests','setting','theme','spotlightTerm','spotlightRomanization','spotlightMeaning','howToMake','steps','premise','arc'],
      properties:{
        number:{type:'integer'}, slug:{type:'string'}, title:{type:'string'},
        mainCharacter:{type:'string'}, type:{type:'string',enum:['new','existing']},
        guests:{type:'string'}, setting:{type:'string'}, theme:{type:'string'},
        spotlightTerm:{type:'string'}, spotlightRomanization:{type:'string'}, spotlightMeaning:{type:'string'},
        howToMake:{type:'string', description:'the thing being made/done, e.g. "boba milk tea"'},
        steps:{type:'array', items:{type:'string'}, description:'5-8 simple, accurate, kid-friendly steps in order'},
        premise:{type:'string'}, arc:{type:'string'} }}},
  },
}

const prompt = `Plan a NEW cozy bedtime "HOW-TO" story collection for a 9-YEAR-OLD GIRL (ages 9-12), in the warm, silly "Boba Bedtime Stories" style. Exactly 30 stories, numbered 1-30.

THE TWIST: each story TEACHES how to make a food/dessert or do a fun activity, woven INTO a cozy adventure. The expert character guides a friend (and the reader) through the REAL steps, which must be accurate but simplified and safe. For any hot/sharp/fryer step, the steps should say to "ask a grown-up to help." End each story with the treat finished and shared.

MUST INCLUDE these topics (plus more): how to make bread, how to make shaved ice, how to make bing tang hu lu (冰糖葫蘆 candied hawthorn/strawberries), how to make boba milk tea, how to make several Japanese foods (sushi/onigiri/ramen/takoyaki/taiyaki/mochi), how to make beef noodle soup, how to make Taiwanese foods & desserts (pineapple cake, scallion pancake, tangyuan, douhua, egg waffle, sesame ball, grass jelly), and how to go shrimp fishing (Taiwan-style 釣蝦 indoor shrimp fishing). Fill the rest with other fun how-tos (e.g. how to make dumplings, mochi, matcha, malasadas, spam musubi, dorayaki, a paper lantern, sugarcane juice, etc.). Each story teaches a DIFFERENT thing — no duplicate how-tos.

CHARACTERS: REUSE the natural expert from the existing universe wherever possible (the food teaches its own recipe): Boba (tapioca pearl)->boba; Beef Noodle (Niu Niu)->beef noodle soup; Shaved Ice->shaved ice; Mochi->mochi; Egg Waffle->egg waffle; Pineapple Cake->pineapple cake; Tangyuan->tangyuan; Douhua->douhua/tofu pudding; Scallion Pancake->scallion pancake; Sesame Ball->sesame ball; Grass Jelly->grass jelly; Sweet Potato; Red Bean. Japanese cast: Niko Nigiri->sushi; Rin Ramen->ramen; Momo Mochi->mochi; Tako & Yaki->takoyaki; Tai Taiyaki->taiyaki; Dora Dorayaki->dorayaki. Invent NEW characters where there is no natural expert (e.g. a Bread/Bao baker, a Bing Tang Hu Lu candied-fruit character, a friendly Shrimp guide for shrimp fishing, a Malasada, a Matcha whisk-friend).

For each story give: number, kebab-case slug (no number prefix; e.g. "boba-and-how-to-pour-the-perfect-pearls"), a fun title (NOT just "How To Make X" — make it a story title), main character, type (new/existing), guests, setting, theme/lesson, a language Spotlight (use the right language for the dish: Mandarin / Japanese / etc.), howToMake, 5-8 accurate simple steps, a 1-2 sentence premise, and an arc grouping (e.g. "Sweet Treats", "Savory Kitchen", "Japanese Kitchen", "Night-Market Fun", "Crafts & Activities").

Keep it cozy, funny, bedtime-safe. Return all 30.`

const r = await agent(prompt, { label:'plan:how-to', phase:'Plan how-to roadmap', schema:SCHEMA })
log(`how-to plan: ${r.stories?.length} stories, ${r.newCharacters?.length} new characters`)
return r
