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


def solve_board(board, tries=None):
    if tries is None:
        tries = []
    cell = get_first_empty_cell(board)
    if not cell:  # no empty cells -> finished
        return True
    else:
        for i in range(1, 10):
            board[cell[0]][cell[1]] = i
            if check_board(board):
                tries.append(i)
                solvable = solve_board(board, tries)
                if solvable:
                    return True
            board[cell[0]][cell[1]] = "_"
        return False


sudoku_board = [
    [7, 8, "_", 4, "_", "_", 1, 2, "_"],
    [6, "_", "_", "_", 7, 5, "_", "_", 9],
    ["_", "_", "_", 6, "_", 1, "_", 7, 8],
    ["_", "_", 7, "_", 4, "_", 2, 6, "_"],
    ["_", "_", 1, "_", 5, "_", 9, 3, "_"],
    [9, "_", 4, "_", 6, "_", "_", "_", 5],
    ["_", 7, "_", 3, "_", "_", "_", 1, 2],
    [1, 2, "_", "_", "_", 7, 4, "_", "_"],
    ["_", 4, 9, 2, "_", 6, "_", "_", 7]
]

# print_sudoku_board(sudoku_board)
# print(get_first_empty_cell(sudoku_board))
# print(check_board(sudoku_board))
# solve_board(sudoku_board)
# print_sudoku_board(sudoku_board)
