"""An example main Python module."""

import sys

from . import fibonacci_sequence


def main() -> None:
    """Print a Fibonacci sequence based on user input."""
    sequence = fibonacci_sequence(int(sys.argv[1]))
    print(" ".join(str(item) for item in sequence))


if __name__ == "__main__":
    main()
