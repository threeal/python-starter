def fibonacci_series(n: int) -> list[int]:
    series = [0, 1]
    for i in range(n - 1):
        series.append(series[-1] + series[-2])
    return series[1:]
