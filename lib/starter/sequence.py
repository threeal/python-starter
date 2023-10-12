def fibonacci_sequence(n: int) -> list[int]:
    sequence = [0, 1]
    for i in range(n - 1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[1:]
