from pathlib import Path

# Path to the JSON file used in other modules
DATA_FILE = Path(__file__).parent / "dino-data.json"

# Conversion rates: how many lvl 1 dinos are needed for higher level
BALANCES = {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}

# Each totem and golden chest costs 63 lvl1 value
TARGET_TOTEM = sum(BALANCES.values())  # 63

# Value of recovered lvl 6 dino after getting totem
RETURN_VALUE_AFTER_TOTEM = BALANCES[6]  # 32
