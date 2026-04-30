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
    calculate_progress(dino)


# -----------------------------
# Missing amounts
# -----------------------------

def calculate_missing_for_next_totem(levels: dict[int, int]) -> int:
    """
    Missing dinosaurs (in lvl1 value) to obtain the NEXT totem.
    """
    total_value = calculate_total_value(levels)
    return max(TARGET_TOTEM - total_value, 0)


def calculate_missing_for_golden_chest(
    eff_totems: int,
    levels: dict[int, int]
) -> int:
    """
    Missing value to reach golden chest, in a simplified model:
    - what you miss to the next totem
    - plus RETURN_VALUE_AFTER_TOTEM for each remaining totem
    - plus RETURN_VALUE_AFTER_TOTEM for the chest itself
    """
    missing_next = calculate_missing_for_next_totem(levels)

    remaining_totems = max(0, 3 - eff_totems)

    return missing_next + remaining_totems * RETURN_VALUE_AFTER_TOTEM


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

    # Full enclosure = at least 1 dino on each level 1-6
    full_enclosure = all(levels.get(lvl, 0) >= 1 for lvl in range(1, 7))

    golden = (eff_totems == 3 and full_enclosure)
    dino["golden_chest"] = golden

    missing_next = calculate_missing_for_next_totem(levels)
    missing_chest = calculate_missing_for_golden_chest(eff_totems, levels)

    return {
        "totems": eff_totems,
        "golden_chest": dino["golden_chest"],
        "missing_for_next_totem": missing_next,
        "missing_for_golden_chest": missing_chest
    }
