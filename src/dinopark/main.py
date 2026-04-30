from dinopark.data import load_all_dinos, save_all_dinos, validate_park_data
from dinopark.logic import calculate_progress
from dinopark.ui import (
    ask_totems,
    choose_dino,
    choose_update_mode,
    confirm,
    display_progress,
    update_single_level_ui,
    update_whole_enclosure_ui,
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
        print("Invalid data structure. Fix dino-data.json and try again.")
        return

    if not dinos:
        print("Error! No dinosaur data found!")
        return

    # List of all updated dinos in this session
    session_updates: list[tuple[str, dict]] = []

    while True:
        # Step 1: choose dinosaur
        dino_key = choose_dino(dinos)
        dino = dinos[dino_key]

        print(f"\nSelected dinosaur: {dino_key}")

        # Step 2: ask ho many totems user has
        dino["totems"] = ask_totems()

        # Step 3: choose update mode
        mode = choose_update_mode()

        if mode == 1:
            # Update whole enclosure
            dino["levels"] = update_whole_enclosure_ui(dino["levels"])

        elif mode == 2:
            # Update single level
            dino["levels"] = update_single_level_ui(dino["levels"])

        elif mode == 3:
            # Return to dino list WITHOUT saving summary
            print("\nReturning to dinosaur list...\n")
            continue

        elif mode == 4:
            # Exit program immediately
            print("\nExiting program...\n")
            if not session_updates:
                print("No changes were made in this session.\n")

            print("Thank you for using DinoPark Calculator!\n")
            return

        # If we reach here, user chose mode 1 or 2 → changes were made

        # Save changes
        save_all_dinos(dinos)

        # Step 4: show summary for THIS dino
        progress = calculate_progress(dino)
        display_progress(dino_key, progress)

        # Save this dino's summary for final session report
        session_updates.append((dino_key, progress))

        # Step 5: switch to another dinosaur
        if not confirm("Do you want to switch to another dinosaur?"):
            break

    # Final session summary
    print("\n===== SESSION SUMMARY =====\n")

    for name, progress in session_updates:
        print(f"Dinosaur: {name}")
        print(f"  Totems: {progress['totems']}")
        print(f"  Golden chest: {progress['golden_chest']}")
        print(
            f"  Missing for next totem: {progress['missing_for_next_totem']}"
        )
        print(
            f"  Missing for golden chest: "
            f"{progress['missing_for_golden_chest']}"
        )
        print()

    print("Thank you for using DinoPark Calculator!\n")


if __name__ == "__main__":
    main()
