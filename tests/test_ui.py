import pytest  # noqa: F401
from pytest import CaptureFixture, MonkeyPatch

from dinopark.ui import (
    choose_dino,
    choose_level,
    confirm,
    display_progress,
    get_int,
    get_int_in_range,
    get_menu_choice,
)

# -----------------------------
# Tests for get_int
# -----------------------------

def test_get_int_valid(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert get_int("Enter: ") == 5


def test_get_int_negative(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str]
):
    inputs = iter(["-3", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_int("Enter: ")
    captured = capsys.readouterr()
    assert "Value cannot be negative" in captured.out
    assert result == 2


def test_get_int_invalid(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str]
):
    inputs = iter(["abc", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_int("Enter: ")
    captured = capsys.readouterr()
    assert "Invalid input!" in captured.out
    assert result == 4


# -----------------------------
# Tests for get_int_in_range
# -----------------------------

def test_get_int_in_range_valid(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert get_int_in_range("Enter: ", 0, 3) == 2


def test_get_int_in_range_outside(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str]
):
    inputs = iter(["5", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_int_in_range("Enter: ", 0, 3)
    captured = capsys.readouterr()

    assert "Value must be between 0 and 3" in captured.out
    assert result == 2


# -----------------------------
# Tests for get_menu_choice
# -----------------------------

def test_get_menu_choice(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert get_menu_choice("Choose: ", 5) == 3


# -----------------------------
# Tests for confirm
# -----------------------------

def test_confirm_yes(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert confirm("Continue") is True


def test_confirm_no(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert confirm("Continue") is False


def test_confirm_invalid_than_yes(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str]
):
    inputs = iter(["maybe", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert confirm("Continue") is True
    captured = capsys.readouterr()
    assert "Please enter y or n" in captured.out


# -----------------------------
# Tests for choose_dino
# -----------------------------

def test_choose_dino(monkeypatch: MonkeyPatch):
    dinos = {"ammonite": {}, "velociraptor": {}, "pterodactyl": {}}
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert choose_dino(dinos) == "velociraptor"


# -----------------------------
# Tests for choose_level
# -----------------------------

def test_choose_level(monkeypatch: MonkeyPatch):
    levels = {1: 0, 2: 2, 3: 1}
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert choose_level(levels) == 3


# -----------------------------
# Tests for display_progress
# ----------------------------

def test_display_progress(capsys: CaptureFixture[str]):
    progress = {
        "totems": 1,
        "golden_chest": False,
        "missing_for_next_totem": 8,
        "missing_for_golden_chest": 3,
    }

    display_progress("velociraptor", progress)
    captured = capsys.readouterr()

    assert "VELOCIRAPTOR PROGRESS" in captured.out
    assert "Totems: 1" in captured.out
    assert "Golden chest: False" in captured.out
    assert "Missing for next totem: 8" in captured.out
    assert "Missing for golden chest: 3" in captured.out
