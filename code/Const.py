# W
import pygame

# LENGTH SCREEN
WIN_WIDTH = 600
WIN_HEIGHT = 480

# COLOR
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 253, 85)

# MENU
MENU_OPTION = ('NEW GAME 1P',
               'COOPERATIVE GAME (soon)',
               'SCORE',
               'EXIT')
# SPEED FOR ENTITY'S
SPEED_ENTITY = {
    #Speed Background
    'level1BG0': 0, #1
    'level1BG1': 0, #8
    'level1BG2': 0, #7
    'level1BG3': 0, #6
    'level1BG4': 0, #5
    'level1BG5': 0, #4
    'level1BG6': 0, #3
    'level1BG7': 0, #2
    #Speed Player
    'player1-11': 5,
    #Speed Enemy
    'Enemy1-2': 1,
}

# PLAYER BOX
LENGTH_PLAYER_BOX_MAX_Y = 300
LENGTH_PLAYER_BOX_MAX_X = 150

# ENEMY'S SPAWN RANGE
RANDOM_ENEMY_SPAWN_MAX = 325
RANDOM_ENEMY_SPAWN_MIN = 400

# SPAWN ENEMY'S AT SCREEN
SPAWN_ENEMY = pygame.USEREVENT + 1
SPAWN_ENEMY_TIME = 30000