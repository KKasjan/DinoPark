import json
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest  # noqa: F401

from dinopark.data import load_all_dinos, validate_park_data

# -----------------------------
# Tests for load_all_dino
# -----------------------------


def test_load_all_dinos_converts_keys_to_int() -> None:
    fake_json: str = json.dumps(
        {
            "ammonite": {
                "type": "herbivore",
                "golden_chest": False,
                "totems": 1,
                "levels": {"1": 1, "2": 0, "3": 1, "4": 1, "5": 1, "6": 0},
            }
        }
    )

    with (
        # Patch DATA_FILE → pretend it points to "fake.json"
        patch("dinopark.data.DATA_FILE", Path("fake.json")),
        # Patch Path.exists → pretend that the file exists
        patch("pathlib.Path.exists", return_value=True),
        # Patch open → return fake_json
        patch("builtins.open", mock_open(read_data=fake_json)),
    ):
        data: dict[str, dict] = load_all_dinos()

    assert set(data["ammonite"]["levels"].keys()) == {1, 2, 3, 4, 5, 6}


# -----------------------------
# Tests for validate_park_data
# -----------------------------


def test_validate_ok_structure() -> None:
    data: dict[str, dict] = {
        "ammonite": {
            "type": "herbivore",
            "golden_chest": False,
            "totems": 1,
            "levels": {6: 1, 5: 0, 4: 1, 3: 1, 2: 1, 1: 0},
        }
    }

    assert validate_park_data(data) is True


def test_missing_required_key() -> None:
    data: dict[str, dict] = {
        "ammonite": {
            # missing type
            "golden_chest": False,
            "totems": 1,
            "levels": {"6": 1, "5": 0, "4": 1, "3": 1, "2": 1, "1": 0},
        }
    }

    assert validate_park_data(data) is False


def test_missing_level_key() -> None:
    data: dict[str, dict] = {
        "ammonite": {
            "type": "herbivore",
            "golden_chest": False,
            "totems": 1,
            # missing level "4"
            "levels": {"6": 1, "5": 0, "3": 1, "2": 1, "1": 0},
        }
    }

    assert validate_park_data(data) is False


def test_invalid_totems_type() -> None:
    data: dict[str, dict] = {
        "ammonite": {
            "type": "herbivore",
            "golden_chest": False,
            "totems": "two",  # invalid type
            "levels": {"6": 1, "5": 0, "4": 1, "3": 1, "2": 1, "1": 0},
        }
    }

    assert validate_park_data(data) is False


def test_invalid_golden_chest_type() -> None:
    data: dict[str, dict] = {
        "ammonite": {
            "type": "herbivore",
            "golden_chest": 1,  # invalid type
            "totems": 1,
            "levels": {"6": 1, "5": 0, "4": 1, "3": 1, "2": 1, "1": 0},
        }
    }

    assert validate_park_data(data) is False


def test_invalid_type_field() -> None:
    data: dict[str, dict] = {
        "ammonite": {
            "type": 123,  # invalid type
            "golden_chest": False,
            "totems": 1,
            "levels": {"6": 1, "5": 0, "4": 1, "3": 1, "2": 1, "1": 0},
        }
    }

    assert validate_park_data(data) is False
