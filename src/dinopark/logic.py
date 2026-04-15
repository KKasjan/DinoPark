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
