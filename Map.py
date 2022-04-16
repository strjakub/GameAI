from typing import List
from random import randint


class Map:
    graininess: int = 120

    def __init__(self) -> None:
        self.blocks_height = 8
        self.blocks_width = 15
        self.pattern: List[List[int]] = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        self.generate()
        self.grid = self.to_grid()

    def to_grid(self) -> List[List[int]]:
        result = [[0 for _ in range(Map.graininess * len(self.pattern[0]))] for _ in range(Map.graininess * len(self.pattern))]
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j] == 1:
                    self.add_wall(result, j, i)
                if self.pattern[i][j] == 2 or self.pattern[i][j] == 3:
                    self.add_spike(result, j, i)

        return result

    def add_spike(self, tab: List[List[int]], x: int, y: int) -> None:
        is_upside_down = False
        if y == 0 or self.pattern[y - 1][x] == 1:
            is_upside_down = True

        x *= Map.graininess
        y *= Map.graininess

        if not is_upside_down:
            for i in range(1, Map.graininess + 1):
                for j in range(1, Map.graininess):
                    if i / j <= 2 and i / (j - Map.graininess) >= -2:
                        tab[y + Map.graininess - i][x + j] = 2
        else:
            for i in range(1, Map.graininess + 1):
                for j in range(1, Map.graininess):
                    if i / j <= 2 and i / (j - Map.graininess) >= -2:
                        tab[y + i - 1][x + j] = 2


    def add_wall(self, tab: List[List[int]], x: int, y: int) -> None:
        x *= Map.graininess
        y *= Map.graininess
        for i in range(Map.graininess):
            for j in range(Map.graininess):
                tab[y + i][x + j] = 1

    def generate(self) -> None:
        start_level = 1
        for i in range(30):
            filename = "pattern_" + str(start_level) + "_"
            x = randint(1, 6)
            filename = filename + str(x) + ".txt"
            file = open(filename, "r")
            tab = file.read().split('\n')
            for j in range(len(tab)):
                for k in tab[j]:
                    self.pattern[j].append(int(k))
            start_level = 0
            for j in range(len(self.pattern) - 1, len(self.pattern) - 4, -1):
                if self.pattern[j][len(self.pattern[j]) - 1] != 0:
                    start_level = start_level + 1
                else:
                    break

        for i in range(10):
            for j in range(len(self.pattern)):
                if j < len(self.pattern) - 1:
                    self.pattern[j].append(0)
                else:
                    self.pattern[j].append(1)
