import pygame
import sys

#Simulation Defenition
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MAX_FRAMERATE = 120

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()

#Simulation Loop
while True:

    # 1. Event Handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Update State

    # 3. Drawing

    pygame.display.flip()
    clock.tick(MAX_FRAMERATE)