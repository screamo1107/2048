from game_logic import compress, merge_cells, reverse, transpose


# Matrix update upon LEFT action (MAIN)
def move_left(grid) -> [list, bool]:
    # Compress the grid
    new_grid, changed1 = compress(grid)
    # Merge the cells.
    new_grid, changed2 = merge_cells(new_grid)
    changed = changed1 or changed2
    # Compress after merging
    new_grid, temp = compress(new_grid)
    return new_grid, changed


# Matrix update upon RIGHT action
def move_right(grid) -> [list, bool]:
    # Reverse the matrix
    new_grid = reverse(grid)
    # Move left
    new_grid, changed = move_left(new_grid)
    # Reverse the matrix
    new_grid = reverse(new_grid)
    return new_grid, changed


# Matrix update upon UP action
def move_up(grid) -> [list, bool]:
    # Transpose the matrix
    new_grid = transpose(grid)
    # Move left
    new_grid, changed = move_left(new_grid)
    # Transpose the matrix
    new_grid = transpose(new_grid)
    return new_grid, changed


# Matrix update upon DOWN action
def move_down(grid) -> [list, bool]:
    # Transpose the matrix
    new_grid = transpose(grid)
    # Move right
    new_grid, changed = move_right(new_grid)
    # Transpose the matrix
    new_grid = transpose(new_grid)
    return new_grid, changed
