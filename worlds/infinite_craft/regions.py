from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import InfiniteCraftWorld


def create_regions(world: InfiniteCraftWorld) -> None:
    crafting_view = Region("Crafting View", world.player, world.multiworld)

    regions = [crafting_view]

    world.multiworld.regions += regions
