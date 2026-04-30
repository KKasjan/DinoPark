import pytest

from dinopark.logic import (
    calculate_effective_totems,
    calculate_missing_for_golden_chest,
    calculate_missing_for_next_totem,
    calculate_progress,
    calculate_total_value,
    update_golden_chest_flag,
)


# -----------------------------
# Fixtures
# -----------------------------

@pytest.fixture
def levels_full():
    return {6: 1, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}


@pytest.fixture
def levels_empty():
    return {6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}


@pytest.fixture
def levels_partial():
    return {6: 1, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}


# -----------------------------
# Helpers
# -----------------------------

def make_dino(levels: dict[int, int], totems: int = 0) -> dict:
    """
    Helper to build a valid dino structure.
    """
    return {
        "totems": totems,
        "levels": {str(k): v for k, v in levels.items()},
        "golden_chest": False,
    }


# -----------------------------
# calculate_total_value
# -----------------------------

def test_total_value_full(levels_full):
    assert calculate_total_value(levels_full) == 63


def test_total_value_empty(levels_empty):
    assert calculate_total_value(levels_empty) == 0


def test_total_value_partial(levels_partial):
    assert calculate_total_value(levels_partial) == 32


# -----------------------------
# calculate_effective_totems
# -----------------------------

def test_effective_totems_no_bonus(levels_partial):
    assert calculate_effective_totems(0, levels_partial) == 0


def test_effective_totems_gain_one(levels_full):
    assert calculate_effective_totems(0, levels_full) == 1


def test_effective_totems_cap_at_three(levels_full):
    assert calculate_effective_totems(3, levels_full) == 3


# -----------------------------
# Tests for update_golden_chest_flag
# -----------------------------

def test_golden_chest_true_when_3_totems_amd_full_enclosure():
    levels = {6: 1, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}
    dino = make_dino(levels, totems=3)

    update_golden_chest_flag(dino)

    assert dino["golden_chest"] is True


def test_golden_chest_false_when_3_totems_but_not_full_enclosure():
    levels = {6: 1, 5: 1, 4: 0, 3: 1, 2: 1, 1: 1}
    dino = make_dino(levels, totems=3)

    update_golden_chest_flag(dino)

    assert dino["golden_chest"] is False


def test_golden_chest_false_when_full_enclosure_but_only_1_totem():
    levels = {6: 1, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}
    dino = make_dino(levels, totems=1)

    update_golden_chest_flag(dino)

    assert dino["golden_chest"] is False


def test_golden_chest_true_when_effective_totems_reach_3_from_value():
    # The value should give 3 totems even if the user entered 0
    # BALANCES: 6=32, 5=16, 4=8, 3=4, 2=2, 1=1
    # If we give e.g. 6:6 → 6*32 = 192 → 192//63 = 3 extra totems
    levels = {6: 6, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}
    dino = make_dino(levels, totems=0)

    update_golden_chest_flag(dino)

    assert dino["golden_chest"] is True


def test_golden_chest_false_when_eff3_but_not_full():
    # 6:6 gives 192 values ​​→ 3 totems
    # but no level 4 → incomplete enclosure
    levels = {6: 6, 5: 1, 4: 0, 3: 1, 2: 1, 1: 1}
    dino = make_dino(levels, totems=0)

    update_golden_chest_flag(dino)

    assert dino["golden_chest"] is False


# -----------------------------
# calculate_missing_for_next_totem
# -----------------------------

def test_missing_next_totem_full(levels_full):
    assert calculate_missing_for_next_totem(levels_full) == 0


def test_missing_next_totem_partial(levels_partial):
    assert calculate_missing_for_next_totem(levels_partial) == 31


# -----------------------------
# calculate_missing_for_golden_chest
# -----------------------------'

def test_missing_chest_when_0_totems(levels_partial):
    # missing_next = 31, remaining_totems = 3
    assert calculate_missing_for_golden_chest(0, levels_partial) == 31 + 3 * 32


def test_missing_chest_when_1_totem(levels_partial):
    # missing_next = 31, remaining_totems = 2
    assert calculate_missing_for_golden_chest(1, levels_partial) == 31 + 2 * 32


def test_missing_chest_when_2_totems(levels_partial):
    # missing_next = 31, remaining_totems = 1
    assert calculate_missing_for_golden_chest(2, levels_partial) == 31 + 32


def test_missing_chest_when_3_totems(levels_full):
    assert calculate_missing_for_golden_chest(3, levels_full) == 0


# -----------------------------
# calculate_progress
# -----------------------------

def test_progress_basic():
    dino = {
        "totems": 1,
        "golden_chest": False,
        "levels": {"6": 1, "5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
    }

    result = calculate_progress(dino)

    assert result["totems"] == 1
    assert result["missing_for_next_totem"] == 31
    assert result["missing_for_golden_chest"] == 31 + 2 * 32
