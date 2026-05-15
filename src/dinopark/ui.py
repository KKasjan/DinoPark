# ============================================
# 1. Validators
# ============================================


def get_int(prompt: str) -> int:
    """
    Reads any non-negative integer.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def get_int_in_range(prompt: str, min_value: int, max_value: int) -> int:
    """
    Reads an integer within a specific range.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(
                f"Value must be between {min_value} and {max_value}.Try again."
            )
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def get_menu_choice(prompt: str, options_count: int) -> int:
    """
    Reads a menu choice from 1 to options_count.
    """
    return get_int_in_range(prompt, 1, options_count)


# ============================================
# 2. Basic UI
# ============================================


def confirm(prompt: str) -> bool:
    """
    Asks the user for a yes/no confirmation.
    """
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n: ")


def choose_dino(dinos: dict[str, dict]) -> str:
    """
    Displays a list of dinosaurs and returns the selected key.
    """
    print("\nChoose a dinosaur:\n")

    keys = list(dinos.keys())
    for i, key in enumerate(keys, start=1):
        print(f"{i}. {key}")

    choice = get_menu_choice("\nSelect number: ", len(keys))
    return keys[choice - 1]


# ============================================
# 3. New Functions
# ============================================


def verify_totems_ui(totems: int) -> int:
    """
    Shows current totem count and asks to confirm or update.
    """
    print(f"\n[DATA_CHECK] Current state: {totems} totems.")
    if confirm("Is this correct?"):
        return totems

    print("\nHow many totems do you have now?")
    return get_int_in_range("Enter numbers of totems (0-3): ", 0, 3)


# def ask_totems() -> int:
#     """
#     Asks the user how many totems they currently have (0–3).
#     """
#     print("\nHow many totems do you have?")
#     print("0 = no totems")
#     print("1 = first totem")
#     print("2 = second totem")
#     print("3 = third totem")
#     return get_int_in_range("Enter number of totems (0–3): ", 0, 3)


def choose_update_mode() -> int:
    """
    Asks the user how they want to update the enclosure.
    Returns:
    1 = whole enclosure
    2 = single level
    3 = return do dinosaur list
    4 = exit
    """
    print("\nHow do you want to update this dinosaur?")
    print("1. Update whole enclosure")
    print("2. Update single level")
    print("3. Return to dinosaur list")
    print("4. Exit")

    return get_menu_choice("choose option (1-4): ", 4)


def _calculate_total_dinos(levels: dict[int, int]) -> int:
    """
    Returns total number of dinosaurs in the enclosure.
    Max allowed = 6.
    """
    return sum(levels.values())


def update_whole_enclosure_ui(levels: dict[int, int]) -> dict[int, int]:
    """
    Updates the entire enclosure (levels 6 → 1).
    Validates that total slot usage does not exceed 6.
    """
    while True:
        print("\nUpdate whole enclosure (max 6 dinosaurs total).")
        new_levels: dict[int, int] = {}

        for lvl in range(6, 0, -1):
            current = levels.get(lvl, 0)
            prompt = f"How many dinos on level {lvl}? (current: {current}): "
            new_levels[lvl] = get_int(prompt)

        total_dinos = _calculate_total_dinos(new_levels)

        if total_dinos > 6:
            print(
                f"\nToo many dinos! Total slot usage would be {total_dinos}/6."
                "Please enter values that fit into 6 slots.\n"
            )
            continue

        return new_levels


def choose_level(levels: dict[int, int]) -> int:
    """
    Displays levels in natural order (1 → 6) and returns chosen level.
    """
    print("\nChoose a level to update:\n")

    sorted_levels = sorted(levels.keys())  # 1, 2, 3, 4, 5, 6

    for i, lvl in enumerate(sorted_levels, start=1):
        print(f"{i}. Level {lvl} (current: {levels[lvl]})")

    choice = get_menu_choice("\nSelect number: ", len(sorted_levels))
    return sorted_levels[choice - 1]


def update_single_level_ui(levels: dict[int, int]) -> dict[int, int]:
    """
    Updates a single level and validates total number of dinos.
    """
    while True:
        lvl = choose_level(levels)
        current = levels[lvl]
        prompt = f"Enter new value for level {lvl} (current: {current}): "
        new_value = get_int(prompt)

        new_levels = levels.copy()
        new_levels[lvl] = new_value

        total_dinos = _calculate_total_dinos(new_levels)

        if total_dinos > 6:
            print(
                f"\nToo many dinos! Total slot usage would be {total_dinos}/6."
                "Please enter a smaller value.\n"
            )
            continue

        return new_levels


# ============================================
# 4. Display
# ============================================


def display_progress(dino_name: str, progress: dict) -> None:
    """
    Displays a full progress report for a dinosaur.
    """
    print(f"\n=== {dino_name.upper()} PROGRESS ===")
    print(f"Totems: {progress['totems']}")
    print(f"Golden chest: {progress['golden_chest']}")
    print(f"Missing dinos on lvl 1 for next totem: "
          f"{progress['missing_for_next_totem']}"
    )
    print(
        f"Missing dinos on lvl 1 for golden chest: "
        f"{progress['missing_for_golden_chest']}"
    )
    print("==============================\n")
