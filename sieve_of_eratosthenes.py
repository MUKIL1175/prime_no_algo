def sieve_of_eratosthenes(limit):
    """Returns a list of all prime numbers up to the specified limit."""
    # Handle edge case where limit is less than 2
    if limit < 2:
        return []

    # Initialize a boolean array indicating potential primality
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Start sieving
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            # Mark multiples of the current number as non-prime
            for multiple in range(number*number, limit + 1, number):
                is_prime[multiple] = False

    # Collect and return all prime numbers
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

# Example usage
limit = 30
print(sieve_of_eratosthenes(limit))
print("length: ",len(sieve_of_eratosthenes(limit)))