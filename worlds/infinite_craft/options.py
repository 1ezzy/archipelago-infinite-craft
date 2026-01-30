from dataclasses import dataclass

from Options import PerGameCommonOptions, Range


class IndividualItemChecks(Range):
    """
    The number of individual item checks to generate. Item checks can be a single word or a short phrase.
    """

    display_name = "number of item checks"

    range_start = 1
    range_end = 20

    default = 5


class CategoryChecks(Range):
    """
    The number of category checks to generate. Each category contains N items (configured below).
    Every word or phrase in a category must be discovered before the check is considered completed.
    This option can make the game significantly harder, use with caution.
    """

    display_name = "number of category checks"

    range_start = 1
    range_end = 5

    default = 0


class CategoryCheckItemCount(Range):
    """
    The number of individual items to generate for each category check.
    This setting is only used when the "number of category checks" setting is a non-zero value.
    """

    display_name = "items per category checks"

    range_start = 1
    range_end = 5

    default = 0


@dataclass
class InfiniteCraftOptions(PerGameCommonOptions):
    number_of_item_checks: IndividualItemChecks
    number_of_category_checks: CategoryChecks
    items_per_category_check: CategoryCheckItemCount
