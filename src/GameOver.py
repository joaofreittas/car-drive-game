import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from src.util.Const import GAME_OVER_MENU_OPTION, C_ORANGE, WIN_WIDTH, C_YELLOW, C_WHITE


class GameOver:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets-game/window.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        # pygame.mixer_music.load('./asset/Menu.mp3')
        # pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Game Over", C_ORANGE, ((WIN_WIDTH / 2), 50))

            for i in range(len(GAME_OVER_MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, GAME_OVER_MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, GAME_OVER_MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(GAME_OVER_MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(GAME_OVER_MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return GAME_OVER_MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
