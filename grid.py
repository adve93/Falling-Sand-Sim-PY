import pygame

EMPTY_CELL_COLOR = (55,55,55)

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                pygame.draw.rect(window, EMPTY_CELL_COLOR,
                    (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))