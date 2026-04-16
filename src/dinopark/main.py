from dinopark.data import load_all_dinos, save_all_dinos, validate_park_data
from dinopark.logic import calculate_progress, update_golden_chest_flag
from dinopark.ui import (
    choose_dino,
    choose_level,
    confirm,
    display_progress,
    get_safe_number,
)


def main() -> None:
    """
    Main entry point of the DinoPark Calculator application.
    Allows the user to update dinosaur levels and view progress
    toward totems and the golden chest.
    """

    dinos = load_all_dinos()

    # Validate JSON data structure
    if not validate_park_data(dinos):
        print("Invalid data structure. Fix dino-data.json. and try again")
        return

    if not dinos:
        print("Error! No dinosaur data found!")
        return

    while True:
        # Step 1 - choose dinosaur
        dino_key = choose_dino(dinos)
        dino = dinos[dino_key]

        print(f"\nSelected dinosaur: {dino_key}")

        # Step 2 - Show current progress
        progress = calculate_progress(dino)
        display_progress(dino_key, progress)

        # Step 3 - edit levels loop
        while confirm("Do you want to update levels?"):
            lvl = choose_level(dino["levels"])
            new_value = get_safe_number(f"Enter new value for level {lvl}: ")

            dino["levels"][lvl] = new_value

            # Update golden chest flag:
            update_golden_chest_flag(dino)

            # Save changes:
            save_all_dinos(dinos)

            # Show updated progress:
            progress = calculate_progress(dino)
            display_progress(dino_key, progress)

        # Step 4 - switch to another dinosaur:
        if not confirm("Do you want to switch to another dinosaur?"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
