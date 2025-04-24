def print_fibonacci_sequence(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    a, b = 0, 1
    for _ in range(n + 1):  # +1 to include the n-th term
        print(a, end=" ")
        a, b = b, a + b

print_fibonacci_sequence(5)  # Output: 0 1 1 2 3 5