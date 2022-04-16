from Vector import Vector
from Map import Map
from math import floor, ceil
import pygame as pg


class Square:
    jumpPower: Vector = Vector(0, -16)
    gravity: Vector = Vector(0, 1)
    position: Vector
    board: Map

    def __init__(self, position, board) -> None:
        self.position = position
        self.map = board
        self.velocity: Vector = Vector(6, 0)
        self.grid = self.map.to_grid()
        self.left = Map.graininess
        self.top = (self.map.blocks_height - 2) * Map.graininess
        self.block = pg.Rect(self.left, self.top, Map.graininess, Map.graininess)
        self.color = pg.Color(0, 255, 0)

    def __str__(self) -> str:
        return f"position: {self.position}\nvelocity: {self.velocity}\n{self.is_stable()}\n{self.is_dead()}"

    def jump(self) -> None:
        if self.is_stable():
            self.velocity.add(Square.jumpPower)

    def move(self, move_value) -> None:
        if self.velocity.y > self.above().y:
            self.position.add(self.above())
        else:
            self.position.add(self.velocity)

        if not self.is_stable():
            self.velocity.add(Square.gravity)
        else:
            self.velocity.y = 0

        self.left = self.position.x
        self.top = self.position.y - Map.graininess

    def is_stable(self) -> bool:
        y = (self.position.y + 1) // Map.graininess
        x = self.position.x // Map.graininess
        flag = self.position.x % Map.graininess
        if self.map.pattern[y][x] == 1 or (self.map.pattern[y][x + 1] == 1 and not flag):
            return True
        return False

    def is_dead(self) -> int:
        z = Map.graininess - 1
        grid = self.map.to_grid()
        for i in range(Map.graininess):
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
        while level < len(self.grid) and self.grid[level][self.position.x] != 1 and self.grid[level][self.position.x + Map.graininess - 1] != 1:
            level = level + 1
            cnt = cnt + 1
        return Vector(self.velocity.x, cnt - 1)

    # !!
    def contain_square_body(self, x: int, y: int) -> bool:
        return self.position.x <= x < self.position.x + Map.graininess and self.position.y >= y > self.position.y - Map.graininess

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.block)
