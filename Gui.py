from typing import Tuple

import keyboard

from Map import Map
from MapBlock import MapBlock
from Square import Square
from Vector import Vector

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

    def __init__(self, game_map, game_player, screen, width, height, is_hover=False):
        pg.init()
        self.is_hover = is_hover
        self.map = game_map
        self.player = game_player
        self.FPS = 60
        self.screen = screen
        self.width = width
        self.height = height
        Gui.block_width = self.width // self.map.blocks_width
        Gui.block_height = self.height // (self.map.blocks_height + 1)
        self.blocks = self.fill_map()
        self.iter = self.map.blocks_width + 1
        self.frame = 0
        self.slide = True

    def fill_map(self):
        blocks = []
        for y in range(self.map.blocks_height):
            for x in range(self.map.blocks_width + 1):
                if self.map.pattern[y][x] == 2:
                    blocks.append(MapBlock(x, y, Gui.red, "spike", Gui.block_width, Gui.block_height))
                elif self.map.pattern[y][x] == 1:
                    blocks.append(MapBlock(x, y, Gui.black, "block", Gui.block_width, Gui.block_height))
                elif self.map.pattern[y][x] == 3:
                    blocks.append(MapBlock(x, y, Gui.red, "reverse_spike", Gui.block_width, Gui.block_height))

        return blocks

    def run(self, EA=None, move_list=None):
        clock = pg.time.Clock()
        i = 0
        while True:
            self.frame += 1
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            if not EA:
                keys = pg.key.get_pressed()
                if keys[pg.K_SPACE]:
                    self.player.jump = True
                if keys[pg.K_q] and self.is_hover:
                    self.player.hover_pressed = True
                else:
                    self.player.hover_pressed = False
            else:
                if move_list[i] == 1:
                    self.player.jump = True
                i += 1

            if self.player.position.x // Map.graininess >= len(self.map.pattern[0]):
                rect1 = pg.Rect((390, 180), (120, 80))
                rect2 = pg.Rect((390, 280), (120, 80))
                text_surf1 = pg.font.Font(None, 80).render("YOU WIN!", True, (0, 0, 0))
                text_surf2 = pg.font.Font(None, 40).render("('Esc' to exit)", True, (0, 0, 0))
                text_rect1 = text_surf1.get_rect(center=rect1.center)
                text_rect2 = text_surf2.get_rect(center=rect2.center)
                self.screen.blit(text_surf1, text_rect1)
                self.screen.blit(text_surf2, text_rect2)
                pg.display.update()
                while True:
                    if keyboard.is_pressed("esc"):
                        break
                return

            if self.slide and self.player.alive:
                self.screen.fill(Gui.light_blue)
                self.player.draw(self.screen)
                self.player.move()
                blocks_len = len(self.blocks)
                for block in self.blocks:
                    block.draw(self.screen)
                    block.move(6)

                if self.frame % (Gui.block_width // 6) == 0:
                    self.blocks = [block for block in self.blocks if block.in_borders()]
                    if blocks_len != len(self.blocks):
                        for y in range(self.map.blocks_height):
                            if self.map.pattern[y][self.iter] == 1:
                                self.blocks.append(MapBlock(self.map.blocks_width, y, Gui.black, "block", Gui.block_width, Gui.block_height))
                            elif self.map.pattern[y][self.iter] == 2:
                                self.blocks.append(MapBlock(self.map.blocks_width, y, Gui.red, "spike", Gui.block_width, Gui.block_height))
                            elif self.map.pattern[y][self.iter] == 3:
                                self.blocks.append(MapBlock(self.map.blocks_width, y, Gui.red, "reverse_spike", Gui.block_width, Gui.block_height))

                        self.iter += 1
                        if self.iter >= len(self.map.pattern[0]):
                            self.slide = False

                    self.frame = 0

            elif self.player.alive:
                self.player.slide = True
                self.screen.fill(Gui.light_blue)
                self.player.draw(self.screen)
                if self.player.alive:
                    self.player.move()
                for block in self.blocks:
                    block.draw(self.screen)

            else:
                rect1 = pg.Rect((390, 180), (120, 80))
                rect2 = pg.Rect((390, 280), (120, 80))
                text_surf1 = pg.font.Font(None, 60).render("Press 'R' to restart", True, (255, 255, 255))
                text_rect1 = text_surf1.get_rect(center=rect1.center)
                text_surf2 = pg.font.Font(None, 60).render("Press 'Esc' to exit", True, (255, 255, 255))
                text_rect2 = text_surf2.get_rect(center=rect2.center)
                self.screen.blit(text_surf1, text_rect1)
                self.screen.blit(text_surf2, text_rect2)
                pg.display.update()

                while True:
                    if keyboard.is_pressed("r"):
                        new_player = Square(Vector(Map.graininess, (self.map.blocks_height - 1) * Map.graininess - 1), self.map)
                        new_gui = Gui(self.map, new_player, self.screen, self.width, self.height, self.is_hover)
                        if move_list:
                            new_gui.run(EA, EA.make_evolution_step())
                        else:
                            new_gui.run()
                        break
                    if keyboard.is_pressed("esc"):
                        break
                return

            pg.draw.rect(self.screen, Gui.black, pg.Rect(0, 0, self.width, self.block_height))
            if self.is_hover:
                pg.draw.rect(self.screen, (255, 255, 255),
                             pg.Rect(self.block_width // 2, self.block_height * 1 // 4,
                                     self.block_width * 2, self.block_height // 2), 0)
                pg.draw.rect(self.screen, (255, 0, 255),
                             pg.Rect(self.block_width // 2, self.block_height * 1 // 4,
                                     self.block_width * 2, self.block_height // 2), 1)
                pg.draw.rect(self.screen, (255, 0, 255),
                             pg.Rect(self.block_width // 2, self.block_height * 1 // 4,
                                     self.block_width * 2 * self.player.hover // 80, self.block_height // 2), 0)
            pg.display.update()
            clock.tick(self.FPS)
