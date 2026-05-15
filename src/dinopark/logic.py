from dinopark.config import BALANCES, RETURN_VALUE_AFTER_TOTEM, TARGET_TOTEM

# -----------------------------
# Value calculation
# -----------------------------


def calculate_total_value(levels: dict[int, int]) -> int:
    """
    Converts all dinosaurs into their level-1 equivalent value.
    """
    return sum(count * BALANCES[lvl] for lvl, count in levels.items())


# ---------------------------------------
# EFFECTIVE TOTEMS
# ---------------------------------------
def calculate_effective_totems(totems: int, levels: dict[int, int]) -> int:
    """
    Calculates how many totems the user *should have*
    based on total dino value.
    User-entered totems is the minimum; value may increase it.
    """
    value = calculate_total_value(levels)
    eff = totems

    # Each 63 values = 1 totem
    extra = value // TARGET_TOTEM
    eff = min(3, eff + extra)

    return eff


# -----------------------------
# Golden chest flag
# -----------------------------


def update_golden_chest_flag(dino: dict) -> None:
    """
    Golden chest is awarded when:
    - user has 3 totems
    - enclosure is full (each level has 1 dinosaur)
    """
    progress = calculate_progress(dino)
    dino["golden_chest"] = progress["golden_chest"]


# -----------------------------
# Missing amounts
# -----------------------------


def calculate_missing_for_next_totem(
    totems: int, levels: dict[int, int]
) -> int:
    """
    Missing dinosaurs (in lvl1 value) to obtain the NEXT totem.
    Returns 0 if user already has 3 effective totems.
    """
    eff_totems = calculate_effective_totems(totems, levels)
    if eff_totems >= 3:
        return 0

    total_value = calculate_total_value(levels)
    return max(TARGET_TOTEM - total_value, 0)


def is_full_enclosure(levels: dict[int, int]) -> bool:
    return all(levels.get(lvl, 0) > 0 for lvl in range(1, 7))


def missing_for_full_enclosure(levels: dict[int, int]) -> int:
    return sum(1 for lvl in range(1, 7) if levels.get(lvl, 0) == 0)


def calculate_missing_for_golden_chest(
    totems: int, levels: dict[int, int]
) -> int:
    """
    Calculates total value needed for golden chest
    based on explicit totem stages.
    """
    effective_totems = calculate_effective_totems(totems, levels)
    total_value = calculate_total_value(levels)
    missing_value = 0

    # Case 1 - 0 totems
    if effective_totems == 0:
        missing_value = (TARGET_TOTEM - total_value) + (
            3 * RETURN_VALUE_AFTER_TOTEM
        )

    # Case 2 - 1 totem:
    elif effective_totems == 1:
        missing_next = max(0, TARGET_TOTEM - total_value)
        missing_value = missing_next + (2 * RETURN_VALUE_AFTER_TOTEM)

    # Case 3 - 2 totems;
    elif effective_totems == 2:
        missing_next = max(0, TARGET_TOTEM - total_value)
        missing_value = missing_next + (1 * RETURN_VALUE_AFTER_TOTEM)

    # Case 4 - Collected 3 totems, but missing dino in the enclosure
    else:
        if not is_full_enclosure(levels):
            # Find the lowest missing level and return its value from BALANCES
            for lvl in range(1, 7):
                if levels.get(lvl, 0) == 0:
                    missing_value += BALANCES[lvl]

    return missing_value


# -----------------------------
# Progress summary
# -----------------------------


def calculate_progress(dino: dict) -> dict:
    """
    Returns:
    - effective totems
    - golden_chest flag
    - missing_for_next_totem
    - missing_for_golden_chest
    """
    levels = {int(k): v for k, v in dino["levels"].items()}
    base_totems = dino["totems"]

    eff_totems = calculate_effective_totems(base_totems, levels)

    missing_next = calculate_missing_for_next_totem(base_totems, levels)
    missing_chest = calculate_missing_for_golden_chest(base_totems, levels)

    # Full enclosure = at least 1 dino on each level 1-6
    full_enclosure = is_full_enclosure(levels)
    golden = eff_totems == 3 and full_enclosure

    return {
        "totems": eff_totems,
        "golden_chest": golden,
        "missing_for_next_totem": missing_next,
        "missing_for_golden_chest": missing_chest,
    }
