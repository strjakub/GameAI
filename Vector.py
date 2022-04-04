class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def add(self, other: "Vector") -> None:
        self.x += other.x
        self.y += other.y

    def __eq__(self, other: "Vector") -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x} ; {self.y})"
