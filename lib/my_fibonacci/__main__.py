import sys

from . import fibonacci_sequence


def main() -> None:
    sequence = fibonacci_sequence(int(sys.argv[1]))
    print(" ".join(str(item) for item in sequence))


if __name__ == "__main__":
    main()
