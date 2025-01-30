import random

# set up class and grid of game
class Tic_Tac_Toe:
    def __init__(self):
        self.grid = []

    def create_grid(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.grid.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)
    
    def fix_spot(self, row, column, player):
        self.grid[row][column] = player

    def did_player_win(self, player):
        no = len(self.grid)
        grid_values = set()

        # Check rows
        for i in range(no):
            for j in range(no):
                grid_values.add(self.grid[i][j])
            
            if grid_values == {player}:
                return True
            else:
                grid_values.clear()

        # Check columns
        for i in range(no):
            for j in range(no):
                grid_values.add(self.grid[j][i])

            if grid_values == {player}:
                return True
            else:
                grid_values.clear()

        # check diagnals
        for i in range(no):
            grid_values.add(self.grid[i][i])
        if grid_values == {player}:
            return True
        else:
            grid_values.clear()

        grid_values.add(self.grid[0][2])
        grid_values.add(self.grid[1][1])
        grid_values.add(self.grid[2][0])
        if grid_values == {player}:
            return True
        else:
            return False
        
    def is_grid_filled(self):
        for row in self.grid:
            for item in row:
                if item == '-':
                    return False
        return True
    
    def switch_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
    
    def show_grid(self):
        for row in self.grid:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_grid()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_grid()
                print(f'\nPlayer {player} trun')

                row, column = list(
                    map(int, input(
                        'Enter row and column numbers to fix spot: ').split()))
                print()

                if column is None:
                    raise ValueError(
                        'not enough values to unpack (expeced 2, got 1)')
                
                self.fix_spot(row -1, column -1, player)

                game_over = self.did_player_win(player)
                if game_over:
                    print(f'Player {player} has Victory!')
                    continue
                
                game_over = self.is_grid_filled()
                if game_over:
                    print('Scratch Game!')
                    continue
                

                player = self.switch_player_turn(player)

            except ValueError as err:
                print(err)
        
        print()
        self.show_grid()

if __name__ == '__main__':
    tic_tac_toe = Tic_Tac_Toe()
    tic_tac_toe.start()