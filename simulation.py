from grid import Grid
from particles import SandParticles

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)

    def draw(self, window):
        self.grid.draw(window)

    def add_particles(self, row, column):
        self.grid.add_particles(row, column, SandParticles)
    
    def remove_particle(self, row, column):
        self.grid.remove_particle(row, column)