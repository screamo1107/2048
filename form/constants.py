import pygame


COLORS = {
         "HEADER": (255, 255, 255, 255),
         "CELL": (130, 130, 130, 130),
         "2": (),
         "4": (),
         "8": (),
         "16": (),
         "32": (),
         "64": (),
         "128": (),
         "256": (),
         "512": (),
         "1024": (),
         "2048": ()
}

BLOCKS = 4
BLOCK_SIZE = 110
MARGIN = 10
WIDTH = BLOCKS * BLOCK_SIZE + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + BLOCK_SIZE
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)
