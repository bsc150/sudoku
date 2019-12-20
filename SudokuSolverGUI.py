import pygame
from SudokuSolver import *
import time


class SudokuSquare(object):
    def __init__(self, value, width, height, row, col):
        self.value = value
        self.temp = 0
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

        if self.temp != 0 and self.value == "_":
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif not (self.value == "_"):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)


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
            pygame.draw.line(self.window, (0, 0, 0), (0, i * gap), (self.width, i * gap), thickness)
            pygame.draw.line(self.window, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thickness)

        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].draw(self.window)


def redraw_window(win, board):
    win.fill((255, 255, 255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
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
        redraw_window(window, board)
        pygame.display.update()
    pygame.quit()
