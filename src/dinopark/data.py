import json
from typing import Any

from dinopark.config import DATA_FILE


def load_all_dinos() -> dict[str, dict[str, Any]]:
    """
    Loads dinosaur data from the JSON file 'dino-data.json'.
    Converts level key to int.
    """
    # Checking if the file exists at all
    if not DATA_FILE.exists():
        raise FileNotFoundError("dino-data.json not found!")

    with open(DATA_FILE, encoding="utf-8") as f:
        data: dict[str, dict[str, Any]] = json.load(f)

    # Convert level keys to int
    for dino in data.values():
        if "levels" in dino:
            dino["levels"] = {int(k): v for k, v in dino["levels"].items()}

    return data


def save_all_dinos(data: dict[str, dict[str, Any]]) -> None:
    """
    Saves the entire dinosaur dataset back to dino-data.json
    """

    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def validate_park_data(data: dict[str, dict[str, Any]]) -> bool:
    """
    Validates the structure of dinosaur data loaded from JSON.
    After load_all_dinos(), levels keys are already converted to int.
    """
    required_keys = ["type", "golden_chest", "totems", "levels"]
    issues = []

    for name, dino_info in data.items():
        # Check required top-level keys
        for key in required_keys:
            if key not in dino_info:
                issues.append(f"Dino '{name}' is missing required key: {key}")

        # Validate levels structure
        if "levels" in dino_info:
            levels = dino_info["levels"]

            # Must contain levels 1-6 as int keys
            for lvl in range(1, 7):
                if lvl not in levels:
                    issues.append(
                        f"Dino '{name}' level {lvl} must be an integer"
                    )

        # Validate totems
        if "totems" in dino_info and not isinstance(dino_info["totems"], int):
            issues.append(f"Dino '{name}' has invalid 'totems' value")

        # Validate golden_chest
        if "golden_chest" in dino_info and not isinstance(
            dino_info["golden_chest"], bool
        ):
            issues.append(f"Dino '{name}' has invalid 'golden_chest' value")

        # Validate type
        if "type" in dino_info and not isinstance(dino_info["type"], str):
            issues.append(f"Dino '{name}' has invalid 'type' value")

    if issues:
        for issue in issues:
            print(issue)
        return False

    return True
