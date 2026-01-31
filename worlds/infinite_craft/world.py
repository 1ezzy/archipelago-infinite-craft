from worlds.AutoWorld import World

from . import locations, regions, rules
from .options import InfiniteCraftOptions
from .items import (
    ITEM_NAME_TO_ID,
    ITEM_NAME_GROUPS,
    DEFAULT_ITEM_CLASSIFICATIONS,
    InfiniteCraftItem,
)
from .locations import LOCATION_NAME_TO_ID, InfiniteCraftLocation


class InfiniteCraftWorld(World):
    """
    Craft words into words into words into... you get the idea. Infinite Craft is a word combination game where
    you merge discovered words to create new ones. Your goal is to find all the randomly generated goal words.
    Perfect for when you're BKed.
    """

    game = "Infinite Craft"

    # web = InfiniteCraftWebWorld()

    options_dataclass = InfiniteCraftOptions
    options: InfiniteCraftOptions  # type: ignore

    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_to_id = ITEM_NAME_TO_ID
    item_name_groups = ITEM_NAME_GROUPS
    item_classifications = DEFAULT_ITEM_CLASSIFICATIONS

    origin_region_name = "Crafting View"

    def create_item(self, name: str) -> InfiniteCraftItem:
        return InfiniteCraftItem(
            name,
            self.item_classifications[name],
            self.item_name_to_id[name],
            self.player,
        )

    def calculate_location_sum(self) -> int:
        return self.options.items_per_category_check + (
            self.options.number_of_category_checks
            * self.options.items_per_category_check
        )

    def create_regions(self) -> None:
        regions.create_regions(self)
        locations.create_all_locations(self, self.calculate_location_sum())

    def create_items(self) -> None:
        # add all crafting items from the itempool
        for item in map(self.create_item, self.item_name_groups["Crafting Items"]):
            self.multiworld.itempool.append(item)

        # add all progressive items from the itempool
        for item in map(self.create_item, self.item_name_groups["Progressive Items"]):
            self.multiworld.itempool.append(item)

        # fill remaining itempool space with filler
        filler = 0  # TODO calculate this based off items vs locations
        self.multiworld.itempool += [
            self.create_item("Clear Canvas Trap") for _ in range(filler)
        ]

    def set_rules(self) -> None:
        rules.set_completion_condition(self)

    ap_world_version = "0.0.1"
