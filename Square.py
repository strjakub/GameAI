from Vector import Vector
from Map import Map
import pygame as pg


class Square:
    jumpPower: Vector = Vector(0, -24)
    gravity: Vector = Vector(0, 1)
    position: Vector
    board: Map
    alive: bool

    def __init__(self, position, board) -> None:
        self.position = position
        self.map = board
        self.velocity: Vector = Vector(12, 0)
        self.grid = self.map.to_grid()
        self.block = pg.Rect(Map.graininess // 2, (self.map.blocks_height - 2) * Map.graininess // 2, Map.graininess // 2, Map.graininess // 2)
        self.color = pg.Color(100, 200, 100)
        self.jump = False
        self.slide = False
        self.alive = True

    def __str__(self) -> str:
        return f"position: {self.position}\nvelocity: {self.velocity}\n{self.is_stable()}\n{self.is_dead()}"

    def make_jump(self) -> None:
        if (self.position.x // Map.graininess) + 1 < len(self.map.pattern[0]) and self.is_stable():
            self.velocity.add(Square.jumpPower)

    def move(self) -> None:
        if self.jump:
            self.make_jump()
            self.jump = False

        if self.velocity.y > self.above().y:
            self.position.add(self.above())
        else:
            self.position.add(self.velocity)

        if (self.position.x // Map.graininess) + 1 < len(self.map.pattern[0]) and not self.is_stable():
            self.velocity.add(Square.gravity)
        else:
            self.velocity.y = 0

        if self.slide:
            self.block.left += 6
        self.block.top = self.position.y // 2 - (Map.graininess // 2 - 1)

    def is_stable(self) -> bool:
        y = (self.position.y + 1) // Map.graininess
        x = self.position.x // Map.graininess
        flag = self.position.x % Map.graininess
        if self.map.pattern[y][x] == 1 or (self.map.pattern[y][x + 1] == 1 and not flag):
            return True
        return False

    def is_dead(self) -> int:
        z = Map.graininess - 1
        for i in range(Map.graininess):
            if self.position.x + i < len(self.grid[0]) and self.grid[self.position.y][self.position.x + i] != 0 or \
                    self.position.y - z >= 0 and self.grid[self.position.y - z + i][self.position.x] != 0 or \
                    self.position.x + z < len(self.grid[self.position.y]) and self.grid[self.position.y - i][self.position.x + z] != 0 or \
                    self.position.y - z >= 0 and self.position.x + z < len(self.grid[self.position.y]) and \
                    self.grid[self.position.y - z][self.position.x + z - i] != 0:
                return self.position.x
        return -1

    def above(self):
        level = self.position.y
        cnt = 0
        while level < len(self.grid) and self.grid[level][self.position.x] != 1 and self.position.x + Map.graininess - 1 < len(self.grid[0]) and self.grid[level][self.position.x + Map.graininess - 1] != 1:
            level = level + 1
            cnt = cnt + 1
        return Vector(self.velocity.x, cnt - 1)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.block)
        if self.position.x >= len(self.map.grid[0]) or self.is_dead() != -1:
            self.alive = False
