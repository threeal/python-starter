import argparse

from . import fibonacci_sequence


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bonacci",
        description="Generate a Fibonacci sequence up to the given number of terms",
    )
    parser.add_argument("-v", "--version", action="version", version="0.0.0")
    parser.add_argument("n", type=int, help="The number of terms")
    args = parser.parse_args()

    sequence = fibonacci_sequence(args.n)
    print(" ".join(str(item) for item in sequence))


if __name__ == "__main__":
    main()
