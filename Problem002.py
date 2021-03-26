"""This is the solution to Problem 2 of Project Euler."""
"""Copyright 2021 Dimitris Mantas"""


import time


def GenerateTheFibonacciSequence():
    """Generate The Fibonacci Sequence."""

    # Register F1 and F2.
    F1, F2 =  0, 1

    while True:
        yield F1
        
        F1, F2 = F2, F1 + F2


# These lines are for debugging purposes.
# Register a generator for The Fibonacci Sequence.
# TheFibonacciSequence = GenerateTheFibonacciSequence()

# Register a dump list for said generator.
# ans = []

# for _ in range(12): # Generate the first twelve terms of The Fibonacci Sequence.
#     ans.append(next(TheFibonacciSequence))

# print(ans)


if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    TheFibonacciSequence = GenerateTheFibonacciSequence() 

    # Keep producing the next term in The Fibonacci Sequence until the value of said term becomes greater than four million.
    i = 0

    ii = next(TheFibonacciSequence)

    while ii <= 4 * (10**(6)):
        i += 1

        ii = next(TheFibonacciSequence)

    # Register said generator once more in order to bring it back to its original state.
    TheFibonacciSequence = GenerateTheFibonacciSequence()

    ans = []

    for _ in range(i):
        iii = next(TheFibonacciSequence)

        if not iii % 2:
            ans.append(iii)

    print(ans)
    print(sum(ans))

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))
