from typing import Dict

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World

# from .Items import 
# from .Locations import
# from .Options import
# from .Rules import


class InfiniteCraftWebWorld(WebWorld):
    tutorials = [
        Tutorial(
            "Infinite Craft Setup Guide",
            "A guide to setting up the Archipelago implementation of Infinite Craft.",
            "English",
            "setup_en.md",
            "setup/en",
            ["1ezzy"],
        )
    ]


class InfiniteCraftWorld(World):
    """
    Craft words into words into words into... you get the idea. Infinite Craft is a word combination game where 
    you merge discovered words to create new ones. Your goal is to find all the randomly generated goal words. 
    Perfect for when you're BKed.
    """

    game: str = "Infinite Craft"
    web = InfiniteCraftWebWorld()

    # item_name_to_id = {name: data.code for name, data in item_table.items()}
    # location_name_to_id = {name: data.id for name, data in location_table.items()}
    
    # item_name_groups = item_groups
    
    ap_world_version = "0.0.1"