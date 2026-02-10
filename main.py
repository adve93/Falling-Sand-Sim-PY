import pygame
import sys
from grid import Grid

#Simulation Defenition
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MAX_FRAMERATE = 120
CELL_SIZE = 20
WINDOW_COLOR = (100, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()
grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#Simulation Loop
while True:
    # 1. Event Handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Update State

    # 3. Drawing
    window.fill(WINDOW_COLOR)
    grid.draw(window)

    pygame.display.flip()
    clock.tick(MAX_FRAMERATE)