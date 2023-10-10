#!/usr/bin/env python3

def print_fibonacci(length):
    if length < 0:
        return []

    # Initialize the first two Fibonacci numbers
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
    if length > 1:
        fibonacci_sequence.append(1)

    # Generate the Fibonacci sequence up to the specified length
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)
