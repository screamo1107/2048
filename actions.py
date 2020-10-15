from game_logic import compress, merge_cells, reverse, transpose


# Matrix update upon LEFT action (MAIN)
def move_left(matrix: list) -> [list, bool]:
    # Compress the grid
    new_matrix, changed_compress = compress(matrix)
    # Merge the cells
    new_matrix, changed_merge = merge_cells(new_matrix)
    changed = changed_compress or changed_merge
    # Compress after merging
    new_matrix, temp = compress(new_matrix)
    return new_matrix, changed


# Matrix update upon RIGHT action
def move_right(matrix: list) -> [list, bool]:
    # Reverse the matrix
    new_matrix = reverse(matrix)
    # Move left
    new_matrix, changed = move_left(new_matrix)
    # Reverse the matrix
    new_matrix = reverse(new_matrix)
    return new_matrix, changed


# Matrix update upon UP action
def move_up(matrix: list) -> [list, bool]:
    # Transpose the matrix
    new_matrix = transpose(matrix)
    # Move left
    new_matrix, changed = move_left(new_matrix)
    # Transpose the matrix
    new_matrix = transpose(new_matrix)
    return new_matrix, changed


# Matrix update upon DOWN action
def move_down(matrix: list) -> [list, bool]:
    # Transpose the matrix
    new_matrix = transpose(matrix)
    # Move right
    new_matrix, changed = move_right(new_matrix)
    # Transpose the matrix
    new_matrix = transpose(new_matrix)
    return new_matrix, changed
