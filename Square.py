from Vector import Vector
from Map import Map


class Square:
    jumpPower = Vector(0, -5)
    gravity = Vector(0, 1)

    def __init__(self, vector: Vector, board: Map):
        self.position = vector
        self.velocity = Vector(1, 0)
        self.map = board

    def __str__(self):
        return f"position: {self.position}\nvelocity: {self.velocity}\n{self.isStable()}"

    def jump(self):
        if self.isStable():
            self.velocity.add(Square.jumpPower)

    def move(self):
        self.position.add(self.velocity)
        if not self.isStable():
            self.velocity.add(Square.gravity)
        else:
            self.velocity.y = 0

    def isStable(self):
        y = (self.position.y + 1) // 10
        x = self.position.x // 10
        flag = self.position.x % 10
        if self.map.pattern[y][x] == 1 or self.map.pattern[y][x + 1] == 1 and not flag:
            return True
        return False
