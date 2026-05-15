from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock, patch

import pytest  # noqa: F401

from dinopark.main import main

# ---------------------------------------------------------
# Helper: fake dino dataset
# ---------------------------------------------------------


def make_fake_dinos() -> dict[str, dict[str, Any]]:
    return {
        "ammonite": {
            "type": "herbivore",
            "golden_chest": False,
            "totems": 0,
            "levels": {"6": 0, "5": 0, "4": 0, "3": 0, "2": 0, "1": 0},
        }
    }


# ---------------------------------------------------------
# TEST 1 — save happens AFTER calculate_progress
# ---------------------------------------------------------
@patch("dinopark.main.save_all_dinos")
@patch("dinopark.main.display_progress")
@patch("dinopark.main.confirm", return_value=False)
@patch(
    "dinopark.main.update_whole_enclosure_ui",
    return_value={"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1},
)
@patch("dinopark.main.choose_update_mode", return_value=1)
@patch("dinopark.main.verify_totems_ui", return_value=3)
@patch("dinopark.main.choose_dino", return_value="ammonite")
@patch("dinopark.main.load_all_dinos", side_effect=lambda: make_fake_dinos())
@patch("dinopark.main.validate_park_data", return_value=True)
def test_save_happens_after_progress(
    mock_validate: MagicMock,
    mock_load: MagicMock,
    mock_choose_dino: MagicMock,
    mock_verify_totems_ui: MagicMock,
    mock_mode: MagicMock,
    mock_update: MagicMock,
    mock_confirm: MagicMock,
    mock_display: MagicMock,
    mock_save: MagicMock,
) -> None:
    main()

    # Save must be called
    assert mock_save.called

    # Extract saved data
    saved_data: dict[str, dict[str, Any]] = mock_save.call_args[0][0]
    ammonite = saved_data["ammonite"]

    # Golden chest must be True (3 totems + full enclosure)
    assert ammonite["golden_chest"] is True


# ---------------------------------------------------------
# TEST 2 — canceling the update does NOT save changes
# ---------------------------------------------------------
@patch("dinopark.main.save_all_dinos")
@patch("dinopark.main.confirm", return_value=False)
# Return to list
@patch("dinopark.main.choose_update_mode", side_effect=[3, 4])
@patch("dinopark.main.verify_totems_ui", return_value=2)
@patch("dinopark.main.choose_dino", return_value="ammonite")
@patch("dinopark.main.load_all_dinos", side_effect=lambda: make_fake_dinos())
@patch("dinopark.main.validate_park_data", return_value=True)
def test_cancel_does_not_save(
    mock_validate: MagicMock,
    mock_load: MagicMock,
    mock_choose_dino: MagicMock,
    mock_verify_totems_ui: MagicMock,
    mock_mode: MagicMock,
    mock_confirm: MagicMock,
    mock_save: MagicMock,
) -> None:
    main()

    # save_all_dinos MUST NOT be called
    mock_save.assert_not_called()


# ---------------------------------------------------------
# TEST 3 — golden_chest persistence after saving
# ---------------------------------------------------------
@patch("dinopark.main.save_all_dinos")
@patch("dinopark.main.display_progress")
@patch("dinopark.main.confirm", return_value=False)
@patch(
    "dinopark.main.update_whole_enclosure_ui",
    return_value={"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1},
)
@patch("dinopark.main.choose_update_mode", side_effect=[1])
@patch("dinopark.main.verify_totems_ui", return_value=3)
@patch("dinopark.main.choose_dino", return_value="ammonite")
@patch("dinopark.main.load_all_dinos", side_effect=lambda: make_fake_dinos())
@patch("dinopark.main.validate_park_data", return_value=True)
def test_golden_chest_persistence(
    mock_validate: MagicMock,
    mock_load: MagicMock,
    mock_choose_dino: MagicMock,
    mock_verify_totes_ui: MagicMock,
    mock_mode: MagicMock,
    mock_update: MagicMock,
    mock_confirm: MagicMock,
    mock_display: MagicMock,
    mock_save: MagicMock,
) -> None:
    main()

    saved_data: dict[str, dict[str, Any]] = mock_save.call_args[0][0]
    ammonite = saved_data["ammonite"]

    assert ammonite["golden_chest"] is True
    assert ammonite["totems"] == 3
    assert ammonite["levels"] == {
        "1": 1,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 1,
    }
