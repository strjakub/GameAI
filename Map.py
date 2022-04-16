from typing import List


class Map:
    graininess: int = 120

    def __init__(self) -> None:
        self.blocks_height = 8
        self.blocks_width = 15
        self.pattern: List[List[int]] = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.grid = self.to_grid()

    def to_grid(self) -> List[List[int]]:
        result = [[0 for _ in range(Map.graininess * len(self.pattern[0]))] for _ in range(Map.graininess * len(self.pattern))]
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j] == 1:
                    self.add_wall(result, j, i)
                if self.pattern[i][j] == 2:
                    self.add_spike(result, j, i)

        return result

    def add_spike(self, tab: List[List[int]], x: int, y: int) -> None:
        is_floating = False
        is_upside_down = False
        if self.pattern[y - 1][x] == 0 and 0 < y < len(self.pattern) - 1 and self.pattern[y + 1][x] == 0:
            is_floating = True
        if y == 0 or self.pattern[y - 1][x] == 1:
            is_upside_down = True

        x *= Map.graininess
        y *= Map.graininess

        if is_floating:
            for i in range(Map.graininess):
                for j in range(Map.graininess):
                    if i % 2 == j % 2:
                        tab[y + i][x + j] = 2
            return

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


    # def generate(self) -> List[List[int]]:
    #     tmp = [0] * 8

    # def pattern_1_1(self, tab: List[List[int]]) -> None:
    #     tab = [0] * 8
