from my_fibonacci import fibonacci_sequence


def test_fibonacci_sequence() -> None:
    assert fibonacci_sequence(-1) == []
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [1]
    assert fibonacci_sequence(2) == [1, 1]
    assert fibonacci_sequence(5) == [1, 1, 2, 3, 5]
