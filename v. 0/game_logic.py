import numpy as np
import random


# Add 2 to a random zero-cell after each turn
def add_new_2(mat: list) -> None:
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    # Finding a random cell with 0 inside
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


# Check current status: WON / PROCEED
def get_current_state(mat: list) -> str:
    # WON condition
    for i in mat:
        if 2048 in i:
            return 'WON'
    # "Zero cell presence" condition
    for i in mat:
        if 0 in i:
            return 'GAME NOT OVER'
    # "Zero cell appearing after next turn" condition
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'


# Initialize the game matrix
def start_game() -> list:
    # Tip for the user
    print("""
    Commands:
    W / w - Move UP
    S / s - Move DOWN
    A / a - Move LEFT
    D / d - Move RIGHT
    """)
    mat = [[0]*4]*4
    add_new_2(mat)  # Add 2 to a random cell
    return mat


# Compress the grid after every step before and after merging cells.
def compress(mat) -> [list, bool]:
    # Check for the changes
    changed = False

    # Empty grid
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    # here we will shift entries
    # of each cell to it's extreme
    # left row by row
    # loop to traverse rows
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed


# Merge sells after compression
def merge_cells(mat: list) -> [list, bool]:
    changed = False
    for i in range(4):
        for j in range(3):

            # if current cell has same value as
            # next cell in the row and they
            # are non empty then
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                # Double current cell value and clear the next cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed


# Reverse action (reverse rows)
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat


# Transpose action (interchanging rows and columns)
def transpose(mat):
    return np.transpose(mat)
