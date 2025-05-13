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
    #Shoot Player
    'Arrow': 2,
}

# PLAYER BOX
LENGTH_PLAYER_BOX_MAX_Y = 300
LENGTH_PLAYER_BOX_MAX_X = 150

# ENEMY'S SPAWN RANGE
RANDOM_ENEMY_SPAWN_MAX = 325
RANDOM_ENEMY_SPAWN_MIN = 400

# SPAWN ENEMY'S AT SCREEN
SPAWN_ENEMY = pygame.USEREVENT + 1
SPAWN_ENEMY_TIME = 3000

# Enemy Life
ENTITY_LIFE = {
    # Life Background
    'level1BG0': 9999,  # 1
    'level1BG1': 9999,  # 8
    'level1BG2': 9999,  # 7
    'level1BG3': 9999,  # 6
    'level1BG4': 9999,  # 5
    'level1BG5': 9999,  # 4
    'level1BG6': 9999,  # 3
    'level1BG7': 9999,  # 2
    # LIFE Player
    'player1-11': 100,
    # LIFE Enemy
    'Enemy1-2': 75,
    'Arrow': 9999,
               }

# Intervalo entre os tiros
SHOOT_DELAY_ENTITY = {'player1-11': 75}