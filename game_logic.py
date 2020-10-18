# MOVE ACTIONS:

# Matrix update upon LEFT key pressed
def move_left(mas: list) -> [list, int]:
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas, delta


# Matrix update upon RIGHT key pressed
def move_right(mas: list) -> [list, int]:
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j-1)
                mas[i].insert(0, 0)
    return mas, delta


# Matrix update upon UP key pressed
def move_up(mas: list) -> [list, int]:
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i+1] and column[i] != 0:
                column[i] *= 2
                delta += mas[i][j]
                column.pop(i+1)
                column.append(0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas, delta


# Matrix update upon DOWN key pressed
def move_down(mas: list) -> [list, int]:
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if column[i] == column[i-1] and column[i] != 0:
                column[i] *= 2
                delta += mas[i][j]
                column.pop(i-1)
                column.insert(0, 0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas, delta


# SUPPLEMENT ACTIONS

# Get the list of empty cells
def get_empty_list(mas: list) -> list:
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


# Get cell number by provided index [i][j]
def get_number_from_index(i: int, j: int) -> int:
    return i * 4 + j + 1


# Get the index [i][j] by cell number
def get_index_from_number(number: int) -> [int, int]:
    number -= 1
    x, y = number // 4, number % 4
    return x, y


# Add '2' to selected cell
def insert_2(mas: list, x: int, y: int) -> list:
    mas[x][y] = 2
    return mas


# Print the matrix in 2-d array view
def pretty_print(mas: list):
    for row in mas:
        print(*row)


# CHECK THE STATE:

# Check if possible to move when no empty cells
def can_move(mas: list) -> bool:
    state = False
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] or mas[i][j] == mas[i+1][j]:
                state = True
    # Additional check for the moves within the last column and the last row
    j = 3
    for i in range(3):
        if mas[i][j] == mas[i+1][j] or mas[j][i] == mas[j][i+1]:
            state = True
    return state


# Check if zeros presented in the matrix
def is_zero_in_mas(mas: list) -> bool:
    for row in mas:
        if 0 in row:
            return True
    return False
