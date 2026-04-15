from pathlib import Path

# Path to the JSON file used in other modules
DATA_FILE = Path(__file__).parent / "dino-data.json"

# Conversion rates: how many lvl 1 dinos are needed for higher level
BALANCES = {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}

# The number of dinos needed to get the first totem
TARGET_FIRST_TOTEM = sum(BALANCES.values())

# Number of dinos needed to get the remaining totems / golden chest
TARGET_OTHER_TOTEMS = BALANCES[max(BALANCES.keys())]
