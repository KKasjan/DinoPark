import json
from typing import Any

from dinopark.config import DATA_FILE


def load_all_dinos() -> dict[str, dict[str, Any]]:
    """
    Loads dinosaur data from the JSON file 'dino-data.json'.
    """
    # Checking if the file exists at all
    if not DATA_FILE.exists():
        raise FileNotFoundError("dino-data.json not found!")

    with open(DATA_FILE, encoding="utf-8") as f:
        data: dict[str, dict[str, Any]] = json.load(f)
        return data


def save_all_dinos(data: dict[str, dict[str, Any]]) -> None:
    """
    Saves the entire dinosaur dataset back to dino-data.json
    """

    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def update_dino_level(dino_key: str, level: str, amount: int) -> None:
    """
    Updates only ONE value for a selected dinosaur
    """
    data = load_all_dinos()

    if dino_key not in data:
        raise ValueError(f"Dino '{dino_key}' not found in dino-data.json")

    if level not in data[dino_key]["levels"]:
        raise ValueError(f"Level '{level}' not valid for dino '{dino_key}'")

    data[dino_key]["levels"][level] = amount

    save_all_dinos(data)


def validate_park_data(data: dict[str, dict[str, Any]]) -> bool:
    """
    Validates the structure of dinosaur data loaded from JSON.
    """
    required_keys = ["golden_chest", "type", "levels"]
    issues = []

    for name, dino_info in data.items():
        for key in required_keys:
            if key not in dino_info:
                issues.append(f"Dino {name} is missing required key: {key}")

    if issues:
        for issue in issues:
            print(issue)
        return False

    return True
