"""A Fibonacci sequence generator module."""


def fibonacci_sequence(n: int) -> list[int]:
    """Generate a Fibonacci sequence up to the given number of terms."""
    if n <= 0:
        return []
    if n == 1:
        return [1]

    sequence = [1, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-2] + sequence[-1])

    return sequence


__all__ = ["fibonacci_sequence"]
