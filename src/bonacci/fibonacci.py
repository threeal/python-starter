"""An example module for generating a Fibonacci sequence.

This is the placeholder module of a project template; replace this module and
its tests with your own logic.
"""


def fibonacci_sequence(n: int) -> list[int]:
    """Generate a Fibonacci sequence up to the given number of terms.

    The sequence starts from `1, 1`, and exactly `n` terms are returned, so an
    `n` of 0 yields an empty sequence.
    """
    sequence = [1] * n
    for i in range(2, n):
        sequence[i] = sequence[i - 2] + sequence[i - 1]
    return sequence


__all__ = ["fibonacci_sequence"]
