from typing import List


class Map:
    def __init__(self) -> None:
        self.pattern: List[List[int]] = [
            [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def to_grid(self) -> List[List[int]]:
        result = [[0 for _ in range(10 * len(self.pattern[0]))] for _ in range(10 * len(self.pattern))]
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j] == 1:
                    self.add_wall(result, j, i)
                if self.pattern[i][j] == 2:
                    self.add_spike(result, j, i)

        return result


    def add_spike(self, tab: List[List[int]], x: int, y: int) -> None:
        is_upside_down = False
        if y == 0 or self.pattern[y - 1][x] == 1:
            is_upside_down = True

        x *= 10
        y *= 10
        memory = 0
        if is_upside_down:
            memory = 11

        for i in range(10):
            if not is_upside_down:
                memory += 1
                memory2 = memory
                if memory % 2:
                    memory += 1
                tmp = (10 - memory) // 2
            else:
                memory -= 1
                memory2 = memory
                if memory % 2:
                    memory += 1
                tmp = (10 - memory) // 2

            for o in range(tmp):
                tab[y + i][x + o] = 0
            for o in range(memory):
                tab[y + i][x + tmp + o] = 2
            for o in range(tmp):
                tab[y + i][x + tmp + memory + o] = 0

            memory = memory2

    def add_wall(self, tab: List[List[int]], x: int, y: int) -> None:
        x *= 10
        y *= 10
        for i in range(10):
            for j in range(10):
                tab[y + i][x + j] = 1
