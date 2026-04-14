import json
from pathlib import Path
from typing import Any

DATA_FILE = Path(__file__).parent / "dino-data.json"


def load_all_dinos() -> dict[str, Any]:
    """
    Loads dinosaur data from the JSON file 'dino-data.json'.

    If the file does not exist, an empty dictionary is returned.

    Returns:
    dict[str, Any]: Parsed JSON data containing dinosaur definitions.
    """
    # Checking if the file exists at all
    if not DATA_FILE.exists():
        raise FileNotFoundError("dino-data.json not found!")

    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_all_dinos(data: dict[str, Any]) -> None:
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

    Checks whether each dinosaur entry contains the required keys:
    'golden_chest', 'type', and 'levels'.

    Parameters:
        data (dict[str, dict[str, Any]]): Parsed JSON data where each key
            is a dinosaur name and each value is a dictionary of attributes.

    Returns:
        bool: True if the data is valid, False otherwise.
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

    print("Data validation passed: JSON is healthy")
    return True
