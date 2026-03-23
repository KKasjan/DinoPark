import json
import os


def load_all_dinos():
    file_path = "dino-data.json"

    if not os.path.exists(file_path):
        # Checking if the file exists at all
        print(f"Error! {file_path} not found!")
        return {}

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_park_data(data):
    required_keys = ["golden_chest", "type", "levels"]
    issues = []

    for name, dino_info in park.items():
        for key in required_keys:
            if key not in dino_info:
                issues.append(f"Dino {name} is missing required key")

    if issues:
        for issue in issues:
            print(issue)
        return False

    print("Data validation passed: JSON is healthy")


# The variable with data will be loaded dynamically
park = load_all_dinos()
is_data_valid = validate_park_data(park)

if not is_data_valid:
    print("Warning! App may crash due to invalid data!")
