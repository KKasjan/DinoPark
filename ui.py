# A function that checks the correctness of the number entered by the user
def get_safe_number(prompt):
    while True:
        try:
            user_input = input(prompt)
            # Conversion to integer
            value = int(user_input)

            if value not in [0, 1]:
                print("Wrong! The dino number should be between 0 and 1")
                continue

            return value
        except ValueError:
            print("Invalid input! Please enter a digit (0 or 1).")


# A function that collects data from the user about the number of dinos
# owned per level.
def get_user_input(dino_name):
    print(f"\n--- {dino_name.upper()} ---")
    counts = {}
    for lvl in range(6, 0, -1):
        counts[lvl] = get_safe_number(f"How many {dino_name} on lvl  {lvl}\
 you have:")
        # counts[lvl] = int(input(f"How many {dino_name} on lvl  {lvl}\
        # you have:"))
    # return a "package" of data, not a finished result
    return counts


# displaying results
def display_result(dino_name, missing):
    if missing > 0:
        print(f"{dino_name}: missing {missing}")
    else:
        print(f"{dino_name}: ready for totem!")
