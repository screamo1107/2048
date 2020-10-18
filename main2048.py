import constants as c
import pygame
import random
import sys
from game_logic import *


# Initial matrix
mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
      ]

# Game-board initialize
pygame.init()
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption(c.HEADER_TEXT)


def draw_interface(score):
    font_digit = pygame.font.SysFont(c.DIGIT_FONT, c.DIGIT_SIZE)
    font_score = pygame.font.SysFont(c.SCORE_FONT, c.SCORE_SIZE)
    text_score = font_score.render("Your score: ", True, c.COLORS['SCORE'])
    score_value = font_score.render(f"{score}", True, c.COLORS['SCORE'])
    pygame.draw.rect(screen, c.COLORS['HEADER'], c.TITLE_REC)
    screen.blit(text_score, (20, 35))
    screen.blit(score_value, (220, 35))
    for row in range(c.BLOCKS):
        for column in range(c.BLOCKS):
            value = mas[row][column]
            text = font_digit.render(str(value), True, c.COLORS['DIGIT'])
            w = column * c.BLOCK_SIZE + (column + 1) * c.MARGIN
            h = row * c.BLOCK_SIZE + (row + 1) * c.MARGIN + c.BLOCK_SIZE
            pygame.draw.rect(screen, c.COLORS[str(value)], (w, h, c.BLOCK_SIZE, c.BLOCK_SIZE))
            # Draw digit inside the cell
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (c.BLOCK_SIZE - font_w) / 2
                text_y = h + (c.BLOCK_SIZE - font_h) / 2
                screen.blit(text, (int(text_x), int(text_y)))


# Draw initial game-board
score = 0
draw_interface(score)
pygame.display.update()


# Main game-cycle
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        # Close action handling
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            # Keys handling
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta

            # Actions once key is pressed
            zeros = get_empty_list(mas)
            random.shuffle(zeros)
            random_zero_number = zeros.pop()
            x, y = get_index_from_number(random_zero_number)
            mas = insert_2(mas, x, y)

            # Re-drawing of the updated game-board
            draw_interface(score)
            pygame.display.update()
