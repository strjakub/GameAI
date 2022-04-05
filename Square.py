from Vector import Vector
from Map import Map


class Square:
    jumpPower: Vector = Vector(0, -5)
    gravity: Vector = Vector(0, 1)

    def __init__(self, position: Vector, board: Map) -> None:
        self.position = position
        self.map = board
        self.velocity: Vector = Vector(3, 0)

    def __str__(self) -> str:
        return f"position: {self.position}\nvelocity: {self.velocity}\n{self.is_stable()}\n{self.is_dead()}"

    def jump(self) -> None:
        if self.is_stable():
            self.velocity.add(Square.jumpPower)

    def move(self) -> None:
        self.position.add(self.velocity)
        if not self.is_stable():
            self.velocity.add(Square.gravity)
        else:
            self.velocity.y = 0

    def is_stable(self) -> bool:
        y = (self.position.y + 1) // 10
        x = self.position.x // 10
        flag = self.position.x % 10
        if self.map.pattern[y][x] == 1 or self.map.pattern[y][x + 1] == 1 and not flag:
            return True
        return False

    def is_dead(self) -> int:
        grid = self.map.to_grid()
        if grid[self.position.y][self.position.x] != 0 or\
                self.position.y - 9 >= 0 and grid[self.position.y - 9][self.position.x] != 0 or\
                self.position.x + 9 < len(grid[self.position.y]) and grid[self.position.y][self.position.x + 9] != 0 or\
                self.position.y - 9 >= 0 and self.position.x + 9 < len(grid[self.position.y]) and grid[self.position.y - 9][self.position.x + 9] != 0:
            return self.position.x
        return -1
