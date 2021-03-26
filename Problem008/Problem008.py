"""This is the solution to Problem 8 of Project Euler."""
"""Copyright 2021 Dimitris Mantas"""


import pickle
import time


def compute_products(of_adjacent_digits, in_number):
    """Compute the products of all N-sized groups of adjacent digits in a predefined number."""

    # Convert said number to a string.
    numberToString = str(in_number)

    # Register the list of digit group products.
    products = []

    # Build said groups.
    for i in range(len(numberToString) - of_adjacent_digits + 1):

        digit_group = numberToString[i:of_adjacent_digits + i]

        # Register the digit product of the current group.
        product = 1

        for ii in digit_group:

            product = product * int(ii)

        products.append(product)
    
    return products


# These lines are for debugging purposes.
# NUMBER = 1234567890
# NUMBER_TO_STRING = str(NUMBER)

# products = compute_products(3, NUMBER)

# print(products)
# print(max(products))
# print(NUMBER_TO_STRING[products.index(max(products)):products.index(max(products)) + 3])


if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    with open("Problem8.txt", "r") as NUMBER:
        NUMBER = int(NUMBER.read())

    NUMBER_TO_STRING = str(NUMBER)

    products = compute_products(13, NUMBER)

    print(products)
    print(max(products))
    print(NUMBER_TO_STRING[products.index(max(products)):products.index(max(products)) + 13])

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))
