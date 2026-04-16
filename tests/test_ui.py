import pytest
from pytest import CaptureFixture, MonkeyPatch

from dinopark.ui import (
    choose_dino,
    choose_level,
    confirm,
    display_progress,
    get_safe_number,
)


# ----------------------------
# Tests for get_safe_number
# ----------------------------


def test_get_safe_number_valid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert get_safe_number("Enter: ") == 3


def test_get_safe_number_out_of_range(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["7", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_safe_number("Enter: ")
    captured = capsys.readouterr()
    assert "Wrong!" in captured.out
    assert result == 3


def test_get_safe_number_invalid_input(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["abc", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_safe_number("Enter: ")
    captured = capsys.readouterr()
    assert "Invalid input!" in captured.out
    assert result == 2


def test_get_safe_number_multiple_invalid_inputs(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["abc", "7", "-1", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_safe_number("Enter: ")
    captured = capsys.readouterr()
    assert "Invalid input!" in captured.out
    assert "Wrong!" in captured.out
    assert result == 3


@pytest.mark.parametrize("val", ["0", "6"])
def test_get_safe_number_number_boundary(
    monkeypatch: MonkeyPatch, val: str
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: val)
    assert get_safe_number("Enter: ") == int(val)


# -----------------------------
# Tests for confirm
# -----------------------------


def test_confirm_yes(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert confirm("Continue") is True


def test_confirm_no(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert confirm("Continue") is False


def test_confirm_invalid_then_yes(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(["maybe", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert confirm("Continue") is True
    captured = capsys.readouterr()
    assert "Please enter y or n." in captured.out


# -----------------------------
# Tests for choose_dino
# -----------------------------


def test_choose_dino(monkeypatch: MonkeyPatch) -> None:
    dinos: dict[str, dict] = {
        "ammonite": {},
        "spinosaurus": {},
        "velociraptor": {},
    }
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert choose_dino(dinos) == "TRex"


# -----------------------------
# Tests for choose_level
# -----------------------------


def test_choose_level(monkeypatch: MonkeyPatch) -> None:
    levels = {"6": 0, "5": 2, "4": 1}
    monkeypatch.setattr("builtins.input", lambda _: "1")  # highest level = 6
    assert choose_level(levels) == "6"


# -----------------------------
# Tests for display_progress
# -----------------------------


def test_display_progress(capsys: CaptureFixture[str]) -> None:
    progress = {
        "totems": 1,
        "golden_chest": False,
        "possessed_sum": 12,
        "missing_for_next_totem": 8,
        "missing_for_golden_chest": 3,
    }

    display_progress("Raptor", progress)
    captured = capsys.readouterr()

    assert "RAPTOR PROGRESS" in captured.out
    assert "Totems: 1" in captured.out
    assert "Golden chest: False" in captured.out
    assert "Possessed sum: 12" in captured.out
    assert "Missing for next totem: 8" in captured.out
    assert "Missing for golden chest: 3" in captured.out
