import json
from typing import Any

from dinopark.config import DATA_FILE

# ---------------------------------------
# LOADING & SAVING
# ---------------------------------------


def load_all_dinos() -> dict[str, dict[str, Any]]:
    """
    Loads dinosaur data from JSON.
    Performs ONLY raw loading — no structure assumptions.
    Validation happens separately in validate_park_data().
    """
    # Checking if the file exists at all
    if not DATA_FILE.exists():
        return {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error: dino-data.json is corrupted or invalid JSON.")
        return {}

    # Data must be a dict[str, dict]
    if not isinstance(data, dict):
        print("Error: dino-data.json must contain a dictionary at top level.")
        return {}

    return data


def save_all_dinos(data: dict[str, dict[str, Any]]) -> None:
    """
    Saves the entire dinosaur dataset back to dino-data.json
    """

    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def validate_park_data(data: Any) -> bool:
    """
    Validates the entire dino JSON structure and business rules.
    Ensures:
    - correct types
    - correct keys
    - levels 1–6 exist and are ints >= 0
    - totems in range 0–3
    - golden_chest is bool
    - sum(levels) <= 6
    """
    if not isinstance(data, dict):
        return False

    for _name, dino in data.items():
        if not isinstance(dino, dict):
            return False

        # Required keys
        required_keys = {"type", "golden_chest", "totems", "levels"}
        if not required_keys.issubset(dino.keys()):
            return False

        # Validate type
        if not isinstance(dino["type"], str):
            return False

        # Validate totems
        totems = dino["totems"]
        if not isinstance(totems, int) or not (0 <= totems <= 3):
            return False

        # Validate golden chest
        if not isinstance(dino["golden_chest"], bool):
            return False

        # Validate levels
        levels = dino["levels"]
        if not isinstance(levels, dict):
            return False

        # Must contain exactly levels 1-6
        expected_levels = {str(i) for i in range(1, 7)}
        if set(levels.keys()) != expected_levels:
            return False

        # Validate each level count
        total = 0
        for _lvl, count in levels.items():
            if not isinstance(count, int) or count < 0:
                return False
            total += count

        # Business rule: max 6 dinos in enclosure
        if total > 6:
            return False

    return True
