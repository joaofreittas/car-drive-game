import pygame

# C

COLLISIONS_LIMIT = 3
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# D
DIFFICULT_MENU_OPTION = ('EASY', 'MEDIUM', 'HARD', 'IMPOSSIBLE')
DIFFICULT_SPAWN_TIME = {
    'EASY': 6000,
    'MEDIUM': 3500,
    'HARD': 1000,
    'IMPOSSIBLE': 400,
}

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'street': 2,
    'car-player': 3,
    'car-enemy': 4
}

# M
MENU_OPTION = ('PLAY',
               'EXIT')
# M
GAME_OVER_MENU_OPTION = ('RESTART', 'QUIT')


# P
PLAYER_KEY_UP = {'car-player': pygame.K_UP}
PLAYER_KEY_DOWN = {'car-player': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'car-player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'car-player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'car-player': pygame.K_RCTRL}

# S
SPAWN_TIME = 500

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s
# W
WIN_WIDTH = 581
WIN_HEIGHT = 588

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
