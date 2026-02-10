import pygame
from simulation import Simulation

#Simulation Defenition
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MAX_FRAMERATE = 120
CELL_SIZE = 6
WINDOW_COLOR = (29, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)


#Simulation Loop
while True:

    # 1. Event Handling
    simulation.handle_controls()

    # 2. Update State
    simulation.update()

    # 3. Drawing
    window.fill(WINDOW_COLOR)
    simulation.draw(window)

    pygame.display.flip()
    clock.tick(MAX_FRAMERATE)