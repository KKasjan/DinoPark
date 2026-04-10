import pytest

from logic import calculate_possessed_sum, get_missing_amount


@pytest.fixture
def standard_balances() -> dict[int, int]:
    return {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}


# Test 1 - multiplication test for one level
# Expected result:
def test_calculate_possessed_sum_basic(
    standard_balances: dict[int, int]
) -> None:
    counts: dict[int, int] = {6: 1, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

    result = calculate_possessed_sum(counts, standard_balances)
    assert result == 32


# Test 2 - multiplication test for multiple levels
def test_calculate_possessed_sum_multiple_levels(
    standard_balances: dict[int, int]
) -> None:
    counts = {6: 1, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}

    # manual calculation:
    # 1*32 + 1*16 + 1*8 + 1*4 + 1*2 + 1*1 = 32 + 16 + 8 + 4 + 2 + 1 = 63
    expected = 63

    assert calculate_possessed_sum(counts, standard_balances) == expected


# Test 3 - multiplication test for missing data
def test_calculate_possessed_sum_empty(
    standard_balances: dict[int, int]
) -> None:
    counts = {}

    assert calculate_possessed_sum(counts, standard_balances) == 0


# Test 4 - Parameterized test of calculate_possessed_sum
@pytest.mark.parametrize(
    "counts, expected",
    [
        ({6: 1, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}, 32),
        ({6: 0, 5: 1, 4: 0, 3: 0, 2: 0, 1: 0}, 16),
        ({6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 0}, 8),
        ({6: 0, 5: 0, 4: 0, 3: 1, 2: 0, 1: 0}, 4),
        ({6: 0, 5: 0, 4: 0, 3: 0, 2: 1, 1: 0}, 2),
        ({6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 1}, 1),
    ],
)
def test_calculate_possessed_sum_param(
    counts: dict[int, int],
    expected: int,
    standard_balances: dict[int, int]
) -> None:
    assert calculate_possessed_sum(counts, standard_balances) == expected


# Test 5 - Case with unknown level
def test_calculate_possessed_sum_unknown_level(
    standard_balances: dict[int, int]
) -> None:
    counts = {7: 1}

    with pytest.raises(KeyError):
        calculate_possessed_sum(counts, standard_balances)


# Test 6 - Case when possessed_sum is lower than target
def test_missing_amount_positive_input() -> None:
    assert get_missing_amount(1, 63) == 62


# Test 7 - Case when the number of dinos is equal to the required number
def test_missing_amount_exact() -> None:
    assert get_missing_amount(63, 63) == 0


# Test 8 - Case when the number of dinos is greater than the required number
def test_missing_amount_overflow() -> None:
    assert get_missing_amount(70, 63) == 0


# Test 9 - Case when the number of dinos is negative
def test_missing_amount_negative_input() -> None:
    assert get_missing_amount(-1, 63) == 63


# Test 10 - Case when the number of dinos is large negative
def test_missing_amount_large_negative_input() -> None:
    assert get_missing_amount(-999, 63) == 63


# Test 11 - Parameterized test of get_missing_amount
@pytest.mark.parametrize(
    "possessed_sum, target, expected",
    [(1, 63, 62), (63, 63, 0), (-1, 63, 63), (-999, 63, 63)])
def test_get_missing_amount_parametrized(
    possessed_sum: int,
    target: int,
    expected: int
) -> None:
    assert get_missing_amount(possessed_sum, target) == expected
