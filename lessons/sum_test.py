"""Test for sum function."""

from lessons.sum import sum


def test_sum_empty() -> None:
    assert sum([]) == 0.0


def test_sum_single_item() -> None:
    assert sum([110.0]) == 110.0


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6


def test_sum_many_items_zero_sum() -> None:
    assert sum([-1.0, 1.0, -2.0, 2.0]) == 0.0