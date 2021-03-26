"""This is the solution to Problem 4 of Project Euler."""
"""Copyright 2021 Dimitris Mantas"""


import time


def compute_all_palindromes(of_digit_numbers):
    """Compute the largest palindromic number, which is the result of the product of two natural numbers, which have the same amount of digits."""

    # Register the list of palindromes.
    palindromes = []

    # This is loop in the range [10**(N - 1), 10**(N) + 1], which happens to be the range of all N-digit numbers.
    for i in range(10**(of_digit_numbers - 1), 10**(of_digit_numbers) - 1 + 1): # This is the first N-digit number.
        for ii in range(10**(of_digit_numbers - 1), 10**(of_digit_numbers) - 1 + 1): # his is the second N-digit number.

            productToNumber = i * ii
            productToString = str(productToNumber)

            if productToString == productToString[::-1]:
                palindromes.append(productToNumber)
    
    return palindromes


# These lines are for debugging purposes.
# print(compute_all_palindromes(2))
# print(max(compute_all_palindromes(2)))


if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    ans = compute_all_palindromes(3)

    print(ans)
    print(max(ans))

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))