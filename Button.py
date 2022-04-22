import pygame as pg

class Button:
    def __init__(self, screen, text, pos, font, width, height):
        self.pos = pos
        self.pressed = False
        self.screen = screen
        self.top_rect = pg.Rect(pos, (width, height))
        self.top_color = (100, 100, 200)
        self.text_surf = font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self) -> None:
        pg.draw.rect(self.screen, self.top_color, self.top_rect, border_radius=12)
        self.screen.blit(self.text_surf, self.text_rect)

    def check_click(self) -> bool:
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (200, 100, 100)
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    return True
        else:
            self.top_color = (100, 100, 200)
            return False
