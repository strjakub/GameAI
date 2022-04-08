from Vector import Vector
from Map import Map, graininess
from math import floor, ceil


class Square:
    jumpPower: Vector = Vector(0, ceil(-7 * graininess / 10))
    gravity: Vector = Vector(0, floor(1 * graininess / 10))

    def __init__(self, position: Vector, board: Map) -> None:
        self.position = position
        self.map = board
        self.velocity: Vector = Vector(floor(1 * graininess / 5), 0)
        self.grid = self.map.to_grid()

    def __str__(self) -> str:
        return f"position: {self.position}\nvelocity: {self.velocity}\n{self.is_stable()}\n{self.is_dead()}"

    def jump(self) -> None:
        if self.is_stable():
            self.velocity.add(Square.jumpPower)

    def move(self) -> None:
        if self.velocity.y > self.above().y:
            self.position.add(self.above())
        else:
            self.position.add(self.velocity)

        if not self.is_stable():
            self.velocity.add(Square.gravity)
        else:
            self.velocity.y = 0


    def is_stable(self) -> bool:
        y = (self.position.y + 1) // graininess
        x = self.position.x // graininess
        flag = self.position.x % graininess
        if self.map.pattern[y][x] == 1 or (self.map.pattern[y][x + 1] == 1 and not flag):
            return True
        return False

    def is_dead(self) -> int:
        z = graininess - 1
        grid = self.map.to_grid()
        for i in range(graininess):
            if grid[self.position.y][self.position.x + i] != 0 or \
                    self.position.y - z >= 0 and grid[self.position.y - z + i][self.position.x] != 0 or \
                    self.position.x + z < len(grid[self.position.y]) and grid[self.position.y - i][self.position.x + z] != 0 or \
                    self.position.y - z >= 0 and self.position.x + z < len(grid[self.position.y]) and \
                    grid[self.position.y - z][self.position.x + z - i] != 0:
                return self.position.x
        return -1

    def above(self):
        level = self.position.y
        cnt = 0
        grid = self.map.to_grid()
        while level < len(grid) and grid[level][self.position.x] != 1 and grid[level][self.position.x + graininess - 1] != 1:
            level = level + 1
            cnt = cnt + 1
        return Vector(self.velocity.x, cnt - 1)

    # !!
    def contain_square_body(self, x: int, y: int) -> bool:
        return self.position.x <= x < self.position.x + graininess and self.position.y >= y > self.position.y - graininess
