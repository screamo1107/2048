import form.constants as const
import pygame
import sys
import time


pygame.init()
screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("2048!")


# Within main While:

# X(cross) handling
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    elif event.type == pygame.KEYDOWN:

        pygame.draw.rect(screen, const.WHITE, const.TITLE_REC)
        for row in range(const.BLOCKS):
            for column in range(const.BLOCKS):
                w = column * const.BLOCK_SIZE + (column + 1) * const.MARGIN
                h = row * const.BLOCK_SIZE + (row + 1) * const.MARGIN + 110
                pygame.draw.rect(screen, const.GREY, (w, h, 110, 110))
pygame.display.update()
