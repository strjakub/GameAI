from Vector import Vector


class Square:
    jumpPower = Vector(0, 5)

    def __init__(self, vector: Vector):
        self.position = vector
        self.velocity = Vector(1, 0)

    def __str__(self):
        return f"position: {self.position}\nvelocity: {self.velocity}"

    def jump(self):
        self.velocity.add(Square.jumpPower)

    

