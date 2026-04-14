from dinopark.config import BALANCES, TARGET
from dinopark.data import load_all_dinos, update_dino_level, validate_park_data
from dinopark.logic import calculate_possessed_sum, get_missing_amount
from dinopark.ui import choose_dino, confirm, display_result, get_user_input


def main() -> None:
    """
    Main entry point of the application.
    """
    dinos = load_all_dinos()

    # Validate JSON structure
    if not validate_park_data(dinos):
        print("Invalid JSON structure. Fix dino-data.json and try again.")
        return

    if not dinos:
        print("Error! No dinosaur data found!")
        return

    # Step 1 - Choose dinosaur
    dino_key = choose_dino(dinos)
    print(f"\nSelected dinosaur: {dino_key}")

    current_levels = dinos[dino_key]["levels"]
    has_existing = any(value > 0 for value in current_levels.values())

    # Step 2 - Check if user already has data
    if has_existing:
        print("\nExisting data found: ")
        for lvl, val in current_levels.items():
            print(f"Level {lvl}: {val}")

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
