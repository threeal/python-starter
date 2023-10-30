import sys

from .sequence import fibonacci_sequence


def main():
    """Main function to print a Fibonacci sequence based on user input."""
    sequence = fibonacci_sequence(int(sys.argv[1]))
    print(" ".join(str(item) for item in sequence))


if __name__ == "__main__":
    main()
