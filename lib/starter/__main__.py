import sys

from .series import fibonacci_series


def main():
    series = fibonacci_series(int(sys.argv[1]))
    print(" ".join(str(item) for item in series))


if __name__ == "__main__":
    main()
