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

    def get_random_first_player(self):
        return random.randit(0, 1)
    
    def fix_spot(self, row, column, player):
        self.grid[row][column] = player

    def did_player_win(self, player):
        no = len(self.grid)
        board_value = set()

        