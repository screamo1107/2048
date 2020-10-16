import pygame


COLORS = {
         "HEADER": (255, 255, 255),
         'DIGIT': (0, 0, 0),
         '0': (190, 190, 190),
         '2': (255, 255, 255),
         '4': (255, 255, 125),
         '8': (255, 255, 65),
         '16': (255, 255, 30),
         '32': (255, 255, 0),
         '64': (255, 200, 80),
         '128': (255, 190, 30),
         '256': (255, 190, 0),
         '512': (255, 150, 40),
         '1024': (255, 120, 0),
         '2048': (255, 80, 0)
}

BLOCKS = 4
BLOCK_SIZE = 120
MARGIN = 5
WIDTH = BLOCKS * BLOCK_SIZE + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + BLOCK_SIZE
TITLE_REC = pygame.Rect(0, 0, WIDTH, BLOCK_SIZE)
