from typing import Tuple
from Map import Map
from Square import Square
from Vector import Vector
from MapBlock import MapBlock

import pygame as pg
import sys


class Gui:
    map: Map
    width: int
    height: int
    size: Tuple[int, int]
    FPS: int
    block_width: int = 0
    block_height: int = 0
    light_blue = pg.Color(135, 206, 250)
    black = pg.Color(0, 0, 0)
    red = pg.Color(255, 0, 0)

    def __init__(self, game_map, game_player):
        pg.init()
        self.map = game_map
        self.player = game_player
        self.width = 800
        self.height = 640
        self.size = self.width, self.height
        self.FPS = 60
        self.screen = pg.display.set_mode(self.size)
        Gui.block_width = self.width // self.map.blocks_width
        Gui.block_height = self.height // self.map.blocks_height
        self.blocks = self.fill_map()
        self.iter = self.map.blocks_width + 1
        self.frame = 0
        self.slide = True
        self.jump = False

    def fill_map(self):
        blocks = []
        for y in range(self.map.blocks_height):
            for x in range(self.map.blocks_width + 1):
                if self.map.pattern[y][x] == 2:
                    blocks.append(MapBlock(x, y, Gui.red, "spike", Gui.block_width, Gui.block_height))
                elif self.map.pattern[y][x] == 1:
                    blocks.append(MapBlock(x, y, Gui.black, "block", Gui.block_width, Gui.block_height))

        blocks.append(self.player)
        return blocks

    def run(self):
        pg.display.set_caption("Geometry Dash with AI")
        clock = pg.time.Clock()

        while True:
            self.frame += 1
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                elif event.type == pg.KEYDOWN:
                    self.jump = True
                    print("JUMP!!!")

            if self.slide:
                self.screen.fill(Gui.light_blue)
                blocks_len = len(self.blocks)
                for block in self.blocks:
                    block.draw(self.screen)
                    block.move(4)

                if self.frame % (Gui.block_width // 4) == 0:
                    self.blocks = [block for block in self.blocks if isinstance(block, Square) or not isinstance(block, Square) and block.in_borders()]
                    if blocks_len != len(self.blocks):
                        for y in range(self.map.blocks_height):
                            if self.map.pattern[y][self.iter] == 1:
                                self.blocks.append(MapBlock(self.map.blocks_width, y, Gui.black, "block", Gui.block_width, Gui.block_height))
                            elif self.map.pattern[y][self.iter] == 2:
                                self.blocks.append(MapBlock(self.map.blocks_width, y, Gui.red, "spike", Gui.block_width, Gui.block_height))

                        self.iter += 1
                        if self.iter >= len(self.map.pattern[0]):
                            self.slide = False

                    self.frame = 0

            pg.display.update()
            clock.tick(self.FPS)


if __name__ == "__main__":
    graininess = 20
    game_map1 = Map()
    player = Square(Vector(20, 6 * 20), game_map1)

    gui = Gui(game_map1, player)
    gui.run()
