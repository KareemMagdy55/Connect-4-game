# Connect 4 game
# Author  : Kareem Magdy
# Date    : 24 Feb. 2022
# Version : 1.0

def game_board():
    return [["-" for columns in range(7)] for rows in range(6)]


def gravity(list1, row, column, token):
    if list1[row][column - 1] == "-":
        list1[row][column - 1] = token
    else:
        gravity(list1, row - 1, column, token)
    return list1


def player_O(player_list1):
    for i in player_list1:
        print(" ".join(i))
    player_o_columns = int(input("Please input the column to insert your O token : "))
    player_list1 = gravity(player_list1, 5, player_o_columns, 'O')

    if check_winner(player_list1, 5, player_o_columns, 'O') is True:
        print("Congratulations you won")
    elif check_tie(player_list1, 6, "-") is True:
        print("It is a tie")
    else:
        player_x(player_list1)


def player_x(player_list2):
    for i in player_list2:
        print(" ".join(i))
    player_x_columns = int(input("Please input the column to insert your X token : "))
    player_list2 = gravity(player_list2, 5, player_x_columns, 'X')

    if check_winner(player_list2, 5, player_x_columns, 'X') is True:
        print("Congratulations you won")
    elif check_tie(player_list2, 6, "-") is True:
        print("It is a tie")
    else:
        player_O(player_list2)


def check_winner(winner_list, rows, column, token):
    if check_columns(winner_list, rows, column, token) is True:
        return True

    elif check_rows(winner_list, rows, token) is True:
        return True

    elif check_diagonal1(winner_list, rows, token) is True:
        return True

    elif check_diagonal2(winner_list, rows, token) is True:
        return True


def check_tie(tie_list, column, board_pattern):
    tie_counter = 0
    for i in range(column):
        for char in tie_list[i]:
            if char != board_pattern:
                tie_counter = tie_counter + 1
            else:
                continue
    if tie_counter == 42:
        return True


def check_columns(winner_list, rows, column, token):
    temp_string = ''
    for i in range(rows + 1):
        temp_string += winner_list[i][column - 1]
    if token * 4 in temp_string:
        return True


def check_rows(winner_list, rows, token):
    temp_string = ''
    for i in range(rows + 1):
        temp_string += winner_list[rows][i]
    if token * 4 in temp_string:
        return True


def check_diagonal1(winner_list, rows, token):
    temp_string = ''
    for i in range(rows + 1):
        temp_string += winner_list[rows][i]
        rows = rows - 1
    if token * 4 in temp_string:
        return True


def check_diagonal2(winner_list, rows, token):
    temp_string = ''
    for i in range(rows + 1):
        temp_string += winner_list[i][i + 1]
    if token * 4 in temp_string:
        return True


player_O(game_board())
