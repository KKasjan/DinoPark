from dinopark.config import BALANCES, TARGET_FIRST_TOTEM, TARGET_OTHER_TOTEMS


def calculate_possessed_sum(
    counts: dict[int, int], balances: dict[int, int]
) -> int:
    """
    Calculates the total number of units you have by converting dinosaur
    levels to their base values ​from the balances.
    """
    total = 0
    for lvl, quantity in counts.items():
        total += quantity * balances[lvl]
    return total


def get_missing_amount(possessed_sum: int, target: int) -> int:
    """
    Calculates the missing number of dinosaurs to obtain the totem.

    Negative possessed_sum values are treated as 0.
    """
    if possessed_sum < 0:
        possessed_sum = 0

    if possessed_sum >= target:
        return 0
    return target - possessed_sum


def update_golden_chest_flag(dino: dict) -> None:
    """
    Updates the 'golden_chest' flag based on game rules.

    A dinosaur receives the golden chest if:
    - it has exactly 3 totems
    - it has at least one dinosaur on every level (full enclosure)

    This function updates the 'golden_chest' field in-place.
    """
    totems = dino["totems"]
    levels = dino["levels"]

    has_full_enclosure = all(count > 0 for count in levels.values())

    dino["golden_chest"] = (totems == 3 and has_full_enclosure)


def calculate_missing_for_next_totem(totems: int, possessed_sum: int) -> int:
    """
    Calculates the missing number of dinosaurs needed to obtain the next totem
    """
    if totems == 0:
        return get_missing_amount(possessed_sum, TARGET_FIRST_TOTEM)

    if totems in (1, 2):
        return get_missing_amount(possessed_sum, TARGET_OTHER_TOTEMS)

    return 0


def calculate_missing_for_golden_chest(levels: dict[int, int]) -> int:
    """
    Calculates the missing number of dinosaurs needed
    to obtain the golden chest.
    """
    missing_levels = [lvl for lvl, count in levels.items() if count == 0]
    return len(missing_levels)


def calculate_progress(dino: dict) -> dict:
    """
    Calculates the progress towards the next totem and golden
    chest for a given dinosaur.

    Returns a dictionary with the following keys:
    - 'missing_for_next_totem': number of dinosaurs
    needed for the next totem
    - 'missing_for_golden_chest': number of dinosaurs
    needed for the golden chest
    """
    int_levels = {int(k): v for k, v in dino["levels"].items()}
    possessed_sum = calculate_possessed_sum(int_levels, BALANCES)

    totems = dino["totems"]

    missing_next_totem = calculate_missing_for_next_totem(
        totems,
        possessed_sum
    )
    missing_golden_chest = calculate_missing_for_golden_chest(dino["levels"])

    return {
        "totems": totems,
        "golden_chest": dino["golden_chest"],
        "possessed_sum": possessed_sum,
        "missing_for_next_totem": missing_next_totem,
        "missing_for_golden_chest": missing_golden_chest,
    }
