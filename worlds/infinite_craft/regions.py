from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import InfiniteCraftWorld


# helper function to create all regions (in this case just the crafting view)
# called from the world file
def create_regions(world: InfiniteCraftWorld) -> None:
    crafting_view = Region("Crafting View", world.player, world.multiworld)

    regions = [crafting_view]

    world.multiworld.regions += regions
