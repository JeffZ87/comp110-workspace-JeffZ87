"""Unit testing for exercise 05 utils.py."""

__author__ = "730480180"

# from exercises.ex05.utils import only_evens
# from exercises.ex05.utils import sub
# from exercises.ex05.utils import concat

from utils import only_evens, sub, concat


def test_only_even_empty_list() -> None: 
    """Test only_even() with empty list; expecting empty list. Test edge case with empty list."""
    assert only_evens([]) == []


def test_only_even_three_elements() -> None: 
    """Test only_even() with three element list; expecting [2]. Test use case."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_even_even_list() -> None: 
    """Test only_even() with all even elements [2, 4, 6, 8]; expecting [2, 4, 6, 8]. Test use case."""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_sub_empty_list() -> None: 
    """Test sub with empty list; expecting empty list. Test edge case with empty list."""
    assert sub([], 0, 0) == []


def test_sub_three_element() -> None: 
    """Test sub with [1, 2, 3]; expecting [1,2]. Test use case."""
    assert sub([1, 2, 3], 0, 2) == [1, 2]


def test_sub_same_int() -> None: 
    """Test sub with same integer value on each element; expecting a sub-list with same elements. Test use case."""
    assert sub([1, 1, 1, 1, 1, 1], 2, 6) == [1, 1, 1, 1]


def test_concat_two_empty_list() -> None: 
    """Test concat with two empty list as input; expecting empty list. Test edge case with empty lists."""
    assert concat([], []) == []


def test_concat_three_elements() -> None: 
    """Test concat with two lists each with three elements; expecting the first list then a second list combined into a single list. Test use case with matching length list."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_random_elements() -> None: 
    """Test concat with two lists each with random number of elements; expecting the first list then a second list combined into a single list. Test use case with not matching length list."""
    assert concat([1, 2], [3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
