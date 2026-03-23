def calculate_missing(dino, BALANCES, TARGET=63):
    # Calculates how many lvl 1 dinos are missing for the next totem
    print(f"\n--- Calculation for: {dino['name']} ---")
    possessed_sum = 0

    # Collect data from user and calculating on level 1
    for lvl in range(6, 0, -1):
        quantity = int(input(f"How many {dino['name']} on lvl  {lvl}\
 you have:"))
        possessed_sum += quantity * BALANCES[lvl]

    # Calculating the difference
    if possessed_sum < TARGET:
        missing_value = TARGET - possessed_sum
    else:
        missing_value = 0

    return missing_value


def main():
    # List of dinosurs with their attributes and collection status
    park = [
        {"name": "Ammonite",
         "type": "Herbivore",
         "golden_chest": True},
        {"name": "Velociraptor",
         "type": "Carnovore",
         "golden_chest": True},
        {"name": "Pterodactyl",
         "type": "Carnivore",
         "golden_chest": True},
        {"name": "T-Rex",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Stegosaurus",
         "type": "Herbivore",
         "golden_chest": True},
        {"name": "Oviraptor",
         "type": "Herbivore",
         "golden_chest": True},
        {"name": "Triceratops",
         "type": "Herbivore",
         "golden_chest": True},
        {"name": "Gallimimus",
         "type": "Herbivore",
         "golden_chest": True},
        {"name": "Ankylosaurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Archaeopteryx",
         "type": "Carnivore",
         "golden_chest": True},
        {"name": "Smilodon",
         "type": "Carnivore",
         "golden_chest": True},
        {"name": "Mammoth",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Therizinosaurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Diplodocus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Dimetrodon",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Parasaurolophus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Protoceratops",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Iguanodon",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Amargasaurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Ceratosaurus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Incisivosaurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Brachiosaurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Dacentrurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Allosaurus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Shell-don",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Styracosaurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Plesiosaurus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Kentrosaurus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Carnotaurus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Bulldosaurus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Pterocopter",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Mechasaurus-Rex",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Yeti",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Azure Dragon",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Wawel Dragon",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Quetzalcoatlus",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Spinosaurus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Kraken",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Unicorn",
         "type": "Herbivore",
         "golden_chest": False},
        {"name": "Spike-o-tron",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Dunkleosteus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Rhizodus",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Liopleurodon",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Lunaspis",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Megalodon",
         "type": "Carnivore",
         "golden_chest": False},
        {"name": "Ichthyosaurus",
         "type": "Carnivore",
         "golden_chest": False},
    ]

    # Conversion rates: how many lvl 1 dinos are needed for higher level
    BALANCES = {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}

    to_do_totem = []

    for dino in park:
        if not dino["golden_chest"]:
            miss = calculate_missing(dino, BALANCES)
            if miss > 0:
                to_do_totem.append({"dino_name": dino['name'], "miss": miss})
                print(f"To complete the next totem you need: {miss} dino")
            else:
                print("You have the right amount of dinos for the totem!")
        else:
            print(f"\n{dino['name']} already has a golden box -\
I'll skip that")

    # - SUMMARY
    print("\n" + "="*40)
    print("MISSING TOTEMS")
    print("="*40)

    if not to_do_totem:
        print("Nothing is missing! All totems captured!")
    else:
        for item in to_do_totem:
            print(f"- {item['dino_name']}: missing {item['miss']}\
    dino on lvl 1")


# Calling the main function
if __name__ == "__main__":
    main()
