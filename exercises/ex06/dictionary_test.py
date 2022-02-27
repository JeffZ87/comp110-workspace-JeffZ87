"""Unit test for ex06 dictionary."""

__author__ = "730480180"

import pytest
from exercises.ex06.dictionary import count, favorite_color, invert
# from dictionary import invert
# from dictionary import favorite_color
# from dictionary import count


def test_invert_duplicate_key_value() -> None:
    """Test an edge case with repeated key-value pair for dictionary."""
    with pytest.raises(KeyError):
        my_dictionary: dict[str, str] = {"jeff": "jeff", "joe": "jeff"}
        invert(my_dictionary)


def test_invert_three_key_value_pair() -> None:
    """Test an use case with three key-value pairs."""
    my_dictionary: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(my_dictionary) == {"b": "a", "d": "c"}


def test_invert_five_key_value_pair() -> None:
    """Test an use case with five key-value pairs."""
    my_dictionary: dict[str, str] = {"a": "b", "c": "d", "e": "f", "g": "h", "i": "j"}
    assert invert(my_dictionary) == {"b": "a", "d": "c", "f": "e", "h": "g", "j": "i"}


def test_favorite_color_empty_dictionary() -> None:
    """Test an edge case with empty dictionary object."""
    my_dictionary: dict[str, str] = dict()
    assert favorite_color(my_dictionary) == "No color"


def test_favorite_color_four_element_dictionary() -> None:
    """Test an use case with dictionary object with four elements."""
    my_dictionary: dict[str, str] = {"a": "red", "c": "blue", "e": "red", "g": "blue", "i": "yellow"}
    assert favorite_color(my_dictionary) == "red"


def test_favorite_color_one_color_dictionary() -> None:
    """Test an use case with dictionary object with only one color type."""
    my_dictionary: dict[str, str] = {"a": "red", "c": "red", "e": "red", "g": "red", "i": "red"}
    assert favorite_color(my_dictionary) == "red"


def test_count_no_element() -> None:
    """Test an edge case with empty dictionary object."""
    my_list: list[str] = list()
    assert count(my_list) == {}


def test_count_no_repeat_list() -> None:
    """Test an use case with no repeat element in the list."""
    my_list: list[str] = ["hello", "world", "hi", "bye", "jk", "nvm"]
    assert count(my_list) == {"hello": 1, "world": 1, "hi": 1, "bye": 1, "jk": 1, "nvm": 1}


def test_count_two_repeat_list() -> None:
    """Test an use case with two repeated element in the list."""
    my_list: list[str] = ["hello", "world", "hello", "bye", "world", "nvm"]
    assert count(my_list) == {"hello": 2, "world": 2, "bye": 1, "nvm": 1}