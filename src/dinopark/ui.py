def get_safe_number(prompt: str) -> int:
    """
    Reads a number from user input and validates that it is between 0 and 6.

    Parameters:
    prompt (str): Text displayed to the user.

    Returns:
    int: A valid number between 0 and 6.
    """
    while True:
        try:
            user_input = input(prompt)
            # Conversion to integer
            value = int(user_input)

            # The game allows for a maximum of 6 dinos in the enclosure
            if value < 0 or value > 6:
                print("Wrong! The number of dinos should be between 0 and 6.")
                continue

            return value
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 6.")


def confirm(prompt: str) -> bool:
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y od n.")


def get_user_input(dino_name: str, levels: dict[str, int]) -> dict[str, int]:
    """
    Collects the number of dinosaurs the user owns for each level (1–6).

    The function dynamically reads available levels from the JSON data,
    so it does not depend on a hardcoded range.
    """
    print(f"\n--- {dino_name.upper()} ---")
    counts: dict[str, int] = {}

    # Sort levels numerically (e.g. "6", "5", "4"...)
    sorted_levels = sorted(levels.keys(), key=lambda x: int(x), reverse=True)

    for lvl in sorted_levels:
        counts[lvl] = get_safe_number(
            f"How many {dino_name} on lvl  {lvl} you have:"
        )

    return counts


def display_result(dino_name: str, missing: int) -> None:
    """
    Displays the result for a given dinosaur based on how many
    units are missing.

    Parameters:
    dino_name (str): Name of the dinosaur.
    missing (int): Number of units still needed to obtain the totem.

    Returns:
    None
    """
    if missing > 0:
        print(f"{dino_name}: missing {missing}")
    else:
        print(f"{dino_name}: ready for totem!")


def choose_dino(dinos: dict[str, dict]) -> str:
    """
    Displays a list of dinosaurs and returns the selected key.
    """
    print("\nChoose a dinosaur to complete:\n")

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
            print("Enter the number.")
