import pygame


# Screen:
BLOCKS = 4
BLOCK_SIZE = 120
HEADER_TEXT = "Let's play 2048!"
MARGIN = 5

WIDTH = BLOCKS * BLOCK_SIZE + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + BLOCK_SIZE
TITLE_REC = pygame.Rect(0, 0, WIDTH, BLOCK_SIZE)


# Font sizes:
BEST_HEADER_SIZE = 35
BEST_PLAYERS_SIZE = 30
DELTA_SIZE = 30
DIGIT_SIZE = 65
END_SIZE = 75
INTRO_SIZE = 75
SCORE_SIZE = 45


# Fonts:
DIGIT_FONT = 'arial'
END_FONT = 'allegro'
INTRO_FONT = 'allegro'
SCORE_FONT = 'simsun'


# Colors:
COLORS = {
         'BLACK': (0, 0, 0),
         'DELTA': (100, 0, 0),
         'SCORE_TEXT': (160, 100, 0),
         'SCORE_VALUE': (170, 0, 0),
         'WHITE': (255, 255, 255),
         '0': (190, 190, 190),
         '2': (255, 255, 255),
         '4': (255, 255, 135),
         '8': (255, 255, 65),
         '16': (255, 255, 20),
         '32': (255, 240, 0),
         '64': (255, 190, 70),
         '128': (255, 190, 10),
         '256': (255, 160, 0),
         '512': (255, 150, 10),
         '1024': (255, 110, 0),
         '2048': (255, 30, 0)
}
