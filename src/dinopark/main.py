from dinopark.config import BALANCES, TARGET
from dinopark.data import load_all_dinos, validate_park_data, update_dino_level
from dinopark.logic import calculate_possessed_sum, get_missing_amount
from dinopark.ui import (
    display_result,
    choose_dino,
    get_safe_number,
    get_user_input,
    confirm
)


def main() -> None:
    """
    Main entry point of the application.

    Loads dinosaur data from JSON, validates its structure, and then
    processes each dinosaur that does not have a golden chest. For each
    such dinosaur, the function collects user input, calculates the
    current total value, determines how many units are missing to obtain
    the totem, and displays the result.

    Returns:
    None
    """

    dinos = load_all_dinos()

    if not dinos:
        print("Error! No dinosaur data found!")
        return
    
    # Step 1 - Choose dinosaur
    dino_key = choose_dino(dinos)
    print(f"\nSelected dinosaur: {dino_key}")
    current_levels = dinos[dino_key]["levels"]

    # Step 2 - Check if user already has data
    has_existing = any(value > 0 for value in current_levels.values())

    if has_existing:
        print("\nExisting data found: ")
        for lvl, val in current_levels.items():
            print(f"Level {lvl}: {lvl}")

        if confirm("Do you want update these values?"):
            new_data = get_user_input(dino_key)
        else:
            new_data = {int(k): v for k, v in current_levels.items()}
    else:
        new_data = get_user_input(dino_key)

    # Step 3 - Save all levels
    for lvl, amount in new_data.items():
        update_dino_level(dino_key, str(lvl), amount)

    # Step 4 - Recalc logic
    current_sum = calculate_possessed_sum(new_data, BALANCES)
    missing = get_missing_amount(current_sum, TARGET)

    # Step 5 - Display result
    display_result(dino_key, missing)


if __name__ == "__main__":
    main()
