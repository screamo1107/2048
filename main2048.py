import random
from game_logic import *
import constants as const
import pygame
import sys


mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

pygame.init()
screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("2048!")


while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, const.COLORS['HEADER'], const.TITLE_REC)
            for row in range(const.BLOCKS):
                for column in range(const.BLOCKS):
                    w = column * const.BLOCK_SIZE + (column + 1) * const.MARGIN
                    h = row * const.BLOCK_SIZE + (row + 1) * const.MARGIN + 110
                    pygame.draw.rect(screen, const.COLORS['CELL'], (w, h, 110, 110))
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2(mas, x, y)
            pretty_print(mas)
    pygame.display.update()
