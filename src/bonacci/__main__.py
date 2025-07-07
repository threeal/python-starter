"""Example main module for the CLI application."""

import argparse
import sys

from . import fibonacci_sequence


def main() -> None:
    """Generate and print a Fibonacci sequence based on command line arguments."""
    parser = argparse.ArgumentParser(
        prog="bonacci",
        description="Generate a Fibonacci sequence up to the given number of terms",
    )
    parser.add_argument("-v", "--version", action="version", version="0.0.0")
    parser.add_argument("n", type=int, help="The number of terms")
    args = parser.parse_args()

    sequence = fibonacci_sequence(args.n)
    sys.stdout.write(f"{' '.join(str(item) for item in sequence)}\n")


if __name__ == "__main__":
    main()
