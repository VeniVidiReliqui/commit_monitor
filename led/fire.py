"""
Forest fire model cellular automaton. Simulates the growth
of trees in a forest, with sporadic outbreaks of forest fires.

https://en.wikipedia.org/wiki/Forest-fire_model

Based on Rosetta Code Python Forest Fire example.
https://rosettacode.org/wiki/Forest_fire#Python
"""
import model_base
import random
import time


# Initial probability of a grid square having a tree
initial_trees = 0.55

# p = probability of tree growing, f = probability of fire
p = 0.01
f = 0.0005

# Brightness values for a tree, fire, and blank space
tree = [0, 255, 0]
burning = [255, 0, 0]
space = [0, 0, 0]

# Each square's neighbour coordinates
hood = ((-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1))

class LedFire(LedModel):
    def __init__(self, height, width):
        super().__init__(height, width)

    def get_name(self):
        return "Fire"

    def initialize(self):
        """Initialize grid with random values."""
        self.grid = {(x, y): (tree if random.random() <= initial_trees else space) for x in range(self.width) for y in range(self.height)}

    def get_grid(self):
        """Update grid and return grid."""
        new_grid = {}
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[(x, y)] == burning:
                    new_grid[(x, y)] = space
                elif self.grid[(x, y)] == space:
                    new_grid[(x, y)] = tree if random.random() <= p else space
                elif self.grid[(x, y)] == tree:
                    new_grid[(x, y)] = (burning if any(self.grid.get((x + dx, y + dy), space) == burning for dx, dy in hood) or random.random() <= f else tree)
        self.grid = new_grid
        return self.grid
