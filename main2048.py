import constants as c
import pygame
import random
import sys
from game_logic import *
from db_leaderboard import crsr, get_best_results, insert_result


# Initial matrix
mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
      ]

GAMERS_DATA = get_best_results()
USERNAME = ''


# Game-board initialize
pygame.init()
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption(c.HEADER_TEXT)


def draw_best_results():
    font_best_header = pygame.font.SysFont(c.SCORE_FONT, c.BEST_HEADER_SIZE)
    text_best_header = font_best_header.render("Best results: ", True, c.COLORS['BLACK'])
    font_best_player = pygame.font.SysFont(c.SCORE_FONT, c.BEST_PLAYERS_SIZE)
    screen.blit(text_best_header, (310, 5))
    for index, player in enumerate(GAMERS_DATA):
        name, pl_score = player
        r = f"{index+1}. {name} - {pl_score}"
        text_best_player = font_best_player.render(r, True, c.COLORS['BLACK'])
        screen.blit(text_best_player, (310, 35 + 25 * index))


def draw_interface(score: int, delta: int = 0):
    font_digit = pygame.font.SysFont(c.DIGIT_FONT, c.DIGIT_SIZE)
    font_score = pygame.font.SysFont(c.SCORE_FONT, c.SCORE_SIZE)
    text_score = font_score.render("Your score: ", True, c.COLORS['BLACK'])
    score_value = font_score.render(f"{score}", True, c.COLORS['SCORE_VALUE'])
    font_delta = pygame.font.SysFont(c.SCORE_FONT, c.DELTA_SIZE)

    # Drawing header with score text and value
    pygame.draw.rect(screen, c.COLORS['WHITE'], c.TITLE_REC)
    screen.blit(text_score, (20, 35))
    screen.blit(score_value, (215, 37))

    # Drawing +score update dynamically
    if delta > 0:
        delta_value = font_delta.render(f"+{delta}!", True, c.COLORS['DELTA'])
        screen.blit(delta_value, (221, 70))

    draw_best_results()  # Trigger displaying of best players score-board
    for row in range(c.BLOCKS):
        for column in range(c.BLOCKS):
            value = mas[row][column]
            text = font_digit.render(str(value), True, c.COLORS['BLACK'])
            w = column * c.BLOCK_SIZE + (column + 1) * c.MARGIN
            h = row * c.BLOCK_SIZE + (row + 1) * c.MARGIN + c.BLOCK_SIZE
            pygame.draw.rect(screen, c.COLORS[str(value)], (w, h, c.BLOCK_SIZE, c.BLOCK_SIZE))

            # Draw digit inside the cell
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (c.BLOCK_SIZE - font_w) / 2
                text_y = h + (c.BLOCK_SIZE - font_h) / 2
                screen.blit(text, (int(text_x), int(text_y)))


def draw_intro_screen():
    # start_img = pygame.image.load('bg.png')
    font_intro = pygame.font.SysFont(c.INTRO_FONT, c.INTRO_SIZE)
    text_intro = font_intro.render("WELCOME!", True, c.COLORS['WHITE'])

    name_input = 'Enter your name!'
    is_name_found = False
    # Looping until correct name entered
    while not is_name_found:
        for event in pygame.event.get():
            # Close action handling
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name_input == "Enter your name!":
                        name_input = event.unicode
                    else:
                        name_input += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name_input = name_input[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name_input) > 2 and name_input != "Enter your name!":
                        global USERNAME
                        USERNAME = name_input
                        is_name_found = True
                        break
        screen.fill(c.COLORS['BLACK'])

        # Rendering intro background image, text and username
        text_name = font_intro.render(name_input, True, c.COLORS['WHITE'])
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        # screen.blit(pygame.transform.scale(start_img, [200, 200]), [10, 10])
        screen.blit(text_intro, (110, 230))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(c.COLORS['BLACK'])


def draw_game_over():
    font_end = pygame.font.SysFont(c.END_FONT, c.END_SIZE)
    text_end = font_end.render("GAME OVER.", True, c.COLORS['WHITE'])
    text_score = font_end.render(f"Your score: {score}", True, c.COLORS['WHITE'])
    if not GAMERS_DATA:
        best_score = 0
    else:
        best_score = GAMERS_DATA[0][1]
    if score > best_score:
        text_b = "New record!"
    else:
        text_b = f"Best: {best_score}"
    text_best = font_end.render(text_b, True, c.COLORS['WHITE'])
    insert_result(USERNAME, score)
    while True:
        for event in pygame.event.get():
            # Close action handling
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.fill(c.COLORS['BLACK'])
        screen.blit(text_end, (85, 200))
        screen.blit(text_score, (50, 270))
        screen.blit(text_best, (110, 340))
        pygame.display.update()


# GAME SEQUENCE:

# Draw intro screen firstly
draw_intro_screen()

# Draw initial game-board once intro is passed
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
            if is_zero_in_mas(mas):
                zeros = get_empty_list(mas)
                random.shuffle(zeros)
                random_zero_number = zeros.pop()
                x, y = get_index_from_number(random_zero_number)
                mas = insert_2(mas, x, y)

            # Re-drawing of the updated game-board
            draw_interface(score, delta)
            pygame.display.update()

# Display game-over screen once the main loop is finished
draw_game_over()
