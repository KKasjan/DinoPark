from logic import calculate_possessed_sum


# Test 1 - multiplication test for one level
def test_calculate_possessed_sum_basic():
    counts = {6: 1, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    balances = {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}

    result = calculate_possessed_sum(counts, balances)

    assert result == 32


# Test 2 - multiplication test for multiple levels
def test_calculate_possessed_sum_multiple_levels():
    counts = {6: 1, 5: 1, 4: 1, 3: 1, 2: 1, 1: 1}
    balances = {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}

    # manual calculation:
    # 1*32 + 1*16 + 1*8 + 1*4 + 1*2 + 1*1 = 32 + 16 + 16 + 0 + 2 + 3 = 63
    expected = 63

    assert calculate_possessed_sum(counts, balances) == expected


# Test 3 - multiplication test for missing data
def test_calculate_possessed_sum_empty():
    counts = {}
    balances = {6: 32, 5: 16, 4: 8, 3: 4, 2: 2, 1: 1}

    assert calculate_possessed_sum(counts, balances) == 0
