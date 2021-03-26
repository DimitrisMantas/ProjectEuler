"""This is the solution to Problem 3 of Project Euler."""
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


def compute_all_prime_factors(of_number):
    """Compute all prime and non-prime factors of a natural number."""

    def compute_smallest_prime_factor(of_number):
        """Compute the smallest prime factor of a natural number."""

        # Register a generator for the prime sequence.
        ThePrimeNumbers = GenerateThePrimeNumbers()

        # Keep producing the next term in said sequence until the remainder of the operation N % P is equal to zero.
        i = next(ThePrimeNumbers)

        # Compute the quotient and the remainder of said operation.
        q, r = divmod(of_number, i)

        while r:
            i = next(ThePrimeNumbers)

            q, r = divmod(of_number, i)
        
        return i, q

    # Unpack (i, q).
    i, q = compute_smallest_prime_factor(of_number)
    
    # This guard clause is in casse the number is prime, because then the contents of (i, q) are equal to (N, 1).
    if i == of_number and q: return [q, i]

    # Register the list of prime factors.
    ii = []

    # Keep calling said function with q until q is a prime number.
    # The prime factors of the original number are all resulting values of i, as well as the last value of said remainder.
    while not is_prime(q):
        ii.append(i)

        i, q = compute_smallest_prime_factor(q)
    
    # Append the last (i, q) to the said list.
    ii.extend((i, q))

    # The resulting list can contain multiple instances of some factors. This is not a bug, but the actual prime decomposition of the number.
    # An example of said behavior is observable with 288, whose prime decomposition is equal to 2**(2) * 3 * 9.
    return ii


# These lines are for debugging purposes.
# print(compute_all_prime_factors(13195))
# print(compute_all_prime_factors(13195)[-1])
print(compute_all_prime_factors(232792560))

if __name__ == "__main__":
    # This line is for debugging purposes.
    # Start measuring the program runtime.
    runtime = time.time()

    ans = compute_all_prime_factors(600851475143)

    print(ans)
    print(ans[-1])

    # These lines are for debugging purposes.
    # Compute the program runtime.
    print("This problem was solved in {0} seconds.".format(time.time() - runtime))