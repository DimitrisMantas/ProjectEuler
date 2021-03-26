"""This is the solution to Problem 1 of Project Euler."""
"""Copyright 2021 Dimitris Mantas"""


import time


def compute_all_multiples(of_number, below_number):
    """Compute all natural numbers, which are multiples of a natural number below a predefined number."""

    # Register the list of said multiples.
    multiples = []

    for i in range(1, below_number):
        if not i % of_number:
            multiples.append(i)
    
    return multiples


# These lines are for debugging purposes.
# print(compute_all_multiples(3,10))
# print(compute_all_multiples(5,10))


if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    # The resulting list is not sorted and contains the unique values the lists involved in the calculation.
    # This is because the multiples of 15 are contained on both said lists.
    ans = set([i for i in (compute_all_multiples(3, 1000) + compute_all_multiples(5, 1000))])

    print(ans)
    print(sum(ans))

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))
