from typing import List


class Map:
    def __init__(self) -> None:
        self.pattern: List[List[int]] = [
            [0] * 10,
            [0] * 10,
            [0] * 10,
            [0] * 10,
            [0] * 10,
            [2] * 10
        ]

    def to_grid(self) -> List[List[int]]:
        result = []
        dictionary = {}
        for i in range(len(self.pattern)):
            tab = []
            for j in range(len(self.pattern[i])):
                if self.pattern[i][j] == 2:
                    dictionary[(i, j)] = 1
                for _ in range(10):
                    tab.append(self.pattern[i][j])
            for _ in range(10):
                result.append(tab.copy())

        for key in dictionary:
            self.add_spike(result, key[1], key[0])
        return result

    def add_spike(self, tab: List[List[int]], x: int, y: int) -> None:
        x *= 10
        y *= 10
        memory = 0
        for i in range(10):
            memory += 1
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
