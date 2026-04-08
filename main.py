from config import TARGET, BALANCES
from data import park
from ui import get_user_input, display_result
from logic import calculate_possessed_sum, get_missing_amount


def main():
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
