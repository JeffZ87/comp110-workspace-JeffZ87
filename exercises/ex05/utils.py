"""Exercise 05 utility file write out."""

__author__ = "730480180"


def only_evens(int_list: list[int]) -> list[int]:
    """Given a list of integers, it will return a list of even integers withing the original list."""
    even_list: list[int] = list()
    i: int = 0

    while i < len(int_list):
        is_even: bool = int_list[i] % 2 == 0
        if is_even:
            even_list.append(int_list[i])
        i += 1

    return even_list


def sub(int_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list of integers, a start_index, and an end_index, it will return a sub list of the input list starting and the start_index and end with the end_index(not conclusive)."""
    sub_list: list[int] = list()

    if len(int_list) == 0 or start_index > len(int_list) or end_index <= 0:
        return sub_list

    if start_index < 0:
        start_index = 0

    if end_index > len(int_list):
        end_index = len(int_list)

    i: int = start_index

    while i < end_index:
        sub_list.append(int_list[i])
        i += 1

    return sub_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combines two lists into a single list."""
    concat_list: list[int] = list()
    i: int = 0

    while i < len(list1):
        concat_list.append(list1[i])
        i += 1

    i = 0

    while i < len(list2):
        concat_list.append(list2[i])
        i += 1

    return concat_list