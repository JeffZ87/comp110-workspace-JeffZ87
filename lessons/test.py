from __future__ import annotations
from typing import Union

class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        self.plots = []
        for i in range(initial_planting):
            self.plots.append(1)
        for i in range(plots - initial_planting):
            self.plots.append(0)

    def plant(self, plant: int) -> None:
        self.plots[plant] = 1

    def growth(self) -> None:
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1     
            i += 1

    def harvest(self, union: Union[str, int] = "", replant: bool = True) -> int:
        harvest_amount: int = 0
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] >= 5:
                harvest_amount += 1
                if replant:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
            i += 1
        return harvest_amount

    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        result: ChristmasTreeFarm = ChristmasTreeFarm(0, 0)
        for plant in self.plots:
            result.plots.append(plant)
        for plant in rhs.plots:
            result.plots.append(plant)
        return result

    # def __str__(self) -> str:
    #     result: str = ""
    #     for plot in self.plots:
    #         result += f"{plot}, "
        
    #     return result

    def __repr__(self) -> str:
        return "repr"
        

farm: ChristmasTreeFarm = ChristmasTreeFarm(5, 2)
farm2: ChristmasTreeFarm = ChristmasTreeFarm(5, 5)
farm.plant(2)
farm.growth()
farm.growth()
farm.growth()
farm.growth()
farm.growth()
print(farm + farm2)
# print(farm)
# print(farm.harvest(False))
# print(farm)

print(str(farm))