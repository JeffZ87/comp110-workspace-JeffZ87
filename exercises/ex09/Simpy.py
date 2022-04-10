"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730480180"


class Simpy:
    """A Simpy object that mimics a feature in the numpy library."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor method for Simply."""
        self.values = values

    def __str__(self) -> str:
        """To string method for Simply."""
        return f"Simpy({self.values})"

    def fill(self, value: float, repeat: int) -> None:
        """Assign [values] to a list of [value] with [repeat] repeats."""
        result: list[float] = []
        for i in range(repeat):
            result.append(value)
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Assign [values] to a list ranging form [start] to [stop] with [step] as the step size."""
        assert step != 0
        result: list[float] = []
        value: float = start
        if step < 0:
            assert start > stop
            while value > stop:
                result.append(value)
                value += step
        else:
            assert start < stop
            while value < stop:
                result.append(value)
                value += step

        self.values = result
        
    def sum(self) -> float:
        """Return the sum of all items in the values list."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the add operator for python; add either a float point value or a Simpy object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1

        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the power operator for python; exponent either a float point value or a Simpy object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else: 
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1

        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check if the float or each Simpy element is equal."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1

        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check if self is greater than the float or each Simpy element."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1

        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Get an item with index or get a Simpy object with a boolean mask."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result        