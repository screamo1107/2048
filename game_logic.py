def get_empty_list(mas: list) -> list:
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_number(number):
    number -= 1
    x, y = number // 4, number % 4
    return x, y


def insert_2(mas, x, y):
    mas[x][y] = 2
    return mas


def pretty_print(mas):
    for row in mas:
        print(*row)


def is_zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False


def move_left(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas
