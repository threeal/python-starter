"""A Fibonacci sequence generator module."""


def fibonacci_sequence(n: int) -> list[int]:
    """Generate a Fibonacci sequence up to the given number of terms."""
    sequence = [0, 1]
    for _ in range(n - 1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[1:]


__all__ = ["fibonacci_sequence"]
