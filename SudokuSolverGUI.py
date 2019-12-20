import pygame
from SudokuSolver import *
import SudokuSquare
from tkinter import *
from tkinter import messagebox

# colors and consts
grey = (128, 128, 128)
white = (255, 255, 255)
light_green = (0, 200, 0)
black = (0, 0, 0)  # 1
yellow = (255, 255, 0)  # 2
green = (0, 128, 0)  # 3
blue = (0, 0, 255)  # 4
pink = (255, 105, 180)  # 5
brown = (102, 51, 0)  # 6
orange = (255, 140, 0)  # 7
red = (255, 0, 0)  # 8
dark_brown = (51, 25, 0)  # 9
num_to_col = dict()
num_to_col[1] = black
num_to_col[2] = yellow
num_to_col[3] = green
num_to_col[4] = blue
num_to_col[5] = pink
num_to_col[6] = brown
num_to_col[7] = orange
num_to_col[8] = red
num_to_col[9] = dark_brown


class Board(object):

    def __init__(self, width, height, win, sud_board: list, rows=9, cols=9):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.window = win
        self.square_selected = None
        self.board = sud_board
        self.squares = [[SudokuSquare.SudokuSquare(self.board[i][j], width, height, i, j) for j in range(cols)] for i in
                        range(rows)]

    def draw(self):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.window, black, (0, i * gap), (self.width, i * gap), thickness)
            pygame.draw.line(self.window, black, (i * gap, 0), (i * gap, self.height), thickness)

        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].draw(self.window)

    def is_win(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.squares[i][j].value == "_":
                    return False
        return True

    def position_click(self, position):
        if self.width > position[0] and self.height > position[1]:
            # in the screen
            div_x = self.width / 9
            div_y = self.height / 9
            x = position[0] // div_x
            y = position[1] // div_y
            return x, y  # fixme was y,x in tutorial???
        else:
            # out of screen
            return None

    def clear_square_selected(self):
        if self.squares[self.square_selected[0]][self.square_selected[1]].value == "_":
            self.squares[self.square_selected[0]][self.square_selected[1]].grey = 0

    def select_square(self, row, col):
        if self.square_selected is not None:
            self.squares[self.square_selected[0]][self.square_selected[1]].selected = False
        self.square_selected = (row, col)
        self.squares[row][col].selected = True

    def update_board(self):
        self.board = [[self.squares[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def write_square(self, value):
        i, j = self.square_selected
        if self.squares[i][j].value != "_":
            return
        self.squares[i][j].value = value
        self.update_board()
        # check if board is solvable (if so, then the move is ok)
        if check_pos(self.board, i, j, value) and solve_board(self.board):
            return
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('Sudoku', 'mistakes were made')
        self.squares[i][j].value = "_"
        self.squares[i][j].set_grey_value(0)
        self.update_board()
        return

    def mark_square(self, grey_value):
        self.squares[self.square_selected[0]][self.square_selected[1]].set_grey_value(grey_value)


def redraw_window(win, board):
    win.fill(white)
    # Draw time
    fnt = pygame.font.SysFont("Arial", 40)
    # solve button
    pygame.draw.rect(window, green, (430, 550, 100, 40))
    fnt = pygame.font.SysFont("timesnewroman", 25)
    text = fnt.render("solve", 1, white)
    win.blit(text, (455, 555))
    # Draw grid and board
    board.draw()


def check_solve_button(mouse, win):
    if 530 > mouse[0] > 430 and 590 > mouse[1] > 550:
        pygame.draw.rect(window, light_green, (430, 550, 100, 40))
        fnt = pygame.font.SysFont("timesnewroman", 25)
        text = fnt.render("solve", 1, white)
        win.blit(text, (455, 555))
        return True
    else:
        pygame.draw.rect(window, green, (430, 550, 100, 40))
        fnt = pygame.font.SysFont("timesnewroman", 25)
        text = fnt.render("solve", 1, white)
        win.blit(text, (455, 555))
        return False


def solve_board_gui(s_board: Board, win, tries=None):
    if tries is None:
        tries = []
    cell = get_first_empty_cell(s_board.board)
    if not cell:  # no empty cells -> finished
        return True
    else:
        for i in range(1, 10):
            s_board.squares[cell[0]][cell[1]].value = i
            s_board.update_board()
            redraw_window(win, s_board)
            pygame.display.update()
            pygame.time.delay(20)
            if check_board(s_board.board):
                tries.append(i)
                solvable = solve_board_gui(s_board, win, tries)
                if solvable:
                    return True
            s_board.squares[cell[0]][cell[1]].value = "_"
            s_board.update_board()
            redraw_window(win, s_board)
            pygame.display.update()
            pygame.time.delay(20)
        return False


if __name__ == "__main__":
    pygame.font.init()
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Board(540, 540, window, sudoku_board)
    pygame.draw.rect(window, green, (0, 540, 60, 60))
    board.draw()
    key = None
    playing = True

    while playing:
        for event in pygame.event.get():
            key = None
            if event.type == pygame.QUIT:
                playing = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    selected = board.square_selected
                    if selected is not None:
                        row, col = selected
                        if board.squares[row][col].grey != 0:
                            # the square is marked
                            board.write_square(board.squares[row][col].grey)
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9
                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    board.clear_square_selected()
                    key = None
            elif event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                clicked = board.position_click(position)
                if clicked:
                    board.select_square(int(clicked[1]), int(clicked[0]))
                    key = None
                if check_solve_button(position, window):
                    print("solving")
                    solve_board_gui(board, window)
        if key is not None and board.square_selected:
            board.mark_square(key)
        redraw_window(window, board)
        check_solve_button(pygame.mouse.get_pos(), window)
        pygame.display.update()
        if board.is_win():
            print("winner!!!")
            Tk().wm_withdraw()  # to hide the main window
            messagebox.showinfo('Sudoku', 'You Win!!!!')
            break
    pygame.quit()
