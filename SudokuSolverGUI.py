import pygame
from SudokuSolver import *
import time


class Board(object):

    def __init__(self, width, height, win, rows=9, cols=9):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.window = win
        self.square_selected = None

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


if __name__ == "__main__":
    pygame.font.init()
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Board(540, 540, window)
    board.draw()
    pygame.time.delay(10000)
    pygame.quit()
