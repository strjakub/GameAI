from Button import Button
from Map import Map
from Square import Square
from Vector import Vector
from Gui import Gui
import pygame as pg
import sys


if __name__ == '__main__':
    first_stage_done = False
    second_stage_done = False
    third_stage_done = False
    ML = False
    is_hover = False
    length = 0

    pg.init()
    width = 900
    height = 540
    size = width, height
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Geometry Dash with AI")
    clock = pg.time.Clock()
    gui = None

    button_font = pg.font.Font(None, 30)
    rect = pg.Rect((0, 0), (width, height))
    text_surf = pg.font.Font(None, 60).render("Loading...", True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=rect.center)

    button1 = Button(screen, "Machine Learning", (75, 70), button_font, 300, 80)
    button2 = Button(screen, "Casual Gameplay", (525, 70), button_font, 300, 80)
    button3 = Button(screen, "With Hover", (75, 185), button_font, 300, 80)
    button4 = Button(screen, "Non Hover", (525, 185), button_font, 300, 80)
    button5 = Button(screen, "Tiny", (75, 335), button_font, 150, 80)
    button6 = Button(screen, "Short", (275, 335), button_font, 150, 80)
    button7 = Button(screen, "Long", (475, 335), button_font, 150, 80)
    button8 = Button(screen, "Super Long", (675, 335), button_font, 150, 80)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((200, 200, 200))
        if not first_stage_done:
            button1.draw()
            button2.draw()
        elif not second_stage_done:
            button3.draw()
            button4.draw()
        elif not third_stage_done:
            button5.draw()
            button6.draw()
            button7.draw()
            button8.draw()
        else:
            screen.blit(text_surf, text_rect)
            pg.display.update()
            game_map1 = Map(length)
            player = Square(Vector(Map.graininess, (game_map1.blocks_height - 1) * Map.graininess - 1), game_map1)
            gui = Gui(game_map1, player, screen, width, height, is_hover)
            break

        if button1.check_click():
            first_stage_done = True
            second_stage_done = True
            third_stage_done = True
            ML = True
        if button2.check_click():
            first_stage_done = True

        if button3.check_click():
            is_hover = True
            second_stage_done = True
        if button4.check_click():
            second_stage_done = True

        if button5.check_click():
            third_stage_done = True
            length = 100
        if button6.check_click():
            third_stage_done = True
            length = 200
        if button7.check_click():
            third_stage_done = True
            length = 300
        if button8.check_click():
            third_stage_done = True
            length = 400

        pg.display.update()
        clock.tick(60)

    if third_stage_done and not ML:
        gui.run()
    elif third_stage_done and ML:
        print("ML")
        exit(0)
    else:
        pass
