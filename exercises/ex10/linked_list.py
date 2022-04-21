"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730480180"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the value of a Linked List at specific index, or raises a IndexError when index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns the maximum value of a Linked List, or raise a  ValueError when the Linked List is empty."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    elif head.next is None:
        return head.data
    else:
        next_max = max(head.next)
        if head.data > next_max:
            return head.data
        else:
            return next_max


def linkify(items: list[int]) -> Optional[Node]:
    """Returns the head node for Linked List generated from the provided items list. The order of the original list will be kept in the new Linked List."""
    items_len: int = len(items)
    if items_len == 0:
        return None
    else:
        return Node(items.pop(0), linkify(items))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Given a head node of a Linked List and a int factor scale, return a new linked list of Nodes where the original value of each node is scaled by scaling int factor."""
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))
