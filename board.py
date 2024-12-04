from ship import Ship

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.ships = []

    def place_ship(self, ship, row, col, orientation):
            # Row and col are already 0-based from the input parsing, no need to adjust
            if not self.is_valid_placement(ship, row, col, orientation):
                return False

            if orientation == 'h':  # Horizontal placement
                start_col = col - (ship.size // 2)
                for i in range(ship.size):
                    self.grid[row][start_col + i] = ship
            elif orientation == 'v':  # Vertical placement
                start_row = row - (ship.size // 2)
                for i in range(ship.size):
                    self.grid[start_row + i][col] = ship

            self.ships.append(ship)
            return True

                    

    def is_valid_placement(self, ship, row, col, orientation):
        if orientation == 'h':  # Check horizontal placement
            start_col = col - (ship.size // 2)
            end_col = start_col + ship.size - 1

            # Check bounds
            if start_col < 0 or end_col >= self.width:
                return False

            # Check for overlap
            for i in range(start_col, end_col + 1):
                if self.grid[row][i] != ' ':
                    return False

        elif orientation == 'v':  # Check vertical placement
            start_row = row - (ship.size // 2)
            end_row = start_row + ship.size - 1

            # Check bounds
            if start_row < 0 or end_row >= self.height:
                return False

            # Check for overlap
            for i in range(start_row, end_row + 1):
                if self.grid[i][col] != ' ':
                    return False

        return True

    def attack(self, row, col):
        if self.grid[row][col] != ' ' and isinstance(self.grid[row][col], Ship):
            ship = self.grid[row][col]
            #if ship.hit():  # Ship has been hit, check if it is sunk
            ship.hit()
            self.grid[row][col] = 'X'  # Mark the hit on the board
            return True
        else:
            self.grid[row][col] = 'O'  # Mark the miss
            return False


    def is_game_over(self):
        """Returns True if all ships are sunk."""
        return all(ship.is_sunk() for ship in self.ships)


    def print_board(self, reveal_ships=False):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print(' ', ' '.join(str(i) for i in range(self.width)))

        for i, row in enumerate(self.grid):
            print(letters[i], end=' ')
            for cell in row:
                if reveal_ships and isinstance(cell, Ship):
                    print('S', end=' ')  # Show ships as 'S' during placement phase
                elif isinstance(cell, Ship):  # During gameplay, don't show ships
                    print(' ', end=' ')
                elif cell == 'O':
                    print('O', end=' ')  # Mark miss
                elif cell == 'X':
                    print('X', end=' ')  # Mark hit
                else:
                    print(' ', end=' ')  # Empty space
            print()


