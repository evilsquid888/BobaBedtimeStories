"""Places that recur across the 24 Days of Xmas, so they look the same in every video.

A spec imports what it needs (build.py puts this folder on the path):

    from places import DOORWALL, LANE_DAY, LANE_NIGHT, bunk

and adds its own new place for the day's adventure. Shots in LANE_NIGHT and
bunk(...) must be marked "time": "night"; DOORWALL and LANE_DAY are day places.
"""

DOORWALL = {
    "name": "the great hall of Frostpeak Lodge",
    "scene": "the lodge great hall",
    "props": "the Door Wall, a tall wooden wall of many little carved doors with brass knobs, each door carved "
             "with a small plain picture, a crackling stone fireplace, fir garlands, an antler coat rack, "
             "a long woven rug, a copper cocoa urn",
    "light": "Firelight and snowy window light fill the hall",
    "accents": "fir green and berry red",
    "atmo": "Firelight flickers and snow drifts past the tall windows",
    "motion": "firelight flickers across the little carved doors",
}

LANE_DAY = {
    "name": "Lantern Lane at the Frostpeak winter market",
    "scene": "Lantern Lane",
    "props": "a long string of paper lanterns overhead, snowy wooden stalls with striped awnings, a grill stall "
             "with rising steam, a cocoa cart, snow-dusted fir trees, footprints in the snow",
    "light": "Bright winter daylight sparkles on the snowy lane",
    "accents": "lantern red and icy blue",
    "atmo": "Soft snowflakes drift between the stalls",
    "motion": "soft snowflakes drift between the stalls",
}

LANE_NIGHT = {
    "name": "Lantern Lane at the Frostpeak winter night market",
    "scene": "Lantern Lane at night",
    "props": "a long string of glowing paper lanterns overhead, snowy wooden stalls with striped awnings, "
             "a glowing grill stall with rising steam, a cocoa cart, snow-dusted fir trees, footprints in the snow",
    "light": "Warm lantern glow lights the snowy lane at night",
    "accents": "lantern red and deep winter blue",
    "atmo": "Soft snow drifts through the lantern light",
    "motion": "soft snow drifts through the lantern light",
}


def bunk(day_props):
    """The closing bedtime place. day_props: two small things from the day, e.g.
    'a purple paper lantern and a tiny snowboard on the nightstand'."""
    return {
        "name": "the cozy bunk room of Frostpeak Lodge",
        "scene": "the cozy bunk room",
        "props": f"{day_props}, wooden bunk beds, patchwork quilts, a plain lamp, a frosted round window",
        "light": "A plain bedside lamp lights the cozy bunk room at night",
        "accents": "rose pink and warm amber",
        "atmo": "Snow drifts past the frosted window and fairy lights twinkle",
        "motion": "fairy lights twinkle",
    }
