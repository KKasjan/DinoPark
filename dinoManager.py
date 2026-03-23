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
    {"name": "Archaeopteryx", "type": "Carnivore", "goldenChest": True},
    {"name": "Smilodon", "type": "Carnivore", "goldenChest": True},
    {"name": "Mammoth", "type": "Herbivore", "goldenChest": False},
    {"name": "Therizinosaurus", "type": "Herbivore", "goldenChest": False},
    {"name": "Diplodocus", "type": "Herbivore", "goldenChest": False},
    {"name": "Dimetrodon", "type": "Carnivore", "goldenChest": False},
    {"name": "Parasaurolophus", "type": "Herbivore", "goldenChest": False},
    {"name": "Protoceratops", "type": "Herbivore", "goldenChest": False},
    {"name": "Iguanodon", "type": "Herbivore", "goldenChest": False},
    {"name": "Amargasaurus", "type": "Herbivore", "goldenChest": False},
    {"name": "Ceratosaurus", "type": "Carnivore", "goldenChest": False},
    {"name": "Incisivosaurus", "type": "Herbivore", "goldenChest": False},
    {"name": "Brachiosaurus", "type": "Herbivore", "goldenChest": False},
    {"name": "Dacentrurus", "type": "Herbivore", "goldenChest": False},
    {"name": "Allosaurus", "type": "Carnivore", "goldenChest": False},
    {"name": "Shell-don", "type": "Carnivore", "goldenChest": False},
    {"name": "Styracosaurus", "type": "Herbivore", "goldenChest": False},
    {"name": "Plesiosaurus", "type": "Carnivore", "goldenChest": False},
    {"name": "Kentrosaurus", "type": "Herbivore", "goldenChest": False},
    {"name": "Carnotaurus", "type": "Carnivore", "goldenChest": False},
    {"name": "Bulldosaurus", "type": "Carnivore", "goldenChest": False},
    {"name": "Pterocopter", "type": "Carnivore", "goldenChest": False},
    {"name": "Mechasaurus-Rex", "type": "Carnivore", "goldenChest": False},
    {"name": "Yeti", "type": "Carnivore", "goldenChest": False},
    {"name": "Azure Dragon", "type": "Carnivore", "goldenChest": False},
    {"name": "Wawel Dragon", "type": "Carnivore", "goldenChest": False},
    {"name": "Quetzalcoatlus", "type": "Herbivore", "goldenChest": False},
    {"name": "Spinosaurus", "type": "Carnivore", "goldenChest": False},
    {"name": "Kraken", "type": "Carnivore", "goldenChest": False},
    {"name": "Unicorn", "type": "Herbivore", "goldenChest": False},
    {"name": "Spike-o-tron", "type": "Carnivore", "goldenChest": False},
    {"name": "Dunkleosteus", "type": "Carnivore", "goldenChest": False},
    {"name": "Rhizodus", "type": "Carnivore", "goldenChest": False},
    {"name": "Liopleurodon", "type": "Carnivore", "goldenChest": False},
    {"name": "Lunaspis", "type": "Carnivore", "goldenChest": False},
    {"name": "Megalodon", "type": "Carnivore", "goldenChest": False},
    {"name": "Ichthyosaurus", "type": "Carnivore", "goldenChest": False},
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
