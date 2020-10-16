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


def draw_interface():
    font = pygame.font.SysFont("arial", 65)
    pygame.draw.rect(screen, const.COLORS['HEADER'], const.TITLE_REC)
    for row in range(const.BLOCKS):
        for column in range(const.BLOCKS):
            value = mas[row][column]
            text = font.render(str(value), True, const.COLORS['NUMBER'])
            w = column * const.BLOCK_SIZE + (column + 1) * const.MARGIN
            h = row * const.BLOCK_SIZE + (row + 1) * const.MARGIN + const.BLOCK_SIZE
            pygame.draw.rect(screen, const.COLORS[str(value)], (w, h, const.BLOCK_SIZE, const.BLOCK_SIZE))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (const.BLOCK_SIZE - font_w) / 2
                text_y = h + (const.BLOCK_SIZE - font_h) / 2
                screen.blit(text, (int(text_x), int(text_y)))


draw_interface()
pygame.display.update()

while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                mas = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas = move_right(mas)
            elif event.key == pygame.K_UP:
                mas = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas = move_down(mas)

            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2(mas, x, y)
            draw_interface()
            pygame.display.update()
