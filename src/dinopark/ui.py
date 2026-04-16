def get_safe_number(prompt: str) -> int:
    """
    Reads a number from user input and validates that it is between 0 and 6.
    """
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 6:
                return value
            print("Wrong! The number of dinos should be between 0 and 6.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 6.")


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
        print("Please enter y or n.")


def choose_dino(dinos: dict[str, dict]) -> str:
    """
    Displays a list of dinosaurs and returns the selected key.
    """
    print("\nChoose a dinosaur:\n")

    keys = list(dinos.keys())
    for i, key in enumerate(keys, start=1):
        print(f"{i}. {key}")

    while True:
        try:
            choice = int(input("\nSelect number: ")) - 1
            if 0 <= choice < len(keys):
                return keys[choice]
            print("Incorrect number! Try again.")
        except ValueError:
            print("Enter a valid number.")


def choose_level(levels: dict[str, int]) -> str:
    """
    Displays a list of levels and returns the selected key.
    """
    print("\nChoose a level:\n")

    sorted_levels = sorted(levels.keys(), key=lambda x: int(x), reverse=True)

    for i, lvl in enumerate(sorted_levels, start=1):
        print(f"{i}. {lvl} (current: {levels[lvl]})")

    while True:
        try:
            choice = int(input("\nSelect number: ")) - 1
            if 0 <= choice < len(sorted_levels):
                return sorted_levels[choice]
            print("Incorrect number! Try again.")
        except ValueError:
            print("Enter a valid number.")


def display_progress(dino_name: str, progress: dict) -> None:
    """
    Displays a full progress report for a dinosaur.
    """
    print(f"\n=== {dino_name.upper()} PROGRESS ===")
    print(f"Totems: {progress['totems']}")
    print(f"Golden chest: {progress['golden_chest']}")
    print(f"Possessed sum: {progress['possessed_sum']}")
    print(f"Missing for next totem: {progress['missing_for_next_totem']}")
    print(f"Missing for golden chest: {progress['missing_for_golden_chest']}")
    print("==============================\n")
