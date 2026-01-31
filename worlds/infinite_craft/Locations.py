from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import InfiniteCraftWorld


class InfiniteCraftLocation(Location):
    game = "Infinite Craft"


def create_all_locations(world: InfiniteCraftWorld, location_count: int) -> None:
    create_regular_locations(world, location_count)
    create_events(world)


def create_regular_locations(world: InfiniteCraftWorld, location_count: int) -> None:
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


# generating the max number of possible locations
def populate_locations_data() -> dict[str, int]:
    locations: dict[str, int] = {}
    id_incrementer = 1

    for i in range(1, 26):
        locations[f"Item {i}"] = id_incrementer
        id_incrementer += 1

    for i in range(1, 26):
        locations[f"Category {i}"] = id_incrementer
        id_incrementer += 1

    return locations


LOCATION_NAME_TO_ID = populate_locations_data()
