"""Tests for linked list utils."""

import pytest
from typing import Optional
from exercises.ex10.linked_list import Node, is_equal, last, value_at, max, linkify, scale

__author__ = "730480180"


def test_is_equal_empty() -> None:
    """Two empty Linked List should equal."""
    assert is_equal(None, None) is True


def test_is_equal_non_empty_list() -> None:
    """Two Linked List of the same order and values should return True."""
    lhs: Optional[Node] = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    rhs: Optional[Node] = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    assert is_equal(lhs, rhs) is True


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_out_of_bound() -> None:
    """Index out of valide range should raise IndexError."""
    linked_list: Optional[Node] = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 5)


def test_value_at_second_index() -> None:
    """The value of the second index of Linked List should be 2."""
    linked_list: Optional[Node] = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_max_empty() -> None:
    """max() should return ValueError when an empty Linked List is inputted."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """With a randomly generated Linked List, max function should return 5."""
    linked_list: Optional[Node] = Node(3, Node(2, Node(5, Node(4, Node(5, None)))))
    assert max(linked_list) == 5


def test_linkify_empty() -> None:
    """An empty list should not generate a Node. Instead, return a None."""
    assert linkify([]) is None


def test_linkify_non_empty() -> None:
    """Linkify should return the node head of a linked list that links the nodes in the same order and value as list."""
    assert is_equal(linkify([1, 2, 3, 4, 5]), Node(1, Node(2, Node(3, Node(4, Node(5, None)))))) is True


def test_scale_factor_of_zero() -> None:
    """Factoring by a scale of zero should change all data in nodes to zero."""
    assert is_equal(scale(linkify([1, 2, 3, 4, 5]), 0), Node(0, Node(0, Node(0, Node(0, Node(0, None)))))) is True


def test_scale_factor_of_2() -> None:
    """Factoring by a scale of zero should change all data in nodes to zero."""
    assert is_equal(scale(linkify([1, 2, 3, 4, 5]), 2), Node(2, Node(4, Node(6, Node(8, Node(10, None)))))) is True
