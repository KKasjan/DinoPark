def calculate_possessed_sum(
    counts: dict[int, int],
    balances: dict[int, int]
) -> int:
    """
    Calculates the total number of units you have by converting dinosaur
    levels to their base values ​from the balances.

    Parameters:
    counts (dict[int, int]): Dictionary where key is level
    and value is quantity.
    balances (dict[int, int]):: Dictionary where key is level
    and value is its unit worth.
    Returns:
    int: Total number of level 1 units
    """
    total = 0
    for lvl, quantity in counts.items():
        total += quantity * balances[lvl]
    return total


def get_missing_amount(
    possessed_sum: int,
    target: int
) -> int:
    """
    Calculates the missing number of dinosaurs to obtain the totem.

    Negative possessed_sum values are treated as 0.

    Parameters:
    possessed_sum: (int): Current number of units the user has.
    target: (int): Required number of units to obtain the totem.

    Returns:
    int: How many level 1 units are needed to get the totem
    (never less than 0).
    """
    if possessed_sum < 0:
        possessed_sum = 0

    if possessed_sum >= target:
        return 0
    return target - possessed_sum
