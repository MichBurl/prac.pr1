def nth_prime(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer greater than 0."

    primes = []
    num = 2

    while len(primes) < n:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1

    return primes[-1]

# Test cases:
print("f(1) returns:", nth_prime(1))  # Output: 2
print("f(5) returns:", nth_prime(5))  # Output: 11
