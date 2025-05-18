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
C_RED = (237,56,20)

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
    'level2BG0': 0,
    'level2BG1': 0,
    'level2BG2': 0,
    'level2BG3': 0,
    'level2BG4': 0,
    'level2BG5': 0,
    'level3BG0': 0,
    'level3BG1': 0,
    'level3BG2': 0,
    'level3BG3': 0,
    'level3BG4': 0,
    #Speed Player
    'player1-11': 5,
    #Speed Enemy
    'Enemy1-2': 1,
    #Shoot Player
    'Arrow': 2,    }

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
    'level1BG0': 9999,
    'level1BG1': 9999,
    'level1BG2': 9999,
    'level1BG3': 9999,
    'level1BG4': 9999,
    'level1BG5': 9999,
    'level1BG6': 9999,
    'level1BG7': 9999,
    'level2BG0': 9999,
    'level2BG1': 9999,
    'level2BG2': 9999,
    'level2BG3': 9999,
    'level2BG4': 9999,
    'level2BG5': 9999,
    'level3BG0': 9999,
    'level3BG1': 9999,
    'level3BG2': 9999,
    'level3BG3': 9999,
    'level3BG4': 9999,
    # LIFE Player
    'player1-11': 100,
    # LIFE Enemy
    'Enemy1-2': 80,
    'Arrow': 9999,
    }

# DELAY BETWEEN SHOTS
SHOOT_DELAY_ENTITY = {'player1-11': 70}

# ALL DAMAGE GIVEN
DAMAGE_GENERAL = {
    # Damage Background
    'level1BG0': 0,
    'level1BG1': 0,
    'level1BG2': 0,
    'level1BG3': 0,
    'level1BG4': 0,
    'level1BG5': 0,
    'level1BG6': 0,
    'level1BG7': 0,
    'level2BG0': 0,
    'level2BG1': 0,
    'level2BG2': 0,
    'level2BG3': 0,
    'level2BG4': 0,
    'level2BG5': 0,
    'level3BG0': 0,
    'level3BG1': 0,
    'level3BG2': 0,
    'level3BG3': 0,
    'level3BG4': 0,
    # Damage Player
    'player1-11': 1,
    'Arrow': 20,
    # Damage Enemy
    'Enemy1-2': 50,
    }

# SCOREBOARD
SCORE = {
    # Score Background
    'level1BG0': 0,
    'level1BG1': 0,
    'level1BG2': 0,
    'level1BG3': 0,
    'level1BG4': 0,
    'level1BG5': 0,
    'level1BG6': 0,
    'level1BG7': 0,
    'level2BG0': 0,
    'level2BG1': 0,
    'level2BG2': 0,
    'level2BG3': 0,
    'level2BG4': 0,
    'level2BG5': 0,
    'level3BG0': 0,
    'level3BG1': 0,
    'level3BG2': 0,
    'level3BG3': 0,
    'level3BG4': 0,
    # Score Player
    'player1-11': 0,
    # Score Enemy
    'Enemy1-2': 50,
    # Score Projection
    'Arrow': 0,
    }

# TIMEOUT W/ MS - LEVEL
TIMEOUT_LEVEL = 15000
TIMEOUT_LEVEL_CHECK = pygame.USEREVENT + 2
TIMEOUT_LEVEL_VERIFY = 150
TIMEOUT_GAME_OVER = 4000
TIMEOUT_CHANGE_LEVEL = 2000