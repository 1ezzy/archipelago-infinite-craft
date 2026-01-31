from BaseClasses import Item, ItemClassification

ITEM_NAME_TO_ID = {
    "Water": 1,
    "Earth": 2,
    "Fire": 3,
    "Wind": 4,
    "Progressive Clear Canvas": 5,
    "Progressive Filter Input": 6,
    "Clear Canvas Trap": 7,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Water": ItemClassification.progression | ItemClassification.useful,
    "Earth": ItemClassification.progression | ItemClassification.useful,
    "Fire": ItemClassification.progression | ItemClassification.useful,
    "Wind": ItemClassification.progression | ItemClassification.useful,
    "Progressive Clear Canvas": ItemClassification.useful,
    "Progressive Filter Input": ItemClassification.useful,
    "Clear Canvas Trap": ItemClassification.filler,
}

ITEM_NAME_GROUPS = {
    "Crafting Items": {"Water", "Earth", "Fire", "Wind"},
    "Progressive Items": {
        "Progressive Clear Canvas",
        "Progressive Filter Input",
    },
    "Traps": {"Clear Canvas Trap"},
}


class InfiniteCraftItem(Item):
    game = "Infinite Craft"
