from typing import Any

from dinopark.data import validate_park_data
from dinopark.logic import calculate_progress, update_golden_chest_flag


def test_integration_full_flow() -> None:
    dino: dict[str, Any] = {
        "type": "herbivore",
        "golden_chest": False,
        "totems": 2,
        "levels": {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1},
    }

    assert validate_park_data({"ammonite": dino}) is True

    update_golden_chest_flag(dino)
    progress: dict[str, Any] = calculate_progress(dino)

    assert progress["totems"] >= 2
    assert isinstance(progress["golden_chest"], bool)
