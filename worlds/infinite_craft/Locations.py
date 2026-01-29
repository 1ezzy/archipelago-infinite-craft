from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import InfiniteCraftWorld

# TODO make this list dynamic based off word count/custom word list length
LOCATION_NAME_TO_ID = {}


class InfiniteCraftLocation(Location):
    game = "Infinite Craft"


def create_all_locations(world: InfiniteCraftWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: InfiniteCraftWorld) -> None:
    crafting_view = world.get_region("Crafting View")

    craftable_locations = LOCATION_NAME_TO_ID
    crafting_view.add_locations(craftable_locations, InfiniteCraftLocation)


def create_events(world: InfiniteCraftWorld) -> None:
    crafting_view = world.get_region("Crafting View")

    crafting_view.add_event(
        "All Checks Completed",
        "All Checks Completed",
        location_type=InfiniteCraftLocation,
        item_type=items.InfiniteCraftItem,
    )
