import random


# Add 2 to a random cell after each turn
def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    # Finding a random cell with 0 inside
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


# Check current status: WON / PROCEED
def get_current_state(mat):
    # WON condition
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    # "Zero cell presence" condition
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    # "Zero cell appearing after next turn" condition
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
    # TBD
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'
    # TBD
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'


# Initialize the game matrix
def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    # Tip for the user
    print("""
    Commands:
    W / w - Move UP
    S / s - Move DOWN
    A / a - Move LEFT
    D / d - Move RIGHT
    """)

    add_new_2(mat)  # Add 2 to a random cell after each turn
    return mat


# Compress the grid after every step before and after merging cells.
def compress(mat):
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

        # loop to traverse each column
        # in respective row
        for j in range(4):
            if (mat[i][j] != 0):

                # if cell is non empty then
                # we will shift it's number to
                # previous empty cell in that row
                # denoted by pos variable
                new_mat[i][pos] = mat[i][j]

                if (j != pos):
                    changed = True
                pos += 1

    # returning new compressed matrix
    # and the flag variable.
    return new_mat, changed


# function to merge the cells
# in matrix after compressing
def merge(mat):
    changed = False

    for i in range(4):
        for j in range(3):

            # if current cell has same value as
            # next cell in the row and they
            # are non empty then
            if (mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
                # double current cell value and
                # empty the next cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0

                # make bool variable True indicating
                # the new grid after merging is
                # different.
                changed = True

    return mat, changed


# function to reverse the matrix
# maens reversing the content of
# each row (reversing the sequence)
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat


# function to get the transpose
# of matrix means inerchanging
# rows and column
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


# function to update the matrix
# if we move / swipe left
def move_left(grid):
    # first compress the grid
    new_grid, changed1 = compress(grid)

    # then merge the cells.
    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    # again compress after merging.
    new_grid, temp = compress(new_grid)

    # return new matrix and bool changed
    # telling whether the grid is same
    # or different
    return new_grid, changed


# function to update the matrix
# if we move / swipe right
def move_right(grid):
    # to move right we just reverse
    # the matrix
    new_grid = reverse(grid)

    # then move left
    new_grid, changed = move_left(new_grid)

    # then again reverse matrix will
    # give us desired result
    new_grid = reverse(new_grid)
    return new_grid, changed


# function to update the matrix
# if we move / swipe up
def move_up(grid):
    # to move up we just take
    # transpose of matrix
    new_grid = transpose(grid)

    # then move left (calling all
    # included functions) then
    new_grid, changed = move_left(new_grid)

    # again take transpose will give
    # desired results
    new_grid = transpose(new_grid)
    return new_grid, changed


# function to update the matrix
# if we move / swipe down
def move_down(grid):
    # to move down we take transpose
    new_grid = transpose(grid)

    # move right and then again
    new_grid, changed = move_right(new_grid)

    # take transpose will give desired
    # results.
    new_grid = transpose(new_grid)
    return new_grid, changed

# this file only contains all the logic
# functions to be called in main function
# present in the other file