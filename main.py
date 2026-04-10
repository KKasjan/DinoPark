from config import BALANCES, TARGET
from data import load_all_dinos, validate_park_data
from logic import calculate_possessed_sum, get_missing_amount
from ui import display_result, get_user_input


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
    park = load_all_dinos()
    if not validate_park_data(park):
        print("Warning! App may crash due to invalid data!")
        return

    for name, dino_info in park.items():
        if not dino_info["golden_chest"]:
            # 1. UI fetches data
            user_counts = get_user_input(name)

            # 2. LOGIC calculates
            current_sum = calculate_possessed_sum(user_counts, BALANCES)
            missing = get_missing_amount(current_sum, TARGET)
            # 3. UI displaying
            display_result(name, missing)
        else:
            print(f"\n{name} has golden box - skipping.")


if __name__ == "__main__":
    main()
