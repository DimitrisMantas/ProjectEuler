"""This is the solution to Problem 5 of Project Euler."""
"""Copyright 2021 Dimitris Mantas"""


import time


def compute_smallest_multiple(of_range):
    """Compute the smallest natural number, which is a multiple of all natural numbers in a predefined range."""

    # Some numbers in the range (N/2, N] happen to be multiples of the numbers in the range [1, N/2], so only the first one must be generated.
    rangeToList = list(range(int(0.5 * (of_range - 1)) + 1, of_range))

    # Check all numbers in the range [N, ∞) and keep track of the amount of their divisors.
    i = of_range - 1

    ii = 0

    for iii in rangeToList:
        if not i % iii:
            ii += 1

    while not ii == len(rangeToList):
        # Check all numbers in the form kN, where k = {0, 1, 2,...}.
        i += of_range - 1

        ii = 0

        for iii in rangeToList:
            if not i % iii:
                ii += 1

    return i


# This line is for debugging purposes.
# print(compute_smallest_multiple(11))


if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    ans = compute_smallest_multiple(21)

    print(ans)

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))
