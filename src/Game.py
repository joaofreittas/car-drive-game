import sys

import pygame

from src.DifficultLevel import DifficultLevel
from src.Level import Level
from src.Menu import Menu
from src.util.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                difficult_level = DifficultLevel(self.window)
                difficult_return = difficult_level.run()

                level = Level(self.window, difficult_return)
                level.run()
            if menu_return == MENU_OPTION[1]:
                pygame.quit()
                sys.exit()




