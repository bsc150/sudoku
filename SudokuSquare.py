import SudokuSolverGUI


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
        fnt = SudokuSolverGUI.pygame.font.SysFont("david", 40)
        grey_fnt = SudokuSolverGUI.pygame.font.SysFont("david", 30)
        # if self.row == 2 and self.col == 2:
        #     print("(22).grey: " + str(self.grey))
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.grey != 0 and self.value == "_":
            text = grey_fnt.render(str(self.grey), 1, SudokuSolverGUI.grey)
            win.blit(text, (x + 5, y + 5))
        elif not (self.value == "_"):
            text = fnt.render(str(self.value), 1, SudokuSolverGUI.num_to_col[self.value])
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            SudokuSolverGUI.pygame.draw.rect(win, SudokuSolverGUI.red, (x, y, gap, gap), 3)

    def set_grey_value(self, value):
        self.grey = value
