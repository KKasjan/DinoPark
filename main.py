from config import TARGET, BALANCES
from data import park
from ui import get_user_input, display_result
from logic import calculate_possessed_sum, get_missing_amount


def main():
    for dino in park:
        if not dino["golden_chest"]:
            # 1. UI fetches data
            user_counts = get_user_input(dino["name"])
            # 2. LOGIC calculates
            current_sum = calculate_possessed_sum(user_counts, BALANCES)
            missing = get_missing_amount(current_sum, TARGET)
            # 3. UI displayin
            display_result(dino["name"], missing)
        else:
            print(f"\n{dino['name']} has golden box - skipping.")


if __name__ == "__main__":
    main()
