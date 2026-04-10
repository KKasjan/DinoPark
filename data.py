import json
import os
from typing import Any


def load_all_dinos() -> dict[str, Any]:
    """
    Loads dinosaur data from the JSON file 'dino-data.json'.

    If the file does not exist, an empty dictionary is returned.

    Returns:
    dict[str, Any]: Parsed JSON data containing dinosaur definitions.
    """
    file_path = "dino-data.json"

    # Checking if the file exists at all
    if not os.path.exists(file_path):
        print(f"Error! {file_path} not found!")
        return {}

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


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
