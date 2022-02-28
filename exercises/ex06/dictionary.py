"""Exercise 06, practice using dictionary by implementing invert(), favorite_colors(), and count() functions."""

__author__ = "730480180"


def invert(origin: dict[str, str]) -> dict[str, str]:
    """The key becomes the value of the dictionary and vice versa. If value is not unique, a KeyError is thrown."""
    invert_dict: dict[str, str] = dict()
    value_list: list[str] = list()

    for key in origin:
        # checks for repetitive values
        if origin[key] in value_list:
            raise KeyError("KeyError")

        value_list.append(origin[key])
        invert_dict[origin[key]] = key

    return invert_dict


def favorite_color(origin: dict[str, str]) -> str:
    """Given a dictionary of names and their favorite color. Return the first and most frequently color in dictionary."""
    appeared_colors_list: list[str] = list()

    for name in origin:
        appeared_colors_list.append(origin[name])

    colors_frequency: dict[str, int] = dict()

    for color in appeared_colors_list:
        colors_frequency[color] = colors_frequency.get(color, 0) + 1
    
    frequency: list[int] = list(colors_frequency.values())
    # avoid max() no argument error when the list is empty
    frequency.append(0)
    max_color_count: int = max(frequency)
    
    for color in colors_frequency:
        if colors_frequency[color] == max_color_count:
            return color

    return "No color"


def count(origin: list[str]) -> dict[str, int]:
    """Return a dictionary object with each element in list and number of times it repeats in values."""
    repeat_dict: dict[str, int] = dict()

    for key in origin:
        if key in repeat_dict:
            repeat_dict[key] += 1
        else:
            repeat_dict[key] = 1

    return repeat_dict