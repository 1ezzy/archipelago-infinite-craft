from worlds.AutoWorld import World

from . import locations, regions, rules
from . import options as infinitecraft_options


class InfiniteCraftWorld(World):
    """
    Craft words into words into words into... you get the idea. Infinite Craft is a word combination game where
    you merge discovered words to create new ones. Your goal is to find all the randomly generated goal words.
    Perfect for when you're BKed.
    """

    game = "Infinite Craft"

    # web = InfiniteCraftWebWorld()

    options_dataclass = infinitecraft_options.InfiniteCraftOptions
    options: infinitecraft_options.InfiniteCraftOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = {}

    origin_region_name = "Crafting View"

    def create_regions(self) -> None:
        regions.create_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_completion_condition(self)

    ap_world_version = "0.0.1"
