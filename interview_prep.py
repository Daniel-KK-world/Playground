def get_prime(n):
    if n < 0:
        raise ValueError("Input must be a non-negative number")
    
    primes = []
    for num in range(2, n + 1):  # Check numbers from 2 to n
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Example usage
print(get_prime(10))  # Output: [2, 3, 5, 7]