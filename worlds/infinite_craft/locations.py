from typing import TYPE_CHECKING, Any

import orjson
import pkgutil

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import InfiniteCraftWorld


class InfiniteCraftLocation(Location):
    game = "Infinite Craft"


# load all current locations from json file
def _load_location_json_data() -> dict[str, Any]:
    location_data = pkgutil.get_data(__name__, "data/locations.json")
    if location_data is None:
        raise FileNotFoundError("Could not load location data for Infinite Craft")

    return orjson.loads(location_data.decode("utf-8"))


# generate ids for all loaded locations
def _build_location_name_to_id(location_data: dict[str, Any]) -> dict[str, int]:
    names_sorted = sorted(location_data.keys())
    return {name: i + 1 for i, name in enumerate(names_sorted)}


# define variables for location data and location + id dict
_LOCATION_DEFS: dict[str, Any] = _load_location_json_data()
LOCATION_NAME_TO_ID: dict[str, int] = _build_location_name_to_id(_LOCATION_DEFS)


# external helper function to create all locations and game completion event
def create_all_locations(world: InfiniteCraftWorld, location_count: int) -> None:
    create_regular_locations(world, location_count)
    create_events(world)


# internal helper function to randomly select a subset of items from the locations
def _random_subset_locations(
    world: InfiniteCraftWorld, locations: dict[str, int], location_count: int
):
    location_keys = list(locations.keys())
    location_count = min(location_count, len(location_keys))

    random_locations = world.random.sample(location_keys, location_count)
    return {name: locations[name] for name in random_locations}


# helper function to create all locations, called by create_all_locations from the world file
def create_regular_locations(world: InfiniteCraftWorld, location_count: int) -> None:
    crafting_view = world.get_region("Crafting View")

    selected_locations = _random_subset_locations(
        world, LOCATION_NAME_TO_ID, location_count
    )

    crafting_view.add_locations(selected_locations, InfiniteCraftLocation)


# helper function to create all events, called by create_all_locations from the world file
def create_events(world: InfiniteCraftWorld) -> None:
    crafting_view = world.get_region("Crafting View")

    crafting_view.add_event(
        "All Checks Completed",
        "All Checks Completed",
        location_type=InfiniteCraftLocation,
        item_type=items.InfiniteCraftItem,
    )
