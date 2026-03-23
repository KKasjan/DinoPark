# A function that collects data from the user about the number of dinos
# owned per level.
def get_user_input(dino_name):
    print(f"\n--- {dino_name.upper()} ---")
    counts = {}
    for lvl in range(6, 0, -1):
        counts[lvl] = int(input(f"How many {dino_name} on lvl  {lvl}\
 you have:"))
    # return a "package" of data, not a finished result
    return counts


# displaying results
def display_result(dino_name, missing):
    if missing > 0:
        print(f"{dino_name}: missing {missing}")
    else:
        print(f"{dino_name}: ready for totem!")
