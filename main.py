import actions as a
from game_logic import add_new_2, get_current_state, start_game


if __name__ == '__main__':
    mat = start_game()


while True:
    # User input
    x = input("Press the command: ")

    # Moving UP?
    if x in 'Ww':
        mat, flag = a.move_up(mat)
        status = get_current_state(mat)
        if status == 'GAME NOT OVER':
            add_new_2(mat)
        else:
            break
    # Moving DOWN?
    elif x in 'Ss':
        mat, flag = a.move_down(mat)
        status = get_current_state(mat)
        if status == 'GAME NOT OVER':
            add_new_2(mat)
        else:
            break

    # Moving LEFT?
    elif x in 'Aa':
        mat, flag = a.move_left(mat)
        status = get_current_state(mat)
        if status == 'GAME NOT OVER':
            add_new_2(mat)
        else:
            break
    # Moving RIGHT?
    elif x in 'Dd':
        mat, flag = a.move_right(mat)
        status = get_current_state(mat)
        if status == 'GAME NOT OVER':
            add_new_2(mat)
        else:
            break
    else:
        print("Invalid Key Pressed")

    print("\n".join([' '.join(str(a)) for a in mat]))
