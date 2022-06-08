import pygame as pg


class MapBlock:

    def __init__(self, x, y, color, block_type, block_width, block_height):
        y = y + 1
        self.x = x
        self.y = y
        self.block_width = block_width
        self.block_height = block_height
        if block_type == "block":
            self.left = x * block_width
            self.top = y * block_height
            self.block = pg.Rect(self.left, self.top, block_width, block_height)
        elif block_type == "spike":
            self.left_bot = [x * block_width, y * block_height + block_height]
            self.right_bot = [x * block_width + block_width, y * block_height + block_height]
            self.mid_top = [(self.left_bot[0] + self.right_bot[0]) // 2, y * block_height]
        else:
            self.left_top = [x * block_width, y * block_height]
            self.right_top = [x * block_width + block_width, y * block_height]
            self.mid_bot = [(self.left_top[0] + self.right_top[0]) // 2, y * block_height + block_height]

        self.color = color
        self.type = block_type

    def draw(self, screen):
        if self.type == "block":
            pg.draw.rect(screen, self.color, self.block)
        elif self.type == "spike":
            pg.draw.polygon(screen, self.color, (self.left_bot, self.mid_top, self.right_bot))
        else:
            pg.draw.polygon(screen, self.color, (self.left_top, self.mid_bot, self.right_top))

    def move(self, move_value):
        if self.type == "block":
            self.block.left -= move_value
        elif self.type == "spike":
            self.left_bot[0] -= move_value
            self.mid_top[0] -= move_value
            self.right_bot[0] -= move_value
        else:
            self.left_top[0] -= move_value
            self.mid_bot[0] -= move_value
            self.right_top[0] -= move_value

    def in_borders(self):
        if self.type == "block":
            return self.block.left > -self.block_width
        elif self.type == "spike":
            return self.left_bot[0] > -self.block_width
        return self.left_top[0] > -self.block_width
