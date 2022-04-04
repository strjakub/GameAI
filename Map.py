from typing import List


class Map:
    def __init__(self) -> None:
        self.pattern: List[List[int]] = [
            [0] * 10,
            [0] * 10,
            [0] * 10,
            [0] * 10,
            [0] * 10,
            [1] * 10
        ]
