import random

class TicTacToe:
    def __init__(self):
        self.grid = [['-' for _ in range(3)] for _ in range(3)]  # Grid initialization in one line

    def get_random_first_player(self):
        return random.choice(['X', 'O'])

    def fix_spot(self, row, column, player):
        self.grid[row][column] = player

    def did_player_win(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.grid[i][j] == player for j in range(3)):  # Row check
                return True
            if all(self.grid[j][i] == player for j in range(3)):  # Column check
                return True
        
        # Diagonal checks
        if all(self.grid[i][i] == player for i in range(3)) or \
           all(self.grid[i][2 - i] == player for i in range(3)):
            return True
        
        return False

    def is_grid_filled(self):
        return all(self.grid[i][j] != '-' for i in range(3) for j in range(3))

    def switch_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_grid(self):
        for row in self.grid:
            print(' '.join(row))

    def start(self):
        player = self.get_random_first_player()
        while True:
            self.show_grid()
            print(f'\nPlayer {player} turn')

            # Take user input with the option to exit the game
            try:
                user_input = input('Enter row and column numbers to fix spot (or type "exit" to quit): ')
                if user_input.lower() == 'exit':
                    print('Exiting the game.')
                    break  # Exit the game loop
                
                row, column = map(int, user_input.split())
                row, column = row - 1, column - 1  # Adjust for 0-indexed grid

                if self.grid[row][column] != '-':
                    print('This spot is already taken! Try again.')
                    continue

                self.fix_spot(row, column, player)

                if self.did_player_win(player):
                    self.show_grid()
                    print(f'Player {player} wins!')
                    break

                if self.is_grid_filled():
                    self.show_grid()
                    print('It\'s a draw!')
                    break

                player = self.switch_player_turn(player)

            except ValueError:
                print('Invalid input! Please enter two numbers separated by a space.')
            except IndexError:
                print('Invalid row or column. Please enter numbers between 1 and 3.')

if __name__ == '__main__':
    game = TicTacToe()
    game.start()
