import pygame
import sys
from simulation import Simulation

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
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)


#Simulation Loop
while True:
    # 1. Event Handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        pos = pygame.mouse.get_pos()
        row = pos[1] // CELL_SIZE
        column = pos[0] // CELL_SIZE
        simulation.add_particles(row, column)
    # 2. Update State
    simulation.update()
    
    # 3. Drawing
    window.fill(WINDOW_COLOR)
    simulation.draw(window)

    pygame.display.flip()
    clock.tick(MAX_FRAMERATE)