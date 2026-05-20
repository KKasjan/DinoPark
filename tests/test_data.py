from unittest.mock import MagicMock, patch

import pytest  # noqa: F401

from dinopark.data import load_all_dinos, validate_park_data

# -----------------------------
# Tests for load_all_dino
# -----------------------------


def test_load_all_dinos_converts_keys_to_int() -> None:
    fake_db_row = ("ammonite", "herbivore", 0, 1, 1, 0, 1, 1, 1, 0)

    mock_connect = MagicMock()
    mock_cursor = mock_connect.cursor.return_value
    mock_cursor.fetchall.return_value = [fake_db_row]

    with patch("sqlite3.connect", return_value=mock_connect):
        data = load_all_dinos()
    
    expected_levels = {"1", "2", "3", "4", "5", "6"}
    assert set(data["ammonite"]["levels"].keys()) == expected_levels


# -----------------------------
# Tests for validate_park_data
# -----------------------------


def test_validate_ok_structure() -> None:
    data: dict[str, dict] = {
        "ammonite": {
            "type": "herbivore",
            "golden_chest": False,
            "totems": 1,
            "levels": {"6": 1, "5": 0, "4": 1, "3": 1, "2": 1, "1": 0},
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
