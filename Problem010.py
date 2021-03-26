"""This is the solution to Problem 10 of Project Euler."""
"""Copyright 2021 Dimitris Mantas"""


import time


def is_prime(number):
    """Check if a number is prime."""
    
    # In case the number is in the range [0, 3], then the result happens to be the same as the logical expression: N > 1.
    if number <= 3:
        return number > 1

    # Check if said number is divisible by either two or three.
    if not number % 2 or not number % 3:
        return False


    # This is a prime number in the form 6k +/- 1, where k = {1, 2, 3,...}.
    i = 5 # This is the smallest number in said form for k = 1.

    while i**(2) <= number:
        if not number % i or not number % (i + 2): # This is the smallest number in said form for k = 1.
            return False

        i += 6 # This is the same as incrementing the value of k.

    # In case the number has no divisors in the range [2, sqrt(N)], then it must be prime.
    return True


def GenerateThePrimeNumbers():
    """Generate the prime numbers."""
    # Register P1.
    P1 = 2
    
    while True:
        if is_prime(P1):
            yield P1
        
        P1 += 1


# These lines are for debugging purposes.
# Register a generator for the prime numbers.
# ThePrimeNumbers = GenerateThePrimeNumbers()

# Register a dump list for said generator.
# ans = []

# for _ in range(10): # Generate the first 10 prime numbers.
#     ans.append(next(ThePrimeNumbers))

# print(ans)
# print(sum(ans))


if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    ThePrimeNumbers = GenerateThePrimeNumbers()

    ans = [next(ThePrimeNumbers)]

    while ans[-1] < 2000000:
        ans.append(next(ThePrimeNumbers))
    
    if ans[-1] >= 2000000:
        ans.pop(-1)
    
    print(ans)
    print(sum(ans))

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))