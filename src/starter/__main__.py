import sys
from . import fibonacci_series

if __name__ == "__main__":
    series = fibonacci_series(int(sys.argv[1]))
    print(" ".join(str(item) for item in series))
