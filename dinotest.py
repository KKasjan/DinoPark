park = [
    {"name": "Ammonite", "type": "Herbivore", "goldenChest": True},
    {"name": "Velociraptor", "type": "Carnovore", "goldenChest": True},
    {"name": "Pterodactyl", "type": "Carnivore", "goldenChest": True},
    {"name": "T-Rex", "type": "Carnivore", "goldenChest": False},
    {"name": "Stegosaurus", "type": "Herbivore", "goldenChest": True},
    {"name": "Oviraptor", "type": "Herbivore", "goldenChest": True},
    {"name": "Triceratops", "type": "Herbivore", "goldenChest": True},
    {"name": "Gallimimus", "type": "Herbivore", "goldenChest": True},
    {"name": "Ankylosaurus", "type": "Herbivore", "goldenChest": False},
]

balances = {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}

toDoTotem = []

for dino in park:
    if not dino["goldenChest"]:
        print(f"\n--- Calculation for: {dino["name"]} ---")
        possessedSum = 0

        for lvl in range(6, 0, -1):
            quantity = int(input(f"How many {dino['name']} on lvl  {lvl}\
 you have:"))
            possessedSum += quantity * balances[lvl]

        target = 63
        if possessedSum < target:
            missing = target - possessedSum
            toDoTotem.append({"nameDino": dino['name'], "miss": missing})
            print(f"To complete the next totem you need: {missing} dino")
        else:
            print("You have the right amount of dinos for the totem!")
    else:
        print(f"\n{dino['name']} already has a golden box - I'll skip that")

# - SUMMARY
print("\n" + "="*40)
print("MISSING TOTEMS")
print("="*40)

for item in toDoTotem:
    if not toDoTotem:
        print("Nothing is missing! All totems captured!")
    else:
        print(f"- {item['nameDino']}: missing {item['miss']}\
 dino on lvl 1")
