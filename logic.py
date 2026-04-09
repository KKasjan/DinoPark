# Converting a quantity dictionary to a level 1 total value
def calculate_possessed_sum(counts, balances):
    total = 0
    for lvl, quantity in counts.items():
        total += quantity * balances[lvl]
    return total


# Returns how much is missing (but not less than 0)
# Normalize negative values to 0
def get_missing_amount(possessed_sum, target):
    if possessed_sum < 0:
        possessed_sum = 0

    if possessed_sum >= target:
        return 0
    return target - possessed_sum
