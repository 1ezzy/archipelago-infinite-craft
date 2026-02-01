from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import InfiniteCraftWorld


# helper function to create the completion condition
# called from the world file
def set_completion_condition(world: InfiniteCraftWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has(
        "All Checks Completed", world.player
    )
