"""This is the solution to Problem 6 of Project Euler."""
"""Copyright 2021 Dimitris Mantas"""


import time


def compute_all_squares(of_range):
    """Compute the squares of all the natural numbers in a range."""
    
    # Register the list of squares.
    squares = []

    for i in range(of_range):
        squares.append(i*i)
    
    return squares

# This line is for debugging purposes.
# print(compute_all_squares(11))
# print(sum(compute_all_squares(11)))


if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    ans = sum([i for i in range(101)])**(2) - sum(compute_all_squares(101))

    print(ans)

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))