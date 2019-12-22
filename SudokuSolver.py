import random

import numpy

import boards


def print_sudoku_board(board: list):
    for i in range(9):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" "),
            print(board[i][j], end=" ")
        print("|")
    print("-------------------------")


def get_first_empty_cell(board: list):
    for i in range(9):
        for j in range(9):
            if board[i][j] == "_":
                return i, j
    return None


def check_board(board: list) -> bool:
    # check rows
    for i in range(9):
        hist = []
        for j in range(9):
            if board[i][j] in hist and board[i][j] != "_":
                return False
            hist.append(board[i][j])

    # check cols
    for j in range(9):
        hist = []
        for i in range(9):
            if board[i][j] in hist and board[i][j] != "_":
                return False
            hist.append(board[i][j])

    # check squares
    for sq in range(9):
        x = sq // 3
        y = sq % 3
        hist = []
        for i in range(x * 3, x * 3 + 3):
            for j in range(y * 3, y * 3 + 3):
                if board[i][j] in hist and board[i][j] != "_":
                    return False
                hist.append(board[i][j])
    return True


def check_pos(board: list, y, x, num) -> bool:
    # check rows
    for j in range(9):
        if board[x][j] == num:
            return False

    # check cols
    for i in range(9):
        if board[i][y] == num:
            return False

    # check squares
    x = x // 3
    y = y % 3
    for i in range(x * 3, x * 3 + 3):
        for j in range(y * 3, y * 3 + 3):
            if board[i][j] == num:
                return False
    return True


def solve_board(board, tries=None):
    if tries is None:
        tries = []
    cell = get_first_empty_cell(board)
    if not cell:  # no empty cells -> finished
        return True
    else:
        for i in range(1, 10):
            board[cell[0]][cell[1]] = i
            if check_board(board): # check_pos cell[0], cell[1], i
                tries.append(i)
                solvable = solve_board(board, tries)
                if solvable:
                    return True
            board[cell[0]][cell[1]] = "_"
        return False


board_num = random.randint(0, 31)
sudoku_board = boards.boards[board_num]
ran = random.randint(0, 2)
if ran == 2:
    list(map(list, zip(*sudoku_board)))
elif ran == 1:
    sudoku_board = sudoku_board[::-1]
