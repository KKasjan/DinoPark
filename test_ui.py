import pytest
from ui import get_safe_number, display_result, get_user_input


# Test 1 - Mocking the correct input
def test_get_safe_number_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert get_safe_number("Enter: ") == 3


# Test 2 - Mocking out of range input
def test_get_safe_number_out_of_range(monkeypatch, capsys):
    inputs = iter(["7", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_safe_number("Enter: ")

    captured = capsys.readouterr()
    assert "Wrong!" in captured.out
    assert result == 3


# Test 3 - Invalid input
def test_get_safe_number_invalid_input(monkeypatch, capsys):
    inputs = iter(["abc", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_safe_number("Enter: ")

    captured = capsys.readouterr()
    assert "Invalid input!" in captured.out
    assert result == 2


# Test 4 - Multiple invalid inputs
def test_get_safe_number_multiple_invalid_inputs(monkeypatch, capsys):
    inputs = iter(["abc", "7", "-1", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_safe_number("Enter: ")

    captured = capsys.readouterr()
    assert "Invalid input!" in captured.out
    assert "Wrong!" in captured.out
    assert result == 3


# Test 5 - Parameterized test of get_safe_number
@pytest.mark.parametrize(
        "val",
        ["0", "6"]
)
def test_get_safe_number_number_boundary(monkeypatch, val):
    monkeypatch.setattr("builtins.input", lambda _: val)
    assert get_safe_number("Enter: ") == int(val)


# Test 6 - display_result - missing > 0
def test_display_result_missing(capsys):
    display_result("Dimetrodon", 5)
    captured = capsys.readouterr()
    assert "Dimetrodon: missing 5" in captured.out


# Test 7 - display_result - ready
def test_display_result_ready(capsys):
    display_result("Dimetrodon", 0)
    captured = capsys.readouterr()
    assert "ready for totem!" in captured.out


# Test 8 - get_user_input
def test_get_user_input(monkeypatch):
    inputs = iter(["1", "2", "3", "4", "5", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_user_input("Dimetrodon")

    assert result == {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6}
