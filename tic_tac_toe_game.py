import random

# set up class and grid of game
class Tic_Tac_Toe:
    def __init__(self):
        self.grid = []

    def create_grid(self):
        for i in range (3):
            row = []
            for j in  range(3):
                row.append('-')
            self.grid.append(row)

    