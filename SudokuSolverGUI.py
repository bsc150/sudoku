import pygame
from SudokuSolver import *
import time

# colors and consts
grey = (128, 128, 128)
white = (255, 255, 255)
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


class SudokuSquare(object):
    def __init__(self, value, width, height, row, col):
        self.value = value
        self.grey = 0  # invalid number to grey out
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.grey != 0 and self.value == "_":
            text = fnt.render(str(self.grey), 1, grey)
            win.blit(text, (x + 5, y + 5))
        elif not (self.value == "_"):
            text = fnt.render(str(self.value), 1, num_to_col[self.value])  # change to fit color
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, red, (x, y, gap, gap), 3)


class Board(object):

    def __init__(self, width, height, win, sud_board, rows=9, cols=9):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.window = win
        self.square_selected = None
        self.board = sud_board
        self.squares = [[SudokuSquare(self.board[i][j], width, height, i, j) for j in range(cols)] for i in range(rows)]

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


def redraw_window(win, board):
    win.fill(white)
    # Draw time
    fnt = pygame.font.SysFont("Arial", 40)
    # Draw grid and board
    board.draw()


if __name__ == "__main__":
    pygame.font.init()
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Board(540, 540, window, sudoku_board)
    board.draw()
    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
        redraw_window(window, board)
        pygame.display.update()
    pygame.quit()
